#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: variant_sets_forest
##
## Purpose of script: One figure per gene of its pooled (IVW over cohorts)
##     carrier-burden estimates per variant set (`--sets`, default all of
##     `Burden.VARIANT_SETS`), each set its own
##     `meta_analysis.py` run ``<label>_<set>``: left the binary outcomes
##     (OR), right the lipids (beta, native UKB units), per outcome one
##     row per variant set, 95% CI, with side tables (OR or beta (95% CI),
##     p-value, UKB carriers / cases, lipids carriers / N). Marker colour
##     shows the variant set, marker shape significance: circle
##     p >= 0.05, square p < 0.05, diamond below the Bonferroni threshold
##     0.05 / (outcomes x variant sets with an estimate, per panel). Run
##     locally in the `plot-misc` env on burden files copied from Snellius
##     into `results/output/`. Writes
##     `results/figures/forest_variant_sets_<label>_<gene>.pdf` (main
##     analysis, `FigureNames.MAIN_FIGURES`) or
##     `results/figures/sensitivity/`. `--lipids-left` swaps the panels;
##     `--combined` writes one multi-page PDF instead, one gene per page:
##     `forest_variant_sets_<label>_<sets>_by_gene.pdf`.
##
## Author: M. van Vugt
## Date created: 09/10/2026
## Last updated: 10/11/2026
##
## Copyright (c) M. van Vugt, 2026
## Email: m.vanvugt1@amsterdamumc.nl
##
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Imports
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import sys
import logging
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import figure_utils as futils
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
from project_constants import (
        Const,
        FigureColumns as FCols,
        FigureNames as FigNames,
        FigureStyle as FStyle,
        HarmonisedColumns,
        MetaColumns,
        MetaLevel,
        Paths,
        VariantListColumns,
        )

logging.basicConfig(level = logging.INFO,
                    format = '[%(levelname)s] %(message)s')
logger = logging.getLogger('variant_sets_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Forests per gene of the pooled carrier-burden '
        'estimates per variant set: binary outcomes and lipids.')
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the runs (default: %(default)s)')
parser.add_argument('-l', '--label',
                    type = str,
                    default = 'cohort_burden_eur',
                    help = 'meta_analysis.py --label without the variant-set '
                    'suffix (default: %(default)s)')
parser.add_argument('-s', '--sets',
                    nargs = '+',
                    choices = list(FigNames.VARIANT_SETS),
                    default = list(FigNames.VARIANT_SETS),
                    help = 'variant sets, one row each (default: all)')
parser.add_argument('-g', '--genes',
                    nargs = '+',
                    default = None,
                    help = 'genes, one figure each (default: all with an '
                    'estimate)')
parser.add_argument('-o', '--out-dir',
                    type = Path,
                    default = Paths.FIGURES,
                    help = 'output directory (default: %(default)s)')
parser.add_argument('-m', '--max-or',
                    type = float,
                    default = FStyle.MAX_OR,
                    help = 'odds-ratio axis limit (default: %(default)s)')
parser.add_argument('--lipids-left',
                    action = 'store_true',
                    help = 'put the lipid panel left of the binary outcomes '
                    '(default: binary outcomes left)')
parser.add_argument('--combined',
                    action = 'store_true',
                    help = 'write all genes into one multi-page PDF, one '
                    'gene per page: forest_variant_sets_<label>_<sets>_'
                    'by_gene.pdf (default: one PDF per gene)')

args = parser.parse_args()
if args.max_or <= 1:
    parser.error('--max-or must be > 1')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENE = VariantListColumns.OUT_GENE
