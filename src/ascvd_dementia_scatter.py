#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: ascvd_dementia_scatter
##
## Purpose of script: Scatter of the pooled carrier-burden odds ratios of
##     one `meta_analysis.py` run (`--label`, e.g.
##     `cohort_burden_eur_ptv_am`): x the ASCVD OR, y a dementia OR, one
##     point per gene with its 95% CI in both directions, one panel per
##     dementia outcome (`--outcomes`). Shows whether genes that lower
##     ASCVD (the positive control) also shift dementia risk. Log axes,
##     reference lines at OR 1. PPARA loss of function proxies the
##     opposite of a fibrate (an agonist). Run locally in the `plot-misc`
##     env on burden files copied from Snellius into `results/output/`.
##     Writes `results/figures/scatter_ascvd_dementia_<label>.pdf` (main
##     analysis, `FigureNames.MAIN_FIGURES`) or
##     `results/figures/sensitivity/`.
##
## Author: M. van Vugt
## Date created: 26/10/2026
## Last updated: 26/10/2026
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
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import figure_utils as futils
from pathlib import Path
from project_constants import (
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
logger = logging.getLogger('ascvd_dementia_scatter')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Scatter of the pooled ASCVD vs dementia odds ratios, '
        'one point per gene.')
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the run (default: %(default)s)')
parser.add_argument('-l', '--label',
                    type = str,
                    default = 'cohort_burden_eur_ptv_am',
                    help = 'meta_analysis.py --label of the run (default: '
                    '%(default)s)')
