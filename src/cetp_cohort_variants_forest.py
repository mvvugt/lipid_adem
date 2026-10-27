#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: cetp_cohort_variants_forest
##
## Purpose of script: Why the pooled (UKB + Thomassen + FinnGen) and the
##     UKB-only results of one gene (default CETP) differ: one forest per
##     dementia outcome, with on top the UKB carrier burden per variant
##     set (`cohort_burden_<anc>_<set>` runs), then per FinnGen variant
##     its FinnGen estimate (from the `pooled_<anc>_<set>` runs, where
##     FinnGen adds only single variants) next to the UKB estimate of the
##     same variant (per-variant rows of the `cohort_burden` runs, written
##     with `--stratified`). All effects oriented to the therapeutic
##     direction (`Constants.THERAPY_DIRECTION`; CETP: lower function),
##     OR with 95% CI, with side tables (OR (95% CI), p-value, UKB
##     carriers / cases of the burden rows); the forests in a grid
##     (`--n-cols`). Run locally in the `plot-misc` env on files copied
##     from Snellius into `results/output/`. Writes
##     `results/figures/forest_cohort_variants_<gene>.pdf` (main analysis,
##     `FigureNames.MAIN_FIGURES`) or `results/figures/sensitivity/`.
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
import pandas as pd
import matplotlib.pyplot as plt
import figure_utils as futils
from pathlib import Path
from project_constants import (
        FigureColumns as FCols,
        FigureNames as FigNames,
        FigureStyle as FStyle,
        FileNames,
        HarmonisedColumns,
        MetaColumns,
        MetaLevel,
        Paths,
        VariantListColumns,
        )

logging.basicConfig(level = logging.INFO,
                    format = '[%(levelname)s] %(message)s')
logger = logging.getLogger('cetp_cohort_variants_forest')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser(
        description = 'Forest of a gene\'s UKB carrier burden next to the '
        'FinnGen and UKB estimates of the FinnGen variants.')
parser.add_argument('-a', '--ancestry',
                    type = str.upper,
                    default = MetaColumns.DEFAULT_ANCESTRY,
                    help = 'ancestry code of the runs (default: %(default)s)')
parser.add_argument('-c', '--cohort-label',
                    type = str,
                    default = 'cohort_burden_eur',
                    help = 'label of the carrier-burden runs without the '
                    'variant-set suffix (default: %(default)s)')
parser.add_argument('-p', '--pooled-label',
                    type = str,
                    default = 'pooled_eur',
                    help = 'label of the pooled runs without the '
                    'variant-set suffix (default: %(default)s)')
parser.add_argument('-s', '--sets',
                    nargs = '+',
                    choices = list(FigNames.VARIANT_SETS),
                    default = ['ptv', 'am', 'ptv_am'],
                    help = 'variant sets (default: %(default)s)')
parser.add_argument('-g', '--gene',
                    type = str,
                    default = 'CETP',
                    help = 'gene (default: %(default)s)')
parser.add_argument('-d', '--outcomes',
                    nargs = '+',
                    default = ['alzheimers_dementia', 'all_cause_dementia',
                               'vascular_dementia'],
                    help = 'outcomes, one forest each (default: %(default)s)')
