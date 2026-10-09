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
##     outcome, 95% CI, with side tables (outcome, OR (95% CI), p-value).
##     Marker shape shows significance: circle p >= 0.05, square
##     p < 0.05, diamond below the Bonferroni threshold
##     0.05 / (genes x outcomes with a pooled estimate). Run locally in
##     the `plot-misc` env on burden files copied from Myriad into
##     `results/output/`. Writes
##     `results/figures/forest_pooled_<label>.pdf`.
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
        HarmonisedColumns,
        MetaColumns,
        MetaLevel,
        Paths,
        VariantListColumns,
        )

logging.basicConfig(level = logging.INFO, format = '[%(levelname)s] %(message)s')
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
                    default = 20.0,
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
# side tables: column, header, alignment, x location
TABLES = (
    (futils.ROW_NAME, 'Outcome', 'left', 0.05),
    (futils.OR_TEXT, 'OR (95% CI)', 'center', 0.5),
    (futils.P_TEXT, 'P-value', 'center', 0.5),
)


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
pool_df['order'] = pool_df[OUTCOME].map(futils.OUTCOME_RANK).fillna(
        len(futils.OUTCOME_RANK))
pool_df = pool_df.sort_values([GENE, 'order', OUTCOME])
pool_df[futils.MARKER] = futils.significance_marker(
        pool_df[MetaColumns.P], strict)
pool_df[futils.COLOUR] = futils.POOLED_COLOUR
pool_df[futils.SIZE] = futils.POOLED_SIZE
pool_df[futils.ROW_NAME] = [futils.outcome_name(str(name))
                            for name in pool_df[OUTCOME]]

# axis range
pool_df, n_clipped = futils.limit_or(pool_df, 1 / args.max_or, args.max_or,
                                     TITLE)
if len(pool_df) < 2:
    sys.exit(f'{TITLE}: fewer than two estimates')
pool_df = futils.set_y(pool_df, GENE)
test_y = (pool_df[futils.Y].min() - 3, pool_df[futils.Y].max() + 3)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plot
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# start figure
height_cm = 1.6 + futils.CM_PER_Y * (test_y[1] - test_y[0])
matplotlib.rcParams['axes.linewidth'] = futils.LWD
fig = plt.figure(figsize = (futils.WIDTH_CM * futils.CM,
                            height_cm * futils.CM))
gs = gridspec.GridSpec(nrows = 1, ncols = 4,
                       width_ratios = [1.3, .7, .8, .35],
                       figure = fig, wspace = 0.0,
                       bottom = 1.0 / height_cm,
                       top = 1 - .35 / height_cm)
# plot
ax = fig.add_subplot(gs[0])
ax.set_xscale('log')
ax.set_zorder(1)
bm_forest = forest.ForestPlot(
        data = pool_df, x_col = futils.OR, y_col = futils.Y,
        lb_col = futils.LB, ub_col = futils.UB, g_col = GENE, ax = ax,
        )
_, ax = bm_forest.plot(
        s_col = futils.MARKER, c_col = futils.COLOUR,
        s_size_col = futils.SIZE, ci_colour = 'black',
        ci_lwd = futils.LWD, span = True, ylim = test_y,
        kwargs_scatter_dict = {
            'edgecolors': 'black',
            'linewidth': .3,
        },
        kwargs_plot_ci_dict = {
            'zorder': 1,
            'solid_capstyle': 'round',
            'linestyle': '-',
        }
        )
# formatting
ax.axvline(1, linewidth = futils.LWD, linestyle = '--', c = 'black',
           zorder = .5)
ax.spines[['right', 'top']].set_visible(False)
x_lim, x_tic = futils.x_axis(pool_df)
ax.set_xlim(x_lim)
ax.set_xticks(x_tic)
ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%g'))
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.tick_params(axis = 'both', which = 'minor', bottom = False,
               labelsize = futils.AX_LAB_SZ, width = futils.LWD)
ax.tick_params(axis = 'both', labelsize = futils.AX_LAB_SZ,
               width = futils.LWD)
for label in ax.get_yticklabels():
    label.set_fontstyle('italic')
xlabel = 'Odds ratio (95% CI)'
if n_clipped:
    xlabel += (f'\n{n_clipped} CIs truncated at '
               f'{1 / args.max_or:g}-{args.max_or:g}')
ax.set_xlabel(xlabel, fontsize = futils.LAB_SIZE)
ax.set_title(TITLE, fontweight = 'bold', fontsize = futils.TITLE_SIZE,
             loc = 'left', pad = 6)
# create side tables
span = bm_forest.span_dict
for i, (column, header, align, xloc) in enumerate(TABLES, start = 1):
    side_ax = fig.add_subplot(gs[i])
    side_ax.set_ylim(ax.get_ylim())
    side_ax.set_zorder(1 - .1 * i)
    _ = forest.plot_table(
            pool_df, ax = side_ax, string_col = column, y_col = futils.Y,
            annoteheader = header, xloc = xloc, xloc_header = xloc,
            halignment_text = align, halignment_header = align,
            size_text = futils.STEXT_SIZE,
            size_header = futils.STEXT_SIZE,
            negative_padding = 1, span = span,
            )
# add legend
fig.legend(handles = leg_handles, loc = 'lower left',
           bbox_to_anchor = (0.02, 0.0), ncol = 3, frameon = False,
           fontsize = futils.STEXT_SIZE, handletextpad = 0.2,
           columnspacing = 1.0)
# save
futils.save(fig, args.out_dir / f'forest_pooled_{args.label}')
