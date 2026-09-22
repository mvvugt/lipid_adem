#!/usr/bin/env python3
"""
Runs once per row of the pyjasub job-array file (data/temp/tasks.tsv).
Remote-tabix-queries one gene x study pair's GWAS Catalog harmonised summary
stats, filters to MAF < Constants.MAF_THRESHOLD, and writes the row's output
file.
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
        GWAS Catalog study accession.

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
    pd.DataFrame(columns=["gene", "study_accession"]).to_csv(
        outfile, sep="\t", index=False
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_filter(
    gene: str,
    study_accession: str,
    chrom: str,
    start: int,
    end: int,
    outfile: Path,
) -> None:
    """Filter one gene x study pair's sumstats and write the result.

    Parameters
    ----------
    gene : `str`
        HGNC gene symbol (for logging/traceability only).
    study_accession : `str`
        GWAS Catalog study accession.
    chrom : `str`
        Chromosome of the (already-flanked) gene region.
    start : `int`
        Region start.
    end : `int`
        Region end.
    outfile : `Path`
        Path to write the filtered TSV to.

    Returns
    -------
    `None`

    Notes
    -----
    If the study has no full summary statistics available, or its
    available statistics can't be resolved to a usable file (ambiguous/
    missing raw file, unexpected column layout), a header-only (0-row)
    result is written instead of raising, so the pyjasub job-array row
    is marked done and never retried. Transient failures (network
    errors, a `.tbi`-missing `OSError` on the tabix path) are not
    caught here and still propagate, so pyjasub retries those.
    """
    region = functions.GeneRegion(chrom=chrom, start=start, end=end)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    location = functions.study_summary_stats_location(study_accession)
    if location is None:
        log_warn(
            f"{study_accession} has no full summary statistics available "
            f"on GWAS Catalog; writing empty result for {gene}"
        )
        _write_empty_result(outfile, gene, study_accession)
        return

    try:
        source_url, is_indexed = functions.resolve_sumstats_source(
            location, study_accession
        )
    except ValueError as exc:
        log_warn(f"{exc}; writing empty result for {gene}")
        _write_empty_result(outfile, gene, study_accession)
        return

    if is_indexed:
        filtered = functions.filter_sumstats_region(
            tabix_source=source_url,
            region=region,
            maf_col="effect_allele_frequency",
            maf_threshold=Constants.MAF_THRESHOLD,
        )
    else:
        try:
            filtered = functions.filter_raw_sumstats_region(
                url=source_url,
                region=region,
                maf_col="effect_allele_frequency",
                maf_threshold=Constants.MAF_THRESHOLD,
            )
        except ValueError as exc:
            log_warn(f"{exc}; writing empty result for {gene}")
            _write_empty_result(outfile, gene, study_accession)
            return

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
        )


if __name__ == "__main__":
    main()
