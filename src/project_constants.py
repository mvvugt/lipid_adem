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
    # must match `log_dir` in config/filter_task.cnf
    FILTER_TASK_LOGS: Path = HERE / "src" / "logs" / "filter_task_logs"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Constants

class Constants:
    """Pipeline thresholds and external API endpoints (gwas_cat.md)."""
    MAF_THRESHOLD: float = 0.01
    GENE_COORD_FLANK_BP: int = 10_000
    MAX_STUDIES_PER_OUTCOME: int = 10
    # overall ceiling per child-trait search, on top of the per-term cap
    MAX_STUDIES_PER_CHILD_QUERY: int = 30
    # trait IDs never searched: MONDO_0011057 (I67.3, Binswanger disease)
    # expands via child traits to general cerebrovascular disease (stroke,
    # TIA, aneurysm) rather than dementia
    EXCLUDED_EFO_IDS: frozenset[str] = frozenset({"MONDO_0011057"})
    NCBI_ESUMMARY_URL: str = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    )
    PUBMED_BATCH_SIZE: int = 200
    GRCH_BUILD: str = "GRCh38"
    EBI_OLS_SEARCH_URL: str = "https://www.ebi.ac.uk/ols/api/search"
    # term lookup by obo_id; also serves MONDO terms imported into EFO
    EBI_OLS_TERMS_URL: str = (
        "https://www.ebi.ac.uk/ols4/api/ontologies/efo/terms"
    )
    # obsolete term -> replacement chain length followed before giving up
    MAX_REPLACEMENT_HOPS: int = 5
    # outcomes whose trait IDs also match GWAS Catalog child traits (broad);
    # every other outcome uses the exact term only (strict)
    CHILD_TRAIT_OUTCOMES: frozenset[str] = frozenset(
        {
            "all_cause_dementia",
            "alzheimers_dementia",
            "frontotemporal_dementia",
            "lewy_body_dementia",
            "parkinsons_disease_dementia",
            "vascular_dementia",
        }
    )
    ICD10_CODE_PATTERN: str = r"^[A-Z]\d{2}$"
    EFO_ID_PATTERN: str = r"^EFO[:_]\d+$"
    GWAS_CATALOG_API_V2: str = "https://www.ebi.ac.uk/gwas/rest/api/v2"
    GWAS_CATALOG_FTP_BASE: str = (
        "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics"
    )
    OPEN_TARGETS_GRAPHQL_URL: str = (
        "https://api.platform.opentargets.org/api/v4/graphql"
    )
    OPEN_TARGETS_PAGE_SIZE: int = 1000
    # extra Open Targets disease IDs queried alongside an outcome ID:
    # Open Targets still files HDL/LDL cholesterol evidence under the older
    # EFO terms, and labels the current ones "free cholesterol in HDL/LDL"
    OPEN_TARGETS_EXTRA_DISEASE_IDS: dict[str, tuple[str, ...]] = {
        "EFO_0022264": ("EFO_0004612",),
        "EFO_0022266": ("EFO_0004611",),
    }
    # written to a gene-table cell that was looked up but not found;
    # treated as resolved on reruns (clear the cell by hand to retry)
    NA_STRING: str = "NA"
    UNIPROT_HUMAN_TAXON: int = 9606


class RunlogOrder:
    """RUN_LOG.md section order per pipeline step.

    Explicit because each step runs in its own process tree (qsub,
    pyjasub, `mamba run`), so log_tools' PPID-based auto-order would
    give every step 10. The Bash job wrappers hard-code the same values
    in `RUNLOG_ORDER` and must be kept in sync.
    """
    GWAS_CAT_PREP: int = 10
    FILTER_GWAS_CAT: int = 20
    MERGE_ASSOCIATIONS: int = 30


