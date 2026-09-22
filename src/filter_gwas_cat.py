#!/usr/bin/env python3
"""
Runs once per row of the pyjasub job-array file (data/temp/tasks.tsv).
Remote-tabix-queries one gene x study pair's summary stats (GWAS Catalog
harmonised, or FinnGen, per the row's `source`), filters to
MAF < Constants.MAF_THRESHOLD, and writes the row's output file.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations
import argparse
from pathlib import Path

import pandas as pd

from log_tools.emitter import log_info, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import Constants, Paths


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def _write_empty_result(outfile: Path, gene: str, study_accession: str) -> None:
    """Write a header-only (0-row) result for an unusable study.

    Parameters
    ----------
    outfile : `Path`
        Path to write the empty TSV to.
    gene : `str`
        HGNC gene symbol.
    study_accession : `str`
        GWAS Catalog study accession or FinnGen phenocode.

    Returns
    -------
    `None`

    Notes
    -----
    Deliberately not a 0-byte file: `merge_associations.py`'s
    `pd.read_csv` raises `EmptyDataError` on a truly empty file, but
    parses a header-only file fine as a 0-row frame. Satisfies pyjasub's
    outfile-existence check so the row is never retried.
    """
    pd.DataFrame(columns=["gene", "study_accession", "source_db"]).to_csv(
        outfile, sep="\t", index=False
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _run_filter_gwas_catalog(
    gene: str, study_accession: str, region: functions.GeneRegion, outfile: Path
) -> pd.DataFrame | None:
    """Resolve and filter one gene x study pair from GWAS Catalog.

    Returns
    -------
    filtered : `pd.DataFrame` or `NoneType`
        The filtered sumstats, or `None` if an empty result was already
        written for an unusable study (caller should return without
        further writes).
    """
    location = functions.study_summary_stats_location(study_accession)
    if location is None:
        log_warn(
            f"{study_accession} has no full summary statistics available "
            f"on GWAS Catalog; writing empty result for {gene}"
        )
        _write_empty_result(outfile, gene, study_accession)
        return None

    try:
        source_url, is_indexed = functions.resolve_sumstats_source(
            location, study_accession
        )
    except ValueError as exc:
        log_warn(f"{exc}; writing empty result for {gene}")
        _write_empty_result(outfile, gene, study_accession)
        return None

    if is_indexed:
        return functions.filter_sumstats_region(
            tabix_source=source_url,
            region=region,
            maf_col="effect_allele_frequency",
            maf_threshold=Constants.MAF_THRESHOLD,
        )
    try:
        return functions.filter_raw_sumstats_region(
            url=source_url,
            region=region,
            maf_col="effect_allele_frequency",
            maf_threshold=Constants.MAF_THRESHOLD,
        )
    except ValueError as exc:
        log_warn(f"{exc}; writing empty result for {gene}")
        _write_empty_result(outfile, gene, study_accession)
        return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _run_filter_finngen(
    gene: str, phenocode: str, region: functions.GeneRegion, outfile: Path
) -> pd.DataFrame | None:
    """Resolve and filter one gene x phenocode pair from FinnGen.

    Returns
    -------
    filtered : `pd.DataFrame` or `NoneType`
        The filtered sumstats, or `None` if an empty result was already
        written for an unusable phenocode (caller should return without
        further writes).
    """
    manifest_df = functions.load_finngen_manifest()
    url = functions.finngen_sumstats_url(phenocode, manifest_df)
    if url is None:
        log_warn(
            f"{phenocode} not found in FinnGen manifest; writing empty "
            f"result for {gene}"
        )
        _write_empty_result(outfile, gene, phenocode)
        return None

    return functions.filter_sumstats_region(
        tabix_source=url,
        region=region,
        maf_col="af_alt",
        maf_threshold=Constants.MAF_THRESHOLD,
        chrom_col="chrom",
        pos_col="pos",
        transform_to_maf=True,
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_filter(
    gene: str,
    study_accession: str,
    chrom: str,
    start: int,
    end: int,
    outfile: Path,
    source: str = "gwas_catalog",
) -> None:
    """Filter one gene x study pair's sumstats and write the result.

    Parameters
    ----------
    gene : `str`
        HGNC gene symbol (for logging/traceability only).
    study_accession : `str`
        GWAS Catalog study accession, or FinnGen phenocode if
        `source == "finngen"`.
    chrom : `str`
        Chromosome of the (already-flanked) gene region.
    start : `int`
        Region start.
    end : `int`
        Region end.
    outfile : `Path`
        Path to write the filtered TSV to.
    source : `str`, optional, default: `"gwas_catalog"`
        Which sumstats source `study_accession` refers to: `"gwas_catalog"`
        or `"finngen"`.

    Returns
    -------
    `None`

    Notes
    -----
    If the study/phenocode has no usable summary statistics (not
    available, ambiguous/missing raw file, unexpected column layout, or
    absent from the FinnGen manifest), a header-only (0-row) result is
    written instead of raising, so the pyjasub job-array row is marked
    done and never retried. Transient failures (network errors, a
    `.tbi`-missing `OSError` on the tabix path) are not caught here and
    still propagate, so pyjasub retries those.
    """
    region = functions.GeneRegion(chrom=chrom, start=start, end=end)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    if source == "finngen":
        filtered = _run_filter_finngen(gene, study_accession, region, outfile)
    else:
        filtered = _run_filter_gwas_catalog(gene, study_accession, region, outfile)
    if filtered is None:
        return

    filtered.insert(0, "source_db", source)
    filtered.insert(0, "study_accession", study_accession)
    filtered.insert(0, "gene", gene)

    filtered.to_csv(outfile, sep="\t", index=False)
    log_info(f"{gene} x {study_accession}: {len(filtered)} rows -> {outfile}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Filter: one gene x study pair's sumstats."
    )
    parser.add_argument("--gene", required=True)
    parser.add_argument("--study-accession", required=True)
    parser.add_argument("--chrom", required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--outfile", type=Path, required=True)
    parser.add_argument(
        "--source", required=True, choices=["gwas_catalog", "finngen"]
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

    with runlog_setup(root=Paths.HERE):
        run_filter(
            gene=args.gene,
            study_accession=args.study_accession,
            chrom=args.chrom,
            start=args.start,
            end=args.end,
            outfile=args.outfile,
            source=args.source,
        )


if __name__ == "__main__":
    main()
