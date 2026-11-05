#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: selected_variants_forest
##
## Purpose of script: The selected single GoF variants
##     (`data/raw/selected_variants.tsv`, source `SelectedGoF`) one by one,
##     separate from the burden analyses: one figure per variant of the
##     `meta_analysis.py --variant-sources SelectedGoF --stratified
##     --no-gene-burden` run (`--label`, default `selected_gof_eur`), left
##     the binary outcomes of the other figures (`FigureNames.OUTCOMES`,
##     OR), right the lipids (beta, native UKB units), each panel its own
##     y limits,
##     per outcome each study's estimate (UK Biobank, FinnGen, Thomassen
##     strata, GWAS Catalog accessions) and their IVW last, 95% CI, with
##     side tables (study, OR or beta (95% CI), p-value). All effects
##     oriented to lower gene function (flipped as GoF) and then to the
##     therapeutic direction (`TherapyDirection.GENES`; CETP: lower
##     function). Marker shape shows significance: circle p >= 0.05,
##     square p < 0.05, diamond below the Bonferroni threshold 0.05 /
##     (outcomes with a pooled estimate, per panel). Run locally in the
##     `plot-misc` env on the meta file copied from Snellius into
##     `results/output/`. Writes
##     `results/figures/forest_<label>_<chrom>_<pos>_<a1>_<a2>.pdf` (main
##     analysis, `FigureNames.MAIN_FIGURES`: the EUR run) or
##     `results/figures/sensitivity/` (e.g. MULTI). Also one figure with
##     all variants, per outcome each variant's IVW coloured by variant:
##     `forest_<label>_all_variants.pdf`.
##
## Author: M. van Vugt
## Date created: 27/10/2026
## Last updated: 27/10/2026
##
## Copyright (c) M. van Vugt, 2026
## Email: m.vanvugt1@amsterdamumc.nl
##
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Imports
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys
import logging
import argparse
import numpy as np
import pandas as pd
import figure_utils as futils
from pathlib import Path
from project_constants import (
        Const,
        FigureColumns as FCols,
        FigureNames as FigNames,
        FigureStyle as FStyle,
        FileNames,
        HarmonisedColumns,
        MetaColumns,
        MetaLevel,
        Paths,
        VariantListColumns,
        VariantSource,
        )

logging.basicConfig(level = logging.INFO,
                    format = '[%(levelname)s] %(message)s')
logger = logging.getLogger('selected_variants_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Forests per selected GoF variant: each study and '
        'the IVW per outcome, binary outcomes and lipids.')
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the run (default: %(default)s)')
parser.add_argument('-l', '--label',
                    type = str,
                    default = 'selected_gof_eur',
                    help = 'meta_analysis.py --label of the run (default: '
                    '%(default)s)')
parser.add_argument('-o', '--out-dir',
                    type = Path,
                    default = Paths.FIGURES,
                    help = 'output directory (default: %(default)s)')
parser.add_argument('-m', '--max-or',
                    type = float,
                    default = FStyle.MAX_OR,
                    help = 'odds-ratio axis limit (default: %(default)s)')

args = parser.parse_args()
if args.max_or <= 1:
    parser.error('--max-or must be > 1')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENE = VariantListColumns.OUT_GENE