OUTCOME = HarmonisedColumns.OUTCOME
# helper columns: variant set key and the readable outcome (y tick label)
VARIANT_SET = 'variant_set'
OUTCOME_LABEL = 'outcome_label'
# side tables: column, header, alignment; the variant sets are shown by
# colour
TABLES = (
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center'),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center'),
    (FCols.CARRIER_TEXT, FigNames.CARRIERS_HEADER, 'center'),
)
LIPID_TABLES = (
    (FCols.BETA_TEXT, FigNames.BETA_HEADER, 'center'),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center'),
    (FCols.CARRIER_TEXT, FigNames.CARRIERS_N_HEADER, 'center'),
)
# space for the outcome names left of each forest (cm)
LABEL_CM = 1.7


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_sets(ancestry: str, label: str, sets: list[str]) -> pd.DataFrame:
    """Read the pooled burden rows of every variant-set run.

    Parameters
    ----------
    ancestry : `str`
        Ancestry code of the runs.
    label : `str`
        Run label without the variant-set suffix; each run is
        ``<label>_<set>``.
    sets : `list[str]`
        Variant sets (`Burden.VARIANT_SETS` keys).

    Returns
    -------
    pooled : `pd.DataFrame`
        The `MetaLevel.POOLED` rows (binary outcomes and lipids, from
        `figure_utils.load_burden`), with `VARIANT_SET`. Sets without a
        burden file are left out (logged).
    """
    frames = []
    for variant_set in sets:
        burden = futils.load_burden(
                futils.burden_path(ancestry, f'{label}_{variant_set}'),
                keep_lipids = True)
        if burden is None:
            continue
        rows = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
        rows[VARIANT_SET] = variant_set
        frames.append(rows)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def panel_rows(data: pd.DataFrame, outcome_rank: dict[str, int],
               outcome_names: dict[str, str]) -> tuple[pd.DataFrame, float,
                                                       int]:
    """Rows of one panel in plotting order, with marker and colour.

    Parameters
    ----------
    data : `pd.DataFrame`
        Pooled rows of one gene and one kind of outcome (binary or
        lipids), with `VARIANT_SET`.
    outcome_rank : `dict[str, int]`
        Outcome key -> plotting order; others last.
    outcome_names : `dict[str, str]`
        Outcome key -> y tick label; others `figure_utils.outcome_name`.

    Returns
    -------
    rows : `pd.DataFrame`
        Sorted by outcome order, then `FigureNames.VARIANT_SET_RANK`, with
        `OUTCOME_LABEL` and the `FigureColumns` `ORDER`, `MARKER`, `COLOUR`,
        `SIZE` and `Y`.
    strict : `float`
        Bonferroni threshold of the panel.
    n_tests : `int`
        Rows with a finite p-value.
    """
    strict, n_tests = futils.strict_threshold(data)
    rows = data.copy()
    rows[FCols.ORDER] = rows[OUTCOME].map(outcome_rank).fillna(
            len(outcome_rank))
    rows['_set_order'] = rows[VARIANT_SET].map(FigNames.VARIANT_SET_RANK)
    rows = rows.sort_values([FCols.ORDER, OUTCOME, '_set_order'])
    rows = rows.drop(columns = '_set_order').reset_index(drop = True)
    rows[OUTCOME_LABEL] = [
        outcome_names.get(outcome, futils.outcome_name(outcome))
        for outcome in rows[OUTCOME]
    ]
    rows[FCols.MARKER] = futils.significance_marker(rows[MetaColumns.P],
                                                    strict)
    rows[FCols.COLOUR] = rows[VARIANT_SET].map(FStyle.VARIANT_SET_COLOURS)
    rows[FCols.SIZE] = FStyle.MARKER_SIZE
    return futils.set_y(rows, OUTCOME_LABEL), strict, n_tests


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_legend(data: pd.DataFrame) -> list:
    """Colour legend handles of the panel's variant sets, in plotting order.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows from `panel_rows`.

    Returns
    -------
    handles : `list[Line2D]`
        From `figure_utils.colour_legend`, named with
        `FigureNames.VARIANT_SETS`.
    """
    present = set(data[VARIANT_SET])
    return futils.colour_legend({
        name: FStyle.VARIANT_SET_COLOURS[variant_set]
        for variant_set, name in FigNames.VARIANT_SETS.items()
        if variant_set in present
    })


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_panels(pooled: pd.DataFrame, gene: str) -> list[tuple]:
    """The binary-outcome and lipid panels of one gene.

    Parameters
    ----------
    pooled : `pd.DataFrame`
        All pooled rows, with `VARIANT_SET` and the carrier text.
    gene : `str`
        Variant-list gene.

    Returns
    -------
    panels : `list[tuple]`
        Per panel (binary outcomes first, then lipids, each left out when
        empty): rows from `panel_rows`, side tables, title, log x,
        Bonferroni threshold and number of tests. Odds ratios outside
        `--max-or` are dropped after the Bonferroni count, as in
        pooled_forest.py.
    """
    rows = pooled.loc[pooled[GENE] == gene]
    is_lipid = rows[OUTCOME].isin(Const.LIPID_OUTCOMES)
    binary = rows.loc[~is_lipid]
    lipids = futils.add_beta_ci(rows.loc[is_lipid])
    panels = []
    if binary.empty:
        logger.info(f'{gene}: no binary-outcome rows, no OR panel')
    else:
        title = f'{gene}'
        bin_df, strict, n_tests = panel_rows(binary, FigNames.OUTCOME_RANK,
                                             FigNames.OUTCOMES)
        bin_df = futils.limit_or(bin_df, 1 / args.max_or, args.max_or,
                                 title)
        if bin_df.empty:
            logger.info(f'{gene}: no OR within the axis limits')
        else:
            bin_df = futils.set_y(bin_df, OUTCOME_LABEL)
            panels.append((bin_df, TABLES, title, True, strict, n_tests))
    if lipids.empty:
        logger.info(f'{gene}: no lipid rows, no lipid panel')
    else:
        lipid_df, strict, n_tests = panel_rows(
                lipids, FigNames.LIPID_RANK, FigNames.LIPIDS)
        panels.append((lipid_df, LIPID_TABLES,
                       f'{gene}', False, strict,
                       n_tests))
    if args.lipids_left:
        panels.reverse()
    return panels


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def combined_stem(out_dir: Path, label: str, sets: list[str]) -> Path:
    """Output path (no suffix) of the one multi-page PDF of `--combined`.

    Parameters
    ----------
    out_dir : `Path`
        Figure `--out-dir`.
    label : `str`
        Run label without the variant-set suffix.
    sets : `list[str]`
        Variant sets plotted.

    Returns
    -------
    stem : `Path`
        ``forest_variant_sets_<label>_<sets>_by_gene``, in `out_dir` for
        a main-analysis figure (`figure_utils.is_main_figure`), else in
        its `Paths.FIGURES_SENSITIVITY` subfolder, as `figure_utils.save`.
    """
    stem = out_dir / f'forest_variant_sets_{label}_{"_".join(sets)}_by_gene'
    if not futils.is_main_figure(stem.name):
        stem = stem.parent / Paths.FIGURES_SENSITIVITY / stem.name
    return stem


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pooled = load_sets(args.ancestry, args.label, args.sets)
if pooled.empty:
    sys.exit(f'no pooled rows in any {args.ancestry} {args.label}_<set> run')
