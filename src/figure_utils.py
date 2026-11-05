#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: figure_utils
##
## Purpose of script: Shared helpers of the figure scripts
##     (cohort_burden_forest.py, variant_sets_forest.py,
##     sources_forest.py, ascvd_dementia_scatter.py,
##     cetp_cohort_variants_forest.py, pooled_forest.py,
##     burden_apoe_forest.py, apoe_genotype_forest.py):
##     reading burden files, odds ratios (binary outcomes) and betas
##     (lipids) with 95% CI, p-value formatting, UKB carrier counts,
##     readable names, significance markers, axis limits, grids of
##     forests with side tables and saving.
##     Constants shared by the figure scripts are in `project_constants`
##     (`FigureColumns`, `FigureNames`, `FigureStyle`).
##     Only `project_constants` is imported from the pipeline;
##     `functions.py` needs the biomed-api env (Snellius).
##
## Author: M. van Vugt
## Date created: 09/10/2026
## Last updated: 09/10/2026
##
## Copyright (c) M. van Vugt, 2026
## Email: m.vanvugt1@amsterdamumc.nl
##
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Imports
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from __future__ import annotations

import os
import math
import logging
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plot_misc.forest as forest
from collections.abc import Iterable
from functools import lru_cache
from pathlib import Path
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator
from project_constants import (
        Burden,
        Const,
        FigureColumns as FCols,
        FigureNames as FigNames,
        FigureStyle as FStyle,
        FileNames,
        HarmonisedColumns,
        MarvelColumns,
        MetaColumns,
        MetaLevel,
        Paths,
        VariantListColumns,
        )