parser.add_argument('-n', '--n-cols',
                    type = int,
                    default = 1,
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
STUDY = HarmonisedColumns.STUDY_ACCESSION
SITE = MetaColumns.VARIANT_SITE
SOURCE = VariantListColumns.OUT_SOURCE
# helper columns: block (y group), row label, row order in the block
BLOCK = 'block'
ROW_LABEL = 'row_label'
BURDEN_BLOCK = 'UKB carrier burden'
FINNGEN_ROW = futils.FINNGEN_NAME
UKB_ROW = FigNames.UKB
# helper columns: variant set of the burden rows and the row's one study,
# for the carrier counts
VARIANT_SET = 'variant_set'
ROW_STUDY = '_study'
# colours of the per-variant rows
FINNGEN_COLOUR = FStyle.POOLED_COLOUR
UKB_COLOUR = FStyle.STUDY_COLOUR
# side tables: column, header, alignment; carriers / cases of the
# burden rows only
TABLES = (
    (FCols.OR_TEXT, FigNames.OR_HEADER, 'center'),
    (FCols.P_TEXT, FigNames.P_HEADER, 'center'),
    (FCols.CARRIER_TEXT, FigNames.CARRIERS_HEADER, 'center'),
)
# space for the block and row labels left of each forest (cm)
LABEL_CM = 3.0


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Functions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def meta_path(ancestry: str, label: str) -> Path:
    """Path of a `meta_analysis.py` per-variant file.

    Parameters
    ----------
    ancestry : `str`
        `Ancestry` code of the run.
    label : `str`
        The run's `--label`.

    Returns
    -------
    path : `Path`
        In `Paths.RESULTS_OUTPUT`.
    """
    return Paths.RESULTS_OUTPUT / FileNames.META_ANALYSIS_TEMPLATE.format(
        ancestry = ancestry, suffix = f'_{label}')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def site_label(site: str, source: str) -> str:
    """Readable variant label, e.g. ``16:56962097 TGTAA>T (PTV)``.

    Parameters
    ----------
    site : `str`
        `variant_site`, ``chr:pos:a1:a2``.
    source : `str`
        Variant-list source(s) of the site.

    Returns
    -------
    label : `str`
    """
    parts = site.split(':')
    if len(parts) != 4:
        return f'{site} ({source})'
    chrom, pos, a1, a2 = parts
    return f'{chrom}:{pos} {a1}>{a2} ({source})'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def burden_rows() -> pd.DataFrame:
    """The gene's pooled UKB carrier burden per variant set.

    Returns
    -------
    rows : `pd.DataFrame`
        `MetaLevel.POOLED` rows of `args.gene` and `args.outcomes` with
        the `figure_utils.add_or` columns, `BLOCK`, `ROW_LABEL`,
        `FigureColumns.ORDER` and `FigureColumns.COLOUR`; sets without a
        burden file left out (logged).
    """
    frames = []
    for i, variant_set in enumerate(args.sets):
        burden = futils.load_burden(futils.burden_path(
                args.ancestry, f'{args.cohort_label}_{variant_set}'))
        if burden is None:
            continue
        rows = burden[(burden[MetaColumns.LEVEL] == MetaLevel.POOLED)
                      & (burden[GENE] == args.gene)
                      & burden[OUTCOME].isin(args.outcomes)].copy()
        rows[BLOCK] = BURDEN_BLOCK
        rows[ROW_LABEL] = FigNames.VARIANT_SETS[variant_set]
        rows[VARIANT_SET] = variant_set
        rows[FCols.ORDER] = i
        rows[FCols.COLOUR] = FStyle.VARIANT_SET_COLOURS[variant_set]
        frames.append(rows)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index = True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def variant_rows() -> pd.DataFrame:
    """FinnGen and UKB per-variant estimates of the FinnGen variants.

    Returns
    -------
    rows : `pd.DataFrame`
        Per FinnGen site (`args.gene`, `args.outcomes`) a FinnGen row from
        the pooled runs and, where present, a UKB row from the
        carrier-burden runs (both `level` ``stratum``, one study each),
        with the `figure_utils.add_or` columns, `BLOCK` (the site label),
        `ROW_LABEL`, `FigureColumns.ORDER` and `FigureColumns.COLOUR`.
        Sites in several sets' runs are kept once.
    """
    names = futils.study_names()
    finngen, ukb = [], []
    for variant_set in args.sets:
        for label, keep in ((args.pooled_label, finngen),
                            (args.cohort_label, ukb)):
            meta = futils.load_burden(meta_path(
                    args.ancestry, f'{label}_{variant_set}'))
            if meta is None:
                continue
            meta = meta[(meta[MetaColumns.LEVEL] == MetaLevel.STRATUM)
                        & (meta[GENE] == args.gene)
                        & meta[OUTCOME].isin(args.outcomes)]
            study = meta[STUDY].astype(str)
            if keep is finngen:
                is_cohort = study.map(names).eq(FINNGEN_ROW)
            else:
                is_cohort = study.str.startswith(futils.UKB_PREFIX)
            keep.append(meta.loc[is_cohort])
    if not finngen:
        logger.info(f'{args.gene}: no FinnGen per-variant rows')
        return pd.DataFrame()
    finngen = pd.concat(finngen).drop_duplicates([SITE, OUTCOME, STUDY])
    ukb = (pd.concat(ukb).drop_duplicates([SITE, OUTCOME, STUDY])
           if ukb else finngen.iloc[:0])
    ukb = ukb.loc[ukb[SITE].isin(finngen[SITE])]
    missing = sorted(set(finngen[SITE]) - set(ukb[SITE]))
    if missing:
        logger.info(f'{args.gene}: no UKB per-variant row for '
                    f'{", ".join(missing)}')
    finngen = finngen.assign(**{ROW_LABEL: FINNGEN_ROW, FCols.ORDER: 0,
                                FCols.COLOUR: FINNGEN_COLOUR})
    ukb = ukb.assign(**{ROW_LABEL: UKB_ROW, FCols.ORDER: 1,
                        FCols.COLOUR: UKB_COLOUR})
    rows = pd.concat([finngen, ukb], ignore_index = True)
    sources = (finngen.groupby(SITE)[SOURCE]
               .agg(lambda values: ' + '.join(sorted(set(map(str, values))))))
    rows[BLOCK] = [site_label(site, sources[site]) for site in rows[SITE]]
    return rows


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def block_y(rows: pd.DataFrame) -> tuple[dict[tuple[str, str], float],
                                         dict[str, float],
                                         list[tuple[float, float]]]:
    """Y per block header and row, shared by the forests, and grey bands.

    Each block starts with a header slot, its rows follow 2 apart, 4
    between blocks (`figure_utils.set_y`); a block keeps a slot for each
    of its row labels in every forest.

    Parameters
    ----------
    rows : `pd.DataFrame`
        All rows, burden block first, with `BLOCK`, `ROW_LABEL` and
        `FigureColumns.ORDER`.

    Returns
    -------
    y : `dict[tuple[str, str], float]`
        (block, row label) -> y.
    headers : `dict[str, float]`
        Block -> y of its header.
    bands : `list[tuple[float, float]]`
        Y ranges of every other block, header included, shaded grey.
    """
    slots = (rows[[BLOCK, ROW_LABEL, FCols.ORDER]].drop_duplicates()
             .sort_values(FCols.ORDER, kind = 'stable'))
    y: dict[tuple[str, str], float] = {}
    headers: dict[str, float] = {}
    bands: list[tuple[float, float]] = []
    position = 1.0
    for i, block in enumerate(dict.fromkeys(rows[BLOCK])):
        headers[block] = position
        labels = slots.loc[slots[BLOCK] == block, ROW_LABEL]
        for j, label in enumerate(labels):
            y[(block, label)] = position + 2 * (j + 1)
        last = position + 2 * len(labels)
        if i % 2:
            bands.append((position - 2, last + 2))
        position = last + 4
    return y, headers, bands


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_row_ticks(ax: plt.Axes, data: pd.DataFrame,
                  headers: dict[str, float]) -> None:
    """One y tick per row and a bold one per block header.

    Replaces the ticks `ForestPlot` derives from its group column, which
    merges rows that share a label (e.g. the UK Biobank row of every
    variant) into a single misplaced tick.

    Parameters
    ----------
    ax : `plt.Axes`
        Forest axis from `figure_utils.draw_table_forest`.
    data : `pd.DataFrame`
        The forest's rows, with `FigureColumns.Y` and `ROW_LABEL`.
    headers : `dict[str, float]`
        Block -> y of its header, from `block_y`.

    Returns
    -------
    `None`
    """
    ticks = {y: label for y, label in zip(data[FCols.Y], data[ROW_LABEL])}
    ticks.update({y: block for block, y in headers.items()})
    positions = sorted(ticks)
    ax.set_yticks(positions, [ticks[y] for y in positions])
    header_y = set(headers.values())
    for y, label in zip(positions, ax.get_yticklabels()):
        if y in header_y:
            label.set_fontweight('bold')
    # no tick mark next to the headers
    for y, tick in zip(positions, ax.yaxis.get_major_ticks()):
        if y in header_y:
            tick.tick1line.set_visible(False)


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Load data
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

frames = [frame for frame in (burden_rows(), variant_rows())
          if not frame.empty]
if not frames:
    sys.exit(f'{args.gene}: nothing to plot')
rows = pd.concat(frames, ignore_index = True)
logger.info(f'{args.gene}: ' + ', '.join(
    f'{block} {n}' for block, n in rows[BLOCK].value_counts(
        sort = False).items()))

# markers: nominal significance only, no Bonferroni (descriptive figure)
rows[FCols.MARKER] = futils.significance_marker(rows[MetaColumns.P], 0.0)
rows[FCols.SIZE] = FStyle.MARKER_SIZE
y_map, headers, bands = block_y(rows)
rows[FCols.Y] = [y_map[key] for key in zip(rows[BLOCK], rows[ROW_LABEL])]
# unique group per row for `ForestPlot`; the shown ticks are set after
# drawing (`set_row_ticks`)
rows['_tick'] = rows[BLOCK] + ': ' + rows[ROW_LABEL]
rows = rows.sort_values(FCols.Y).reset_index(drop = True)
ylim = futils.table_ylim([*y_map.values(), *headers.values()])
# UKB carriers / cases of the burden rows: their pooled row names the one
# study in `studies`; the per-variant rows have no variant set, so no
# counts
rows[ROW_STUDY] = rows[HarmonisedColumns.STUDY_ACCESSION].fillna(
        rows[MetaColumns.STUDIES])
rows = futils.add_carrier_text(rows, ROW_STUDY, VARIANT_SET)

panels = []
for outcome in args.outcomes:
    name = FigNames.OUTCOMES.get(outcome, futils.outcome_name(outcome))
    data = futils.limit_or(rows.loc[rows[OUTCOME] == outcome],
                           1 / args.max_or, args.max_or, name)
    if data.empty:
        logger.info(f'{name}: no estimates, forest left out')
        continue
    panels.append((data, name))
if not panels:
    sys.exit('nothing to plot')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Forest plots
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# the forests in a grid row by row, one extra legend row for the row
# colours
fig, cells, height_cm = futils.table_grid(
        len(panels), min(args.n_cols, len(panels)),
        [column for column, _, _ in TABLES], ylim, n_legend_rows = 2,
        label_cm = LABEL_CM)
axes = [futils.draw_table_forest(fig, cell, data, name, ylim, True, '_tick',
                                 TABLES, bands)
        for cell, (data, name) in zip(cells, panels)]
for ax, (data, _) in zip(axes, panels):
    set_row_ticks(ax, data, headers)
# legends below the first forest: row colours above the significance shapes
colours = {FigNames.VARIANT_SETS[variant_set]:
           FStyle.VARIANT_SET_COLOURS[variant_set]
           for variant_set in args.sets
           if FigNames.VARIANT_SETS[variant_set] in set(rows[ROW_LABEL])}
colours.update({f'{FINNGEN_ROW} per variant': FINNGEN_COLOUR,
                f'{UKB_ROW} per variant': UKB_COLOUR})
futils.add_legend(fig, axes[0], futils.colour_legend(colours), 'Estimate',
                  y = FStyle.LEGEND_ROW_CM / height_cm)
futils.add_legend(fig, axes[0], futils.significance_legend(0.0, 0)[:2],
                  FigNames.SIGNIFICANCE_TITLE)
# save
futils.save(fig, args.out_dir / f'forest_cohort_variants_{args.gene}')
