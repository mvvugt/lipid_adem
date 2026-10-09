#!/usr/bin/env python3
"""
Figures of the gene-burden meta-analysis (`meta_analysis.py` burden files).

Run locally in the `plot-misc` env on burden files copied from Myriad
into `results/output/`. Writes PDF and PNG files to `results/figures/`:

- ``forest_burden_<label>_<outcome>``: per gene the pooled odds ratio
  and each study's own estimate, 95% CI, with side tables (study,
  OR (95% CI), p-value);
- ``forest_apoe_<label>_<outcome>``: per gene the pooled odds ratio over
  all APOE genotypes and per APOE stratum; skipped (logged) until the
  ``_apoe_strata`` burden file exists;
- ``heatmap_burden_<label>``: pooled log odds ratio per gene and outcome;
- ``forest_sources_<label>_<outcome>``: per gene each source's estimate
  (Thomassen, as the IVW of its APOE strata; FinnGen; UK Biobank, each
  over the variants it contributes) and the pooled one last; for a
  `meta_analysis.py --prefer-groups` run;
- ``forest_pooled_<label>``: the pooled estimates of that run, per gene
  one row per outcome;
- ``forest_apoe_genotype_<population>``: UK Biobank marvel association
  of each APOE genotype vs ε3/ε3 (`config/marvel_apoe_task.cnf`), per
  outcome one row per genotype; read from the loose marvel files of the
  `FileNames.MARVEL_APOE_TASKS` outdirs copied into `results/`.

Layout follows `cox_forest.py` (small cm-sized panels, black CIs, dashed
OR = 1 line, shaded gene bands, plot_misc side tables). Significance is
shown by marker shape: circle p >= 0.05, square p < 0.05, diamond p below
the Bonferroni threshold 0.05 / (genes x outcomes with a pooled estimate
in the run's burden file). The heatmap uses the same glyphs.

Only `project_constants` is imported from the pipeline; `functions.py`
needs the Myriad biomed-api env.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import logging
import math
import os
import re
import warnings
from pathlib import Path

import matplotlib
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from plot_misc.forest import ForestPlot, plot_table
from plot_misc.heatmap import annotate_heatmap, heatmap

from project_constants import (
    ApoeStratum,
    Constants,
    FileNames,
    HarmonisedColumns,
    MarvelColumns,
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
_Y: str = "y_axis"
_MARKER: str = "marker"
_COLOUR: str = "colour"
_SIZE: str = "size"
_ROW_NAME: str = "row_name"
_OR_TEXT: str = "or_text"
_P_TEXT: str = "p_text"
# colours: pooled estimate vs single study / stratum
_POOLED_COLOUR: str = "black"
_STUDY_COLOUR: str = "#bdbdbd"
_POOLED_SIZE: float = 14
_STUDY_SIZE: float = 9
# significance -> marker shape, and the matching heatmap glyph
_MARKER_NS: str = "o"
_MARKER_NOMINAL: str = "s"
_MARKER_STRICT: str = "D"
_GLYPH_NOMINAL: str = "■"
_GLYPH_STRICT: str = "◆"
_P_NOMINAL: float = 0.05
# APOE strata in plotting order, `ApoeStratum.ALL` = all genotypes
_STRATUM_ORDER: tuple[str, ...] = (
    ApoeStratum.ALL,
    ApoeStratum.E44,
    ApoeStratum.E43,
    ApoeStratum.E33,
    ApoeStratum.E22_E32,
)
_STRATUM_NAMES: dict[str, str] = {
    ApoeStratum.ALL: "All genotypes",
    ApoeStratum.E44: "ε4/ε4",
    ApoeStratum.E43: "ε4/ε3",
    ApoeStratum.E33: "ε3/ε3",
    ApoeStratum.E22_E32: "ε2/ε2 + ε3/ε2",
}
_OUTCOME_NAMES: dict[str, str] = {
    "all_cause_dementia": "All-cause dementia",
    "alzheimers_dementia": "Alzheimer's disease",
    "vascular_dementia": "Vascular dementia",
    "frontotemporal_dementia": "Frontotemporal dementia",
    "ascvd": "ASCVD",
}
# APOE genotype figure: marvel variable -> outcome key, in plotting order
_APOE_GENOTYPE_OUTCOMES: dict[str, str] = {
    **Constants.MARVEL_UKB_OUTCOMES,
    "ascvd_ii": "ascvd",
}
# genotypes vs the reference (`Constants.UKB_APOE_REFERENCE`), in
# plotting order: ε2 dose down, then ε4 dose up
_GENOTYPE_NAMES: dict[str, str] = {
    "e2e2": "ε2/ε2",
    "e2e3": "ε2/ε3",
    "e3e4": "ε3/ε4",
    "e2e4": "ε2/ε4",
    "e4e4": "ε4/ε4",
}
# name of `Constants.UKB_APOE_REFERENCE`
_REFERENCE_GENOTYPE_NAME: str = "ε3/ε3"
_APOE_GENOTYPE_MODEL: str = "model_3"
# marvel `subset` (`FileNames.MARVEL_APOE_TASKS`) -> population label
_SUBSET_POPULATIONS: dict[str, str] = {
    "all": "all",
    "eur_overall": "EUR",
}
_POPULATION_NAMES: dict[str, str] = {
    "all": "UK Biobank, all participants",
    "EUR": "UK Biobank, EUR",
}
# columns added to the APOE genotype rows
_GENOTYPE: str = "genotype"
_POPULATION: str = "population"
_OUTCOME_GROUP: str = "outcome_name"
# marvel results column with the error of a skipped test
_MARVEL_REMARKS: str = "remarks"
# dummy-coded marvel exposure of the genotype vs `strata_ref`
_APOE_EXPOSURE_RE: re.Pattern = re.compile(
    rf"^{re.escape(Constants.UKB_APOE_COLUMN)}: (?P<genotype>\S+)$"
)
_UKB_PREFIX: str = "marvel_ukb_"
_FINNGEN_NAME: str = "FinnGen R13"
_UKB_NAME: str = "UK Biobank"
_POOLED_NAME: str = "Pooled (IVW)"
# x-axis tick candidates (odds ratio), coarse first
_TICKS_COARSE: tuple[float, ...] = (0.05, 0.1, 0.25, 0.5, 1, 2, 4, 10, 20)
_TICKS_FINE: tuple[float, ...] = (0.5, 0.75, 1, 1.5, 2)
_TICKS_FINER: tuple[float, ...] = (0.8, 0.9, 1, 1.1, 1.2)
# sizes, as in cox_forest.py (points, cm)
_CM: float = 1 / 2.54
_TITLE_SIZE: float = 3.5
_LAB_SIZE: float = 3
_LWD: float = 0.5
_AX_LAB_SZ: float = 2.7
_STEXT_SIZE: float = 2.7
_WIDTH_CM: float = 9.0
_CM_PER_Y: float = 0.12
_DPI: int = 300


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
        Rows with a finite beta and SE, plus `_OR`, `_LB`, `_UB`,
        `_OR_TEXT` and `_P_TEXT`; `None` (logged) when the file does not
        exist.
    """
    if not path.exists():
        _LOGGER.info(f"{path} not found, skipped")
        return None
    burden = pd.read_csv(path, sep="\t", low_memory=False)
    is_excluded = burden[VariantListColumns.OUT_GENE].isin(
        Constants.EXCLUDED_GENES
    )
    if is_excluded.any():
        _LOGGER.info(
            f"{path.name}: {int(is_excluded.sum())} rows of excluded "
            f"gene(s) {', '.join(Constants.EXCLUDED_GENES)} dropped"
        )
        burden = burden.loc[~is_excluded]
    beta =pd.to_numeric(burden[MetaColumns.BETA], errors="coerce")
    se = pd.to_numeric(burden[MetaColumns.SE], errors="coerce")
    usable = np.isfinite(beta) & np.isfinite(se)
    if not usable.all():
        _LOGGER.info(
            f"{path.name}: {int((~usable).sum())} rows without beta/SE"
        )
    burden = burden.loc[usable].copy()
    burden[MetaColumns.BETA] = beta[usable]
    burden[MetaColumns.SE] = se[usable]
    burden[MetaColumns.P] = pd.to_numeric(
        burden[MetaColumns.P], errors="coerce"
    )
    burden = _add_or(burden)
    _LOGGER.info(f"{path.name}: {len(burden)} rows")
    return burden


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _add_or(burden: pd.DataFrame) -> pd.DataFrame:
    """Add the odds ratio, its 95% CI and the side-table texts.

    Parameters
    ----------
    burden : `pd.DataFrame`
        Rows with a finite numeric beta and SE, and a numeric p-value.

    Returns
    -------
    burden : `pd.DataFrame`
        Copy with `_OR`, `_LB`, `_UB`, `_OR_TEXT` and `_P_TEXT`.
    """
    burden = burden.copy()
    beta, se = burden[MetaColumns.BETA], burden[MetaColumns.SE]
    burden[_OR] = np.exp(beta)
    burden[_LB] = np.exp(beta - _Z_95 * se)
    burden[_UB] = np.exp(beta + _Z_95 * se)
    # text before any axis clipping, so the tables show the real CI
    burden[_OR_TEXT] = [
        f"{point:.2f} ({low:.2f}; {high:.2f})"
        for point, low, high in zip(burden[_OR], burden[_LB], burden[_UB])
    ]
    burden[_P_TEXT] = burden[MetaColumns.P].map(_format_p)
    return burden


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _format_p(p: float) -> str:
    """Format a p-value for a side table.

    Parameters
    ----------
    p : `float`
        P-value, may be NaN.

    Returns
    -------
    text : `str`
        ``"0.034"`` style from 0.001 up, ``"1.2e-04"`` below,
        ``"< 1e-300"`` for 0; empty for NaN.
    """
    if not np.isfinite(p):
        return ""
    if p == 0:
        # below double precision
        return "< 1e-300"
    if p < 0.001:
        return f"{p:.1e}"
    return f"{p:.3f}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _genotype_of_exposure(exposure: str) -> str | None:
    """APOE genotype of a dummy-coded marvel exposure label.

    Parameters
    ----------
    exposure : `str`
        marvel `Exposure`, e.g. ``"genotype: e4e4"``.

    Returns
    -------
    genotype : `str` or `None`
        One of `Constants.APOE_GENOTYPES`, e.g. ``"e4e4"``; `None` for
        `Constants.APOE_MISSING_VALUES` (e.g. ``"genotype: Unknown"``, its
        own dummy term in marvel) and any other exposure (intercept,
        covariates).

    Raises
    ------
    ValueError
        If the genotype is neither in `Constants.APOE_GENOTYPES` nor in
        `Constants.APOE_MISSING_VALUES`.
    """
    match = _APOE_EXPOSURE_RE.match(str(exposure))
    if match is None:
        return None
    genotype = match.group("genotype")
    if genotype in Constants.APOE_MISSING_VALUES:
        return None
    if genotype not in Constants.APOE_GENOTYPES:
        raise ValueError(
            f"{exposure!r}: {genotype!r} not in Constants.APOE_GENOTYPES "
            f"{Constants.APOE_GENOTYPES}"
        )
    return genotype


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_apoe_genotype(
    task_file: Path = FileNames.MARVEL_APOE_TASKS,
    results_dir: Path = Paths.HERE / "results",
    model: str = _APOE_GENOTYPE_MODEL,
) -> pd.DataFrame | None:
    """Read the marvel APOE genotype results and add the odds ratios.

    Parameters
    ----------
    task_file : `Path`, optional, default: `FileNames.MARVEL_APOE_TASKS`
        Job-array file of the runs; its ``outdir`` (Myriad path) and
        ``subset`` columns give the result directory and population.
    results_dir : `Path`, optional, default: ``results/``
        Local directory holding copies of the outdirs (same base names).
    model : `str`, optional, default: `_APOE_GENOTYPE_MODEL`
        marvel `Model name` to keep.

    Returns
    -------
    results : `pd.DataFrame` or `None`
        One row per population, outcome and genotype (reference left
        out) with a finite estimate and SE, with `_POPULATION`,
        `_GENOTYPE`, `HarmonisedColumns.OUTCOME`, `MetaColumns.BETA`/
        `SE`/`P`, `_OR`, `_LB`, `_UB`, `_OR_TEXT` and `_P_TEXT`; `None`
        (logged) when no result files are found.

    Raises
    ------
    ValueError
        If a subset has no population label, a marvel column is missing,
        or a population has two rows for one outcome and genotype (e.g.
        two stratifications).
    """
    tasks = pd.read_csv(task_file, sep="\t", dtype=str)
    unknown = sorted(set(tasks["subset"]) - set(_SUBSET_POPULATIONS))
    if unknown:
        raise ValueError(
            f"{task_file}: subset(s) {unknown} not in _SUBSET_POPULATIONS"
        )
    required = [
        MarvelColumns.MODEL_NAME,
        MarvelColumns.VARIABLE,
        MarvelColumns.EXPOSURE,
        MarvelColumns.EXPOSED,
        MarvelColumns.ESTIMATE,
        MarvelColumns.SE,
        MarvelColumns.P_VALUE,
    ]
    frames = []
    for row in tasks.itertuples(index=False):
        outdir = results_dir / Path(row.outdir).name
        files = sorted(outdir.glob(FileNames.MARVEL_LOOSE_GLOB))
        if not files:
            _LOGGER.info(f"{outdir}: no marvel result files, skipped")
            continue
        for path in files:
            frame = pd.read_csv(path, sep="\t", low_memory=False)
            missing = [col for col in required if col not in frame.columns]
            if missing:
                raise ValueError(f"{path}: missing marvel column(s) {missing}")
            frame[_POPULATION] = _SUBSET_POPULATIONS[row.subset]
            frames.append(frame)
        _LOGGER.info(f"{outdir}: {len(files)} marvel result files")
    if not frames:
        return None
    results = pd.concat(frames, ignore_index=True)
    # skipped tests (marvel exits 0 anyway): one row per outcome and model
    # with the error in `remarks` and no estimate
    if _MARVEL_REMARKS in results.columns:
        remarks = results[_MARVEL_REMARKS].dropna()
        for remark, n in remarks.value_counts().items():
            _LOGGER.warning(
                f"APOE genotype: {n} skipped marvel tests: {remark}"
            )
    results[_GENOTYPE] = results[MarvelColumns.EXPOSURE].map(
        _genotype_of_exposure
    )
    keep = (
        (results[MarvelColumns.MODEL_NAME] == model)
        & results[MarvelColumns.VARIABLE].isin(_APOE_GENOTYPE_OUTCOMES)
        & results[_GENOTYPE].isin(_GENOTYPE_NAMES)
    )
    results = results.loc[keep].copy()
    results[HarmonisedColumns.OUTCOME] = results[MarvelColumns.VARIABLE].map(
        _APOE_GENOTYPE_OUTCOMES
    )
    results[MetaColumns.BETA] = pd.to_numeric(
        results[MarvelColumns.ESTIMATE], errors="coerce"
    )
    results[MetaColumns.SE] = pd.to_numeric(
        results[MarvelColumns.SE], errors="coerce"
    )
    results[MetaColumns.P] = pd.to_numeric(
        results[MarvelColumns.P_VALUE], errors="coerce"
    )
    results[MarvelColumns.EXPOSED] = pd.to_numeric(
        results[MarvelColumns.EXPOSED], errors="coerce"
    )
    usable = np.isfinite(results[MetaColumns.BETA]) & np.isfinite(
        results[MetaColumns.SE]
    )
    if not usable.all():
        _LOGGER.info(
            f"APOE genotype: {int((~usable).sum())} rows without "
            "estimate/SE dropped"
        )
    results = results.loc[usable]
    key = [_POPULATION, HarmonisedColumns.OUTCOME, _GENOTYPE]
    repeats = results.duplicated(key, keep=False)
    if repeats.any():
        raise ValueError(
            f"APOE genotype: {int(repeats.sum())} rows share a population, "
            f"outcome and genotype ({model}):\n"
            + results.loc[repeats, key].to_string(index=False)
        )
    if results.empty:
        _LOGGER.info(f"APOE genotype: no {model} rows for the outcomes")
        return None
    results = _add_or(results)
    _LOGGER.info(f"APOE genotype ({model}): {len(results)} rows")
    return results


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def study_names() -> dict[str, str]:
    """Readable names of the APOE-stratum studies and FinnGen phenocodes.

    Returns
    -------
    names : `dict[str, str]`
        Accession -> name: ``"Thomassen ε4/ε4"`` from
        `FileNames.APOE_STRATA`, `_FINNGEN_NAME` for every phenocode in
        `FileNames.FINNGEN_MANIFEST`. UKB accessions are named in
        `_study_name`.
    """
    names: dict[str, str] = {}
    if FileNames.FINNGEN_MANIFEST.exists():
        manifest = pd.read_csv(
            FileNames.FINNGEN_MANIFEST, sep="\t", usecols=["phenocode"]
        )
        names.update(dict.fromkeys(manifest["phenocode"], _FINNGEN_NAME))
    if FileNames.APOE_STRATA.exists():
        strata = pd.read_csv(FileNames.APOE_STRATA, sep="\t")
        for _, row in strata.iterrows():
            stratum = _STRATUM_NAMES.get(
                row[MetaColumns.APOE_STRATUM], row[MetaColumns.APOE_STRATUM]
            )
            names[row[HarmonisedColumns.STUDY_ACCESSION]] = (
                f"{str(row[MetaColumns.STUDY_GROUP]).capitalize()} {stratum}"
            )
    return names


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_name(accession: str, names: dict[str, str]) -> str:
    """Readable name of one study.

    Parameters
    ----------
    accession : `str`
        Study accession of a burden row.
    names : `dict[str, str]`
        From `study_names`.

    Returns
    -------
    name : `str`
        `_UKB_NAME` for marvel UKB accessions, else the `names` entry,
        else the accession itself.
    """
    if accession.startswith(_UKB_PREFIX):
        return _UKB_NAME
    return names.get(accession, accession)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def source_names() -> dict[str, str]:
    """Readable source (study group) name per accession.

    Returns
    -------
    names : `dict[str, str]`
        Accession -> name: the capitalised `study_group` of
        `FileNames.APOE_STRATA` (e.g. all Thomassen strata ->
        ``"Thomassen"``), `_FINNGEN_NAME` for every FinnGen phenocode.
        UKB accessions are named in `_study_name`.
    """
    names = {
        accession: name
        for accession, name in study_names().items()
        if name == _FINNGEN_NAME
    }
    if FileNames.APOE_STRATA.exists():
        strata = pd.read_csv(FileNames.APOE_STRATA, sep="\t")
        names.update(
            zip(
                strata[HarmonisedColumns.STUDY_ACCESSION],
                strata[MetaColumns.STUDY_GROUP].astype(str).str.capitalize(),
            )
        )
    return names


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def source_rows(per_study: pd.DataFrame) -> pd.DataFrame:
    """One estimate per gene, outcome and source.

    A source with several studies (the Thomassen APOE strata) is the
    fixed-effect IVW of their estimates, the same pooling as
    `meta_analysis.py`.

    Parameters
    ----------
    per_study : `pd.DataFrame`
        Burden rows of level ``stratum`` (one per gene, outcome and study),
        from `load_burden`.

    Returns
    -------
    sources : `pd.DataFrame`
        Gene, outcome, `_ROW_NAME` (source name), beta, SE, p and the
        `_add_or` columns.
    """
    gene = VariantListColumns.OUT_GENE
    outcome = HarmonisedColumns.OUTCOME
    names = source_names()
    rows = per_study.copy()
    rows[_ROW_NAME] = [
        _study_name(str(accession), names)
        for accession in rows[HarmonisedColumns.STUDY_ACCESSION]
    ]
    rows["_weight"] = 1.0 / rows[MetaColumns.SE] ** 2
    rows["_weighted"] = rows["_weight"] * rows[MetaColumns.BETA]
    sums = (
        rows.groupby([gene, outcome, _ROW_NAME], sort=False)[
            ["_weight", "_weighted"]
        ]
        .sum()
        .reset_index()
    )
    sums[MetaColumns.BETA] = sums["_weighted"] / sums["_weight"]
    sums[MetaColumns.SE] = 1.0 / np.sqrt(sums["_weight"])
    z = (sums[MetaColumns.BETA] / sums[MetaColumns.SE]).abs()
    sums[MetaColumns.P] = [math.erfc(value / math.sqrt(2)) for value in z]
    return _add_or(sums.drop(columns=["_weight", "_weighted"]))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _outcome_name(outcome: str) -> str:
    """Readable outcome name.

    Parameters
    ----------
    outcome : `str`
        `outcome` value of a burden row.

    Returns
    -------
    name : `str`
        From `_OUTCOME_NAMES`, else underscores replaced by spaces.
    """
    return _OUTCOME_NAMES.get(outcome, outcome.replace("_", " "))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def strict_threshold(burden: pd.DataFrame) -> tuple[float, int]:
    """Bonferroni threshold over the pooled gene x outcome estimates.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`, the run's main burden file.

    Returns
    -------
    threshold : `float`
        `_P_NOMINAL` / number of tests.
    n_tests : `int`
        Pooled rows with a finite p-value (one per gene and outcome).
    """
    pooled = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED]
    n_tests = int(np.isfinite(pooled[MetaColumns.P]).sum())
    return _P_NOMINAL / max(n_tests, 1), n_tests


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# drawing

