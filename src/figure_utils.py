#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: figure_utils
##
## Purpose of script: Shared helpers of the figure scripts
##     (burden_forest.py, burden_apoe_forest.py, sources_forest.py,
##     pooled_forest.py, burden_heatmap.py, apoe_genotype_forest.py):
##     reading burden files, odds ratios with 95% CI, p-value formatting,
##     readable names, significance markers, axis limits and saving.
##     Constants shared by the figure scripts are in `project_constants`
##     (`FigureColumns`, `FigureNames`, `FigureStyle`).
##     Only `project_constants` is imported from the pipeline;
##     `functions.py` needs the Myriad biomed-api env.
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
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.lines import Line2D
from project_constants import (
        Constants,
        FigureColumns as FCols,
        FigureNames as FigNames,
        FigureStyle as FStyle,
        FileNames,
        HarmonisedColumns,
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
# p-values below this are shown as this (p = 0 is below double precision)
P_MIN = 1e-100
DPI = 300


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
        In `Paths.RESULTS_OUTPUT`.
    """
    return Paths.RESULTS_OUTPUT / FileNames.BURDEN_TEMPLATE.format(
        ancestry = ancestry, suffix = f'_{label}{extra}'
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_burden(path: Path) -> pd.DataFrame | None:
    """Read a burden file and add the odds ratio with its 95% CI.

    Parameters
    ----------
    path : `Path`
        A `meta_analysis.py` burden file.

    Returns
    -------
    burden : `pd.DataFrame` or `None`
        Rows of genes not in `Constants.EXCLUDED_GENES` with a finite beta
        and SE, plus the `add_or` columns; `None` (logged) when the file
        does not exist.
    """
    if not path.exists():
        LOGGER.info(f'{path} not found, skipped')
        return None
    burden = pd.read_csv(path, sep = '\t', low_memory = False)
    is_excluded = burden[VariantListColumns.OUT_GENE].isin(
        Constants.EXCLUDED_GENES)
    if is_excluded.any():
        LOGGER.info(
            f'{path.name}: {int(is_excluded.sum())} rows of excluded '
            f'gene(s) {", ".join(Constants.EXCLUDED_GENES)} dropped'
        )
        burden = burden.loc[~is_excluded]
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
        `FileNames.FINNGEN_MANIFEST`. UKB accessions are named in
        `study_name`.
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
    `meta_analysis.py`.

    Parameters
    ----------
    per_study : `pd.DataFrame`
        Burden rows of level ``stratum`` (one per gene, outcome and
        study), from `load_burden`.

    Returns
    -------
    sources : `pd.DataFrame`
        Gene, outcome, `FigureColumns.ROW_NAME` (source name), beta, SE,
        p and the `add_or` columns.
    """
    gene = VariantListColumns.OUT_GENE
    outcome = HarmonisedColumns.OUTCOME
    names = source_names()
    rows = per_study.copy()
    rows[FCols.ROW_NAME] = [
        study_name(str(accession), names)
        for accession in rows[HarmonisedColumns.STUDY_ACCESSION]
    ]
    rows['_weight'] = 1.0 / rows[MetaColumns.SE] ** 2
    rows['_weighted'] = rows['_weight'] * rows[MetaColumns.BETA]
    sums = (
        rows.groupby([gene, outcome, FCols.ROW_NAME], sort = False)[
            ['_weight', '_weighted']]
        .sum()
        .reset_index()
    )
    sums[MetaColumns.BETA] = sums['_weighted'] / sums['_weight']
    sums[MetaColumns.SE] = 1.0 / np.sqrt(sums['_weight'])
    z = (sums[MetaColumns.BETA] / sums[MetaColumns.SE]).abs()
    sums[MetaColumns.P] = [math.erfc(value / math.sqrt(2)) for value in z]
    return add_or(sums.drop(columns = ['_weight', '_weighted']))


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
