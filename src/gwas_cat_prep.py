#!/usr/bin/env python3
"""
Resolves gene coordinates and outcome-to-EFO mappings (persisting any new
lookups back to data/raw/gene_list.txt and data/raw/icd_codes.txt),
discovers GWAS Catalog studies per outcome, and writes the pyjasub
job-array file that src/filter_gwas_cat.sh consumes.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations
import argparse

from log_tools.emitter import log_info
from log_tools.setup import runlog_setup

import functions
from project_constants import ColumnNames, Constants, FileNames, Paths


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def build_tasks() -> None:
    """Resolve lookups, discover studies, and write the job-array file.

    Loads `FileNames.GENE_LIST`/`ICD_CODE_LIST`, fills in any blank gene
    coordinates and outcome/code-to-EFO mappings (persisting the results
    back to those files so reruns skip already-resolved rows), discovers
    GWAS Catalog studies per outcome (grouped by the distinct EFO IDs
    under that outcome), and writes `FileNames.TASKS_FILE` with columns:
    rowidx, gene, study_accession, efo_id, outcome, chrom, start, end,
    outfile.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If the gene or ICD/outcome placeholder files have not been filled
        in.
    """
    genes_df = functions.load_gene_table(FileNames.GENE_LIST)
    icd_df = functions.load_icd_table(FileNames.ICD_CODE_LIST)
    log_info(f"{len(genes_df)} genes, {len(icd_df)} icd codes")

    genes_before = genes_df.copy()
    genes_df = functions.resolve_gene_regions(genes_df)
    if not genes_df.equals(genes_before):
        functions.write_table_atomic(genes_df, FileNames.GENE_LIST)
        log_info(f"wrote resolved gene coordinates to {FileNames.GENE_LIST}")

    icd_before = icd_df.copy()
    icd_df = functions.resolve_efo_ids(icd_df)
    if not icd_df.equals(icd_before):
        functions.write_table_atomic(icd_df, FileNames.ICD_CODE_LIST, sep=",")
        log_info(f"wrote resolved efo_ids to {FileNames.ICD_CODE_LIST}")

    Paths.DATA_TEMP.mkdir(parents=True, exist_ok=True)

    # Discover studies once per distinct efo_id (global dedupe), then
    # union each outcome's accessions from its own distinct efo_ids.
    distinct_efo_ids = sorted(
        {efo_id for efo_id in icd_df[ColumnNames.EFO_ID] if efo_id}
    )
    studies_by_efo = {
        efo_id: functions.discover_studies(efo_id) for efo_id in distinct_efo_ids
    }

    rows: list[dict[str, str]] = []
    for outcome, group in icd_df.groupby(ColumnNames.OUTCOME):
        outcome_efo_ids = sorted({e for e in group[ColumnNames.EFO_ID] if e})
        accession_to_efo: dict[str, str] = {}
        for efo_id in outcome_efo_ids:
            for accession in studies_by_efo[efo_id]:
                accession_to_efo.setdefault(accession, efo_id)

        for _, gene_row in genes_df.iterrows():
            gene = gene_row[ColumnNames.GENE]
            region = functions.gene_row_region(
                gene_row, Constants.GENE_COORD_FLANK_BP
            )
            for accession, efo_id in accession_to_efo.items():
                outfile = Paths.DATA_TEMP / f"{gene}_{accession}_result.tsv"
                rows.append(
                    {
                        ColumnNames.GENE: gene,
                        ColumnNames.STUDY_ACCESSION: accession,
                        ColumnNames.EFO_ID: efo_id,
                        ColumnNames.OUTCOME: outcome,
                        ColumnNames.CHROM: region.chrom,
                        ColumnNames.START: str(region.start),
                        ColumnNames.END: str(region.end),
                        ColumnNames.OUTFILE: str(outfile),
                    }
                )

    header = [
        ColumnNames.ROWIDX,
        ColumnNames.GENE,
        ColumnNames.STUDY_ACCESSION,
        ColumnNames.EFO_ID,
        ColumnNames.OUTCOME,
        ColumnNames.CHROM,
        ColumnNames.START,
        ColumnNames.END,
        ColumnNames.OUTFILE,
    ]
    with FileNames.TASKS_FILE.with_suffix(".tmp").open("w") as handle:
        handle.write("\t".join(header) + "\n")
        for rowidx, row in enumerate(rows, start=1):
            handle.write(
                "\t".join([str(rowidx)] + [row[col] for col in header[1:]]) + "\n"
            )
    FileNames.TASKS_FILE.with_suffix(".tmp").replace(FileNames.TASKS_FILE)

    log_info(f"wrote {len(rows)} tasks to {FileNames.TASKS_FILE}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    return argparse.ArgumentParser(
        description=(
            "Resolve gene/outcome lookups, discover studies, write the "
            "job-array file."
        )
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

    with runlog_setup():
        build_tasks()


if __name__ == "__main__":
    main()
