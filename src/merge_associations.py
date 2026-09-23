#!/usr/bin/env python3
"""
Gathers filtered sumstats, adds curated GWAS Catalog associations and Open
Targets gene-burden evidence, and writes the combined final results table.
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
from project_constants import ColumnNames, Constants, FileNames, Paths


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def load_filter_results() -> pd.DataFrame:
    """Load and tag the filtered result files listed in the tasks file.

    Only the `outfile` paths in the current `FileNames.TASKS_FILE` are
    read, so stale files left in `gwas_filtered/` (from studies bumped
    past the cap, or genes since removed) are ignored. Listed outfiles
    that do not exist yet are skipped with a warning.

    Returns
    -------
    combined : `pd.DataFrame`
        Concatenated filtered outputs with a `source` column set to
        `"summary-stats"`. Empty if no filtered output files exist yet.

    Raises
    ------
    FileNotFoundError
        If the tasks file does not exist.
    """
    frames = []
    missing: list[Path] = []
    for result_path in functions.load_task_outfiles(FileNames.TASKS_FILE):
        if not result_path.exists():
            missing.append(result_path)
            continue
        frame = pd.read_csv(result_path, sep="\t")
        frame[ColumnNames.SOURCE] = "summary-stats"
        frames.append(frame)

    if missing:
        preview = ", ".join(str(p) for p in missing[:3])
        log_warn(
            f"{len(missing)} outfiles listed in {FileNames.TASKS_FILE} "
            f"do not exist yet, skipped (first: {preview})"
        )

    if not frames:
        log_info("no filtered result files found yet")
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def merge_results() -> None:
    """Merge all three evidence sources and write the final results table.

    Reuses the `efo_id`/`chrom`/`start`/`end` already resolved and
    persisted by `gwas_cat_prep.py` -- no lookups are repeated here.
    Curated associations are downloaded once per unique `efo_id` (the
    download is gene-independent) and then filtered per gene region.

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

    regions = {
        gene_row[ColumnNames.GENE]: functions.gene_row_region(
            gene_row, Constants.GENE_COORD_FLANK_BP
        )
        for _, gene_row in genes_df.iterrows()
    }

    # fetch each efo_id once and filter it for every gene; only one EFO's
    # full record list is held in memory at a time
    curated_by_gene_efo: dict[tuple[str, str], pd.DataFrame] = {}
    # dict.fromkeys de-duplicates while keeping first-seen order
    unique_efo_ids = list(dict.fromkeys(
        efo_id for efo_ids in outcome_efo_ids for efo_id in efo_ids
    ))
    for efo_id in unique_efo_ids:
        records = functions.fetch_curated_associations(efo_id)
        for gene, region in regions.items():
            curated = functions.filter_curated_associations(
                records, region, Constants.MAF_THRESHOLD
            )
            log_info(
                f"{efo_id} / {gene} -> {len(curated)} curated associations "
                "in region"
            )
            curated_by_gene_efo[(gene, efo_id)] = curated
        del records

    # assemble in gene -> outcome -> efo_id order so row order is unchanged
    for gene in regions:
        for outcome, efo_ids in outcome_efo_ids.items():
            for efo_id in efo_ids:
                curated = curated_by_gene_efo[(gene, efo_id)].copy()
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
