#!/usr/bin/env python3
"""
lipid_adem helper functions
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import ast
import gzip
import io
import json
import re
import time
import warnings
from collections.abc import Callable, Collection, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from biomed_api.errors import ReaderError
from biomed_api.readers.reader_ensembl import EnsemblReader
from biomed_api.readers.reader_gwascat import GwasCatalogReader
from biomed_api.readers.reader_uniprot import UniProtIdMappingReader
from log_tools.emitter import log_debug, log_info, log_warn

from project_constants import (
    ColumnNames,
    Constants,
    EnsemblAlleleCheck,
    EnsemblRsidCheck,
    FileNames,
    HarmonisedColumns,
    MafStatus,
    Paths,
    SourceColumnMaps,
)

# curated GWAS Catalog effect text, e.g. "0.18 g/l increase"
_CURATED_BETA_PATTERN = re.compile(
    r"""
    ^\s*
    (?P<value>[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)
    (?P<text>.*)$
    """,
    re.VERBOSE,
)
# curated GWAS Catalog risk-allele string, e.g. "rs183130-T" or "rs1-?"
_CURATED_ALLELE_PATTERN = re.compile(
    r"""
    ^(?P<rsid>[^-]+)
    -(?P<allele>.+)$
    """,
    re.VERBOSE,
)
# Ensembl alleles usable for the allele check ("-" = deletion/insertion
# side); records with e.g. "HGMD_MUTATION" alleles are skipped
_ENSEMBL_ALLELE_PATTERN = re.compile(r"^(?:[ACGT]+|-)$")
_RSID_PATTERN = re.compile(r"^rs\d+$")
# Ensembl mappings on primary assembly chromosomes (not patches/haplotypes)
_PRIMARY_CHROM_PATTERN = re.compile(r"^(?:\d+|X|Y|MT)$")
# source rsid cells can hold several ids, e.g. FinnGen "rs1,rs2"
_RSID_SPLIT_PATTERN = re.compile(r"[,;\s]+")
_CNV_TRAIT_PATTERN = re.compile(Constants.CNV_TRAIT_PATTERN, re.IGNORECASE)
_X_CHROM_TRAIT_PATTERN = re.compile(
    Constants.X_CHROM_TRAIT_PATTERN, re.IGNORECASE
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data containers

@dataclass
class GeneRegion:
    """A gene's genomic region.

    Attributes
    ----------
    chrom : `str`
        Chromosome name (e.g. "1", "X").
    start : `int`
        Region start (1-based).
    end : `int`
        Region end (1-based).
    """
    chrom: str
    start: int
    end: int


@dataclass
class GeneRecord:
    """A gene's Ensembl identity and (unflanked) region.

    Attributes
    ----------
    symbol : `str`
        Gene symbol as Ensembl reports it (`display_name`).
    ensembl_id : `str`
        Ensembl stable gene ID (ENSG...).
    region : `GeneRegion`
        The gene body's region.
    """
    symbol: str
    ensembl_id: str
    region: GeneRegion


@dataclass
class SumstatsSource:
    """A study's queryable summary-stats file and its column layout.

    Attributes
    ----------
    url : `str`
        URL of the sumstats file.
    is_tabix_indexed : `bool`
        `True` if a `.tbi` index sits next to `url` (query via
        `filter_sumstats_regions`), else `False` (query via
        `filter_raw_sumstats_regions`).
    chrom_col : `str`
        Name of the chromosome column to filter on.
    pos_col : `str`
        Name of the position column to filter on.
    maf_col : `str`
        Name of the allele-frequency column to filter on.
    """
    url: str
    is_tabix_indexed: bool
    chrom_col: str = "chromosome"
    pos_col: str = "base_pair_location"
    maf_col: str = "effect_allele_frequency"


class GeneTableError(ValueError):
    """A gene-table row cannot be resolved or its identifiers disagree."""


class SumstatsColumnError(ValueError):
    """A sumstats file lacks an expected chrom/pos/MAF column."""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def write_table_atomic(df: pd.DataFrame, path: Path, sep: str = "\t") -> None:
    """Write a table to disk atomically (stage-then-move).

    Writes to a sibling temp file first, then moves it into place, so a
    failed/interrupted write can never leave `path` (which may be a
    hand-maintained input file) partially written.

    Parameters
    ----------
    df : `pd.DataFrame`
        Table to write.
    path : `Path`
        Destination path. Gzip-compressed if it ends in `.gz`.
    sep : `str`, optional, default: `"\\t"`
        Field separator.

    Returns
    -------
    `None`
    """
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    # the ".tmp" suffix stops pandas inferring compression, so set it here
    compression = "gzip" if path.suffix == ".gz" else None
    df.to_csv(tmp_path, sep=sep, index=False, compression=compression)
    tmp_path.replace(path)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def archive_dir(path: Path) -> Path | None:
    """Rename an existing directory aside, stamped with its mtime.

    The new name is `<name>_<mtime %Y%m%d_%H%M%S>` in the same parent
    directory, with `_1`, `_2`, ... appended if that name is taken, so
    nothing is ever overwritten.

    Parameters
    ----------
    path : `Path`
        Directory to archive.

    Returns
    -------
    archived : `Path` or `None`
        The directory's new path, or `None` if `path` did not exist.

    Notes
    -----
    Used to move an old pyjasub log directory out of the way: pyjasub
    errors when the job-array file is newer than an existing log dir. The
    mtime (not "now") is used so the name reflects the run the logs
    belong to. A same-directory rename is atomic.
    """
    if not path.exists():
        return None
    stamp = time.strftime(
        "%Y%m%d_%H%M%S", time.localtime(path.stat().st_mtime)
    )
    archived = path.with_name(f"{path.name}_{stamp}")
    suffix = 1
    while archived.exists():
        archived = path.with_name(f"{path.name}_{stamp}_{suffix}")
        suffix += 1
    path.rename(archived)
    log_info(f"archived {path} -> {archived}")
    return archived


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_tasks(path: Path) -> pd.DataFrame:
    """Load a task table with an `outfile` column.

    Used for the job-array file (`tasks.tsv`, one row per study) and the
    study-outcome label table (`study_outcomes.tsv`, one row per study x
    outcome), both written by `gwas_cat_prep.py`.

    Parameters
    ----------
    path : `Path`
        The tab-separated task table.

    Returns
    -------
    tasks : `pd.DataFrame`
        All rows, all columns as strings (blank cells as NaN), rows
        without an `outfile` dropped. In `study_outcomes.tsv` several
        rows can share an `outfile` (one per outcome).

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Tasks file not found: {path}")
    tasks = pd.read_csv(path, sep="\t", dtype=str)
    return tasks.dropna(subset=[ColumnNames.OUTFILE])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_gene_regions(path: Path) -> dict[str, GeneRegion]:
    """Load the flanked gene regions written by `gwas_cat_prep.py`.

    Parameters
    ----------
    path : `Path`
        Tab-separated file with `gene`, `chrom`, `start`, `end` columns
        (`FileNames.GENE_REGIONS_FILE`).

    Returns
    -------
    regions : `dict[str, GeneRegion]`
        Gene symbol -> flanked region, in file order.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Gene regions file not found: {path}")
    table = pd.read_csv(path, sep="\t", dtype=str)
    return {
        row[ColumnNames.GENE]: GeneRegion(
            chrom=row[ColumnNames.CHROM],
            start=int(row[ColumnNames.START]),
            end=int(row[ColumnNames.END]),
        )
        for _, row in table.iterrows()
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_gene_table(path: Path) -> pd.DataFrame:
    """Load the gene reference table, adding any missing standard column.

    Parameters
    ----------
    path : `Path`
        Tab-separated file with at least one identifier column from
        `ColumnNames.GENE_ID_COLUMNS` (`gene`, `ensemblid`, `uniprot`).
        Every other standard column (`ColumnNames.GENE_TABLE_COLUMNS`)
        is optional, and any cell may be blank; `resolve_gene_table`
        fills them in.

    Returns
    -------
    genes : `pd.DataFrame`
        The gene table as strings, with blank cells as "" and a literal
        "NA" kept as-is. Standard columns come first, in standard order,
        followed by any extra columns.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    GeneTableError
        If the file has no identifier column, or a row has no usable
        identifier (all blank or "NA").
    """
    if not path.exists():
        raise FileNotFoundError(f"Gene list not found: {path}")
    # keep_default_na=False so a literal "NA" (looked up, not found) is not
    # read back as blank and re-resolved on every run
    df = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False)
    df.columns = [c.strip() for c in df.columns]
    if not any(c in df.columns for c in ColumnNames.GENE_ID_COLUMNS):
        raise GeneTableError(
            f"{path} needs at least one identifier column out of "
            f"{', '.join(ColumnNames.GENE_ID_COLUMNS)}; got "
            f"{', '.join(df.columns)}"
        )
    for col in ColumnNames.GENE_TABLE_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df = df.apply(lambda col: col.str.strip())
    extra = [c for c in df.columns if c not in ColumnNames.GENE_TABLE_COLUMNS]
    df = df[list(ColumnNames.GENE_TABLE_COLUMNS) + extra]
    for idx in df.index:
        if not _given_gene_ids(df.loc[idx]):
            raise GeneTableError(
                f"{path} row {idx + 2} has no identifier: set one of "
                f"{', '.join(ColumnNames.GENE_ID_COLUMNS)}"
            )
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _given_gene_ids(row: pd.Series) -> dict[str, str]:
    """Return a gene-table row's usable identifiers.

    Parameters
    ----------
    row : `pd.Series`
        A row from `load_gene_table`.

    Returns
    -------
    given : `dict` [`str`, `str`]
        Identifier column -> value, for each of
        `ColumnNames.GENE_ID_COLUMNS` that is neither blank nor "NA".
    """
    return {
        col: row[col]
        for col in ColumnNames.GENE_ID_COLUMNS
        if row[col] not in ("", Constants.NA_STRING)
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def resolve_gene_table(df: pd.DataFrame) -> pd.DataFrame:
    """Fill in every blank gene-table cell via Ensembl and UniProt, in place.

    Each row is resolved from one anchor identifier, picked in this order:
    `ensemblid`, `gene`, `uniprot` (via its primary gene name). The anchor
    gives the Ensembl record, which fills blank `gene`, `ensemblid`,
    `chr`, `start` and `end`. A blank `uniprot` is filled with the gene's
    single reviewed human UniProt accession.

    Only blank ("") cells are filled; given values are never overwritten.
    "NA" means "looked up before, not found" and is left alone, so rows
    with no blank cell cost no API calls and `gene_list.txt` doubles as a
    persisted cache across reruns (clear a cell by hand to retry it).

    Parameters
    ----------
    df : `pd.DataFrame`
        Gene table (as returned by `load_gene_table`).

    Returns
    -------
    df : `pd.DataFrame`
        The same table, with blank cells filled in.

    Raises
    ------
    GeneTableError
        If a row's anchor identifier is not found (so it would have no
        coordinates), or if a row being resolved has identifiers that
        disagree: a given `gene` that differs from the Ensembl symbol,
        or a given `uniprot` that differs from the gene's reviewed
        accession.
    """
    for idx in df.index:
        row = df.loc[idx]
        if not (row[list(ColumnNames.GENE_TABLE_COLUMNS)] == "").any():
            continue
        given = _given_gene_ids(row)
        label = f"gene table row {idx + 2} {given}"
        record = _anchor_gene_record(given)
        if record is None:
            raise GeneTableError(f"{label}: not found in Ensembl/UniProt")
        gene = given.get(ColumnNames.GENE)
        if gene is not None and gene.upper() != record.symbol.upper():
            raise GeneTableError(
                f"{label}: gene {gene!r} does not match Ensembl symbol "
                f"{record.symbol!r} ({record.ensembl_id})"
            )
        resolved = {
            ColumnNames.GENE: record.symbol,
            ColumnNames.ENSEMBL_ID: record.ensembl_id,
            ColumnNames.GENE_CHR: record.region.chrom,
            ColumnNames.START: str(record.region.start),
            ColumnNames.END: str(record.region.end),
        }
        for col, value in resolved.items():
            if row[col] == "":
                df.at[idx, col] = value
        _resolve_uniprot_cell(df, idx, given, record, label)
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _anchor_gene_record(given: dict[str, str]) -> GeneRecord | None:
    """Look up a gene's Ensembl record from its best given identifier.

    Parameters
    ----------
    given : `dict` [`str`, `str`]
        A row's usable identifiers (see `_given_gene_ids`).

    Returns
    -------
    record : `GeneRecord` or `None`
        The Ensembl record, from `ensemblid` if given, else `gene`, else
        `uniprot`. `None` if that identifier is not found.
    """
    if ColumnNames.ENSEMBL_ID in given:
        return ensembl_by_id(given[ColumnNames.ENSEMBL_ID])
    if ColumnNames.GENE in given:
        return ensembl_by_symbol(given[ColumnNames.GENE])
    symbol = symbol_by_uniprot(given[ColumnNames.UNIPROT])
    if symbol is None:
        return None
    return ensembl_by_symbol(symbol)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _resolve_uniprot_cell(
    df: pd.DataFrame,
    idx: int,
    given: dict[str, str],
    record: GeneRecord,
    label: str,
) -> None:
    """Fill a blank `uniprot` cell, or check a given one, in place.

    Parameters
    ----------
    df : `pd.DataFrame`
        Gene table being resolved.
    idx : `int`
        Row index in `df`.
    given : `dict` [`str`, `str`]
        The row's usable identifiers (see `_given_gene_ids`).
    record : `GeneRecord`
        The row's resolved Ensembl record.
    label : `str`
        Row description for log/error messages.

    Raises
    ------
    GeneTableError
        If a given `uniprot` (not used as the anchor) differs from the
        gene's single reviewed accession.
    """
    cell = df.at[idx, ColumnNames.UNIPROT]
    if cell == Constants.NA_STRING:
        return
    uniprot_is_anchor = set(given) == {ColumnNames.UNIPROT}
    if cell != "" and uniprot_is_anchor:
        return
    accession = uniprot_by_symbol(record.symbol)
    if cell == "":
        if accession is None:
            log_warn(f"{label}: no single reviewed UniProt entry, set NA")
            accession = Constants.NA_STRING
        df.at[idx, ColumnNames.UNIPROT] = accession
    elif accession is None:
        log_warn(f"{label}: cannot check uniprot {cell!r}, no single entry")
    elif accession != cell:
        raise GeneTableError(
            f"{label}: uniprot {cell!r} does not match the reviewed "
            f"accession {accession!r} for {record.symbol}"
        )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_row_region(row: pd.Series, flank_bp: int) -> GeneRegion:
    """Build a flanked `GeneRegion` from a gene-table row.

    Parameters
    ----------
    row : `pd.Series`
        A row from a resolved gene table (`chr`/`start`/`end` populated).
    flank_bp : `int`
        Number of base pairs to add either side of the gene body.

    Returns
    -------
    region : `GeneRegion`
        The flanked region.
    """
    return GeneRegion(
        chrom=str(row[ColumnNames.GENE_CHR]),
        start=max(1, int(row[ColumnNames.START]) - flank_bp),
        end=int(row[ColumnNames.END]) + flank_bp,
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_icd_table(path: Path) -> pd.DataFrame:
    """Load the outcome/ICD-code reference table.

    Parameters
    ----------
    path : `Path`
        CSV file with `outcome`, `code`, `code_type`, `description`
        columns. Adds empty `efo_id`/`finngen_phenocode` columns if the
        file doesn't have them yet (one-time migration).

    Returns
    -------
    icd_codes : `pd.DataFrame`
        The ICD-code table, with `efo_id` and `finngen_phenocode`
        guaranteed present. A literal "NA" `efo_id` (looked up before,
        not found) is kept as-is; clear the cell by hand to retry.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"ICD code list not found: {path}")
    # keep_default_na=False so a literal "NA" (looked up, not found) is not
    # read back as blank and re-resolved on every run
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    if ColumnNames.EFO_ID not in df.columns:
        df[ColumnNames.EFO_ID] = ""
    if ColumnNames.FINNGEN_PHENOCODE not in df.columns:
        df[ColumnNames.FINNGEN_PHENOCODE] = ""
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def normalize_icd10_code(code: str) -> str:
    """Normalize an ICD-10 code to its 3-character category form.

    Strips any decimal subdivision and non-standard suffix, e.g.
    "F02.0A" -> "F02", "G31.09" -> "G31". Codes with no "." are
    returned unchanged apart from trimming/upper-casing, e.g. "I20"
    stays "I20".

    Parameters
    ----------
    code : `str`
        Raw ICD-10 code, e.g. "F02.0A", "I20".

    Returns
    -------
    normalized : `str`
        Category-level code, upper-cased.
    """
    return code.strip().upper().split(".", 1)[0]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_efo_ukb_mapping(path: Path) -> dict[str, str]:
    """Parse the vendored EFO-UKB master file into an ICD10->EFO dict.

    Keeps only rows whose code column is ICD10-shaped (matches
    `Constants.ICD10_CODE_PATTERN`), discarding UK Biobank
    self-reported field codes (numeric, or `number_number`). Within
    `MAPPED_TERM_URI`, which may list several comma-separated ontology
    term IDs (not always EFO), the first EFO-shaped candidate
    (`Constants.EFO_ID_PATTERN`) is used; rows with no EFO-shaped
    candidate are skipped. Later rows win on a duplicate normalized
    code.

    Parameters
    ----------
    path : `Path`
        Path to the vendored master TSV
        (`FileNames.EFO_UKB_MAPPING`).

    Returns
    -------
    mapping : `dict[str, str]`
        `{normalized_icd10_code: efo_id}`, e.g. `{"K55": "EFO_0009431"}`.
    """
    code_col = "ICD10_CODE/SELF_REPORTED_TRAIT_FIELD_CODE"
    uri_col = "MAPPED_TERM_URI"
    df = pd.read_csv(path, sep="\t", dtype=str).fillna("")

    mapping: dict[str, str] = {}
    for _, row in df.iterrows():
        code = row[code_col].strip()
        if not re.fullmatch(Constants.ICD10_CODE_PATTERN, code):
            continue

        efo_id = None
        for candidate in row[uri_col].split(","):
            candidate = candidate.strip().upper()
            if re.fullmatch(Constants.EFO_ID_PATTERN, candidate):
                efo_id = candidate.replace(":", "_")
                break
        if efo_id is None:
            continue

        mapping[normalize_icd10_code(code)] = efo_id
    return mapping


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def resolve_efo_ids(
    df: pd.DataFrame, mapping_path: Path = FileNames.EFO_UKB_MAPPING
) -> pd.DataFrame:
    """Fill in blank `efo_id` cells, in place.

    Precedence per blank-`efo_id` row: (1) the vendored EFO-UKB
    master-file lookup, keyed on the row's normalized ICD-10 category
    code; (2) for rows still unresolved, the EBI OLS free-text search,
    keyed on `description` when non-blank else raw `code`, with
    identical search terms deduped so a repeated one is only queried
    once. Rows that already have an `efo_id` (including "NA", i.e. looked
    up before and not found) are left untouched, so `icd_codes.txt`
    doubles as a persisted cache across reruns.

    Parameters
    ----------
    df : `pd.DataFrame`
        ICD-code table (as returned by `load_icd_table`).
    mapping_path : `Path`, optional, default: `FileNames.EFO_UKB_MAPPING`
        Path to the vendored EFO-UKB master mapping file.

    Returns
    -------
    df : `pd.DataFrame`
        The same table, with blank `efo_id` cells filled in.
    """
    mask = df[ColumnNames.EFO_ID].str.strip() == ""
    if not mask.any():
        return df

    master_mapping = load_efo_ukb_mapping(mapping_path)
    normalized_codes = df.loc[mask, ColumnNames.ICD_CODE].map(
        normalize_icd10_code
    )
    df.loc[mask, ColumnNames.EFO_ID] = normalized_codes.map(
        master_mapping
    ).fillna("")

    still_blank = df[ColumnNames.EFO_ID].str.strip() == ""
    if not still_blank.any():
        return df

    search_terms = df.loc[still_blank].apply(
        lambda row: row[ColumnNames.DESCRIPTION].strip()
        or row[ColumnNames.ICD_CODE].strip(),
        axis=1,
    )
    term_to_efo = {term: icd_to_efo(term) for term in search_terms.unique()}
    df.loc[still_blank, ColumnNames.EFO_ID] = search_terms.map(term_to_efo)
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apply_outcome_efo_overrides(
    df: pd.DataFrame,
    overrides: Mapping[str, str] = Constants.OUTCOME_EFO_OVERRIDES,
) -> pd.DataFrame:
    """Replace the `efo_id` of whole outcomes with a code-defined term.

    Applied in memory only, after any write-back of `icd_codes.txt`, so
    the raw file is never changed and a rerun reproduces the same
    mapping from code alone.

    Parameters
    ----------
    df : `pd.DataFrame`
        ICD-code table (as returned by `load_icd_table`).
    overrides : `Mapping[str, str]`, optional, default: `Constants.OUTCOME_EFO_OVERRIDES`
        Outcome -> EFO ID to use for every row of that outcome.

    Returns
    -------
    df : `pd.DataFrame`
        A copy of the table with overridden `efo_id` cells.
    """
    df = df.copy()
    for outcome, efo_id in overrides.items():
        mask = df[ColumnNames.OUTCOME] == outcome
        if not mask.any():
            continue
        previous = sorted(set(df.loc[mask, ColumnNames.EFO_ID]))
        df.loc[mask, ColumnNames.EFO_ID] = efo_id
        log_info(f"{outcome}: efo_id {', '.join(previous)} -> {efo_id}")
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def icd_to_efo(term: str) -> str:
    """Map an ICD code or trait/description string to an EFO ID.

    Parameters
    ----------
    term : `str`
        ICD code or free-text trait/description.

    Returns
    -------
    efo_id : `str`
        The first matching EFO term's short OBO ID (e.g. "EFO_0001645"),
        or "NA" if there is no match or the match has no OBO ID.
    """
    response = requests.get(
        Constants.EBI_OLS_SEARCH_URL,
        params={"q": term, "ontology": "efo"},
        timeout=30,
    )
    response.raise_for_status()
    docs = response.json().get("response", {}).get("docs", [])
    if not docs:
        log_warn(f"No EFO term found for: {term}")
        return Constants.NA_STRING

    obo_id = docs[0].get("obo_id")
    if not obo_id:
        log_warn(f"EFO match for {term!r} has no obo_id: {docs[0]}")
        return Constants.NA_STRING
    log_info(f"mapped {term} -> {obo_id}")
    return obo_id.replace(":", "_")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ols_term(trait_id: str) -> dict | None:
    """Look up one ontology term in EBI OLS by its short ID.

    Parameters
    ----------
    trait_id : `str`
        Underscore-form term ID, e.g. "EFO_0000249" or "MONDO_0004975".

    Returns
    -------
    term : `dict` or `NoneType`
        The OLS term record (with `label`, `is_obsolete`,
        `term_replaced_by`), or `None` if OLS does not know the ID.

    Raises
    ------
    requests.RequestException
        On a network or HTTP error.
    """
    response = requests.get(
        Constants.EBI_OLS_TERMS_URL,
        params={"obo_id": trait_id.replace("_", ":", 1)},
        timeout=30,
    )
    if response.status_code == 404:
        return None
    response.raise_for_status()
    terms = response.json().get("_embedded", {}).get("terms", [])
    return terms[0] if terms else None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _replacement_id(term: dict) -> str | None:
    """Return the short ID an obsolete OLS term was replaced by.

    Parameters
    ----------
    term : `dict`
        An OLS term record from `_ols_term`.

    Returns
    -------
    replacement : `str` or `NoneType`
        Underscore-form ID (e.g. "MONDO_0004975") taken from the last
        path segment of `term_replaced_by`, or `None` if there is none.
    """
    replaced_by = term.get("term_replaced_by")
    if isinstance(replaced_by, list):
        replaced_by = replaced_by[0] if replaced_by else None
    if not replaced_by:
        return None
    return str(replaced_by).rstrip("/").rsplit("/", 1)[-1].replace(":", "_")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def current_trait_id(trait_id: str) -> str:
    """Follow obsolete-term replacements to the current trait ID.

    The GWAS Catalog annotates studies with current terms only, so an
    obsolete ID (e.g. EFO_0000249, replaced by MONDO_0004975) finds
    nothing.

    Parameters
    ----------
    trait_id : `str`
        Underscore-form term ID.

    Returns
    -------
    current : `str`
        The last ID in the `term_replaced_by` chain (at most
        `Constants.MAX_REPLACEMENT_HOPS` hops), or `trait_id` unchanged
        if it is current, unknown to OLS, obsolete without replacement,
        or OLS cannot be reached (each non-current case is warned).
    """
    current = trait_id
    for _ in range(Constants.MAX_REPLACEMENT_HOPS):
        try:
            term = _ols_term(current)
        except requests.RequestException as err:
            log_warn(f"OLS lookup failed for {current}, kept as is: {err}")
            return current
        if term is None:
            log_warn(f"{current} not found in OLS, kept as is")
            return current
        if not term.get("is_obsolete"):
            return current
        replacement = _replacement_id(term)
        if replacement is None:
            log_warn(
                f"{current} ({term.get('label')}) is obsolete without a "
                "replacement, kept as is"
            )
            return current
        current = replacement
    log_warn(
        f"{trait_id}: replacement chain longer than "
        f"{Constants.MAX_REPLACEMENT_HOPS} hops, using {current}"
    )
    return current


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def replace_obsolete_trait_ids(df: pd.DataFrame) -> pd.DataFrame:
    """Replace obsolete trait IDs in the ICD table, in place.

    Every run checks each distinct `efo_id` against OLS (one lookup per
    ID), since cached IDs in `icd_codes.txt` can become obsolete later.
    Blank and "NA" cells are left alone.

    Parameters
    ----------
    df : `pd.DataFrame`
        ICD-code table (as returned by `load_icd_table`), `efo_id`
        already resolved by `resolve_efo_ids`.

    Returns
    -------
    df : `pd.DataFrame`
        The same table, obsolete IDs replaced by their current ID.
    """
    trait_ids = [
        trait_id
        for trait_id in df[ColumnNames.EFO_ID].unique()
        if trait_id.strip() not in ("", Constants.NA_STRING)
    ]
    replacements: dict[str, str] = {}
    for trait_id in trait_ids:
        current = current_trait_id(trait_id)
        if current != trait_id:
            log_warn(f"obsolete trait id {trait_id} -> {current}")
            replacements[trait_id] = current
    if replacements:
        df[ColumnNames.EFO_ID] = df[ColumnNames.EFO_ID].replace(replacements)
    log_info(
        f"trait ids checked: {len(trait_ids)}, obsolete replaced: "
        f"{len(replacements)}"
    )
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _is_not_found(err: ReaderError) -> bool:
    """Tell whether a biomed-api `ReaderError` is an HTTP "not found".

    Parameters
    ----------
    err : `ReaderError`
        Error raised by a biomed-api reader.

    Returns
    -------
    not_found : `bool`
        `True` if it wraps an HTTP 400/404 response (Ensembl answers an
        unknown symbol or ID with 400), `False` for any other failure
        (network, server error, bad JSON).
    """
    cause = err.__cause__
    response = getattr(cause, "response", None)
    return response is not None and response.status_code in (400, 404)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ensembl_gene_record(profile: str, **params: str) -> GeneRecord | None:
    """Run one Ensembl lookup profile and pack it as a `GeneRecord`.

    Parameters
    ----------
    profile : `str`
        `EnsemblReader` profile: "gene_lookup" or "lookup_id".
    **params : `str`
        The profile's endpoint parameter (`symbol=` or `id=`).

    Returns
    -------
    record : `GeneRecord` or `None`
        The gene's record, or `None` if Ensembl does not know it.

    Raises
    ------
    ReaderError
        If the lookup fails for any reason other than "not found".
    """
    try:
        result = EnsemblReader().read(profile=profile, **params)
    except ReaderError as err:
        if _is_not_found(err):
            log_warn(f"Ensembl {profile} found nothing for {params}")
            return None
        raise
    data = result.records[0]
    record = GeneRecord(
        symbol=str(data["display_name"]),
        ensembl_id=str(data["id"]),
        region=GeneRegion(
            chrom=str(data["seq_region_name"]),
            start=int(data["start"]),
            end=int(data["end"]),
        ),
    )
    region = record.region
    log_info(
        f"{params} -> {record.symbol} {record.ensembl_id} "
        f"{region.chrom}:{region.start}-{region.end}"
    )
    return record


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ensembl_by_symbol(symbol: str) -> GeneRecord | None:
    """Look up a gene's Ensembl ID and coordinates from its symbol.

    Parameters
    ----------
    symbol : `str`
        HGNC gene symbol.

    Returns
    -------
    record : `GeneRecord` or `None`
        The gene's (unflanked) record; use `gene_row_region` for
        flanking. `None` if Ensembl has no record for `symbol`.

    Raises
    ------
    ReaderError
        If the lookup fails for any reason other than "not found".
    """
    return _ensembl_gene_record("gene_lookup", symbol=symbol)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ensembl_by_id(ensembl_id: str) -> GeneRecord | None:
    """Look up a gene's symbol and coordinates from its Ensembl ID.

    Parameters
    ----------
    ensembl_id : `str`
        Ensembl stable gene ID (ENSG...).

    Returns
    -------
    record : `GeneRecord` or `None`
        The gene's (unflanked) record. `None` if Ensembl has no record
        for `ensembl_id`.

    Raises
    ------
    ReaderError
        If the lookup fails for any reason other than "not found".
    """
    return _ensembl_gene_record("lookup_id", id=ensembl_id)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _uniprot_search(query: str) -> list[dict]:
    """Run a UniProtKB search through biomed-api.

    Parameters
    ----------
    query : `str`
        UniProtKB query string.

    Returns
    -------
    entries : `list` [`dict`]
        Matching UniProtKB entries (raw JSON), possibly empty. Also empty
        when UniProt rejects the query (HTTP 400, e.g. a malformed
        accession).

    Raises
    ------
    ReaderError
        If the search request fails for any other reason.
    """
    reader = UniProtIdMappingReader()
    try:
        return reader.read(profile="entry_lookup", query=query).records
    except ReaderError as err:
        # entry_lookup raises its own ReaderError (no HTTP cause attached),
        # so the status code can only be read from the message
        if "HTTP 400" in str(err):
            log_warn(f"UniProt rejected query {query!r}: {err}")
            return []
        raise


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def uniprot_by_symbol(symbol: str) -> str | None:
    """Look up a gene's reviewed (Swiss-Prot) human UniProt accession.

    Parameters
    ----------
    symbol : `str`
        HGNC gene symbol.

    Returns
    -------
    accession : `str` or `None`
        The single reviewed human accession for `symbol`, or `None` if
        there are zero or several.

    Raises
    ------
    ReaderError
        If the search request fails.
    """
    query = (
        f"gene_exact:{symbol} AND "
        f"organism_id:{Constants.UNIPROT_HUMAN_TAXON} AND reviewed:true"
    )
    accessions = [e["primaryAccession"] for e in _uniprot_search(query)]
    if len(accessions) != 1:
        log_warn(f"{symbol}: {len(accessions)} reviewed UniProt entries")
        return None
    log_info(f"{symbol} -> UniProt {accessions[0]}")
    return accessions[0]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def symbol_by_uniprot(accession: str) -> str | None:
    """Look up the primary gene symbol of a UniProt accession.

    Parameters
    ----------
    accession : `str`
        UniProt accession (e.g. "P02649").

    Returns
    -------
    symbol : `str` or `None`
        The entry's primary gene name, or `None` if the accession is not
        found or has no gene name.

    Raises
    ------
    ReaderError
        If the search request fails.
    """
    entries = _uniprot_search(f"accession:{accession}")
    if len(entries) != 1:
        log_warn(f"UniProt {accession}: {len(entries)} entries found")
        return None
    genes = entries[0].get("genes") or [{}]
    symbol = genes[0].get("geneName", {}).get("value")
    if symbol is None:
        log_warn(f"UniProt {accession}: entry has no primary gene name")
        return None
    log_info(f"UniProt {accession} -> {symbol}")
    return symbol


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _fetch_gwas_catalog_study_records(
    efo_id: str, include_child_traits: bool = False
) -> list[dict]:
    """Fetch raw GWAS Catalog study records for an EFO trait.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form, e.g. "EFO_0001645").
    include_child_traits : `bool`, optional, default: `False`
        Also return studies annotated with a child term of `efo_id`.

    Returns
    -------
    records : `list[dict]`
        One dict per study with `accession_id`,
        `full_summary_stats_available`, `pubmed_id`, `disease_trait`,
        `initial_sample_size`, `discovery_ancestry`, `cohort`,
        `efo_traits` (the terms the study is annotated with), and the
        `gxe`/`gxg` interaction-study flags, as returned by the GWAS
        Catalog studies-list search (absent fields are `None`, absent
        flags `False`).
    """
    reader = GwasCatalogReader()
    query = {"show_child_trait": True} if include_child_traits else {}
    with warnings.catch_warnings():
        # biomed-api warns (rather than raising) on zero matches; an
        # empty accession list is a normal outcome for callers here.
        warnings.simplefilter("ignore", UserWarning)
        result = reader.read(profile="studies", efo_id=efo_id, **query)

    return [
        {
            "accession_id": row["accession_id"],
            "full_summary_stats_available": row.get(
                "full_summary_stats_available", False
            ),
            "pubmed_id": row.get("pubmed_id"),
            "disease_trait": row.get("disease_trait"),
            "initial_sample_size": row.get("initial_sample_size"),
            "discovery_ancestry": row.get("discovery_ancestry"),
            "cohort": row.get("cohort"),
            "efo_traits": row.get("efo_traits"),
            "gxe": row.get("gxe", False),
            "gxg": row.get("gxg", False),
        }
        for row in result.records
        if "accession_id" in row
    ]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def includes_child_traits(outcome: str) -> bool:
    """Tell whether an outcome's trait searches include child traits.

    Parameters
    ----------
    outcome : `str`
        Outcome name from `icd_codes.txt`.

    Returns
    -------
    broad : `bool`
        `True` if `outcome` is in `Constants.CHILD_TRAIT_OUTCOMES`.
    """
    return outcome in Constants.CHILD_TRAIT_OUTCOMES


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mapped_traits(efo_traits: object) -> tuple[str, str]:
    """Render a GWAS Catalog `efo_traits` field as ID and label cells.

    Parameters
    ----------
    efo_traits : `object`
        A list of `{"efo_id", "efo_trait"}` dicts, its string repr (as
        read back from a TSV), or `None`/NA.

    Returns
    -------
    ids_labels : `tuple[str, str]`
        `(mapped_trait_id, mapped_trait)`, each joined with `"; "` in
        record order; `("", "")` if there are no terms.
    """
    if isinstance(efo_traits, str) and efo_traits.startswith("["):
        try:
            efo_traits = ast.literal_eval(efo_traits)
        except (ValueError, SyntaxError):
            return "", ""
    if not isinstance(efo_traits, (list, tuple)):
        return "", ""
    terms = [t for t in efo_traits if isinstance(t, dict)]
    ids = "; ".join(clean_cell(t.get("efo_id")) for t in terms)
    labels = "; ".join(clean_cell(t.get("efo_trait")) for t in terms)
    return ids, labels


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def discover_studies(
    efo_id: str,
    cap: int = Constants.MAX_STUDIES_PER_OUTCOME,
    include_child_traits: bool = False,
) -> list[str]:
    """Discover GWAS Catalog study accessions for an EFO trait.

    Well-studied traits (e.g. common diseases, lipid biomarkers) can have
    hundreds of associated studies; only those with full summary
    statistics available are usable downstream, and pulling all of them
    is expensive (a sumstats download and filter per gene). Results are
    therefore filtered to non-interaction, non-CNV studies with full
    summary statistics available and capped to the `cap` most recently
    published, via
    `filter_and_cap_studies`.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form, e.g. "EFO_0001645").
    cap : `int`, optional, default: `Constants.MAX_STUDIES_PER_OUTCOME`
        Maximum number of studies to keep, most recent first (per mapped
        term when `include_child_traits`).
    include_child_traits : `bool`, optional, default: `False`
        Also discover studies annotated with a child term of `efo_id`.

    Returns
    -------
    accessions : `list[str]`
        Study accession IDs (e.g. "GCST######"), filtered and capped.
    """
    classified = discover_studies_with_reasons(
        efo_id, cap=cap, include_child_traits=include_child_traits
    )
    return [r["accession_id"] for r in classified if r["reason"] == "included"]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def discover_studies_with_reasons(
    efo_id: str,
    cap: int = Constants.MAX_STUDIES_PER_OUTCOME,
    include_child_traits: bool = False,
) -> list[dict]:
    """Discover and classify GWAS Catalog studies for an EFO trait.

    Like `discover_studies`, but returns every discovered study annotated
    with why it was or wasn't kept, for the study-discovery audit log
    written by `gwas_cat_prep.build_tasks`.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form, e.g. "EFO_0001645").
    cap : `int`, optional, default: `Constants.MAX_STUDIES_PER_OUTCOME`
        Maximum number of studies to mark `"included"`, most recent
        first (per mapped term when `include_child_traits`).
    include_child_traits : `bool`, optional, default: `False`
        Also discover studies annotated with a child term of `efo_id`;
        the cap is then applied per term, so child terms cannot push
        out the studies of `efo_id` itself, with an overall ceiling of
        `Constants.MAX_STUDIES_PER_CHILD_QUERY` included studies.

    Returns
    -------
    classified : `list[dict]`
        As returned by `classify_studies` -- `accession_id`, `pubmed_id`,
        `reason`, plus publication/trait/sample metadata.
    """
    records = _fetch_gwas_catalog_study_records(efo_id, include_child_traits)
    # printed only; gwas_cat_prep records one summary line per EFO
    log_debug(f"{efo_id} -> {len(records)} studies")
    return classify_studies(
        records,
        cap=cap,
        per_term=include_child_traits,
        total_cap=(
            Constants.MAX_STUDIES_PER_CHILD_QUERY
            if include_child_traits
            else None
        ),
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def clean_cell(value: object) -> str:
    """Render a value as a single TSV-safe cell.

    Parameters
    ----------
    value : `object`
        Scalar, list, or `None` (e.g. a GWAS Catalog field such as
        `discovery_ancestry`, which is a list of strings).

    Returns
    -------
    cell : `str`
        `""` for `None`/NaN, list items joined with `"; "`, and any
        tabs/newlines replaced by a single space.
    """
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        value = "; ".join(clean_cell(v) for v in value if v is not None)
    elif isinstance(value, float) and pd.isna(value):
        return ""
    return re.sub(r"[\t\r\n]+", " ", str(value)).strip()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pubmed_summaries(pubmed_ids: list) -> dict[int, dict]:
    """Batch-fetch publication metadata from PubMed via NCBI E-utils.

    GWAS Catalog study records carry a `pubmed_id` but no publication
    date of their own; PubMed's `esummary` endpoint is the source of
    truth for when a study was actually published. IDs are deduplicated
    and fetched in chunks of `Constants.PUBMED_BATCH_SIZE` (one request
    per chunk), not one request per ID.

    Parameters
    ----------
    pubmed_ids : `list`
        PubMed IDs to look up, as `int` or numeric `str` (`None`/falsy/
        non-numeric entries are ignored).

    Returns
    -------
    summaries : `dict[int, dict]`
        `{pubmed_id: {"date", "first_author", "journal", "title"}}`,
        where `date` is a `pd.Timestamp` or `None` if `pubdate` could not
        be parsed. IDs PubMed does not return are omitted, so callers
        should use `.get(...)` with a fallback.
    """
    unique_ids = sorted(
        {int(pid) for pid in pubmed_ids if pid and str(pid).isdigit()}
    )
    summaries: dict[int, dict] = {}
    for start in range(0, len(unique_ids), Constants.PUBMED_BATCH_SIZE):
        chunk = unique_ids[start : start + Constants.PUBMED_BATCH_SIZE]
        response = requests.get(
            Constants.NCBI_ESUMMARY_URL,
            params={
                "db": "pubmed",
                "id": ",".join(str(pid) for pid in chunk),
                "retmode": "json",
            },
            timeout=30,
        )
        response.raise_for_status()
        result = response.json().get("result", {})
        for uid in result.get("uids", []):
            entry = result.get(uid, {})
            parsed = pd.to_datetime(entry.get("pubdate", ""), errors="coerce")
            summaries[int(uid)] = {
                "date": parsed if pd.notna(parsed) else None,
                "first_author": clean_cell(entry.get("sortfirstauthor")),
                "journal": clean_cell(entry.get("fulljournalname")),
                "title": clean_cell(entry.get("title")),
            }
    return summaries


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def study_exclusion_reason(record: dict) -> str | None:
    """Tell whether a GWAS Catalog study is a design we never use.

    Gene-environment (GxE) and gene-gene (GxG) interaction studies and
    copy-number-variant (CNV) models report interaction or CNV effects,
    not the SNP main effects filtered downstream, yet would otherwise
    take recency-cap slots (e.g. one GWAS Catalog paper deposits dozens
    of "<trait> x <environment> interaction" studies).
    X-chromosome-only analyses (e.g. X-inactivation models) cannot cover
    the autosomal gene regions filtered downstream.

    Parameters
    ----------
    record : `dict`
        Study record with optional `gxe`, `gxg` and `disease_trait`
        fields (as returned by `_fetch_gwas_catalog_study_records`).

    Returns
    -------
    reason : `str` or `NoneType`
        `"gxe_interaction"`, `"gxg_interaction"`, `"cnv_study"` or
        `"x_chromosome_study"` (checked in that order), or `None` if the
        study is usable.
    """
    if record.get("gxe"):
        return "gxe_interaction"
    if record.get("gxg"):
        return "gxg_interaction"
    trait = record.get("disease_trait")
    if isinstance(trait, str) and _CNV_TRAIT_PATTERN.search(trait):
        return "cnv_study"
    if isinstance(trait, str) and _X_CHROM_TRAIT_PATTERN.search(trait):
        return "x_chromosome_study"
    return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def classify_studies(
    records: list[dict],
    cap: int = Constants.MAX_STUDIES_PER_OUTCOME,
    per_term: bool = False,
    total_cap: int | None = None,
) -> list[dict]:
    """Classify candidate GWAS Catalog studies as included or excluded.

    Studies with a `study_exclusion_reason` (GxE/GxG interaction, CNV,
    X-chromosome-only) are set aside first, so they never take a cap
    slot. The rest go through the same eligibility filter (full summary stats available)
    and recency cap as `filter_and_cap_studies`, but every input record
    is returned
    with the reason it was kept or dropped, rather than only
    the surviving accessions -- the basis for the study-discovery audit
    log (see `gwas_cat_prep.build_tasks`).

    Parameters
    ----------
    records : `list[dict]`
        Candidate study records, each with `accession_id`,
        `full_summary_stats_available`, and `pubmed_id` (as returned by
        the GWAS Catalog studies-list search).
    cap : `int`, optional, default: `Constants.MAX_STUDIES_PER_OUTCOME`
        Maximum number of eligible studies to mark `"included"`, most
        recent first.
    per_term : `bool`, optional, default: `False`
        Apply `cap` per mapped term (each ID in a record's `efo_traits`)
        instead of overall, and include the union. Used with child
        traits, so each term (the queried parent included) keeps its
        own `cap` most recent studies.
    total_cap : `int` or `NoneType`, optional, default: `None`
        With `per_term`, also stop including once this many studies are
        included overall (most recent first); later per-term survivors
        are marked `"over_total_cap"`. `None` means no overall ceiling.

    Returns
    -------
    classified : `list[dict]`
        One dict per input record, each with `accession_id`, `pubmed_id`,
        `reason`, plus display-only metadata (all `str`, `""` if
        unknown): `pub_date` (YYYY-MM-DD), `first_author`, `journal`,
        `title` (from PubMed), and `trait`, `sample_size`, `ancestry`,
        `cohort`, `mapped_trait_id`, `mapped_trait` (from the GWAS
        Catalog record). `reason` is one of
        `"included"`, `"over_cap"` (eligible but
        beyond `cap`), `"over_total_cap"` (within its per-term `cap` but
        beyond `total_cap`), `"no_full_sumstats"`, or a
        `study_exclusion_reason` (`"gxe_interaction"`,
        `"gxg_interaction"`, `"cnv_study"`, `"x_chromosome_study"`).
        `"included"`, `"over_cap"`
        and `"over_total_cap"` records appear first, in that order and
        most-recent-publication-date first within each (unresolved dates
        sort last), followed by `"no_full_sumstats"` records and then
        excluded-design records, both in their original input order.
    """
    excluded = [
        (r, reason)
        for r in records
        if (reason := study_exclusion_reason(r)) is not None
    ]
    usable = [r for r in records if study_exclusion_reason(r) is None]
    eligible = [r for r in usable if r.get("full_summary_stats_available")]
    ineligible = [
        r for r in usable if not r.get("full_summary_stats_available")
    ]
    # Fetched for every record (not just eligible ones) so the audit log
    # shows dates for no_full_sumstats studies too.
    summaries = pubmed_summaries([r.get("pubmed_id") for r in records])

    def _summary(record: dict) -> dict:
        pid = record.get("pubmed_id")
        if pid and str(pid).isdigit():
            return summaries.get(int(pid), {})
        return {}

    def sort_key(record: dict) -> tuple[bool, pd.Timestamp]:
        date = _summary(record).get("date")
        return (date is not None, date or pd.Timestamp.min)

    eligible.sort(key=sort_key, reverse=True)

    over_total_cap: list[dict] = []
    if per_term:
        # eligible is sorted, so each term's first `cap` are its most recent
        included_ids: set[str] = set()
        over_total_ids: set[str] = set()
        per_term_counts: dict[str, int] = {}
        for record in eligible:
            terms = mapped_traits(record.get("efo_traits"))[0].split("; ")
            if any(per_term_counts.get(term, 0) < cap for term in terms):
                if total_cap is not None and len(included_ids) >= total_cap:
                    over_total_ids.add(record["accession_id"])
                else:
                    included_ids.add(record["accession_id"])
            for term in terms:
                per_term_counts[term] = per_term_counts.get(term, 0) + 1
        included = [r for r in eligible if r["accession_id"] in included_ids]
        over_total_cap = [
            r for r in eligible if r["accession_id"] in over_total_ids
        ]
        over_cap = [
            r
            for r in eligible
            if r["accession_id"] not in included_ids
            and r["accession_id"] not in over_total_ids
        ]
    else:
        included, over_cap = eligible[:cap], eligible[cap:]

    def _row(record: dict, reason: str) -> dict:
        summary = _summary(record)
        date = summary.get("date")
        trait_ids, trait_labels = mapped_traits(record.get("efo_traits"))
        return {
            "accession_id": record["accession_id"],
            "pubmed_id": record.get("pubmed_id"),
            "reason": reason,
            "pub_date": date.strftime("%Y-%m-%d") if date is not None else "",
            "first_author": summary.get("first_author", ""),
            "journal": summary.get("journal", ""),
            "title": summary.get("title", ""),
            "trait": clean_cell(record.get("disease_trait")),
            "sample_size": clean_cell(record.get("initial_sample_size")),
            "ancestry": clean_cell(record.get("discovery_ancestry")),
            "cohort": clean_cell(record.get("cohort")),
            "mapped_trait_id": trait_ids,
            "mapped_trait": trait_labels,
        }

    classified = (
        [_row(r, "included") for r in included]
        + [_row(r, "over_cap") for r in over_cap]
        + [_row(r, "over_total_cap") for r in over_total_cap]
        + [_row(r, "no_full_sumstats") for r in ineligible]
        + [_row(r, reason) for r, reason in excluded]
    )
    log_debug(
        f"{len(records)} studies -> {len(usable)} after dropping "
        f"GxE/GxG/CNV -> {len(eligible)} with full sumstats "
        f"-> {len(included)} included after cap={cap}"
        + (" per term" if per_term else "")
        + (f", total_cap={total_cap}" if total_cap is not None else "")
    )
    return classified


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_and_cap_studies(
    records: list[dict], cap: int = Constants.MAX_STUDIES_PER_OUTCOME
) -> list[str]:
    """Keep studies with full summary stats, capped to the N most recent.

    GxE/GxG interaction and CNV studies (`study_exclusion_reason`) are
    dropped before the cap.

    Parameters
    ----------
    records : `list[dict]`
        Candidate study records, each with `accession_id`,
        `full_summary_stats_available`, and `pubmed_id` (as returned by
        the GWAS Catalog studies-list search).
    cap : `int`, optional, default: `Constants.MAX_STUDIES_PER_OUTCOME`
        Maximum number of studies to return, most recent first.

    Returns
    -------
    capped : `list[str]`
        At most `cap` study accessions, all with full summary statistics
        available, ordered most-recent-publication-date first (studies
        whose date could not be resolved from PubMed sort last).
    """
    classified = classify_studies(records, cap=cap)
    return [r["accession_id"] for r in classified if r["reason"] == "included"]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_finngen_manifest(
    path: Path = FileNames.FINNGEN_MANIFEST,
) -> pd.DataFrame:
    """Load the vendored FinnGen R13 summary-stats manifest.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.FINNGEN_MANIFEST`
        TSV file with `phenocode`, `phenotype`, `category`, `num_cases`,
        `num_controls`, `path_bucket`, `path_https` columns, as published
        at the FinnGen R13 manifest URL.

    Returns
    -------
    manifest : `pd.DataFrame`
        The manifest table, all columns as strings.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"FinnGen manifest not found: {path}")
    return pd.read_csv(path, sep="\t", dtype=str).fillna("")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def finngen_studies_for_phenocode(
    phenocode: str, manifest_df: pd.DataFrame
) -> list[str]:
    """Validate a curated FinnGen phenocode against the manifest.

    FinnGen phenocode curation is manual (one phenocode per outcome, set
    by hand in `icd_codes.txt`), unlike GWAS Catalog's `discover_studies`
    which searches an API -- this only confirms the curated value is a
    real, current phenocode. Kept list-returning (rather than
    `str | None`) so callers can treat both sources identically.

    Parameters
    ----------
    phenocode : `str`
        Curated FinnGen phenocode (e.g. "G6_ALZHEIMER").
    manifest_df : `pd.DataFrame`
        Manifest table from `load_finngen_manifest`.

    Returns
    -------
    accessions : `list[str]`
        `[phenocode]` if present in the manifest, else `[]`.
    """
    if phenocode in set(manifest_df["phenocode"]):
        return [phenocode]
    log_warn(f"{phenocode} not found in FinnGen manifest")
    return []


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_manual_gwas_catalog_studies(
    path: Path = FileNames.GWAS_CATALOG_MANUAL_STUDIES,
) -> pd.DataFrame:
    """Load the curated entry-point table of manually-added GWAS studies.

    A GWAS Catalog study can have summary statistics deposited on the
    FTP server before the REST API has indexed it, which makes it
    unreachable via `discover_studies` (EFO search) no matter its
    outcome mapping. This table is a hand-curated list of such studies,
    added by outcome from a paper's own Data Availability section -- see
    `data/raw/gwas_catalog_manual_studies.SOURCE.md`.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.GWAS_CATALOG_MANUAL_STUDIES`
        TSV file with required `accession_id`, `outcome` columns and
        optional (may be absent or empty) `pubmed_id`, `disease_trait`,
        `pub_date`, `first_author`, `journal`, `title`, `sample_size`,
        `ancestry`, `cohort`, `note` columns. The metadata columns only
        feed the study-discovery audit log; non-empty values override
        what PubMed returns for `pubmed_id`.

    Returns
    -------
    manual_studies : `pd.DataFrame`
        The table, all columns as strings. Empty (but correctly
        columned) if `path` does not exist yet -- unlike the vendored
        FinnGen manifest, this file is expected to grow over time rather
        than always being present.
    """
    columns = [
        "accession_id",
        "outcome",
        ColumnNames.PUBMED_ID,
        ColumnNames.DISEASE_TRAIT,
        ColumnNames.PUB_DATE,
        ColumnNames.FIRST_AUTHOR,
        ColumnNames.JOURNAL,
        ColumnNames.TITLE,
        ColumnNames.SAMPLE_SIZE,
        ColumnNames.ANCESTRY,
        ColumnNames.COHORT,
        ColumnNames.NOTE,
    ]
    if not path.exists():
        return pd.DataFrame(columns=columns)
    manual_df = pd.read_csv(path, sep="\t", dtype=str).fillna("")
    # Metadata columns are optional (empty allowed); add any missing ones
    # so older files without them still load.
    for column in columns:
        if column not in manual_df.columns:
            manual_df[column] = ""
    return manual_df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def manual_studies_for_outcome(
    outcome: str, manual_df: pd.DataFrame
) -> list[str]:
    """Look up curated GWAS Catalog accessions for an outcome.

    Parameters
    ----------
    outcome : `str`
        Outcome name, as used in `icd_codes.txt`'s `outcome` column.
    manual_df : `pd.DataFrame`
        Table from `load_manual_gwas_catalog_studies`.

    Returns
    -------
    accessions : `list[str]`
        `accession_id` values curated for `outcome`. `[]` if none.
    """
    is_outcome = manual_df["outcome"] == outcome
    return manual_df.loc[is_outcome, "accession_id"].tolist()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def finngen_sumstats_url(
    phenocode: str, manifest_df: pd.DataFrame
) -> str | None:
    """Look up a FinnGen phenocode's summary-stats file URL.

    Parameters
    ----------
    phenocode : `str`
        FinnGen phenocode (e.g. "G6_ALZHEIMER").
    manifest_df : `pd.DataFrame`
        Manifest table from `load_finngen_manifest`.

    Returns
    -------
    url : `str` or `NoneType`
        The `path_https` URL of the bgzip+tabix-indexed sumstats file
        (with a `.tbi` index at `url + ".tbi"`), or `None` if the
        phenocode is not in the manifest.
    """
    matches = manifest_df.loc[
        manifest_df["phenocode"] == phenocode, "path_https"
    ]
    if matches.empty:
        return None
    return matches.iloc[0]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def finngen_phenocodes_in_cell(cell: str) -> list[str]:
    """Split a possibly comma-separated `finngen_phenocode` cell.

    A single outcome can be curated against more than one FinnGen
    endpoint (e.g. several definitional variants of the same disease,
    each with different case criteria/exclusions); `icd_codes.txt`
    stores these as a comma-separated list in one cell.

    Parameters
    ----------
    cell : `str`
        Raw cell value, e.g. "F5_DEMENTIA,F5_DEMENTIA_INCLAVO" or "".

    Returns
    -------
    phenocodes : `list[str]`
        Individual phenocodes, whitespace-trimmed, blanks dropped.
    """
    return [p.strip() for p in cell.split(",") if p.strip()]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _accession_bucket_location(study_accession: str) -> str | None:
    """Derive and verify a study's FTP directory from its accession alone.

    GWAS Catalog buckets its FTP summary-stats directories in
    consecutive, non-overlapping ranges of 1000 accessions (e.g.
    "GCST90004001-GCST90005000"). A study can be deposited there before
    the REST API has indexed it (`study_summary_stats_location`'s `GET
    /studies/{accession}` 404s in that window), so this derives the same
    bucket the API would eventually report and confirms it by actually
    requesting it -- a malformed or nonexistent accession still safely
    returns `None` rather than a guessed-wrong URL.

    Parameters
    ----------
    study_accession : `str`
        GWAS Catalog study accession (e.g. "GCST90861026").

    Returns
    -------
    location : `str` or `NoneType`
        URL of the study's bucketed FTP directory if it responds `200`,
        else `None` (including when `study_accession` isn't in the
        expected "GCST" + digits shape).
    """
    match = re.fullmatch(r"GCST(\d+)", study_accession)
    if not match:
        return None

    digits = match.group(1)
    width = len(digits)
    accession_num = int(digits)
    bucket_start = ((accession_num - 1) // 1000) * 1000 + 1
    bucket_end = bucket_start + 999
    bucket_name = (
        f"GCST{bucket_start:0{width}d}-GCST{bucket_end:0{width}d}"
    )
    location = (
        f"{Constants.GWAS_CATALOG_FTP_BASE}/{bucket_name}/{study_accession}"
    )

    response = requests.head(f"{location}/", timeout=30)
    if response.status_code != 200:
        log_warn(f"{study_accession}: derived FTP bucket {location} not found")
        return None
    return location


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _get_with_retry(url: str, timeout: int) -> requests.Response:
    """GET a URL, retrying on server errors, timeouts and dropped connections.

    Parameters
    ----------
    url : `str`
        URL to fetch.
    timeout : `int`
        Per-attempt request timeout in seconds.

    Returns
    -------
    response : `requests.Response`
        The first response with a status below 500, or the last response
        if every attempt returned a 5xx status. Other statuses (e.g. 404)
        are returned unchanged for the caller to handle.

    Raises
    ------
    requests.Timeout, requests.ConnectionError
        If the last attempt times out or cannot connect.

    Notes
    -----
    Makes `len(Constants.HTTP_RETRY_BACKOFF) + 1` attempts, sleeping the
    listed number of seconds before each retry.
    """
    n_retries = len(Constants.HTTP_RETRY_BACKOFF)
    for attempt, wait in enumerate((*Constants.HTTP_RETRY_BACKOFF, None), 1):
        try:
            response = requests.get(url, timeout=timeout)
        except (requests.Timeout, requests.ConnectionError) as exc:
            if wait is None:
                raise
            reason = type(exc).__name__
        else:
            if response.status_code < 500 or wait is None:
                return response
            reason = f"HTTP {response.status_code}"
        log_warn(f"{url}: {reason}, retry {attempt}/{n_retries} in {wait}s")
        time.sleep(wait)
    raise AssertionError("unreachable")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def study_summary_stats_location(study_accession: str) -> str | None:
    """Look up a study's harmonised summary-stats FTP directory.

    Parameters
    ----------
    study_accession : `str`
        GWAS Catalog study accession (e.g. "GCST######").

    Returns
    -------
    location : `str` or `NoneType`
        URL of the study's summary-stats directory (accession-bucketed,
        e.g. ".../GCST90004001-GCST90005000/GCST90004758"), or `None` if
        the study has no full summary statistics available. If the study
        isn't found via the API (`404` -- can happen for a study whose
        sumstats are already deposited on the FTP server but not yet
        indexed by the API), falls back to `_accession_bucket_location`.

    Raises
    ------
    requests.HTTPError
        If the API call fails for a reason other than "not found".
    """
    response = _get_with_retry(
        f"{Constants.GWAS_CATALOG_API_V2}/studies/{study_accession}",
        timeout=30,
    )
    if response.status_code == 404:
        return _accession_bucket_location(study_accession)
    response.raise_for_status()
    data = response.json()
    if not data.get("full_summary_stats_available"):
        return None
    return data["full_summary_stats"]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _list_ftp_dir(url: str) -> list[str]:
    """List the entries (href targets) of an FTP-over-HTTP directory page.

    Parameters
    ----------
    url : `str`
        Directory URL (without trailing slash).

    Returns
    -------
    entries : `list` [`str`]
        The `href` values on the directory's index page.
    """
    response = requests.get(f"{url}/", timeout=30)
    response.raise_for_status()
    return re.findall(r'href="([^"]+)"', response.text)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def resolve_sumstats_source(
    location: str, study_accession: str
) -> SumstatsSource:
    """Determine the queryable summary-stats file for a study.

    GWAS Catalog studies with full summary statistics available come in
    three layouts:

    - current harmonised: `harmonised/{accession}.h.tsv.gz` (+ `.tbi`),
      standard column names.
    - legacy harmonised: `harmonised/{pmid}-{accession}-{efo}.h.tsv.gz`,
      usually without a `.tbi`; the harmonised GRCh38 values are in the
      `hm_*` columns (the plain columns hold the author's original
      coordinates, which may be another build).
    - raw only: a single author-submitted file at the top level of the
      study's FTP directory, standard column names, not indexed.

    Parameters
    ----------
    location : `str`
        The study's summary-stats FTP directory (from
        `study_summary_stats_location`).
    study_accession : `str`
        GWAS Catalog study accession (e.g. "GCST######").

    Returns
    -------
    source : `SumstatsSource`
        URL, whether it is tabix-indexed, and the column names to use.

    Raises
    ------
    ValueError
        If there is no single harmonised file and the directory listing
        does not contain exactly one identifiable raw data file.
    """
    entries = _list_ftp_dir(location)

    if "harmonised/" in entries:
        hm_dir = f"{location}/harmonised"
        hm_entries = _list_ftp_dir(hm_dir)
        hm_files = [e for e in hm_entries if e.endswith(".h.tsv.gz")]
        if len(hm_files) == 1:
            name = hm_files[0]
            is_indexed = f"{name}.tbi" in hm_entries
            if name == f"{study_accession}.h.tsv.gz":
                return SumstatsSource(f"{hm_dir}/{name}", is_indexed)
            return SumstatsSource(
                url=f"{hm_dir}/{name}",
                is_tabix_indexed=is_indexed,
                chrom_col="hm_chrom",
                pos_col="hm_pos",
                maf_col="hm_effect_allele_frequency",
            )
        log_warn(
            f"{study_accession}: expected one *.h.tsv.gz in {hm_dir}, "
            f"found {hm_files}; falling back to raw file"
        )

    # lower-case match: some directories hold only a `readme.txt`
    exclude = {"readme.txt", "md5sum.txt"}
    candidates = [
        entry
        for entry in entries
        if not entry.endswith("/")
        and not entry.startswith("?")
        and entry.lower() not in exclude
        and not entry.endswith("-meta.yaml")
    ]
    if len(candidates) != 1:
        raise ValueError(
            f"{study_accession}: could not identify a single raw sumstats "
            f"file in {location} (candidates: {candidates})"
        )
    return SumstatsSource(f"{location}/{candidates[0]}", False)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fetch_curated_associations(
    efo_id: str, include_child_traits: bool = False
) -> list[dict]:
    """Fetch all curated genome-wide-significant associations for a trait.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form).
    include_child_traits : `bool`, optional, default: `False`
        Also fetch associations annotated with a child term of `efo_id`;
        each record's `efo_traits` names the term it is annotated with.

    Returns
    -------
    records : `list[dict]`
        Every association record for `efo_id`, unfiltered. The download
        does not depend on any gene, so fetch once per EFO ID and filter
        per gene with `filter_curated_associations`.

    Notes
    -----
    Sourced via biomed-api's `GwasCatalogReader` (GWAS Catalog REST v2).
    Pages are requested at `Constants.GWAS_CATALOG_PAGE_SIZE` records, so
    large traits (e.g. HDL-C, 25k records) stay under biomed-api's
    500-page cap.
    """
    reader = GwasCatalogReader()
    query: dict[str, object] = {"size": Constants.GWAS_CATALOG_PAGE_SIZE}
    if include_child_traits:
        query["show_child_trait"] = True
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        result = reader.read(profile="associations", efo_id=efo_id, **query)

    records = list(result.records)
    # printed only; merge_associations records one summary line per EFO
    log_debug(f"{efo_id} -> {len(records)} curated associations fetched")
    return records


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_curated_associations(
    records: list[dict], region: GeneRegion, maf_threshold: float
) -> pd.DataFrame:
    """Restrict curated association records to a region and MAF threshold.

    Parameters
    ----------
    records : `list[dict]`
        Association records from `fetch_curated_associations`.
    region : `GeneRegion`
        Gene region to restrict associations to.
    maf_threshold : `float`
        Only associations with a reported MAF below this are kept.

    Returns
    -------
    associations : `pd.DataFrame`
        Curated associations, region- and MAF-filtered, with an added
        `region_location` column: the record's first `"chrom:pos"`
        location inside `region` (used by `harmonise_curated`). Empty if
        none.
    """
    kept = []
    for row in records:
        location = _region_location(row.get("locations"), region)
        if location is None:
            continue
        if _maf_at_or_above_threshold(row.get("risk_frequency"), maf_threshold):
            continue
        kept.append({**row, "region_location": location})
    return pd.DataFrame.from_records(kept)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _location_in_region(
    locations: list[str] | None, region: GeneRegion
) -> bool:
    """Check whether any GWAS Catalog v2 `"chrom:pos"` location is in `region`.

    Parameters
    ----------
    locations : `list[str]` or `NoneType`
        Values of an association record's `locations` field.
    region : `GeneRegion`
        Region to test against.

    Returns
    -------
    `bool`
        `True` if at least one location falls within `region`.
    """
    return _region_location(locations, region) is not None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _region_location(
    locations: list[str] | None, region: GeneRegion
) -> str | None:
    """Return the first GWAS Catalog v2 `"chrom:pos"` location in `region`.

    Parameters
    ----------
    locations : `list[str]` or `NoneType`
        Values of an association record's `locations` field.
    region : `GeneRegion`
        Region to test against.

    Returns
    -------
    location : `str` or `NoneType`
        The first location falling within `region`, or `None` if none does.
    """
    for location in locations or []:
        chrom, _, pos = str(location).partition(":")
        if chrom != region.chrom or not pos.isdigit():
            continue
        if region.start <= int(pos) <= region.end:
            return str(location)
    return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _maf_at_or_above_threshold(maf: str | None, maf_threshold: float) -> bool:
    """Check whether a GWAS Catalog v2 `risk_frequency` clears `maf_threshold`.

    Parameters
    ----------
    maf : `str` or `NoneType`
        Value of an association record's `risk_frequency` field: the
        risk-allele frequency, not a MAF. Not always numeric (e.g. blank
        or "NR").
    maf_threshold : `float`
        Threshold to compare against.

    Returns
    -------
    `bool`
        `True` only if `maf` parses to a float `f` with
        `min(f, 1 - f) >= maf_threshold`, so a rare variant reported with
        its common allele as risk allele (e.g. `f = 0.995`) is kept.
        Missing or unparseable values are treated as not excluding the
        record.
    """
    if maf is None:
        return False
    try:
        frequency = float(maf)
    except ValueError:
        return False
    return min(frequency, 1.0 - frequency) >= maf_threshold


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _plain_header(tabix_source: str) -> list[str]:
    """Read a sumstats file's first line as its header.

    Fallback for when a tabix index has no comment-prefixed header line
    (e.g. GWAS Catalog harmonised files, whose header row is excluded
    from the `.tbi` index via a skip-lines count rather than a `#`
    comment character, so `pysam.TabixFile.header` returns `[]`).

    Parameters
    ----------
    tabix_source : `str`
        Path or URL to the bgzip-compressed sumstats file.

    Returns
    -------
    header : `list[str]`
        The first line's tab-separated fields.
    """
    if tabix_source.startswith(("http://", "https://", "ftp://")):
        with requests.get(tabix_source, stream=True, timeout=30) as response:
            response.raise_for_status()
            with gzip.GzipFile(fileobj=response.raw) as gz:
                line = gz.readline().decode("utf-8")
    else:
        with gzip.open(tabix_source, "rt") as fh:
            line = fh.readline()
    # CRLF source files leave a trailing "\r" on the last column name
    return line.rstrip("\r\n").split("\t")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_freq(value: str) -> float | None:
    """Parse an allele-frequency field, treating missing values as `None`.

    Parameters
    ----------
    value : `str`
        Raw field value (e.g. "0.012", "NA", "").

    Returns
    -------
    freq : `float` or `NoneType`
        The frequency, or `None` if the field is missing/non-numeric/NaN.
    """
    try:
        freq = float(value)
    except ValueError:
        return None
    if freq != freq:  # NaN
        return None
    return freq


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _passes_maf(
    fields: list[str],
    maf_idx: int,
    maf_threshold: float,
    transform_to_maf: bool,
) -> bool:
    """Check one sumstats row against the MAF cutoff.

    Parameters
    ----------
    fields : `list[str]`
        The row's tab-split fields.
    maf_idx : `int`
        Index of the allele-frequency column.
    maf_threshold : `float`
        Rows with MAF below this pass.
    transform_to_maf : `bool`
        Apply `min(af, 1 - af)` before comparing (see
        `filter_sumstats_regions`).

    Returns
    -------
    passes : `bool`
        `True` if the frequency parses and is below `maf_threshold`.
    """
    maf = _parse_freq(fields[maf_idx])
    if maf is None:
        return False
    if transform_to_maf:
        maf = min(maf, 1.0 - maf)
    return maf < maf_threshold


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _norm_chrom(value: str) -> str:
    """Normalise a sumstats chromosome field to the gene-region form.

    Parameters
    ----------
    value : `str`
        Raw chromosome field (e.g. "16", " 16", "chr16").

    Returns
    -------
    chrom : `str`
        `value` without surrounding whitespace or a leading "chr"/"CHR"
        (e.g. "16").
    """
    chrom = value.strip()
    if chrom[:3].lower() == "chr":
        chrom = chrom[3:]
    return chrom


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _warn_if_empty(
    source: str,
    n_rows: int,
    n_in_region: int,
    n_no_freq: int,
    maf_threshold: float,
) -> None:
    """Warn with a likely cause when a sumstats file yields 0 rows.

    Parameters
    ----------
    source : `str`
        Path or URL of the sumstats file (message only).
    n_rows : `int`
        Rows kept after the region and MAF filters.
    n_in_region : `int`
        Rows inside any gene region, before the MAF filter.
    n_no_freq : `int`
        Of `n_in_region`, rows with a missing/non-numeric frequency.
    maf_threshold : `float`
        MAF cutoff used (message only).

    Returns
    -------
    `None`

    Notes
    -----
    0 rows in region points to a build, coverage or parsing problem;
    rows in region but none kept points to missing frequencies or an
    author-side MAF filter.
    """
    if n_rows > 0:
        return
    if n_in_region == 0:
        log_warn(
            f"{source}: 0 rows -- 0 in region (check build, coverage or "
            f"chrom/pos format)"
        )
        return
    log_warn(
        f"{source}: 0 rows -- {n_in_region} in region, {n_no_freq} "
        f"missing frequency, none with MAF < {maf_threshold}"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _header_indices(
    header: list[str], url: str, columns: list[str]
) -> list[int]:
    """Look up the positions of the required columns in a header.

    Parameters
    ----------
    header : `list[str]`
        The sumstats file's column names.
    url : `str`
        URL of the sumstats file (error message only).
    columns : `list[str]`
        Column names to look up.

    Returns
    -------
    indices : `list[int]`
        The index of each of `columns` in `header`, in the same order.

    Raises
    ------
    SumstatsColumnError
        If any of `columns` is not in `header`.
    """
    missing = [col for col in columns if col not in header]
    if missing:
        raise SumstatsColumnError(
            f"{url}: missing column(s) {missing}; header: {header}"
        )
    return [header.index(col) for col in columns]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_sumstats_regions(
    tabix_source: str,
    regions: dict[str, GeneRegion],
    maf_col: str,
    maf_threshold: float,
    chrom_col: str = "chromosome",
    pos_col: str = "base_pair_location",
    transform_to_maf: bool = False,
) -> pd.DataFrame:
    """Filter a tabix-indexed sumstats file to gene regions and a MAF cutoff.

    Based on GWAS catalog downloads, but should work on any
    bgzip+tabix-indexed sumstats file. The file (and its remote `.tbi`)
    is opened once and queried once per region.

    Parameters
    ----------
    tabix_source : `str`
        Path or URL to a bgzip+tabix-indexed sumstats file.
    regions : `dict[str, GeneRegion]`
        Gene symbol -> region to query.
    maf_col : `str`
        Name of the allele-frequency column.
    maf_threshold : `float`
        Only rows with MAF below this are kept.
    chrom_col : `str`, optional, default: `"chromosome"`
        Name of the chromosome column in the file header.
    pos_col : `str`, optional, default: `"base_pair_location"`
        Name of the position column in the file header.
    transform_to_maf : `bool`, optional, default: `False`
        If `True`, `maf_col` is treated as a single-allele frequency
        (which may exceed 0.5) rather than a true minor-allele frequency,
        and `min(af, 1 - af)` is applied before the threshold comparison.

    Returns
    -------
    filtered : `pd.DataFrame`
        A leading `gene` column plus the file's columns: rows in each
        gene's region with MAF < `maf_threshold`. A row in overlapping
        regions appears once per gene. A gene whose chromosome is absent
        from the index contributes no rows.

    Raises
    ------
    OSError
        If `tabix_source` has no `.tbi` index (no remote-tabix fallback is
        implemented here -- see gwas_cat.md's caveat on falling back to a
        full-file download).
    SumstatsColumnError
        If `chrom_col`, `pos_col`, or `maf_col` are not in the file's
        header.
    """
    import pysam

    with pysam.TabixFile(tabix_source) as tabix_file:
        header_lines = tabix_file.header
        header = (
            header_lines[0].lstrip("#").rstrip("\r\n").split("\t")
            if header_lines
            else _plain_header(tabix_source)
        )
        chrom_idx, pos_idx, maf_idx = _header_indices(
            header, tabix_source, [chrom_col, pos_col, maf_col]
        )
        log_debug(
            f"header columns: chrom={chrom_idx} pos={pos_idx} maf={maf_idx}"
        )

        records = []
        n_in_region = 0
        n_no_freq = 0
        contigs = set(tabix_file.contigs)
        for gene, region in regions.items():
            # sparse sumstats can lack whole chromosomes; fetch() on a
            # contig absent from the index raises ValueError. Some files
            # name contigs "chr16" rather than "16".
            contig = region.chrom
            if contig not in contigs and f"chr{contig}" in contigs:
                contig = f"chr{contig}"
            if contig not in contigs:
                log_info(
                    f"{gene} @ chr{region.chrom}: chromosome not in "
                    f"{tabix_source} -> 0 rows"
                )
                continue
            n_before = len(records)
            for line in tabix_file.fetch(contig, region.start, region.end):
                # CRLF source files leave a trailing "\r" on the last field
                fields = line.rstrip("\r\n").split("\t")
                n_in_region += 1
                if _parse_freq(fields[maf_idx]) is None:
                    n_no_freq += 1
                elif _passes_maf(
                    fields, maf_idx, maf_threshold, transform_to_maf
                ):
                    records.append([gene, *fields])
            log_debug(
                f"{gene} @ {region.chrom}:{region.start}-{region.end} -> "
                f"{len(records) - n_before} rows"
            )

    log_info(
        f"{tabix_source} @ {len(regions)} regions -> {len(records)} rows "
        f"with MAF < {maf_threshold}"
    )
    _warn_if_empty(
        tabix_source, len(records), n_in_region, n_no_freq, maf_threshold
    )
    return pd.DataFrame.from_records(
        records, columns=[ColumnNames.GENE, *header]
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_raw_sumstats_regions(
    url: str,
    regions: dict[str, GeneRegion],
    maf_col: str,
    maf_threshold: float,
    chrom_col: str = "chromosome",
    pos_col: str = "base_pair_location",
    transform_to_maf: bool = False,
) -> pd.DataFrame:
    """Stream-filter a non-indexed sumstats file to gene regions and MAF.

    No tabix index is available for raw (non-harmonised) sumstats files,
    so the file is scanned sequentially via HTTP streaming, decompressed
    on the fly if gzip-compressed; only matching rows are held in memory.
    Rows are not assumed sorted, so the full file is always scanned --
    once, whatever the number of regions.

    Parameters
    ----------
    url : `str`
        URL of the raw (non-tabix-indexed) sumstats file.
    regions : `dict[str, GeneRegion]`
        Gene symbol -> region to filter to.
    maf_col : `str`
        Name of the allele-frequency column.
    maf_threshold : `float`
        Only rows with MAF below this are kept.
    chrom_col : `str`, optional, default: `"chromosome"`
        Name of the chromosome column in the file header.
    pos_col : `str`, optional, default: `"base_pair_location"`
        Name of the position column in the file header.
    transform_to_maf : `bool`, optional, default: `False`
        If `True`, `maf_col` is treated as a single-allele frequency
        (which may exceed 0.5) rather than a true minor-allele frequency,
        and `min(af, 1 - af)` is applied before the threshold comparison.

    Returns
    -------
    filtered : `pd.DataFrame`
        A leading `gene` column plus the file's columns: rows in each
        gene's region with MAF < `maf_threshold`. A row in overlapping
        regions appears once per gene.

    Raises
    ------
    SumstatsColumnError
        If `chrom_col`, `pos_col`, or `maf_col` are not in the file's
        header.
    """
    # chrom -> [(gene, region)], so each line is only tested against the
    # regions on its own chromosome
    regions_by_chrom: dict[str, list[tuple[str, GeneRegion]]] = {}
    for gene, region in regions.items():
        regions_by_chrom.setdefault(region.chrom, []).append((gene, region))

    with requests.get(url, stream=True, timeout=60) as response:
        response.raise_for_status()
        raw_stream = response.raw
        if url.endswith(".gz"):
            raw_stream = gzip.GzipFile(fileobj=raw_stream)
        text_stream = io.TextIOWrapper(raw_stream, encoding="utf-8")

        header = next(text_stream).rstrip("\r\n").split("\t")
        chrom_idx, pos_idx, maf_idx = _header_indices(
            header, url, [chrom_col, pos_col, maf_col]
        )
        log_debug(
            f"header columns: chrom={chrom_idx} pos={pos_idx} maf={maf_idx}"
        )

        records = []
        n_in_region = 0
        n_no_freq = 0
        for line in text_stream:
            fields = line.rstrip("\r\n").split("\t")
            # author files may pad fields (e.g. "   940005") or prefix
            # "chr"; left as-is in the output, only matched normalised
            chrom_regions = regions_by_chrom.get(
                _norm_chrom(fields[chrom_idx])
            )
            if chrom_regions is None:
                continue
            pos = fields[pos_idx].strip()
            if not pos.isdigit():
                continue
            genes = [
                gene
                for gene, region in chrom_regions
                if region.start <= int(pos) <= region.end
            ]
            if not genes:
                continue
            n_in_region += 1
            if _parse_freq(fields[maf_idx]) is None:
                n_no_freq += 1
            elif _passes_maf(
                fields, maf_idx, maf_threshold, transform_to_maf
            ):
                records.extend([gene, *fields] for gene in genes)

    log_info(
        f"{url} @ {len(regions)} regions -> {len(records)} rows with "
        f"MAF < {maf_threshold} (raw scan)"
    )
    _warn_if_empty(url, len(records), n_in_region, n_no_freq, maf_threshold)
    return pd.DataFrame.from_records(
        records, columns=[ColumnNames.GENE, *header]
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _open_targets_query(query: str, variables: dict) -> dict:
    """Run one Open Targets GraphQL query.

    Parameters
    ----------
    query : `str`
        GraphQL query text.
    variables : `dict`
        Query variables.

    Returns
    -------
    data : `dict`
        The response's `data` object.

    Raises
    ------
    requests.HTTPError
        On an HTTP error status.
    RuntimeError
        If the response reports GraphQL errors (these come with HTTP 200).
    """
    response = requests.post(
        Constants.OPEN_TARGETS_GRAPHQL_URL,
        json={"query": query, "variables": variables},
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("errors"):
        raise RuntimeError(f"Open Targets query failed: {payload['errors']}")
    return payload["data"]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def open_targets_disease_ids(
    outcome_efo_ids: Mapping[str, Sequence[str]],
) -> dict[str, set[tuple[str, str]]]:
    """Map Open Targets disease IDs to the outcome trait IDs they count for.

    Open Targets evidence only matches exact disease IDs, so each outcome
    `efo_id` is widened to its `Constants.OPEN_TARGETS_EXTRA_DISEASE_IDS`
    and, for child-trait outcomes (`includes_child_traits`), to the
    Open Targets descendants of those IDs.

    Parameters
    ----------
    outcome_efo_ids : `Mapping[str, Sequence[str]]`
        Outcome -> its `efo_id` values.

    Returns
    -------
    lookup : `dict[str, set[tuple[str, str]]]`
        Open Targets disease ID -> the `(outcome, efo_id)` pairs it
        belongs to. IDs unknown to Open Targets are left out (warned).
    """
    query_ids: dict[str, set[str]] = {}
    for _, efo_ids in outcome_efo_ids.items():
        for efo_id in efo_ids:
            query_ids[efo_id] = {efo_id} | set(
                Constants.OPEN_TARGETS_EXTRA_DISEASE_IDS.get(efo_id, ())
            )
    all_ids = sorted(set().union(*query_ids.values())) if query_ids else []
    data = _open_targets_query(
        "query Diseases($ids: [String!]!) {"
        " diseases(efoIds: $ids) { id descendants } }",
        {"ids": all_ids},
    )
    descendants = {d["id"]: d["descendants"] for d in data["diseases"]}
    for disease_id in all_ids:
        if disease_id not in descendants:
            log_warn(f"{disease_id} unknown to Open Targets, not queried")

    lookup: dict[str, set[tuple[str, str]]] = {}
    for outcome, efo_ids in outcome_efo_ids.items():
        child_traits = includes_child_traits(outcome)
        for efo_id in efo_ids:
            for disease_id in query_ids[efo_id]:
                if disease_id not in descendants:
                    continue
                matched = [disease_id]
                if child_traits:
                    matched += descendants[disease_id]
                for match in matched:
                    lookup.setdefault(match, set()).add((outcome, efo_id))
    log_info(
        f"Open Targets disease ids: {len(lookup)} "
        f"(from {len(all_ids)} outcome ids)"
    )
    return lookup


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_burden_evidence(
    ensembl_id: str, disease_ids: Collection[str]
) -> pd.DataFrame:
    """Fetch gene-based rare-variant burden evidence from Open Targets.

    Parameters
    ----------
    ensembl_id : `str`
        Ensembl gene ID of the target.
    disease_ids : `Collection[str]`
        Open Targets disease IDs to fetch evidence for (exact matches).

    Returns
    -------
    evidence : `pd.DataFrame`
        One row per `gene_burden` evidence record (all pages), with the
        evidence fields plus `disease_id`, `disease_name`, `p_value` and
        `neg_log10_p`. Empty if none.
    """
    query = """
    query GeneBurden(
      $ensemblId: String!, $efoIds: [String!]!, $size: Int!, $cursor: String
    ) {
      target(ensemblId: $ensemblId) {
        evidences(
          efoIds: $efoIds, datasourceIds: ["gene_burden"],
          size: $size, cursor: $cursor
        ) {
          cursor
          rows {
            disease { id name }
            studyId projectId cohortId ancestry statisticalMethod
            studySampleSize score pValueMantissa pValueExponent
            beta betaConfidenceIntervalLower betaConfidenceIntervalUpper
            oddsRatio oddsRatioConfidenceIntervalLower
            oddsRatioConfidenceIntervalUpper
          }
        }
      }
    }
    """
    records: list[dict] = []
    cursor = None
    while disease_ids:
        data = _open_targets_query(
            query,
            {
                "ensemblId": ensembl_id,
                "efoIds": sorted(disease_ids),
                "size": Constants.OPEN_TARGETS_PAGE_SIZE,
                "cursor": cursor,
            },
        )
        if data["target"] is None:
            log_warn(f"{ensembl_id} unknown to Open Targets")
            break
        evidences = data["target"]["evidences"]
        for row in evidences["rows"]:
            disease = row.pop("disease")
            records.append(
                {
                    "disease_id": disease["id"],
                    "disease_name": disease["name"],
                    **row,
                }
            )
        cursor = evidences["cursor"]
        if not cursor or not evidences["rows"]:
            break

    evidence = pd.DataFrame.from_records(records)
    if not evidence.empty:
        mantissa = pd.to_numeric(evidence["pValueMantissa"], errors="coerce")
        exponent = pd.to_numeric(evidence["pValueExponent"], errors="coerce")
        evidence["p_value"] = mantissa * 10.0**exponent
        # from mantissa/exponent so tiny p-values do not underflow to 0
        evidence["neg_log10_p"] = -(
            np.log10(mantissa.where(mantissa > 0)) + exponent
        )
    # printed only; merge_associations records one summary line
    log_debug(f"{ensembl_id} -> {len(evidence)} gene-burden evidence rows")
    return evidence


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# harmonisation

def harmonise_frame(
    df: pd.DataFrame,
    column_map: dict[str, str],
    has_variants: bool = True,
    parsed: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Map one source's table onto the shared final-results schema.

    Parameters
    ----------
    df : `pd.DataFrame`
        One source's rows, with its original columns plus any identity
        columns (`HarmonisedColumns.IDENTITY_COLUMNS`) already set.
    column_map : `dict[str, str]`
        Core column -> original column, from `SourceColumnMaps`.
    has_variants : `bool`, optional, default: `True`
        `False` for gene-level rows (gene burden): `maf_status` is then
        left NA instead of flagging a missing MAF.
    parsed : `pd.DataFrame` or `NoneType`, optional, default: `None`
        Core-named columns already parsed from `df` (same index), which
        take precedence over `column_map` (see `harmonise_curated`).

    Returns
    -------
    harmonised : `pd.DataFrame`
        `HarmonisedColumns.CORE_ORDER` columns, then every original,
        non-identity column of `df` as `src_<name>`.

    Notes
    -----
    Values derived only where missing: `p_value` <-> `neg_log10_p`, and
    `maf = min(eaf, 1 - eaf)`. `maf_status` is `numeric` where `maf`
    is known and `not_reported` otherwise. `variant_id` is always
    derived as `chrom:pos:other_allele:effect_allele` (NA if any part is
    missing); a source's own `variant_id` is kept as `src_variant_id`.
    `duplicate_variant` is left NA here (see `flag_duplicate_variants`).
    """
    hc = HarmonisedColumns
    core = pd.DataFrame(index=df.index)
    for col in hc.CORE_ORDER:
        if parsed is not None and col in parsed.columns:
            core[col] = parsed[col]
        elif col in column_map and column_map[col] in df.columns:
            core[col] = df[column_map[col]]
        elif col in hc.IDENTITY_COLUMNS and col in df.columns:
            core[col] = df[col]
        else:
            core[col] = pd.NA
    for col in hc.NUMERIC_COLUMNS:
        core[col] = pd.to_numeric(core[col], errors="coerce")
    # nullable types so NA rows do not turn "16" / 56961324 into floats
    core[hc.POS] = core[hc.POS].round().astype("Int64")
    core[hc.CHROM] = (
        core[hc.CHROM]
        .astype("string")
        .str.strip()
        .str.replace(r"(?i)^chr", "", regex=True)
        .str.replace(r"\.0$", "", regex=True)
    )
    _derive_columns(core, has_variants)
    raw = df.drop(
        columns=[c for c in df.columns if c in hc.IDENTITY_COLUMNS]
    ).add_prefix(hc.RAW_PREFIX)
    return pd.concat([core, raw], axis=1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _derive_columns(core: pd.DataFrame, has_variants: bool) -> None:
    """Fill derivable core columns in place.

    `p_value`, `neg_log10_p` and `maf` are filled only where missing;
    `variant_id` is always rebuilt as `chrom:pos:other:effect`.

    Parameters
    ----------
    core : `pd.DataFrame`
        Core columns with numeric columns already converted.
    has_variants : `bool`
        If `False`, `maf_status` and `variant_id` are left NA.

    Returns
    -------
    `None`
    """
    hc = HarmonisedColumns
    neg_log10 = core[hc.NEG_LOG10_P]
    p_value = core[hc.P_VALUE]
    core[hc.P_VALUE] = p_value.fillna(10.0 ** -neg_log10)
    # p == 0 (underflow) has no finite -log10, so it stays NA
    positive_p = core[hc.P_VALUE].where(core[hc.P_VALUE] > 0)
    core[hc.NEG_LOG10_P] = neg_log10.fillna(-np.log10(positive_p))
    eaf = core[hc.EAF]
    core[hc.MAF] = core[hc.MAF].fillna(eaf.where(eaf <= 0.5, 1.0 - eaf))
    if has_variants:
        core[hc.MAF_STATUS] = np.where(
            core[hc.MAF].notna(), MafStatus.NUMERIC, MafStatus.NOT_REPORTED
        )
        parts = [
            core[col].astype("string").str.strip()
            for col in (hc.CHROM, hc.POS, hc.OTHER_ALLELE, hc.EFFECT_ALLELE)
        ]
        complete = pd.concat(parts, axis=1).notna().all(axis=1)
        variant_id = parts[0].str.cat(parts[1:], sep=":")
        core[hc.VARIANT_ID] = variant_id.where(complete, pd.NA)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def flag_duplicate_variants(df: pd.DataFrame) -> pd.DataFrame:
    """Flag rows that repeat a variant within one study/outcome/gene.

    E.g. two source variants harmonised to the same site. Rows are kept;
    only `duplicate_variant` is set.

    Parameters
    ----------
    df : `pd.DataFrame`
        Harmonised rows (`HarmonisedColumns.CORE_ORDER` columns).

    Returns
    -------
    flagged : `pd.DataFrame`
        `df` with `duplicate_variant` `True` for every row sharing
        `source`, `study_accession`, `outcome`, `gene` and a non-NA
        `variant_id` with another row, else `False`.
    """
    hc = HarmonisedColumns
    keys = [hc.SOURCE, hc.STUDY_ACCESSION, hc.OUTCOME, hc.GENE, hc.VARIANT_ID]
    has_id = df[hc.VARIANT_ID].notna()
    duplicated = df[keys].astype("string").duplicated(keep=False)
    flagged = df.copy()
    flagged[hc.DUPLICATE_VARIANT] = (duplicated & has_id).astype(bool)
    return flagged


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def harmonise_curated(df: pd.DataFrame) -> pd.DataFrame:
    """Harmonise curated GWAS Catalog association records.

    Parameters
    ----------
    df : `pd.DataFrame`
        Rows from `filter_curated_associations`, with the identity columns
        (`gene`, `outcome`, `efo_id`, `source`, ...) already set.

    Returns
    -------
    harmonised : `pd.DataFrame`
        As `harmonise_frame`, with location, allele, effect, p-value,
        frequency and trait parsed from the curated record fields.
    """
    hc = HarmonisedColumns
    parsed = pd.DataFrame(index=df.index)

    # the in-region location (see filter_curated_associations), not
    # simply the first one, so chrom/pos always fall inside the gene
    locations = df["locations"].map(_first_item)
    if "region_location" in df.columns:
        locations = df["region_location"].where(
            df["region_location"].notna(), locations
        )
    parsed[hc.CHROM] = locations.map(lambda v: _split_location(v)[0])
    parsed[hc.POS] = locations.map(lambda v: _split_location(v)[1])

    alleles = df["snp_effect_allele"].map(_first_item)
    parsed[hc.RSID] = alleles.map(lambda v: _split_risk_allele(v)[0])
    parsed[hc.EFFECT_ALLELE] = alleles.map(lambda v: _split_risk_allele(v)[1])

    parsed[hc.EAF] = pd.to_numeric(df["risk_frequency"], errors="coerce")
    parsed[hc.BETA] = df["beta"].map(_parse_curated_beta)
    mantissa = pd.to_numeric(df["pvalue_mantissa"], errors="coerce")
    exponent = pd.to_numeric(df["pvalue_exponent"], errors="coerce")
    parsed[hc.P_VALUE] = mantissa * 10.0**exponent
    # computed directly: very small p-values (e.g. 2e-1861) underflow to 0
    parsed[hc.NEG_LOG10_P] = -(np.log10(mantissa) + exponent)
    parsed[hc.TRAIT_LABEL] = df["reported_trait"].map(_first_item)
    if "efo_traits" in df.columns:
        traits = df["efo_traits"].map(mapped_traits)
        parsed[hc.MAPPED_TRAIT_ID] = traits.map(lambda t: t[0] or pd.NA)
        parsed[hc.MAPPED_TRAIT] = traits.map(lambda t: t[1] or pd.NA)
    return harmonise_frame(df, SourceColumnMaps.CURATED, parsed=parsed)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _first_item(value: object) -> object:
    """Return the first element of a list-valued curated field.

    Parameters
    ----------
    value : `object`
        A list, a string repr of a list (as read back from a TSV), a
        scalar, or NA.

    Returns
    -------
    item : `object`
        The first element, the scalar itself, or `pd.NA` if empty/NA.
    """
    if isinstance(value, str) and value.startswith("["):
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value
    if isinstance(value, (list, tuple)):
        return value[0] if value else pd.NA
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return pd.NA
    return value


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _split_location(value: object) -> tuple[object, object]:
    """Split a GWAS Catalog v2 `"chrom:pos"` location.

    Parameters
    ----------
    value : `object`
        A location string such as `"16:56961324"`, or NA.

    Returns
    -------
    chrom_pos : `tuple[object, object]`
        `(chrom, pos)` as strings, or `(pd.NA, pd.NA)` if unparseable.
    """
    if not isinstance(value, str) or ":" not in value:
        return pd.NA, pd.NA
    chrom, _, pos = value.partition(":")
    return chrom, pos


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _split_risk_allele(value: object) -> tuple[object, object]:
    """Split a GWAS Catalog `"rsid-allele"` risk-allele string.

    Parameters
    ----------
    value : `object`
        A string such as `"rs183130-T"` or `"rs1800775-?"`, or NA.

    Returns
    -------
    rsid_allele : `tuple[object, object]`
        `(rsid, allele)`; the allele is `pd.NA` when unknown (`"?"`).
        `(value, pd.NA)` if there is no allele part.
    """
    if not isinstance(value, str):
        return pd.NA, pd.NA
    match = _CURATED_ALLELE_PATTERN.match(value)
    if match is None:
        return value, pd.NA
    allele = match.group("allele")
    return match.group("rsid"), pd.NA if allele == "?" else allele


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_curated_beta(value: object) -> float:
    """Parse a curated effect such as `"0.18 g/l increase"` to a number.

    Parameters
    ----------
    value : `object`
        The curated `beta` field: a number, a text effect, or NA.

    Returns
    -------
    beta : `float`
        The effect: negative when the text says "decrease", positive when
        it says "increase", else the number as given; NaN if unparseable.
    """
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str):
        return float("nan")
    match = _CURATED_BETA_PATTERN.match(value)
    if match is None:
        return float("nan")
    beta = float(match.group("value"))
    text = match.group("text").lower()
    if "decrease" in text:
        return -abs(beta)
    if "increase" in text:
        return abs(beta)
    return beta


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ensembl variant check

