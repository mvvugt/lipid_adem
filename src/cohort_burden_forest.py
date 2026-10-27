#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: cohort_burden_forest
##
## Purpose of script: One figure of the pooled (IVW over cohorts) carrier-
##     burden estimates of the `cohort_burden_<anc>_<set>` runs of
##     `meta_analysis.py`: one forest per outcome in a grid (`--n-cols`),
##     per gene one row per variant set (`--sets`), 95% CI, with side
##     tables (OR or beta (95% CI), p-value, UKB carriers / cases, lipids
##     carriers / N). `--panel controls`: the lipids (beta, native UKB
##     units) and ASCVD (OR), the positive controls; `--panel dementia`:
##     the dementia outcomes (OR). Marker colour shows the variant set,
##     marker shape significance: circle p >= 0.05, square p < 0.05,
##     diamond below the Bonferroni threshold 0.05 / (genes x outcomes with
##     an estimate); the variant sets are nested (PTV + AM holds PTV and
##     AM), so they do not add tests. Run locally in the `plot-misc` env on
##     burden files copied from Snellius into `results/output/`. Writes
##     `results/figures/forest_<label>_<panel>.pdf` (main analysis,
##     `FigureNames.MAIN_FIGURES`) or `results/figures/sensitivity/`.
##
## Author: M. van Vugt
## Date created: 26/10/2026
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
logger = logging.getLogger('cohort_burden_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Forests of the pooled carrier-burden estimates per '
        'outcome, per gene one row per variant set.')
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
                    choices = list(Constants.BURDEN_VARIANT_SETS),
                    default = ['ptv', 'am', 'ptv_am'],
                    help = 'variant sets, one row each (default: '
                    '%(default)s)')
parser.add_argument('-p', '--panel',
                    choices = ('controls', 'dementia'),
                    required = True,
                    help = 'controls: lipids + ASCVD; dementia: the '
                    'dementia outcomes')
parser.add_argument('-n', '--n-cols',
                    type = int,
                    default = 2,
                    help = 'forests per figure row (default: %(default)s)')
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
if args.n_cols < 1:
    parser.error('--n-cols must be >= 1')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENE = VariantListColumns.OUT_GENE
