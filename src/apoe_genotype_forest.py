#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: apoe_genotype_forest
##
## Purpose of script: Forest plot per population of the UK Biobank marvel
##     association of each APOE genotype vs ε3/ε3
##     (`config/marvel_apoe_task.cnf`): per outcome one row per genotype,
##     odds ratio with 95% CI, side tables (genotype (n), OR (95% CI),
##     p-value). No title or legend; circles coloured by genotype (blue
##     ε2, red ε4, purple ε2/ε4); x axis from 0.5. Reads the loose marvel
##     files of the `FileNames.MARVEL_APOE_TASKS` outdirs copied into
##     `results/`. Run locally in the `plot-misc` env. Writes
##     `results/figures/forest_apoe_genotype_<population>.pdf`.
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

import re
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
        Constants,
        FileNames,
        HarmonisedColumns,
        MarvelColumns,
        MetaColumns,
        Paths,
        )

logging.basicConfig(level = logging.INFO, format = '[%(levelname)s] %(message)s')
logger = logging.getLogger('apoe_genotype_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = ('Forest plot of the marvel APOE genotype vs e3e3 runs, '
                       'read from the outdirs of marvel_apoe_tasks.tsv copied '
                       'into results/.'))
parser.add_argument('-m', '--model',
                    type = str,
                    default = 'model_3',
                    help = 'marvel model (default: %(default)s)')
parser.add_argument('-r', '--results-dir',
                    type = Path,
                    default = Paths.HERE / 'results',
                    help = ('local directory holding copies of the outdirs '
                            '(default: %(default)s)'))
parser.add_argument('-o', '--out-dir',
                    type = Path,
                    default = Paths.RESULTS_FIGURES,
                    help = 'output directory (default: %(default)s)')
parser.add_argument('--max-or',
                    type = float,
                    default = 20.0,
                    help = 'odds-ratio axis limit (default: %(default)s)')

args = parser.parse_args()
if args.max_or <= 1:
    parser.error('--max-or must be > 1')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OUTCOME = HarmonisedColumns.OUTCOME
GENOTYPE = 'genotype'
POPULATION = 'population'
OUTCOME_GROUP = 'outcome_name'
# marvel results column with the error of a skipped test
MARVEL_REMARKS = 'remarks'
# marvel variable -> outcome key (`futils.OUTCOME_NAMES`)
APOE_OUTCOMES = {
    **Constants.MARVEL_UKB_OUTCOMES,
    'ascvd_ii': 'ascvd',
}
# genotypes vs the reference (`Constants.UKB_APOE_REFERENCE`, ε3/ε3), in
# plotting order: ε2 dose down, then ε4 dose up
GENOTYPE_NAMES = {
    'e2e2': 'ε2/ε2',
    'e2e3': 'ε2/ε3',
    'e3e4': 'ε3/ε4',
    'e2e4': 'ε2/ε4',
    'e4e4': 'ε4/ε4',
}
GENOTYPE_RANK = {name: i for i, name in enumerate(GENOTYPE_NAMES)}
# blue = ε2, red = ε4, purple = both (ColorBrewer)
GENOTYPE_COLOURS = {
    'e2e2': '#2166ac',
    'e2e3': '#67a9cf',
    'e3e4': '#ef8a62',
    'e2e4': '#8073ac',
    'e4e4': '#b2182b',
}
MARKER_SIZE = 9
MIN_OR = .5
# marvel `subset` (`FileNames.MARVEL_APOE_TASKS`) -> population label
SUBSET_POPULATIONS = {
    'all': 'all',
    'eur_overall': 'EUR',
}
# dummy-coded marvel exposure of the genotype vs `strata_ref`
APOE_EXPOSURE_RE = re.compile(
    rf'^{re.escape(Constants.UKB_APOE_COLUMN)}: (?P<genotype>\S+)$')
