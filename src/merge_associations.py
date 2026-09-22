#!/usr/bin/env python3
"""
Gathers filtered sumstats, adds curated GWAS Catalog associations and Open
Targets gene-burden evidence, and writes the combined final results table.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations
import argparse

import pandas as pd
from log_tools.emitter import log_info
from log_tools.setup import runlog_setup

import functions
from project_constants import ColumnNames, Constants, FileNames, Paths


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def load_filter_results() -> pd.DataFrame:
    """Load and tag all filtered result files.

    Returns
    -------
    combined : `pd.DataFrame`
        Concatenated filtered outputs with a `source` column set to
        `"summary-stats"`. Empty if no filtered output files exist yet.
    """
    frames = []
    for result_path in sorted(Paths.GWAS_FILTERED.glob("*_result.tsv.gz")):
        frame = pd.read_csv(result_path, sep="\t")
        frame[ColumnNames.SOURCE] = "summary-stats"
        frames.append(frame)

    if not frames:
        log_info("no filtered result files found yet")
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def merge_results() -> None:
    """Merge all three evidence sources and write the final results table.

    Reuses the `efo_id`/`chrom`/`start`/`end` already resolved and
    persisted by `gwas_cat_prep.py` -- no lookups are repeated here.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If the gene or ICD/outcome placeholder files have not been filled in.
    """
    genes_df = functions.load_gene_table(FileNames.GENE_LIST)
    icd_df = functions.load_icd_table(FileNames.ICD_CODE_LIST)

    parts = [load_filter_results()]

    outcome_efo_ids = (
        icd_df[icd_df[ColumnNames.EFO_ID] != ""]
        .groupby(ColumnNames.OUTCOME)[ColumnNames.EFO_ID]
        .unique()
    )

    for _, gene_row in genes_df.iterrows():
        gene = gene_row[ColumnNames.GENE]
        region = functions.gene_row_region(gene_row, Constants.GENE_COORD_FLANK_BP)

        for outcome, efo_ids in outcome_efo_ids.items():
            for efo_id in efo_ids:
                curated = functions.curated_associations(
                    efo_id, region, Constants.MAF_THRESHOLD
                )
                if not curated.empty:
                    curated[ColumnNames.GENE] = gene
                    curated[ColumnNames.OUTCOME] = outcome
                    curated[ColumnNames.SOURCE] = "curated"
                    parts.append(curated)

        burden = functions.gene_burden_evidence(gene)
        if not burden.empty:
            burden[ColumnNames.SOURCE] = "gene-burden"
            parts.append(burden)

    combined = pd.concat([p for p in parts if not p.empty], ignore_index=True)

    Paths.RESULTS_OUTPUT.mkdir(parents=True, exist_ok=True)
    functions.write_table_atomic(combined, FileNames.FINAL_RESULTS)
    log_info(f"wrote {len(combined)} rows to {FileNames.FINAL_RESULTS}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    return argparse.ArgumentParser(
        description="Merge: summary-stats, curated, and gene-burden evidence."
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

    with runlog_setup(root=Paths.HERE):
        merge_results()


if __name__ == "__main__":
    main()
