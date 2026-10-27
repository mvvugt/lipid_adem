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
##     `Constants.BURDEN_VARIANT_SETS`), each set its own
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
##     `results/figures/sensitivity/`.
##
## Author: M. van Vugt
## Date created: 09/10/2026
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
import pandas as pd
import figure_utils as futils
from pathlib import Path
from project_constants import (
        Constants,
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
                    default = Paths.RESULTS_FIGURES,
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
        Variant sets (`Constants.BURDEN_VARIANT_SETS` keys).

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
    is_lipid = rows[OUTCOME].isin(Constants.LIPID_OUTCOMES)
    binary = rows.loc[~is_lipid]
    lipids = futils.add_beta_ci(rows.loc[is_lipid])
    panels = []
    if binary.empty:
        logger.info(f'{gene}: no binary-outcome rows, no OR panel')
    else:
        title = f'{gene} carrier burden per variant set'
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
                       f'{gene} lipids per variant set', False, strict,
                       n_tests))
    return panels


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
# are equally spaced; two legend rows (variant sets, significance)
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
    futils.save(fig, args.out_dir / f'forest_variant_sets_{args.label}_{gene}')
