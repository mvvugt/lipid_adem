#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: variant_sets_forest
##
## Purpose of script: Forest plots of one gene's pooled (IVW) gene-burden
##     estimates per variant set (`Constants.BURDEN_VARIANT_SETS`: GoF,
##     AM, PTV, ClinVar, PTV + ClinVar, PTV + AM, AM + ClinVar,
##     PTV + ClinVar + AM): per outcome one row per variant set, 95% CI,
##     with side tables, as `pooled_forest.py`. Marker colour shows the
##     variant set, marker shape significance: circle p >= 0.05, square
##     p < 0.05, diamond below the Bonferroni threshold 0.05 / (outcomes x
##     variant sets with a pooled estimate, per panel). Each set is its
##     own `meta_analysis.py` run: `--label` plus the set's suffix
##     (`SET_LABEL_SUFFIX`, as src/lipid_adem.sh); a missing burden file
##     is skipped (logged). Binary outcomes (OR) and, to the right, lipids
##     (beta, native UKB units) are side by side in one file, each panel
##     with its own Bonferroni threshold. Run locally in the `plot-misc`
##     env on burden files copied from Myriad into `results/output/`.
##     Writes `results/figures/forest_variant_sets_<label>_<gene>.pdf`
##     (main analysis, `FigureNames.MAIN_FIGURES`) or
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
import matplotlib.gridspec as gridspec
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
logger = logging.getLogger('variant_sets_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Forest plots of one gene\'s pooled gene-burden '
        'estimates per variant set.')
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the runs (default: %(default)s)')
parser.add_argument('-l', '--label',
                    type = str,
                    required = True,
                    help = 'meta_analysis.py --label of the PTV + ClinVar run; '
                    'the other sets add their suffix')
