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
    HarmonisedColumns,
    MafStatus,
    Paths,
    RunlogOrder,
    SourceColumnMaps,
)


# log_count key for EFO ids with no curated associations at all
_NO_CURATED_COUNT_KEY: str = "efo_no_curated"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def load_filter_results(
    outcome_desc: dict[tuple[str, str], str],
    trait_labels: dict[str, str],
) -> pd.DataFrame:
    """Load, label and harmonise the filtered result files in the tasks file.

    Only the `outfile` paths in the current `FileNames.TASKS_FILE` are
    read, so stale files left in `gwas_filtered/` (from studies bumped
    past the cap, or genes since removed) are ignored. Listed outfiles
    that do not exist yet are skipped with a warning. Each file is read
    once; when several task rows (outcomes) point to the same file, its
    rows are repeated once per outcome.

    Parameters
    ----------
    outcome_desc : `dict[tuple[str, str], str]`
        `(outcome, efo_id)` -> outcome description in words.
    trait_labels : `dict[str, str]`
        `study_accession` -> the study's trait label.

    Returns
    -------
    combined : `pd.DataFrame`
        Harmonised rows (see `functions.harmonise_frame`) with `source`
        set to `"summary-stats"`. Empty if no filtered output files exist.

    Raises
    ------
    FileNotFoundError
        If the tasks file does not exist.
    """
    tasks = functions.load_tasks(FileNames.TASKS_FILE)
    frames = []
    missing: list[Path] = []
    n_files = 0
    # groupby(sort=False) keeps the tasks-file order
    for outfile, file_tasks in tasks.groupby(
        ColumnNames.OUTFILE, sort=False
    ):
        result_path = Path(outfile)
        if not result_path.exists():
            missing.append(result_path)
            continue
        n_files += 1
        frame = _read_filtered_file(result_path)
        if frame.empty:
            continue
        for _, task in file_tasks.iterrows():
            labelled = frame.copy()
            outcome = task[ColumnNames.OUTCOME]
            efo_id = task[ColumnNames.EFO_ID]
            accession = task[ColumnNames.STUDY_ACCESSION]
            labelled[ColumnNames.SOURCE] = "summary-stats"
            labelled[ColumnNames.OUTCOME] = outcome
            labelled[ColumnNames.EFO_ID] = efo_id
            labelled[HarmonisedColumns.OUTCOME_DESC] = outcome_desc.get(
                (outcome, efo_id), pd.NA
            )
            labelled[HarmonisedColumns.TRAIT_LABEL] = trait_labels.get(
                accession, pd.NA
            )
            frames.append(labelled)

    if missing:
        preview = ", ".join(str(p) for p in missing[:3])
        log_warn(
            f"{len(missing)} outfiles listed in {FileNames.TASKS_FILE} "
            f"do not exist yet, skipped (first: {preview})"
        )

    n_rows = sum(len(frame) for frame in frames)
    log_info(
        f"summary-stats: {n_files} files, {n_rows} rows incl. one copy "
        f"per outcome ({len(missing)} missing)"
    )
    if not frames:
        return pd.DataFrame()
    harmonised = []
    for frame in frames:
        column_map = (
            SourceColumnMaps.FINNGEN
            if frame[ColumnNames.SOURCE_DB].iloc[0] == "finngen"
            else SourceColumnMaps.GWAS_CATALOG
        )
        harmonised.append(functions.harmonise_frame(frame, column_map))
    return pd.concat(harmonised, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _read_filtered_file(path: Path) -> pd.DataFrame:
    """Read one filtered result file, removing stray CRLF carriage returns.

    Files filtered before the CRLF fix in `functions` can carry a
    trailing `"\\r"` on their last column name and values.

    Parameters
    ----------
    path : `Path`
        A filtered result file (`*_result.tsv.gz`).

    Returns
    -------
    frame : `pd.DataFrame`
        The file's rows, with `"\\r"` stripped from the last column.
    """
    frame = pd.read_csv(path, sep="\t", low_memory=False)
    frame.columns = [str(col).rstrip("\r") for col in frame.columns]
    last = frame.columns[-1]
    if frame[last].dtype == object:
        frame[last] = frame[last].str.rstrip("\r")
    return frame


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _outcome_descriptions(
    icd_df: pd.DataFrame,
) -> dict[tuple[str, str], str]:
    """Describe each (outcome, efo_id) pair in words, from the ICD table.

    Parameters
    ----------
    icd_df : `pd.DataFrame`
        The ICD/outcome table from `functions.load_icd_table`.

    Returns
    -------
    descriptions : `dict[tuple[str, str], str]`
        `(outcome, efo_id)` -> unique non-empty `description` values,
        joined with `"; "`, in file order.
    """
    descriptions: dict[tuple[str, str], str] = {}
    grouped = icd_df.groupby(
        [ColumnNames.OUTCOME, ColumnNames.EFO_ID], sort=False
    )
    for key, group in grouped:
        texts = [
            text
            for text in dict.fromkeys(group[ColumnNames.DESCRIPTION])
            if isinstance(text, str) and text.strip()
        ]
        descriptions[key] = "; ".join(texts)
    return descriptions


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_trait_labels() -> dict[str, str]:
    """Map each study accession to the trait label its source reports.

    Uses the `trait` column of `FileNames.STUDY_DISCOVERY_LOG` (written by
    `gwas_cat_prep.py`), then fills FinnGen phenocodes still missing from
    the `phenotype` column of the FinnGen manifest.

    Returns
    -------
    labels : `dict[str, str]`
        `study_accession` (or FinnGen phenocode) -> trait label. Missing
        sources are skipped with a warning.
    """
    labels: dict[str, str] = {}
    if FileNames.STUDY_DISCOVERY_LOG.exists():
        audit = pd.read_csv(
            FileNames.STUDY_DISCOVERY_LOG, sep="\t", dtype=str
        ).fillna("")
        for accession, trait in zip(
            audit[ColumnNames.STUDY_ACCESSION], audit[ColumnNames.TRAIT]
        ):
            if trait and accession not in labels:
                labels[accession] = trait
    else:
        log_warn(
            f"{FileNames.STUDY_DISCOVERY_LOG} not found: GWAS Catalog "
            "trait labels left empty (rerun gwas_cat_prep.py, or gzip an "
            "existing uncompressed study_discovery_log.tsv)"
        )
    manifest = functions.load_finngen_manifest()
    for phenocode, phenotype in zip(
        manifest["phenocode"], manifest["phenotype"]
    ):
        if phenotype and phenocode not in labels:
            labels[phenocode] = phenotype
    return labels


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

    outcome_desc = _outcome_descriptions(icd_df)

    log_stage("load_sumstats")
    parts = [load_filter_results(outcome_desc, _study_trait_labels())]

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
    maf_status_counts: dict[str, int] = {
        MafStatus.NUMERIC: 0,
        MafStatus.NOT_REPORTED: 0,
    }
    for gene in regions:
        for outcome, efo_ids in outcome_efo_ids.items():
            for efo_id in efo_ids:
                curated = curated_by_gene_efo[(gene, efo_id)].copy()
                if not curated.empty:
                    curated[ColumnNames.GENE] = gene
                    curated[ColumnNames.OUTCOME] = outcome
                    curated[ColumnNames.EFO_ID] = efo_id
                    curated[HarmonisedColumns.OUTCOME_DESC] = (
                        outcome_desc.get((outcome, efo_id), pd.NA)
                    )
                    curated[ColumnNames.SOURCE] = "curated"
                    curated[ColumnNames.SOURCE_DB] = "gwas_catalog"
                    harmonised = functions.harmonise_curated(curated)
                    for status, n in (
                        harmonised[HarmonisedColumns.MAF_STATUS]
                        .value_counts()
                        .items()
                    ):
                        maf_status_counts[status] += n
                    parts.append(harmonised)

        burden = functions.gene_burden_evidence(gene)
        burden_rows[gene] = len(burden)
        if not burden.empty:
            burden[ColumnNames.SOURCE] = "gene-burden"
            burden[ColumnNames.SOURCE_DB] = "open_targets"
            parts.append(
                functions.harmonise_frame(
                    burden, SourceColumnMaps.GENE_BURDEN, has_variants=False
                )
            )
    log_info(
        "curated MAF: "
        + " ".join(f"{k}={n}" for k, n in maf_status_counts.items())
    )
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