class ColumnNames:
    """Column names for the pyjasub job-array file and final output table."""
    ROWIDX: str = "rowidx"
    GENE: str = "gene"
    GENE_CHR: str = "chr"
    ENSEMBL_ID: str = "ensemblid"
    UNIPROT: str = "uniprot"
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
    STATUS: str = "status"
    REASON: str = "reason"
    PUBMED_ID: str = "pubmed_id"
    PUB_DATE: str = "pub_date"
    FIRST_AUTHOR: str = "first_author"
    JOURNAL: str = "journal"
    TITLE: str = "title"
    TRAIT: str = "trait"
    DISEASE_TRAIT: str = "disease_trait"
    SAMPLE_SIZE: str = "sample_size"
    ANCESTRY: str = "ancestry"
    COHORT: str = "cohort"
    NOTE: str = "note"
    CHILD_TRAITS: str = "child_traits"
    MAPPED_TRAIT_ID: str = "mapped_trait_id"
    MAPPED_TRAIT: str = "mapped_trait"
    # gene_list.txt: any one of GENE_ID_COLUMNS is enough as input, the
    # rest of GENE_TABLE_COLUMNS is resolved (see resolve_gene_table)
    GENE_ID_COLUMNS: tuple[str, ...] = (GENE, ENSEMBL_ID, UNIPROT)
    GENE_TABLE_COLUMNS: tuple[str, ...] = (
        GENE,
        GENE_CHR,
        START,
        END,
        ENSEMBL_ID,
        UNIPROT,
    )


class HarmonisedColumns:
    """Core columns of the final results table, shared by every source.

    Each source's original columns are kept after the core ones, renamed
    to `RAW_PREFIX + <original name>` so they can never collide with a
    core name.
    """
    GENE: str = ColumnNames.GENE
    SOURCE: str = ColumnNames.SOURCE
    SOURCE_DB: str = ColumnNames.SOURCE_DB
    STUDY_ACCESSION: str = ColumnNames.STUDY_ACCESSION
    OUTCOME: str = ColumnNames.OUTCOME
    EFO_ID: str = ColumnNames.EFO_ID
    # efo_id is the queried term; mapped_trait_* the term(s) the study or
    # association is actually annotated with (a child when CHILD_TRAITS)
    CHILD_TRAITS: str = ColumnNames.CHILD_TRAITS
    MAPPED_TRAIT_ID: str = ColumnNames.MAPPED_TRAIT_ID
    MAPPED_TRAIT: str = ColumnNames.MAPPED_TRAIT
    OUTCOME_DESC: str = "outcome_desc"
    TRAIT_LABEL: str = "trait_label"
    CHROM: str = ColumnNames.CHROM
    POS: str = "pos"
    RSID: str = "rsid"
    VARIANT_ID: str = "variant_id"
    EFFECT_ALLELE: str = "effect_allele"
    OTHER_ALLELE: str = "other_allele"
    EAF: str = "eaf"
    MAF: str = ColumnNames.MAF
    MAF_STATUS: str = "maf_status"
    BETA: str = "beta"
    SE: str = "se"
    ODDS_RATIO: str = "odds_ratio"
    P_VALUE: str = ColumnNames.P_VALUE
    NEG_LOG10_P: str = "neg_log10_p"
    N: str = "n"
    DISEASE_ID: str = "disease_id"
    GENE_BURDEN_SCORE: str = "gene_burden_score"
    CORE_ORDER: tuple[str, ...] = (
        GENE,
        SOURCE,
        SOURCE_DB,
        STUDY_ACCESSION,
        OUTCOME,
        EFO_ID,
        CHILD_TRAITS,
        MAPPED_TRAIT_ID,
        MAPPED_TRAIT,
        OUTCOME_DESC,
        TRAIT_LABEL,
        CHROM,
        POS,
        RSID,
        VARIANT_ID,
        EFFECT_ALLELE,
        OTHER_ALLELE,
        EAF,
        MAF,
        MAF_STATUS,
        BETA,
        SE,
        ODDS_RATIO,
        P_VALUE,
        NEG_LOG10_P,
        N,
        DISEASE_ID,
        GENE_BURDEN_SCORE,
    )
    # set by the pipeline itself (not source data): copied through as-is
    # and not duplicated as `src_*` columns
    IDENTITY_COLUMNS: tuple[str, ...] = (
        GENE,
        SOURCE,
        SOURCE_DB,
        STUDY_ACCESSION,
        OUTCOME,
        EFO_ID,
        CHILD_TRAITS,
        MAPPED_TRAIT_ID,
        MAPPED_TRAIT,
        OUTCOME_DESC,
        TRAIT_LABEL,
    )
    # core columns converted to numbers (unparseable values become NA)
    NUMERIC_COLUMNS: tuple[str, ...] = (
        POS,
        EAF,
        MAF,
        BETA,
        SE,
        ODDS_RATIO,
        P_VALUE,
        NEG_LOG10_P,
        N,
        GENE_BURDEN_SCORE,
    )
    RAW_PREFIX: str = "src_"


