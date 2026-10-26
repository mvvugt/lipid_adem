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
##     threshold 0.05 / (genes x outcomes with a pooled estimate). When
##     the run has lipid outcomes (`Constants.LIPID_OUTCOMES`), a second
##     panel to the right shows their betas (95% CI, native UKB units),
##     each gene at the same height, with its own Bonferroni threshold
##     (genes x lipids). Run
##     locally in the `plot-misc` env on burden files copied from Snellius into
##     `results/output/`. Writes
##     `results/figures/forest_pooled_<label>.pdf` (main analysis,
##     `FigureNames.MAIN_FIGURES`) or `results/figures/sensitivity/`.
##
## Author: M. van Vugt
## Date created: 09/10/2026
## Last updated: 23/10/2026
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
import numpy as np
import pandas as pd
import plot_misc.forest as forest
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
LIPID_TITLE = 'Lipids, pooled (IVW)'
# side tables: column, header, alignment, x location; no outcome column,
# the outcomes are shown by colour
TABLES = (
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center', 0.5),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center', 0.5),
)
LIPID_TABLES = (
    (FCols.BETA_TEXT, FigNames.BETA_HEADER, 'center', 0.5),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center', 0.5),
)
# panel widths: the forest and the OR and p-value tables, at the same
# absolute size as in the other forests
WIDTH_RATIOS = (FStyle.FOREST_WIDTH_RATIOS[0],
                *FStyle.FOREST_WIDTH_RATIOS[2:])
WIDTH_CM = (FStyle.WIDTH_CM * sum(WIDTH_RATIOS)
            / sum(FStyle.FOREST_WIDTH_RATIOS))
