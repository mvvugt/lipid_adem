#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: sources_forest
##
## Purpose of script: Why the pooled (UKB + Thomassen + FinnGen) estimate
##     differs from the UKB carrier burden: one figure per variant set of
##     the `<label>_<set>` runs of `meta_analysis.py --prefer-groups`
##     (default `pooled_eur`), one forest per binary outcome in a grid
##     (`--n-cols`), per gene each source's estimate (Thomassen, as the
##     IVW of its APOE strata; FinnGen; UK Biobank, each over the variants
##     it contributes) and the pooled one last, 95% CI, with side tables
##     (source, OR (95% CI), p-value, UKB carriers / cases). Marker shape
##     shows significance: circle p >= 0.05, square p < 0.05, diamond
##     below the Bonferroni threshold 0.05 / (genes x outcomes with a
##     pooled estimate). Run locally in the `plot-misc` env on burden files
##     copied from Snellius into `results/output/`. Writes
##     `results/figures/sensitivity/forest_sources_<label>_<set>.pdf`
##     (main analysis when listed in `FigureNames.MAIN_FIGURES`).
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

import logging
import argparse
import numpy as np
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
logger = logging.getLogger('sources_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = ('Forests per outcome of --prefer-groups gene-burden '
                       'runs, by source, one figure per variant set.'))
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the runs (default: %(default)s)')
parser.add_argument('-l', '--label',
                    type = str,
                    default = 'pooled_eur',
                    help = 'meta_analysis.py --label without the variant-set '
                    'suffix (default: %(default)s)')
parser.add_argument('-s', '--sets',
                    nargs = '+',
                    choices = list(FigNames.VARIANT_SETS),
                    default = list(FigNames.VARIANT_SETS),
                    help = 'variant sets, one figure each (default: all)')
parser.add_argument('-n', '--n-cols',
                    type = int,
                    default = 2,
                    help = 'forests per figure row (default: %(default)s)')
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
if args.n_cols < 1:
    parser.error('--n-cols must be >= 1')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CONSTANTS
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENE = VariantListColumns.OUT_GENE
OUTCOME = HarmonisedColumns.OUTCOME
VARIANT_SET = 'variant_set'
# the row's one study, for the carrier counts
STUDY = '_study'
# row order per gene: other sources, UK Biobank, pooled
POOLED_ORDER = 2
# side tables: column, header, alignment
TABLES = (
    (FCols.ROW_NAME, FigNames.SOURCE_HEADER, 'left'),
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center'),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center'),
    (FCols.CARRIER_TEXT, FigNames.CARRIERS_HEADER, 'center'),
)
# space for the gene names left of each forest (cm)
LABEL_CM = 0.8


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def source_table(burden: pd.DataFrame, variant_set: str) -> pd.DataFrame:
    """One row per gene, outcome and source, then the pooled estimate.

    Parameters
    ----------
    burden : `pd.DataFrame`
        A run's burden file, from `figure_utils.load_burden`.
    variant_set : `str`
        The run's variant set (for the carrier counts).

    Returns
    -------
    rows : `pd.DataFrame`
        `figure_utils.source_rows` of the per-study rows plus the
        `MetaLevel.POOLED` rows, with `FigureColumns` `ROW_NAME`, `ORDER`
        and `CARRIER_TEXT`.
    """
    is_pooled = burden[MetaColumns.LEVEL] == MetaLevel.POOLED
    sources = futils.source_rows(burden.loc[~is_pooled])
    sources[FCols.ORDER] = np.where(sources[FCols.ROW_NAME] == FigNames.UKB,
                                    1, 0)
    sources[STUDY] = sources[HarmonisedColumns.STUDY_ACCESSION]
    pooled = burden.loc[is_pooled].copy()
    pooled[FCols.ROW_NAME] = FigNames.POOLED
    pooled[FCols.ORDER] = POOLED_ORDER
    # a pooled row of a single study (UKB only) names it in `studies`
    pooled[STUDY] = pooled[MetaColumns.STUDIES]
    rows = pd.concat([sources, pooled], ignore_index = True)
    rows[VARIANT_SET] = variant_set
    return futils.add_carrier_text(rows, STUDY, VARIANT_SET)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def outcome_rows(rows: pd.DataFrame, strict: float, title: str
                 ) -> pd.DataFrame:
    """One outcome's rows in plotting order, with marker, colour and y.

    Parameters
    ----------
    rows : `pd.DataFrame`
        The outcome's rows from `source_table`.
    strict : `float`
        Bonferroni threshold.
    title : `str`
        Forest title, for the warning on dropped estimates.

    Returns
    -------
    rows : `pd.DataFrame`
        Per gene the sources, then the pooled estimate, odds ratios
        within `--max-or`, with the `FigureColumns` `MARKER`, `COLOUR`,
        `SIZE` and `Y`.
    """
    rows = rows.sort_values([GENE, FCols.ORDER, FCols.ROW_NAME],
                            key = futils.gene_sort_key).copy()
    is_pooled = rows[FCols.ORDER] == POOLED_ORDER
    rows[FCols.MARKER] = futils.significance_marker(rows[MetaColumns.P],
                                                    strict)
    rows[FCols.COLOUR] = np.where(is_pooled, FStyle.POOLED_COLOUR,
                                  FStyle.STUDY_COLOUR)
    rows[FCols.SIZE] = np.where(is_pooled, FStyle.POOLED_SIZE,
                                FStyle.STUDY_SIZE)
    rows = futils.limit_or(rows, 1 / args.max_or, args.max_or, title)
    return futils.set_y(rows, GENE)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for variant_set in args.sets:
    label = f'{args.label}_{variant_set}'
    burden = futils.load_burden(futils.burden_path(args.ancestry, label))
    if burden is None:
        continue
    # significance markers and legend
    strict, n_tests = futils.strict_threshold(burden)
    rows = source_table(burden, variant_set)
    # one forest per outcome, in `FigureNames.OUTCOMES` order
    outcomes = sorted(rows[OUTCOME].unique(), key = lambda outcome:
                      FigNames.OUTCOME_RANK.get(outcome, len(
                          FigNames.OUTCOME_RANK)))
    panels = []
    for outcome in outcomes:
        title = futils.outcome_name(str(outcome))
        out_df = outcome_rows(rows.loc[rows[OUTCOME] == outcome], strict,
                              title)
        if len(out_df) < 2:
            logger.warning(f'{label} {title}: fewer than two estimates, '
                           'skipped')
            continue
        panels.append((out_df, title))
    if not panels:
        logger.warning(f'{label}: nothing to plot')
        continue
    # one y range for all forests (equal row spacing, panels aligned at
    # the top)
    ylim = futils.table_ylim(pd.concat([data[FCols.Y]
                                        for data, _ in panels]))
    fig, cells, _ = futils.table_grid(
            len(panels), min(args.n_cols, len(panels)),
            [column for column, _, _ in TABLES], ylim,
            label_cm = LABEL_CM)
    axes = [futils.draw_table_forest(fig, cell, data, title, ylim, True,
                                     GENE, TABLES,
                                     futils.group_bands(data, GENE),
                                     italic = True)
            for cell, (data, title) in zip(cells, panels)]
    futils.add_legend(fig, axes[0],
                      futils.significance_legend(strict, n_tests),
                      FigNames.SIGNIFICANCE_TITLE)
    futils.save(fig, args.out_dir / f'forest_sources_{label}')
