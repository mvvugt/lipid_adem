#!/usr/bin/env python3
"""
lipid_adem constants
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations
from pathlib import Path


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Paths

class Paths:
    """Project paths, anchored to this file's location in the repo."""
    HERE: Path = Path(__file__).resolve().parent.parent
    DATA_RAW: Path = HERE / "data" / "raw"
    DATA_TEMP: Path = HERE / "data" / "temp"
    GWAS_FILTERED: Path = DATA_TEMP / "gwas_filtered"
    RESULTS_OUTPUT: Path = HERE / "results" / "output"
    LOGS: Path = HERE / "logs"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Constants

class Constants:
    """Pipeline thresholds and external API endpoints (gwas_cat.md)."""
    MAF_THRESHOLD: float = 0.01
    GENE_COORD_FLANK_BP: int = 10_000
    MAX_STUDIES_PER_OUTCOME: int = 10
    NCBI_ESUMMARY_URL: str = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    )
    PUBMED_BATCH_SIZE: int = 200
    GRCH_BUILD: str = "GRCh38"
    EBI_OLS_SEARCH_URL: str = "https://www.ebi.ac.uk/ols/api/search"
    ICD10_CODE_PATTERN: str = r"^[A-Z]\d{2}$"
    EFO_ID_PATTERN: str = r"^EFO[:_]\d+$"
    GWAS_CATALOG_API_V2: str = "https://www.ebi.ac.uk/gwas/rest/api/v2"
    GWAS_CATALOG_FTP_BASE: str = (
        "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics"
    )
    OPEN_TARGETS_GRAPHQL_URL: str = (
        "https://api.platform.opentargets.org/api/v4/graphql"
    )


class ColumnNames:
    """Column names for the pyjasub job-array file and final output table."""
    ROWIDX: str = "rowidx"
    GENE: str = "gene"
    GENE_CHR: str = "chr"
    STUDY_ACCESSION: str = "study_accession"
    EFO_ID: str = "efo_id"
    CHROM: str = "chrom"
    START: str = "start"
    END: str = "end"
    OUTFILE: str = "outfile"
    OUTCOME: str = "outcome"
    ICD_CODE: str = "code"
    DESCRIPTION: str = "description"
    SOURCE: str = "source"
    VARIANT_OR_STAT: str = "variant_or_stat"
    P_VALUE: str = "p_value"
    EFFECT_SIZE: str = "effect_size"
    MAF: str = "maf"
    FINNGEN_PHENOCODE: str = "finngen_phenocode"
    SOURCE_DB: str = "source_db"


class FileNames:
    """File paths, built from `Paths` so they move together."""
    GENE_LIST: Path = Paths.DATA_RAW / "gene_list.txt"
    ICD_CODE_LIST: Path = Paths.DATA_RAW / "icd_codes.txt"
    EFO_UKB_MAPPING: Path = Paths.DATA_RAW / "efo_ukb_master_mapping.tsv"
    FINNGEN_MANIFEST: Path = Paths.DATA_RAW / "finngen_r13_manifest.tsv"
    GWAS_CATALOG_MANUAL_STUDIES: Path = (
        Paths.DATA_RAW / "gwas_catalog_manual_studies.tsv"
    )
    TASKS_FILE: Path = Paths.DATA_TEMP / "tasks.tsv"
    FINAL_RESULTS: Path = Paths.RESULTS_OUTPUT / "final_results.tsv"
