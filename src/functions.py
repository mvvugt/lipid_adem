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
import warnings
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests
from biomed_api.readers.reader_ensembl import EnsemblReader
from biomed_api.readers.reader_gwascat import GwasCatalogReader
from log_tools.emitter import log_debug, log_info, log_warn

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
def load_gene_table(path: Path) -> pd.DataFrame:
    """Load the gene reference table.

    Parameters
    ----------
    path : `Path`
        Tab-separated file with (at least) `gene`, `chr`, `start`, `end`
        columns. `chr`/`start`/`end` may be blank for a gene not yet
        resolved.

    Returns
    -------
    genes : `pd.DataFrame`
        The gene table, as-is.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Gene list not found: {path}")
    return pd.read_csv(path, sep="\t", dtype=str).fillna("")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def resolve_gene_regions(df: pd.DataFrame) -> pd.DataFrame:
    """Fill in blank gene coordinates via Ensembl, in place.

    Rows that already have `chr`/`start`/`end` are left untouched -- only
    blank rows trigger an Ensembl lookup, so `gene_list.txt` doubles as a
    persisted cache across reruns.

    Parameters
    ----------
    df : `pd.DataFrame`
        Gene table (as returned by `load_gene_table`).

    Returns
    -------
    df : `pd.DataFrame`
        The same table, with blank coordinate cells filled in.
    """
    mask = df[ColumnNames.GENE_CHR].str.strip() == ""
    for idx in df.index[mask]:
        gene = df.at[idx, ColumnNames.GENE]
        region = gene_coordinates(gene)
        df.at[idx, ColumnNames.GENE_CHR] = region.chrom
        df.at[idx, ColumnNames.START] = str(region.start)
        df.at[idx, ColumnNames.END] = str(region.end)
    return df


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
        columns. Adds an empty `efo_id` column if the file doesn't have
        one yet (one-time migration).

    Returns
    -------
    icd_codes : `pd.DataFrame`
        The ICD-code table, with `efo_id` guaranteed present.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"ICD code list not found: {path}")
    df = pd.read_csv(path, dtype=str).fillna("")
    if ColumnNames.EFO_ID not in df.columns:
        df[ColumnNames.EFO_ID] = ""
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
    once. Rows that already have an `efo_id` are left untouched, so
    `icd_codes.txt` doubles as a persisted cache across reruns.

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
def icd_to_efo(term: str) -> str:
    """Map an ICD code or trait/description string to an EFO ID.

    Parameters
    ----------
    term : `str`
        ICD code or free-text trait/description.

    Returns
    -------
    efo_id : `str`
        The first matching EFO term's short OBO ID (e.g. "EFO_0001645").
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
        return "NA"

    obo_id = docs[0].get("obo_id")
    if not obo_id:
        log_warn(f"EFO match for {term!r} has no obo_id: {docs[0]}")
    log_info(f"mapped {term} -> {obo_id}")
    return obo_id.replace(":", "_")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gene_coordinates(symbol: str) -> GeneRegion:
    """Look up a gene's coordinates via Ensembl.

    Parameters
    ----------
    symbol : `str`
        HGNC gene symbol.

    Returns
    -------
    region : `GeneRegion`
        The gene's (unflanked) region. Use `gene_row_region` /
        equivalent flanking at the point of use.

    Raises
    ------
    biomed_api.readers.utils.base.ReaderError
        If Ensembl has no record for `symbol`, or the lookup fails.
    """
    reader = EnsemblReader()
    result = reader.read(profile="gene_lookup", symbol=symbol)
    data = result.records[0]

    region = GeneRegion(
        chrom=str(data["seq_region_name"]),
        start=int(data["start"]),
        end=int(data["end"]),
    )
    log_info(f"{symbol} -> {region.chrom}:{region.start}-{region.end}")
    return region


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def discover_studies(
    efo_id: str, cap: int = Constants.MAX_STUDIES_PER_OUTCOME
) -> list[str]:
    """Discover GWAS Catalog study accessions for an EFO trait.

    Well-studied traits (e.g. common diseases, lipid biomarkers) can have
    hundreds of associated studies; only those with full summary
    statistics available are usable downstream, and pulling all of them
    is expensive (one HTTP call per accession, then a sumstats download
    and filter per gene). Results are therefore filtered to studies with
    full summary statistics available and capped to the `cap` most
    recently published, via `filter_and_cap_studies`.

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
    reader = GwasCatalogReader()
    with warnings.catch_warnings():
        # biomed-api warns (rather than raising) on zero matches; an
        # empty accession list is a normal outcome for callers here.
        warnings.simplefilter("ignore", UserWarning)
        result = reader.read(profile="studies", efo_id=efo_id)

    accessions = [
        row["accession_id"] for row in result.records if "accession_id" in row
    ]
    log_info(f"{efo_id} -> {len(accessions)} studies")
    return filter_and_cap_studies(accessions, cap=cap)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_metadata(study_accession: str) -> dict:
    """Fetch a study's raw metadata from the GWAS Catalog v2 API.

    Parameters
    ----------
    study_accession : `str`
        GWAS Catalog study accession (e.g. "GCST######").

    Returns
    -------
    data : `dict`
        Parsed JSON response for the study.

    Raises
    ------
    requests.HTTPError
        If the study accession is not found or the API call fails.
    """
    response = requests.get(
        f"{Constants.GWAS_CATALOG_API_V2}/studies/{study_accession}",
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _publication_date(data: dict) -> str:
    """Extract a study's publication date from its raw metadata.

    Notes
    -----
    The exact field name has not been confirmed against a live API
    response in this environment (sandboxed, no network access to
    ebi.ac.uk) -- `publication_date` and the nested
    `publication_info.publication_date` are both tried since the
    confirmed-working `full_summary_stats_available`/`full_summary_stats`
    fields on this same endpoint use snake_case. Verify this against a
    real response on first live run; if both are wrong, ranking silently
    degrades to input order (empty dates sort last, ties keep discovery
    order) rather than failing.

    Parameters
    ----------
    data : `dict`
        Raw study metadata, as returned by `_study_metadata`.

    Returns
    -------
    date : `str`
        ISO-ish date string, or `""` if not found.
    """
    return (
        data.get("publication_date")
        or data.get("publication_info", {}).get("publication_date", "")
        or ""
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def filter_and_cap_studies(
    accessions: list[str], cap: int = Constants.MAX_STUDIES_PER_OUTCOME
) -> list[str]:
    """Keep studies with full summary stats, capped to the N most recent.

    Parameters
    ----------
    accessions : `list[str]`
        Candidate study accession IDs.
    cap : `int`, optional, default: `Constants.MAX_STUDIES_PER_OUTCOME`
        Maximum number of studies to return, most recent first.

    Returns
    -------
    capped : `list[str]`
        At most `cap` study accessions, all with full summary statistics
        available, ordered most-recent-publication-date first.
    """
    eligible: list[tuple[str, str]] = []
    for accession in accessions:
        data = _study_metadata(accession)
        if not data.get("full_summary_stats_available"):
            continue
        eligible.append((accession, _publication_date(data)))

    eligible.sort(key=lambda item: item[1], reverse=True)
    capped = [accession for accession, _ in eligible[:cap]]
    log_info(
        f"{len(accessions)} studies -> {len(eligible)} with full sumstats "
        f"-> {len(capped)} after cap={cap}"
    )
    return capped


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
        the study has no full summary statistics available.

    Raises
    ------
    requests.HTTPError
        If the study accession is not found or the API call fails.
    """
    response = requests.get(
        f"{Constants.GWAS_CATALOG_API_V2}/studies/{study_accession}",
        timeout=30,
    )
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
def curated_associations(
    efo_id: str, region: GeneRegion, maf_threshold: float
) -> pd.DataFrame:
    """Fetch curated genome-wide-significant associations for a trait.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form).
    region : `GeneRegion`
        Gene region to restrict associations to.
    maf_threshold : `float`
        Only associations with a reported MAF below this are kept.

    Returns
    -------
    associations : `pd.DataFrame`
        Curated associations, region- and MAF-filtered. Empty if none.

    Notes
    -----
    Sourced via biomed-api's `GwasCatalogReader` (GWAS Catalog REST v2).
    """
    reader = GwasCatalogReader()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        result = reader.read(profile="associations", efo_id=efo_id)

    records = []
    for row in result.records:
        if not _location_in_region(row.get("locations"), region):
            continue
        if _maf_at_or_above_threshold(row.get("risk_frequency"), maf_threshold):
            continue
        records.append(row)

    log_info(f"{efo_id} -> {len(records)} curated associations in region")
    return pd.DataFrame.from_records(records)


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
def filter_sumstats_region(
    tabix_source: str,
    region: GeneRegion,
    maf_col: str,
    maf_threshold: float,
    chrom_col: str = "chromosome",
    pos_col: str = "base_pair_location",
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
        Name of the minor-allele-frequency column.
    maf_threshold : `float`
        Only rows with MAF below this are kept.
    chrom_col : `str`, optional, default: `"chromosome"`
        Name of the chromosome column in the file header.
    pos_col : `str`, optional, default: `"base_pair_location"`
        Name of the position column in the file header.

    Returns
    -------
    filtered : `pd.DataFrame`
        Rows in `region` with `maf_col` < `maf_threshold`.

    Raises
    ------
    OSError
        If `tabix_source` has no `.tbi` index (no remote-tabix fallback is
        implemented here -- see gwas_cat.md's caveat on falling back to a
        full-file download).
    """
    import pysam

    with pysam.TabixFile(tabix_source) as tabix_file:
        header = tabix_file.header[0].lstrip("#").split("\t")
        chrom_idx = header.index(chrom_col)
        pos_idx = header.index(pos_col)
        maf_idx = header.index(maf_col)
        log_debug(f"header columns: chrom={chrom_idx} pos={pos_idx} maf={maf_idx}")

        records = []
        for line in tabix_file.fetch(region.chrom, region.start, region.end):
            fields = line.split("\t")
            if float(fields[maf_idx]) < maf_threshold:
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
        Name of the minor-allele-frequency column.
    maf_threshold : `float`
        Only rows with MAF below this are kept.
    chrom_col : `str`, optional, default: `"chromosome"`
        Name of the chromosome column in the file header.
    pos_col : `str`, optional, default: `"base_pair_location"`
        Name of the position column in the file header.

    Returns
    -------
    filtered : `pd.DataFrame`
        Rows in `region` with `maf_col` < `maf_threshold`.

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
            if float(fields[maf_idx]) < maf_threshold:
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