parser.add_argument('-d', '--outcomes',
                    nargs = '+',
                    default = ['alzheimers_dementia', 'all_cause_dementia'],
                    help = 'dementia outcomes, one panel each (default: '
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
X_OUTCOME = 'ascvd'
# x / y column suffixes after the merge
X_SUFFIX = '_x'
Y_SUFFIX = '_y'
# panel size (cm)
PANEL_CM = 5.0
# odds-ratio ticks of both axes, those within the limits are used
TICKS = (0.05, 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2, 4, 10, 20)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def paired_rows(pooled: pd.DataFrame, outcome: str) -> pd.DataFrame:
    """Per gene the ASCVD and one dementia estimate side by side.

    Parameters
    ----------
    pooled : `pd.DataFrame`
        Pooled burden rows with the `figure_utils.add_or` columns.
    outcome : `str`
        Dementia outcome of the y axis.

    Returns
    -------
    pairs : `pd.DataFrame`
        One row per gene with both estimates: `GENE` and the `OR`, `LB`,
        `UB` columns with `X_SUFFIX` (ASCVD) and `Y_SUFFIX` (dementia).
        Genes lacking either are left out (logged).
    """
    columns = [GENE, FCols.OR, FCols.LB, FCols.UB]
    x = pooled.loc[pooled[OUTCOME] == X_OUTCOME, columns]
    y = pooled.loc[pooled[OUTCOME] == outcome, columns]
    pairs = x.merge(y, on = GENE, suffixes = (X_SUFFIX, Y_SUFFIX))
    lacking = sorted(set(x[GENE]) ^ set(y[GENE]))
    if lacking:
        logger.info(f'{outcome}: gene(s) {", ".join(lacking)} lack ASCVD or '
                    'the dementia estimate, left out')
    return pairs.sort_values(GENE).reset_index(drop = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_scatter(ax: plt.Axes, pairs: pd.DataFrame, title: str,
                 limits: tuple[float, float]) -> None:
    """Draw one panel: points with 95% CI bars and gene labels.

    Parameters
    ----------
    ax : `plt.Axes`
        Panel axis.
    pairs : `pd.DataFrame`
        From `paired_rows`.
    title : `str`
        Panel title (the dementia outcome).
    limits : `tuple[float, float]`
        Odds-ratio limits of both axes; CIs are clipped to them.

    Returns
    -------
    `None`
    """
    low, high = limits
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.axvline(1, linewidth = FStyle.LWD, linestyle = '--', c = 'black',
               zorder = .5)
    ax.axhline(1, linewidth = FStyle.LWD, linestyle = '--', c = 'black',
               zorder = .5)
    x = pairs[f'{FCols.OR}{X_SUFFIX}']
    y = pairs[f'{FCols.OR}{Y_SUFFIX}']
    x_err = [x - pairs[f'{FCols.LB}{X_SUFFIX}'].clip(lower = low),
             pairs[f'{FCols.UB}{X_SUFFIX}'].clip(upper = high) - x]
    y_err = [y - pairs[f'{FCols.LB}{Y_SUFFIX}'].clip(lower = low),
             pairs[f'{FCols.UB}{Y_SUFFIX}'].clip(upper = high) - y]
    ax.errorbar(x, y, xerr = x_err, yerr = y_err, fmt = 'none',
                ecolor = FStyle.STUDY_COLOUR, elinewidth = FStyle.LWD,
                zorder = 1)
    ax.scatter(x, y, s = FStyle.MARKER_SIZE, c = FStyle.POOLED_COLOUR,
               zorder = 2, **FStyle.SCATTER_KWARGS)
    for gene, x_point, y_point in zip(pairs[GENE], x, y):
        ax.annotate(gene, (x_point, y_point), xytext = (2, 2),
                    textcoords = 'offset points',
                    fontsize = FStyle.STEXT_SIZE, fontstyle = 'italic')
    # formatting
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ticks = [tick for tick in TICKS if low <= tick <= high]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%g'))
        axis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.spines[['right', 'top']].set_visible(False)
    ax.tick_params(axis = 'both', which = 'minor', left = False,
                   bottom = False)
    ax.tick_params(axis = 'both', labelsize = FStyle.AX_LAB_SZ,
                   width = FStyle.LWD)
    ax.set_xlabel(f'{FigNames.OUTCOMES[X_OUTCOME]}, odds ratio (95% CI), '
                  f'{FigNames.THERAPY_SUFFIX}', fontsize = FStyle.LAB_SIZE)
    ax.set_ylabel(f'{title}, odds ratio (95% CI), {FigNames.THERAPY_SUFFIX}',
                  fontsize = FStyle.LAB_SIZE)
    ax.set_title(title, fontweight = 'bold', fontsize = FStyle.TITLE_SIZE,
                 loc = 'left', pad = 6)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

burden = futils.load_burden(futils.burden_path(args.ancestry, args.label))
if burden is None:
    sys.exit(f'no burden file for {args.ancestry} {args.label}')
pooled = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED]
panels = []
for outcome in args.outcomes:
    pairs = paired_rows(pooled, outcome)
    if pairs.empty:
        logger.info(f'{outcome}: no gene with both estimates, panel left out')
        continue
    panels.append((pairs, FigNames.OUTCOMES.get(
        outcome, futils.outcome_name(outcome))))
if not panels:
    sys.exit('nothing to plot')

# shared limits: the points (not the CIs), padded, within --max-or
points = pd.concat([pairs[[f'{FCols.OR}{X_SUFFIX}', f'{FCols.OR}{Y_SUFFIX}']]
                    for pairs, _ in panels]).stack()
low = max(min(float(points.min()), 1.0) / 2, 1 / args.max_or)
high = min(max(float(points.max()), 1.0) * 2, args.max_or)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Scatter plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
fig, axes = plt.subplots(
        nrows = 1, ncols = len(panels), squeeze = False,
        figsize = (PANEL_CM * len(panels) * FStyle.CM, PANEL_CM * FStyle.CM),
        )
for ax, (pairs, title) in zip(axes[0], panels):
    draw_scatter(ax, pairs, title, (low, high))
fig.tight_layout()
# save
futils.save(fig, args.out_dir / f'scatter_ascvd_dementia_{args.label}')
