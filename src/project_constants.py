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
    # gzipped JSON per Ensembl overlap window / rsid lookup; delete a file
    # to refetch it
    ENSEMBL_CACHE: Path = DATA_TEMP / "ensembl_cache"
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
    # REST v2 page-size maximum; the default (20) hits biomed-api's
    # 500-page cap (10k records) for large traits
    GWAS_CATALOG_PAGE_SIZE: int = 500
    # seconds slept before each retry of a failed (5xx/timeout) REST call
    HTTP_RETRY_BACKOFF: tuple[int, ...] = (30, 60, 120)
    GWAS_CATALOG_FTP_BASE: str = (
        "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics"
    )
    OPEN_TARGETS_GRAPHQL_URL: str = (
        "https://api.platform.opentargets.org/api/v4/graphql"
    )
    OPEN_TARGETS_PAGE_SIZE: int = 1000
    # extra Open Targets disease IDs queried alongside an outcome ID; none
    # needed currently
    OPEN_TARGETS_EXTRA_DISEASE_IDS: dict[str, tuple[str, ...]] = {}
    # outcome -> efo_id applied in memory over icd_codes.txt (never written
    # back, so the raw file stays as-is), for outcomes whose resolved
    # efo_id is the wrong term; none needed currently
    OUTCOME_EFO_OVERRIDES: dict[str, str] = {}
    # GWAS Catalog studies whose disease_trait matches this (case-
    # insensitive) are copy-number-variant association models, not SNP
    # GWAS; the REST API has no CNV flag, unlike gxe/gxg
    CNV_TRAIT_PATTERN: str = r"\bCNV\b|copy[- ]number"
    # disease_trait of X-chromosome-only analyses (e.g. "(r-XCI
    # inactivation)"); no gene in gene_list.txt is on X, so they can
    # never return rows
    X_CHROM_TRAIT_PATTERN: str = r"\bXCI\b|X[- ]chromosom|\bXWAS\b"
    # written to a gene-table cell that was looked up but not found;
    # treated as resolved on reruns (clear the cell by hand to retry)
    NA_STRING: str = "NA"
    UNIPROT_HUMAN_TAXON: int = 9606
    # gene regions are fetched from Ensembl overlap/region in windows of
    # this size: ~1.3 variant records per bp, so ~6.5k records per call
    ENSEMBL_OVERLAP_WINDOW_BP: int = 5_000
    # a study is warned about when more than this fraction of its rows is
    # not_found/mismatch against Ensembl (e.g. a GRCh37 file)
    ENSEMBL_BAD_FRACTION_WARN: float = 0.5
    # ... but only when it has at least this many variant rows
    ENSEMBL_BAD_MIN_ROWS: int = 20
    # per-gene variant lists (external, not written by this pipeline)
    VARIANT_LIST_GLOB: str = "*_variants.tsv"
    # variant-list sources not matched to GWAS lookups (AlphaMissense)
    EXCLUDED_VARIANT_SOURCES: frozenset[str] = frozenset({"AM"})
    # GWAS result sources with single variants (gene-burden has none)
    VARIANT_LEVEL_SOURCES: tuple[str, ...] = ("summary-stats", "curated")
    # variant-list source flipped in the meta-analysis so the a1 allele's
    # effect is reported
    GOF_VARIANT_SOURCE: str = "GoF"
    # meta-analysis dedupe: per study/outcome/variant the first source here
    # is kept (rows from other sources go last)
    GWAS_SOURCE_PREFERENCE: tuple[str, ...] = ("summary-stats", "curated")


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
    MATCH_VARIANTS: int = 40
    META_ANALYSIS: int = 50


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
    # canonical chrom:pos:other_allele:effect_allele; the source's own ID
    # is kept as src_variant_id
    VARIANT_ID: str = "variant_id"
    # True for rows sharing source/study/outcome/gene/variant_id (e.g. two
    # source variants harmonised to the same site)
    DUPLICATE_VARIANT: str = "duplicate_variant"
    # GRCh38 chrom:pos:ref:alt of the matching Ensembl variant (alts joined
    # with "/" when the row's allele does not pick one); NA if not found
    ENSEMBL_VARIANT_ID: str = "ensembl_variant_id"
    # row alleles vs Ensembl alleles, see `EnsemblAlleleCheck`
    ENSEMBL_ALLELE_CHECK: str = "ensembl_allele_check"
    # row rsid vs Ensembl rsid, see `EnsemblRsidCheck`
    ENSEMBL_RSID_CHECK: str = "ensembl_rsid_check"
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
        DUPLICATE_VARIANT,
        ENSEMBL_VARIANT_ID,
        ENSEMBL_ALLELE_CHECK,
        ENSEMBL_RSID_CHECK,
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


class VariantListColumns:
    """Columns of the per-gene `*_variants.tsv` lists and the columns
    `match_variants.py` adds to the matched GWAS rows.

    `A1` is taken to be the GRCh38 reference allele and `A2` the
    alternate allele.
    """
    CHROM: str = "chr"
    POS: str = "pos"
    A1: str = "a1"
    A2: str = "a2"
    SOURCE: str = "source"
    GENE: str = "gene"
    TRI_CLASS: str = "tri_class"
    # added to the matched output, after the final-results columns
    OUT_SOURCE: str = "variant_list_source"
    OUT_GENE: str = "variant_list_gene"
    OUT_A1: str = "variant_list_a1"
    OUT_A2: str = "variant_list_a2"
    OUT_TRI_CLASS: str = "variant_list_tri_class"
    # "a2" or "a1": which list allele is the GWAS effect allele
    EFFECT_ALLELE_IS: str = "effect_allele_is"
    # "both" (effect + other allele) or "effect_only" (curated rows)
    MATCH_ALLELES: str = "match_alleles"