parser.add_argument('-g', '--gene',
                    type = str,
                    default = 'CETP',
                    help = 'gene (default: %(default)s)')
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
# label suffix of each variant set's run (src/lipid_adem.sh): none for the
# main PTV + ClinVar set, else '_<set>'
SET_LABEL_SUFFIX = {
    variant_set: '' if variant_set == Constants.BURDEN_MASK_LOF
    else f'_{variant_set}'
    for variant_set in Constants.BURDEN_VARIANT_SETS
}
TITLE = f'{args.gene} gene burden per variant set, pooled (IVW)'
LIPID_TITLE = f'{args.gene} lipids per variant set, pooled (IVW)'
# side tables: column, header, alignment, x location; the variant sets are
# shown by colour
TABLES = (
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center', 0.5),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center', 0.5),
)
LIPID_TABLES = (
    (FCols.BETA_TEXT, FigNames.BETA_HEADER, 'center', 0.5),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center', 0.5),
)
# panel widths: the forest and the two tables, at the same absolute size
# as in the other forests
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
def load_sets(ancestry: str, label: str, gene: str) -> pd.DataFrame:
    """Read the gene's pooled burden rows of every variant-set run.

    Parameters
    ----------
    ancestry : `str`
        Ancestry code of the runs.
    label : `str`
        Label of the PTV + ClinVar run; each set adds its
        `SET_LABEL_SUFFIX`.
    gene : `str`
        Variant-list gene.

    Returns
    -------
    pooled : `pd.DataFrame`
        The `MetaLevel.POOLED` rows of `gene` (binary outcomes and
        lipids, from `figure_utils.load_burden`), with `VARIANT_SET`.
        Sets without a burden file or without rows of `gene` are left out
        (logged).
    """
    frames = []
    for variant_set, suffix in SET_LABEL_SUFFIX.items():
        burden = futils.load_burden(
                futils.burden_path(ancestry, f'{label}{suffix}'),
                keep_lipids = True)
        if burden is None:
            continue
        rows = burden[(burden[MetaColumns.LEVEL] == MetaLevel.POOLED)
                      & (burden[GENE] == gene)].copy()
        if rows.empty:
            logger.info(f'{variant_set}: no pooled rows of {gene}')
            continue
        rows[VARIANT_SET] = variant_set
        frames.append(rows)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def panel_rows(data: pd.DataFrame, outcome_rank: dict[str, int],
               outcome_names: dict[str, str]) -> tuple[pd.DataFrame, float,
                                                       int]:
    """Rows of one figure in plotting order, with marker and colour.

    Parameters
    ----------
    data : `pd.DataFrame`
        Pooled rows of one kind of outcome (binary or lipids), with
        `VARIANT_SET`.
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
        Bonferroni threshold of the figure.
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
    """Colour legend handles of the figure's variant sets, in plotting order.

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
def draw_panel(fig: plt.Figure, axes: list[gridspec.SubplotSpec],
               data: pd.DataFrame, x_col: str, lb_col: str, ub_col: str,
               tables: tuple[tuple[str, str, str, float], ...], title: str,
               ylim: tuple[float, float], log_x: bool, strict: float,
               n_tests: int, height_cm: float) -> None:
    """Draw one forest with its side tables and legends.

    Parameters
    ----------
    fig : `plt.Figure`
        The figure.
    axes : `list[gridspec.SubplotSpec]`
        Grid cells: the forest, then one per side table.
    data : `pd.DataFrame`
        Rows from `panel_rows`.
    x_col, lb_col, ub_col : `str`
        Point estimate and 95% CI columns.
    tables : `tuple`
        Side tables: column, header, alignment, x location.
    title : `str`
        Panel title.
    ylim : `tuple[float, float]`
        Y limits, shared by the panels (same row spacing).
    log_x : `bool`
        Odds ratios on a log axis with reference 1 (`figure_utils.x_axis`);
        else betas on a linear axis with reference 0
        (`figure_utils.beta_axis`).
    strict : `float`
        Bonferroni threshold of the panel (significance legend).
    n_tests : `int`
        Number of tests behind `strict`.
    height_cm : `float`
        Figure height, to place the legends.

    Returns
    -------
    `None`
    """
    ax = fig.add_subplot(axes[0])
    if log_x:
        ax.set_xscale('log')
    ax.set_zorder(1)
    bm_forest = forest.ForestPlot(
            data = data, x_col = x_col, y_col = FCols.Y,
            lb_col = lb_col, ub_col = ub_col, g_col = OUTCOME_LABEL, ax = ax,
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
    # add legends: variant-set colours above the significance shapes
    futils.add_legend(fig, ax, set_legend(data), FigNames.VARIANT_SET_TITLE,
                      y = FStyle.LEGEND_ROW_CM / height_cm)
    futils.add_legend(fig, ax, futils.significance_legend(strict, n_tests),
                      FigNames.SIGNIFICANCE_TITLE)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pooled = load_sets(args.ancestry, args.label, args.gene)
if pooled.empty:
    sys.exit(f'{args.gene}: no pooled rows in any variant-set run of '
             f'{args.ancestry} {args.label}')
logger.info(f'{args.gene}: pooled rows per variant set: ' + ', '.join(
    f'{variant_set} {n}'
    for variant_set, n in pooled[VARIANT_SET].value_counts().items()))
is_lipid = pooled[OUTCOME].isin(Constants.LIPID_OUTCOMES)
binary = pooled.loc[~is_lipid]
lipids = futils.add_beta_ci(pooled.loc[is_lipid])
stem = args.out_dir / f'forest_variant_sets_{args.label}_{args.gene}'


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# panels: binary outcomes (odds ratios; out-of-range estimates dropped
# after the Bonferroni count, as in pooled_forest.py), then the lipids
# (betas in native units), each with its own Bonferroni threshold
panels = []
if binary.empty:
    logger.info(f'{args.gene}: no binary-outcome rows, no OR panel')
else:
    bin_df, strict, n_tests = panel_rows(binary, FigNames.OUTCOME_RANK,
                                         FigNames.OUTCOMES)
    bin_df = futils.limit_or(bin_df, 1 / args.max_or, args.max_or, TITLE)
    if bin_df.empty:
        logger.info(f'{args.gene}: no OR within the axis limits')
    else:
        bin_df = futils.set_y(bin_df, OUTCOME_LABEL)
        panels.append((bin_df, FCols.OR, FCols.LB, FCols.UB, TABLES, TITLE,
                       True, strict, n_tests))
if lipids.empty:
    logger.info(f'{args.gene}: no lipid rows, no lipid panel')
else:
    lipid_df, lipid_strict, lipid_n_tests = panel_rows(
            lipids, FigNames.LIPID_RANK, FigNames.LIPIDS)
    panels.append((lipid_df, MetaColumns.BETA, FCols.BETA_LB,
                   FCols.BETA_UB, LIPID_TABLES, LIPID_TITLE, False,
                   lipid_strict, lipid_n_tests))
if not panels:
    sys.exit(f'{args.gene}: nothing to plot')

# one figure, the panels side by side (forest + tables, a gap between),
# y limits shared so rows are equally spaced; one extra legend row for
# the variant-set colours
y_all = pd.concat([panel[0][FCols.Y] for panel in panels])
ylim = (y_all.min() - FStyle.FOREST_Y_PAD, y_all.max() + FStyle.FOREST_Y_PAD)
n_cols = len(WIDTH_RATIOS)
ratios = WIDTH_RATIOS
for _ in panels[1:]:
    ratios = (*ratios, GAP_RATIO, *WIDTH_RATIOS)
width_cm = WIDTH_CM * sum(ratios) / sum(WIDTH_RATIOS)
height_cm = (FStyle.FOREST_BASE_HEIGHT_CM + FStyle.LEGEND_ROW_CM
             + FStyle.CM_PER_Y * (ylim[1] - ylim[0]))
matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
fig = plt.figure(figsize = (width_cm * FStyle.CM, height_cm * FStyle.CM))
gs = gridspec.GridSpec(nrows = 1, ncols = len(ratios),
                       width_ratios = ratios,
                       figure = fig, wspace = 0.0,
                       bottom = ((FStyle.FOREST_BOTTOM_CM
                                  + FStyle.LEGEND_ROW_CM) / height_cm),
                       top = 1 - FStyle.FOREST_TOP_CM / height_cm)
for i, (data, x_col, lb_col, ub_col, tables, title, log_x, strict,
        n_tests) in enumerate(panels):
    start = i * (n_cols + 1)
    draw_panel(fig, [gs[j] for j in range(start, start + n_cols)], data,
               x_col, lb_col, ub_col, tables, title, ylim, log_x, strict,
               n_tests, height_cm)
# save
futils.save(fig, stem)