class SourceColumnMaps:
    """Per-source mapping of core column -> original column name.

    Core columns not listed for a source are left NA (or derived, see
    `functions.harmonise_frame`). Curated GWAS Catalog records need extra
    parsing (locations, allele strings, text betas), done in
    `functions.harmonise_curated`.
    """
    GWAS_CATALOG: dict[str, str] = {
        HarmonisedColumns.CHROM: "chromosome",
        HarmonisedColumns.POS: "base_pair_location",
        HarmonisedColumns.RSID: "rsid",
        HarmonisedColumns.VARIANT_ID: "variant_id",
        HarmonisedColumns.EFFECT_ALLELE: "effect_allele",
        HarmonisedColumns.OTHER_ALLELE: "other_allele",
        HarmonisedColumns.EAF: "effect_allele_frequency",
        HarmonisedColumns.BETA: "beta",
        HarmonisedColumns.SE: "standard_error",
        HarmonisedColumns.ODDS_RATIO: "odds_ratio",
        HarmonisedColumns.P_VALUE: "p_value",
        HarmonisedColumns.NEG_LOG10_P: "neg_log_10_p_value",
        HarmonisedColumns.N: "n",
    }
    FINNGEN: dict[str, str] = {
        HarmonisedColumns.CHROM: "chrom",
        HarmonisedColumns.POS: "pos",
        HarmonisedColumns.RSID: "rsids",
        HarmonisedColumns.EFFECT_ALLELE: "alt",
        HarmonisedColumns.OTHER_ALLELE: "ref",
        HarmonisedColumns.EAF: "af_alt",
        HarmonisedColumns.BETA: "beta",
        HarmonisedColumns.SE: "sebeta",
        HarmonisedColumns.P_VALUE: "pval",
        HarmonisedColumns.NEG_LOG10_P: "mlogp",
    }
    CURATED: dict[str, str] = {
        HarmonisedColumns.STUDY_ACCESSION: "accession_id",
    }
    GENE_BURDEN: dict[str, str] = {
        HarmonisedColumns.STUDY_ACCESSION: "studyId",
        HarmonisedColumns.MAPPED_TRAIT_ID: "disease_id",
        HarmonisedColumns.MAPPED_TRAIT: "disease_name",
        HarmonisedColumns.TRAIT_LABEL: "disease_name",
        HarmonisedColumns.BETA: "beta",
        HarmonisedColumns.ODDS_RATIO: "oddsRatio",
        HarmonisedColumns.P_VALUE: "p_value",
        HarmonisedColumns.NEG_LOG10_P: "neg_log10_p",
        HarmonisedColumns.N: "studySampleSize",
        HarmonisedColumns.DISEASE_ID: "disease_id",
        HarmonisedColumns.GENE_BURDEN_SCORE: "score",
    }


class MafStatus:
    """Values of the `maf_status` column."""
    NUMERIC: str = "numeric"
    NOT_REPORTED: str = "not_reported"


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
    STUDY_DISCOVERY_LOG: Path = Paths.DATA_TEMP / "study_discovery_log.tsv.gz"
    FINAL_RESULTS: Path = Paths.RESULTS_OUTPUT / "final_results.tsv.gz"