OUTCOME = HarmonisedColumns.OUTCOME
STUDY = HarmonisedColumns.STUDY_ACCESSION
SITE = MetaColumns.VARIANT_SITE
SOURCE = VariantListColumns.OUT_SOURCE
# helper column: the readable outcome (y tick label)
OUTCOME_LABEL = 'outcome_label'
# row order per outcome: UK Biobank, other studies, pooled
UKB_ORDER = 0
STUDY_ORDER = 1
POOLED_ORDER = 2
# side tables: column, header, alignment
TABLES = (
    (FCols.ROW_NAME, FigNames.SOURCE_HEADER, 'left'),
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center'),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center'),
)
LIPID_TABLES = (
    (FCols.ROW_NAME, FigNames.SOURCE_HEADER, 'left'),
    (FCols.BETA_TEXT, FigNames.BETA_HEADER, 'center'),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center'),
)
# space for the outcome names left of each forest (cm)
LABEL_CM = 1.7
# all-variants figure: colour legend title
VARIANT_TITLE = 'Variant'


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def variant_names(path: Path = FileNames.SELECTED_VARIANTS
                  ) -> dict[str, str]:
    """Figure label per selected variant site.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.SELECTED_VARIANTS`
        The hand-made list (`chr`, `pos`, `a1`, `a2`, ..., `name`).

    Returns
    -------
    names : `dict[str, str]`
        ``chrom:pos:a1:a2`` (chrom without ``chr``, as `variant_site`) ->
        name; empty (logged) when the list does not exist.
    """
    if not path.exists():
        logger.info(f'{path} not found: variants labelled by site only')
        return {}
    vc = VariantListColumns
    table = pd.read_csv(path, sep = '\t', dtype = str)
    chrom = table[vc.CHROM].str.removeprefix('chr')
    sites = (chrom + ':' + table[vc.POS] + ':' + table[vc.A1] + ':'
             + table[vc.A2])
    return dict(zip(sites, table[vc.NAME]))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def study_rows(meta: pd.DataFrame) -> pd.DataFrame:
    """Each study's row and the pooled row, with name and order.

    Parameters
    ----------
    meta : `pd.DataFrame`
        Rows of one variant from `figure_utils.load_burden` (lipids kept).

    Returns
    -------
    rows : `pd.DataFrame`
        `meta` with `FigureColumns.ROW_NAME` (study name, or
        `FigureNames.POOLED`) and `FigureColumns.ORDER`.
    """
    names = futils.study_names()
    rows = meta.copy()
    is_pooled = rows[MetaColumns.LEVEL] == MetaLevel.POOLED
    study = rows[STUDY].astype(str)
    is_ukb = study.str.startswith(futils.UKB_PREFIX)
    rows[FCols.ROW_NAME] = np.where(
            is_pooled, FigNames.POOLED,
            [futils.study_name(accession, names) for accession in study])
    rows[FCols.ORDER] = np.select([is_pooled, is_ukb],
                                  [POOLED_ORDER, UKB_ORDER],
                                  default = STUDY_ORDER)
    return rows


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def panel_rows(data: pd.DataFrame, outcome_rank: dict[str, int],
               outcome_names: dict[str, str]) -> tuple[pd.DataFrame, float,
                                                       int]:
    """Rows of one panel in plotting order, with marker, colour and size.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows from `study_rows` of one variant and one kind of outcome
        (binary or lipids).
    outcome_rank : `dict[str, int]`
        Outcome key -> plotting order; others last, alphabetically.
    outcome_names : `dict[str, str]`
        Outcome key -> y tick label; others `figure_utils.outcome_name`.

    Returns
    -------
    rows : `pd.DataFrame`
        Per outcome the studies (UK Biobank first) and the pooled row
        last, with `OUTCOME_LABEL` and the `FigureColumns` `MARKER`,
        `COLOUR` and `SIZE`.
    strict : `float`
        Bonferroni threshold of the panel (its pooled rows).
    n_tests : `int`
        Pooled rows with a finite p-value.
    """
    strict, n_tests = futils.strict_threshold(data)
    rows = data.copy()
    rows['_outcome_order'] = rows[OUTCOME].map(outcome_rank).fillna(
            len(outcome_rank))
    rows = rows.sort_values(['_outcome_order', OUTCOME, FCols.ORDER,
                             FCols.ROW_NAME, STUDY], kind = 'stable')
    rows = rows.drop(columns = '_outcome_order').reset_index(drop = True)
    rows[OUTCOME_LABEL] = [
        outcome_names.get(outcome, futils.outcome_name(str(outcome)))
        for outcome in rows[OUTCOME]
    ]
    is_pooled = rows[FCols.ORDER] == POOLED_ORDER
    rows[FCols.MARKER] = futils.significance_marker(rows[MetaColumns.P],
                                                    strict)
    rows[FCols.COLOUR] = np.where(is_pooled, FStyle.POOLED_COLOUR,
                                  FStyle.STUDY_COLOUR)
    rows[FCols.SIZE] = np.where(is_pooled, FStyle.POOLED_SIZE,
                                FStyle.STUDY_SIZE)
    return rows, strict, n_tests


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def variant_colours(sites: list[str]) -> dict[str, str]:
    """Marker colour per variant site, for the all-variants figure.

    Parameters
    ----------
    sites : `list[str]`
        Variant sites, sorted.

    Returns
    -------
    colours : `dict[str, str]`
        Site -> colour from `FigureStyle.SELECTED_VARIANT_COLOURS`, in
        order (reused when there are more sites than colours, logged).
    """
    palette = FStyle.SELECTED_VARIANT_COLOURS
    if len(sites) > len(palette):
        logger.warning(f'{len(sites)} variants but {len(palette)} colours: '
                       'colours reused')
    return {site: palette[i % len(palette)] for i, site in enumerate(sites)}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def all_variant_rows(meta: pd.DataFrame, names: dict[str, str],
                     colours: dict[str, str]) -> pd.DataFrame:
    """The pooled (IVW) row of every variant and outcome, named by variant.

    Parameters
    ----------
    meta : `pd.DataFrame`
        All selected-variant rows (lipids kept).
    names : `dict[str, str]`
        Site -> variant label, from `variant_names`.
    colours : `dict[str, str]`
        Site -> marker colour, from `variant_colours`.

    Returns
    -------
    rows : `pd.DataFrame`
        The `MetaLevel.POOLED` rows with `FigureColumns.ROW_NAME` (gene
        and variant label), `ORDER` (variant-site order) and `COLOUR`.
    """
    rows = meta.loc[meta[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
    site_rank = {site: i for i, site in enumerate(colours)}
    rows[FCols.ROW_NAME] = [names.get(site, site) for site in rows[SITE]]
    rows[FCols.ORDER] = rows[SITE].map(site_rank)
    rows[FCols.COLOUR] = rows[SITE].map(colours)
    return rows


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def all_variant_panel_rows(data: pd.DataFrame, outcome_rank: dict[str, int],
                           outcome_names: dict[str, str]
                           ) -> tuple[pd.DataFrame, float, int]:
    """Rows of one all-variants panel in plotting order, with marker.

    As `panel_rows`, but the rows are the variants' pooled estimates,
    coloured by variant (`all_variant_rows`) instead of by pooled/study.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows from `all_variant_rows` of one kind of outcome.
    outcome_rank : `dict[str, int]`
        Outcome key -> plotting order; others last, alphabetically.
    outcome_names : `dict[str, str]`
        Outcome key -> y tick label; others `figure_utils.outcome_name`.

    Returns
    -------
    rows : `pd.DataFrame`
        Per outcome the variants in site order, with `OUTCOME_LABEL` and
        the `FigureColumns` `MARKER` and `SIZE`.
    strict : `float`
        Bonferroni threshold of the panel (variants x outcomes).
    n_tests : `int`
        Rows with a finite p-value.
    """
    strict, n_tests = futils.strict_threshold(data)
    rows = data.copy()
    rows['_outcome_order'] = rows[OUTCOME].map(outcome_rank).fillna(
            len(outcome_rank))
    rows = rows.sort_values(['_outcome_order', OUTCOME, FCols.ORDER],
                            kind = 'stable')
    rows = rows.drop(columns = '_outcome_order').reset_index(drop = True)
    rows[OUTCOME_LABEL] = [
        outcome_names.get(outcome, futils.outcome_name(str(outcome)))
        for outcome in rows[OUTCOME]
    ]
    rows[FCols.MARKER] = futils.significance_marker(rows[MetaColumns.P],
                                                    strict)
    rows[FCols.SIZE] = FStyle.MARKER_SIZE
    return rows, strict, n_tests


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_figure(panels: list[tuple], stem: str,
                colour_handles: list | None = None) -> None:
    """Draw the panels side by side, each with its own y limits, and save.

    The figure height is set by the longest panel, so a short panel fills
    the height instead of leaving empty space.

    Parameters
    ----------
    panels : `list[tuple]`
        From `variant_panels`.
    stem : `str`
        Output file name without extension, in `--out-dir`.
    colour_handles : `list` or `NoneType`, optional, default: `None`
        Colour legend handles, drawn once above the first panel's
        significance legend; `None` for none.

    Returns
    -------
    `None`
    """
    n_legend_rows = 1 if colour_handles is None else 2
    ylims = [futils.table_ylim(panel[0][FCols.Y]) for panel in panels]
    fig, cells, height_cm = futils.table_grid(
            len(panels), len(panels), [column for column, _, _ in TABLES],
            max(ylims, key = lambda ylim: ylim[1] - ylim[0]),
            n_legend_rows = n_legend_rows, label_cm = LABEL_CM)
    for i, (cell, ylim, (data, tables, panel_title, log_x, strict,
                         n_tests)) in enumerate(zip(cells, ylims, panels)):
        ax = futils.draw_table_forest(
                fig, cell, data, panel_title, ylim, log_x, OUTCOME_LABEL,
                tables, futils.group_bands(data, OUTCOME_LABEL))
        if i == 0 and colour_handles is not None:
            futils.add_legend(fig, ax, colour_handles, VARIANT_TITLE,
                              y = FStyle.LEGEND_ROW_CM / height_cm)
        futils.add_legend(fig, ax,
                          futils.significance_legend(strict, n_tests),
                          FigNames.SIGNIFICANCE_TITLE)
    futils.save(fig, args.out_dir / stem)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def variant_panels(rows: pd.DataFrame, title: str,
                   build_rows = panel_rows,
                   row_header: str = FigNames.SOURCE_HEADER) -> list[tuple]:
    """The binary-outcome and lipid panels of one variant.

    Parameters
    ----------
    rows : `pd.DataFrame`
        Rows from `study_rows` of one variant, or from `all_variant_rows`.
    title : `str`
        Variant label, for the panel titles.
    build_rows : `callable`, optional, default: `panel_rows`
        Orders and marks a panel's rows (`panel_rows` or
        `all_variant_panel_rows`).
    row_header : `str`, optional, default: `FigureNames.SOURCE_HEADER`
        Header of the `FigureColumns.ROW_NAME` side-table column.

    Returns
    -------
    panels : `list[tuple]`
        Per panel (binary outcomes first, then lipids, each left out when
        empty): rows with `FigureColumns.Y`, side tables, title, log x,
        Bonferroni threshold and number of tests. Binary outcomes are
        restricted to `FigureNames.OUTCOMES` (as in the other figures)
        before the Bonferroni count; odds ratios outside `--max-or` are
        dropped after it.
    """
    is_lipid = rows[OUTCOME].isin(Const.LIPID_OUTCOMES)
    is_shown = rows[OUTCOME].isin(FigNames.OUTCOMES)
    dropped = sorted(set(rows.loc[~is_lipid & ~is_shown, OUTCOME]))
    if dropped:
        logger.info(f'{title}: binary outcomes not in FigureNames.OUTCOMES '
                    f'dropped: {", ".join(dropped)}')
    binary = rows.loc[~is_lipid & is_shown]
    lipids = futils.add_beta_ci(rows.loc[is_lipid])
    tables, lipid_tables = (
        ((FCols.ROW_NAME, row_header, 'left'), *panel_tables[1:])
        for panel_tables in (TABLES, LIPID_TABLES))
    panels = []
    if binary.empty:
        logger.info(f'{title}: no binary-outcome rows, no OR panel')
    else:
        bin_title = f'{title}: binary outcomes'
        bin_df, strict, n_tests = build_rows(
                binary, FigNames.OUTCOME_RANK, FigNames.OUTCOMES)
        bin_df = futils.limit_or(bin_df, 1 / args.max_or, args.max_or,
                                 bin_title)
        if bin_df.empty:
            logger.info(f'{title}: no OR within the axis limits')
        else:
            panels.append((futils.set_y(bin_df, OUTCOME_LABEL), tables,
                           bin_title, True, strict, n_tests))
    if lipids.empty:
        logger.info(f'{title}: no lipid rows, no lipid panel')
    else:
        lipid_df, strict, n_tests = build_rows(
                lipids, FigNames.LIPID_RANK, FigNames.LIPIDS)
        panels.append((futils.set_y(lipid_df, OUTCOME_LABEL), lipid_tables,
                       f'{title}: lipids', False, strict, n_tests))
    return panels


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

path = Paths.OUTPUT / FileNames.META_ANALYSIS_TEMPLATE.format(
        ancestry = args.ancestry, suffix = f'_{args.label}')
meta = futils.load_burden(path, keep_lipids = True)
if meta is None:
    sys.exit(f'{path} not found')
is_selected = meta[SOURCE] == VariantSource.SELECTED_GOF
if not is_selected.all():
    logger.info(f'{path.name}: {int((~is_selected).sum())} rows of other '
                'variant-list sources dropped')
meta = meta.loc[is_selected]
if meta.empty:
    sys.exit(f'{path.name}: no {VariantSource.SELECTED_GOF} '
             'rows')
names = variant_names()


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# per variant one figure: each study and the IVW per outcome; one legend
# row (significance, per panel)
for site, variant in meta.groupby(SITE, sort = True):
    gene = ', '.join(sorted(set(variant[GENE].astype(str))))
    title = f'{gene} {names.get(site, site)}'
    panels = variant_panels(study_rows(variant), title)
    if not panels:
        logger.warning(f'{title}: nothing to plot')
        continue
    logger.info(f'{title}: ' + ', '.join(
        f'{panel[2]} {len(panel[0])} rows' for panel in panels))
    draw_figure(panels, f'forest_{args.label}_{site.replace(":", "_")}')

# all variants in one figure: per outcome each variant's IVW, coloured by
# variant; two legend rows (variants once, significance per panel)
colours = variant_colours(sorted(meta[SITE].unique()))
gene = ', '.join(sorted(set(meta[GENE].astype(str))))
title = f'{gene} selected GoF variants'
panels = variant_panels(all_variant_rows(meta, names, colours), title,
                        build_rows = all_variant_panel_rows,
                        row_header = VARIANT_TITLE)
if panels:
    logger.info(f'{title}: ' + ', '.join(
        f'{panel[2]} {len(panel[0])} rows' for panel in panels))
    draw_figure(panels, f'forest_{args.label}_all_variants',
                futils.colour_legend({names.get(site, site): colour
                                      for site, colour in colours.items()}))
else:
    logger.warning(f'{title}: nothing to plot')
