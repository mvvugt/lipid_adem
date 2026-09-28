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
from log_tools.emitter import (
    log_count,
    log_count_summary,
    log_info,
    log_stage,
    log_warn,
)
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    ColumnNames,
    Constants,
    FileNames,
    Paths,
    RunlogOrder,
)


# log_count key for EFO ids with no curated associations at all
_NO_CURATED_COUNT_KEY: str = "efo_no_curated"


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

    n_rows = sum(len(frame) for frame in frames)
    log_info(
        f"summary-stats: {len(frames)} files, {n_rows} rows "
        f"({len(missing)} missing)"
    )
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _format_counts(counts: dict[str, int]) -> str:
    """Render non-zero counts as ``KEY=n`` pairs, or ``none``.

    Parameters
    ----------
    counts : `dict[str, int]`
        Count per key (e.g. per gene), in display order.

    Returns
    -------
    text : `str`
        Space-separated ``KEY=n`` pairs for keys with a count above 0,
        or ``"none"`` if every count is 0.
    """
    pairs = [f"{key}={n}" for key, n in counts.items() if n > 0]
    return " ".join(pairs) if pairs else "none"


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

    log_stage("load_sumstats")
    parts = [load_filter_results()]

    outcome_efo_ids = (
        icd_df[~icd_df[ColumnNames.EFO_ID].isin(["", Constants.NA_STRING])]
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
    log_stage("fetch_curated")
    for efo_id in unique_efo_ids:
        records = functions.fetch_curated_associations(efo_id)
        in_region: dict[str, int] = {}
        for gene, region in regions.items():
            curated = functions.filter_curated_associations(
                records, region, Constants.MAF_THRESHOLD
            )
            in_region[gene] = len(curated)
            curated_by_gene_efo[(gene, efo_id)] = curated
        # one line per EFO with any associations; empty EFOs only counted
        if records:
            log_info(
                f"{efo_id}: {len(records)} fetched; in region: "
                f"{_format_counts(in_region)}"
            )
        else:
            log_count(_NO_CURATED_COUNT_KEY)
        del records
    log_count_summary(
        _NO_CURATED_COUNT_KEY, label="EFO ids with 0 curated associations"
    )

    # assemble in gene -> outcome -> efo_id order so row order is unchanged
    log_stage("gene_burden")
    burden_rows: dict[str, int] = {}
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
        burden_rows[gene] = len(burden)
        if not burden.empty:
            burden[ColumnNames.SOURCE] = "gene-burden"
            parts.append(burden)
    n_zero_genes = sum(1 for n in burden_rows.values() if n == 0)
    log_info(
        f"gene-burden rows: {_format_counts(burden_rows)} "
        f"({n_zero_genes} genes with 0)"
    )

    combined = pd.concat([p for p in parts if not p.empty], ignore_index=True)

    log_stage("write")
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

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.MERGE_ASSOCIATIONS):
        merge_results()


if __name__ == "__main__":
    main()
