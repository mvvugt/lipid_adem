#!/usr/bin/env python3
"""annotate_clinvar

Extract ClinVar variants with an aggregate (variant-level) classification of
Pathogenic, Likely pathogenic or Pathogenic/Likely pathogenic
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations
from pathlib import Path

import pandas as pd

from log_tools.emitter import log_info, log_warn
from log_tools.setup import runlog_setup
from project_constants import (
    ClinVarColumnNames as CVCNames,
    Constants,
    FileNames,
    Paths,
)

COLUMNS_TO_KEEP = [v for k, v in vars(CVCNames).items() if not k.startswith('_')]

# Columns that differ between the two assembly rows of the same
# variant/condition pairing (coordinates, and occasionally alleles on a
# strand flip) -- widened into per-assembly columns by widen_by_assembly.
ASSEMBLY_SPECIFIC_COLUMNS: list[str] = [
    CVCNames.CHR_COL,
    CVCNames.START_COL,
    CVCNames.STOP_COL,
    CVCNames.POSITION_VCF_COL,
    CVCNames.REFERENCE_ALLELE_COL,
    CVCNames.ALTERNATE_ALLELE_COL,
]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# read


def read_clinvar_variants(path: Path) -> pd.DataFrame:
    """Read the raw ClinVar variant export.

    Parameters
    ----------
    path : `Path`
        Path to the ClinVar variant TSV export.

    Returns
    -------
    data : `pd.DataFrame`
        One row per (variant x condition x molecular consequence x RCV).

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"ClinVar variant file not found: {path}")

    log_info(f"Reading ClinVar variants from {path}")
    data = pd.read_csv(path, sep="\t")
    log_info(f"Read {len(data)} rows")
    return data


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# filter


def filter_plp_variants(data: pd.DataFrame) -> pd.DataFrame:
    """Filter to variants with an aggregate P/LP classification.

    Kept if the variant-level `ac_classification` is in
    `Constants.PATHOGENIC_CLASSIFICATIONS`. Conflicting, VUS and benign
    variants are dropped, whatever their per-condition
    `rcv_classification`. All condition rows of a kept variant are kept,
    so the lipid direction can still be derived per condition. Rows
    without an `assembly` (old records without coordinates) are dropped,
    as they cannot be matched.

    Parameters
    ----------
    data : `pd.DataFrame`
        Raw ClinVar variant rows, as returned by `read_clinvar_variants`.

    Returns
    -------
    filtered : `pd.DataFrame`
        Matching rows. No rows are deduplicated or collapsed.
    """
    pathogenic_mask = data[CVCNames.AC_CLASSIFICATION_COL].isin(
        Constants.PATHOGENIC_CLASSIFICATIONS
    )
    no_assembly_mask = pathogenic_mask & data[CVCNames.ASSEMBLY_COL].isna()
    log_info(
        f"{pathogenic_mask.sum()} rows have an aggregate P/LP "
        f"ac_classification; {no_assembly_mask.sum()} of them without an "
        "assembly dropped"
    )
    return data.loc[pathogenic_mask & ~no_assembly_mask].copy()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# scope-reduction summary


def _summarize_scope_reduction(
    filtered: pd.DataFrame,
    group_col: str,
    strictness_order: tuple[str, ...],
    core_label: str,
    all_included_label: str,
) -> pd.DataFrame:
    """Report unique-variant counts as a group column's scope narrows.

    Successively excludes `strictness_order` groups (broadest first),
    down to `core_label` only. A variant only counts as "removed" once
    it has no row left in any still-included group -- one with rows in
    both `core_label` and the next-narrowest group stays counted until
    that group is also excluded.

    Parameters
    ----------
    filtered : `pd.DataFrame`
        Output of `filter_plp_variants`, before column trimming (must
        still have `group_col` and `variation_id`).
    group_col : `str`
        Column being narrowed (e.g. `review_status`).
    strictness_order : `tuple[str, ...]`
        Values of `group_col`, broadest-to-exclude first; `core_label` is
        never included here and is never excluded.
    core_label : `str`
        The one value of `group_col` that is never excluded.
    all_included_label : `str`
        `scope` label for the first row, before anything is excluded.

    Returns
    -------
    summary : `pd.DataFrame`
        One row per scope, from broadest to strictest, with columns
        `scope`, `n_unique_variants`, `n_variants_removed_cumulative`,
        `n_variants_removed_this_step`.
    """
    rows = []
    baseline_variants: set | None = None
    previous_variants: set | None = None

    for n_excluded in range(len(strictness_order) + 1):
        excluded_groups = set(strictness_order[:n_excluded])
        included_mask = ~filtered[group_col].isin(excluded_groups)
        variants = set(
            filtered.loc[included_mask, CVCNames.VARIATION_ID_COL]
        )

        if n_excluded == 0:
            scope = all_included_label
            baseline_variants = variants
        else:
            included_groups = (core_label,) + tuple(
                group
                for group in reversed(strictness_order)
                if group not in excluded_groups
            )
            scope = "Include: " + " + ".join(included_groups)

        rows.append(
            {
                "scope": scope,
                "n_unique_variants": len(variants),
                "n_variants_removed_cumulative": len(
                    baseline_variants - variants
                ),
                "n_variants_removed_this_step": (
                    len(previous_variants - variants)
                    if previous_variants is not None
                    else 0
                ),
            }
        )
        previous_variants = variants

    return pd.DataFrame(rows)


