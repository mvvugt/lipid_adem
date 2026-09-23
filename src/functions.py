#!/usr/bin/env python3
"""
lipid_adem helper functions
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import gzip
import io
import re
import time
import warnings
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests
from biomed_api.errors import ReaderError
from biomed_api.readers.reader_ensembl import EnsemblReader
from biomed_api.readers.reader_gwascat import GwasCatalogReader
from biomed_api.readers.reader_uniprot import UniProtIdMappingReader
from log_tools.emitter import log_debug, log_info, log_warn, log_stage

from project_constants import ColumnNames, Constants, FileNames


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


class GeneTableError(ValueError):
    """A gene-table row cannot be resolved or its identifiers disagree."""


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
        Destination path.
    sep : `str`, optional, default: `"\\t"`
        Field separator.

    Returns
    -------
    `None`
    """
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    df.to_csv(tmp_path, sep=sep, index=False)
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
def load_task_outfiles(path: Path) -> list[Path]:
    """Load the unique `outfile` paths from the job-array file.

    Parameters
    ----------
    path : `Path`
        The job-array file (`tasks.tsv`) written by `gwas_cat_prep.py`.

    Returns
    -------
    outfiles : `list[Path]`
        Unique `outfile` paths, in file order.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Tasks file not found: {path}")
    tasks = pd.read_csv(path, sep="\t", dtype=str)
    return [Path(p) for p in tasks[ColumnNames.OUTFILE].dropna().unique()]


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
        log_stage('resolve_genes')
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

    log_stage('resolve_efo')
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
def _fetch_gwas_catalog_study_records(efo_id: str) -> list[dict]:
    """Fetch raw GWAS Catalog study records for an EFO trait.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form, e.g. "EFO_0001645").

    Returns
    -------
    records : `list[dict]`
        One dict per study with `accession_id`,
        `full_summary_stats_available`, `pubmed_id`, `disease_trait`,
        `initial_sample_size`, `discovery_ancestry`, and `cohort`, as
        returned by the GWAS Catalog studies-list search (absent fields
        are `None`).
    """
    reader = GwasCatalogReader()
    with warnings.catch_warnings():
        # biomed-api warns (rather than raising) on zero matches; an
        # empty accession list is a normal outcome for callers here.
        warnings.simplefilter("ignore", UserWarning)
        result = reader.read(profile="studies", efo_id=efo_id)

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
        }
        for row in result.records
        if "accession_id" in row
    ]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def discover_studies(
    efo_id: str, cap: int = Constants.MAX_STUDIES_PER_OUTCOME
) -> list[str]:
    """Discover GWAS Catalog study accessions for an EFO trait.

    Well-studied traits (e.g. common diseases, lipid biomarkers) can have
    hundreds of associated studies; only those with full summary
    statistics available are usable downstream, and pulling all of them
    is expensive (a sumstats download and filter per gene). Results are
    therefore filtered to studies with full summary statistics available
    and capped to the `cap` most recently published, via
    `filter_and_cap_studies`.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form, e.g. "EFO_0001645").
    cap : `int`, optional, default: `Constants.MAX_STUDIES_PER_OUTCOME`
        Maximum number of studies to keep, most recent first.

    Returns
    -------
    accessions : `list[str]`
        Study accession IDs (e.g. "GCST######"), filtered and capped.
    """
    classified = discover_studies_with_reasons(efo_id, cap=cap)
    return [r["accession_id"] for r in classified if r["reason"] == "included"]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def discover_studies_with_reasons(
    efo_id: str, cap: int = Constants.MAX_STUDIES_PER_OUTCOME
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
        first.

    Returns
    -------
    classified : `list[dict]`
        As returned by `classify_studies` -- `accession_id`, `pubmed_id`,
        `reason`, plus publication/trait/sample metadata.
    """
    log_stage('discover_gwas')
    records = _fetch_gwas_catalog_study_records(efo_id)
    log_info(f"{efo_id} -> {len(records)} studies")
    return classify_studies(records, cap=cap)


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
def classify_studies(
    records: list[dict], cap: int = Constants.MAX_STUDIES_PER_OUTCOME
) -> list[dict]:
    """Classify candidate GWAS Catalog studies as included or excluded.

    Same eligibility filter (full summary stats available) and recency
    cap as `filter_and_cap_studies`, but returns every input record
    annotated with the reason it was kept or dropped, rather than only
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

    Returns
    -------
    classified : `list[dict]`
        One dict per input record, each with `accession_id`, `pubmed_id`,
        `reason`, plus display-only metadata (all `str`, `""` if
        unknown): `pub_date` (YYYY-MM-DD), `first_author`, `journal`,
        `title` (from PubMed), and `trait`, `sample_size`, `ancestry`,
        `cohort` (from the GWAS Catalog record). `reason` is one of
        `"included"`, `"over_cap"` (eligible but
        beyond `cap`), or `"no_full_sumstats"`. `"included"` and
        `"over_cap"` records appear first, most-recent-publication-date
        first (unresolved dates sort last), followed by
        `"no_full_sumstats"` records in their original input order.
    """
    eligible = [r for r in records if r.get("full_summary_stats_available")]
    ineligible = [
        r for r in records if not r.get("full_summary_stats_available")
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

    def _row(record: dict, reason: str) -> dict:
        summary = _summary(record)
        date = summary.get("date")
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
        }

    classified = (
        [_row(r, "included") for r in eligible[:cap]]
        + [_row(r, "over_cap") for r in eligible[cap:]]
        + [_row(r, "no_full_sumstats") for r in ineligible]
    )
    log_info(
        f"{len(records)} studies -> {len(eligible)} with full sumstats "
        f"-> {len(eligible[:cap])} included after cap={cap}"
    )
    return classified


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_and_cap_studies(
    records: list[dict], cap: int = Constants.MAX_STUDIES_PER_OUTCOME
) -> list[str]:
    """Keep studies with full summary stats, capped to the N most recent.

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
def load_finngen_manifest(path: Path = FileNames.FINNGEN_MANIFEST) -> pd.DataFrame:
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
def manual_studies_for_outcome(outcome: str, manual_df: pd.DataFrame) -> list[str]:
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
    return manual_df.loc[manual_df["outcome"] == outcome, "accession_id"].tolist()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def finngen_sumstats_url(phenocode: str, manifest_df: pd.DataFrame) -> str | None:
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
    matches = manifest_df.loc[manifest_df["phenocode"] == phenocode, "path_https"]
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
    response = requests.get(
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
def resolve_sumstats_source(
    location: str, study_accession: str
) -> tuple[str, bool]:
    """Determine the queryable summary-stats URL for a study.

    GWAS Catalog studies with full summary statistics available are not
    all harmonised (bgzip+tabix-indexed) -- some only have a raw,
    author-submitted file at the top level of their FTP directory. This
    checks the study's directory listing to tell the two cases apart.

    Parameters
    ----------
    location : `str`
        The study's summary-stats FTP directory (from
        `study_summary_stats_location`).
    study_accession : `str`
        GWAS Catalog study accession (e.g. "GCST######").

    Returns
    -------
    url : `str`
        URL of the sumstats file to use.
    is_tabix_indexed : `bool`
        `True` if `url` is the harmonised, tabix-indexed file (query via
        `filter_sumstats_region`); `False` if `url` is a raw, non-indexed
        file (query via `filter_raw_sumstats_region`).

    Raises
    ------
    ValueError
        If no `harmonised/` folder exists and the directory listing does
        not contain exactly one identifiable raw data file.
    """
    response = requests.get(f"{location}/", timeout=30)
    response.raise_for_status()
    entries = re.findall(r'href="([^"]+)"', response.text)

    if "harmonised/" in entries:
        return f"{location}/harmonised/{study_accession}.h.tsv.gz", True

    exclude = {"README.txt", "md5sum.txt"}
    candidates = [
        entry
        for entry in entries
        if not entry.endswith("/")
        and not entry.startswith("?")
        and entry not in exclude
        and not entry.endswith("-meta.yaml")
    ]
    if len(candidates) != 1:
        raise ValueError(
            f"{study_accession}: could not identify a single raw sumstats "
            f"file in {location} (candidates: {candidates})"
        )
    return f"{location}/{candidates[0]}", False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fetch_curated_associations(efo_id: str) -> list[dict]:
    """Fetch all curated genome-wide-significant associations for a trait.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form).

    Returns
    -------
    records : `list[dict]`
        Every association record for `efo_id`, unfiltered. The download
        does not depend on any gene, so fetch once per EFO ID and filter
        per gene with `filter_curated_associations`.

    Notes
    -----
    Sourced via biomed-api's `GwasCatalogReader` (GWAS Catalog REST v2).
    """
    reader = GwasCatalogReader()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        result = reader.read(profile="associations", efo_id=efo_id)

    records = list(result.records)
    log_info(f"{efo_id} -> {len(records)} curated associations fetched")
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
        Curated associations, region- and MAF-filtered. Empty if none.
    """
    kept = []
    for row in records:
        if not _location_in_region(row.get("locations"), region):
            continue
        if _maf_at_or_above_threshold(row.get("risk_frequency"), maf_threshold):
            continue
        kept.append(row)
    return pd.DataFrame.from_records(kept)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _location_in_region(locations: list[str] | None, region: GeneRegion) -> bool:
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
    for location in locations or []:
        chrom, _, pos = str(location).partition(":")
        if chrom != region.chrom or not pos.isdigit():
            continue
        if region.start <= int(pos) <= region.end:
            return True
    return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _maf_at_or_above_threshold(maf: str | None, maf_threshold: float) -> bool:
    """Check whether a GWAS Catalog v2 `risk_frequency` clears `maf_threshold`.

    Parameters
    ----------
    maf : `str` or `NoneType`
        Value of an association record's `risk_frequency` field. Not
        always numeric (e.g. blank or "NR").
    maf_threshold : `float`
        Threshold to compare against.

    Returns
    -------
    `bool`
        `True` only if `maf` parses to a float that is `>= maf_threshold`.
        Missing or unparseable values are treated as not excluding the
        record.
    """
    if maf is None:
        return False
    try:
        return float(maf) >= maf_threshold
    except ValueError:
        return False


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
    return line.rstrip("\n").split("\t")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_sumstats_region(
    tabix_source: str,
    region: GeneRegion,
    maf_col: str,
    maf_threshold: float,
    chrom_col: str = "chromosome",
    pos_col: str = "base_pair_location",
    transform_to_maf: bool = False,
) -> pd.DataFrame:
    """Filter a tabix-indexed sumstats file to one region and a MAF cutoff.

    Based on GWAS catalog downloads, but should work on any
    bgzip+tabix-indexed sumstats file.

    Parameters
    ----------
    tabix_source : `str`
        Path or URL to a bgzip+tabix-indexed sumstats file.
    region : `GeneRegion`
        Region to query.
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
        Rows in `region` with MAF < `maf_threshold`.

    Raises
    ------
    OSError
        If `tabix_source` has no `.tbi` index (no remote-tabix fallback is
        implemented here -- see gwas_cat.md's caveat on falling back to a
        full-file download).
    """
    import pysam

    with pysam.TabixFile(tabix_source) as tabix_file:
        header_lines = tabix_file.header
        header = (
            header_lines[0].lstrip("#").split("\t")
            if header_lines
            else _plain_header(tabix_source)
        )
        chrom_idx = header.index(chrom_col)
        pos_idx = header.index(pos_col)
        maf_idx = header.index(maf_col)
        log_debug(f"header columns: chrom={chrom_idx} pos={pos_idx} maf={maf_idx}")

        records = []
        for line in tabix_file.fetch(region.chrom, region.start, region.end):
            fields = line.split("\t")
            maf = float(fields[maf_idx])
            if transform_to_maf:
                maf = min(maf, 1.0 - maf)
            if maf < maf_threshold:
                records.append(fields)

    log_info(
        f"{tabix_source} @ {region.chrom}:{region.start}-{region.end} -> "
        f"{len(records)} rows with MAF < {maf_threshold}"
    )
    return pd.DataFrame.from_records(records, columns=header)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_raw_sumstats_region(
    url: str,
    region: GeneRegion,
    maf_col: str,
    maf_threshold: float,
    chrom_col: str = "chromosome",
    pos_col: str = "base_pair_location",
    transform_to_maf: bool = False,
) -> pd.DataFrame:
    """Stream-filter a non-indexed sumstats file to one region and MAF cutoff.

    No tabix index is available for raw (non-harmonised) sumstats files,
    so the file is scanned sequentially via HTTP streaming, decompressed
    on the fly if gzip-compressed; only matching rows are held in memory.
    Rows are not assumed sorted, so the full file is always scanned.

    Parameters
    ----------
    url : `str`
        URL of the raw (non-tabix-indexed) sumstats file.
    region : `GeneRegion`
        Region to filter to.
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
        Rows in `region` with MAF < `maf_threshold`.

    Raises
    ------
    ValueError
        If `chrom_col`, `pos_col`, or `maf_col` are not in the file's
        header.
    """
    with requests.get(url, stream=True, timeout=60) as response:
        response.raise_for_status()
        raw_stream = response.raw
        if url.endswith(".gz"):
            raw_stream = gzip.GzipFile(fileobj=raw_stream)
        text_stream = io.TextIOWrapper(raw_stream, encoding="utf-8")

        header = next(text_stream).rstrip("\n").split("\t")
        chrom_idx = header.index(chrom_col)
        pos_idx = header.index(pos_col)
        maf_idx = header.index(maf_col)
        log_debug(f"header columns: chrom={chrom_idx} pos={pos_idx} maf={maf_idx}")

        records = []
        for line in text_stream:
            fields = line.rstrip("\n").split("\t")
            if fields[chrom_idx] != region.chrom:
                continue
            pos = fields[pos_idx]
            if not pos.isdigit() or not (region.start <= int(pos) <= region.end):
                continue
            maf = float(fields[maf_idx])
            if transform_to_maf:
                maf = min(maf, 1.0 - maf)
            if maf < maf_threshold:
                records.append(fields)

    log_info(
        f"{url} @ {region.chrom}:{region.start}-{region.end} -> "
        f"{len(records)} rows with MAF < {maf_threshold} (raw scan)"
    )
    return pd.DataFrame.from_records(records, columns=header)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_burden_evidence(gene: str) -> pd.DataFrame:
    """Fetch gene-based rare-variant burden evidence from Open Targets.

    Parameters
    ----------
    gene : `str`
        HGNC gene symbol.

    Returns
    -------
    evidence : `pd.DataFrame`
        Evidence rows where `datasourceId == "gene_burden"`. Empty if none.
    """
    query = """
    query GeneBurdenEvidence($geneSymbol: String!) {
      search(queryString: $geneSymbol, entityNames: ["target"]) {
        hits {
          id
          object {
            ... on Target {
              associatedDiseases {
                rows {
                  disease { id name }
                  datasourceScores { id score }
                }
              }
            }
          }
        }
      }
    }
    """
    response = requests.post(
        Constants.OPEN_TARGETS_GRAPHQL_URL,
        json={"query": query, "variables": {"geneSymbol": gene}},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()

    records = []
    for hit in payload.get("data", {}).get("search", {}).get("hits", []):
        rows = (
            hit.get("object", {})
            .get("associatedDiseases", {})
            .get("rows", [])
        )
        for row in rows:
            scores = {s["id"]: s["score"] for s in row.get("datasourceScores", [])}
            if "gene_burden" in scores:
                records.append(
                    {
                        "gene": gene,
                        "disease_id": row["disease"]["id"],
                        "disease_name": row["disease"]["name"],
                        "gene_burden_score": scores["gene_burden"],
                    }
                )

    log_info(f"{gene} -> {len(records)} gene-burden evidence rows")
    return pd.DataFrame.from_records(records)