REQUIRED = [
    MarvelColumns.MODEL_NAME,
    MarvelColumns.VARIABLE,
    MarvelColumns.EXPOSURE,
    MarvelColumns.EXPOSED,
    MarvelColumns.ESTIMATE,
    MarvelColumns.SE,
    MarvelColumns.P_VALUE,
]
# side tables: column, header, alignment, x location
TABLES = (
    (futils.ROW_NAME, 'APOE genotype', 'left', 0.05),
    (futils.OR_TEXT, 'OR (95% CI)', 'center', 0.5),
    (futils.P_TEXT, 'P-value', 'center', 0.5),
)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# job-array file: `outdir` (Myriad path) and `subset` per run
tasks = pd.read_csv(FileNames.MARVEL_APOE_TASKS, sep = '\t', dtype = str)
unknown = sorted(set(tasks['subset']) - set(SUBSET_POPULATIONS))
if unknown:
    raise ValueError(f'{FileNames.MARVEL_APOE_TASKS}: subset(s) {unknown} '
                     'not in SUBSET_POPULATIONS')

# loose marvel result files per outdir
frames = []
for task in tasks.itertuples(index = False):
    outdir = args.results_dir / Path(task.outdir).name
    files = sorted(outdir.glob(FileNames.MARVEL_LOOSE_GLOB))
    if not files:
        logger.info(f'{outdir}: no marvel result files, skipped')
        continue
    for path in files:
        tmp = pd.read_csv(path, sep = '\t', low_memory = False)
        missing = [col for col in REQUIRED if col not in tmp.columns]
        if missing:
            raise ValueError(f'{path}: missing marvel column(s) {missing}')
        tmp[POPULATION] = SUBSET_POPULATIONS[task.subset]
        frames.append(tmp)
    logger.info(f'{outdir}: {len(files)} marvel result files')
if not frames:
    sys.exit('APOE genotype: no marvel result files found')
gen_df = pd.concat(frames, ignore_index = True)

# skipped tests (marvel exits 0 anyway): one row per outcome and model with
# the error in `remarks` and no estimate
if MARVEL_REMARKS in gen_df.columns:
    for remark, n in gen_df[MARVEL_REMARKS].dropna().value_counts().items():
        logger.warning(f'APOE genotype: {n} skipped marvel tests: {remark}')

# genotype of the dummy-coded exposure; missing genotypes (e.g. 'Unknown',
# their own dummy term in marvel), intercept and covariates -> NaN
gen_df[GENOTYPE] = gen_df[MarvelColumns.EXPOSURE].astype(str).str.extract(
        APOE_EXPOSURE_RE)['genotype']
gen_df.loc[gen_df[GENOTYPE].isin(Constants.APOE_MISSING_VALUES),
           GENOTYPE] = np.nan
unknown = sorted(set(gen_df[GENOTYPE].dropna())
                 - set(Constants.APOE_GENOTYPES))
if unknown:
    raise ValueError(f'genotype(s) {unknown} not in Constants.APOE_GENOTYPES '
                     f'{Constants.APOE_GENOTYPES}')

# model, outcomes and genotypes vs the reference
gen_df = gen_df[(gen_df[MarvelColumns.MODEL_NAME] == args.model) &
                (gen_df[MarvelColumns.VARIABLE].isin(APOE_OUTCOMES)) &
                (gen_df[GENOTYPE].isin(GENOTYPE_NAMES))].copy()
gen_df[OUTCOME] = gen_df[MarvelColumns.VARIABLE].map(APOE_OUTCOMES)
gen_df[MetaColumns.BETA] = pd.to_numeric(gen_df[MarvelColumns.ESTIMATE],
                                         errors = 'coerce')
gen_df[MetaColumns.SE] = pd.to_numeric(gen_df[MarvelColumns.SE],
                                       errors = 'coerce')
gen_df[MetaColumns.P] = pd.to_numeric(gen_df[MarvelColumns.P_VALUE],
                                      errors = 'coerce')
gen_df[MarvelColumns.EXPOSED] = pd.to_numeric(gen_df[MarvelColumns.EXPOSED],
                                              errors = 'coerce')
usable = (np.isfinite(gen_df[MetaColumns.BETA]) &
          np.isfinite(gen_df[MetaColumns.SE]))
if not usable.all():
    logger.info(f'APOE genotype: {int((~usable).sum())} rows without '
                'estimate/SE dropped')
