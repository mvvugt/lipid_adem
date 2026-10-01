#!/usr/bin/env python3
"""
Fixed-effect inverse-variance weighted (IVW) meta-analysis of the GWAS
rows matched to the gene variant lists (`matched_variants.tsv.gz`).

Effects are oriented towards the LDL-lowering allele when the variant has
an LDL-C estimate; otherwise towards the a2 (alt) allele, flipped for GoF
variants. Rows are pooled per named grouping (`MetaColumns.GROUPINGS`).
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import math
from statistics import NormalDist

import numpy as np
import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    Constants,
    FileNames,
    HarmonisedColumns,
    MetaColumns,
    Orientation,
    Paths,
    RunlogOrder,
    VariantListColumns,
)


# helper columns, dropped before writing
_P_KEY: str = "_p"
_RANK_KEY: str = "_source_rank"
# vectorised stdlib functions (scipy is not a project dependency)
_ERFC = np.vectorize(math.erfc, otypes=[float])
_NORMAL_INV_CDF = np.vectorize(NormalDist().inv_cdf, otypes=[float])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def _normalise_chrom(chrom: pd.Series) -> pd.Series:
    """Write chromosomes without a ``chr`` prefix, as nullable strings.

    Parameters
    ----------
    chrom : `pd.Series`
        Chromosome names, e.g. ``"chr1"`` or ``"1"``.

    Returns
    -------
    normalised : `pd.Series`
        `string` dtype, prefix and surrounding blanks removed.
    """
    return (
        chrom.astype("string")
        .str.strip()
        .str.replace(r"^chr", "", regex=True, case=False)
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _join_unique(values: pd.Series) -> str:
    """Join the sorted unique non-missing values of a column with ``;``.

    Parameters
    ----------
    values : `pd.Series`
        Values of one group.

    Returns
    -------
    joined : `str`
        ``""`` when every value is missing.
    """
    return ";".join(sorted(values.dropna().astype(str).unique()))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_matched() -> pd.DataFrame:
    """Read the matched GWAS rows and add the variant-site key.

    Returns
    -------
    matched : `pd.DataFrame`
        `matched_variants.tsv.gz` plus `MetaColumns.VARIANT_SITE`
        (``chrom:pos:a1:a2`` of the variant-list entry).

    Raises
    ------
    FileNotFoundError
        If `FileNames.MATCHED_VARIANTS` does not exist (run
        match_variants.py first).
    """
    if not FileNames.MATCHED_VARIANTS.exists():
        raise FileNotFoundError(
            f"{FileNames.MATCHED_VARIANTS} not found: run "
            "match_variants.py first"
        )
    matched = pd.read_csv(
        FileNames.MATCHED_VARIANTS,
        sep="\t",
        dtype={
            HarmonisedColumns.CHROM: str,
            HarmonisedColumns.EFFECT_ALLELE: str,
            HarmonisedColumns.OTHER_ALLELE: str,
            VariantListColumns.OUT_A1: str,
            VariantListColumns.OUT_A2: str,
        },
        low_memory=False,
    )
    pos = pd.to_numeric(
        matched[HarmonisedColumns.POS], errors="coerce"
    ).astype("Int64")
    matched[MetaColumns.VARIANT_SITE] = (
        _normalise_chrom(matched[HarmonisedColumns.CHROM])
        + ":"
        + pos.astype("string")
        + ":"
        + matched[VariantListColumns.OUT_A1].astype("string")
        + ":"
        + matched[VariantListColumns.OUT_A2].astype("string")
    )
    log_info(
        f"{FileNames.MATCHED_VARIANTS}: {len(matched)} rows, "
        f"{matched[MetaColumns.VARIANT_SITE].nunique()} variants"
    )
    return matched


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def prepare_effects(matched: pd.DataFrame) -> pd.DataFrame:
    """Set the beta and SE used per row, aligned to the a2 allele.

    The beta is `beta`, or log(`odds_ratio`) when `beta` is missing. The
    SE is `se` when > 0, otherwise derived from the two-sided p-value as
    ``|beta| / z``. Rows without a usable beta or SE are dropped and
    counted per reason.

    Parameters
    ----------
    matched : `pd.DataFrame`
        From `load_matched`.

    Returns
    -------
    rows : `pd.DataFrame`
        Usable rows with `BETA_USED`, `EFFECT_SCALE`, `SE_USED`,
        `SE_DERIVED`, `BETA_A2` and helper `_P_KEY`.
    """
    rows = matched.copy()
    beta = pd.to_numeric(rows[HarmonisedColumns.BETA], errors="coerce")
    odds_ratio = pd.to_numeric(
        rows[HarmonisedColumns.ODDS_RATIO], errors="coerce"
    )
    se = pd.to_numeric(rows[HarmonisedColumns.SE], errors="coerce")
    p_value = pd.to_numeric(rows[HarmonisedColumns.P_VALUE], errors="coerce")
    neg_log10_p = pd.to_numeric(
        rows[HarmonisedColumns.NEG_LOG10_P], errors="coerce"
    )

    has_beta = beta.notna() & np.isfinite(beta)
    has_or = odds_ratio.notna() & (odds_ratio > 0) & np.isfinite(odds_ratio)
    log_or = np.log(odds_ratio.where(has_or))
    rows[MetaColumns.BETA_USED] = beta.where(has_beta, log_or)
    rows[MetaColumns.EFFECT_SCALE] = np.where(
        has_beta, "beta", np.where(has_or, "log_or", None)
    )

    # p_value of 0 is an underflow; -log10 p keeps the value then
    p = p_value.where(p_value > 0, 10 ** -neg_log10_p)
    rows[_P_KEY] = p
    has_se = se.notna() & (se > 0) & np.isfinite(se)
    p_ok = p.notna() & (p > 0) & (p < 1)
    beta_used = rows[MetaColumns.BETA_USED]
    derivable = ~has_se & p_ok & beta_used.notna() & (beta_used != 0)
    z = pd.Series(np.nan, index=rows.index)
    z[derivable] = -_NORMAL_INV_CDF(p[derivable].to_numpy() / 2)
    rows[MetaColumns.SE_USED] = se.where(has_se, beta_used.abs() / z)
    rows[MetaColumns.SE_DERIVED] = ~has_se

    reasons = {
        "no beta or odds ratio": beta_used.isna(),
        "no SE and p missing, 0 or 1": (
            beta_used.notna() & ~has_se & ~p_ok
        ),
        "no SE and beta 0": (
            beta_used.notna() & ~has_se & p_ok & (beta_used == 0)
        ),
    }
    for reason, mask in reasons.items():
        if mask.any():
            log_info(f"{int(mask.sum())} rows dropped: {reason}")
    usable = beta_used.notna() & rows[MetaColumns.SE_USED].notna()
    rows = rows[usable].copy()

    to_a2 = np.where(
        rows[VariantListColumns.EFFECT_ALLELE_IS] == "a2", 1.0, -1.0
    )
    rows[MetaColumns.BETA_A2] = rows[MetaColumns.BETA_USED] * to_a2
    log_info(
        f"{len(rows)} usable rows, "
        f"{int(rows[MetaColumns.SE_DERIVED].sum())} with SE derived from p"
    )
    return rows.reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dedupe(rows: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    """Keep one row per study, variant, outcome and grouping key.

    Rows are ranked by `Constants.GWAS_SOURCE_PREFERENCE`, then by
    smallest p. Rows without a study accession cannot be told apart and
    are all kept (warned).

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `prepare_effects` (or `orient`).
    keys : `list[str]`
        Grouping columns; deduped together with study accession, variant
        site and outcome.

    Returns
    -------
    deduped : `pd.DataFrame`
        In the original row order.
    """
    subset = list(
        dict.fromkeys(
            [
                HarmonisedColumns.STUDY_ACCESSION,
                MetaColumns.VARIANT_SITE,
                HarmonisedColumns.OUTCOME,
                *keys,
            ]
        )
    )
    n_no_study = int(rows[HarmonisedColumns.STUDY_ACCESSION].isna().sum())
    if n_no_study:
        log_warn(
            f"{n_no_study} rows without "
            f"{HarmonisedColumns.STUDY_ACCESSION} kept without deduping"
        )
    rank = {
        source: i
        for i, source in enumerate(Constants.GWAS_SOURCE_PREFERENCE)
    }
    ranked = rows.assign(
        **{
            _RANK_KEY: rows[HarmonisedColumns.SOURCE]
            .map(rank)
            .fillna(len(rank))
        }
    )
    ranked = ranked.sort_values(
        [_RANK_KEY, _P_KEY], kind="stable", na_position="last"
    )
    no_study = ranked[HarmonisedColumns.STUDY_ACCESSION].isna()
    kept = ranked[no_study].index.union(
        ranked[~no_study].drop_duplicates(subset).index
    )
    return rows.loc[kept].sort_index()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ivw(rows: pd.DataFrame, keys: list[str], beta: str) -> pd.DataFrame:
    """Fixed-effect inverse-variance weighted meta-analysis per group.

    Parameters
    ----------
    rows : `pd.DataFrame`
        One row per estimate, with `beta` and `MetaColumns.SE_USED`.
    keys : `list[str]`
        Grouping columns.
    beta : `str`
        Column holding the (oriented) effect estimates.

    Returns
    -------
    pooled : `pd.DataFrame`
        Per group: `keys`, `N_ESTIMATES`, `BETA`, `SE`, `Z`, `P`, `Q`,
        `Q_DF` and `I2` (`Q`, `Q_DF`, `I2` NA for a single estimate).

    Notes
    -----
    ``w = 1/se^2``, ``beta = sum(w*b)/sum(w)``, ``se = sqrt(1/sum(w))``,
    ``p = erfc(|z|/sqrt(2))``, ``Q = sum(w*(b - beta)^2)`` on
    ``k - 1`` df and ``I^2 = max(0, (Q - df)/Q)``.
    """
    weights = 1.0 / rows[MetaColumns.SE_USED] ** 2
    work = rows[keys].assign(_w=weights, _wb=weights * rows[beta])
    grouped = work.groupby(keys, sort=True, dropna=False)
    pooled = grouped.agg(
        **{
            MetaColumns.N_ESTIMATES: ("_w", "size"),
            "_sum_w": ("_w", "sum"),
            "_sum_wb": ("_wb", "sum"),
        }
    ).reset_index()
    pooled[MetaColumns.BETA] = pooled["_sum_wb"] / pooled["_sum_w"]
    pooled[MetaColumns.SE] = np.sqrt(1.0 / pooled["_sum_w"])
    pooled[MetaColumns.Z] = pooled[MetaColumns.BETA] / pooled[MetaColumns.SE]
    pooled[MetaColumns.P] = _ERFC(
        pooled[MetaColumns.Z].abs().to_numpy() / math.sqrt(2)
    )

    # Q needs each estimate's distance to its own group's pooled beta
    with_pooled = work.assign(_b=rows[beta]).merge(
        pooled[[*keys, MetaColumns.BETA]], on=keys, how="left"
    )
    with_pooled[MetaColumns.Q] = (
        with_pooled["_w"]
        * (with_pooled["_b"] - with_pooled[MetaColumns.BETA]) ** 2
    )
    q = with_pooled.groupby(keys, sort=True, dropna=False)[
        MetaColumns.Q
    ].sum()
    pooled = pooled.merge(q.reset_index(), on=keys, how="left")
    pooled[MetaColumns.Q_DF] = pooled[MetaColumns.N_ESTIMATES] - 1
    single = pooled[MetaColumns.Q_DF] == 0
    pooled[MetaColumns.I2] = np.where(
        pooled[MetaColumns.Q] > 0,
        np.maximum(
            0.0,
            (pooled[MetaColumns.Q] - pooled[MetaColumns.Q_DF])
            / pooled[MetaColumns.Q].where(pooled[MetaColumns.Q] > 0),
        ),
        0.0,
    )
    for column in (MetaColumns.Q, MetaColumns.Q_DF, MetaColumns.I2):
        pooled[column] = pooled[column].astype(float).mask(single)
    return pooled.drop(columns=["_sum_w", "_sum_wb"])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def orient(rows: pd.DataFrame) -> pd.DataFrame:
    """Orient every row's effect per variant.

    A variant with any `Constants.LDL_OUTCOME` estimate is oriented
    towards its LDL-lowering allele (sign of its pooled a2 LDL-C beta,
    no p threshold). Otherwise the a2 allele is used, or a1 when any of
    the variant's list sources is `Constants.GOF_VARIANT_SOURCE`.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `prepare_effects`.

    Returns
    -------
    oriented : `pd.DataFrame`
        `rows` plus `ORIENTATION`, `ORIENTED_ALLELE` and `BETA_ORIENTED`.
    """
    site = MetaColumns.VARIANT_SITE
    ldl_rows = rows[rows[HarmonisedColumns.OUTCOME] == Constants.LDL_OUTCOME]
    ldl = ivw(
        dedupe(ldl_rows, [site, HarmonisedColumns.OUTCOME]),
        [site],
        MetaColumns.BETA_A2,
    ).set_index(site)[MetaColumns.BETA]
    gof_sites = set(
        rows.loc[
            rows[VariantListColumns.OUT_SOURCE]
            == Constants.GOF_VARIANT_SOURCE,
            site,
        ]
    )

    ldl_beta = rows[site].map(ldl)
    has_ldl = ldl_beta.notna()
    is_gof = rows[site].isin(gof_sites)
    sign = np.where(
        has_ldl, np.where(ldl_beta > 0, -1.0, 1.0), np.where(is_gof, -1.0, 1.0)
    )
    oriented = rows.copy()
    oriented[MetaColumns.ORIENTATION] = np.where(
        has_ldl,
        Orientation.LDL_LOWERING,
        np.where(is_gof, Orientation.A2_GOF_FLIPPED, Orientation.A2),
    )
    oriented[MetaColumns.ORIENTED_ALLELE] = np.where(
        sign > 0,
        oriented[VariantListColumns.OUT_A2],
        oriented[VariantListColumns.OUT_A1],
    )
    oriented[MetaColumns.BETA_ORIENTED] = oriented[MetaColumns.BETA_A2] * sign

    per_variant = oriented.drop_duplicates(site)[MetaColumns.ORIENTATION]
    for orientation, n in per_variant.value_counts().items():
        log_info(f"{n} variants oriented as {orientation}")
    return oriented


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def meta_analyse(rows: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    """Pool the oriented effects per group and describe each group.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `orient`, deduped with `dedupe` on `keys`.
    keys : `list[str]`
        Grouping columns.

    Returns
    -------
    pooled : `pd.DataFrame`
        `ivw` output plus `N_STUDIES`, `N_SE_DERIVED`, `STUDIES` and the
        `MetaColumns.DESCRIBE_COLUMNS` (unique values joined with ``;``).
    """
    pooled = ivw(rows, keys, MetaColumns.BETA_ORIENTED)
    grouped = rows.groupby(keys, sort=True, dropna=False)
    extra = grouped.agg(
        **{
            MetaColumns.N_STUDIES: (
                HarmonisedColumns.STUDY_ACCESSION,
                "nunique",
            ),
            MetaColumns.N_SE_DERIVED: (MetaColumns.SE_DERIVED, "sum"),
        }
    )
    extra[MetaColumns.STUDIES] = grouped[
        HarmonisedColumns.STUDY_ACCESSION
    ].agg(_join_unique)
    describe = [
        column
        for column in MetaColumns.DESCRIBE_COLUMNS
        if column in rows.columns and column not in keys
    ]
    for column in describe:
        extra[column] = grouped[column].agg(_join_unique)
    pooled = pooled.merge(extra.reset_index(), on=keys, how="left")

    n_multi = int((pooled[MetaColumns.N_ESTIMATES] > 1).sum())
    log_info(
        f"{len(pooled)} groups, {n_multi} pooling more than one estimate"
    )
    return pooled


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def meta_analysis(grouping: str) -> None:
    """Run the meta-analysis for one named grouping and write it.

    Parameters
    ----------
    grouping : `str`
        A key of `MetaColumns.GROUPINGS`.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If there is no matched-variants table.
    """
    keys = list(MetaColumns.GROUPINGS[grouping])
    log_info(f"grouping {grouping}: {', '.join(keys)}")

    log_stage("load_matched")
    matched = load_matched()

    log_stage("prepare_effects")
    rows = prepare_effects(matched)
    del matched

    log_stage("orient")
    rows = orient(rows)

    log_stage("dedupe")
    n_before = len(rows)
    rows = dedupe(rows, keys)
    log_info(f"{n_before - len(rows)} duplicate rows removed")

    log_stage("meta_analyse")
    pooled = meta_analyse(rows, keys)

    log_stage("write")
    path = Paths.RESULTS_OUTPUT / FileNames.META_ANALYSIS_TEMPLATE.format(
        grouping=grouping
    )
    Paths.RESULTS_OUTPUT.mkdir(parents=True, exist_ok=True)
    functions.write_table_atomic(pooled, path)
    log_info(f"wrote {len(pooled)} rows to {path}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Fixed-effect IVW meta-analysis of the matched variants."
    )
    parser.add_argument(
        "--group-by",
        choices=sorted(MetaColumns.GROUPINGS),
        default=MetaColumns.DEFAULT_GROUPING,
        help="named grouping to pool by (default: %(default)s)",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    return parser.parse_args()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.META_ANALYSIS):
        meta_analysis(args.group_by)


if __name__ == "__main__":
    main()
