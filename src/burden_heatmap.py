#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: burden_heatmap
##
## Purpose of script: Heatmap of the pooled gene-burden log odds ratio per
##     gene (rows) and outcome (columns, in `OUTCOME_NAMES` order) of a
##     `meta_analysis.py` run. Glyphs show significance: square p < 0.05,
##     diamond below the Bonferroni threshold 0.05 / (genes x outcomes
##     with a pooled estimate); blank cells have no estimate. Run locally
##     in the `plot-misc` env on burden files copied from Myriad into
##     `results/output/`. Writes
##     `results/figures/sensitivity/heatmap_burden_<label>.pdf`.
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
import warnings
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import figure_utils as futils
from pathlib import Path
from plot_misc.heatmap import annotate_heatmap, heatmap
from project_constants import (
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
logger = logging.getLogger('burden_heatmap')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Heatmap of the pooled gene-burden log odds ratios.')
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

args = parser.parse_args()


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENE = VariantListColumns.OUT_GENE
OUTCOME = HarmonisedColumns.OUTCOME
CBAR_LABEL = 'Pooled log odds ratio'


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

burden = futils.load_burden(futils.burden_path(args.ancestry, args.label))
if burden is None:
    sys.exit(f'no burden file for {args.ancestry} {args.label}')
strict, n_tests = futils.strict_threshold(burden)

# gene x outcome matrices, outcomes in `OUTCOME_NAMES` order (others last)
pooled = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED]
beta = pooled.pivot(index = GENE, columns = OUTCOME,
                    values = MetaColumns.BETA)
columns = sorted(beta.columns, key = lambda name: (
        FigNames.OUTCOME_RANK.get(name, len(FigNames.OUTCOME_RANK)), name))
beta = beta[columns]
p = pooled.pivot(index = GENE, columns = OUTCOME, values = MetaColumns.P)
p = p.reindex_like(beta)

# significance glyphs
glyphs = pd.DataFrame('', index = beta.index, columns = beta.columns)
glyphs = glyphs.mask(p < FStyle.P_NOMINAL, FStyle.GLYPH_NOMINAL)
glyphs = glyphs.mask(p < strict, FStyle.GLYPH_STRICT)

# symmetric colour range
n_cells = int(beta.notna().sum().sum())
limit = float(np.nanmax(np.abs(beta.to_numpy()))) if n_cells else 1.0


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Heatmap
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# start figure
matplotlib.rcParams['axes.linewidth'] = FStyle.LWD
fig, ax = plt.subplots(figsize = ((2.5 + 1.0 * beta.shape[1]) * FStyle.CM,
                                  (2.0 + 0.6 * beta.shape[0]) * FStyle.CM))
# plot
im, cbar = heatmap(
        beta.to_numpy(dtype = float),
        row_labels = list(beta.index),
        col_labels = [futils.outcome_name(str(name)) for name in beta.columns],
        ax = ax, cbar_bool = True, cbar_label = CBAR_LABEL,
        cmap = 'RdBu_r', vmin = -limit, vmax = limit, grid_linewidth = 1,
        )
with warnings.catch_warnings():
    # empty (NaN) cells are masked; matplotlib warns per masked cell
    warnings.simplefilter('ignore', UserWarning)
    annotate_heatmap(im, data = glyphs, threshold = limit / 2,
                     fontsize = FStyle.STEXT_SIZE)
# formatting
ax.tick_params(axis = 'both', labelsize = FStyle.AX_LAB_SZ,
               width = FStyle.LWD, length = 2)
for tick in ax.get_yticklabels():
    tick.set_fontstyle('italic')
cbar.ax.tick_params(labelsize = FStyle.AX_LAB_SZ, width = FStyle.LWD,
                    length = 2)
cbar.outline.set_linewidth(FStyle.LWD)
cbar.set_label(CBAR_LABEL, fontsize = FStyle.LAB_SIZE)
ax.set_title('Gene burden', fontweight = 'bold',
             fontsize = FStyle.TITLE_SIZE, loc = 'left')
# footnote
fig.text(0.0, -0.08,
         f'{FStyle.GLYPH_NOMINAL} p < {FStyle.P_NOMINAL:g}; '
         f'{FStyle.GLYPH_STRICT} p < '
         f'{futils.sci_notation(strict, sig_fig = 1)} '
         f'(Bonferroni, {n_tests} tests); blank: no estimate',
         fontsize = FStyle.STEXT_SIZE)
# save
futils.save(fig, args.out_dir / f'heatmap_burden_{args.label}')
