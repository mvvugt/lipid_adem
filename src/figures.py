#!/usr/bin/env python3
"""
Figures of the gene-burden meta-analysis (`meta_analysis.py` burden files).

Run locally in the `plot-misc` env on burden files copied from Myriad
into `results/output/`. Writes PDF and PNG files to `results/figures/`:

- ``forest_burden_<label>_<outcome>``: per gene the pooled odds ratio
  (diamond) and each study's own estimate (circles), 95% CI;
- ``forest_apoe_<label>_<outcome>``: per gene the pooled odds ratio over
  all APOE genotypes and per APOE stratum; skipped (logged) until the
  ``_apoe_strata`` burden file exists;
- ``heatmap_burden_<label>``: pooled log odds ratio per gene and outcome,
  ``*`` p < 0.05, ``**`` p below the Bonferroni threshold over the cells
  shown.

Only `project_constants` is imported from the pipeline; `functions.py`
needs the Myriad biomed-api env.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import logging
import os
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import to_hex
from matplotlib.lines import Line2D
from plot_misc.forest import ForestPlot
from plot_misc.heatmap import annotate_heatmap, heatmap

from project_constants import (
    ApoeStratum,
    Constants,
    FileNames,
    HarmonisedColumns,
    MetaColumns,
    MetaLevel,
    Paths,
    VariantListColumns,
)


_LOGGER = logging.getLogger("figures")
_Z_95: float = 1.959963984540054
# plotted columns added to the burden rows
_OR: str = "odds_ratio"
_LB: str = "or_lower"
_UB: str = "or_upper"
_Y: str = "y"
_MARKER: str = "marker"
_COLOUR: str = "colour"
_SIZE: str = "size"
_POOLED_COLOUR: str = "black"
_POOLED_MARKER: str = "D"
_STUDY_MARKER: str = "o"
# APOE strata in plotting order, `ApoeStratum.ALL` = all genotypes
_STRATUM_ORDER: tuple[str, ...] = (
    ApoeStratum.ALL,
    ApoeStratum.E44,
    ApoeStratum.E43,
    ApoeStratum.E33,
    ApoeStratum.E22_E32,
)
_DPI: int = 300
_P_NOMINAL: float = 0.05


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# reading

def burden_path(ancestry: str, label: str, extra: str = "") -> Path:
    """Path of a `meta_analysis.py` burden file.

    Parameters
    ----------
    ancestry : `str`
        `Ancestry` code of the run.
    label : `str`
        The run's `--label`.
    extra : `str`, optional, default: `""`
        Further suffix, e.g. ``"_apoe_strata"``.

    Returns
    -------
    path : `Path`
        In `Paths.RESULTS_OUTPUT`.
    """
    return Paths.RESULTS_OUTPUT / FileNames.BURDEN_TEMPLATE.format(
        ancestry=ancestry, suffix=f"_{label}{extra}"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_burden(path: Path) -> pd.DataFrame | None:
    """Read a burden file and add the odds ratio with its 95% CI.

    Parameters
    ----------
    path : `Path`
        A `meta_analysis.py` burden file.

    Returns
    -------
    burden : `pd.DataFrame` or `None`
        Rows with a finite beta and SE, plus `_OR`, `_LB` and `_UB`;
        `None` (logged) when the file does not exist.
    """
    if not path.exists():
        _LOGGER.info(f"{path} not found, skipped")
        return None
    burden = pd.read_csv(path, sep="\t", low_memory=False)
    beta = pd.to_numeric(burden[MetaColumns.BETA], errors="coerce")
    se = pd.to_numeric(burden[MetaColumns.SE], errors="coerce")
    usable = np.isfinite(beta) & np.isfinite(se)
    if not usable.all():
        _LOGGER.info(
            f"{path.name}: {int((~usable).sum())} rows without beta/SE"
        )
    burden = burden.loc[usable].copy()
    beta, se = beta[usable], se[usable]
    burden[_OR] = np.exp(beta)
    burden[_LB] = np.exp(beta - _Z_95 * se)
    burden[_UB] = np.exp(beta + _Z_95 * se)
    _LOGGER.info(f"{path.name}: {len(burden)} rows")
    return burden


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# drawing

def _clip_ci(data: pd.DataFrame, max_or: float) -> int:
    """Clip CI bounds to ``[1/max_or, max_or]``, in place.

    Parameters
    ----------
    data : `pd.DataFrame`
        With `_LB` and `_UB`.
    max_or : `float`
        Largest odds ratio shown.

    Returns
    -------
    n_clipped : `int`
        Rows with a clipped bound.
    """
    low, high = 1.0 / max_or, max_or
    clipped = (data[_LB] < low) | (data[_UB] > high)
    data[_LB] = data[_LB].clip(lower=low)
    data[_UB] = data[_UB].clip(upper=high)
    return int(clipped.sum())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_forest(
    data: pd.DataFrame,
    title: str,
    legend: list[Line2D],
    max_or: float,
) -> plt.Figure:
    """Draw a log-scale odds-ratio forest plot with plot_misc.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows with `_OR`, `_LB`, `_UB`, `_Y` (numeric, unique per row),
        `_MARKER`, `_COLOUR`, `_SIZE` and the gene column (y tick labels,
        one per gene).
    title : `str`
        Axes title.
    legend : `list[Line2D]`
        Legend handles.
    max_or : `float`
        Odds ratios and CI bounds are shown within ``[1/max_or, max_or]``.

    Returns
    -------
    figure : `plt.Figure`
    """
    data = data.copy()
    points_out = (data[_OR] < 1.0 / max_or) | (data[_OR] > max_or)
    if points_out.any():
        _LOGGER.warning(
            f"{title}: {int(points_out.sum())} estimates outside "
            f"[1/{max_or:g}, {max_or:g}] not shown"
        )
        data = data.loc[~points_out]
    n_clipped = _clip_ci(data, max_or)
    height = 1.0 + 0.28 * len(data)
    figure, ax = plt.subplots(figsize=(6.5, height))
    if len(data) < 2:
        # ForestPlot needs two rows to set its y margins
        for _, row in data.iterrows():
            ax.plot([row[_LB], row[_UB]], [row[_Y]] * 2, c="indianred")
            ax.scatter(row[_OR], row[_Y], marker=row[_MARKER], c=row[_COLOUR])
        ax.set_yticks(data[_Y], data[VariantListColumns.OUT_GENE])
    else:
        ForestPlot(
            data,
            x_col=_OR,
            y_col=_Y,
            lb_col=_LB,
            ub_col=_UB,
            g_col=VariantListColumns.OUT_GENE,
            ax=ax,
        ).plot(
            s_col=_MARKER,
            c_col=_COLOUR,
            s_size_col=_SIZE,
            ci_lwd=1.5,
            ci_colour="grey",
        )
    ax.set_xscale("log")
    ax.set_xlim(1.0 / max_or, max_or)
    ax.axvline(1.0, color="black", linestyle="--", linewidth=0.8, zorder=1)
    xlabel = "Odds ratio (95% CI), lower gene function"
    if n_clipped:
        xlabel += f"\n{n_clipped} CIs truncated at the axis limits"
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontsize=10)
    ax.legend(
        handles=legend,
        loc="upper left",
        bbox_to_anchor=(1.01, 1.0),
        frameon=False,
        fontsize=8,
    )
    figure.tight_layout()
    return figure


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _y_positions(data: pd.DataFrame, order: list[str]) -> pd.Series:
    """Give each row a y position: genes one after the other, a gap of one
    row between genes.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows sorted within gene in plotting order.
    order : `list[str]`
        Genes in plotting order.

    Returns
    -------
    y : `pd.Series`
        Float y per row, aligned to `data`.
    """
    y = pd.Series(np.nan, index=data.index)
    position = 0.0
    for gene in order:
        rows = data.index[data[VariantListColumns.OUT_GENE] == gene]
        y[rows] = position + np.arange(len(rows))
        position += len(rows) + 1
    return y


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_colours(studies: list[str]) -> dict[str, str]:
    """Assign a tab10 colour to each study.

    Parameters
    ----------
    studies : `list[str]`
        Study accessions.

    Returns
    -------
    colours : `dict[str, str]`
        Accession -> hex colour (cycling after 10 studies).
    """
    cmap = plt.get_cmap("tab10")
    return {
        study: to_hex(cmap(i % cmap.N))
        for i, study in enumerate(sorted(studies))
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save(figure: plt.Figure, stem: Path) -> None:
    """Save a figure as PDF and PNG, each written then moved into place.

    Parameters
    ----------
    figure : `plt.Figure`
        Figure to save; closed afterwards.
    stem : `Path`
        Output path without suffix.

    Returns
    -------
    `None`
    """
    stem.parent.mkdir(parents=True, exist_ok=True)
    for suffix in ("pdf", "png"):
        path = stem.with_name(f"{stem.name}.{suffix}")
        tmp = path.with_name(f"{path.name}.tmp")
        figure.savefig(tmp, format=suffix, dpi=_DPI, bbox_inches="tight")
        os.replace(tmp, path)
    plt.close(figure)
    _LOGGER.info(f"wrote {stem}.pdf/.png")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# figures

def forest_burden(
    burden: pd.DataFrame, label: str, out_dir: Path, max_or: float
) -> None:
    """Per outcome: pooled and per-study gene-burden odds ratios.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden` (pooled run, levels pooled and stratum).
    label : `str`
        Run label, used in titles and file names.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.

    Returns
    -------
    `None`
    """
    gene = VariantListColumns.OUT_GENE
    study = HarmonisedColumns.STUDY_ACCESSION
    is_study = burden[MetaColumns.LEVEL] == MetaLevel.STRATUM
    colours = _study_colours(
        sorted(set(burden.loc[is_study, study].dropna()))
    )
    for outcome, rows in burden.groupby(HarmonisedColumns.OUTCOME):
        rows = rows.copy()
        is_pooled = rows[MetaColumns.LEVEL] == MetaLevel.POOLED
        rows["_order"] = np.where(is_pooled, 0, 1)
        rows = rows.sort_values([gene, "_order", study], na_position="first")
        genes = list(dict.fromkeys(rows[gene]))
        rows[_Y] = _y_positions(rows, genes)
        rows[_MARKER] = np.where(
            is_pooled.loc[rows.index], _POOLED_MARKER, _STUDY_MARKER
        )
        rows[_COLOUR] = [
            _POOLED_COLOUR if pooled else colours[accession]
            for pooled, accession in zip(
                is_pooled.loc[rows.index], rows[study]
            )
        ]
        rows[_SIZE] = np.where(is_pooled.loc[rows.index], 50, 25)
        shown = sorted(set(rows.loc[~is_pooled.loc[rows.index], study]))
        legend = [
            Line2D(
                [],
                [],
                marker=_POOLED_MARKER,
                color=_POOLED_COLOUR,
                linestyle="",
                label="pooled (IVW)",
            )
        ] + [
            Line2D(
                [],
                [],
                marker=_STUDY_MARKER,
                color=colours[accession],
                linestyle="",
                label=accession,
            )
            for accession in shown
        ]
        figure = draw_forest(rows, f"{outcome} ({label})", legend, max_or)
        save(figure, out_dir / f"forest_burden_{label}_{outcome}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def forest_apoe(
    burden: pd.DataFrame,
    strata: pd.DataFrame,
    label: str,
    out_dir: Path,
    max_or: float,
) -> None:
    """Per outcome: pooled gene-burden odds ratio overall and per stratum.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`, the pooled run (all APOE genotypes).
    strata : `pd.DataFrame`
        From `load_burden`, the ``_apoe_strata`` run.
    label : `str`
        Run label, used in titles and file names.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.

    Returns
    -------
    `None`
    """
    gene = VariantListColumns.OUT_GENE
    stratum = MetaColumns.APOE_STRATUM
    overall = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
    overall[stratum] = ApoeStratum.ALL
    per_stratum = strata[strata[MetaColumns.LEVEL] == MetaLevel.POOLED]
    rows_all = pd.concat([overall, per_stratum], ignore_index=True)
    rank = {name: i for i, name in enumerate(_STRATUM_ORDER)}
    rows_all["_order"] = rows_all[stratum].map(rank)
    cmap = plt.get_cmap("tab10")
    colours = {
        name: to_hex(
            _POOLED_COLOUR if name == ApoeStratum.ALL else cmap(i)
        )
        for i, name in enumerate(_STRATUM_ORDER)
    }
    for outcome, rows in rows_all.groupby(HarmonisedColumns.OUTCOME):
        has_strata = rows[stratum] != ApoeStratum.ALL
        if not has_strata.any():
            _LOGGER.info(f"{outcome}: no APOE strata, forest skipped")
            continue
        rows = rows.sort_values([gene, "_order"]).copy()
        genes = list(dict.fromkeys(rows[gene]))
        rows[_Y] = _y_positions(rows, genes)
        rows[_MARKER] = np.where(
            rows[stratum] == ApoeStratum.ALL, _POOLED_MARKER, _STUDY_MARKER
        )
        rows[_COLOUR] = rows[stratum].map(colours)
        rows[_SIZE] = 35
        legend = [
            Line2D(
                [],
                [],
                marker=_POOLED_MARKER if name == ApoeStratum.ALL
                else _STUDY_MARKER,
                color=colours[name],
                linestyle="",
                label="all genotypes" if name == ApoeStratum.ALL else name,
            )
            for name in _STRATUM_ORDER
            if name in set(rows[stratum])
        ]
        figure = draw_forest(
            rows, f"{outcome} by APOE stratum ({label})", legend, max_or
        )
        save(figure, out_dir / f"forest_apoe_{label}_{outcome}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def burden_heatmap(burden: pd.DataFrame, label: str, out_dir: Path) -> None:
    """Pooled gene-burden log odds ratio per gene and outcome.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`.
    label : `str`
        Run label, used in the title and file name.
    out_dir : `Path`
        Output directory.

    Returns
    -------
    `None`
    """
    gene = VariantListColumns.OUT_GENE
    outcome = HarmonisedColumns.OUTCOME
    pooled = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED]
    beta = pooled.pivot(index=gene, columns=outcome, values=MetaColumns.BETA)
    p = pooled.pivot(index=gene, columns=outcome, values=MetaColumns.P)
    p = p.reindex_like(beta)
    n_cells = int(beta.notna().sum().sum())
    bonferroni = _P_NOMINAL / max(n_cells, 1)
    stars = pd.DataFrame("", index=beta.index, columns=beta.columns)
    stars = stars.mask(p < _P_NOMINAL, "*").mask(p < bonferroni, "**")
    limit = float(np.nanmax(np.abs(beta.to_numpy()))) if n_cells else 1.0
    figure, ax = plt.subplots(
        figsize=(3.0 + 1.1 * beta.shape[1], 2.0 + 0.5 * beta.shape[0])
    )
    im, _ = heatmap(
        beta.to_numpy(dtype=float),
        row_labels=list(beta.index),
        col_labels=[name.replace("_", " ") for name in beta.columns],
        ax=ax,
        cbar_bool=True,
        cbar_label="pooled log odds ratio",
        cmap="RdBu_r",
        vmin=-limit,
        vmax=limit,
    )
    with warnings.catch_warnings():
        # empty (NaN) cells are masked; matplotlib warns per masked cell
        warnings.simplefilter("ignore", UserWarning)
        annotate_heatmap(im, data=stars, threshold=limit / 2, fontsize=12)
    ax.set_title(f"Gene burden ({label})", fontsize=10)
    figure.tight_layout()
    figure.text(
        0.01,
        0.01,
        f"* p < {_P_NOMINAL:g}; ** p < {bonferroni:.1e} (Bonferroni, "
        f"{n_cells} cells); blank: no estimate",
        fontsize=7,
    )
    save(figure, out_dir / f"heatmap_burden_{label}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def figures(
    ancestry: str,
    forest_label: str | None,
    heatmap_label: str | None,
    out_dir: Path,
    max_or: float,
) -> None:
    """Draw every figure whose input exists.

    Parameters
    ----------
    ancestry : `str`
        `Ancestry` code of the runs.
    forest_label : `str` or `None`
        Label of the run for the forest plots; `None` skips them.
    heatmap_label : `str` or `None`
        Label of the run for the heatmap; `None` skips it.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Forest-plot axis limit.

    Returns
    -------
    `None`
    """
    if forest_label:
        burden = load_burden(burden_path(ancestry, forest_label))
        if burden is not None:
            forest_burden(burden, forest_label, out_dir, max_or)
            strata = load_burden(
                burden_path(
                    ancestry, forest_label, f"_{Constants.APOE_STRATA_LABEL}"
                )
            )
            if strata is not None:
                forest_apoe(burden, strata, forest_label, out_dir, max_or)
    if heatmap_label:
        burden = load_burden(burden_path(ancestry, heatmap_label))
        if burden is not None:
            burden_heatmap(burden, heatmap_label, out_dir)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Forest plots and heatmap of the gene-burden results."
    )
    parser.add_argument(
        "--ancestry",
        type=str.upper,
        default=MetaColumns.DEFAULT_ANCESTRY,
        help="ancestry code of the runs (default: %(default)s)",
    )
    parser.add_argument(
        "--forest-label",
        help="meta_analysis.py --label of the run for the forest plots",
    )
    parser.add_argument(
        "--heatmap-label",
        help="meta_analysis.py --label of the run for the heatmap",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Paths.RESULTS_FIGURES,
        help="output directory (default: %(default)s)",
    )
    parser.add_argument(
        "--max-or",
        type=float,
        default=20.0,
        help="forest-plot odds-ratio axis limit (default: %(default)s)",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    args = parser.parse_args()
    if not (args.forest_label or args.heatmap_label):
        parser.error("give --forest-label and/or --heatmap-label")
    if args.max_or <= 1:
        parser.error("--max-or must be > 1")
    return args


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(message)s"
    )
    figures(
        args.ancestry,
        args.forest_label,
        args.heatmap_label,
        args.out_dir,
        args.max_or,
    )


if __name__ == "__main__":
    main()