# empty column between the outcome and the lipid panel (width ratio)
GAP_RATIO = 0.25


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pooled_rows(data: pd.DataFrame, rank: dict[str, int],
                colours: dict[str, str], strict: float) -> pd.DataFrame:
    """Pooled rows per gene in outcome order, with marker and colour.

    Parameters
    ----------
    data : `pd.DataFrame`
        Burden rows (binary outcomes or lipids).
    rank : `dict[str, int]`
        Outcome key -> plotting order; others last.
    colours : `dict[str, str]`
        Outcome key -> marker colour; others `FigureStyle.POOLED_COLOUR`.
    strict : `float`
        Bonferroni threshold of the panel.

    Returns
    -------
    pooled : `pd.DataFrame`
        The `MetaLevel.POOLED` rows, sorted by gene and outcome order,
        with `FigureColumns` `ORDER`, `MARKER`, `COLOUR` and `SIZE`.
    """
    pooled = data[data[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
    pooled[FCols.ORDER] = pooled[OUTCOME].map(rank).fillna(len(rank))
    pooled = pooled.sort_values([GENE, FCols.ORDER, OUTCOME])
    pooled[FCols.MARKER] = futils.significance_marker(
            pooled[MetaColumns.P], strict)
    pooled[FCols.COLOUR] = pooled[OUTCOME].map(colours).fillna(
            FStyle.POOLED_COLOUR)
    pooled[FCols.SIZE] = FStyle.MARKER_SIZE
    return pooled.reset_index(drop = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shared_y(frames: list[pd.DataFrame]) -> list[pd.DataFrame]:
    """Y coordinates shared by panels, so each gene sits at the same height.

    As `figure_utils.set_y` (rows 2 apart, 4 between genes), but each
    gene's block is as tall as its largest panel, and a gene missing in
    a panel keeps its empty block there.

    Parameters
    ----------
    frames : `list[pd.DataFrame]`
        One frame per panel, rows sorted in plotting order per gene.

    Returns
    -------
    frames : `list[pd.DataFrame]`
        Copies with `FigureColumns.Y`.
    """
    genes = sorted(set().union(*(frame[GENE] for frame in frames)))
    out = [frame.copy() for frame in frames]
    for frame in out:
        frame[FCols.Y] = np.nan
    position = 1.0
    for gene in genes:
        n_rows = 1
        for frame in out:
            rows = frame.index[frame[GENE] == gene]
            frame.loc[rows, FCols.Y] = position + 2 * np.arange(len(rows))
            n_rows = max(n_rows, len(rows))
        position += 2 * (n_rows - 1) + 4
    return out


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_panel(fig: plt.Figure, axes: list[gridspec.SubplotSpec],
               data: pd.DataFrame, x_col: str, lb_col: str, ub_col: str,
               tables: tuple[tuple[str, str, str, float], ...],
               title: str, ylim: tuple[float, float], log_x: bool,
               gene_labels: bool) -> plt.Axes:
    """Draw one forest with its side tables.

    Parameters
    ----------
    fig : `plt.Figure`
        The figure.
    axes : `list[gridspec.SubplotSpec]`
        Grid cells: the forest, then one per side table.
    data : `pd.DataFrame`
        Rows from `pooled_rows`, with `FigureColumns.Y`.
    x_col, lb_col, ub_col : `str`
        Point estimate and 95% CI columns.
    tables : `tuple`
        Side tables: column, header, alignment, x location.
    title : `str`
        Panel title.
    ylim : `tuple[float, float]`
        Y limits, shared by the panels.
    log_x : `bool`
        Odds ratios on a log axis with reference 1 (`figure_utils.x_axis`);
        else betas on a linear axis with reference 0
        (`figure_utils.beta_axis`).
    gene_labels : `bool`
        Show the gene names as y tick labels.

    Returns
    -------
    ax : `plt.Axes`
        The forest axis.
    """
    ax = fig.add_subplot(axes[0])
    if log_x:
        ax.set_xscale('log')
    ax.set_zorder(1)
    bm_forest = forest.ForestPlot(
            data = data, x_col = x_col, y_col = FCols.Y,
            lb_col = lb_col, ub_col = ub_col, g_col = GENE, ax = ax,
            )
    _, ax = bm_forest.plot(
            s_col = FCols.MARKER, c_col = FCols.COLOUR,
            s_size_col = FCols.SIZE, ci_colour = 'black',
            ci_lwd = FStyle.LWD, span = True, ylim = ylim,
            kwargs_scatter_dict = FStyle.SCATTER_KWARGS,
            kwargs_plot_ci_dict = FStyle.CI_KWARGS,
            )
    # formatting
    ax.axvline(1 if log_x else 0, linewidth = FStyle.LWD, linestyle = '--',
               c = 'black', zorder = .5)
    ax.spines[['right', 'top']].set_visible(False)
    if log_x:
        x_lim, x_tic = futils.x_axis(data)
        ax.xaxis.set_major_formatter(
                matplotlib.ticker.FormatStrFormatter('%g'))
        ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    else:
        x_lim, x_tic = futils.beta_axis(data)
    ax.set_xlim(x_lim)
    ax.set_xticks(x_tic)
    ax.tick_params(axis = 'both', which = 'minor', bottom = False,
                   labelsize = FStyle.AX_LAB_SZ, width = FStyle.LWD)
    ax.tick_params(axis = 'both', labelsize = FStyle.AX_LAB_SZ,
                   width = FStyle.LWD)
    if gene_labels:
        for label in ax.get_yticklabels():
            label.set_fontstyle('italic')
    else:
        ax.tick_params(axis = 'y', labelleft = False)
    ax.set_xlabel(FigNames.OR_LABEL if log_x else FigNames.BETA_LABEL,
                  fontsize = FStyle.LAB_SIZE)
    ax.set_title(title, fontweight = 'bold', fontsize = FStyle.TITLE_SIZE,
                 loc = 'left', pad = 6)
    # create side tables
    span = bm_forest.span_dict
    for i, (column, header, align, xloc) in enumerate(tables, start = 1):
        side_ax = fig.add_subplot(axes[i])
        side_ax.set_ylim(ax.get_ylim())
        side_ax.set_zorder(1 - .1 * i)
        _ = forest.plot_table(
                data, ax = side_ax, string_col = column, y_col = FCols.Y,
                annoteheader = header, xloc = xloc, xloc_header = xloc,
                halignment_text = align, halignment_header = align,
                size_text = FStyle.STEXT_SIZE,
                size_header = FStyle.STEXT_SIZE,
                negative_padding = FStyle.TABLE_NEGATIVE_PADDING,
                span = span,
                )
    return ax


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def outcome_legend(data: pd.DataFrame) -> list:
    """Colour legend handles of a panel's outcomes, in plotting order.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows from `pooled_rows`.

    Returns
    -------
    handles : `list[Line2D]`
        From `figure_utils.colour_legend`, named with
        `FigureNames.LIPIDS` or else `figure_utils.outcome_name`.
    """
    rows = data.drop_duplicates(OUTCOME).sort_values([FCols.ORDER, OUTCOME])
    return futils.colour_legend({
        FigNames.LIPIDS.get(str(outcome), futils.outcome_name(str(outcome))):
        colour
        for outcome, colour in zip(rows[OUTCOME], rows[FCols.COLOUR])
    })


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

burden = futils.load_burden(futils.burden_path(args.ancestry, args.label),
                            keep_lipids = True)
if burden is None:
    sys.exit(f'no burden file for {args.ancestry} {args.label}')
is_lipid = burden[OUTCOME].isin(Constants.LIPID_OUTCOMES)
binary = burden.loc[~is_lipid]
lipids = futils.add_beta_ci(burden.loc[is_lipid])

# significance markers and legend; one Bonferroni threshold per panel
strict, n_tests = futils.strict_threshold(binary)
leg_handles = futils.significance_legend(strict, n_tests)
lipid_strict, lipid_n_tests = futils.strict_threshold(lipids)
lipid_leg_handles = futils.significance_legend(lipid_strict, lipid_n_tests)

# pooled estimates, per gene the outcomes in plotting order
pool_df = pooled_rows(binary, FigNames.OUTCOME_RANK, FStyle.OUTCOME_COLOURS,
                      strict)
pool_df = futils.limit_or(pool_df, 1 / args.max_or, args.max_or, TITLE)
if len(pool_df) < 2:
    sys.exit(f'{TITLE}: fewer than two estimates')
lipid_df = pooled_rows(lipids, FigNames.LIPID_RANK, FStyle.LIPID_COLOURS,
                       lipid_strict)
has_lipids = not lipid_df.empty
if has_lipids:
    pool_df, lipid_df = shared_y([pool_df, lipid_df])
else:
    logger.info(f'{args.label}: no lipid rows, outcome panel only')
    pool_df = futils.set_y(pool_df, GENE)
y_all = pd.concat([pool_df[FCols.Y], lipid_df.get(FCols.Y, pd.Series())])
test_y = (y_all.min() - FStyle.FOREST_Y_PAD,
          y_all.max() + FStyle.FOREST_Y_PAD)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plot
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# start figure, one extra legend row for the outcome colours; the lipid
# panel (forest + tables) to the right of the outcome panel
ratios = WIDTH_RATIOS
width_cm = WIDTH_CM
if has_lipids:
    ratios = (*WIDTH_RATIOS, GAP_RATIO, *WIDTH_RATIOS)
    width_cm = WIDTH_CM * sum(ratios) / sum(WIDTH_RATIOS)
height_cm = (FStyle.FOREST_BASE_HEIGHT_CM + FStyle.LEGEND_ROW_CM
             + FStyle.CM_PER_Y * (test_y[1] - test_y[0]))
matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
fig = plt.figure(figsize = (width_cm * FStyle.CM, height_cm * FStyle.CM))
gs = gridspec.GridSpec(nrows = 1, ncols = len(ratios),
                       width_ratios = ratios,
                       figure = fig, wspace = 0.0,
                       bottom = ((FStyle.FOREST_BOTTOM_CM
                                  + FStyle.LEGEND_ROW_CM) / height_cm),
                       top = 1 - FStyle.FOREST_TOP_CM / height_cm)
n_cols = len(WIDTH_RATIOS)
ax = draw_panel(fig, [gs[i] for i in range(n_cols)], pool_df,
                FCols.OR, FCols.LB, FCols.UB, TABLES, TITLE, test_y,
                log_x = True, gene_labels = True)
# add legends: outcome colours above the significance shapes
futils.add_legend(fig, ax, outcome_legend(pool_df), FigNames.OUTCOME_TITLE,
                  y = FStyle.LEGEND_ROW_CM / height_cm)
futils.add_legend(fig, ax, leg_handles, FigNames.SIGNIFICANCE_TITLE)
if has_lipids:
    start = n_cols + 1
    lipid_ax = draw_panel(
            fig, [gs[i] for i in range(start, start + n_cols)], lipid_df,
            MetaColumns.BETA, FCols.BETA_LB, FCols.BETA_UB, LIPID_TABLES,
            LIPID_TITLE, test_y, log_x = False, gene_labels = False)
    futils.add_legend(fig, lipid_ax, outcome_legend(lipid_df),
                      FigNames.LIPID_TITLE,
                      y = FStyle.LEGEND_ROW_CM / height_cm)
    futils.add_legend(fig, lipid_ax, lipid_leg_handles,
                      FigNames.SIGNIFICANCE_TITLE)
# save
futils.save(fig, args.out_dir / f'forest_pooled_{args.label}')
