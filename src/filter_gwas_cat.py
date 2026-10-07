#!/usr/bin/env python3
"""
Runs once per pyjasub array task over `--step` rows of the job-array file
(data/temp/tasks.tsv), one row per study. For each study, remote-queries
its summary stats (GWAS Catalog harmonised or raw, or FinnGen, per the
row's `source`) for every gene region in data/temp/gene_regions.tsv in one
pass, filters to MAF < Constants.MAF_THRESHOLD (no MAF filter when it is
`None`: every in-region row is kept), and writes the row's output file.
Rows whose output file already exists are skipped.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import requests
from log_tools.emitter import log_info, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    ColumnNames,
    Constants,
    FileNames,
    Paths,
    RunlogOrder,
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def _write_empty_result(outfile: Path, study_accession: str) -> None:
    """Write a header-only (0-row) result for an unusable study.

    Parameters
    ----------
    outfile : `Path`
        Path to write the empty TSV to.
    study_accession : `str`
        GWAS Catalog study accession or FinnGen phenocode (logging only).

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
    functions.write_table_atomic(
        pd.DataFrame(columns=["gene", "study_accession", "source_db"]),
        outfile,
    )
    log_info(f"{study_accession}: empty result -> {outfile}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _run_filter_gwas_catalog(
    study_accession: str, regions: dict[str, functions.GeneRegion]
) -> pd.DataFrame | None:
    """Resolve and filter one GWAS Catalog study over all gene regions.

    Parameters
    ----------
    study_accession : `str`
        GWAS Catalog study accession.
    regions : `dict[str, functions.GeneRegion]`
        Gene symbol -> flanked region.

    Returns
    -------
    filtered : `pd.DataFrame` or `NoneType`
        The filtered sumstats (leading `gene` column), or `None` if the
        study has no usable summary statistics.

    Raises
    ------
    functions.SumstatsColumnError
        If the sumstats file lacks the expected chrom/pos/MAF columns.
    """
    location = functions.study_summary_stats_location(study_accession)
    if location is None:
        log_warn(
            f"{study_accession} has no full summary statistics available "
            f"on GWAS Catalog"
        )
        return None

    try:
        source = functions.resolve_sumstats_source(location, study_accession)
    except ValueError as exc:
        log_warn(str(exc))
        return None

    # maf_col is an effect-allele frequency (may exceed 0.5), so
    # min(af, 1 - af) is applied, as for FinnGen; gene-burden mask rows
    # (effect allele e.g. "M1.0001") are kept whatever their MAF
    if source.is_tabix_indexed:
        return functions.filter_sumstats_regions(
            tabix_source=source.url,
            regions=regions,
            maf_col=source.maf_col,
            maf_threshold=Constants.MAF_THRESHOLD,
            chrom_col=source.chrom_col,
            pos_col=source.pos_col,
            transform_to_maf=True,
            effect_allele_col="effect_allele",
        )
    return functions.filter_raw_sumstats_regions(
        url=source.url,
        regions=regions,
        maf_col=source.maf_col,
        maf_threshold=Constants.MAF_THRESHOLD,
        chrom_col=source.chrom_col,
        pos_col=source.pos_col,
        transform_to_maf=True,
        effect_allele_col="effect_allele",
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _run_filter_finngen(
    phenocode: str,
    regions: dict[str, functions.GeneRegion],
    manifest_df: pd.DataFrame,
) -> pd.DataFrame | None:
    """Resolve and filter one FinnGen phenocode over all gene regions.

    Parameters
    ----------
    phenocode : `str`
        FinnGen phenocode.
    regions : `dict[str, functions.GeneRegion]`
        Gene symbol -> flanked region.
    manifest_df : `pd.DataFrame`
        As returned by `functions.load_finngen_manifest`.

    Returns
    -------
    filtered : `pd.DataFrame` or `NoneType`
        The filtered sumstats (leading `gene` column), or `None` if the
        phenocode is not in the manifest.
    """
    url = functions.finngen_sumstats_url(phenocode, manifest_df)
    if url is None:
        log_warn(f"{phenocode} not found in FinnGen manifest")
        return None

    return functions.filter_sumstats_regions(
        tabix_source=url,
        regions=regions,
        maf_col="af_alt",
        maf_threshold=Constants.MAF_THRESHOLD,
        chrom_col="chrom",
        pos_col="pos",
        transform_to_maf=True,
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_filter(
    study_accession: str,
    source: str,
    outfile: Path,
    regions: dict[str, functions.GeneRegion],
    manifest_df: pd.DataFrame | None,
) -> None:
    """Filter one study's sumstats over all gene regions and write it.

    Parameters
    ----------
    study_accession : `str`
        GWAS Catalog study accession, or FinnGen phenocode if
        `source == "finngen"`.
    source : `str`
        Which sumstats source `study_accession` refers to: `"gwas_catalog"`,
        `"manual"` (a curated GWAS Catalog accession, same FTP route) or
        `"finngen"`.
    outfile : `Path`
        Path to write the filtered TSV to.
    regions : `dict[str, functions.GeneRegion]`
        Gene symbol -> flanked region.
    manifest_df : `pd.DataFrame` or `NoneType`
        FinnGen manifest; required when `source == "finngen"`.

    Returns
    -------
    `None`

    Raises
    ------
    ValueError
        If `source` is not `"gwas_catalog"`, `"manual"` or `"finngen"`.

    Notes
    -----
    If the study/phenocode has no usable summary statistics (not
    available, ambiguous/missing raw file, or absent from the FinnGen
    manifest), a header-only (0-row) result is written instead of
    raising, so the row is marked done and never retried. Transient
    failures (network errors, a `.tbi`-missing `OSError` on the tabix
    path) and a `functions.SumstatsColumnError` (unexpected column
    layout) are not caught here and propagate without writing an
    outfile, so the row is never marked done. The outfile is written
    atomically, so an interrupted task never leaves a partial file that
    pyjasub would count as done.
    """
    outfile.parent.mkdir(parents=True, exist_ok=True)

    if source == "finngen":
        filtered = _run_filter_finngen(study_accession, regions, manifest_df)
    elif source in ("gwas_catalog", "manual"):
        filtered = _run_filter_gwas_catalog(study_accession, regions)
    else:
        raise ValueError(f"unknown source {source!r} for {study_accession}")
    if filtered is None:
        _write_empty_result(outfile, study_accession)
        return

    filtered.insert(1, "study_accession", study_accession)
    filtered.insert(2, "source_db", source)

    functions.write_table_atomic(filtered, outfile)
    log_info(
        f"{study_accession}: {len(filtered)} rows over "
        f"{filtered[ColumnNames.GENE].nunique()} genes -> {outfile}"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_task(tasks_file: Path, task_id: int, step: int) -> None:
    """Filter the `step` job-array rows starting at `task_id`.

    Parameters
    ----------
    tasks_file : `Path`
        The pyjasub job-array file (`tasks.tsv`), columns: rowidx,
        study_accession, source, outfile.
    task_id : `int`
        First row to process (1-based, excluding the header).
    step : `int`
        Number of rows to process; capped at the last row.

    Returns
    -------
    `None`

    Raises
    ------
    ValueError
        If `task_id` is past the last row, or a row's `rowidx` does not
        match its position.
    RuntimeError
        After the whole chunk has been attempted, if any row failed with
        a transient (network/IO) error or a column mismatch.

    Notes
    -----
    Rows whose outfile already exists are skipped, so a chunk re-run by
    pyjasub after a partial failure only redoes the missing studies. A
    row failing with `requests.RequestException`, `OSError` or
    `functions.SumstatsColumnError` is logged and left without an
    outfile; the remaining rows still run, and the task then exits
    non-zero. A column mismatch will not resolve on a rerun: it needs
    the study's source or column names fixed.
    """
    tasks = functions.load_tasks(tasks_file).reset_index(drop=True)
    if not 1 <= task_id <= len(tasks):
        raise ValueError(
            f"task_id {task_id} out of range: {tasks_file} has "
            f"{len(tasks)} rows"
        )
    chunk = tasks.iloc[task_id - 1 : task_id - 1 + step]
    regions = functions.load_gene_regions(FileNames.GENE_REGIONS_FILE)
    log_info(
        f"rows {task_id}-{task_id + len(chunk) - 1} of {len(tasks)}, "
        f"{len(regions)} gene regions"
    )
    manifest_df = None
    failed: list[str] = []
    mismatched: list[str] = []
    for position, (_, row) in enumerate(chunk.iterrows(), start=task_id):
        if int(row[ColumnNames.ROWIDX]) != position:
            raise ValueError(
                f"row {position} has rowidx {row[ColumnNames.ROWIDX]} in "
                f"{tasks_file}"
            )
        outfile = Path(row[ColumnNames.OUTFILE])
        accession = row[ColumnNames.STUDY_ACCESSION]
        source = row[ColumnNames.SOURCE]
        if outfile.exists():
            log_info(f"{accession}: {outfile} exists, skipped")
            continue
        if source == "finngen" and manifest_df is None:
            manifest_df = functions.load_finngen_manifest()
        try:
            run_filter(accession, source, outfile, regions, manifest_df)
        except (requests.RequestException, OSError) as exc:
            log_warn(
                f"{accession}: failed ({type(exc).__name__}: {exc}), "
                f"left for rerun"
            )
            failed.append(accession)
        except functions.SumstatsColumnError as exc:
            log_warn(
                f"{accession}: column mismatch, no outfile written ({exc})"
            )
            mismatched.append(accession)
    errors = []
    if failed:
        errors.append(
            f"{len(failed)} row(s) failed, rerun pyjasub: {', '.join(failed)}"
        )
    if mismatched:
        errors.append(
            f"{len(mismatched)} row(s) with a column mismatch, fix source/"
            f"columns: {', '.join(mismatched)}"
        )
    if errors:
        raise RuntimeError("; ".join(errors))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Filter the sumstats of `--step` job-array rows (one study "
            "each) over all gene regions."
        )
    )
    parser.add_argument(
        "--tasks-file",
        type=Path,
        required=True,
        help="pyjasub job-array file (data/temp/tasks.tsv)",
    )
    parser.add_argument(
        "--task-id",
        type=int,
        required=True,
        help="first row to process (1-based, excluding the header)",
    )
    parser.add_argument(
        "--step",
        type=int,
        default=1,
        help="number of rows to process (default: 1)",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    args = parser.parse_args()
    if args.step < 1:
        parser.error(f"--step must be >= 1, got {args.step}")
    return args


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.FILTER_GWAS_CAT):
        run_task(args.tasks_file, args.task_id, args.step)


if __name__ == "__main__":
    main()