logger.info('pooled rows per variant set: ' + ', '.join(
    f'{variant_set} {n}'
    for variant_set, n in pooled[VARIANT_SET].value_counts().items()))
# UKB carriers / cases: a pooled row of these single-cohort runs names
# its one study in `studies`
pooled = futils.add_carrier_text(pooled, MetaColumns.STUDIES, VARIANT_SET)
genes = args.genes or sorted(pooled[GENE].unique())


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# per gene one figure: the panels side by side, y limits shared so rows
# are equally spaced; two legend rows (variant sets, significance).
# `--combined`: every figure a page of one PDF, written to a temporary
# file and moved into place once all pages are in (as `figure_utils.save`)
pdf = None
if args.combined:
    combined_path = combined_stem(args.out_dir, args.label, args.sets
                                  ).with_suffix('.pdf')
    combined_path.parent.mkdir(parents = True, exist_ok = True)
    combined_tmp = combined_path.with_name(f'{combined_path.name}.tmp')
    pdf = PdfPages(combined_tmp)
for gene in genes:
    panels = gene_panels(pooled, gene)
    if not panels:
        logger.warning(f'{gene}: nothing to plot')
        continue
    ylim = futils.table_ylim(pd.concat(
        [panel[0][FCols.Y] for panel in panels]))
    fig, cells, height_cm = futils.table_grid(
            len(panels), len(panels), [column for column, _, _ in TABLES],
            ylim, n_legend_rows = 2, label_cm = LABEL_CM)
    for i, (cell, (data, tables, title, log_x, strict, n_tests)) in enumerate(
            zip(cells, panels)):
        ax = futils.draw_table_forest(
                fig, cell, data, title, ylim, log_x, OUTCOME_LABEL, tables,
                futils.group_bands(data, OUTCOME_LABEL))
        # legends: the variant-set colours once, above each panel's
        # significance shapes (own Bonferroni threshold)
        if i == 0:
            sets = pd.concat([panel[0] for panel in panels])
            futils.add_legend(fig, ax, set_legend(sets),
                              FigNames.VARIANT_SET_TITLE,
                              y = FStyle.LEGEND_ROW_CM / height_cm)
        futils.add_legend(fig, ax,
                          futils.significance_legend(strict, n_tests),
                          FigNames.SIGNIFICANCE_TITLE)
    if pdf is None:
        futils.save(fig,
                    args.out_dir / f'forest_variant_sets_{args.label}_{gene}')
    else:
        pdf.savefig(fig, dpi = futils.DPI, bbox_inches = 'tight')
        plt.close(fig)
        logger.info(f'{gene}: page added')
if pdf is not None:
    n_pages = pdf.get_pagecount()
    pdf.close()
    if n_pages == 0:
        os.remove(combined_tmp)
        sys.exit('nothing plotted, no combined PDF written')
    os.replace(combined_tmp, combined_path)
    logger.info(f'wrote {combined_path} ({n_pages} pages)')