# fields kept per overlap/region record in the cache
_ENSEMBL_VARIANT_FIELDS: tuple[str, ...] = (
    "id",
    "seq_region_name",
    "start",
    "strand",
    "alleles",
)
# fields kept per variation-endpoint mapping in the cache
_ENSEMBL_MAPPING_FIELDS: tuple[str, ...] = (
    "assembly_name",
    "seq_region_name",
    "start",
    "strand",
    "allele_string",
)
_COMPLEMENT = str.maketrans("ACGT", "TGCA")
# candidate preference when several Ensembl variants fit a row
_ALLELE_CHECK_RANK: dict[str, int] = {
    EnsemblAlleleCheck.MATCH: 0,
    EnsemblAlleleCheck.FLIPPED: 0,
    EnsemblAlleleCheck.STRAND_FLIP: 1,
    EnsemblAlleleCheck.EFFECT_UNKNOWN: 2,
    EnsemblAlleleCheck.MISMATCH: 3,
}


@dataclass
class EnsemblVariant:
    """One Ensembl variant, alleles on the forward strand.

    Attributes
    ----------
    rsid : `str`
        Ensembl variant id (e.g. "rs429358").
    chrom : `str`
        GRCh38 chromosome name.
    start : `int`
        GRCh38 start position (1-based).
    alleles : `tuple[str, ...]`
        Ref allele first, then the alts; `"-"` for an empty allele.
    """
    rsid: str
    chrom: str
    start: int
    alleles: tuple[str, ...]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _read_json_gz(path: Path) -> object:
    """Read a gzipped JSON file.

    Parameters
    ----------
    path : `Path`
        A `.json.gz` file.

    Returns
    -------
    data : `object`
        The decoded JSON.
    """
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _write_json_gz_atomic(path: Path, data: object) -> None:
    """Write `data` as gzipped JSON via a temp file, then rename.

    An interrupted run leaves at most a `.tmp` file, never a truncated
    cache file that later runs would trust.

    Parameters
    ----------
    path : `Path`
        Destination `.json.gz` file; its directory is created if needed.
    data : `object`
        JSON-serialisable data.

    Returns
    -------
    `None`
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(path.name + ".tmp")
    with gzip.open(tmp_path, "wt", encoding="utf-8") as handle:
        json.dump(data, handle)
    tmp_path.replace(path)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _complement(allele: str | None) -> str | None:
    """Reverse-complement an allele (`"-"` and `None` are returned as-is).

    Parameters
    ----------
    allele : `str` or `NoneType`
        Upper-case nucleotide allele, `"-"`, or `None`.

    Returns
    -------
    complement : `str` or `NoneType`
        The reverse complement; non-ACGT characters are left unchanged.
    """
    if allele is None or allele == "-":
        return allele
    return allele.translate(_COMPLEMENT)[::-1]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ensembl_variant(
    rsid: object,
    chrom: object,
    start: object,
    strand: object,
    alleles: Sequence[object] | None,
) -> EnsemblVariant | None:
    """Build an `EnsemblVariant` from raw Ensembl fields.

    Parameters
    ----------
    rsid : `object`
        Ensembl variant id.
    chrom : `object`
        Chromosome name.
    start : `object`
        Start position.
    strand : `object`
        `1` or `-1`; alleles on `-1` are reverse-complemented.
    alleles : `Sequence` or `NoneType`
        Ensembl alleles, ref first.

    Returns
    -------
    variant : `EnsemblVariant` or `NoneType`
        `None` when fields are missing, there are fewer than two alleles,
        or any allele is not plain ACGT/`"-"` (e.g. "HGMD_MUTATION").
    """
    if rsid is None or chrom is None or start is None or not alleles:
        return None
    clean = tuple(str(allele).upper() for allele in alleles)
    if len(clean) < 2 or not all(
        _ENSEMBL_ALLELE_PATTERN.match(allele) for allele in clean
    ):
        return None
    if strand == -1:
        clean = tuple(_complement(allele) for allele in clean)
    return EnsemblVariant(
        rsid=str(rsid), chrom=str(chrom), start=int(start), alleles=clean
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ensembl_read_with_retry(profile: str, **params: str) -> object:
    """Run an `EnsemblReader` profile, retrying transient failures.

    Retries when the wrapped cause is an HTTP 5xx response, a timeout or
    a dropped connection, like `_get_with_retry`.

    Parameters
    ----------
    profile : `str`
        `EnsemblReader` profile, e.g. "overlap_region" or "variation".
    **params : `str`
        The profile's parameters.

    Returns
    -------
    result : `object`
        The reader's result (with `.records`).

    Raises
    ------
    ReaderError
        If the last attempt fails, or on any non-transient failure (e.g.
        400/404) without retrying.

    Notes
    -----
    Makes `len(Constants.HTTP_RETRY_BACKOFF) + 1` attempts, sleeping the
    listed number of seconds before each retry.
    """
    n_retries = len(Constants.HTTP_RETRY_BACKOFF)
    for attempt, wait in enumerate((*Constants.HTTP_RETRY_BACKOFF, None), 1):
        try:
            return EnsemblReader().read(profile=profile, **params)
        except ReaderError as err:
            cause = err.__cause__
            response = getattr(cause, "response", None)
            transient = isinstance(
                cause, (requests.Timeout, requests.ConnectionError)
            ) or (response is not None and response.status_code >= 500)
            if not transient or wait is None:
                raise
            reason = (
                f"HTTP {response.status_code}"
                if response is not None
                else type(cause).__name__
            )
        log_warn(
            f"Ensembl {profile} {params}: {reason}, "
            f"retry {attempt}/{n_retries} in {wait}s"
        )
        time.sleep(wait)
    raise AssertionError("unreachable")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ensembl_window_records(
    chrom: str, start: int, end: int
) -> tuple[list[dict], bool]:
    """Return Ensembl overlap/region variation records for one window.

    Read from `Paths.ENSEMBL_CACHE` when cached, else fetched through
    biomed-api and cached (trimmed to `_ENSEMBL_VARIANT_FIELDS`).

    Parameters
    ----------
    chrom : `str`
        Chromosome name.
    start : `int`
        Window start (1-based, inclusive).
    end : `int`
        Window end (inclusive).

    Returns
    -------
    records : `list[dict]`
        Trimmed variation records overlapping the window.
    fetched : `bool`
        `True` if the window was fetched from Ensembl, `False` if cached.

    Raises
    ------
    ReaderError
        If the Ensembl request fails.
    """
    path = Paths.ENSEMBL_CACHE / f"overlap_{chrom}_{start}_{end}.json.gz"
    if path.exists():
        return list(_read_json_gz(path)), False
    result = _ensembl_read_with_retry(
        profile="overlap_region",
        region=f"{chrom}:{start}-{end}",
        feature="variation",
    )
    records = [
        {field: record.get(field) for field in _ENSEMBL_VARIANT_FIELDS}
        for record in result.records
    ]
    _write_json_gz_atomic(path, records)
    return records, True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fetch_ensembl_region_variants(
    region: GeneRegion,
) -> tuple[list[EnsemblVariant], int]:
    """Fetch every Ensembl variant in a gene region, window by window.

    The region is split into `Constants.ENSEMBL_OVERLAP_WINDOW_BP`
    windows; each window is cached separately, so an interrupted run
    resumes where it stopped.

    Parameters
    ----------
    region : `GeneRegion`
        Flanked gene region (GRCh38).

    Returns
    -------
    variants : `list[EnsemblVariant]`
        Usable variants (see `_ensembl_variant`), each once even when it
        spans a window boundary.
    n_fetched : `int`
        Number of windows fetched from Ensembl (the rest were cached).

    Raises
    ------
    ReaderError
        If an Ensembl request fails.
    """
    window = Constants.ENSEMBL_OVERLAP_WINDOW_BP
    variants: list[EnsemblVariant] = []
    seen: set[tuple[str, int]] = set()
    n_fetched = 0
    for start in range(region.start, region.end + 1, window):
        end = min(start + window - 1, region.end)
        records, fetched = _ensembl_window_records(region.chrom, start, end)
        n_fetched += int(fetched)
        for record in records:
            variant = _ensembl_variant(
                record.get("id"),
                record.get("seq_region_name"),
                record.get("start"),
                record.get("strand"),
                record.get("alleles"),
            )
            if variant is None or (variant.rsid, variant.start) in seen:
                continue
            seen.add((variant.rsid, variant.start))
            variants.append(variant)
    return variants, n_fetched


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ensembl_rsid_variants(rsid: str) -> tuple[list[EnsemblVariant], bool]:
    """Look up one rsid with the Ensembl variation endpoint (cached).

    An rsid Ensembl does not know is cached as having no mappings, so it
    is not requested again.

    Parameters
    ----------
    rsid : `str`
        Lower-case rsid, e.g. "rs429358".

    Returns
    -------
    variants : `list[EnsemblVariant]`
        One variant per GRCh38 primary-chromosome mapping; empty if the
        rsid is unknown.
    fetched : `bool`
        `True` if requested from Ensembl, `False` if cached.

    Raises
    ------
    ReaderError
        If the request fails for any reason other than "not found".
    """
    path = Paths.ENSEMBL_CACHE / f"variation_{rsid}.json.gz"
    fetched = False
    if path.exists():
        data = _read_json_gz(path)
    else:
        try:
            result = _ensembl_read_with_retry(profile="variation", id=rsid)
            record = result.records[0] if result.records else {}
        except ReaderError as err:
            if not _is_not_found(err):
                raise
            record = {}
        data = {
            "name": record.get("name", rsid),
            "mappings": [
                {
                    field: mapping.get(field)
                    for field in _ENSEMBL_MAPPING_FIELDS
                }
                for mapping in record.get("mappings") or []
            ],
        }
        _write_json_gz_atomic(path, data)
        fetched = True
    variants = []
    for mapping in data["mappings"]:
        chrom = str(mapping.get("seq_region_name"))
        if (
            mapping.get("assembly_name") != Constants.GRCH_BUILD
            or not _PRIMARY_CHROM_PATTERN.match(chrom)
        ):
            continue
        variant = _ensembl_variant(
            data["name"],
            chrom,
            mapping.get("start"),
            mapping.get("strand"),
            str(mapping.get("allele_string") or "").split("/"),
        )
        if variant is not None:
            variants.append(variant)
    return variants, fetched


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _clean_allele(value: object) -> str | None:
    """Normalise a row allele to upper case, or `None` when unknown.

    Parameters
    ----------
    value : `object`
        An allele cell (string, NA or `None`).

    Returns
    -------
    allele : `str` or `NoneType`
        Upper-case stripped allele; `None` for NA, blank, `"?"` or "NA".
    """
    if value is None or pd.isna(value):
        return None
    allele = str(value).strip().upper()
    if allele in ("", "?", "NA", "NAN"):
        return None
    return allele


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _source_rsids(value: object) -> list[str]:
    """Split a row's rsid cell into valid lower-case rsids.

    Parameters
    ----------
    value : `object`
        An rsid cell, e.g. "rs1", "rs1,rs2" (FinnGen), NA or `None`.

    Returns
    -------
    rsids : `list[str]`
        Unique `rs<digits>` ids in cell order; empty if none.
    """
    if value is None or pd.isna(value):
        return []
    parts = _RSID_SPLIT_PATTERN.split(str(value).strip().lower())
    return list(dict.fromkeys(p for p in parts if _RSID_PATTERN.match(p)))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _trim_anchor_base(
    effect: str | None, other: str | None
) -> tuple[str, str] | None:
    """Drop a VCF-style shared first base from an indel's alleles.

    Ensembl places e.g. VCF `pos CT/C` at `pos + 1` as `T/-`.

    Parameters
    ----------
    effect : `str` or `NoneType`
        Effect allele.
    other : `str` or `NoneType`
        Other allele.

    Returns
    -------
    trimmed : `tuple[str, str]` or `NoneType`
        `(effect, other)` without the shared base (`"-"` when empty), or
        `None` when not an anchored indel (to look up at `pos + 1`).
    """
    if effect is None or other is None or "-" in (effect, other):
        return None
    if effect[0] != other[0] or max(len(effect), len(other)) < 2:
        return None
    return effect[1:] or "-", other[1:] or "-"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _orientation(
    effect: str | None,
    other: str | None,
    ref: str,
    alts: tuple[str, ...],
) -> tuple[str | None, str | None]:
    """Compare row alleles with an Ensembl ref/alts, without strand flips.

    Parameters
    ----------
    effect : `str` or `NoneType`
        Effect allele (`None` if unknown).
    other : `str` or `NoneType`
        Other allele (`None` if unknown); at least one of the two is set.
    ref : `str`
        Ensembl ref allele.
    alts : `tuple[str, ...]`
        Ensembl alt alleles.

    Returns
    -------
    status_alt : `tuple[str | None, str | None]`
        (`EnsemblAlleleCheck.MATCH` or `FLIPPED`, or `None` if the
        alleles do not fit) and the row's alt allele when it identifies
        one, else `None`.
    """
    if effect is not None and other is not None:
        if other == ref and effect in alts:
            return EnsemblAlleleCheck.MATCH, effect
        if effect == ref and other in alts:
            return EnsemblAlleleCheck.FLIPPED, other
        return None, None
    if effect is not None:
        if effect in alts:
            return EnsemblAlleleCheck.MATCH, effect
        if effect == ref:
            return EnsemblAlleleCheck.FLIPPED, None
        return None, None
    if other == ref:
        return EnsemblAlleleCheck.MATCH, None
    if other in alts:
        return EnsemblAlleleCheck.FLIPPED, other
    return None, None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _allele_status(
    effect: str | None, other: str | None, alleles: tuple[str, ...]
) -> tuple[str, str | None]:
    """Classify row alleles against one Ensembl variant's alleles.

    Parameters
    ----------
    effect : `str` or `NoneType`
        Effect allele (`None` if unknown).
    other : `str` or `NoneType`
        Other allele (`None` if unknown).
    alleles : `tuple[str, ...]`
        Ensembl alleles, ref first.

    Returns
    -------
    status_alt : `tuple[str, str | None]`
        An `EnsemblAlleleCheck` value (never `NOT_FOUND`) and the Ensembl
        alt the row points to, on the forward strand (`None` if none).
    """
    if effect is None and other is None:
        return EnsemblAlleleCheck.EFFECT_UNKNOWN, None
    ref, alts = alleles[0], alleles[1:]
    status, alt = _orientation(effect, other, ref, alts)
    if status is not None:
        return status, alt
    status, alt = _orientation(
        _complement(effect), _complement(other), ref, alts
    )
    if status is not None:
        return EnsemblAlleleCheck.STRAND_FLIP, alt
    return EnsemblAlleleCheck.MISMATCH, None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _ensembl_check(
    chrom: object,
    pos: object,
    effect_allele: object,
    other_allele: object,
    rsid: object,
    by_position: Mapping[tuple[str, int], list[EnsemblVariant]],
    by_rsid: Mapping[str, list[EnsemblVariant]],
    lookup_rsid: Callable[[str], list[EnsemblVariant]],
) -> tuple[object, str, object]:
    """Match one variant row to Ensembl and classify alleles and rsid.

    Candidates are the Ensembl variants at `chrom:pos` (plus `pos + 1`
    for VCF-anchored indels). Only when there are none, the row's rsids
    are looked up: first in the region variants, then via
    `lookup_rsid` (Ensembl variation endpoint). The best candidate has
    the best `_ALLELE_CHECK_RANK`, then the row's own rsid.

    Parameters
    ----------
    chrom : `object`
        Row chromosome.
    pos : `object`
        Row GRCh38 position.
    effect_allele : `object`
        Row effect allele (may be NA).
    other_allele : `object`
        Row other allele (may be NA).
    rsid : `object`
        Row rsid cell (may be NA or hold several ids).
    by_position : `Mapping[tuple[str, int], list[EnsemblVariant]]`
        Region variants by `(chrom, start)`.
    by_rsid : `Mapping[str, list[EnsemblVariant]]`
        Region variants by rsid.
    lookup_rsid : `Callable[[str], list[EnsemblVariant]]`
        Fallback rsid lookup for rsids not among the region variants.

    Returns
    -------
    result : `tuple[object, str, object]`
        `(ensembl_variant_id, ensembl_allele_check, ensembl_rsid_check)`;
        `(NA, "not_found", NA)` if nothing matches.
    """
    effect = _clean_allele(effect_allele)
    other = _clean_allele(other_allele)
    source_rsids = _source_rsids(rsid)
    trimmed = _trim_anchor_base(effect, other)
    chrom, pos = str(chrom), int(pos)

    candidates = [
        (v, effect, other) for v in by_position.get((chrom, pos), [])
    ]
    if trimmed is not None:
        candidates += [
            (v, *trimmed) for v in by_position.get((chrom, pos + 1), [])
        ]
    rsid_only = False
    if not candidates:
        variants = []
        for source_rsid in source_rsids:
            variants += by_rsid.get(source_rsid) or lookup_rsid(source_rsid)
        candidates = [(v, effect, other) for v in variants]
        if trimmed is not None:
            candidates += [(v, *trimmed) for v in variants]
        rsid_only = True
    if not candidates:
        return pd.NA, EnsemblAlleleCheck.NOT_FOUND, pd.NA

    scored = []
    for variant, row_effect, row_other in candidates:
        status, alt = _allele_status(row_effect, row_other, variant.alleles)
        scored.append((variant, status, alt))
    variant, status, alt = min(
        scored,
        key=lambda item: (
            _ALLELE_CHECK_RANK[item[1]],
            item[0].rsid not in source_rsids,
        ),
    )
    alt_text = alt if alt is not None else "/".join(variant.alleles[1:])
    variant_id = (
        f"{variant.chrom}:{variant.start}:{variant.alleles[0]}:{alt_text}"
    )
    if rsid_only:
        rsid_check = EnsemblRsidCheck.RSID_ONLY
    elif variant.rsid in source_rsids:
        rsid_check = EnsemblRsidCheck.SAME
    elif source_rsids:
        rsid_check = EnsemblRsidCheck.DIFFERENT
    else:
        rsid_check = EnsemblRsidCheck.NO_SOURCE_RSID
    return variant_id, status, rsid_check


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def annotate_ensembl_variants(
    df: pd.DataFrame, regions: Mapping[str, GeneRegion]
) -> pd.DataFrame:
    """Check every variant row against Ensembl (GRCh38).

    Sets `ensembl_variant_id`, `ensembl_allele_check` and
    `ensembl_rsid_check` (see `HarmonisedColumns`) for rows with a
    chromosome and position; gene-level rows (gene burden) stay NA.
    Each unique (chrom, pos, alleles, rsid) combination is checked once,
    since rows repeat per outcome.

    Parameters
    ----------
    df : `pd.DataFrame`
        Combined harmonised rows (`HarmonisedColumns.CORE_ORDER`
        columns). Modified in place (no copy of the ~600k-row table).
    regions : `Mapping[str, GeneRegion]`
        Gene -> flanked region; Ensembl variants are fetched for these.

    Returns
    -------
    df : `pd.DataFrame`
        The same frame, with the three Ensembl columns filled.

    Raises
    ------
    ReaderError
        If an Ensembl request fails (cached windows are kept for reruns).
    """
    hc = HarmonisedColumns
    by_position: dict[tuple[str, int], list[EnsemblVariant]] = {}
    by_rsid: dict[str, list[EnsemblVariant]] = {}
    seen: set[tuple[str, int]] = set()
    for gene, region in regions.items():
        variants, n_fetched = fetch_ensembl_region_variants(region)
        log_info(
            f"{gene}: {len(variants)} Ensembl variants in "
            f"{region.chrom}:{region.start}-{region.end} "
            f"({n_fetched} windows fetched, rest cached)"
        )
        for variant in variants:
            if (variant.rsid, variant.start) in seen:
                continue
            seen.add((variant.rsid, variant.start))
            by_position.setdefault(
                (variant.chrom, variant.start), []
            ).append(variant)
            by_rsid.setdefault(variant.rsid.lower(), []).append(variant)

    n_rsid_fetched = 0

    def lookup_rsid(rsid: str) -> list[EnsemblVariant]:
        """Look up an rsid via Ensembl, counting uncached requests.

        Parameters
        ----------
        rsid : `str`
            Lower-case rsid.

        Returns
        -------
        variants : `list[EnsemblVariant]`
            See `_ensembl_rsid_variants`.
        """
        nonlocal n_rsid_fetched
        variants, fetched = _ensembl_rsid_variants(rsid)
        n_rsid_fetched += int(fetched)
        return variants

    has_site = df[hc.CHROM].notna() & df[hc.POS].notna()
    key_columns = [
        hc.CHROM,
        hc.POS,
        hc.EFFECT_ALLELE,
        hc.OTHER_ALLELE,
        hc.RSID,
    ]
    sites = df.loc[has_site, key_columns].astype(object)
    sites = sites.where(sites.notna(), None)
    keys = list(sites.itertuples(index=False, name=None))
    results = {
        key: _ensembl_check(*key, by_position, by_rsid, lookup_rsid)
        for key in dict.fromkeys(keys)
    }
    log_info(
        f"Ensembl check: {len(results)} unique variant rows checked, "
        f"{n_rsid_fetched} rsids fetched via the variation endpoint"
    )
    site_index = df.index[has_site]
    for position, column in enumerate(
        (hc.ENSEMBL_VARIANT_ID, hc.ENSEMBL_ALLELE_CHECK, hc.ENSEMBL_RSID_CHECK)
    ):
        df[column] = pd.Series(pd.NA, index=df.index, dtype=object)
        df.loc[site_index, column] = [results[key][position] for key in keys]

    checked = df.loc[has_site]
    for source, group in checked.groupby(hc.SOURCE, sort=False):
        alleles = group[hc.ENSEMBL_ALLELE_CHECK].value_counts()
        rsids = group[hc.ENSEMBL_RSID_CHECK].value_counts()
        log_info(
            f"{source} rows: alleles "
            + " ".join(f"{k}={n}" for k, n in alleles.items())
            + "; rsid "
            + " ".join(f"{k}={n}" for k, n in rsids.items())
        )
    bad = checked[hc.ENSEMBL_ALLELE_CHECK].isin(
        [EnsemblAlleleCheck.NOT_FOUND, EnsemblAlleleCheck.MISMATCH]
    )
    per_study = bad.groupby(
        [checked[hc.SOURCE], checked[hc.STUDY_ACCESSION]]
    ).agg(["mean", "size"])
    for (source, study), row in per_study.iterrows():
        if (
            row["size"] >= Constants.ENSEMBL_BAD_MIN_ROWS
            and row["mean"] > Constants.ENSEMBL_BAD_FRACTION_WARN
        ):
            log_warn(
                f"{source} {study}: {row['mean']:.0%} of {int(row['size'])} "
                "rows not_found/mismatch in Ensembl (GRCh37 file?)"
            )
    return df