def _significance_marker(p: pd.Series, strict: float) -> np.ndarray:
    """Marker shape per row from its p-value.

    Parameters
    ----------
    p : `pd.Series`
        P-values.
    strict : `float`
        Bonferroni threshold.

    Returns
    -------
    markers : `np.ndarray`
        `_MARKER_STRICT`, `_MARKER_NOMINAL` or `_MARKER_NS`.
    """
    return np.select(
        [p < strict, p < _P_NOMINAL],
        [_MARKER_STRICT, _MARKER_NOMINAL],
        default=_MARKER_NS,
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
def _x_axis(data: pd.DataFrame) -> tuple[tuple[float, float], list[float]]:
    """Log x limits and ticks that fit the (clipped) CIs.

    Parameters
    ----------
    data : `pd.DataFrame`
        With `_LB` and `_UB`.

    Returns
    -------
    limits : `tuple[float, float]`
        Lowest CI bound / 1.15 and highest * 1.15, always around 1.
    ticks : `list[float]`
        The first of `_TICKS_COARSE`, `_TICKS_FINE`, `_TICKS_FINER` with
        at least three ticks within the limits (else `_TICKS_FINER`).
    """
    low = min(float(data[_LB].min()), 1.0) / 1.15
    high = max(float(data[_UB].max()), 1.0) * 1.15
    for candidates in (_TICKS_COARSE, _TICKS_FINE, _TICKS_FINER):
        ticks = [t for t in candidates if low <= t <= high]
        if len(ticks) >= 3:
            break
    return (low, high), ticks


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _significance_legend(strict: float, n_tests: int) -> list[Line2D]:
    """Legend handles of the three marker shapes.

    Parameters
    ----------
    strict : `float`
        Bonferroni threshold.
    n_tests : `int`
        Number of tests behind `strict`.

    Returns
    -------
    handles : `list[Line2D]`
    """
    labels = (
        (_MARKER_NS, f"p ≥ {_P_NOMINAL:g}"),
        (_MARKER_NOMINAL, f"p < {_P_NOMINAL:g}"),
        (
            _MARKER_STRICT,
            f"p < {strict:.1e} (Bonferroni, {n_tests} tests)",
        ),
    )
    return [
        Line2D(
            [0],
            [0],
            marker=marker,
            color=_POOLED_COLOUR,
            markeredgecolor="black",
            markeredgewidth=0.3,
            markersize=2.5,
            lw=0,
            label=label,
        )
        for marker, label in labels
    ]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _plot_points(
    data: pd.DataFrame,
    ax: plt.Axes,
    ylim: tuple,
    group_col: str = VariantListColumns.OUT_GENE,
) -> dict:
    """Draw points and CIs per group, shaded group bands.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows with `_OR`, `_LB`, `_UB`, `_Y`, `_MARKER`, `_COLOUR`,
        `_SIZE` and `group_col`.
    ax : `plt.Axes`
        Forest axes.
    ylim : `tuple`
        Y limits (before inversion).
    group_col : `str`, optional, default: `VariantListColumns.OUT_GENE`
        Column of the groups (y tick labels, one per group).

    Returns
    -------
    span : `dict`
        `ForestPlot.span_dict`, for the side tables; empty for one row.
    """
    gene = group_col
    scatter_kwargs = {"edgecolors": "black", "linewidth": 0.3}
    ci_kwargs = {
        "zorder": 1,
        "solid_capstyle": "round",
        "linestyle": "-",
    }
    if len(data) < 2:
        # ForestPlot needs two rows to set its y margins
        for _, row in data.iterrows():
            ax.plot(
                [row[_LB], row[_UB]],
                [row[_Y]] * 2,
                c="black",
                linewidth=_LWD,
                **ci_kwargs,
            )
            ax.scatter(
                row[_OR],
                row[_Y],
                marker=row[_MARKER],
                c=row[_COLOUR],
                s=row[_SIZE],
                zorder=2,
                **scatter_kwargs,
            )
        ax.set_yticks(data[_Y], data[gene])
        ax.set_ylim(ylim)
        ax.invert_yaxis()
        return {}
    forest = ForestPlot(
        data,
        x_col=_OR,
        y_col=_Y,
        lb_col=_LB,
        ub_col=_UB,
        g_col=gene,
        ax=ax,
    )
    forest.plot(
        s_col=_MARKER,
        c_col=_COLOUR,
        s_size_col=_SIZE,
        ci_colour="black",
        ci_lwd=_LWD,
        span=True,
        ylim=ylim,
        kwargs_scatter_dict=scatter_kwargs,
        kwargs_plot_ci_dict=ci_kwargs,
    )
    return forest.span_dict


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_forest(
    data: pd.DataFrame,
    title: str,
    row_header: str,
    legend: list[Line2D],
    max_or: float,
    group_col: str = VariantListColumns.OUT_GENE,
    italic_groups: bool = True,
) -> plt.Figure:
    """Draw a log-scale odds-ratio forest plot with side tables.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows sorted in plotting order with `_OR`, `_LB`, `_UB`,
        `_MARKER`, `_COLOUR`, `_SIZE`, `_ROW_NAME`, `_OR_TEXT`, `_P_TEXT`
        and `group_col` (y tick labels, one per group).
    title : `str`
        Panel title.
    row_header : `str`
        Header of the `_ROW_NAME` table, e.g. ``"Study"``.
    legend : `list[Line2D]`
        Legend handles (marker shapes).
    max_or : `float`
        Odds ratios and CI bounds are shown within ``[1/max_or, max_or]``.
    group_col : `str`, optional, default: `VariantListColumns.OUT_GENE`
        Column of the groups.
    italic_groups : `bool`, optional, default: `True`
        Italic y tick labels (gene names).

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
    data = data.reset_index(drop=True)
    data = _set_y(data, group_col)
    ylim = (data[_Y].min() - 3, data[_Y].max() + 3)
    height_cm = 1.6 + _CM_PER_Y * (ylim[1] - ylim[0])
    matplotlib.rcParams["axes.linewidth"] = _LWD
    figure = plt.figure(figsize=(_WIDTH_CM * _CM, height_cm * _CM))
    grid = gridspec.GridSpec(
        nrows=1,
        ncols=4,
        width_ratios=[1.3, 0.7, 0.8, 0.35],
        figure=figure,
        wspace=0.0,
        bottom=1.0 / height_cm,
        top=1 - 0.35 / height_cm,
    )
    ax = figure.add_subplot(grid[0])
    ax.set_xscale("log")
    ax.set_zorder(1)
    span = _plot_points(data, ax, ylim, group_col)
    limits, ticks = _x_axis(data)
    ax.set_xlim(limits)
    ax.axvline(1, linewidth=_LWD, linestyle="--", c="black", zorder=0.5)
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%g"))
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.tick_params(
        axis="both",
        which="minor",
        bottom=False,
        labelsize=_AX_LAB_SZ,
        width=_LWD,
    )
    ax.tick_params(axis="both", labelsize=_AX_LAB_SZ, width=_LWD)
    if italic_groups:
        for label in ax.get_yticklabels():
            label.set_fontstyle("italic")
    xlabel = "Odds ratio (95% CI)"
    if n_clipped:
        xlabel += f"\n{n_clipped} CIs truncated at {1 / max_or:g}-{max_or:g}"
    ax.set_xlabel(xlabel, fontsize=_LAB_SIZE)
    ax.set_title(
        title, fontweight="bold", fontsize=_TITLE_SIZE, loc="left", pad=6
    )
    tables = (
        (_ROW_NAME, row_header, "left", 0.05),
        (_OR_TEXT, "OR (95% CI)", "center", 0.5),
        (_P_TEXT, "P-value", "center", 0.5),
    )
    for i, (column, header, align, xloc) in enumerate(tables, start=1):
        table_ax = figure.add_subplot(grid[i])
        table_ax.set_ylim(ax.get_ylim())
        table_ax.set_zorder(1 - 0.1 * i)
        plot_table(
            data,
            ax=table_ax,
            string_col=column,
            y_col=_Y,
            annoteheader=header,
            xloc=xloc,
            xloc_header=xloc,
            halignment_text=align,
            halignment_header=align,
            size_text=_STEXT_SIZE,
            size_header=_STEXT_SIZE,
            negative_padding=1,
            span=span or None,
        )
    figure.legend(
        handles=legend,
        loc="lower left",
        bbox_to_anchor=(0.02, 0.0),
        ncol=3,
        frameon=False,
        fontsize=_STEXT_SIZE,
        handletextpad=0.2,
        columnspacing=1.0,
    )
    return figure


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _set_y(
    data: pd.DataFrame, group_col: str = VariantListColumns.OUT_GENE
) -> pd.DataFrame:
    """Y coordinates: rows 2 apart within a group, 4 between groups.

    Parameters
    ----------
    data : `pd.DataFrame`
        Rows sorted in plotting order, unique index.
    group_col : `str`, optional, default: `VariantListColumns.OUT_GENE`
        Column of the groups (genes).

    Returns
    -------
    data : `pd.DataFrame`
        Copy with `_Y`.
    """
    y = pd.Series(np.nan, index=data.index)
    position = 1.0
    for gene in dict.fromkeys(data[group_col]):
        rows = data.index[data[group_col] == gene]
        y[rows] = position + 2 * np.arange(len(rows))
        position = y[rows].max() + 4
    data = data.copy()
    data[_Y] = y
    return data


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
    burden: pd.DataFrame,
    label: str,
    out_dir: Path,
    max_or: float,
    strict: tuple[float, int],
) -> None:
    """Per outcome: pooled and per-study gene-burden odds ratios.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden` (pooled run, levels pooled and stratum).
    label : `str`
        Run label, used in file names.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.
    strict : `tuple[float, int]`
        From `strict_threshold`.

    Returns
    -------
    `None`
    """
    gene = VariantListColumns.OUT_GENE
    study = HarmonisedColumns.STUDY_ACCESSION
    names = study_names()
    legend = _significance_legend(*strict)
    for outcome, rows in burden.groupby(HarmonisedColumns.OUTCOME):
        rows = rows.copy()
        is_pooled = rows[MetaColumns.LEVEL] == MetaLevel.POOLED
        rows["_order"] = np.where(is_pooled, 0, 1)
        rows = rows.sort_values([gene, "_order", study], na_position="first")
        is_pooled = rows[MetaColumns.LEVEL] == MetaLevel.POOLED
        rows[_MARKER] = _significance_marker(rows[MetaColumns.P], strict[0])
        rows[_COLOUR] = np.where(is_pooled, _POOLED_COLOUR, _STUDY_COLOUR)
        rows[_SIZE] = np.where(is_pooled, _POOLED_SIZE, _STUDY_SIZE)
        rows[_ROW_NAME] = [
            _POOLED_NAME if pooled else _study_name(str(accession), names)
            for pooled, accession in zip(is_pooled, rows[study])
        ]
        figure = draw_forest(
            rows, _outcome_name(str(outcome)), "Study", legend, max_or
        )
        save(figure, out_dir / f"forest_burden_{label}_{outcome}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def forest_apoe(
    burden: pd.DataFrame,
    strata: pd.DataFrame,
    label: str,
    out_dir: Path,
    max_or: float,
    strict: tuple[float, int],
) -> None:
    """Per outcome: pooled gene-burden odds ratio overall and per stratum.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`, the pooled run (all APOE genotypes).
    strata : `pd.DataFrame`
        From `load_burden`, the ``_apoe_strata`` run.
    label : `str`
        Run label, used in file names.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.
    strict : `tuple[float, int]`
        From `strict_threshold` of the pooled run.

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
    legend = _significance_legend(*strict)
    for outcome, rows in rows_all.groupby(HarmonisedColumns.OUTCOME):
        has_strata = rows[stratum] != ApoeStratum.ALL
        if not has_strata.any():
            _LOGGER.info(f"{outcome}: no APOE strata, forest skipped")
            continue
        rows = rows.sort_values([gene, "_order"]).copy()
        is_all = rows[stratum] == ApoeStratum.ALL
        rows[_MARKER] = _significance_marker(rows[MetaColumns.P], strict[0])
        rows[_COLOUR] = np.where(is_all, _POOLED_COLOUR, _STUDY_COLOUR)
        rows[_SIZE] = np.where(is_all, _POOLED_SIZE, _STUDY_SIZE)
        rows[_ROW_NAME] = rows[stratum].map(_STRATUM_NAMES)
        figure = draw_forest(
            rows,
            f"{_outcome_name(str(outcome))} by APOE genotype",
            "APOE",
            legend,
            max_or,
        )
        save(figure, out_dir / f"forest_apoe_{label}_{outcome}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def forest_apoe_genotype(
    results: pd.DataFrame,
    out_dir: Path,
    max_or: float,
    model: str = _APOE_GENOTYPE_MODEL,
) -> None:
    """Per population: odds ratio of each APOE genotype vs ε3/ε3.

    Parameters
    ----------
    results : `pd.DataFrame`
        From `load_apoe_genotype`.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.
    model : `str`, optional, default: `_APOE_GENOTYPE_MODEL`
        marvel model of `results`, shown in the title.

    Returns
    -------
    `None`

    Notes
    -----
    The Bonferroni threshold is 0.05 / (genotype x outcome estimates of
    the population).
    """
    outcome_rank = {
        name: i for i, name in enumerate(_APOE_GENOTYPE_OUTCOMES.values())
    }
    genotype_rank = {name: i for i, name in enumerate(_GENOTYPE_NAMES)}
    for population, rows in results.groupby(_POPULATION):
        rows = rows.copy()
        rows["_outcome_order"] = rows[HarmonisedColumns.OUTCOME].map(
            outcome_rank
        )
        rows["_genotype_order"] = rows[_GENOTYPE].map(genotype_rank)
        rows = rows.sort_values(["_outcome_order", "_genotype_order"])
        n_tests = int(np.isfinite(rows[MetaColumns.P]).sum())
        strict = (_P_NOMINAL / max(n_tests, 1), n_tests)
        rows[_OUTCOME_GROUP] = rows[HarmonisedColumns.OUTCOME].map(
            _outcome_name
        )
        rows[_MARKER] = _significance_marker(rows[MetaColumns.P], strict[0])
        rows[_COLOUR] = _POOLED_COLOUR
        rows[_SIZE] = _POOLED_SIZE
        rows[_ROW_NAME] = [
            _GENOTYPE_NAMES[genotype]
            if not np.isfinite(exposed)
            else f"{_GENOTYPE_NAMES[genotype]} (n={int(exposed):,})"
            for genotype, exposed in zip(
                rows[_GENOTYPE], rows[MarvelColumns.EXPOSED]
            )
        ]
        name = _POPULATION_NAMES.get(str(population), str(population))
        figure = draw_forest(
            rows,
            f"{name}: APOE genotype vs {_REFERENCE_GENOTYPE_NAME} ({model})",
            "APOE genotype",
            _significance_legend(*strict),
            max_or,
            group_col=_OUTCOME_GROUP,
            italic_groups=False,
        )
        save(figure, out_dir / f"forest_apoe_genotype_{population}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def forest_sources(
    burden: pd.DataFrame,
    label: str,
    out_dir: Path,
    max_or: float,
    strict: tuple[float, int],
) -> None:
    """Per outcome: per gene each source's estimate, then the pooled one.

    Row order per gene: other sources (FinnGen, Thomassen), UK Biobank,
    pooled (IVW) last.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden` (a `--prefer-groups` run, levels pooled and
        stratum).
    label : `str`
        Run label, used in file names.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.
    strict : `tuple[float, int]`
        From `strict_threshold`.

    Returns
    -------
    `None`
    """
    gene = VariantListColumns.OUT_GENE
    is_pooled = burden[MetaColumns.LEVEL] == MetaLevel.POOLED
    sources = source_rows(burden.loc[~is_pooled])
    sources["_order"] = np.where(sources[_ROW_NAME] == _UKB_NAME, 1, 0)
    pooled = burden.loc[is_pooled].copy()
    pooled[_ROW_NAME] = _POOLED_NAME
    pooled["_order"] = 2
    rows_all = pd.concat([sources, pooled], ignore_index=True)
    legend = _significance_legend(*strict)
    for outcome, rows in rows_all.groupby(HarmonisedColumns.OUTCOME):
        rows = rows.sort_values([gene, "_order", _ROW_NAME]).copy()
        is_pooled_row = rows["_order"] == 2
        rows[_MARKER] = _significance_marker(rows[MetaColumns.P], strict[0])
        rows[_COLOUR] = np.where(
            is_pooled_row, _POOLED_COLOUR, _STUDY_COLOUR
        )
        rows[_SIZE] = np.where(is_pooled_row, _POOLED_SIZE, _STUDY_SIZE)
        figure = draw_forest(
            rows, _outcome_name(str(outcome)), "Source", legend, max_or
        )
        save(figure, out_dir / f"forest_sources_{label}_{outcome}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def forest_pooled(
    burden: pd.DataFrame,
    label: str,
    out_dir: Path,
    max_or: float,
    strict: tuple[float, int],
) -> None:
    """One forest of the pooled estimates: per gene one row per outcome.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`.
    label : `str`
        Run label, used in the file name.
    out_dir : `Path`
        Output directory.
    max_or : `float`
        Axis limit, see `draw_forest`.
    strict : `tuple[float, int]`
        From `strict_threshold`.

    Returns
    -------
    `None`
    """
    gene = VariantListColumns.OUT_GENE
    outcome = HarmonisedColumns.OUTCOME
    rows = burden[burden[MetaColumns.LEVEL] == MetaLevel.POOLED].copy()
    rank = {name: i for i, name in enumerate(_OUTCOME_NAMES)}
    rows["_order"] = rows[outcome].map(rank).fillna(len(rank))
    rows = rows.sort_values([gene, "_order", outcome])
    rows[_MARKER] = _significance_marker(rows[MetaColumns.P], strict[0])
    rows[_COLOUR] = _POOLED_COLOUR
    rows[_SIZE] = _POOLED_SIZE
    rows[_ROW_NAME] = [_outcome_name(str(name)) for name in rows[outcome]]
    figure = draw_forest(
        rows,
        "Gene burden, pooled (IVW)",
        "Outcome",
        _significance_legend(*strict),
        max_or,
    )
    save(figure, out_dir / f"forest_pooled_{label}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def burden_heatmap(
    burden: pd.DataFrame,
    label: str,
    out_dir: Path,
    strict: tuple[float, int],
) -> None:
    """Pooled gene-burden log odds ratio per gene and outcome.

    Parameters
    ----------
    burden : `pd.DataFrame`
        From `load_burden`.
    label : `str`
        Run label, used in the file name.
    out_dir : `Path`
        Output directory.
    strict : `tuple[float, int]`
        From `strict_threshold`.

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
    glyphs = pd.DataFrame("", index=beta.index, columns=beta.columns)
    glyphs = glyphs.mask(p < _P_NOMINAL, _GLYPH_NOMINAL)
    glyphs = glyphs.mask(p < strict[0], _GLYPH_STRICT)
    n_cells = int(beta.notna().sum().sum())
    limit = float(np.nanmax(np.abs(beta.to_numpy()))) if n_cells else 1.0
    matplotlib.rcParams["axes.linewidth"] = _LWD
    figure, ax = plt.subplots(
        figsize=(
            (2.5 + 1.0 * beta.shape[1]) * _CM,
            (2.0 + 0.6 * beta.shape[0]) * _CM,
        )
    )
    im, cbar = heatmap(
        beta.to_numpy(dtype=float),
        row_labels=list(beta.index),
        col_labels=[_outcome_name(str(name)) for name in beta.columns],
        ax=ax,
        cbar_bool=True,
        cbar_label="Pooled log odds ratio",
        cmap="RdBu_r",
        vmin=-limit,
        vmax=limit,
        grid_linewidth=1,
    )
    with warnings.catch_warnings():
        # empty (NaN) cells are masked; matplotlib warns per masked cell
        warnings.simplefilter("ignore", UserWarning)
        annotate_heatmap(
            im, data=glyphs, threshold=limit / 2, fontsize=_STEXT_SIZE
        )
    ax.tick_params(
        axis="both", labelsize=_AX_LAB_SZ, width=_LWD, length=2
    )
    for tick in ax.get_yticklabels():
        tick.set_fontstyle("italic")
    cbar.ax.tick_params(labelsize=_AX_LAB_SZ, width=_LWD, length=2)
    cbar.outline.set_linewidth(_LWD)
    cbar.set_label("Pooled log odds ratio", fontsize=_LAB_SIZE)
    ax.set_title(
        "Gene burden", fontweight="bold", fontsize=_TITLE_SIZE, loc="left"
    )
    figure.text(
        0.0,
        -0.08,
        f"{_GLYPH_NOMINAL} p < {_P_NOMINAL:g}; {_GLYPH_STRICT} p < "
        f"{strict[0]:.1e} (Bonferroni, {strict[1]} tests); "
        "blank: no estimate",
        fontsize=_STEXT_SIZE,
    )
    save(figure, out_dir / f"heatmap_burden_{label}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def figures(
    ancestry: str,
    forest_label: str | None,
    heatmap_label: str | None,
    out_dir: Path,
    max_or: float,
    sources_label: str | None = None,
    apoe_genotype_model: str | None = None,
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
    sources_label : `str` or `None`, optional, default: `None`
        Label of a `--prefer-groups` run for `forest_sources` and
        `forest_pooled`; `None` skips them.
    apoe_genotype_model : `str` or `None`, optional, default: `None`
        marvel model for `forest_apoe_genotype`; `None` skips it.

    Returns
    -------
    `None`
    """
    if forest_label:
        burden = load_burden(burden_path(ancestry, forest_label))
        if burden is not None:
            strict = strict_threshold(burden)
            forest_burden(burden, forest_label, out_dir, max_or, strict)
            strata = load_burden(
                burden_path(
                    ancestry, forest_label, f"_{Constants.APOE_STRATA_LABEL}"
                )
            )
            if strata is not None:
                forest_apoe(
                    burden, strata, forest_label, out_dir, max_or, strict
                )
    if heatmap_label:
        burden = load_burden(burden_path(ancestry, heatmap_label))
        if burden is not None:
            burden_heatmap(
                burden, heatmap_label, out_dir, strict_threshold(burden)
            )
    if sources_label:
        burden = load_burden(burden_path(ancestry, sources_label))
        if burden is not None:
            strict = strict_threshold(burden)
            forest_sources(burden, sources_label, out_dir, max_or, strict)
            forest_pooled(burden, sources_label, out_dir, max_or, strict)
    if apoe_genotype_model:
        results = load_apoe_genotype(model=apoe_genotype_model)
        if results is not None:
            forest_apoe_genotype(
                results, out_dir, max_or, model=apoe_genotype_model
            )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Forest plots and heatmap of the gene-burden results, and the "
            "APOE genotype forest."
        )
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
        "--sources-label",
        help=(
            "meta_analysis.py --label of a --prefer-groups run: forest per "
            "outcome by source and a forest of the pooled estimates"
        ),
    )
    parser.add_argument(
        "--apoe-genotype",
        action="store_true",
        help=(
            "forest of the marvel APOE genotype vs e3e3 runs, read from "
            "the outdirs of marvel_apoe_tasks.tsv copied into results/"
        ),
    )
    parser.add_argument(
        "--apoe-model",
        default=_APOE_GENOTYPE_MODEL,
        help="marvel model for --apoe-genotype (default: %(default)s)",
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
    if not (
        args.forest_label
        or args.heatmap_label
        or args.sources_label
        or args.apoe_genotype
    ):
        parser.error(
            "give --forest-label, --heatmap-label, --sources-label and/or "
            "--apoe-genotype"
        )
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
        sources_label=args.sources_label,
        apoe_genotype_model=args.apoe_model if args.apoe_genotype else None,
    )


if __name__ == "__main__":
    main()