gen_df = gen_df.loc[usable]
if gen_df.empty:
    sys.exit(f'APOE genotype: no {args.model} rows for the outcomes')

# one row per population, outcome and genotype
key = [POPULATION, OUTCOME, GENOTYPE]
repeats = gen_df.duplicated(key, keep = False)
if repeats.any():
    raise ValueError(
        f'APOE genotype: {int(repeats.sum())} rows share a population, '
        f'outcome and genotype ({args.model}):\n'
        + gen_df.loc[repeats, key].to_string(index = False))

# odds ratios and side-table texts
gen_df = futils.add_or(gen_df)
logger.info(f'APOE genotype ({args.model}): {len(gen_df)} rows')

# order: outcomes in `OUTCOME_NAMES` order, then genotypes
gen_df['outcome_order'] = gen_df[OUTCOME].map(futils.OUTCOME_RANK)
gen_df['genotype_order'] = gen_df[GENOTYPE].map(GENOTYPE_RANK)
gen_df = gen_df.sort_values(['outcome_order', 'genotype_order'])
gen_df[OUTCOME_GROUP] = gen_df[OUTCOME].map(futils.outcome_name)

# one symbol, coloured by genotype
gen_df[futils.MARKER] = futils.MARKER_NS
gen_df[futils.COLOUR] = gen_df[GENOTYPE].map(GENOTYPE_COLOURS)
gen_df[futils.SIZE] = MARKER_SIZE
gen_df[futils.ROW_NAME] = [
    GENOTYPE_NAMES[genotype] if not np.isfinite(exposed)
    else f'{GENOTYPE_NAMES[genotype]} (n={int(exposed):,})'
    for genotype, exposed in zip(gen_df[GENOTYPE],
                                 gen_df[MarvelColumns.EXPOSED])
]


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plot per population
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for pop, pop_df in gen_df.groupby(POPULATION):
    # axis range
    pop_df, n_clipped = futils.limit_or(pop_df, MIN_OR, args.max_or,
                                        f'APOE genotype {pop}')
    if len(pop_df) < 2:
        logger.warning(f'APOE genotype {pop}: fewer than two estimates, '
                       'skipped')
        continue
    pop_df = futils.set_y(pop_df, OUTCOME_GROUP)
    test_y = (pop_df[futils.Y].min() - 3, pop_df[futils.Y].max() + 3)
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
            data = pop_df, x_col = futils.OR, y_col = futils.Y,
            lb_col = futils.LB, ub_col = futils.UB, g_col = OUTCOME_GROUP,
            ax = ax,
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
    x_lim, x_tic = futils.x_axis(pop_df, low = MIN_OR)
    ax.set_xlim(x_lim)
    ax.set_xticks(x_tic)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%g'))
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.tick_params(axis = 'both', which = 'minor', bottom = False,
                   labelsize = futils.AX_LAB_SZ, width = futils.LWD)
    ax.tick_params(axis = 'both', labelsize = futils.AX_LAB_SZ,
                   width = futils.LWD)
    xlabel = 'Odds ratio (95% CI)'
    if n_clipped:
        xlabel += (f'\n{n_clipped} CIs truncated at '
                   f'{MIN_OR:g}-{args.max_or:g}')
    ax.set_xlabel(xlabel, fontsize = futils.LAB_SIZE)
    # create side tables
    span = bm_forest.span_dict
    for i, (column, header, align, xloc) in enumerate(TABLES, start = 1):
        side_ax = fig.add_subplot(gs[i])
        side_ax.set_ylim(ax.get_ylim())
        side_ax.set_zorder(1 - .1 * i)
        _ = forest.plot_table(
                pop_df, ax = side_ax, string_col = column, y_col = futils.Y,
                annoteheader = header, xloc = xloc, xloc_header = xloc,
                halignment_text = align, halignment_header = align,
                size_text = futils.STEXT_SIZE,
                size_header = futils.STEXT_SIZE,
                negative_padding = 1, span = span,
                )
    # save
    futils.save(fig, args.out_dir / f'forest_apoe_genotype_{pop}')