LOGGER = logging.getLogger('figure_utils')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Z_95 = 1.959963984540054
UKB_PREFIX = 'marvel_ukb_'
FINNGEN_NAME = 'FinnGen R13'
# x-axis tick candidates (odds ratio), coarse first
TICKS_COARSE = (0.05, 0.1, 0.25, 0.5, 1, 2, 4, 10, 20)
TICKS_FINE = (0.5, 0.75, 1, 1.5, 2)
TICKS_FINER = (0.8, 0.9, 1, 1.1, 1.2)
# x-axis padding factor around the point estimates (log scale)
X_PAD = 1.15
# beta axis (lipids): padding as a fraction of the point-estimate range,
# and the number of ticks aimed for
BETA_PAD = 0.15
BETA_N_TICKS = 5
# p-values below this are shown as this (p = 0 is below double precision)
P_MIN = 1e-100
DPI = 300
# side-table column widths (cm), by text column (`table_grid`)
TABLE_CM = {
    FCols.ROW_NAME: 1.2,
    FCols.OR_TEXT: 1.3,
    FCols.BETA_TEXT: 1.3,
    FCols.P_TEXT: 0.8,
    FCols.CARRIER_TEXT: 1.3,
}
# shading of every other row group
BAND_COLOUR = 'lightgrey'


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Number formatting
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _superscriptinate(number: str) -> str:
    """Replace digits, separators and arithmetic symbols by superscripts.

    Copied from `clean_data.utils.formatting` (not installed in the
    plot-misc env).

    Parameters
    ----------
    number : `str`
        A string containing digits and/or arithmetic symbols to convert.

    Returns
    -------
    number : `str`
        A string with superscript numbers and symbols.
    """
    return number.replace('0','⁰').replace('1','¹').replace('2','²').\
        replace('3','³').replace('4','⁴').replace('5','⁵').replace('6','⁶')\
        .replace('7','⁷').replace('8','⁸').replace('9','⁹').replace('-','⁻')\
        .replace('+', '⁺').replace('.','·').replace(',','˒')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sci_notation(number: float, sig_fig: int = 2,
                 max: float = np.float_power(10, -100)) -> str:
    """Return a number in scientific notation with Unicode superscripts.

    Copied from `clean_data.utils.formatting` (not installed in the
    plot-misc env). Values below `max` are winsorised to `max`.

    Parameters
    ----------
    number : `float`
        A number as float or integer.
    sig_fig : `int`, optional, default: `2`
        The number of decimals of the mantissa.
    max : `float`, optional, default: `10⁻¹⁰⁰`
        Values strictly below this threshold are replaced by `max`.

    Returns
    -------
    number : `str`
        The number formatted in scientific notation, e.g. ``'2.47×10⁶'``;
        ``'nan'`` when it cannot be formatted.

    Examples
    --------
    >>> sci_notation(2465640, sig_fig=4)
    '2.4656×10⁶'
    """
    if number < max:
        number = max
    # getting string
    ret_string = '{0:.{1:d}e}'.format(number, sig_fig)
    try:
        a, b = ret_string.split('e')
        # removed leading "+" and strips leading zeros too.
        b = int(b)
        return a + '×10' + _superscriptinate(str(b))
    except (ValueError, TypeError):
        return str(np.nan)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def format_p(p: float) -> str:
    """Format a p-value for a side table.

    Parameters
    ----------
    p : `float`
        P-value, may be NaN.

    Returns
    -------
    text : `str`
        `sci_notation` with two decimals, e.g. ``'3.00×10⁻⁵'``; p = 0 (or
        below `P_MIN`) as ``'1.00×10⁻¹⁰⁰'``; empty for NaN.
    """
    if not np.isfinite(p):
        return ''
    return sci_notation(p, sig_fig = 2, max = P_MIN)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_or(data: pd.DataFrame) -> pd.DataFrame:
    """Add the odds ratio, its 95% CI and the side-table texts.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows with a finite numeric `MetaColumns.BETA` and `SE`, and a
        numeric `MetaColumns.P`.

    Returns
    -------
    data : `pd.DataFrame`
        Copy with `FigureColumns` `OR`, `LB`, `UB`, `OR_TEXT` (two
        decimals) and `P_TEXT` (`format_p`).
    """
    data = data.copy()
    beta, se = data[MetaColumns.BETA], data[MetaColumns.SE]
    data[FCols.OR] = np.exp(beta)
    data[FCols.LB] = np.exp(beta - Z_95 * se)
    data[FCols.UB] = np.exp(beta + Z_95 * se)
    # text before any axis clipping, so the tables show the real CI
    data[FCols.OR_TEXT] = [
        f'{point:.2f} ({low:.2f}; {high:.2f})'
        for point, low, high in zip(data[FCols.OR], data[FCols.LB],
                                    data[FCols.UB])
    ]
    data[FCols.P_TEXT] = data[MetaColumns.P].map(format_p)
    return data


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_beta_ci(data: pd.DataFrame) -> pd.DataFrame:
    """Add the beta's 95% CI and the side-table texts (lipid outcomes).

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows with a finite numeric `MetaColumns.BETA` and `SE`, and a
        numeric `MetaColumns.P`.

    Returns
    -------
    data : `pd.DataFrame`
        Copy with `FigureColumns` `BETA_LB`, `BETA_UB`, `BETA_TEXT` (two
        decimals) and `P_TEXT` (`format_p`).
    """
    data = data.copy()
    beta, se = data[MetaColumns.BETA], data[MetaColumns.SE]
    data[FCols.BETA_LB] = beta - Z_95 * se
    data[FCols.BETA_UB] = beta + Z_95 * se
    data[FCols.BETA_TEXT] = [
        f'{point:.2f} ({low:.2f}; {high:.2f})'
        for point, low, high in zip(beta, data[FCols.BETA_LB],
                                    data[FCols.BETA_UB])
    ]
    data[FCols.P_TEXT] = data[MetaColumns.P].map(format_p)
    return data


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Reading
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def burden_path(ancestry: str, label: str, extra: str = '') -> Path:
    """Path of a `meta_analysis.py` burden file.

    Parameters
    ----------
    ancestry : `str`
        `Ancestry` code of the run.
    label : `str`
        The run's `--label`.
    extra : `str`, optional, default: `''`
        Further suffix, e.g. ``'_apoe_strata'``.

    Returns
    -------
    path : `Path`
        In `Paths.OUTPUT`.
    """
    return Paths.OUTPUT / FileNames.BURDEN_TEMPLATE.format(
        ancestry = ancestry, suffix = f'_{label}{extra}'
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ordered_genes(genes: Iterable[str]) -> list[str]:
    """Genes in plotting order: `FigureNames.FIRST_GENES`, then A-Z.

    Parameters
    ----------
    genes : `Iterable[str]`
        Gene names, duplicates allowed.

    Returns
    -------
    genes : `list[str]`
        Unique genes; those in `FIRST_GENES` first, in that order, the
        others alphabetically.
    """
    unique = set(genes)
    first = [gene for gene in FigNames.FIRST_GENES if gene in unique]
    return first + sorted(unique - set(first))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_sort_key(column: pd.Series) -> pd.Series:
    """`sort_values` key that puts the gene column in `ordered_genes` order.

    Parameters
    ----------
    column : `pd.Series`
        A column being sorted; only `VariantListColumns.OUT_GENE` is
        changed.

    Returns
    -------
    key : `pd.Series`
        The gene's rank in `ordered_genes`, or `column` unchanged.

    Examples
    --------
    >>> data.sort_values([GENE, FCols.ORDER], key = gene_sort_key)
    """
    if column.name != VariantListColumns.OUT_GENE:
        return column
    rank = {gene: i for i, gene in enumerate(ordered_genes(column))}
    return column.map(rank)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_burden(path: Path, keep_lipids: bool = False
                ) -> pd.DataFrame | None:
    """Read a burden file and add the odds ratio with its 95% CI.

    Parameters
    ----------
    path : `Path`
        A `meta_analysis.py` burden file.
    keep_lipids : `bool`, optional, default: `False`
        Keep the `Const.LIPID_OUTCOMES` rows (linear effects, their
        `add_or` columns are meaningless); by default they are dropped
        (logged), so the result holds binary outcomes only.

    Returns
    -------
    burden : `pd.DataFrame` or `None`
        Rows of genes not in `Const.EXCLUDED_GENES` with a finite beta
        and SE (in the therapeutic direction, as `meta_analysis.py`
        writes them), plus the `add_or` columns; `None` (logged) when the
        file does not exist.

    Raises
    ------
    ValueError
        If the file has no `MetaColumns.THERAPY_DIRECTION` column (written
        before effects were put in the therapeutic direction).
    """
    if not path.exists():
        LOGGER.info(f'{path} not found, skipped')
        return None
    burden = pd.read_csv(path, sep = '\t', low_memory = False)
    if MetaColumns.THERAPY_DIRECTION not in burden.columns:
        raise ValueError(
            f'{path}: no {MetaColumns.THERAPY_DIRECTION} column, so its '
            'effects are in the old lower-function direction; re-run '
            'meta_analysis.py')
    is_excluded = burden[VariantListColumns.OUT_GENE].isin(
        Const.EXCLUDED_GENES)
    if is_excluded.any():
        LOGGER.info(
            f'{path.name}: {int(is_excluded.sum())} rows of excluded '
            f'gene(s) {", ".join(Const.EXCLUDED_GENES)} dropped'
        )
        burden = burden.loc[~is_excluded]
    is_lipid = burden[HarmonisedColumns.OUTCOME].isin(
        Const.LIPID_OUTCOMES)
    if is_lipid.any() and not keep_lipids:
        LOGGER.info(f'{path.name}: {int(is_lipid.sum())} lipid rows '
                    'dropped (not on the OR scale)')
        burden = burden.loc[~is_lipid]
    beta = pd.to_numeric(burden[MetaColumns.BETA], errors = 'coerce')
    se = pd.to_numeric(burden[MetaColumns.SE], errors = 'coerce')
    usable = np.isfinite(beta) & np.isfinite(se)
    if not usable.all():
        LOGGER.info(f'{path.name}: {int((~usable).sum())} rows without '
                    'beta/SE')
    burden = burden.loc[usable].copy()
    burden[MetaColumns.BETA] = beta[usable]
    burden[MetaColumns.SE] = se[usable]
    burden[MetaColumns.P] = pd.to_numeric(burden[MetaColumns.P],
                                          errors = 'coerce')
    burden = add_or(burden)
    LOGGER.info(f'{path.name}: {len(burden)} rows')
    return burden


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Names
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def outcome_name(outcome: str) -> str:
    """Readable outcome name.

    Parameters
    ----------
    outcome : `str`
        `outcome` value of a result row.

    Returns
    -------
    name : `str`
        From `FigureNames.OUTCOMES`, else underscores replaced by spaces.
    """
    return FigNames.OUTCOMES.get(outcome, outcome.replace('_', ' '))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def study_names() -> dict[str, str]:
    """Readable names of the APOE-stratum studies and FinnGen phenocodes.

    Returns
    -------
    names : `dict[str, str]`
        Accession -> name: ``'Thomassen ε4/ε4'`` from
        `FileNames.APOE_STRATA`, `FINNGEN_NAME` for every phenocode in
        `FileNames.FINNGEN_MANIFEST`. UKB accessions are not listed
        (`UKB_PREFIX`).
    """
    names: dict[str, str] = {}
    if FileNames.FINNGEN_MANIFEST.exists():
        manifest = pd.read_csv(FileNames.FINNGEN_MANIFEST, sep = '\t',
                               usecols = ['phenocode'])
        names.update(dict.fromkeys(manifest['phenocode'], FINNGEN_NAME))
    if FileNames.APOE_STRATA.exists():
        strata = pd.read_csv(FileNames.APOE_STRATA, sep = '\t')
        for _, row in strata.iterrows():
            stratum = FigNames.STRATA.get(row[MetaColumns.APOE_STRATUM],
                                        row[MetaColumns.APOE_STRATUM])
            names[row[HarmonisedColumns.STUDY_ACCESSION]] = (
                f'{str(row[MetaColumns.STUDY_GROUP]).capitalize()} {stratum}'
            )
    return names


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def study_name(accession: str, names: dict[str, str]) -> str:
    """Readable name of one study.

    Parameters
    ----------
    accession : `str`
        Study accession of a burden row.
    names : `dict[str, str]`
        From `study_names` or `source_names`.

    Returns
    -------
    name : `str`
        `FigureNames.UKB` for marvel UKB accessions, else the `names`
        entry, else the accession itself.
    """
    if accession.startswith(UKB_PREFIX):
        return FigNames.UKB
    return names.get(accession, accession)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def source_names() -> dict[str, str]:
    """Readable source (study group) name per accession.

    Returns
    -------
    names : `dict[str, str]`
        Accession -> name: the capitalised `study_group` of
        `FileNames.APOE_STRATA` (e.g. all Thomassen strata ->
        ``'Thomassen'``), `FINNGEN_NAME` for every FinnGen phenocode. UKB
        accessions are named in `study_name`.
    """
    names = {
        accession: name
        for accession, name in study_names().items()
        if name == FINNGEN_NAME
    }
    if FileNames.APOE_STRATA.exists():
        strata = pd.read_csv(FileNames.APOE_STRATA, sep = '\t')
        names.update(zip(
            strata[HarmonisedColumns.STUDY_ACCESSION],
            strata[MetaColumns.STUDY_GROUP].astype(str).str.capitalize(),
        ))
    return names


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def source_rows(per_study: pd.DataFrame) -> pd.DataFrame:
    """One estimate per gene, outcome and source.

    A source with several studies (the Thomassen APOE strata) is the
    fixed-effect IVW of their estimates, the same pooling as
    `meta_analysis.py`; a source with one study keeps that study's row.

    Parameters
    ----------
    per_study : `pd.DataFrame`
        Burden rows of level ``stratum`` (one per gene, outcome and
        study), from `load_burden`.

    Returns
    -------
    sources : `pd.DataFrame`
        Gene, outcome, `FigureColumns.ROW_NAME` (source name), beta, SE,
        p, the `add_or` columns, and, from the source's first study,
        `STUDY_ACCESSION` and `MetaColumns.VARIANTS` (for
        `add_carrier_text`).
    """
    gene = VariantListColumns.OUT_GENE
    outcome = HarmonisedColumns.OUTCOME
    study = HarmonisedColumns.STUDY_ACCESSION
    names = source_names()
    rows = per_study.copy()
    rows[FCols.ROW_NAME] = [
        study_name(str(accession), names) for accession in rows[study]
    ]
    rows['_weight'] = 1.0 / rows[MetaColumns.SE] ** 2
    rows['_weighted'] = rows['_weight'] * rows[MetaColumns.BETA]
    keys = [gene, outcome, FCols.ROW_NAME]
    grouped = rows.groupby(keys, sort = False)
    sums = grouped[['_weight', '_weighted']].sum()
    sums = sums.join(grouped[[study, MetaColumns.VARIANTS]].first())
    sums = sums.reset_index()
    sums[MetaColumns.BETA] = sums['_weighted'] / sums['_weight']
    sums[MetaColumns.SE] = 1.0 / np.sqrt(sums['_weight'])
    z = (sums[MetaColumns.BETA] / sums[MetaColumns.SE]).abs()
    sums[MetaColumns.P] = [math.erfc(value / math.sqrt(2)) for value in z]
    return add_or(sums.drop(columns = ['_weight', '_weighted']))


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Carrier counts
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@lru_cache(maxsize = 1)
def _ukb_counts() -> dict[tuple[str, str], tuple[float, float, float]]:
    """UKB carriers, cases and samples per study and burden exposure.

    Returns
    -------
    counts : `dict[tuple[str, str], tuple[float, float, float]]`
        (study accession, marvel `Exposure`) -> (exposed, cases, samples)
        from `FileNames.MATCHED_BURDEN`; empty (logged) when the file does
        not exist. Read once.
    """
    path = FileNames.MATCHED_BURDEN
    if not path.exists():
        LOGGER.info(f'{path} not found: no carrier counts')
        return {}
    prefix = HarmonisedColumns.RAW_PREFIX
    exposure, exposed, cases, samples = (
        f'{prefix}{column}' for column in (
            MarvelColumns.EXPOSURE, MarvelColumns.EXPOSED,
            MarvelColumns.CASES, MarvelColumns.SAMPLES)
    )
    study = HarmonisedColumns.STUDY_ACCESSION
    table = pd.read_csv(path, sep = '\t', low_memory = False,
                        usecols = [study, exposure, exposed, cases, samples])
    numbers = table[[exposed, cases, samples]].apply(pd.to_numeric,
                                                     errors = 'coerce')
    return {
        (str(accession), str(name)): tuple(values)
        for accession, name, values in zip(table[study], table[exposure],
                                           numbers.to_numpy())
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@lru_cache(maxsize = 1)
def _exposure_sites() -> dict[str, str]:
    """Sites per burden exposure (burden_exposure.py summary).

    Returns
    -------
    sites : `dict[str, str]`
        Exposure (``<GENE>_<mask>``) -> its sites joined by ``;``; empty
        (logged) when `FileNames.BURDEN_EXPOSURE_SUMMARY` does not exist.
        Read once.
    """
    path = FileNames.BURDEN_EXPOSURE_SUMMARY
    if not path.exists():
        LOGGER.info(f'{path} not found: fallback masks not recognised')
        return {}
    summary = pd.read_csv(path, sep = '\t', dtype = str)
    return dict(zip(summary['exposure'], summary['sites'].fillna('')))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def burden_exposure(gene: str, variant_set: str, variants: object) -> str:
    """The marvel exposure behind a UKB carrier-burden row.

    Parameters
    ----------
    gene : `str`
        Variant-list gene.
    variant_set : `str`
        Variant set (`Burden.VARIANT_SETS` key, the mask).
    variants : `object`
        The row's `MetaColumns.VARIANTS` (sites joined by ``;``), may be
        NA.

    Returns
    -------
    exposure : `str`
        ``<gene>_<set>_fb`` when `variants` are the sites of that fallback
        mask and not of the base mask (`meta_analysis.ukb_burden_rows`
        picked it), else ``<gene>_<set>``.
    """
    base = f'{gene}_{variant_set}'
    fallback = f'{base}{Burden.FALLBACK_SUFFIX}'
    sites = _exposure_sites()
    if (isinstance(variants, str) and sites.get(fallback) == variants
            and sites.get(base) != variants):
        return fallback
    return base


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_carrier_text(data: pd.DataFrame, study_col: str,
                     set_col: str) -> pd.DataFrame:
    """Add the UKB carriers / cases (lipids: carriers / N) side-table text.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows with `OUT_GENE`, `OUTCOME`, `study_col`, `set_col` and
        optionally `MetaColumns.VARIANTS`.
    study_col : `str`
        Column with the row's one study accession (e.g. `MetaColumns.STUDIES`
        of a single-study pooled row, or `STUDY_ACCESSION`).
    set_col : `str`
        Column with the row's variant set.

    Returns
    -------
    data : `pd.DataFrame`
        Copy with `FigureColumns.CARRIER_TEXT`, e.g. ``'833 / 67,249'``:
        the carriers and all cases (binary outcomes) or all samples with a
        measurement (lipids) of the UKB analysis, from
        `FileNames.MATCHED_BURDEN`. Empty for rows of other studies,
        several studies, or without counts.
    """
    counts = _ukb_counts()
    variants = (data[MetaColumns.VARIANTS] if MetaColumns.VARIANTS in data
                else pd.Series(pd.NA, index = data.index))
    texts = []
    for gene, outcome, study, variant_set, sites in zip(
            data[VariantListColumns.OUT_GENE],
            data[HarmonisedColumns.OUTCOME], data[study_col].astype(str),
            data[set_col], variants):
        key = (study, burden_exposure(gene, variant_set, sites))
        if not study.startswith(UKB_PREFIX) or key not in counts:
            texts.append('')
            continue
        exposed, cases, samples = counts[key]
        total = samples if outcome in Const.LIPID_OUTCOMES else cases
        if np.isfinite(exposed) and np.isfinite(total):
            texts.append(f'{exposed:,.0f} / {total:,.0f}')
        else:
            texts.append('')
    data = data.copy()
    data[FCols.CARRIER_TEXT] = texts
    return data


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Significance
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def strict_threshold(burden: pd.DataFrame) -> tuple[float, int]:
    """Bonferroni threshold over the pooled gene x outcome estimates.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`, the run's main burden file.

    Returns
    -------
    threshold : `float`
        `FigureStyle.P_NOMINAL` / number of tests.
    n_tests : `int`
        Pooled rows with a finite p-value (one per gene and outcome).
    """
    pooled = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED]
    n_tests = int(np.isfinite(pooled[MetaColumns.P]).sum())
    return FStyle.P_NOMINAL / max(n_tests, 1), n_tests


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def significance_marker(p: pd.Series, strict: float) -> np.ndarray:
    """Marker shape per row from its p-value.

    Parameters
    ----------
    p : `pd.Series`
        P-values.
    strict : `float`
        Bonferroni threshold.

    Returns
    -------
    markers : `np.ndarray`
        `FigureStyle.MARKER_STRICT`, `MARKER_NOMINAL` or `MARKER_NS`.
    """
    return np.select([p < strict, p < FStyle.P_NOMINAL],
                     [FStyle.MARKER_STRICT, FStyle.MARKER_NOMINAL],
                     default = FStyle.MARKER_NS)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def significance_legend(strict: float, n_tests: int) -> list[Line2D]:
    """Legend handles of the three marker shapes.

    Parameters
    ----------
    strict : `float`
        Bonferroni threshold.
    n_tests : `int`
        Number of tests behind `strict`.

    Returns
    -------
    handles : `list[Line2D]`
    """
    labels = (
        (FStyle.MARKER_NS, f'p ≥ {FStyle.P_NOMINAL:g}'),
        (FStyle.MARKER_NOMINAL, f'p < {FStyle.P_NOMINAL:g}'),
        (FStyle.MARKER_STRICT,
         f'p < {sci_notation(strict, sig_fig = 1)} (Bonferroni, '
         f'{n_tests} tests)'),
    )
    return [
        Line2D([0], [0], marker = marker, color = FStyle.POOLED_COLOUR,
               markeredgecolor = 'black', markeredgewidth = .3,
               markersize = 2.5, lw = 0, label = label)
        for marker, label in labels
    ]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_legend(fig: plt.Figure, ax: plt.Axes, handles: list[Line2D],
               title: str, y: float = 0.0) -> None:
    """Add a titled legend below the forest.

    Parameters
    ----------
    fig : `plt.Figure`
        Figure of the forest.
    ax : `plt.Axes`
        Forest axis; the legend's left edge is aligned with it.
    handles : `list[Line2D]`
        E.g. from `significance_legend` or `colour_legend`.
    title : `str`
        Legend title, shown bold above the entries.
    y : `float`, optional, default: `0.0`
        Bottom of the legend as a figure fraction.

    Returns
    -------
    `None`
    """
    kwargs = {**FStyle.LEGEND_KWARGS, 'ncol': len(handles)}
    fig.legend(handles = handles, title = title,
               bbox_to_anchor = (ax.get_position().x0, y), **kwargs)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def colour_legend(colours: dict[str, str]) -> list[Line2D]:
    """Legend handles of coloured circles.

    Parameters
    ----------
    colours : `dict[str, str]`
        Label -> colour, in legend order.

    Returns
    -------
    handles : `list[Line2D]`
    """
    return [
        Line2D([0], [0], marker = FStyle.MARKER_NS, color = colour,
               markeredgecolor = 'black', markeredgewidth = .3,
               markersize = 2.5, lw = 0, label = label)
        for label, colour in colours.items()
    ]


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Axis and rows
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def limit_or(data: pd.DataFrame, min_or: float, max_or: float,
             label: str) -> tuple[pd.DataFrame, int]:
    """Drop estimates outside ``[min_or, max_or]`` and clip the CIs to it.

    Parameters
    ----------
    data : `pd.DataFrame`
        With `FigureColumns.OR`, `FigureColumns.LB` and `FigureColumns.UB`.
    min_or : `float`
        Smallest odds ratio shown.
    max_or : `float`
        Largest odds ratio shown.
    label : `str`
        Figure name for the warning on dropped estimates.

    Returns
    -------
    data : `pd.DataFrame`
        Copy without the estimates outside the range, CIs clipped, index
        reset.
    """
    points_out = (data[FCols.OR] < min_or) | (data[FCols.OR] > max_or)
    if points_out.any():
        LOGGER.warning(f'{label}: {int(points_out.sum())} estimates outside '
                       f'[{min_or:g}, {max_or:g}] not shown')
    data = data.loc[~points_out].copy()
    data[FCols.LB] = data[FCols.LB].clip(lower = min_or)
    data[FCols.UB] = data[FCols.UB].clip(upper = max_or)
    return data.reset_index(drop = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_y(data: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Y coordinates: rows 2 apart within a group, 4 between groups.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows sorted in plotting order, unique index.
    group_col : `str`
        Column of the groups (y tick labels).

    Returns
    -------
    data : `pd.DataFrame`
        Copy with `FigureColumns.Y`.
    """
    y = pd.Series(np.nan, index = data.index)
    position = 1.0
    for group in dict.fromkeys(data[group_col]):
        rows = data.index[data[group_col] == group]
        y[rows] = position + 2 * np.arange(len(rows))
        position = y[rows].max() + 4
    data = data.copy()
    data[FCols.Y] = y
    return data


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def x_axis(data: pd.DataFrame, low: float | None = None
           ) -> tuple[tuple[float, float], list[float]]:
    """Log x limits and ticks that fit the point estimates.

    Confidence intervals do not widen the axis; the parts outside the
    limits are cut off at the axis edge.

    Parameters
    ----------
    data : `pd.DataFrame`
        With `FigureColumns.OR`.
    low : `float` or `None`, optional, default: `None`
        Fixed lower limit; `None` derives it from the point estimates.

    Returns
    -------
    limits : `tuple[float, float]`
        The lowest and highest point estimate (always around 1), padded
        by `X_PAD` and widened to the next tick outside; `low`, when
        given, is used as is.
    ticks : `list[float]`
        Within the limits, from the first of `TICKS_COARSE`,
        `TICKS_FINE`, `TICKS_FINER` with at least three ticks within the
        padded range (else `TICKS_FINER`).
    """
    pad_low = min(float(data[FCols.OR].min()), 1.0) / X_PAD
    pad_high = max(float(data[FCols.OR].max()), 1.0) * X_PAD
    if low is not None:
        pad_low = low
    for candidates in (TICKS_COARSE, TICKS_FINE, TICKS_FINER):
        if sum(pad_low <= t <= pad_high for t in candidates) >= 3:
            break
    # widen to the nearest tick outside the padded range, if any
    below = [t for t in candidates if t <= pad_low]
    above = [t for t in candidates if t >= pad_high]
    if low is None:
        low = max(below) if below else pad_low
    high = min(above) if above else pad_high
    ticks = [t for t in candidates if low <= t <= high]
    return (low, high), ticks


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def beta_axis(data: pd.DataFrame) -> tuple[tuple[float, float], list[float]]:
    """Linear x limits and ticks that fit the beta point estimates.

    As in `x_axis`, confidence intervals do not widen the axis.

    Parameters
    ----------
    data : `pd.DataFrame`
        With `MetaColumns.BETA`.

    Returns
    -------
    limits : `tuple[float, float]`
        The lowest and highest point estimate (always around 0), padded
        by `BETA_PAD` of their range.
    ticks : `list[float]`
        About `BETA_N_TICKS` round ticks within the limits, 0 included.
    """
    low = min(float(data[MetaColumns.BETA].min()), 0.0)
    high = max(float(data[MetaColumns.BETA].max()), 0.0)
    pad = (high - low) * BETA_PAD or 0.1
    low, high = low - pad, high + pad
    locator = MaxNLocator(nbins = BETA_N_TICKS, steps = [1, 2, 2.5, 5, 10])
    ticks = [float(t) for t in locator.tick_values(low, high)
             if low <= t <= high]
    return (low, high), ticks


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forests with side tables
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def table_ylim(y: pd.Series | list[float]) -> tuple[float, float]:
    """Y limits of a table forest: little space above the first row.

    Parameters
    ----------
    y : `pd.Series` or `list[float]`
        Y coordinates of all rows (`set_y` spacing).

    Returns
    -------
    ylim : `tuple[float, float]`
        The first row minus `FigureStyle.TABLE_Y_PAD_TOP`, the last plus
        `TABLE_Y_PAD_BOTTOM`; the forest draws the first row at the top.
    """
    return (float(min(y)) - FStyle.TABLE_Y_PAD_TOP,
            float(max(y)) + FStyle.TABLE_Y_PAD_BOTTOM)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def group_bands(data: pd.DataFrame, group_col: str
                ) -> list[tuple[float, float]]:
    """Y ranges of every other row group, to shade grey.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows with `FigureColumns.Y` (`set_y` spacing) and `group_col`.
    group_col : `str`
        Column of the groups.

    Returns
    -------
    bands : `list[tuple[float, float]]`
        The 2nd, 4th, ... group from the top, from 2 above its first to 2
        below its last row.
    """
    spans = (data.groupby(group_col, sort = False)[FCols.Y]
             .agg(['min', 'max']).sort_values('min'))
    return [(low - 2, high + 2) for low, high in spans.to_numpy()[1::2]]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def table_grid(n_panels: int, n_cols: int, columns: list[str],
               ylim: tuple[float, float], n_legend_rows: int = 1,
               label_cm: float = FStyle.TABLE_LABEL_CM,
               ) -> tuple[plt.Figure, list[list[gridspec.SubplotSpec]],
                          float]:
    """Figure with a grid of panels, each a forest and its side tables.

    Parameters
    ----------
    n_panels : `int`
        Number of panels, filled row by row.
    n_cols : `int`
        Panels per row.
    columns : `list[str]`
        Side-table text columns of each panel (`TABLE_CM` keys).
    ylim : `tuple[float, float]`
        Y limits shared by the panels (sets the panel height).
    n_legend_rows : `int`, optional, default: `1`
        Titled legends below the grid.
    label_cm : `float`, optional, default: `FigureStyle.TABLE_LABEL_CM`
        Space for the y tick labels left of each forest (cm).

    Returns
    -------
    fig : `plt.Figure`
    cells : `list[list[gridspec.SubplotSpec]]`
        Per panel the forest cell, then one per side table.
    height_cm : `float`
        Figure height, to place the legends.
    """
    n_rows = math.ceil(n_panels / n_cols)
    panel_cm = FStyle.CM_PER_Y * (ylim[1] - ylim[0])
    panel_widths = [label_cm, FStyle.TABLE_FOREST_CM,
                    *(TABLE_CM[column] for column in columns)]
    widths = panel_widths * n_cols
    heights = [panel_cm]
    for _ in range(n_rows - 1):
        heights += [FStyle.TABLE_ROW_GAP_CM, panel_cm]
    bottom_cm = (FStyle.FOREST_BOTTOM_CM
                 + FStyle.LEGEND_ROW_CM * (n_legend_rows - 1))
    height_cm = FStyle.FOREST_TOP_CM + sum(heights) + bottom_cm
    matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
    fig = plt.figure(figsize = (sum(widths) * FStyle.CM,
                                height_cm * FStyle.CM))
    gs = gridspec.GridSpec(nrows = len(heights), ncols = len(widths),
                           width_ratios = widths, height_ratios = heights,
                           figure = fig, wspace = 0.0, hspace = 0.0,
                           left = 0.0, right = 1.0,
                           bottom = bottom_cm / height_cm,
                           top = 1 - FStyle.FOREST_TOP_CM / height_cm)
    cells = []
    for i in range(n_panels):
        row, col = divmod(i, n_cols)
        # skip the tick-label column
        start = col * len(panel_widths) + 1
        cells.append([gs[2 * row, j]
                      for j in range(start, start + len(panel_widths) - 1)])
    return fig, cells, height_cm


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_table(ax: plt.Axes, data: pd.DataFrame, column: str, header: str,
               align: str, ylim: tuple[float, float],
               bands: list[tuple[float, float]]) -> None:
    """Write one side-table column next to a forest.

    Parameters
    ----------
    ax : `plt.Axes`
        Empty axis right of the forest.
    data : `pd.DataFrame`
        The forest's rows, with `FigureColumns.Y` and `column`.
    column : `str`
        Text column.
    header : `str`
        Bold header above the column.
    align : `str`
        ``'left'`` or ``'center'``.
    ylim : `tuple[float, float]`
        The forest axis's y limits (as returned by its `get_ylim`, so the
        orientation matches).
    bands : `list[tuple[float, float]]`
        Y ranges shaded grey, as in the forest.

    Returns
    -------
    `None`
    """
    ax.set_ylim(ylim)
    ax.set_xlim(0, 1)
    ax.axis('off')
    for low, high in bands:
        ax.axhspan(low, high, color = BAND_COLOUR, zorder = 0, lw = 0)
    x = 0.05 if align == 'left' else 0.5
    for y, text in zip(data[FCols.Y], data[column]):
        ax.text(x, y, '' if pd.isna(text) else str(text), ha = align,
                va = 'center', fontsize = FStyle.STEXT_SIZE)
    ax.text(x, 1.0, header, transform = ax.transAxes, ha = align,
            va = 'bottom', fontsize = FStyle.STEXT_SIZE,
            fontweight = 'bold')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_table_forest(fig: plt.Figure, cells: list[gridspec.SubplotSpec],
                      data: pd.DataFrame, title: str,
                      ylim: tuple[float, float], log_x: bool, tick_col: str,
                      tables: tuple[tuple[str, str, str], ...],
                      bands: list[tuple[float, float]],
                      italic: bool = False) -> plt.Axes:
    """Draw one forest with its side tables.

    Parameters
    ----------
    fig : `plt.Figure`
        The figure.
    cells : `list[gridspec.SubplotSpec]`
        From `table_grid`: the forest, then one per side table.
    data : `pd.DataFrame`
        Rows with `FigureColumns` `Y`, `MARKER`, `COLOUR`, `SIZE`, the CI
        columns and the table columns.
    title : `str`
        Forest title.
    ylim : `tuple[float, float]`
        From `table_ylim`, shared by the panels.
    log_x : `bool`
        Odds ratios on a log axis with reference 1 (`x_axis`); else betas
        on a linear axis with reference 0 (`beta_axis`).
    tick_col : `str`
        Column of the y tick labels (one per group).
    tables : `tuple[tuple[str, str, str], ...]`
        Side tables: column, header, alignment.
    bands : `list[tuple[float, float]]`
        Y ranges shaded grey across the forest and its tables.
    italic : `bool`, optional, default: `False`
        Italic y tick labels (gene names).

    Returns
    -------
    ax : `plt.Axes`
        The forest axis.
    """
    ax = fig.add_subplot(cells[0])
    if log_x:
        ax.set_xscale('log')
        x_col, lb_col, ub_col = FCols.OR, FCols.LB, FCols.UB
    else:
        x_col, lb_col, ub_col = MetaColumns.BETA, FCols.BETA_LB, FCols.BETA_UB
    ax.set_zorder(1)
    bm_forest = forest.ForestPlot(
            data = data, x_col = x_col, y_col = FCols.Y,
            lb_col = lb_col, ub_col = ub_col, g_col = tick_col, ax = ax,
            )
    _, ax = bm_forest.plot(
            s_col = FCols.MARKER, c_col = FCols.COLOUR,
            s_size_col = FCols.SIZE, ci_colour = 'black',
            ci_lwd = FStyle.LWD, span = False, ylim = ylim,
            kwargs_scatter_dict = FStyle.SCATTER_KWARGS,
            kwargs_plot_ci_dict = FStyle.CI_KWARGS,
            )
    # formatting
    for low, high in bands:
        ax.axhspan(low, high, color = BAND_COLOUR, zorder = 0, lw = 0)
    ax.axvline(1 if log_x else 0, linewidth = FStyle.LWD, linestyle = '--',
               c = 'black', zorder = .5)
    ax.spines[['right', 'top']].set_visible(False)
    if log_x:
        x_lim, x_tic = x_axis(data)
        ax.xaxis.set_major_formatter(
                matplotlib.ticker.FormatStrFormatter('%g'))
        ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    else:
        x_lim, x_tic = beta_axis(data)
    ax.set_xlim(x_lim)
    ax.set_xticks(x_tic)
    ax.tick_params(axis = 'both', which = 'minor', bottom = False,
                   labelsize = FStyle.AX_LAB_SZ, width = FStyle.LWD)
    ax.tick_params(axis = 'both', labelsize = FStyle.AX_LAB_SZ,
                   width = FStyle.LWD)
    if italic:
        for label in ax.get_yticklabels():
            label.set_fontstyle('italic')
    ax.set_xlabel(FigNames.OR_LABEL_THERAPY if log_x
                  else FigNames.BETA_LABEL_THERAPY,
                  fontsize = FStyle.LAB_SIZE)
    ax.set_title(title, fontweight = 'bold', fontsize = FStyle.TITLE_SIZE,
                 loc = 'left', pad = 6)
    # side tables
    for cell, (column, header, align) in zip(cells[1:], tables):
        side_ax = fig.add_subplot(cell)
        draw_table(side_ax, data, column, header, align, ax.get_ylim(),
                   bands)
    return ax


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Saving
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_main_figure(name: str) -> bool:
    """Whether a figure belongs to the main analysis.

    Parameters
    ----------
    name : `str`
        File name without suffix.

    Returns
    -------
    is_main : `bool`
        `True` when `name` equals an entry of `FigureNames.MAIN_FIGURES`,
        or starts with an entry ending in ``'_'``.
    """
    for entry in FigNames.MAIN_FIGURES:
        if name == entry or (entry.endswith('_') and name.startswith(entry)):
            return True
    return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save(fig: plt.Figure, stem: Path) -> None:
    """Save a figure as PDF, written then moved into place.

    Main-analysis figures (`is_main_figure`) are written to the directory
    of `stem`, all others to its `Paths.FIGURES_SENSITIVITY` subfolder.

    Parameters
    ----------
    fig : `plt.Figure`
        Figure to save; closed afterwards.
    stem : `Path`
        Output path without suffix, in the figure `--out-dir`.

    Returns
    -------
    `None`
    """
    if not is_main_figure(stem.name):
        stem = stem.parent / Paths.FIGURES_SENSITIVITY / stem.name
    stem.parent.mkdir(parents = True, exist_ok = True)
    path = stem.with_name(f'{stem.name}.pdf')
    tmp = path.with_name(f'{path.name}.tmp')
    fig.savefig(tmp, format = 'pdf', dpi = DPI, bbox_inches = 'tight')
    os.replace(tmp, path)
    plt.close(fig)
    LOGGER.info(f'wrote {path}')
