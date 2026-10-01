#!/usr/bin/env python3
"""
Fixed-effect inverse-variance weighted (IVW) meta-analysis of the GWAS
rows matched to the gene variant lists (`matched_variants.tsv.gz`).

Effects are oriented towards the a2 (alt) allele, flipped to a1 for GoF
variants. Rows are pooled per named grouping (`MetaColumns.GROUPINGS`),
after keeping one estimate per study, dropping estimates copied under
another accession, and dropping effect-allele-only matches whose tested
alt is unknown.
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
_NEG_LOG10_P_KEY: str = "_neg_log10_p"
_RANK_KEY: str = "_source_rank"
_COPY_OF_KEY: str = "_copy_of"
# `match_alleles` value of rows matched on the effect allele only
_EFFECT_ONLY: str = "effect_only"
# above this -log10 p, 10**-x underflows; z comes from the normal tail
_DIRECT_Z_MAX_NEG_LOG10_P: float = 300.0
_TAIL_ITERATIONS: int = 5
_NORMAL = NormalDist()
# vectorised stdlib function (scipy is not a project dependency)
_ERFC = np.vectorize(math.erfc, otypes=[float])


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
def _z_from_neg_log10_p(neg_log10_p: float) -> float:
    """Convert a two-sided -log10 p-value to an absolute z-score.

    Parameters
    ----------
    neg_log10_p : `float`
        -log10 of the two-sided p-value, > 0.

    Returns
    -------
    z : `float`
        ``|z|`` with ``p = 2 * (1 - Phi(|z|))``.

    Notes
    -----
    Below `_DIRECT_Z_MAX_NEG_LOG10_P` the normal quantile is used
    directly. Above it, ``10**-x`` underflows, so ``z`` is solved from
    the Mills-ratio tail approximation
    ``-ln(p/2) = z^2/2 + ln(z) + ln(2*pi)/2 - ln(1 - 1/z^2)``
    by fixed-point iteration (relative error < 1e-6 for z > 37).
    """
    if neg_log10_p < _DIRECT_Z_MAX_NEG_LOG10_P:
        return -_NORMAL.inv_cdf(10.0**-neg_log10_p / 2)
    tail = neg_log10_p * math.log(10) + math.log(2)
    z = math.sqrt(2 * tail)
    for _ in range(_TAIL_ITERATIONS):
        z = math.sqrt(
            2
            * (
                tail
                - math.log(z)
                - 0.5 * math.log(2 * math.pi)
                + math.log1p(-1 / z**2)
            )
        )
    return z


_Z_FROM_NEG_LOG10_P = np.vectorize(_z_from_neg_log10_p, otypes=[float])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _rank_rows(rows: pd.DataFrame) -> pd.DataFrame:
    """Sort rows by preference: source, then smallest p, then accession.

    Parameters
    ----------
    rows : `pd.DataFrame`
        With `source`, `study_accession` and helper `_NEG_LOG10_P_KEY`.

    Returns
    -------
    ranked : `pd.DataFrame`
        `rows` sorted, index kept, sources ranked by
        `Constants.GWAS_SOURCE_PREFERENCE` (others last).
    """
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
    return ranked.sort_values(
        [_RANK_KEY, _NEG_LOG10_P_KEY, HarmonisedColumns.STUDY_ACCESSION],
        ascending=[True, False, True],
        kind="stable",
        na_position="last",
    ).drop(columns=_RANK_KEY)


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
        `SE_DERIVED`, `BETA_A2` and helper `_NEG_LOG10_P_KEY`.
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

    # p_value of 0 is an underflow; neg_log10_p keeps the value then.
    # Kept on the -log10 scale so it never underflows again.
    from_p = -np.log10(p_value.where(p_value > 0))
    neg_log10 = from_p.where(p_value > 0, neg_log10_p)
    rows[_NEG_LOG10_P_KEY] = neg_log10
    has_se = se.notna() & (se > 0) & np.isfinite(se)
    p_ok = neg_log10.notna() & (neg_log10 > 0) & np.isfinite(neg_log10)
    beta_used = rows[MetaColumns.BETA_USED]
    derivable = ~has_se & p_ok & beta_used.notna() & (beta_used != 0)
    z = pd.Series(np.nan, index=rows.index)
    z[derivable] = _Z_FROM_NEG_LOG10_P(neg_log10[derivable].to_numpy())
    rows[MetaColumns.SE_USED] = se.where(has_se, beta_used.abs() / z)
    rows[MetaColumns.SE_DERIVED] = ~has_se

    reasons = {
        "no beta or odds ratio": beta_used.isna(),
        "no SE and p missing or 1": (
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

    Rows are ranked with `_rank_rows` (source preference, then smallest
    p). Rows without a study accession cannot be told apart and are all
    kept (warned).

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
    ranked = _rank_rows(rows)
    no_study = ranked[HarmonisedColumns.STUDY_ACCESSION].isna()
    kept = ranked[no_study].index.union(
        ranked[~no_study].drop_duplicates(subset).index
    )
    return rows.loc[kept].sort_index()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def resolve_ambiguous(rows: pd.DataFrame) -> pd.DataFrame:
    """Keep effect-allele-only a1 matches only where the alt is known.

    A GWAS row with only an effect allele (curated) whose effect allele
    is `a1` is copied into every list site at a multi-allelic position,
    although the study tested one unknown alt. When summary-stats rows
    of the same study matched exactly one of those sites (both alleles),
    that site is kept; otherwise all copies are dropped and logged, as
    is standard for unresolvable multi-allelic variants.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `prepare_effects`.

    Returns
    -------
    resolved : `pd.DataFrame`
        `rows` without the unresolved and wrong-site copies.
    """
    hc = HarmonisedColumns
    vl = VariantListColumns
    site = MetaColumns.VARIANT_SITE
    candidate = (rows[vl.MATCH_ALLELES] == _EFFECT_ONLY) & (
        rows[vl.EFFECT_ALLELE_IS] == "a1"
    )
    if not candidate.any():
        return rows
    # one key per original GWAS row (its copies share every GWAS column)
    row_columns = [
        hc.SOURCE,
        hc.STUDY_ACCESSION,
        hc.OUTCOME,
        hc.CHROM,
        hc.POS,
        hc.RSID,
        hc.EFFECT_ALLELE,
        MetaColumns.BETA_USED,
        _NEG_LOG10_P_KEY,
    ]
    row_key = (
        rows.loc[candidate, row_columns]
        .astype("string")
        .fillna("")
        .agg("|".join, axis=1)
    )
    n_sites = rows.loc[candidate, site].groupby(row_key).transform("nunique")
    ambiguous = n_sites[n_sites > 1].index
    if ambiguous.empty:
        return rows

    both = rows[rows[vl.MATCH_ALLELES] != _EFFECT_ONLY]
    study_sites = set(zip(both[hc.STUDY_ACCESSION], both[site]))
    confirmed = pd.Series(
        [
            (study, variant) in study_sites
            for study, variant in zip(
                rows.loc[ambiguous, hc.STUDY_ACCESSION],
                rows.loc[ambiguous, site],
            )
        ],
        index=ambiguous,
    )
    keys = row_key[ambiguous]
    n_confirmed = confirmed.groupby(keys).transform("sum")
    keep = confirmed & (n_confirmed == 1)
    drop = ambiguous[~keep.to_numpy()]

    resolved_keys = keys[n_confirmed == 1].unique()
    unresolved = rows.loc[ambiguous[(n_confirmed != 1).to_numpy()]]
    log_info(
        f"{keys.nunique()} effect-allele-only GWAS rows with a1 at a "
        f"multi-allelic site: {len(resolved_keys)} resolved by same-study "
        f"summary stats, {unresolved.groupby(keys).ngroups} dropped"
    )
    for _, group in unresolved.groupby(keys, sort=False):
        first = group.iloc[0]
        log_info(
            f"dropped, tested alt unknown: {first[hc.RSID]} "
            f"{first[hc.STUDY_ACCESSION]} {first[hc.OUTCOME]} "
            f"a1={first[vl.OUT_A1]} a2 in {_join_unique(group[vl.OUT_A2])}"
        )
    log_info(f"{len(drop)} ambiguous copies removed")
    return rows.drop(index=drop)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def drop_copies(
    rows: pd.DataFrame, keys: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Drop estimates that copy another study's estimate exactly.

    The same analysis is sometimes deposited under several accessions
    (identical beta and SE). Pooling the copies would count one
    estimate several times, so per variant, outcome and grouping key
    only the first-ranked (`_rank_rows`) of identical estimates is kept.

    Parameters
    ----------
    rows : `pd.DataFrame`
        Deduped rows (`dedupe`), one per study and group.
    keys : `list[str]`
        Grouping columns.

    Returns
    -------
    kept : `pd.DataFrame`
        `rows` without the copies, in the original row order.
    copies : `pd.DataFrame`
        The dropped rows, with helper `_COPY_OF_KEY` (the accession of
        the kept estimate).
    """
    accession = HarmonisedColumns.STUDY_ACCESSION
    subset = list(
        dict.fromkeys(
            [
                MetaColumns.VARIANT_SITE,
                HarmonisedColumns.OUTCOME,
                *keys,
                MetaColumns.BETA_USED,
                MetaColumns.SE_USED,
            ]
        )
    )
    ranked = _rank_rows(rows)
    is_copy = ranked.duplicated(subset, keep="first")
    originals = ranked.loc[~is_copy, [*subset, accession]].drop_duplicates(
        subset
    )
    copies = ranked.loc[is_copy].copy()
    # a left merge keeps the left row order; originals are unique per subset
    copies[_COPY_OF_KEY] = (
        copies[subset].merge(originals, on=subset, how="left")[accession]
    ).to_numpy()
    return rows.drop(index=copies.index), copies


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

    The a2 allele is used, or a1 when any of the variant's list sources
    is `Constants.GOF_VARIANT_SOURCE`.

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
    gof_sites = set(
        rows.loc[
            rows[VariantListColumns.OUT_SOURCE]
            == Constants.GOF_VARIANT_SOURCE,
            site,
        ]
    )

    is_gof = rows[site].isin(gof_sites)
    sign = np.where(is_gof, -1.0, 1.0)
    oriented = rows.copy()
    oriented[MetaColumns.ORIENTATION] = np.where(
        is_gof, Orientation.A2_GOF_FLIPPED, Orientation.A2
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
def meta_analyse(
    rows: pd.DataFrame, keys: list[str], copies: pd.DataFrame
) -> pd.DataFrame:
    """Pool the oriented effects per group and describe each group.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `orient`, deduped with `dedupe` and `drop_copies` on `keys`.
    keys : `list[str]`
        Grouping columns.
    copies : `pd.DataFrame`
        The copies removed by `drop_copies`.

    Returns
    -------
    pooled : `pd.DataFrame`
        `ivw` output plus `N_STUDIES`, `N_SE_DERIVED`, `STUDIES`,
        `COPIED_STUDIES` (``""`` when none) and the
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
    if copies.empty:
        pooled[MetaColumns.COPIED_STUDIES] = ""
    else:
        copied = (
            copies.groupby(keys, sort=True, dropna=False)[
                HarmonisedColumns.STUDY_ACCESSION
            ]
            .agg(_join_unique)
            .rename(MetaColumns.COPIED_STUDIES)
            .reset_index()
        )
        pooled = pooled.merge(copied, on=keys, how="left")
        pooled[MetaColumns.COPIED_STUDIES] = pooled[
            MetaColumns.COPIED_STUDIES
        ].fillna("")

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

    log_stage("resolve_ambiguous")
    rows = resolve_ambiguous(rows)

    log_stage("orient")
    rows = orient(rows)

    log_stage("dedupe")
    n_before = len(rows)
    rows = dedupe(rows, keys)
    log_info(f"{n_before - len(rows)} duplicate rows removed")
    rows, copies = drop_copies(rows, keys)
    log_info(f"{len(copies)} estimates removed as copies of another study")
    pairs = copies.groupby(
        [_COPY_OF_KEY, HarmonisedColumns.STUDY_ACCESSION]
    ).size()
    for (original, copy), n in pairs.items():
        log_info(f"{copy} copies {original}: {n} estimates")

    log_stage("meta_analyse")
    pooled = meta_analyse(rows, keys, copies)

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
