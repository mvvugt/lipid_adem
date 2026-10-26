#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: burden_apoe_forest
##
## Purpose of script: Forest plot per outcome of the gene-burden
##     meta-analysis by APOE genotype: per gene the pooled odds ratio over
##     all APOE genotypes (the run's burden file) and per APOE stratum
##     (its `_apoe_strata` burden file), 95% CI, with side tables (APOE,
##     OR (95% CI), p-value). Marker shape shows significance: circle
##     p >= 0.05, square p < 0.05, diamond below the Bonferroni threshold
##     0.05 / (genes x outcomes with a pooled estimate in the main run).
##     Run locally in the `plot-misc` env on burden files copied from
##     Snellius into `results/output/`. Writes
##     `results/figures/sensitivity/forest_apoe_<label>_<outcome>.pdf`.
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

import sys
import logging
import argparse
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plot_misc.forest as forest
import figure_utils as futils
from pathlib import Path
from project_constants import (
        ApoeStratum,
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
logger = logging.getLogger('burden_apoe_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = ('Forest plot per outcome of a gene-burden run, '
                       'overall and per APOE stratum.'))
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the run (default: %(default)s)')
parser.add_argument('-l', '--label',
                    type = str,
                    required = True,
                    help = 'meta_analysis.py --label of the run')
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
STRATUM = MetaColumns.APOE_STRATUM
OUTCOME = HarmonisedColumns.OUTCOME
STRATUM_RANK = {name: i for i, name in enumerate(FigNames.STRATUM_ORDER)}
# side tables: column, header, alignment, x location
TABLES = (
    (FCols.ROW_NAME, 'APOE', 'left', 0.05),
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center', 0.5),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center', 0.5),
)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

burden = futils.load_burden(futils.burden_path(args.ancestry, args.label))
strata = futils.load_burden(futils.burden_path(
        args.ancestry, args.label, f'_{Constants.APOE_STRATA_LABEL}'))
if burden is None:
    sys.exit(f'no burden file for {args.ancestry} {args.label}')
if strata is None:
    # not every run is APOE-stratified
    logger.info(f'no APOE strata file for {args.ancestry} {args.label}, '
                'nothing to plot')
    sys.exit(0)

# significance markers and legend, from the main run
strict, n_tests = futils.strict_threshold(burden)
leg_handles = futils.significance_legend(strict, n_tests)

# pooled estimates: all genotypes and per stratum
overall = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
overall[STRATUM] = ApoeStratum.ALL
per_stratum = strata[strata[MetaColumns.LEVEL] == MetaLevel.POOLED]
apoe_df = pd.concat([overall, per_stratum], ignore_index = True)
apoe_df[FCols.ORDER] = apoe_df[STRATUM].map(STRATUM_RANK)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plot per outcome
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for outcome, out_df in apoe_df.groupby(OUTCOME):
    title = f'{futils.outcome_name(str(outcome))} by APOE genotype'
    if (out_df[STRATUM] == ApoeStratum.ALL).all():
        logger.info(f'{outcome}: no APOE strata, skipped')
        continue
    # per gene all genotypes first, then the strata
    out_df = out_df.sort_values([GENE, FCols.ORDER]).copy()
    is_all = out_df[STRATUM] == ApoeStratum.ALL
    out_df[FCols.MARKER] = futils.significance_marker(
        out_df[MetaColumns.P], strict)
    out_df[FCols.COLOUR] = np.where(is_all, FStyle.POOLED_COLOUR,
                                     FStyle.STUDY_COLOUR)
    out_df[FCols.SIZE] = np.where(is_all, FStyle.POOLED_SIZE,
                                   FStyle.STUDY_SIZE)
    out_df[FCols.ROW_NAME] = out_df[STRATUM].map(FigNames.STRATA)
    # axis range
    out_df = futils.limit_or(out_df, 1 / args.max_or, args.max_or,
                                        title)
    if len(out_df) < 2:
        logger.warning(f'{title}: fewer than two estimates, skipped')
        continue
    out_df = futils.set_y(out_df, GENE)
    test_y = (out_df[FCols.Y].min() - FStyle.FOREST_Y_PAD,
              out_df[FCols.Y].max() + FStyle.FOREST_Y_PAD)
    # start figure
    height_cm = (FStyle.FOREST_BASE_HEIGHT_CM
                 + FStyle.CM_PER_Y * (test_y[1] - test_y[0]))
    matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
    fig = plt.figure(figsize = (FStyle.WIDTH_CM * FStyle.CM,
                                height_cm * FStyle.CM))
    gs = gridspec.GridSpec(nrows = 1, ncols = 4,
                           width_ratios = FStyle.FOREST_WIDTH_RATIOS,
                           figure = fig, wspace = 0.0,
                           bottom = FStyle.FOREST_BOTTOM_CM / height_cm,
                           top = 1 - FStyle.FOREST_TOP_CM / height_cm)
    # plot
    ax = fig.add_subplot(gs[0])
    ax.set_xscale('log')
    ax.set_zorder(1)
    bm_forest = forest.ForestPlot(
            data = out_df, x_col = FCols.OR, y_col = FCols.Y,
            lb_col = FCols.LB, ub_col = FCols.UB, g_col = GENE, ax = ax,
            )
    _, ax = bm_forest.plot(
            s_col = FCols.MARKER, c_col = FCols.COLOUR,
            s_size_col = FCols.SIZE, ci_colour = 'black',
            ci_lwd = FStyle.LWD, span = True, ylim = test_y,
            kwargs_scatter_dict = FStyle.SCATTER_KWARGS,
            kwargs_plot_ci_dict = FStyle.CI_KWARGS,
            )
    # formatting
    ax.axvline(1, linewidth = FStyle.LWD, linestyle = '--', c = 'black',
               zorder = .5)
    ax.spines[['right', 'top']].set_visible(False)
    x_lim, x_tic = futils.x_axis(out_df)
    ax.set_xlim(x_lim)
    ax.set_xticks(x_tic)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%g'))
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.tick_params(axis = 'both', which = 'minor', bottom = False,
                   labelsize = FStyle.AX_LAB_SZ, width = FStyle.LWD)
    ax.tick_params(axis = 'both', labelsize = FStyle.AX_LAB_SZ,
                   width = FStyle.LWD)
    for label in ax.get_yticklabels():
        label.set_fontstyle('italic')
    xlabel = FigNames.OR_LABEL
    ax.set_xlabel(xlabel, fontsize = FStyle.LAB_SIZE)
    ax.set_title(title, fontweight = 'bold', fontsize = FStyle.TITLE_SIZE,
                 loc = 'left', pad = 6)
    # create side tables
    span = bm_forest.span_dict
    for i, (column, header, align, xloc) in enumerate(TABLES, start = 1):
        side_ax = fig.add_subplot(gs[i])
        side_ax.set_ylim(ax.get_ylim())
        side_ax.set_zorder(1 - .1 * i)
        _ = forest.plot_table(
                out_df, ax = side_ax, string_col = column, y_col = FCols.Y,
                annoteheader = header, xloc = xloc, xloc_header = xloc,
                halignment_text = align, halignment_header = align,
                size_text = FStyle.STEXT_SIZE,
                size_header = FStyle.STEXT_SIZE,
                negative_padding = FStyle.TABLE_NEGATIVE_PADDING, span = span,
                )
    # add legend
    futils.add_legend(fig, ax, leg_handles,
                      FigNames.SIGNIFICANCE_TITLE)
    # save
    futils.save(fig, args.out_dir / f'forest_apoe_{args.label}_{outcome}')
