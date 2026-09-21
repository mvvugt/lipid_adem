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

from log_tools.emitter import log_info
from log_tools.setup import runlog_setup

import functions
from project_constants import Constants


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def study_tabix_path(study_accession: str) -> str:
    """Build the harmonised-summary-stats tabix URL for a study.

    Parameters
    ----------
    study_accession : `str`
        GWAS Catalog study accession (e.g. "GCST######").

    Returns
    -------
    url : `str`
        URL of the study's bgzip-compressed, tabix-indexed harmonised
        summary statistics file.

    Raises
    ------
    ValueError
        If the study has no full summary statistics available on GWAS
        Catalog.
    """
    location = functions.study_summary_stats_location(study_accession)
    if location is None:
        raise ValueError(
            f"{study_accession} has no full summary statistics available "
            "on GWAS Catalog (full_summary_stats_available=False)"
        )
    return f"{location}/harmonised/{study_accession}.h.tsv.gz"


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
    """
    region = functions.GeneRegion(chrom=chrom, start=start, end=end)
    tabix_source = study_tabix_path(study_accession)

    filtered = functions.filter_sumstats_region(
        tabix_source=tabix_source,
        region=region,
        maf_col="effect_allele_frequency",
        maf_threshold=Constants.MAF_THRESHOLD,
    )
    filtered.insert(0, "study_accession", study_accession)
    filtered.insert(0, "gene", gene)

    outfile.parent.mkdir(parents=True, exist_ok=True)
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

    with runlog_setup():
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
