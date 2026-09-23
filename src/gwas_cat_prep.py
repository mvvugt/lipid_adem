#!/usr/bin/env python3
"""
Resolves gene coordinates and outcome-to-EFO mappings (persisting any new
lookups back to data/raw/gene_list.txt and data/raw/icd_codes.txt),
discovers GWAS Catalog studies, curated FinnGen phenocodes, and curated
not-yet-API-indexed GWAS Catalog studies per outcome, and writes the
pyjasub job-array file that src/filter_gwas_cat.sh consumes, plus a
study-discovery audit log listing every discovered study across all
sources with its inclusion status and reason.
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

# Display-only per-study metadata columns in the study-discovery audit log,
# between `pubmed_id` and `note`.
META_COLUMNS: list[str] = [
    ColumnNames.PUB_DATE,
    ColumnNames.FIRST_AUTHOR,
    ColumnNames.JOURNAL,
    ColumnNames.TITLE,
    ColumnNames.TRAIT,
    ColumnNames.SAMPLE_SIZE,
    ColumnNames.ANCESTRY,
    ColumnNames.COHORT,
]
FINNGEN_COHORT: str = "FinnGen R13"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def _manual_meta(
    manual_row: pd.Series, pubmed: dict[int, dict]
) -> dict[str, str]:
    """Build audit metadata for a curated (manual) GWAS Catalog study.

    Values curated in the manual table win; blanks in the publication
    columns are filled from PubMed.

    Parameters
    ----------
    manual_row : `pd.Series`
        One row of `functions.load_manual_gwas_catalog_studies()`.
    pubmed : `dict[int, dict]`
        As returned by `functions.pubmed_summaries`.

    Returns
    -------
    meta : `dict[str, str]`
        One value per column in `META_COLUMNS`.
    """
    pid = str(manual_row.get(ColumnNames.PUBMED_ID, ""))
    summary = pubmed.get(int(pid), {}) if pid.isdigit() else {}
    date = summary.get("date")
    fetched = {
        ColumnNames.PUB_DATE: (
            date.strftime("%Y-%m-%d") if date is not None else ""
        ),
        ColumnNames.FIRST_AUTHOR: summary.get("first_author", ""),
        ColumnNames.JOURNAL: summary.get("journal", ""),
        ColumnNames.TITLE: summary.get("title", ""),
    }
    curated = {
        col: functions.clean_cell(manual_row.get(col, ""))
        for col in META_COLUMNS
        if col != ColumnNames.TRAIT
    }
    curated[ColumnNames.TRAIT] = functions.clean_cell(
        manual_row.get(ColumnNames.DISEASE_TRAIT, "")
    )
    return {
        col: curated.get(col) or fetched.get(col, "") for col in META_COLUMNS
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _finngen_meta(
    phenocode: str, manifest_df: pd.DataFrame
) -> dict[str, str]:
    """Build audit metadata for a FinnGen phenocode from the manifest.

    Parameters
    ----------
    phenocode : `str`
        Curated FinnGen phenocode (e.g. "G6_ALZHEIMER").
    manifest_df : `pd.DataFrame`
        Manifest table from `functions.load_finngen_manifest`.

    Returns
    -------
    meta : `dict[str, str]`
        One value per column in `META_COLUMNS`; all `""` if `phenocode`
        is not in the manifest.
    """
    meta = {col: "" for col in META_COLUMNS}
    matches = manifest_df.loc[manifest_df["phenocode"] == phenocode]
    if matches.empty:
        return meta
    row = matches.iloc[0]
    meta[ColumnNames.TRAIT] = functions.clean_cell(row.get("phenotype", ""))
    meta[ColumnNames.SAMPLE_SIZE] = (
        f"{row.get('num_cases', '')} cases, "
        f"{row.get('num_controls', '')} controls"
    )
    meta[ColumnNames.COHORT] = FINNGEN_COHORT
    return meta


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def build_tasks() -> None:
    """Resolve lookups, discover studies, and write the job-array file.

    Loads `FileNames.GENE_LIST`/`ICD_CODE_LIST`, fills in any missing gene
    columns/cells (symbol, coordinates, Ensembl ID, UniProt; see
    `functions.resolve_gene_table`) and outcome/code-to-EFO mappings
    (persisting the results
    back to those files so reruns skip already-resolved rows), discovers
    GWAS Catalog studies per outcome (grouped by the distinct EFO IDs
    under that outcome), unions in any curated not-yet-API-indexed GWAS
    Catalog accessions for that outcome (see
    data/raw/gwas_catalog_manual_studies.SOURCE.md), validates each
    outcome's curated FinnGen phenocode (if set) against the vendored
    manifest, and writes
    `FileNames.TASKS_FILE` with columns: rowidx, gene, study_accession,
    efo_id, outcome, chrom, start, end, outfile, source. Then archives any
    existing pyjasub log dir (`Paths.FILTER_TASK_LOGS`) via
    `functions.archive_dir`, since pyjasub refuses a newer array file.

    Also writes `FileNames.STUDY_DISCOVERY_LOG`, an audit trail of every
    study discovered across all three sources (GWAS Catalog, FinnGen,
    manual), one row each, with its inclusion status and reason (e.g.
    "no_full_sumstats", "over_cap", "not_found_in_manifest") -- unlike
    `TASKS_FILE`, which only contains the surviving, capped set. Each
    row also carries display-only metadata (`META_COLUMNS`): publication
    date/first author/journal/title from PubMed, and trait, sample size,
    ancestry and cohort from the GWAS Catalog record, the manual table,
    or the FinnGen manifest, so the recency cap can be checked by eye.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If the gene or ICD/outcome placeholder files have not been filled
        in.
    functions.GeneTableError
        If a gene row cannot be resolved, or its identifiers disagree.
    """
    genes_df = functions.load_gene_table(FileNames.GENE_LIST)
    icd_df = functions.load_icd_table(FileNames.ICD_CODE_LIST)
    log_info(f"{len(genes_df)} genes, {len(icd_df)} icd codes")

    genes_before = genes_df.copy()
    genes_df = functions.resolve_gene_table(genes_df)
    if not genes_df.equals(genes_before):
        functions.write_table_atomic(genes_df, FileNames.GENE_LIST)
        log_info(f"wrote resolved gene annotations to {FileNames.GENE_LIST}")

    icd_before = icd_df.copy()
    icd_df = functions.resolve_efo_ids(icd_df)
    if not icd_df.equals(icd_before):
        functions.write_table_atomic(icd_df, FileNames.ICD_CODE_LIST, sep=",")
        log_info(f"wrote resolved efo_ids to {FileNames.ICD_CODE_LIST}")

    Paths.DATA_TEMP.mkdir(parents=True, exist_ok=True)
    Paths.GWAS_FILTERED.mkdir(parents=True, exist_ok=True)

    # Discover studies once per distinct efo_id (global dedupe), then
    # union each outcome's accessions from its own distinct efo_ids.
    distinct_efo_ids = sorted(
        {efo_id for efo_id in icd_df[ColumnNames.EFO_ID] if efo_id}
    )
    classified_by_efo = {
        efo_id: functions.discover_studies_with_reasons(efo_id)
        for efo_id in distinct_efo_ids
    }

    # Same dedupe/union pattern for FinnGen, keyed by curated phenocode(s)
    # instead of a live-discovered EFO ID. A cell may list more than one
    # phenocode (comma-separated) when an outcome is curated against
    # several definitional variants of the same disease.
    finngen_manifest_df = functions.load_finngen_manifest()
    manual_studies_df = functions.load_manual_gwas_catalog_studies()
    # One batched PubMed lookup for all curated studies (their GWAS
    # Catalog records 404 until indexed, so PubMed is all we can fetch).
    manual_pubmed = functions.pubmed_summaries(
        manual_studies_df[ColumnNames.PUBMED_ID].tolist()
    )
    distinct_phenocodes = sorted(
        {
            phenocode
            for cell in icd_df[ColumnNames.FINNGEN_PHENOCODE]
            for phenocode in functions.finngen_phenocodes_in_cell(cell)
        }
    )
    studies_by_phenocode = {
        phenocode: functions.finngen_studies_for_phenocode(
            phenocode, finngen_manifest_df
        )
        for phenocode in distinct_phenocodes
    }

    rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    for outcome, group in icd_df.groupby(ColumnNames.OUTCOME):
        outcome_efo_ids = sorted({e for e in group[ColumnNames.EFO_ID] if e})
        accession_to_efo: dict[str, str] = {}
        for efo_id in outcome_efo_ids:
            for record in classified_by_efo[efo_id]:
                status = (
                    "included"
                    if record["reason"] == "included"
                    else "excluded"
                )
                audit_rows.append(
                    {
                        ColumnNames.OUTCOME: outcome,
                        ColumnNames.SOURCE: "gwas_catalog",
                        ColumnNames.STUDY_ACCESSION: record["accession_id"],
                        ColumnNames.EFO_ID: efo_id,
                        ColumnNames.STATUS: status,
                        ColumnNames.REASON: record["reason"],
                        ColumnNames.PUBMED_ID: str(
                            record.get("pubmed_id") or ""
                        ),
                        **{col: record[col] for col in META_COLUMNS},
                        ColumnNames.NOTE: "",
                    }
                )
                if record["reason"] == "included":
                    accession_to_efo.setdefault(
                        record["accession_id"], efo_id
                    )

        # Curated accessions deposited on the FTP server but not yet
        # searchable via the API -- see gwas_catalog_manual_studies.SOURCE.md.
        # setdefault: an accession the API *can* already discover keeps
        # its real efo_id rather than being overwritten with "".
        for accession in functions.manual_studies_for_outcome(
            outcome, manual_studies_df
        ):
            accession_to_efo.setdefault(accession, "")

        outcome_manual_rows = manual_studies_df.loc[
            manual_studies_df[ColumnNames.OUTCOME] == outcome
        ]
        for _, manual_row in outcome_manual_rows.iterrows():
            audit_rows.append(
                {
                    ColumnNames.OUTCOME: outcome,
                    ColumnNames.SOURCE: "manual",
                    ColumnNames.STUDY_ACCESSION: manual_row["accession_id"],
                    ColumnNames.EFO_ID: "",
                    ColumnNames.STATUS: "included",
                    ColumnNames.REASON: "included",
                    ColumnNames.PUBMED_ID: str(
                        manual_row.get(ColumnNames.PUBMED_ID, "")
                    ),
                    **_manual_meta(manual_row, manual_pubmed),
                    ColumnNames.NOTE: functions.clean_cell(
                        manual_row.get(ColumnNames.NOTE, "")
                    ),
                }
            )

        outcome_phenocodes = sorted(
            {
                phenocode
                for cell in group[ColumnNames.FINNGEN_PHENOCODE]
                for phenocode in functions.finngen_phenocodes_in_cell(cell)
            }
        )
        finngen_accessions: list[str] = []
        for phenocode in outcome_phenocodes:
            found = studies_by_phenocode[phenocode]
            finngen_accessions.extend(found)
            audit_rows.append(
                {
                    ColumnNames.OUTCOME: outcome,
                    ColumnNames.SOURCE: "finngen",
                    ColumnNames.STUDY_ACCESSION: phenocode,
                    ColumnNames.EFO_ID: "",
                    ColumnNames.STATUS: "included" if found else "excluded",
                    ColumnNames.REASON: (
                        "included" if found else "not_found_in_manifest"
                    ),
                    ColumnNames.PUBMED_ID: "",
                    **_finngen_meta(phenocode, finngen_manifest_df),
                    ColumnNames.NOTE: "",
                }
            )

        for _, gene_row in genes_df.iterrows():
            gene = gene_row[ColumnNames.GENE]
            region = functions.gene_row_region(
                gene_row, Constants.GENE_COORD_FLANK_BP
            )
            for accession, efo_id in accession_to_efo.items():
                outfile = (
                    Paths.GWAS_FILTERED / f"{gene}_{accession}_result.tsv.gz"
                )
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
                        ColumnNames.SOURCE: "gwas_catalog",
                    }
                )
            for accession in finngen_accessions:
                outfile = (
                    Paths.GWAS_FILTERED / f"{gene}_{accession}_result.tsv.gz"
                )
                rows.append(
                    {
                        ColumnNames.GENE: gene,
                        ColumnNames.STUDY_ACCESSION: accession,
                        ColumnNames.EFO_ID: "",
                        ColumnNames.OUTCOME: outcome,
                        ColumnNames.CHROM: region.chrom,
                        ColumnNames.START: str(region.start),
                        ColumnNames.END: str(region.end),
                        ColumnNames.OUTFILE: str(outfile),
                        ColumnNames.SOURCE: "finngen",
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
        ColumnNames.SOURCE,
    ]
    with FileNames.TASKS_FILE.with_suffix(".tmp").open("w") as handle:
        handle.write("\t".join(header) + "\n")
        for rowidx, row in enumerate(rows, start=1):
            handle.write(
                "\t".join([str(rowidx)] + [row[col] for col in header[1:]]) + "\n"
            )
    FileNames.TASKS_FILE.with_suffix(".tmp").replace(FileNames.TASKS_FILE)

    log_info(f"wrote {len(rows)} tasks to {FileNames.TASKS_FILE}")

    # pyjasub errors if the job-array file is newer than an existing log dir
    functions.archive_dir(Paths.FILTER_TASK_LOGS)

    audit_header = [
        ColumnNames.OUTCOME,
        ColumnNames.SOURCE,
        ColumnNames.STUDY_ACCESSION,
        ColumnNames.EFO_ID,
        ColumnNames.STATUS,
        ColumnNames.REASON,
        ColumnNames.PUBMED_ID,
        *META_COLUMNS,
        ColumnNames.NOTE,
    ]
    audit_tmp = FileNames.STUDY_DISCOVERY_LOG.with_suffix(".tmp")
    with audit_tmp.open("w") as handle:
        handle.write("\t".join(audit_header) + "\n")
        for row in audit_rows:
            handle.write(
                "\t".join(str(row[col]) for col in audit_header) + "\n"
            )
    audit_tmp.replace(FileNames.STUDY_DISCOVERY_LOG)

    log_info(
        f"wrote {len(audit_rows)} study-discovery rows to "
        f"{FileNames.STUDY_DISCOVERY_LOG}"
    )


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

    with runlog_setup(root=Paths.HERE):
        build_tasks()


if __name__ == "__main__":
    main()
