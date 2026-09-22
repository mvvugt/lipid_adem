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

from project_constants import ColumnNames, Constants


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
def resolve_efo_ids(df: pd.DataFrame) -> pd.DataFrame:
    """Fill in blank `efo_id` cells via the EBI OLS API, in place.

    Search term is `description` when non-blank, else `code`. Identical
    search terms are deduped so a repeated description/code is only
    queried once. Rows that already have an `efo_id` are left untouched,
    so `icd_codes.txt` doubles as a persisted cache across reruns.

    Parameters
    ----------
    df : `pd.DataFrame`
        ICD-code table (as returned by `load_icd_table`).

    Returns
    -------
    df : `pd.DataFrame`
        The same table, with blank `efo_id` cells filled in.
    """
    mask = df[ColumnNames.EFO_ID].str.strip() == ""
    if not mask.any():
        return df

    search_terms = df.loc[mask].apply(
        lambda row: row[ColumnNames.DESCRIPTION].strip()
        or row[ColumnNames.ICD_CODE].strip(),
        axis=1,
    )
    term_to_efo = {term: icd_to_efo(term) for term in search_terms.unique()}
    df.loc[mask, ColumnNames.EFO_ID] = search_terms.map(term_to_efo)
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
def discover_studies(efo_id: str) -> list[str]:
    """Discover GWAS Catalog study accessions for an EFO trait.

    Parameters
    ----------
    efo_id : `str`
        EFO ID (underscore form, e.g. "EFO_0001645").

    Returns
    -------
    accessions : `list[str]`
        Study accession IDs (e.g. "GCST######").
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
    return accessions


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