class MetaColumns:
    """Columns derived and written by `meta_analysis.py`, and the named
    groupings it can pool by.
    """
    # per matched row
    # chrom:pos:a1:a2 of the variant-list entry (chrom without "chr")
    VARIANT_SITE: str = "variant_site"
    # beta, or log(odds_ratio) when beta is missing
    BETA_USED: str = "beta_used"
    # "beta" or "log_or": where BETA_USED came from
    EFFECT_SCALE: str = "effect_scale"
    # se, or |beta| / z(p) when se is missing
    SE_USED: str = "se_used"
    SE_DERIVED: str = "se_derived"
    # BETA_USED for the a2 allele
    BETA_A2: str = "beta_a2"
    # BETA_A2 for ORIENTED_ALLELE
    BETA_ORIENTED: str = "beta_oriented"
    # "a2" or "a2_gof_flipped", see `Orientation`
    ORIENTATION: str = "orientation"
    ORIENTED_ALLELE: str = "oriented_allele"
    # per pooled group
    # estimates pooled (k) and the distinct studies among them
    N_ESTIMATES: str = "n_estimates"
    N_STUDIES: str = "n_studies"
    STUDIES: str = "studies"
    # accessions dropped because their (beta, se) copies a kept estimate
    COPIED_STUDIES: str = "copied_studies"
    N_SE_DERIVED: str = "n_se_derived"
    BETA: str = "meta_beta"
    SE: str = "meta_se"
    Z: str = "meta_z"
    P: str = "meta_p"
    # Cochran's Q, its degrees of freedom (k - 1) and I^2; NA when k = 1
    Q: str = "q"
    Q_DF: str = "q_df"
    I2: str = "i2"
    # grouping name -> columns pooled over (one output file per grouping);
    # add an entry, e.g. ("variant_list_gene", "variant_list_source",
    # "outcome"), to pool at another level
    GROUPINGS: dict[str, tuple[str, ...]] = {
        "variant": (VARIANT_SITE, HarmonisedColumns.OUTCOME),
    }
    DEFAULT_GROUPING: str = "variant"
    # unique values joined with ";" per group in the output
    DESCRIBE_COLUMNS: tuple[str, ...] = (
        VariantListColumns.OUT_GENE,
        VariantListColumns.OUT_SOURCE,
        VariantListColumns.OUT_TRI_CLASS,
        HarmonisedColumns.RSID,
        ORIENTED_ALLELE,
        ORIENTATION,
        EFFECT_SCALE,
        HarmonisedColumns.SOURCE,
    )


class Orientation:
    """Values of the `orientation` column."""
    # effect of the a2 (alt) allele
    A2: str = "a2"
    # GoF-listed variant: effect of the a1 allele
    A2_GOF_FLIPPED: str = "a2_gof_flipped"


class EnsemblAlleleCheck:
    """Values of the `ensembl_allele_check` column.

    Ensembl ref is the first allele of the Ensembl record. Rows with only
    one allele (curated: effect allele only) are `match` when it is an
    Ensembl alt and `flipped` when it is the ref.
    """
    # other allele = Ensembl ref, effect allele = an Ensembl alt
    MATCH: str = "match"
    # effect allele = Ensembl ref, other allele = an Ensembl alt
    FLIPPED: str = "flipped"
    # match/flipped only after complementing the row's alleles
    STRAND_FLIP: str = "strand_flip"
    # Ensembl variant found, but the row has no allele (curated "?")
    EFFECT_UNKNOWN: str = "effect_unknown"
    # Ensembl variant found, row alleles not among its alleles
    MISMATCH: str = "mismatch"
    # no Ensembl variant at chrom:pos (nor via the row's rsid)
    NOT_FOUND: str = "not_found"


class EnsemblRsidCheck:
    """Values of the `ensembl_rsid_check` column (NA when not found)."""
    # the row's rsid is the matched Ensembl variant's id
    SAME: str = "same"
    # matched by position, but the row's rsid differs (e.g. merged rsid)
    DIFFERENT: str = "different"
    # matched by position; the row has no rsid
    NO_SOURCE_RSID: str = "no_source_rsid"
    # nothing at chrom:pos; matched via the row's rsid at another position
    RSID_ONLY: str = "rsid_only"


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
    # (study, outcome) labels for the per-study filter outfiles
    STUDY_OUTCOMES_FILE: Path = Paths.DATA_TEMP / "study_outcomes.tsv"
    # flanked gene regions, frozen at prep time for the filter tasks
    GENE_REGIONS_FILE: Path = Paths.DATA_TEMP / "gene_regions.tsv"
    STUDY_DISCOVERY_LOG: Path = Paths.DATA_TEMP / "study_discovery_log.tsv.gz"
    FINAL_RESULTS: Path = Paths.RESULTS_OUTPUT / "final_results.tsv.gz"
    # final-results rows matching a (non-AM) gene variant-list entry
    MATCHED_VARIANTS: Path = Paths.RESULTS_OUTPUT / "matched_variants.tsv.gz"
    # IVW meta-analysis per `MetaColumns.GROUPINGS` name
    META_ANALYSIS_TEMPLATE: str = "meta_{grouping}.tsv.gz"
