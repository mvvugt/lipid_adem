#!/usr/bin/env python3
"""
Fixed-effect inverse-variance weighted (IVW) meta-analysis of the GWAS
rows matched to the gene variant lists (`matched_variants.tsv.gz`).

Effects are oriented towards the a2 (alt) allele, flipped to a1 for GoF
variants (lower gene function), then flipped again for genes whose
drugs raise gene function (`Constants.THERAPY_DIRECTION`), so every
written effect is in the therapeutic direction (`therapy_direction`
column). Each run pools the rows of one ancestry group (`--ancestry`,
default `MetaColumns.DEFAULT_ANCESTRY`; ``MULTI`` pools every ancestry
together) per variant and outcome
(`MetaColumns.KEYS`), after keeping one estimate per study, dropping
estimates copied under another accession, and dropping
effect-allele-only matches whose tested alt is unknown.

Optional filters restrict the run to studies, outcomes and variant-list
sources (`--studies`, `--outcomes`, `--variant-sources`); `--stratified`
adds each study's own estimate. Next to the per-variant table a gene
burden table is written: the IVW of the oriented variant effects per gene,
per study and pooled over studies. ClinVar variants with a raising condition
are flipped like GoF variants, as are the selected single GoF variants
(`SelectedGoF`). `--ukb-burden` takes each UKB study's gene
estimate from its carrier burden (`matched_burden.tsv.gz`) instead;
`--no-gene-burden` writes no gene burden (variants reported one by one),
and `--require-expected-scale` keeps only rows on their outcome's scale
(linear for lipids, log-OR otherwise).

APOE strata (`data/raw/apoe_strata.tsv`): the pooled run takes, per study
group, its unstratified study or else its strata; studies that are strata
are also pooled per stratum (`_apoe_strata` files).
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path
from statistics import NormalDist

import numpy as np
import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    Ancestry,
    ApoeStratum,
    ClinVarDirection,
    Constants,
    EffectScale,
    FileNames,
    HarmonisedColumns,
    MetaColumns,
    MetaLevel,
    Orientation,
    Paths,
    RunlogOrder,
    TherapyDirection,
    VariantListColumns,
)


# helper columns, dropped before writing
_NEG_LOG10_P_KEY: str = "_neg_log10_p"
_RANK_KEY: str = "_source_rank"
_DB_RANK_KEY: str = "_source_db_rank"
_COPY_OF_KEY: str = "_copy_of"
# `match_alleles` value of rows matched on the effect allele only
_EFFECT_ONLY: str = "effect_only"
# above this -log10 p, 10**-x underflows; z comes from the normal tail
_DIRECT_Z_MAX_NEG_LOG10_P: float = 300.0
_TAIL_ITERATIONS: int = 5
_NORMAL = NormalDist()
# vectorised stdlib function (scipy is not a project dependency)
_ERFC = np.vectorize(math.erfc, otypes=[float])
# marvel gene-burden `Exposure` (`<GENE>_<mask>`, burden_exposure.py)
_GENE_MASK_RE = re.compile(Constants.MARVEL_GENE_MASK_PATTERN)
# merge_associations keeps the marvel `Exposure` as src_Exposure
_EXPOSURE_COLUMN: str = "src_Exposure"
# helper column of the UKB burden rows: the exposure's mask
_MASK_KEY: str = "_mask"


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
def _join_study_maf(group: pd.DataFrame) -> str:
    """Join each study's MAF as ``<accession>=<maf>`` pairs with ``;``.

    Parameters
    ----------
    group : `pd.DataFrame`
        Rows of one group with `HarmonisedColumns.STUDY_ACCESSION` and
        `HarmonisedColumns.MAF`.

    Returns
    -------
    joined : `str`
        Sorted unique pairs, so in the order of `_join_unique` on the
        accessions; the MAF is given to 3 significant digits, or ``NA``.
    """
    maf = pd.to_numeric(group[HarmonisedColumns.MAF], errors="coerce")
    pairs = [
        f"{accession}={'NA' if pd.isna(value) else f'{value:.3g}'}"
        for accession, value in zip(
            group[HarmonisedColumns.STUDY_ACCESSION].fillna("NA"), maf
        )
    ]
    return ";".join(sorted(set(pairs)))


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
    """Sort rows by preference: source, source_db, smallest p, accession.

    Parameters
    ----------
    rows : `pd.DataFrame`
        With `source`, `source_db`, `study_accession` and helper
        `_NEG_LOG10_P_KEY`.

    Returns
    -------
    ranked : `pd.DataFrame`
        `rows` sorted, index kept, sources ranked by
        `Constants.GWAS_SOURCE_PREFERENCE` and then source databases by
        `Constants.SOURCE_DB_PREFERENCE` (others last in both).
    """
    source_rank = {
        source: i
        for i, source in enumerate(Constants.GWAS_SOURCE_PREFERENCE)
    }
    db_rank = {
        source_db: i
        for i, source_db in enumerate(Constants.SOURCE_DB_PREFERENCE)
    }
    ranked = rows.assign(
        **{
            _RANK_KEY: rows[HarmonisedColumns.SOURCE]
            .map(source_rank)
            .fillna(len(source_rank)),
            _DB_RANK_KEY: rows[HarmonisedColumns.SOURCE_DB]
            .map(db_rank)
            .fillna(len(db_rank)),
        }
    )
    return ranked.sort_values(
        [
            _RANK_KEY,
            _DB_RANK_KEY,
            _NEG_LOG10_P_KEY,
            HarmonisedColumns.STUDY_ACCESSION,
        ],
        ascending=[True, True, False, True],
        kind="stable",
        na_position="last",
    ).drop(columns=[_RANK_KEY, _DB_RANK_KEY])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_matched(path: Path = FileNames.MATCHED_VARIANTS) -> pd.DataFrame:
    """Read the matched GWAS rows and add the variant-site key.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.MATCHED_VARIANTS`
        The matched table.

    Returns
    -------
    matched : `pd.DataFrame`
        `matched_variants.tsv.gz` plus `MetaColumns.VARIANT_SITE`
        (``chrom:pos:a1:a2`` of the variant-list entry); missing
        `ancestry_group` values set to `Ancestry.NR`.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist (run match_variants.py first).
    ValueError
        If the table has no ClinVar direction column (written by an older
        match_variants.py).
    """
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found: run match_variants.py first"
        )
    columns = pd.read_csv(path, sep="\t", nrows=0).columns
    if VariantListColumns.OUT_CLINVAR_DIRECTION not in columns:
        raise ValueError(
            f"{path} has no "
            f"{VariantListColumns.OUT_CLINVAR_DIRECTION} column, so ClinVar "
            "raising variants cannot be oriented: rerun match_variants.py"
        )
    matched = pd.read_csv(
        path,
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
    # matched tables written before ancestry harmonisation have no column
    if HarmonisedColumns.ANCESTRY_GROUP not in matched.columns:
        log_warn(
            f"{path} has no ancestry_group column, "
            f"all rows labelled {Ancestry.NR} (rerun merge and match)"
        )
        matched[HarmonisedColumns.ANCESTRY_GROUP] = Ancestry.NR
    matched[HarmonisedColumns.ANCESTRY_GROUP] = matched[
        HarmonisedColumns.ANCESTRY_GROUP
    ].fillna(Ancestry.NR)
    # matched tables written before the effect-scale check have no column
    if HarmonisedColumns.STUDY_EFFECT_SCALE not in matched.columns:
        log_warn(
            f"{path} has no study_effect_scale "
            f"column, all rows labelled {EffectScale.UNKNOWN} (rerun merge "
            "and match)"
        )
        matched[HarmonisedColumns.STUDY_EFFECT_SCALE] = EffectScale.UNKNOWN
    matched[HarmonisedColumns.STUDY_EFFECT_SCALE] = matched[
        HarmonisedColumns.STUDY_EFFECT_SCALE
    ].fillna(EffectScale.UNKNOWN)
    log_info(
        f"{path}: {len(matched)} rows, "
        f"{matched[MetaColumns.VARIANT_SITE].nunique()} variants"
    )
    return matched


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_effect_scales(
    matched: pd.DataFrame, require_log_or: bool = False
) -> pd.DataFrame:
    """Warn about, or drop, studies whose betas are not log-OR.

    Parameters
    ----------
    matched : `pd.DataFrame`
        Matched rows with `study_effect_scale` (see `load_matched`).
    require_log_or : `bool`, optional, default: `False`
        Drop the rows of studies whose scale is not `EffectScale.LOG_OR`
        (linear, log-HR, unknown, conflict).

    Returns
    -------
    kept : `pd.DataFrame`
        `matched`, or its log-OR rows when `require_log_or`.
    """
    hc = HarmonisedColumns
    is_log_or = matched[hc.STUDY_EFFECT_SCALE] == EffectScale.LOG_OR
    other = (
        matched.loc[~is_log_or, [hc.STUDY_ACCESSION, hc.STUDY_EFFECT_SCALE]]
        .drop_duplicates()
        .sort_values([hc.STUDY_EFFECT_SCALE, hc.STUDY_ACCESSION])
    )
    action = "dropped" if require_log_or else "kept (--require-log-or drops)"
    for accession, scale in zip(
        other[hc.STUDY_ACCESSION], other[hc.STUDY_EFFECT_SCALE]
    ):
        log_warn(f"{accession}: effect scale {scale}, not log-OR; {action}")
    if not require_log_or:
        return matched
    log_info(
        f"--require-log-or: {int((~is_log_or).sum())} rows of "
        f"{other[hc.STUDY_ACCESSION].nunique()} studies dropped"
    )
    return matched.loc[is_log_or].copy()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def keep_expected_scales(matched: pd.DataFrame) -> pd.DataFrame:
    """Keep the rows on the effect scale expected for their outcome.

    Lipids (`Constants.LIPID_OUTCOMES`) are expected `EffectScale.LINEAR`,
    every other outcome `EffectScale.LOG_OR`; rows on another scale
    (unknown, conflict, log-HR, or linear for a binary outcome) are
    dropped, so no pool mixes scales.

    Parameters
    ----------
    matched : `pd.DataFrame`
        Matched rows with `outcome` and `study_effect_scale`.

    Returns
    -------
    kept : `pd.DataFrame`
        The rows on their expected scale; the dropped rows are logged
        per study and scale.
    """
    hc = HarmonisedColumns
    is_lipid = matched[hc.OUTCOME].isin(Constants.LIPID_OUTCOMES)
    expected = np.where(is_lipid, EffectScale.LINEAR, EffectScale.LOG_OR)
    is_expected = matched[hc.STUDY_EFFECT_SCALE].to_numpy() == expected
    dropped = matched.loc[~is_expected]
    counts = dropped.groupby(
        [hc.STUDY_ACCESSION, hc.STUDY_EFFECT_SCALE], dropna=False
    ).size()
    for (accession, scale), n in counts.items():
        log_info(
            f"{accession}: {n} rows on scale {scale}, not the expected "
            "one for their outcome; dropped"
        )
    log_info(
        f"--require-expected-scale: {len(dropped)} of {len(matched)} rows "
        f"of {dropped[hc.STUDY_ACCESSION].nunique()} studies dropped"
    )
    return matched.loc[is_expected].copy()


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
def therapy_sign(genes: pd.Series) -> np.ndarray:
    """Sign that turns a lower-function effect into the therapeutic one.

    Parameters
    ----------
    genes : `pd.Series`
        Gene per row.

    Returns
    -------
    sign : `np.ndarray`
        -1.0 for genes whose drugs raise gene function
        (`TherapyDirection.RAISING` in `Constants.THERAPY_DIRECTION`),
        else 1.0.

    Raises
    ------
    ValueError
        If a gene has no entry in `Constants.THERAPY_DIRECTION`.
    """
    missing = sorted(set(genes.dropna()) - set(Constants.THERAPY_DIRECTION))
    if missing:
        raise ValueError(
            f"no therapeutic direction for {', '.join(missing)}: add to "
            "Constants.THERAPY_DIRECTION"
        )
    raising = genes.map(Constants.THERAPY_DIRECTION).eq(
        TherapyDirection.RAISING
    )
    return np.where(raising, -1.0, 1.0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_therapy_direction(table: pd.DataFrame) -> pd.DataFrame:
    """Add `MetaColumns.THERAPY_DIRECTION` from the gene column.

    Parameters
    ----------
    table : `pd.DataFrame`
        An output table with `VariantListColumns.OUT_GENE` (a single gene
        or genes joined with ";").

    Returns
    -------
    table : `pd.DataFrame`
        Copy with `THERAPY_DIRECTION` right after the gene column.

    Raises
    ------
    ValueError
        If a row's genes have different therapeutic directions.
    """
    def direction(genes: object) -> str | None:
        """The one direction of a row's ";"-joined genes."""
        if not isinstance(genes, str) or not genes:
            return None
        found = {Constants.THERAPY_DIRECTION[gene] for gene in
                 genes.split(";")}
        if len(found) > 1:
            raise ValueError(f"genes {genes}: conflicting therapy direction")
        return found.pop()

    table = table.copy()
    gene = VariantListColumns.OUT_GENE
    values = table[gene].map(direction)
    table.insert(table.columns.get_loc(gene) + 1,
                 MetaColumns.THERAPY_DIRECTION, values)
    return table


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def orient(rows: pd.DataFrame) -> pd.DataFrame:
    """Orient every row's effect per variant.

    The a2 allele is used, or a1 when any of the variant's list sources
    is `Constants.GOF_VARIANT_SOURCE` or `Constants.
    SELECTED_GOF_VARIANT_SOURCE` (`a2_gof_flipped`) or any of its
    rows has `clinvar_direction` `raising` (`a2_clinvar_raising_flipped`;
    GoF wins when both apply). So every effect is that of lower gene
    function. Then genes whose drugs raise gene function are flipped
    (`therapy_sign`), so every effect is in the therapeutic direction;
    `ORIENTED_ALLELE` follows both flips, `ORIENTATION` names only the
    first.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `prepare_effects`.

    Returns
    -------
    oriented : `pd.DataFrame`
        `rows` plus `ORIENTATION`, `ORIENTED_ALLELE` and `BETA_ORIENTED`.

    Raises
    ------
    ValueError
        If a variant site is listed under genes with different therapy
        directions (its rows are pooled together).
    """
    site = MetaColumns.VARIANT_SITE
    gof_sites = set(
        rows.loc[
            rows[VariantListColumns.OUT_SOURCE].isin(
                [
                    Constants.GOF_VARIANT_SOURCE,
                    Constants.SELECTED_GOF_VARIANT_SOURCE,
                ]
            ),
            site,
        ]
    )

    raising_sites = set(
        rows.loc[
            rows[VariantListColumns.OUT_CLINVAR_DIRECTION]
            == ClinVarDirection.RAISING,
            site,
        ]
    )

    is_gof = rows[site].isin(gof_sites)
    is_raising = rows[site].isin(raising_sites)
    therapy = therapy_sign(rows[VariantListColumns.OUT_GENE])
    mixed = (pd.Series(therapy, index=rows.index)
             .groupby(rows[site]).nunique() > 1)
    if mixed.any():
        raise ValueError(
            "site(s) listed under genes with different therapy "
            f"directions: {', '.join(mixed.index[mixed])}"
        )
    sign = np.where(is_gof | is_raising, -1.0, 1.0) * therapy
    oriented = rows.copy()
    oriented[MetaColumns.ORIENTATION] = np.select(
        [is_gof, is_raising],
        [Orientation.A2_GOF_FLIPPED, Orientation.A2_CLINVAR_RAISING_FLIPPED],
        default=Orientation.A2,
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
    flipped = sorted(set(rows.loc[therapy < 0, VariantListColumns.OUT_GENE]))
    if flipped:
        log_info(
            f"{', '.join(flipped)}: flipped to the therapeutic direction "
            "(drugs raise gene function)"
        )
    clinvar = oriented.drop_duplicates(
        [site, VariantListColumns.OUT_CLINVAR_DIRECTION]
    )[VariantListColumns.OUT_CLINVAR_DIRECTION].dropna()
    for direction, n in clinvar.value_counts().items():
        log_info(f"{n} ClinVar variants with direction {direction}")
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
        `STUDY_MAF` (when the rows have a MAF column), `COPIED_STUDIES`
        (``""`` when none) and the
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
    if HarmonisedColumns.MAF in rows.columns:
        extra[MetaColumns.STUDY_MAF] = grouped[
            [HarmonisedColumns.STUDY_ACCESSION, HarmonisedColumns.MAF]
        ].apply(_join_study_maf)
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
def _keep_values(
    rows: pd.DataFrame, column: str, values: list[str] | None
) -> pd.DataFrame:
    """Keep the rows whose `column` is one of `values`, and log it.

    Parameters
    ----------
    rows : `pd.DataFrame`
        Rows to filter.
    column : `str`
        Column to filter on.
    values : `list[str]` or `None`
        Values to keep; `None` keeps every row.

    Returns
    -------
    kept : `pd.DataFrame`
        The kept rows; requested values without any row are warned.
    """
    if values is None:
        return rows
    keep = rows[column].isin(values)
    log_info(
        f"{column} in {', '.join(values)}: {int(keep.sum())} of "
        f"{len(rows)} rows kept"
    )
    absent = sorted(set(values) - set(rows.loc[keep, column]))
    if absent:
        log_warn(f"no rows with {column} {', '.join(absent)}")
    return rows.loc[keep].copy()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stratified(
    rows: pd.DataFrame, keys: list[str], copies: pd.DataFrame
) -> pd.DataFrame:
    """Describe each study's (stratum's) own estimate per variant.

    Parameters
    ----------
    rows : `pd.DataFrame`
        As for `meta_analyse`; one row per study and group.
    keys : `list[str]`
        Grouping columns, without study accession.
    copies : `pd.DataFrame`
        As for `meta_analyse`.

    Returns
    -------
    per_study : `pd.DataFrame`
        `meta_analyse` output per group and study accession (one
        estimate each, so `meta_beta` is the study's oriented beta).
    """
    return meta_analyse(
        rows, [*keys, HarmonisedColumns.STUDY_ACCESSION], copies
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_burden(
    rows: pd.DataFrame,
    keys: list[str],
    ukb: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Pool the oriented variant effects per gene, per study and overall.

    Rare variants are taken as independent, so the IVW of the oriented
    betas over a gene's variants approximates a burden test whose sign
    is the effect of the function-altering allele.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `orient`, deduped (one row per study, variant and group).
    keys : `list[str]`
        Grouping columns, including `MetaColumns.VARIANT_SITE`, which is
        replaced by the variant-list gene.
    ukb : `pd.DataFrame` or `None`, optional, default: `None`
        UKB carrier-burden rows (`ukb_burden_rows`), one per gene, other
        keys and study. When given, they replace the IVW over variants of
        those studies (their per-variant rows are left out here) as the
        studies' stratum estimates.

    Returns
    -------
    burden : `pd.DataFrame`
        `level` ``stratum``: per gene, other keys and study, the IVW over
        variants (`n_estimates` = variants, Q across variants).
        `level` ``pooled``: per gene and other keys, the IVW of the
        stratum estimates (identical to pooling all estimates; Q across
        studies, `n_variants` = distinct variants over studies).
    """
    gene = VariantListColumns.OUT_GENE
    study = HarmonisedColumns.STUDY_ACCESSION
    site = MetaColumns.VARIANT_SITE
    gene_keys = [gene, *(key for key in keys if key != site)]
    study_keys = [*gene_keys, study]
    if ukb is not None:
        # per gene, outcome and study, so a gene without a UKB burden
        # keeps its UKB per-variant rows
        triple = [gene, HarmonisedColumns.OUTCOME, study]
        has_burden = set(map(tuple, ukb[triple].to_numpy()))
        is_ukb = pd.Series(
            [key in has_burden for key in map(tuple, rows[triple].to_numpy())],
            index=rows.index,
            dtype=bool,
        )
        log_info(
            f"gene burden: {int(is_ukb.sum())} per-variant rows of the UKB "
            f"burden studies replaced by {len(ukb)} carrier-burden rows"
        )
        rows = rows.loc[~is_ukb]

    per_study = ivw(rows, study_keys, MetaColumns.BETA_ORIENTED)
    grouped = rows.groupby(study_keys, sort=True, dropna=False)
    extra = pd.DataFrame(
        {
            MetaColumns.N_VARIANTS: grouped[site].nunique(),
            MetaColumns.VARIANTS: grouped[site].agg(_join_unique),
        }
    )
    if HarmonisedColumns.TRAIT_LABEL in rows.columns:
        extra[HarmonisedColumns.TRAIT_LABEL] = grouped[
            HarmonisedColumns.TRAIT_LABEL
        ].agg(_join_unique)
    per_study = per_study.merge(extra.reset_index(), on=study_keys)
    if ukb is not None and not ukb.empty:
        per_study = pd.concat(
            [per_study, _ukb_stratum_rows(ukb, study_keys)],
            ignore_index=True,
        )
    per_study.insert(0, MetaColumns.LEVEL, MetaLevel.STRATUM)

    # second stage: the stratum estimates are the inputs
    stage_two = per_study.rename(
        columns={
            MetaColumns.BETA: "_stratum_beta",
            MetaColumns.SE: MetaColumns.SE_USED,
        }
    )
    pooled = ivw(stage_two, gene_keys, "_stratum_beta")
    # from the stratum rows, so the UKB carrier-burden sites count too
    over_genes = per_study.groupby(gene_keys, sort=True, dropna=False)
    variants = over_genes[MetaColumns.VARIANTS].agg(_join_variant_lists)
    extra = pd.DataFrame(
        {
            MetaColumns.N_VARIANTS: variants.map(
                lambda joined: len(joined.split(";")) if joined else 0
            ),
            MetaColumns.VARIANTS: variants,
            MetaColumns.N_STUDIES: over_genes[study].nunique(),
            MetaColumns.STUDIES: over_genes[study].agg(_join_unique),
        }
    )
    pooled = pooled.merge(extra.reset_index(), on=gene_keys)
    pooled.insert(0, MetaColumns.LEVEL, MetaLevel.POOLED)

    burden = pd.concat([pooled, per_study], ignore_index=True)
    burden = burden.sort_values(
        [*gene_keys, MetaColumns.LEVEL, study],
        kind="stable",
        na_position="first",
    ).reset_index(drop=True)
    log_info(
        f"gene burden: {len(pooled)} pooled and {len(per_study)} "
        "per-study rows"
    )
    return burden


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _join_variant_lists(values: pd.Series) -> str:
    """Join ``;``-separated variant lists into one sorted unique list.

    Parameters
    ----------
    values : `pd.Series`
        `MetaColumns.VARIANTS` cells of one group.

    Returns
    -------
    joined : `str`
        ``""`` when every cell is missing or blank.
    """
    sites = {
        site
        for cell in values.dropna().astype(str)
        for site in cell.split(";")
        if site
    }
    return ";".join(sorted(sites))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ukb_stratum_rows(ukb: pd.DataFrame, study_keys: list[str]) -> pd.DataFrame:
    """Format UKB carrier-burden rows as `gene_burden` stratum rows.

    Parameters
    ----------
    ukb : `pd.DataFrame`
        `ukb_burden_rows` output.
    study_keys : `list[str]`
        `gene_burden` gene keys plus the study accession.

    Returns
    -------
    rows : `pd.DataFrame`
        `study_keys`, `N_ESTIMATES` (1), `BETA`, `SE`, `Z`, `P`, `Q`,
        `Q_DF`, `I2` (NA), `N_VARIANTS`, `VARIANTS` and the trait label.
    """
    missing = [key for key in study_keys if key not in ukb.columns]
    if missing:
        raise ValueError(f"UKB burden rows lack key column(s) {missing}")
    beta = ukb[MetaColumns.BETA_ORIENTED].astype(float)
    se = ukb[MetaColumns.SE_USED].astype(float)
    z = beta / se
    out = ukb[study_keys].copy()
    out[MetaColumns.N_ESTIMATES] = 1
    out[MetaColumns.BETA] = beta
    out[MetaColumns.SE] = se
    out[MetaColumns.Z] = z
    out[MetaColumns.P] = _ERFC(z.abs().to_numpy() / math.sqrt(2))
    for column in (MetaColumns.Q, MetaColumns.Q_DF, MetaColumns.I2):
        out[column] = np.nan
    out[MetaColumns.N_VARIANTS] = ukb[MetaColumns.N_VARIANTS]
    out[MetaColumns.VARIANTS] = ukb[MetaColumns.VARIANTS]
    out[HarmonisedColumns.TRAIT_LABEL] = ukb[HarmonisedColumns.TRAIT_LABEL]
    return out.reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ukb_base_mask(variant_sources: list[str] | None) -> str:
    """Return the burden mask that matches the run's variant sources.

    Parameters
    ----------
    variant_sources : `list[str]` or `None`
        `--variant-sources` of the run.

    Returns
    -------
    mask : `str`
        The `Constants.BURDEN_VARIANT_SETS` key whose sources equal the
        run's (e.g. `BURDEN_MASK_GOF` for GoF, `BURDEN_MASK_LOF` for PTV
        and ClinVar).

    Raises
    ------
    ValueError
        If no variant set has exactly these sources (or none are given):
        no carrier burden matches such a run.
    """
    sources = set(variant_sources or [])
    for mask, mask_sources in Constants.BURDEN_VARIANT_SETS.items():
        if sources == set(mask_sources):
            return mask
    raise ValueError(
        "--ukb-burden needs --variant-sources of one variant set: "
        + "; ".join(
            " ".join(mask_sources)
            for mask_sources in Constants.BURDEN_VARIANT_SETS.values()
        )
        + f" (got {sorted(sources) or 'all'})"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_ukb_burden(
    ancestry: str,
    studies: list[str] | None,
    outcomes: list[str] | None,
    variant_sources: list[str] | None,
    path: Path = FileNames.MATCHED_BURDEN,
    summary_path: Path = FileNames.BURDEN_EXPOSURE_SUMMARY,
) -> pd.DataFrame:
    """Read the UKB carrier-burden rows of the run's mask.

    Parameters
    ----------
    ancestry : `str`
        The run's `Ancestry` code (``MULTI``: every row, relabelled).
    studies, outcomes : `list[str]` or `None`
        `--studies` and `--outcomes`; `None` keeps all.
    variant_sources : `list[str]` or `None`
        `--variant-sources`, which pick the mask (`_ukb_base_mask`).
    path : `Path`, optional, default: `FileNames.MATCHED_BURDEN`
        match_variants.py output.
    summary_path : `Path`, optional
        burden_exposure.py summary, for each exposure's sites.

    Returns
    -------
    ukb : `pd.DataFrame`
        One row per gene, outcome, ancestry, study and mask (the base
        mask and its fallback form):
        `OUT_GENE`, `OUTCOME`, `ANCESTRY_GROUP`, `STUDY_ACCESSION`,
        `_MASK_KEY`, `BETA_ORIENTED`, `SE_USED`, `N_VARIANTS`,
        `VARIANTS`, `TRAIT_LABEL`.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist (rerun match_variants.py).
    """
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found: rerun match_variants.py after the burden "
            "results are in marvel_results.tsv"
        )
    base = _ukb_base_mask(variant_sources)
    suffix = Constants.BURDEN_FALLBACK_SUFFIX
    wanted = {base, f"{base}{suffix}"}
    table = pd.read_csv(path, sep="\t", low_memory=False)
    parsed = table[_EXPOSURE_COLUMN].astype(str).str.extract(_GENE_MASK_RE)
    table[VariantListColumns.OUT_GENE] = parsed["gene"]
    table[_MASK_KEY] = parsed["mask"]
    keep = (
        table[_MASK_KEY].isin(wanted)
        & ~table[VariantListColumns.OUT_GENE].isin(Constants.EXCLUDED_GENES)
    )
    ancestry_col = HarmonisedColumns.ANCESTRY_GROUP
    if ancestry != Ancestry.MULTI:
        keep &= table[ancestry_col] == ancestry
    if studies is not None:
        keep &= table[HarmonisedColumns.STUDY_ACCESSION].isin(studies)
    if outcomes is not None:
        keep &= table[HarmonisedColumns.OUTCOME].isin(outcomes)
    ukb = table.loc[keep].copy()
    if ancestry == Ancestry.MULTI:
        ukb[ancestry_col] = Ancestry.MULTI
    beta = pd.to_numeric(ukb[HarmonisedColumns.BETA], errors="coerce")
    se = pd.to_numeric(ukb[HarmonisedColumns.SE], errors="coerce")
    usable = beta.notna() & se.notna() & (se > 0)
    if (~usable).any():
        log_warn(f"{int((~usable).sum())} UKB burden rows without beta/SE")
    ukb, beta, se = ukb.loc[usable], beta[usable], se[usable]
    # as `orient` flips GoF sites: every effect is that of lower function
    sign = -1.0 if base == Constants.BURDEN_MASK_GOF else 1.0
    # then, as `orient`, the therapeutic direction
    ukb[MetaColumns.BETA_ORIENTED] = beta * sign * therapy_sign(
        ukb[VariantListColumns.OUT_GENE]
    )
    ukb[MetaColumns.SE_USED] = se
    ukb[MetaColumns.N_VARIANTS] = pd.NA
    ukb[MetaColumns.VARIANTS] = pd.NA
    if summary_path.exists():
        summary = pd.read_csv(summary_path, sep="\t", dtype=str)
        sites = dict(zip(summary["exposure"], summary["sites"].fillna("")))
        exposure = ukb[_EXPOSURE_COLUMN].astype(str)
        ukb[MetaColumns.VARIANTS] = exposure.map(sites)
        ukb[MetaColumns.N_VARIANTS] = ukb[MetaColumns.VARIANTS].map(
            lambda joined: len(joined.split(";"))
            if isinstance(joined, str) and joined else 0
        )
    else:
        log_warn(f"{summary_path} not found: UKB burden sites unknown")
    keys = [
        VariantListColumns.OUT_GENE, HarmonisedColumns.OUTCOME,
        ancestry_col, HarmonisedColumns.STUDY_ACCESSION, _MASK_KEY,
    ]
    twice = ukb.duplicated(keys, keep=False)
    if twice.any():
        log_warn(
            f"{int(twice.sum())} UKB burden rows share gene, outcome, "
            "study and mask: the first is kept"
        )
        ukb = ukb.drop_duplicates(keys)
    columns = [
        *keys, MetaColumns.BETA_ORIENTED, MetaColumns.SE_USED,
        MetaColumns.N_VARIANTS, MetaColumns.VARIANTS,
        HarmonisedColumns.TRAIT_LABEL,
    ]
    ukb = ukb[columns].reset_index(drop=True)
    log_info(
        f"UKB carrier burden ({base}"
        + (", gof negated" if sign < 0 else "")
        + f"): {len(ukb)} rows, "
        + ", ".join(
            f"{mask} {n}"
            for mask, n in sorted(ukb[_MASK_KEY].value_counts().items())
        )
    )
    return ukb


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ukb_burden_rows(
    ukb: pd.DataFrame,
    rows: pd.DataFrame,
    variant_sources: list[str] | None,
    prefer: list[str] | None,
    fallback: list[str] | None,
) -> pd.DataFrame:
    """Pick per gene, outcome and UKB study the mask to use.

    When a `prefer` group has rows for a gene and outcome and the UKB
    study is in a `fallback` group, the fallback mask (`_fb`: only the
    sites the preferred studies lack) is used, as `choose_groups` does
    per variant; otherwise the full mask.

    Parameters
    ----------
    ukb : `pd.DataFrame`
        `load_ukb_burden` output, after `_add_apoe_strata`.
    rows : `pd.DataFrame`
        The run's per-variant rows, after `choose_groups`.
    variant_sources : `list[str]` or `None`
        `--variant-sources` (`_ukb_base_mask`).
    prefer, fallback : `list[str]` or `None`
        `--prefer-groups` and `--fallback-groups`.

    Returns
    -------
    chosen : `pd.DataFrame`
        One row per gene, outcome, ancestry and study.
    """
    base = _ukb_base_mask(variant_sources)
    pair = [VariantListColumns.OUT_GENE, HarmonisedColumns.OUTCOME]
    has_prefer: set[tuple] = set()
    if prefer:
        is_prefer = rows[MetaColumns.STUDY_GROUP].isin(prefer)
        has_prefer = set(
            map(tuple, rows.loc[is_prefer, pair].drop_duplicates().to_numpy())
        )
    use_fallback = (
        pd.Series(list(map(tuple, ukb[pair].to_numpy())), index=ukb.index)
        .isin(has_prefer)
        & ukb[MetaColumns.STUDY_GROUP].isin(fallback or [])
    )
    wanted = np.where(
        use_fallback, f"{base}{Constants.BURDEN_FALLBACK_SUFFIX}", base
    )
    chosen = ukb.loc[ukb[_MASK_KEY] == wanted].copy()
    n_fallback = int((chosen[_MASK_KEY] != base).sum())
    log_info(
        f"UKB carrier burden: {len(chosen)} rows of mask {base}, "
        f"{n_fallback} as {base}{Constants.BURDEN_FALLBACK_SUFFIX} "
        "(preferred groups have the gene and outcome)"
    )
    study_keys = [
        *pair, HarmonisedColumns.ANCESTRY_GROUP,
        HarmonisedColumns.STUDY_ACCESSION,
    ]
    chosen_keys = set(map(tuple, chosen[study_keys].to_numpy()))
    needs = ukb.loc[use_fallback & (ukb[_MASK_KEY] == base), study_keys]
    lost = [key for key in map(tuple, needs.to_numpy())
            if key not in chosen_keys]
    if lost:
        log_warn(
            f"{len(lost)} UKB gene/outcome/study rows have no fallback "
            "burden (no carriers outside the preferred sites): UKB left "
            "out there"
        )
    return chosen.reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def meta_analysis(
    ancestry: str,
    studies: list[str] | None = None,
    outcomes: list[str] | None = None,
    variant_sources: list[str] | None = None,
    per_study: bool = False,
    label: str | None = None,
    require_log_or: bool = False,
    prefer_groups: list[str] | None = None,
    fallback_groups: list[str] | None = None,
    ukb_burden: bool = False,
    require_expected_scale: bool = False,
    gene_level: bool = True,
) -> None:
    """Run the meta-analysis for one ancestry group and write it.

    Writes the per-variant meta-analysis and (unless `gene_level` is
    False) the gene burden.

    Studies are grouped with `load_apoe_strata`. The pooled run uses per
    study group its unstratified study, or else its strata
    (`_pooled_rows`). When strata are present, they are also pooled per
    `apoe_stratum` (suffix ``_<label>_apoe_strata``, with the same
    sensitivity files).

    Parameters
    ----------
    ancestry : `str`
        An `Ancestry` code; only rows with this `ancestry_group` are
        pooled. ``MULTI`` pools every row, whatever its ancestry (after
        the study/outcome filters, relabelled ``MULTI``).
    studies : `list[str]` or `None`, optional, default: `None`
        Study accessions to keep; `None` keeps all.
    outcomes : `list[str]` or `None`, optional, default: `None`
        Outcomes to keep; `None` keeps all.
    variant_sources : `list[str]` or `None`, optional, default: `None`
        Variant-list sources to keep (e.g. ``PTV``, ``ClinVar``); applied
        after orientation, so GoF flips still see every list. `None`
        keeps all. ClinVar is the P/LP list of `annotate_clinvar.py`.
    per_study : `bool`, optional, default: `False`
        Also write each study's own per-variant estimate (`level`
        ``stratum``) next to the pooled rows.
    label : `str` or `None`, optional, default: `None`
        Appended to the output file names as ``_<label>``.
    require_log_or : `bool`, optional, default: `False`
        Drop studies whose `study_effect_scale` is not log-OR
        (`check_effect_scales`); otherwise they are only warned about.
    prefer_groups : `list[str]` or `None`, optional, default: `None`
        Study groups (`load_apoe_strata`; an unlisted study is its own
        group, named by its accession) used per variant (gene, outcome,
        site) when they have it; see `choose_groups`. `None` keeps every
        group.
    fallback_groups : `list[str]` or `None`, optional, default: `None`
        Study groups used for a variant only when no `prefer_groups`
        group has it.
    ukb_burden : `bool`, optional, default: `False`
        In the gene burden, use the UKB carrier-burden estimates
        (`FileNames.MATCHED_BURDEN`, `load_ukb_burden`) instead of the IVW
        over UKB's variants; the per-variant tables are unchanged. With
        no per-variant rows left, only the gene burden is written.
    require_expected_scale : `bool`, optional, default: `False`
        Drop rows not on their outcome's expected effect scale
        (`keep_expected_scales`: linear for lipids, log-OR otherwise).
    gene_level : `bool`, optional, default: `True`
        Also write the gene burden (IVW over a gene's variants); False
        writes the per-variant tables only (variants reported one by
        one, e.g. `Constants.SELECTED_GOF_VARIANT_SOURCE`).

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If there is no matched-variants table, or no matched-burden table
        with `ukb_burden`.
    ValueError
        If `ukb_burden` is combined with variant sources no carrier
        burden matches, or with `gene_level` False.
    """
    if ukb_burden and not gene_level:
        raise ValueError("ukb_burden needs the gene burden (gene_level)")
    if ukb_burden:
        _ukb_base_mask(variant_sources)
    keys = list(MetaColumns.KEYS)
    log_info(f"ancestry {ancestry}, pooled by {', '.join(keys)}")

    rows = _prepare_rows(
        ancestry, studies, outcomes, variant_sources, require_log_or,
        require_expected_scale,
    )
    if rows is None:
        if not ukb_burden:
            return
        log_info(
            "no per-variant rows: the gene burden is the UKB carrier "
            "burden only, no per-variant table written"
        )
        rows = _empty_rows(keys)

    log_stage("apoe_strata")
    strata = load_apoe_strata()
    rows = _add_apoe_strata(rows, strata)
    if prefer_groups and not rows.empty:
        log_stage("choose_groups")
        rows = choose_groups(rows, prefer_groups, fallback_groups or [])
        if rows.empty and not ukb_burden:
            log_warn("no rows left after choosing groups; no output written")
            return
    ukb: pd.DataFrame | None = None
    if ukb_burden:
        log_stage("ukb_burden")
        loaded = _add_apoe_strata(
            load_ukb_burden(ancestry, studies, outcomes, variant_sources),
            strata,
        )
        ukb = ukb_burden_rows(
            loaded, rows, variant_sources, prefer_groups, fallback_groups,
        )

    suffix = f"_{label}" if label else ""
    log_stage("pooled_run")
    _analyse_and_write(
        _pooled_rows(rows), keys, ancestry, per_study, suffix,
        None if ukb is None else _pooled_rows(ukb), gene_level,
    )

    is_stratum = rows[MetaColumns.APOE_STRATUM] != ApoeStratum.ALL
    # the UKB carrier burden has its own strata, also when no per-variant
    # rows of a stratum are left
    ukb_strata = ukb is not None and bool(
        (ukb[MetaColumns.APOE_STRATUM] != ApoeStratum.ALL).any()
    )
    if is_stratum.any() or ukb_strata:
        log_stage("apoe_strata_run")
        log_info(
            f"{int(is_stratum.sum())} rows from APOE strata: pooled per "
            "stratum"
        )
        _analyse_and_write(
            rows.loc[is_stratum].copy(),
            [*keys, MetaColumns.APOE_STRATUM],
            ancestry,
            per_study,
            f"{suffix}_{Constants.APOE_STRATA_LABEL}",
            None if ukb is None else ukb.loc[
                ukb[MetaColumns.APOE_STRATUM] != ApoeStratum.ALL
            ].copy(),
            gene_level,
        )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _prepare_rows(
    ancestry: str,
    studies: list[str] | None,
    outcomes: list[str] | None,
    variant_sources: list[str] | None,
    require_log_or: bool,
    require_expected_scale: bool = False,
) -> pd.DataFrame | None:
    """Load, filter and orient the run's per-variant rows.

    Parameters
    ----------
    ancestry, studies, outcomes, variant_sources, require_log_or
        As `meta_analysis`.
    require_expected_scale : `bool`, optional, default: `False`
        As `meta_analysis`.

    Returns
    -------
    rows : `pd.DataFrame` or `None`
        From `orient`, after the variant-source filter; `None` (logged)
        when no rows are left.
    """
    log_stage("load_matched")
    matched = load_matched(FileNames.MATCHED_VARIANTS)
    is_excluded = matched[VariantListColumns.OUT_GENE].isin(
        Constants.EXCLUDED_GENES
    )
    log_info(
        f"{int(is_excluded.sum())} rows of excluded gene(s) "
        f"{', '.join(Constants.EXCLUDED_GENES)} dropped"
    )
    matched = matched.loc[~is_excluded].copy()
    ancestry_col = HarmonisedColumns.ANCESTRY_GROUP
    pool_all = ancestry == Ancestry.MULTI
    if pool_all:
        is_ancestry = pd.Series(True, index=matched.index)
    else:
        is_ancestry = matched[ancestry_col] == ancestry
    counts = matched[ancestry_col].value_counts()
    log_info(
        f"{int(is_ancestry.sum())} of {len(matched)} rows "
        + ("kept (MULTI pools every ancestry) " if pool_all else
           f"are {ancestry} ")
        + "(all: "
        + ", ".join(f"{code}={n}" for code, n in sorted(counts.items()))
        + ")"
    )
    if not is_ancestry.any():
        log_warn(f"no {ancestry} rows, nothing to pool; no output written")
        return None
    matched = matched.loc[is_ancestry].copy()
    matched = _keep_values(
        matched, HarmonisedColumns.STUDY_ACCESSION, studies
    )
    matched = _keep_values(matched, HarmonisedColumns.OUTCOME, outcomes)
    if pool_all:
        # one ancestry_group so every study is pooled together
        kept = matched[ancestry_col].value_counts()
        log_info(
            f"MULTI: {len(matched)} rows pooled across ancestries ("
            + ", ".join(f"{code}={n}" for code, n in sorted(kept.items()))
            + f"), relabelled {Ancestry.MULTI}; a study reported both per "
            "ancestry and combined is counted twice unless --studies "
            "excludes one"
        )
        matched[ancestry_col] = Ancestry.MULTI
    log_stage("effect_scale")
    matched = check_effect_scales(matched, require_log_or)
    if require_expected_scale:
        matched = keep_expected_scales(matched)
    if matched.empty:
        log_warn("no rows left after filtering; no output written")
        return None

    log_stage("prepare_effects")
    rows = prepare_effects(matched)
    del matched

    log_stage("resolve_ambiguous")
    rows = resolve_ambiguous(rows)

    log_stage("orient")
    rows = orient(rows)
    rows = _keep_values(rows, VariantListColumns.OUT_SOURCE, variant_sources)
    if rows.empty:
        log_warn("no rows left after filtering; no output written")
        return None
    return rows


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _empty_rows(keys: list[str]) -> pd.DataFrame:
    """Per-variant rows without any row, for a UKB-burden-only run.

    Parameters
    ----------
    keys : `list[str]`
        Grouping columns (`MetaColumns.KEYS`).

    Returns
    -------
    rows : `pd.DataFrame`
        No rows; the columns the APOE-strata, group and `gene_burden`
        steps read.
    """
    columns = [
        VariantListColumns.OUT_GENE, *keys,
        HarmonisedColumns.STUDY_ACCESSION, MetaColumns.BETA_ORIENTED,
        MetaColumns.SE_USED, HarmonisedColumns.TRAIT_LABEL,
        VariantListColumns.OUT_SOURCE,
        VariantListColumns.OUT_CLINVAR_DIRECTION,
    ]
    return pd.DataFrame(columns=list(dict.fromkeys(columns)))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_apoe_strata(path: Path = FileNames.APOE_STRATA) -> pd.DataFrame:
    """Read the curated study accession -> study group and APOE stratum.

    See `data/raw/apoe_strata.SOURCE.md`.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.APOE_STRATA`
        TSV with `study_accession`, `study_group` and `apoe_stratum`.

    Returns
    -------
    strata : `pd.DataFrame`
        The table, all columns as strings, `apoe_stratum` lower-cased.
        Empty (but correctly columned) if `path` does not exist.

    Raises
    ------
    ValueError
        If a column is missing, an accession is listed twice, a
        `study_group` is blank or an `apoe_stratum` is not in
        `ApoeStratum.CODES` or `ApoeStratum.ALL`.
    """
    columns = [
        HarmonisedColumns.STUDY_ACCESSION,
        MetaColumns.STUDY_GROUP,
        MetaColumns.APOE_STRATUM,
    ]
    if not path.exists():
        log_warn(f"{path} not found: every study is unstratified")
        return pd.DataFrame(columns=columns)
    strata = pd.read_csv(path, sep="\t", dtype=str).fillna("")
    missing = [column for column in columns if column not in strata.columns]
    if missing:
        raise ValueError(f"{path}: missing column(s) {missing}")
    strata = strata[columns].apply(lambda column: column.str.strip())
    strata[MetaColumns.APOE_STRATUM] = strata[
        MetaColumns.APOE_STRATUM
    ].str.lower()
    duplicated = sorted(
        set(
            strata.loc[
                strata[HarmonisedColumns.STUDY_ACCESSION].duplicated(),
                HarmonisedColumns.STUDY_ACCESSION,
            ]
        )
    )
    if duplicated:
        raise ValueError(f"{path}: accession(s) listed twice {duplicated}")
    if (strata[MetaColumns.STUDY_GROUP] == "").any():
        raise ValueError(f"{path}: blank study_group")
    allowed = ApoeStratum.CODES | {ApoeStratum.ALL}
    bad = sorted(set(strata[MetaColumns.APOE_STRATUM]) - allowed)
    if bad:
        raise ValueError(
            f"{path}: unknown apoe_stratum value(s) {bad}, expected one "
            f"of {sorted(allowed)}"
        )
    log_info(f"{path}: {len(strata)} studies with an APOE stratum entry")
    return strata


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _add_apoe_strata(
    rows: pd.DataFrame, strata: pd.DataFrame
) -> pd.DataFrame:
    """Add each row's study group and APOE stratum.

    Parameters
    ----------
    rows : `pd.DataFrame`
        Rows with `study_accession`.
    strata : `pd.DataFrame`
        From `load_apoe_strata`.

    Returns
    -------
    labelled : `pd.DataFrame`
        `rows` plus `study_group` and `apoe_stratum`; a study not in
        `strata` is its own group (its accession) with stratum
        `ApoeStratum.ALL`.
    """
    accession = HarmonisedColumns.STUDY_ACCESSION
    lookup = strata.set_index(accession)
    labelled = rows.copy()
    labelled[MetaColumns.STUDY_GROUP] = (
        labelled[accession]
        .map(lookup[MetaColumns.STUDY_GROUP])
        .fillna(labelled[accession])
    )
    labelled[MetaColumns.APOE_STRATUM] = (
        labelled[accession]
        .map(lookup[MetaColumns.APOE_STRATUM])
        .fillna(ApoeStratum.ALL)
    )
    listed_groups = set(strata[MetaColumns.STUDY_GROUP])
    studies = labelled.drop_duplicates(accession)
    counts = studies.groupby(
        [MetaColumns.STUDY_GROUP, MetaColumns.APOE_STRATUM]
    ).size()
    for (group, stratum), n in counts.items():
        if group in listed_groups:
            log_info(f"study group {group}, stratum {stratum}: {n} studies")
    return labelled


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _pooled_rows(rows: pd.DataFrame) -> pd.DataFrame:
    """Keep the rows used for the pooled (all APOE genotypes) run.

    Per study group: its unstratified (`ApoeStratum.ALL`) studies when it
    has any, otherwise its strata (pooled = the IVW of the strata).

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `_add_apoe_strata`.

    Returns
    -------
    pooled_rows : `pd.DataFrame`
        The kept rows.
    """
    group = MetaColumns.STUDY_GROUP
    is_all = rows[MetaColumns.APOE_STRATUM] == ApoeStratum.ALL
    groups_with_all = set(rows.loc[is_all, group])
    keep = is_all | ~rows[group].isin(groups_with_all)
    stratum_groups = sorted(set(rows.loc[~is_all, group]))
    for name in stratum_groups:
        rule = (
            "unstratified run, strata left out"
            if name in groups_with_all
            else "IVW of the strata"
        )
        log_info(f"pooled run, study group {name}: {rule}")
    return rows.loc[keep].copy()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def choose_groups(
    rows: pd.DataFrame, prefer: list[str], fallback: list[str]
) -> pd.DataFrame:
    """Per variant, keep the preferred or else the fallback groups.

    For each variant-list gene, outcome and variant site: when any row
    (any APOE stratum) comes from a `prefer` study group, the `fallback`
    groups' rows are dropped; otherwise the `fallback` rows are kept.
    Rows of other groups are always kept. Used to avoid sample overlap:
    Thomassen (prefer) holds UKB and FinnGen (fallback), so these add
    only the variants Thomassen does not have.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `_add_apoe_strata`, after orientation and the variant-source
        filter.
    prefer : `list[str]`
        Preferred `study_group` values.
    fallback : `list[str]`
        Fallback `study_group` values.

    Returns
    -------
    chosen : `pd.DataFrame`
        The kept rows.

    Raises
    ------
    ValueError
        If a group is in both `prefer` and `fallback`.
    """
    both = sorted(set(prefer) & set(fallback))
    if both:
        raise ValueError(f"group(s) both preferred and fallback: {both}")
    group = rows[MetaColumns.STUDY_GROUP]
    absent = sorted((set(prefer) | set(fallback)) - set(group))
    if absent:
        log_warn(f"no rows from study group(s) {', '.join(absent)}")
    keys = [
        VariantListColumns.OUT_GENE,
        HarmonisedColumns.OUTCOME,
        MetaColumns.VARIANT_SITE,
    ]
    is_prefer = group.isin(prefer)
    is_fallback = group.isin(fallback)
    has_prefer = is_prefer.groupby(
        [rows[key] for key in keys], dropna=False
    ).transform("any")
    keep = ~is_fallback | ~has_prefer
    used = rows.loc[keep & (is_prefer | is_fallback)]
    for (gene, outcome), part in used.groupby(keys[:2], dropna=False):
        sites = part.groupby(MetaColumns.STUDY_GROUP)[
            MetaColumns.VARIANT_SITE
        ].nunique()
        log_info(
            f"{gene}, {outcome}: "
            + ", ".join(f"{name} {n} variants" for name, n in sites.items())
        )
    log_info(
        f"{int((~keep).sum())} fallback rows dropped for variants a "
        "preferred group has"
    )
    return rows.loc[keep].copy()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _analyse_and_write(
    rows: pd.DataFrame,
    keys: list[str],
    ancestry: str,
    per_study: bool,
    suffix: str,
    ukb: pd.DataFrame | None = None,
    gene_level: bool = True,
) -> None:
    """Dedupe the oriented rows, pool them, add the burden and write both.

    Without per-variant rows only the UKB carrier burden is written;
    without `gene_level` only the per-variant table.

    Parameters
    ----------
    rows : `pd.DataFrame`
        From `orient`, after the variant-source filter.
    keys : `list[str]`
        Grouping columns (`MetaColumns.KEYS`).
    ancestry : `str`
        The run's `Ancestry` code, used in the file names.
    per_study : `bool`
        Also write each study's own per-variant estimate.
    suffix : `str`
        Appended to the file names (``""`` or ``_<label>...``).
    ukb : `pd.DataFrame` or `None`, optional, default: `None`
        UKB carrier-burden rows (`ukb_burden_rows`).
    gene_level : `bool`, optional, default: `True`
        Also write the gene burden.

    Returns
    -------
    `None`
    """
    if rows.empty:
        if ukb is None:
            log_warn(f"no rows for {suffix or 'the run'}; no output written")
            return
        # UKB carrier burden only: no per-variant table
        log_stage("gene_burden")
        burden = add_therapy_direction(gene_burden(rows, keys, ukb))
        log_stage("write")
        Paths.RESULTS_OUTPUT.mkdir(parents=True, exist_ok=True)
        path = Paths.RESULTS_OUTPUT / FileNames.BURDEN_TEMPLATE.format(
            ancestry=ancestry, suffix=suffix
        )
        functions.write_table_atomic(burden, path)
        log_info(f"wrote {len(burden)} rows to {path}")
        return

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
    pooled.insert(0, MetaColumns.LEVEL, MetaLevel.POOLED)
    if per_study:
        per_study_rows = stratified(rows, keys, copies)
        per_study_rows.insert(0, MetaColumns.LEVEL, MetaLevel.STRATUM)
        pooled = pd.concat(
            [pooled, per_study_rows], ignore_index=True
        ).sort_values(
            [*keys, MetaColumns.LEVEL, HarmonisedColumns.STUDY_ACCESSION],
            kind="stable",
            na_position="first",
        )

    outputs = [
        (FileNames.META_ANALYSIS_TEMPLATE, add_therapy_direction(pooled),
         suffix),
    ]
    if gene_level:
        log_stage("gene_burden")
        burden = gene_burden(rows, keys, ukb)
        outputs.append(
            (FileNames.BURDEN_TEMPLATE, add_therapy_direction(burden),
             suffix)
        )
    else:
        log_info("no gene burden (--no-gene-burden)")

    log_stage("write")
    Paths.RESULTS_OUTPUT.mkdir(parents=True, exist_ok=True)
    for template, table, file_suffix in outputs:
        path = Paths.RESULTS_OUTPUT / template.format(
            ancestry=ancestry, suffix=file_suffix
        )
        functions.write_table_atomic(table, path)
        log_info(f"wrote {len(table)} rows to {path}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Fixed-effect IVW meta-analysis of the matched variants."
    )
    parser.add_argument(
        "--ancestry",
        type=str.upper,
        choices=sorted(Ancestry.CODES),
        default=MetaColumns.DEFAULT_ANCESTRY,
        help="ancestry group to pool (default: %(default)s)",
    )
    parser.add_argument(
        "--studies",
        nargs="+",
        metavar="ACCESSION",
        help="study accessions to keep (default: all)",
    )
    parser.add_argument(
        "--outcomes",
        nargs="+",
        metavar="OUTCOME",
        help="outcomes to keep (default: all)",
    )
    parser.add_argument(
        "--variant-sources",
        nargs="+",
        metavar="SOURCE",
        help=(
            "variant-list sources to keep, e.g. PTV ClinVar (default: all); "
            "ClinVar is the P/LP list of annotate_clinvar.py, raising "
            "variants flipped"
        ),
    )
    parser.add_argument(
        "--stratified",
        action="store_true",
        help="also write each study's (stratum's) own per-variant estimate",
    )
    parser.add_argument(
        "--label",
        help="suffix for the output file names (meta_<ancestry>_<label>)",
    )
    parser.add_argument(
        "--require-log-or",
        action="store_true",
        help=(
            "drop studies whose effect scale is not log-OR (linear, log-HR, "
            "unknown, conflict); default: warn and keep them"
        ),
    )
    parser.add_argument(
        "--prefer-groups",
        nargs="+",
        metavar="GROUP",
        help=(
            "study groups (apoe_strata.tsv study_group, else the accession) "
            "used per variant (gene, outcome, site) when they have it; "
            "needs --fallback-groups"
        ),
    )
    parser.add_argument(
        "--fallback-groups",
        nargs="+",
        metavar="GROUP",
        help=(
            "study groups used for a variant only when no "
            "--prefer-groups group has it"
        ),
    )
    parser.add_argument(
        "--ukb-burden",
        action="store_true",
        help=(
            "gene burden: UKB carrier-burden estimates "
            f"({FileNames.MATCHED_BURDEN.name}, burden_exposure.py) instead "
            "of the IVW over UKB's variants; needs --variant-sources GoF "
            "or PTV/ClinVar"
        ),
    )
    parser.add_argument(
        "--require-expected-scale",
        action="store_true",
        help=(
            "drop rows not on their outcome's expected effect scale "
            "(linear for lipids, log-OR otherwise); default: keep them"
        ),
    )
    parser.add_argument(
        "--no-gene-burden",
        action="store_true",
        help=(
            "write only the per-variant table, no gene burden (variants "
            f"reported one by one, e.g. "
            f"{Constants.SELECTED_GOF_VARIANT_SOURCE})"
        ),
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    args = parser.parse_args()
    if bool(args.prefer_groups) != bool(args.fallback_groups):
        parser.error("--prefer-groups and --fallback-groups go together")
    if args.ukb_burden and args.no_gene_burden:
        parser.error("--ukb-burden needs the gene burden (no "
                     "--no-gene-burden)")
    if args.require_log_or and args.require_expected_scale:
        parser.error("--require-log-or and --require-expected-scale "
                     "exclude each other")
    return args


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.META_ANALYSIS):
        meta_analysis(
            args.ancestry,
            studies=args.studies,
            outcomes=args.outcomes,
            variant_sources=args.variant_sources,
            per_study=args.stratified,
            label=args.label,
            require_log_or=args.require_log_or,
            prefer_groups=args.prefer_groups,
            fallback_groups=args.fallback_groups,
            ukb_burden=args.ukb_burden,
            require_expected_scale=args.require_expected_scale,
            gene_level=not args.no_gene_burden,
        )


if __name__ == "__main__":
    main()
