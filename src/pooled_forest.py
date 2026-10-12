#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: pooled_forest
##
## Purpose of script: One forest plot of the pooled (IVW) gene-burden
##     estimates of a `meta_analysis.py` run: per gene one row per
##     outcome, 95% CI, with side tables (OR (95% CI), p-value).
##     Marker colour shows the outcome, marker shape significance:
##     circle p >= 0.05, square p < 0.05, diamond below the Bonferroni
##     threshold 0.05 / (genes x outcomes with a pooled estimate). Run
##     locally in the `plot-misc` env on burden files copied from Myriad into
##     `results/output/`. Writes
##     `results/figures/forest_pooled_<label>.pdf` (main analysis,
##     `FigureNames.MAIN_FIGURES`) or `results/figures/sensitivity/`.
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
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plot_misc.forest as forest
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
logger = logging.getLogger('pooled_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'One forest plot of the pooled gene-burden estimates.')
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
OUTCOME = HarmonisedColumns.OUTCOME
TITLE = 'Gene burden, pooled (IVW)'
# side tables: column, header, alignment, x location; no outcome column,
# the outcomes are shown by colour
TABLES = (
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center', 0.5),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center', 0.5),
)
# panel widths: the forest and the OR and p-value tables, at the same
# absolute size as in the other forests
WIDTH_RATIOS = (FStyle.FOREST_WIDTH_RATIOS[0],
                *FStyle.FOREST_WIDTH_RATIOS[2:])
WIDTH_CM = (FStyle.WIDTH_CM * sum(WIDTH_RATIOS)
            / sum(FStyle.FOREST_WIDTH_RATIOS))


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

burden = futils.load_burden(futils.burden_path(args.ancestry, args.label))
if burden is None:
    sys.exit(f'no burden file for {args.ancestry} {args.label}')

# significance markers and legend
strict, n_tests = futils.strict_threshold(burden)
leg_handles = futils.significance_legend(strict, n_tests)

# pooled estimates, per gene the outcomes in `OUTCOME_NAMES` order
pool_df = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
pool_df[FCols.ORDER] = pool_df[OUTCOME].map(FigNames.OUTCOME_RANK).fillna(
        len(FigNames.OUTCOME_RANK))
pool_df = pool_df.sort_values([GENE, FCols.ORDER, OUTCOME])
pool_df[FCols.MARKER] = futils.significance_marker(
        pool_df[MetaColumns.P], strict)
# colour per outcome, others black
pool_df[FCols.COLOUR] = pool_df[OUTCOME].map(
        FStyle.OUTCOME_COLOURS).fillna(FStyle.POOLED_COLOUR)
pool_df[FCols.SIZE] = FStyle.MARKER_SIZE

# axis range
pool_df = futils.limit_or(pool_df, 1 / args.max_or, args.max_or,
                                     TITLE)
if len(pool_df) < 2:
    sys.exit(f'{TITLE}: fewer than two estimates')
pool_df = futils.set_y(pool_df, GENE)
# outcome colour legend, in plotting order
legend_rows = pool_df.drop_duplicates(OUTCOME).sort_values(
        [FCols.ORDER, OUTCOME])
colour_handles = futils.colour_legend({
    futils.outcome_name(str(outcome)): colour
    for outcome, colour in zip(legend_rows[OUTCOME],
                               legend_rows[FCols.COLOUR])
})
test_y = (pool_df[FCols.Y].min() - FStyle.FOREST_Y_PAD,
          pool_df[FCols.Y].max() + FStyle.FOREST_Y_PAD)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plot
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# start figure, one extra legend row for the outcome colours
height_cm = (FStyle.FOREST_BASE_HEIGHT_CM + FStyle.LEGEND_ROW_CM
             + FStyle.CM_PER_Y * (test_y[1] - test_y[0]))
matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
fig = plt.figure(figsize = (WIDTH_CM * FStyle.CM, height_cm * FStyle.CM))
gs = gridspec.GridSpec(nrows = 1, ncols = len(WIDTH_RATIOS),
                       width_ratios = WIDTH_RATIOS,
                       figure = fig, wspace = 0.0,
                       bottom = ((FStyle.FOREST_BOTTOM_CM
                                  + FStyle.LEGEND_ROW_CM) / height_cm),
                       top = 1 - FStyle.FOREST_TOP_CM / height_cm)
# plot
ax = fig.add_subplot(gs[0])
ax.set_xscale('log')
ax.set_zorder(1)
bm_forest = forest.ForestPlot(
        data = pool_df, x_col = FCols.OR, y_col = FCols.Y,
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
x_lim, x_tic = futils.x_axis(pool_df)
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
ax.set_title(TITLE, fontweight = 'bold', fontsize = FStyle.TITLE_SIZE,
             loc = 'left', pad = 6)
# create side tables
span = bm_forest.span_dict
for i, (column, header, align, xloc) in enumerate(TABLES, start = 1):
    side_ax = fig.add_subplot(gs[i])
    side_ax.set_ylim(ax.get_ylim())
    side_ax.set_zorder(1 - .1 * i)
    _ = forest.plot_table(
            pool_df, ax = side_ax, string_col = column, y_col = FCols.Y,
            annoteheader = header, xloc = xloc, xloc_header = xloc,
            halignment_text = align, halignment_header = align,
            size_text = FStyle.STEXT_SIZE,
            size_header = FStyle.STEXT_SIZE,
            negative_padding = FStyle.TABLE_NEGATIVE_PADDING, span = span,
            )
# add legends: outcome colours above the significance shapes
futils.add_legend(fig, ax, colour_handles, FigNames.OUTCOME_TITLE,
                  y = FStyle.LEGEND_ROW_CM / height_cm)
futils.add_legend(fig, ax, leg_handles, FigNames.SIGNIFICANCE_TITLE)
# save
futils.save(fig, args.out_dir / f'forest_pooled_{args.label}')