OUTCOME = HarmonisedColumns.OUTCOME
VARIANT_SET = 'variant_set'
# outcomes per panel, in plotting order (row by row)
PANEL_OUTCOMES = {
    'controls': (*FigNames.LIPIDS, 'ascvd'),
    'dementia': tuple(outcome for outcome in FigNames.OUTCOMES
                      if outcome != 'ascvd'),
}
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
# space for the gene names left of each forest (cm)
LABEL_CM = 0.8


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_sets(ancestry: str, label: str, sets: list[str],
              outcomes: tuple[str, ...]) -> pd.DataFrame:
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
    outcomes : `tuple[str, ...]`
        Outcomes to keep.

    Returns
    -------
    pooled : `pd.DataFrame`
        The `MetaLevel.POOLED` rows of `outcomes` (from
        `figure_utils.load_burden`, lipids kept), with `VARIANT_SET`.
        Sets without a burden file are left out (logged).
    """
    frames = []
    for variant_set in sets:
        burden = futils.load_burden(
                futils.burden_path(ancestry, f'{label}_{variant_set}'),
                keep_lipids = True)
        if burden is None:
            continue
        rows = burden[(burden[MetaColumns.LEVEL] == MetaLevel.POOLED)
                      & burden[OUTCOME].isin(outcomes)].copy()
        rows[VARIANT_SET] = variant_set
        frames.append(rows)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_set_y(genes: list[str], sets: list[str]) -> dict[tuple[str, str],
                                                         float]:
    """Y coordinate per gene and variant set, shared by all forests.

    As `figure_utils.set_y` (rows 2 apart, 4 between genes), with a slot
    for every set in every gene, so a row sits at the same height in each
    forest even where an estimate is missing.

    Parameters
    ----------
    genes : `list[str]`
        Genes in plotting order (top to bottom of the y axis order).
    sets : `list[str]`
        Variant sets in plotting order.

    Returns
    -------
    y : `dict[tuple[str, str], float]`
        (gene, variant set) -> y.
    """
    block = 2 * (len(sets) - 1) + 4
    return {
        (gene, variant_set): 1.0 + i * block + 2 * j
        for i, gene in enumerate(genes)
        for j, variant_set in enumerate(sets)
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_legend(sets: list[str]) -> list:
    """Colour legend handles of the variant sets, in plotting order.

    Parameters
    ----------
    sets : `list[str]`
        Variant sets shown.

    Returns
    -------
    handles : `list[Line2D]`
        From `figure_utils.colour_legend`, named with
        `FigureNames.VARIANT_SETS`.
    """
    return futils.colour_legend({
        FigNames.VARIANT_SETS[variant_set]:
        FStyle.VARIANT_SET_COLOURS[variant_set]
        for variant_set in sets
    })


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

outcomes = PANEL_OUTCOMES[args.panel]
pooled = load_sets(args.ancestry, args.label, args.sets, outcomes)
if pooled.empty:
    sys.exit(f'no pooled rows in any {args.ancestry} {args.label}_<set> run')
sets = [variant_set for variant_set in args.sets
        if variant_set in set(pooled[VARIANT_SET])]
logger.info('pooled rows per variant set: ' + ', '.join(
    f'{variant_set} {n}'
    for variant_set, n in pooled[VARIANT_SET].value_counts().items()))
pooled = futils.add_beta_ci(pooled)
# UKB carriers / cases: a pooled row of these single-cohort runs names
# its one study in `studies`
pooled = futils.add_carrier_text(pooled, MetaColumns.STUDIES, VARIANT_SET)

# one Bonferroni threshold for the figure: the genes x outcomes with an
# estimate, the nested variant sets not counted as extra tests
has_p = np.isfinite(pooled[MetaColumns.P])
n_tests = int(pooled.loc[has_p, [GENE, OUTCOME]].drop_duplicates().shape[0])
strict = FStyle.P_NOMINAL / max(n_tests, 1)
pooled[FCols.MARKER] = futils.significance_marker(pooled[MetaColumns.P],
                                                  strict)
pooled[FCols.COLOUR] = pooled[VARIANT_SET].map(FStyle.VARIANT_SET_COLOURS)
pooled[FCols.SIZE] = FStyle.MARKER_SIZE

# shared y: genes in `futils.ordered_genes` order (CETP first), per gene
# the sets in --sets order
genes = futils.ordered_genes(pooled[GENE])
y_map = gene_set_y(genes, sets)
pooled[FCols.Y] = [y_map[key] for key in zip(pooled[GENE],
                                              pooled[VARIANT_SET])]
pooled = pooled.sort_values(FCols.Y).reset_index(drop = True)
ylim = futils.table_ylim(list(y_map.values()))
# grey bands: the 2nd, 4th, ... gene, from 2 below its first to 2 above
# its last row
bands = [
    (y_map[(gene, sets[0])] - 2, y_map[(gene, sets[-1])] + 2)
    for gene in genes[1::2]
]

# per outcome: odds ratios limited to the axis range
panels = []
for outcome in outcomes:
    rows = pooled.loc[pooled[OUTCOME] == outcome]
    is_lipid = outcome in Constants.LIPID_OUTCOMES
    name = FigNames.LIPIDS.get(outcome, FigNames.OUTCOMES.get(
        outcome, futils.outcome_name(outcome)))
    if not is_lipid:
        rows = futils.limit_or(rows, 1 / args.max_or, args.max_or, name)
    if rows.empty:
        logger.info(f'{name}: no estimates, forest left out')
        continue
    panels.append((rows, name, not is_lipid))
if not panels:
    sys.exit('nothing to plot')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# one figure, the forests in a grid row by row, one extra legend row for
# the variant-set colours
fig, cells, height_cm = futils.table_grid(
        len(panels), min(args.n_cols, len(panels)),
        [column for column, _, _ in TABLES], ylim, n_legend_rows = 2,
        label_cm = LABEL_CM)
axes = [futils.draw_table_forest(fig, cell, rows, name, ylim, log_x, GENE,
                                 TABLES if log_x else LIPID_TABLES, bands,
                                 italic = True)
        for cell, (rows, name, log_x) in zip(cells, panels)]
# add legends below the first forest: variant-set colours above the
# significance shapes
futils.add_legend(fig, axes[0], set_legend(sets), FigNames.VARIANT_SET_TITLE,
                  y = FStyle.LEGEND_ROW_CM / height_cm)
futils.add_legend(fig, axes[0], futils.significance_legend(strict, n_tests),
                  FigNames.SIGNIFICANCE_TITLE)
# save
futils.save(fig, args.out_dir / f'forest_{args.label}_{args.panel}')