def summarize_review_status_scope(filtered: pd.DataFrame) -> pd.DataFrame:
    """Report unique-variant counts as `rcv_review_status` scope narrows.

    Parameters
    ----------
    filtered : `pd.DataFrame`
        Output of `filter_plp_variants`, before column trimming.

    Returns
    -------
    summary : `pd.DataFrame`
        See `_summarize_scope_reduction`.
    """
    return _summarize_scope_reduction(
        filtered,
        group_col=CVCNames.RCV_REVIEW_STATUS_COL,
        strictness_order=Constants.REVIEW_STATUS_STRICTNESS_ORDER,
        core_label=Constants.REVIEW_STATUS_CORE,
        all_included_label="All review statuses (every tier included)",
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# column selection


def widen_by_assembly(deduped: pd.DataFrame) -> pd.DataFrame:
    """Pivot GRCh37/GRCh38 rows into per-assembly columns.

    Each variant/condition row is duplicated once per assembly (only
    `ASSEMBLY_SPECIFIC_COLUMNS` differ, e.g. on a strand flip); this
    pivots those wide (`chr` -> `chr_grch37`/`chr_grch38`) into one row
    per pairing. Raises, rather than catching, if a
    `(variant/condition, assembly)` combination isn't unique -- that
    would mean conflicting coordinates for the same variant, which must
    surface, not resolve silently.

    Parameters
    ----------
    deduped : `pd.DataFrame`
        Dataframe with only required columns and duplicate rows dropped.

    Returns
    -------
    wide : `pd.DataFrame`
        One row per variant/condition pairing, with
        `ASSEMBLY_SPECIFIC_COLUMNS` replaced by `<column>_<assembly>`
        columns for each assembly value present in the data.
    """
    key_cols = [
        col
        for col in deduped.columns
        if col not in ASSEMBLY_SPECIFIC_COLUMNS + [CVCNames.ASSEMBLY_COL]
    ]
    wide = deduped.set_index(key_cols + [CVCNames.ASSEMBLY_COL])[
        ASSEMBLY_SPECIFIC_COLUMNS
    ].unstack(CVCNames.ASSEMBLY_COL)
    wide.columns = [
        f"{column}_{assembly.lower()}" for column, assembly in wide.columns
    ]
    wide = wide.reset_index()
    log_info(
        f"Widened {len(deduped)} assembly-duplicated rows into "
        f"{len(wide)} variant/condition rows"
    )
    return wide


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main

if __name__ == "__main__":
    with runlog_setup(order=50, root=Paths.HERE):
        variants = read_clinvar_variants(FileNames.CLINVAR_VARIANTS)
        plp_variants = filter_plp_variants(variants)

        log_info(f"Kept {len(plp_variants)} rows after filtering")

        review_status_summary = summarize_review_status_scope(plp_variants)
        log_info(
            "Review-status scope-reduction summary:\n"
            f"{review_status_summary.to_string(index=False)}"
        )
        FileNames.VARIANTS_REVIEW_STATUS_SUMMARY.parent.mkdir(
            parents=True, exist_ok=True
        )
        review_status_summary.to_csv(
            FileNames.VARIANTS_REVIEW_STATUS_SUMMARY, sep="\t", index=False
        )
        log_info(
            "Wrote review-status summary to "
            f"{FileNames.VARIANTS_REVIEW_STATUS_SUMMARY}"
        )

        plp_variants = plp_variants[COLUMNS_TO_KEEP].drop_duplicates()
        plp_variants = widen_by_assembly(plp_variants)

        FileNames.PLP_VARIANTS.parent.mkdir(parents=True, exist_ok=True)
        log_info(
            f"{plp_variants[CVCNames.VCV_ACCESSION_COL].nunique()} "
            "unique variants identified"
        )
        log_info(f"Writing {len(plp_variants)} rows to {FileNames.PLP_VARIANTS}")
        plp_variants.to_csv(FileNames.PLP_VARIANTS, sep="\t", index=False)
