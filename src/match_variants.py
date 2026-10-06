#!/usr/bin/env python3
"""
Matches the variant-level GWAS lookups in the merged associations table to the
per-gene variant lists (`data/temp/*_variants.tsv`), excluding the
AlphaMissense (`AM`) entries, and writes the matched rows.

The `ClinVar` entries of the per-gene lists are replaced by the ClinVar P/LP
list (`data/processed/plp_variants.tsv`), each variant labelled with the
lipid direction of its conditions (`data/raw/clinvar_condition_direction.tsv`).
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    ClinVarColumnNames,
    ClinVarDirection,
    ColumnNames,
    ConditionDirectionColumns,
    Constants,
    FileNames,
    HarmonisedColumns,
    Paths,
    RunlogOrder,
    VariantListColumns,
)


# an allele usable for matching; anything else ("?", "NA", "-") is blank
_ALLELE_PATTERN: str = r"[ACGT]+"
# helper columns, dropped before writing
_ROW_KEY: str = "_row"
_CHROM_KEY: str = "_chrom"
_POS_KEY: str = "_pos"
_EFFECT_KEY: str = "_effect"
_OTHER_KEY: str = "_other"
_CONSEQUENCE_KEY: str = "_consequence"
# variant-list columns renamed for the output, in output order
_LIST_OUTPUT_COLUMNS: dict[str, str] = {
    VariantListColumns.SOURCE: VariantListColumns.OUT_SOURCE,
    VariantListColumns.GENE: VariantListColumns.OUT_GENE,
    VariantListColumns.A1: VariantListColumns.OUT_A1,
    VariantListColumns.A2: VariantListColumns.OUT_A2,
    VariantListColumns.TRI_CLASS: VariantListColumns.OUT_TRI_CLASS,
    VariantListColumns.POS_ORIG: VariantListColumns.OUT_POS_ORIG,
    VariantListColumns.A1_ORIG: VariantListColumns.OUT_A1_ORIG,
    VariantListColumns.A2_ORIG: VariantListColumns.OUT_A2_ORIG,
    VariantListColumns.NORM_STATUS: VariantListColumns.OUT_NORM_STATUS,
    VariantListColumns.CLINVAR_DIRECTION: (
        VariantListColumns.OUT_CLINVAR_DIRECTION
    ),
}


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
def _clean_alleles(alleles: pd.Series) -> pd.Series:
    """Upper-case alleles and blank out values that are not A/C/G/T runs.

    Parameters
    ----------
    alleles : `pd.Series`
        Allele strings, possibly NA, ``"?"`` or lower case.

    Returns
    -------
    cleaned : `pd.Series`
        Plain `str` values; ``""`` where the allele is missing or
        unusable, so equality tests never meet NA.
    """
    upper = alleles.astype("string").str.strip().str.upper()
    valid = upper.str.fullmatch(_ALLELE_PATTERN).fillna(False).astype(bool)
    return upper.where(valid, "").fillna("").astype(str)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _read_gene_regions() -> dict[str, tuple[str, int, int]]:
    """Read the flanked gene regions frozen by `gwas_cat_prep.py`.

    Returns
    -------
    regions : `dict[str, tuple[str, int, int]]`
        `gene` -> `(chrom, start, end)`; empty (warned) if
        `FileNames.GENE_REGIONS_FILE` does not exist.
    """
    if not FileNames.GENE_REGIONS_FILE.exists():
        log_warn(
            f"{FileNames.GENE_REGIONS_FILE} not found: rows outside the "
            "gene region are not counted"
        )
        return {}
    table = pd.read_csv(
        FileNames.GENE_REGIONS_FILE,
        sep="\t",
        dtype={ColumnNames.CHROM: str},
    )
    chroms = _normalise_chrom(table[ColumnNames.CHROM])
    return {
        gene: (chrom, int(start), int(end))
        for gene, chrom, start, end in zip(
            table[ColumnNames.GENE],
            chroms,
            table[ColumnNames.START],
            table[ColumnNames.END],
        )
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _in_region(
    variants: pd.DataFrame, regions: dict[str, tuple[str, int, int]]
) -> pd.Series:
    """Flag variant-list rows that lie inside their gene's region.

    Parameters
    ----------
    variants : `pd.DataFrame`
        Variant-list rows with `_CHROM_KEY` and `_POS_KEY` set.
    regions : `dict[str, tuple[str, int, int]]`
        From `_read_gene_regions`.

    Returns
    -------
    inside : `pd.Series`
        `bool` per row; `False` for genes without a region.
    """
    # NA checks first: comparing pd.NA gives NA, which `and` cannot test
    inside = [
        not pd.isna(chrom)
        and not pd.isna(pos)
        and gene in regions
        and chrom == regions[gene][0]
        and regions[gene][1] <= pos <= regions[gene][2]
        for gene, chrom, pos in zip(
            variants[VariantListColumns.GENE],
            variants[_CHROM_KEY],
            variants[_POS_KEY],
        )
    ]
    return pd.Series(inside, index=variants.index, dtype=bool)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _collapse_direction(directions: pd.Series) -> str:
    """Combine the condition directions of one variant into one value.

    Parameters
    ----------
    directions : `pd.Series`
        `ClinVarDirection` values of the variant's conditions.

    Returns
    -------
    direction : `str`
        `lowering`, `raising` or `altered` when only that one occurs among
        the known directions, `conflicting` when more than one occurs,
        else `unknown`.
    """
    known = set(directions) & {
        ClinVarDirection.LOWERING,
        ClinVarDirection.RAISING,
        ClinVarDirection.ALTERED,
    }
    if len(known) > 1:
        return ClinVarDirection.CONFLICTING
    if len(known) == 1:
        return known.pop()
    return ClinVarDirection.UNKNOWN


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_plp_variants() -> pd.DataFrame:
    """Read the ClinVar P/LP list as variant-list rows with a direction.

    The GRCh38 coordinates are used (`Constants.PLP_ASSEMBLY_SUFFIX`).
    Each row's condition gets its direction from
    `FileNames.CLINVAR_CONDITION_DIRECTION`; conditions missing there are
    `unknown` (warned). The directions are combined per variant by
    `_collapse_direction`, except that a variant with a consequence in
    `Constants.TRUNCATING_CONSEQUENCES` is always `lowering` (less gene
    product, whatever the conditions say).

    Returns
    -------
    plp : `pd.DataFrame`
        One row per variant, with the `VariantListColumns` `chr`, `pos`,
        `a1` (reference), `a2` (alternate), `source`
        (`Constants.CLINVAR_VARIANT_SOURCE`), `gene` and
        `clinvar_direction`, as strings.

    Raises
    ------
    FileNotFoundError
        If the P/LP list or the condition-direction table does not exist.
    """
    for path in (FileNames.PLP_VARIANTS, FileNames.CLINVAR_CONDITION_DIRECTION):
        if not path.exists():
            raise FileNotFoundError(f"{path} not found")
    cv = ClinVarColumnNames
    cd = ConditionDirectionColumns
    vc = VariantListColumns
    suffix = Constants.PLP_ASSEMBLY_SUFFIX
    plp = pd.read_csv(FileNames.PLP_VARIANTS, sep="\t", dtype=str)
    directions = pd.read_csv(
        FileNames.CLINVAR_CONDITION_DIRECTION, sep="\t", dtype=str
    )
    log_info(
        f"{FileNames.PLP_VARIANTS}: {len(plp)} rows; "
        f"{FileNames.CLINVAR_CONDITION_DIRECTION}: {len(directions)} rows"
    )

    variants = pd.DataFrame(
        {
            vc.CHROM: pd.to_numeric(
                plp[f"{cv.CHR_COL}{suffix}"], errors="coerce"
            ).astype("Int64"),
            vc.POS: pd.to_numeric(
                plp[f"{cv.POSITION_VCF_COL}{suffix}"], errors="coerce"
            ).astype("Int64"),
            vc.A1: plp[f"{cv.REFERENCE_ALLELE_COL}{suffix}"],
            vc.A2: plp[f"{cv.ALTERNATE_ALLELE_COL}{suffix}"],
            vc.SOURCE: Constants.CLINVAR_VARIANT_SOURCE,
            vc.GENE: plp[cv.GENE_SYMBOL_COL],
            cd.CONDITION: plp[cv.RCV_CONDITION_COL],
            _CONSEQUENCE_KEY: plp[cv.RCV_MOLECULAR_CONSEQUENCE_COL],
        }
    )
    variants[vc.CHROM] = variants[vc.CHROM].astype("string")
    variants[vc.POS] = variants[vc.POS].astype("string")
    # reference records (e.g. APOE3 isoform "c.388=") are not variants
    is_ref = variants[vc.A1].notna() & (variants[vc.A1] == variants[vc.A2])
    log_info(f"{int(is_ref.sum())} P/LP rows with ref = alt dropped")
    variants = variants.loc[~is_ref].merge(
        directions.rename(columns={cd.GENE: vc.GENE}),
        on=[vc.GENE, cd.CONDITION],
        how="left",
    )
    missing = variants.loc[
        variants[cd.DIRECTION].isna(), [vc.GENE, cd.CONDITION]
    ].drop_duplicates()
    for gene, condition in missing.itertuples(index=False):
        log_warn(
            f"{gene} condition '{condition}' not in "
            f"{FileNames.CLINVAR_CONDITION_DIRECTION}: counted as unknown"
        )
    variants[cd.DIRECTION] = variants[cd.DIRECTION].fillna(
        ClinVarDirection.UNKNOWN
    )

    site = [vc.CHROM, vc.POS, vc.A1, vc.A2, vc.SOURCE, vc.GENE]
    collapsed = (
        variants.groupby(site, dropna=False, sort=True)[cd.DIRECTION]
        .agg(_collapse_direction)
        .rename(vc.CLINVAR_DIRECTION)
        .reset_index()
    )
    truncating = (
        variants[_CONSEQUENCE_KEY]
        .isin(Constants.TRUNCATING_CONSEQUENCES)
        .groupby([variants[col] for col in site], dropna=False, sort=True)
        .any()
        .to_numpy()
    )
    overruled = truncating & (
        collapsed[vc.CLINVAR_DIRECTION] != ClinVarDirection.LOWERING
    )
    log_info(
        f"{int(truncating.sum())} truncating P/LP variants set to "
        f"{ClinVarDirection.LOWERING}, {int(overruled.sum())} of them "
        "against their conditions"
    )
    collapsed.loc[truncating, vc.CLINVAR_DIRECTION] = ClinVarDirection.LOWERING
    counts = collapsed.groupby(
        [vc.GENE, vc.CLINVAR_DIRECTION], sort=True
    ).size()
    for (gene, direction), n in counts.items():
        log_info(f"{gene} ClinVar P/LP: {n} variants {direction}")
    return collapsed


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_variant_lists() -> pd.DataFrame:
    """Read the per-gene variant lists and keep the matchable entries.

    `Constants.EXCLUDED_VARIANT_SOURCES` rows and exact duplicate rows
    are dropped. The lists' `Constants.CLINVAR_VARIANT_SOURCE` rows are
    replaced by the P/LP list (`load_plp_variants`), the only rows with a
    `clinvar_direction`. Per gene and source the rows, the rows without both
    alleles (dropped, they cannot be matched) and the rows outside the
    gene region are logged.

    Returns
    -------
    variants : `pd.DataFrame`
        Variant-list columns plus `_CHROM_KEY` (no ``chr`` prefix),
        `_POS_KEY` (`Int64`) and cleaned `a1`/`a2`, normalised by
        `_normalise_variant_list` (originals in `pos_orig`/`a1_orig`/
        `a2_orig`, plus `norm_status`); only rows with a position and
        both alleles.

    Raises
    ------
    FileNotFoundError
        If no file matches `Constants.VARIANT_LIST_GLOB`.
    """
    paths = sorted(Paths.DATA_TEMP.glob(Constants.VARIANT_LIST_GLOB))
    if not paths:
        raise FileNotFoundError(
            f"no {Constants.VARIANT_LIST_GLOB} files in {Paths.DATA_TEMP}"
        )
    variants = pd.concat(
        [pd.read_csv(path, sep="\t", dtype=str) for path in paths],
        ignore_index=True,
    )
    log_info(
        f"{len(paths)} variant lists, {len(variants)} rows: "
        + ", ".join(path.name for path in paths)
    )

    excluded = variants[VariantListColumns.SOURCE].isin(
        Constants.EXCLUDED_VARIANT_SOURCES
    )
    log_info(
        f"{int(excluded.sum())} rows with source in "
        f"{sorted(Constants.EXCLUDED_VARIANT_SOURCES)} skipped"
    )
    variants = variants[~excluded]
    is_clinvar = (
        variants[VariantListColumns.SOURCE] == Constants.CLINVAR_VARIANT_SOURCE
    )
    log_info(
        f"{int(is_clinvar.sum())} {Constants.CLINVAR_VARIANT_SOURCE} rows "
        f"of the lists dropped, replaced by {FileNames.PLP_VARIANTS}"
    )
    variants = pd.concat(
        [variants[~is_clinvar], load_plp_variants()], ignore_index=True
    )
    n_before = len(variants)
    variants = variants.drop_duplicates().reset_index(drop=True)
    log_info(f"{n_before - len(variants)} duplicate rows removed")

    variants[_CHROM_KEY] = _normalise_chrom(
        variants[VariantListColumns.CHROM]
    )
    variants[_POS_KEY] = pd.to_numeric(
        variants[VariantListColumns.POS], errors="coerce"
    ).astype("Int64")
    for column in (VariantListColumns.A1, VariantListColumns.A2):
        variants[column] = _clean_alleles(variants[column])

    usable = (
        variants[_POS_KEY].notna()
        & (variants[VariantListColumns.A1] != "")
        & (variants[VariantListColumns.A2] != "")
    )
    regions = _read_gene_regions()
    inside = _in_region(variants, regions)
    grouped = variants.groupby(
        [VariantListColumns.GENE, VariantListColumns.SOURCE], sort=True
    )
    for (gene, source), group in grouped:
        log_info(
            f"{gene} {source}: {len(group)} rows, "
            f"{int((~usable[group.index]).sum())} without alleles, "
            f"{int((~inside[group.index]).sum())} outside gene region"
        )
    return _normalise_variant_list(
        variants[usable].reset_index(drop=True), regions
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _normalise_variant_list(
    variants: pd.DataFrame, regions: dict[str, tuple[str, int, int]]
) -> pd.DataFrame:
    """Left-align and trim the variant-list entries against GRCh38.

    Uses `functions.normalise_variant` (the same normalisation as the
    merged associations), with `a1` as other and `a2` as effect allele, so
    list entries and GWAS rows meet in the same form.

    Parameters
    ----------
    variants : `pd.DataFrame`
        Usable variant-list rows, with `_CHROM_KEY`, `_POS_KEY` and
        cleaned `a1`/`a2`.
    regions : `dict[str, tuple[str, int, int]]`
        From `_read_gene_regions`; their reference sequences are fetched
        (or read from the Ensembl cache).

    Returns
    -------
    normalised : `pd.DataFrame`
        `variants` with `_POS_KEY`, `a1` and `a2` normalised, the values
        before in `pos_orig`/`a1_orig`/`a2_orig`, and `norm_status`.
        Counts per status, and entries where `a2` rather than `a1` is the
        reference allele, are logged.

    Raises
    ------
    ReaderError
        If a reference sequence cannot be fetched from Ensembl.
    """
    vc = VariantListColumns
    normalised = variants.copy()
    normalised[vc.POS_ORIG] = normalised[_POS_KEY]
    normalised[vc.A1_ORIG] = normalised[vc.A1]
    normalised[vc.A2_ORIG] = normalised[vc.A2]
    sequences = functions.region_sequences(
        {
            gene: functions.GeneRegion(chrom=chrom, start=start, end=end)
            for gene, (chrom, start, end) in regions.items()
        }
    )
    results = [
        functions.normalise_variant(chrom, pos, a2, a1, sequences)
        for chrom, pos, a1, a2 in zip(
            normalised[_CHROM_KEY],
            normalised[_POS_KEY],
            normalised[vc.A1],
            normalised[vc.A2],
        )
    ]
    normalised[_POS_KEY] = pd.array(
        [result.pos for result in results], dtype="Int64"
    )
    normalised[vc.A2] = [result.effect for result in results]
    normalised[vc.A1] = [result.other for result in results]
    normalised[vc.NORM_STATUS] = [result.status for result in results]

    counts = normalised[vc.NORM_STATUS].value_counts()
    log_info(
        "normalisation: variant-list rows "
        + " ".join(f"{k}={n}" for k, n in counts.items())
    )
    n_a2_ref = sum(result.effect_is_ref is True for result in results)
    if n_a2_ref:
        log_warn(
            f"variant lists: {n_a2_ref} rows where a2, not a1, is the "
            "GRCh38 reference allele"
        )
    return normalised


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_gwas_rows() -> pd.DataFrame:
    """Read the variant-level rows of the merged associations table.

    Returns
    -------
    gwas : `pd.DataFrame`
        Rows whose `source` is in `Constants.VARIANT_LEVEL_SOURCES` and
        that have chrom, pos and a usable effect allele, with helper
        columns `_ROW_KEY` (original row order), `_CHROM_KEY`, `_POS_KEY`,
        `_EFFECT_KEY` and `_OTHER_KEY` (``""`` if missing).

    Raises
    ------
    FileNotFoundError
        If `FileNames.MERGED_ASSOCIATIONS` does not exist (run merge first).
    """
    if not FileNames.MERGED_ASSOCIATIONS.exists():
        raise FileNotFoundError(
            f"{FileNames.MERGED_ASSOCIATIONS} not found: run "
            "merge_associations.py first"
        )
    results = pd.read_csv(
        FileNames.MERGED_ASSOCIATIONS,
        sep="\t",
        dtype={
            HarmonisedColumns.CHROM: str,
            HarmonisedColumns.EFFECT_ALLELE: str,
            HarmonisedColumns.OTHER_ALLELE: str,
        },
        low_memory=False,
    )
    gwas = results[
        results[HarmonisedColumns.SOURCE].isin(Constants.VARIANT_LEVEL_SOURCES)
    ].copy()
    log_info(
        f"{FileNames.MERGED_ASSOCIATIONS}: {len(results)} rows, {len(gwas)} "
        f"variant-level ({', '.join(Constants.VARIANT_LEVEL_SOURCES)})"
    )
    del results

    gwas[_ROW_KEY] = gwas.index
    gwas[_CHROM_KEY] = _normalise_chrom(gwas[HarmonisedColumns.CHROM])
    gwas[_POS_KEY] = pd.to_numeric(
        gwas[HarmonisedColumns.POS], errors="coerce"
    ).astype("Int64")
    gwas[_EFFECT_KEY] = _clean_alleles(gwas[HarmonisedColumns.EFFECT_ALLELE])
    gwas[_OTHER_KEY] = _clean_alleles(gwas[HarmonisedColumns.OTHER_ALLELE])

    usable = (
        gwas[_CHROM_KEY].notna()
        & gwas[_POS_KEY].notna()
        & (gwas[_EFFECT_KEY] != "")
    )
    unusable = gwas.loc[~usable, HarmonisedColumns.SOURCE].value_counts()
    for source, n in unusable.items():
        log_info(
            f"{source}: {n} rows without chrom/pos or effect allele, "
            "cannot be matched"
        )
    return gwas[usable].reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def match_rows(gwas: pd.DataFrame, variants: pd.DataFrame) -> pd.DataFrame:
    """Pair GWAS rows with variant-list rows at the same site and alleles.

    A GWAS row with both alleles matches when `{effect, other}` equals
    `{a1, a2}`, in either order. A row with only an effect allele
    (curated) matches when the effect allele is `a1` or `a2`, so at a
    multi-allelic site it can match several list rows.

    Parameters
    ----------
    gwas : `pd.DataFrame`
        From `load_gwas_rows`.
    variants : `pd.DataFrame`
        From `load_variant_lists`.

    Returns
    -------
    matched : `pd.DataFrame`
        One row per (GWAS row, variant-list row) pair: the merged-associations
        columns, then the `VariantListColumns.OUT_*` columns,
        `effect_allele_is` and `match_alleles`; in merged-associations row
        order. Helper columns are removed.
    """
    keys = [_CHROM_KEY, _POS_KEY]
    list_columns = keys + list(_LIST_OUTPUT_COLUMNS)
    pairs = gwas[[_ROW_KEY, *keys, _EFFECT_KEY, _OTHER_KEY]].merge(
        variants[list_columns], on=keys, how="inner"
    )
    effect = pairs[_EFFECT_KEY]
    other = pairs[_OTHER_KEY]
    a1 = pairs[VariantListColumns.A1]
    a2 = pairs[VariantListColumns.A2]
    has_other = other != ""
    effect_is_a2 = (effect == a2) & (~has_other | (other == a1))
    effect_is_a1 = (effect == a1) & (~has_other | (other == a2))
    pairs[VariantListColumns.EFFECT_ALLELE_IS] = np.where(
        effect_is_a2, "a2", "a1"
    )
    pairs[VariantListColumns.MATCH_ALLELES] = np.where(
        has_other, "both", "effect_only"
    )
    pairs = pairs[effect_is_a2 | effect_is_a1].rename(
        columns=_LIST_OUTPUT_COLUMNS
    )

    added = [
        *_LIST_OUTPUT_COLUMNS.values(),
        VariantListColumns.EFFECT_ALLELE_IS,
        VariantListColumns.MATCH_ALLELES,
    ]
    helpers = [_ROW_KEY, _CHROM_KEY, _POS_KEY, _EFFECT_KEY, _OTHER_KEY]
    result_columns = [col for col in gwas.columns if col not in helpers]
    matched = gwas[[_ROW_KEY, *result_columns]].merge(
        pairs[[_ROW_KEY, *added]], on=_ROW_KEY, how="inner"
    )
    matched = matched.sort_values(
        [_ROW_KEY, VariantListColumns.OUT_SOURCE], kind="stable"
    )
    return matched.drop(columns=_ROW_KEY).reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _log_match_summary(
    variants: pd.DataFrame, matched: pd.DataFrame
) -> None:
    """Log matched variants and GWAS rows per gene and list source.

    Parameters
    ----------
    variants : `pd.DataFrame`
        From `load_variant_lists`.
    matched : `pd.DataFrame`
        From `match_rows`.

    Returns
    -------
    `None`
    """
    site = [_CHROM_KEY, _POS_KEY, VariantListColumns.A1, VariantListColumns.A2]
    out_site = [
        HarmonisedColumns.CHROM,
        HarmonisedColumns.POS,
        VariantListColumns.OUT_A1,
        VariantListColumns.OUT_A2,
    ]
    grouped = variants.groupby(
        [VariantListColumns.GENE, VariantListColumns.SOURCE], sort=True
    )
    for (gene, source), group in grouped:
        rows = matched[
            (matched[VariantListColumns.OUT_GENE] == gene)
            & (matched[VariantListColumns.OUT_SOURCE] == source)
        ]
        by_source = " ".join(
            f"{gwas_source}={n}"
            for gwas_source, n in rows[HarmonisedColumns.SOURCE]
            .value_counts()
            .items()
        )
        log_info(
            f"{gene} {source}: {len(group.drop_duplicates(site))} "
            f"variants, {len(rows.drop_duplicates(out_site))} matched, "
            f"GWAS rows: {by_source or 'none'}"
        )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _check_a1_is_ref(matched: pd.DataFrame) -> None:
    """Log how often list `a1` differs from the Ensembl reference allele.

    Tests the assumption that `a1` is the GRCh38 reference allele, using
    the ref in `ensembl_variant_id` (``chrom:pos:ref:alt``). Only SNVs
    are checked: Ensembl writes indels in its own (unnormalised) form,
    so indels are checked against the reference sequence instead (see
    `_normalise_variant_list`). Skipped when the merged associations predate
    that column.

    Parameters
    ----------
    matched : `pd.DataFrame`
        From `match_rows`.

    Returns
    -------
    `None`
    """
    column = HarmonisedColumns.ENSEMBL_VARIANT_ID
    if column not in matched.columns:
        log_info(f"no {column} column: a1-vs-Ensembl-ref check skipped")
        return
    ref = matched[column].astype("string").str.split(":").str[2]
    a1 = matched[VariantListColumns.OUT_A1]
    a2 = matched[VariantListColumns.OUT_A2]
    snv = (a1.str.len() == 1) & (a2.str.len() == 1)
    checked = ref.notna() & snv
    differs = checked & (ref != a1)
    message = (
        f"a1 vs Ensembl ref: {int(checked.sum())} matched SNV rows checked, "
        f"{int(differs.sum())} where a1 is not the Ensembl ref"
    )
    if differs.any():
        examples = ", ".join(
            matched.loc[differs, column].drop_duplicates().head(3)
        )
        log_warn(f"{message} (e.g. {examples})")
    else:
        log_info(message)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def match_variants() -> None:
    """Match merged-associations GWAS rows to the variant lists and write them.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If there are no variant lists or no merged associations table.
    """
    log_stage("load_variant_lists")
    variants = load_variant_lists()

    log_stage("load_gwas")
    gwas = load_gwas_rows()

    log_stage("match")
    matched = match_rows(gwas, variants)
    del gwas
    _log_match_summary(variants, matched)
    _check_a1_is_ref(matched)

    log_stage("write")
    Paths.RESULTS_OUTPUT.mkdir(parents=True, exist_ok=True)
    functions.write_table_atomic(matched, FileNames.MATCHED_VARIANTS)
    log_info(f"wrote {len(matched)} rows to {FileNames.MATCHED_VARIANTS}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    return argparse.ArgumentParser(
        description="Match GWAS lookups to the (non-AM) gene variant lists."
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    return parser.parse_args()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.MATCH_VARIANTS):
        match_variants()


if __name__ == "__main__":
    main()
