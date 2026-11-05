#!/usr/bin/env python3
"""
lipid_adem constants
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS

from __future__ import annotations
from pathlib import Path


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PATHS

class Paths:
    """Project paths, anchored to this file's location in the repo."""
    ## main repo paths
    HERE: Path = Path(__file__).resolve().parent.parent
    DATA_RAW: Path = HERE / "data" / "raw"
    DATA_TEMP: Path = HERE / "data" / "temp"
    DATA_PROC: Path = HERE / "data" / "processed"
    LOGS: Path = HERE / "logs"
    OUTPUT: Path = HERE / "results" / "output"
    FIGURES: Path = HERE / "results" / "figures"
    # subdir of figure `--out-dir` for figures not in `FigureNames.MAIN_FIGURES`
    FIGURES_SENSITIVITY: str = "sensitivity"
    # per-gene marvel result stores
    MARVEL_STORE: Path = HERE / "results" / "marvel"
    ## gwas pipeline paths
    GWAS_FILTERED: Path = DATA_TEMP / "gwas_filtered"
    # gzipped JSON per Ensembl overlap window / rsid lookup
    ENSEMBL_CACHE: Path = DATA_TEMP / "ensembl_cache"
    # must match `log_dir` in config/filter_task.cnf
    FILTER_TASK_LOGS: Path = HERE / "src" / "logs" / "filter_task_logs"
    ## burden directories
    BURDEN_CONFIG: Path = HERE / "config" / "marvel_burden"
    BURDEN_OUT: Path = HERE / "results" / "marvel_burden"
    # MARVELous chunks, burden, per-variant extract/associate outputs
    MARVEL_RUN: Path = DATA_TEMP / "marvel"
    ## archived result directories
    ARCHIVE: Path = HERE / "results" / "archive"
    README_TEXT: Path = HERE / "config" / "results_readmes"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EFFECT SCALES

class EffectScale:
    """Scale of a study's betas for a binary outcome."""
    # logistic regression (SAIGE, REGENIE with Firth, PLINK, GLM-Binom)
    LOG_OR: str = "log_or"
    # linear model on a 0/1 outcome (BOLT-LMM, linear REGENIE, OLS)
    LINEAR: str = "linear"
    # Cox regression
    LOG_HR: str = "log_hr"
    UNKNOWN: str = "unknown"
    # the metadata (or marvel method) and the inference disagree
    CONFLICT: str = "conflict"
    CODES: frozenset[str] = frozenset(
        {LOG_OR, LINEAR, LOG_HR, UNKNOWN, CONFLICT}
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS

class Const:
    """General constants."""
    GRCH_BUILD: str = "GRCh38"
    # missing-value string in written tables
    NA: str = "NA"
    # bp added to both sides of a gene's coordinates
    GENE_FLANK_BP: int = 10_000
    # continuous outcomes (linear effects, not log-OR)
    LIPID_OUTCOMES: tuple[str, ...] = ("ldl_c", "apob", "hdl_c", "apoa", "tg")
    # genes dropped from meta-analysis and figures (APOE: tables pre-2026-10-08)
    EXCLUDED_GENES: tuple[str, ...] = ("APOE",)


class Ukb:
    """UK Biobank phenotype file (`FileNames.UKB_PHENO`) settings."""
    ID_COL: str = "f.eid"
    # genetic ancestry column and the values making up the EUR subset
    POP_COL: str = "population"
    EUR_POPS: tuple[str, ...] = ("eur_related", "eur_unrelated")


class Gwas:
    """GWAS study search, filtering and harmonisation settings."""
    # `None`: no MAF filter (see filter_gwas_cat.py)
    MAF_THR: float | None = None
    MAX_STUDIES_PER_OUTCOME: int = 10
    # overall ceiling per child-trait search, on top of the per-term cap
    MAX_STUDIES_PER_CHILD_QUERY: int = 30
    # trait IDs never searched (see gwas_cat_prep.py)
    EXCLUDED_EFO_IDS: frozenset[str] = frozenset({"MONDO_0011057"})
    # obsolete term -> replacement chain length followed before giving up
    MAX_REPLACEMENT_HOPS: int = 5
    # outcomes that also match GWAS Catalog child traits; others exact only
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
    # extra Open Targets disease IDs queried alongside an outcome ID
    OT_EXTRA_DISEASE_IDS: dict[str, tuple[str, ...]] = {}
    # outcome -> efo_id applied in memory when the resolved term is wrong
    OUTCOME_EFO_OVERRIDES: dict[str, str] = {}
    # warn about a study with this fraction/min rows not_found/mismatch
    ENSEMBL_BAD_FRAC_WARN: float = 0.5
    ENSEMBL_BAD_MIN_ROWS: int = 20
    # bp padding of a region's reference sequence for indel left-alignment
    INDEL_NORM_PAD_BP: int = 500
    # cohort key -> GWAS Catalog `cohort` tokens (lower case) it matches
    COHORT_ALIASES: dict[str, frozenset[str]] = {
        "finngen": frozenset({"finngen"}),
        "ukb": frozenset({"ukb", "ukbb", "uk biobank"}),
        "aou": frozenset({"aou", "all of us", "allofus"}),
    }
    # cohorts excluded from catalog studies for every outcome
    EXCLUDED_COHORTS: frozenset[str] = frozenset({"ukb", "aou"})
    # catalog reason prefix of a cohort-overlap exclusion, + cohort key
    COHORT_OVERLAP_REASON_PREFIX: str = "cohort_overlap_"
    # catalog reason prefix of a study_outcome_review.tsv exclusion
    REVIEW_REASON_PREFIX: str = "review_"
    # study_outcome_review.tsv `status` acted on; other values are ignored
    REVIEW_EXCLUDE_STATUS: str = "exclude"
    # effect-scale inference cut-off (see `functions.infer_effect_scales`)
    EFFECT_SCALE_CUTOFF: float = 1.0
    EFFECT_SCALE_MIN_MAF: float = 0.01
    # fewer usable variants than this: inferred scale unknown
    EFFECT_SCALE_MIN_VARIANTS: int = 20
    # GWAS-SSF `analysis_software` (lower-case substring) -> `EffectScale`
    SOFTWARE_SCALE: dict[str, str] = {
        "saige": EffectScale.LOG_OR,
        "plink": EffectScale.LOG_OR,
        "snptest": EffectScale.LOG_OR,
        "bolt": EffectScale.LINEAR,
        "fastgwa": EffectScale.LINEAR,
    }
    # GWAS-SSF `effect_statistic` (lower case) -> `EffectScale`
    STATISTIC_SCALE: dict[str, str] = {
        "odds_ratio": EffectScale.LOG_OR,
        "hazard_ratio": EffectScale.LOG_HR,
    }
    # FinnGen R13 binary endpoints: REGENIE with Firth correction
    FINNGEN_SCALE: str = EffectScale.LOG_OR


class Api:
    """External API endpoints and request settings."""
    # seconds slept before each retry of a failed (5xx/timeout) REST call
    RETRY_BACKOFF: tuple[int, ...] = (30, 60, 120)
    NCBI_ESUMMARY: str = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    )
    OLS_SEARCH: str = "https://www.ebi.ac.uk/ols/api/search"
    # term lookup by obo_id; also serves MONDO terms imported into EFO
    OLS_TERMS: str = "https://www.ebi.ac.uk/ols4/api/ontologies/efo/terms"
    GWAS_CATALOG: str = "https://www.ebi.ac.uk/gwas/rest/api/v2"
    GWAS_CATALOG_FTP: str = (
        "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics"
    )
    OPEN_TARGETS: str = "https://api.platform.opentargets.org/api/v4/graphql"
    UNIPROT_HUMAN_TAXON: int = 9606
    # Ensembl overlap/region window (~6.5k variant records per call)
    ENSEMBL_WINDOW_BP: int = 5_000
    PUBMED_BATCH_SIZE: int = 200
    # 200 recommended: 20 hits biomed-api's page cap, 500 its 60 s timeout
    GWAS_CATALOG_PAGE_SIZE: int = 200
    OPEN_TARGETS_PAGE_SIZE: int = 1000


class Regex:
    """Regular expression patterns (compiled where used)."""
    ICD10_CODE: str = r"^[A-Z]\d{2}$"
    EFO_ID: str = r"^EFO[:_]\d+$"
    # CNV studies, excluded from GWAS Catalog results
    CNV_TRAIT: str = r"\bCNV\b|copy[- ]number"
    # X-chromosome studies, excluded from GWAS Catalog results
    X_CHROM_TRAIT: str = r"\bXCI\b|X[- ]chromosom|\bXWAS\b"
    # separators between cohorts in a GWAS Catalog `cohort` cell
    COHORT_SPLIT: str = r"[;|,]"
    # marvel `Exposure` of a single variant (chr:pos:a1:a2, a2 counted)
    MARVEL_VARIANT: str = (
        r"^(?:chr)?(?P<chrom>[0-9XYMT]+):(?P<pos>\d+):"
        r"(?P<a1>[ACGT]+):(?P<a2>[ACGT]+)$"
    )
    # marvel `Exposure` of a gene carrier mask, e.g. "CETP PTV" or "CETP_lof"
    MARVEL_GENE_MASK: str = r"^(?P<gene>[^\s_]+)(?:\s+|_)(?P<mask>\S.*)$"
    # sumstats effect allele of a gene-burden mask row, e.g. "M1.0001"
    BURDEN_MASK_ALLELE: str = r"^M\d+\.(?:\d+|singleton)$"
    # `Name` of a burden mask row, e.g. "PCSK9(ENSG00000169174).GENE.M1.01"
    BURDEN_NAME: str = (
        r"^(?P<gene>[^(]+)\((?P<ensembl_id>ENSG\d+)\)\.GENE\.(?P<mask>.+)$"
    )


class VariantSource:
    """Variant-list and GWAS result sources, and their annotation filters."""
    # GWAS result sources with single variants
    VARIANT_LEVEL: tuple[str, ...] = ("summary-stats", "curated")
    # Open Targets gene burden
    GENE_BURDEN: str = "gene-burden"
    # GoF variants, flipped in meta-analysis so the a1 effect is reported
    GOF: str = "GoF"
    # single GoF variants reported one by one (`FileNames.SELECTED_VARIANTS`)
    SELECTED_GOF: str = "SelectedGoF"
    # ClinVar P/LP (`FileNames.PLP_VARIANTS`)
    CLINVAR: str = "ClinVar"
    # VEP/LOFTEE PTVs (`FileNames.PTV_VARIANTS`)
    PTV: str = "PTV"
    # AlphaMissense missense (`FileNames.AM_VARIANTS`)
    AM: str = "AM"
    LOFTEE_KEEP: str = "HC"
    VEP_CANONICAL: str = "YES"
    AM_KEEP_CLASSES: tuple[str, ...] = ("Pathogenic/Likely pathogenic",)


class ClinVar:
    """ClinVar P/LP selection settings."""
    # assembly suffix of the P/LP coordinate columns used for matching
    ASSEMBLY_SUFFIX: str = "_grch38"
    # `rcv_molecular_consequence` values making a P/LP variant `lowering`
    TRUNCATING_CONSEQUENCES: frozenset[str] = frozenset(
        {
            "frameshift variant",
            "nonsense",
            "splice acceptor variant",
            "splice donor variant",
        }
    )
    PATHOGENIC_CLASSES: frozenset[str] = frozenset(
        {"Pathogenic", "Likely pathogenic", "Pathogenic/Likely pathogenic"}
    )
    REVIEW_STATUS_CORE: str = "reviewed by expert panel"
    REVIEW_STATUS_ORDER: tuple[str, ...] = (
        "no assertion criteria provided",
        "criteria provided, single submitter",
        "criteria provided, multiple submitters, no conflicts",
    )


class Marvel:
    """MARVELous run and result settings."""
    # variant `ID` before normalisation is `variant_id` + this suffix
    ORIG_ID_SUFFIX: str = "_orig"
    # MNV stored by UKB as SNVs -> proxy SNV (docs/variant_matching.md)
    MNV_PROXIES: dict[str, str] = {
        "chr1:62597616:CC:GA": "chr1:62597616:C:G",
    }
    # ancestry-APOE stratum separator in `Stratification name`, e.g. EUR_e44
    ANCESTRY_SEP: str = "_"
    # source_db of marvel rows, + cohort key
    SOURCE_DB_PREFIX: str = "marvel_"
    # `Stratification name` used when marvel_results.tsv leaves it blank
    DEFAULT_STRAT: str = "overall"
    # `Model` (regression method) -> `EffectScale`; others UNKNOWN
    METHOD_SCALE: dict[str, str] = {
        "GLM-Binom": EffectScale.LOG_OR,
        "OLS": EffectScale.LINEAR,
        "Cox": EffectScale.LOG_HR,
    }
    # rows with fewer exposed (carriers) are dropped at merge
    MIN_CARRIERS: int = 5
    # rows with SE outside [MIN_SE, MAX_SE] are dropped at merge
    MIN_SE: float = 1e-6
    MAX_SE: float = 30.0
    # UKB `Variable` -> `outcome`; other variables are left out
    UKB_OUTCOMES: dict[str, str] = {
        "all_cause_dementia_combined": "all_cause_dementia",
        "alzheimers_disease_combined": "alzheimers_dementia",
        "vascular_dementia_algo": "vascular_dementia",
        "frontotemporal_dementia_algo": "frontotemporal_dementia",
        "ascvd_ii": "ascvd",
        "Apolipoprotein A_i0": "apoa",
        "Apolipoprotein B_i0": "apob",
        "HDL cholesterol_i0": "hdl_c",
        "LDL direct_i0": "ldl_c",
        "Triglycerides_i0": "tg",
    }
    # `Model name` of the main analysis
    DEFAULT_MODEL: str = "model_3"
    # old (cnf) `Model name` -> new (TOML) `covariate_model`
    MODEL_MAP: dict[str, str] = {
        "model_1": "unadjusted",
        "model_3": "adjusted",
    }
    # dosage above this is a carrier (config/marvel_config.toml)
    CARRIER_THR: float = 0.5
    # rows per chunk when streaming an old wide carriers file
    OLD_CARRIERS_CHUNK_ROWS: int = 50_000


class Burden:
    """UKB carrier burden masks and runs (burden_exposure.py)."""
    MASK_LOF: str = "lof"
    MASK_LOF_DIRECTED: str = "lof_directed"
    MASK_GOF: str = "gof"
    # mask -> its variant-list sources, in plotting order
    VARIANT_SETS: dict[str, tuple[str, ...]] = {
        "gof": (VariantSource.GOF,),
        "am": (VariantSource.AM,),
        "ptv": (VariantSource.PTV,),
        "clinvar": (VariantSource.CLINVAR,),
        "lof": (VariantSource.PTV, VariantSource.CLINVAR),
        "ptv_am": (VariantSource.PTV, VariantSource.AM),
        "am_clinvar": (VariantSource.AM, VariantSource.CLINVAR),
        "ptv_clinvar_am": (
            VariantSource.PTV, VariantSource.CLINVAR, VariantSource.AM,
        ),
    }
    # mask -> its directed form (ClinVar-only sites without lowering dropped)
    DIRECTED_MASKS: dict[str, str] = {
        "clinvar": "clinvar_directed",
        MASK_LOF: MASK_LOF_DIRECTED,
        "am_clinvar": "am_clinvar_directed",
        "ptv_clinvar_am": "ptv_clinvar_am_directed",
    }
    # mask suffix and outcome of the fallback exposures (`--prefer-groups`)
    FALLBACK_SUFFIX: str = "_fb"
    FALLBACK_OUTCOME: str = "alzheimers_dementia"
    # Thomassen et al. 2026 APOE-stratum AD GWAS (src/lipid_adem.sh)
    PREFER_STUDIES: tuple[str, ...] = (
        "GCST90861026",
        "GCST90861027",
        "GCST90861029",
        "GCST90861030",
    )
    # above this carrier fraction a column counts the other allele
    SWAP_FRAC: float = 0.5
    # default `--max-maf`: 0.5 keeps every listed site
    MAX_MAF: float = 0.5
    # covariate models of the burden cnfs (`Marvel.MODEL_MAP` keys)
    MODELS: dict[str, tuple[str, ...]] = {
        "model_1": (),
        "model_3": ("Sex", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6"),
    }
    # UKB subsets of the burden runs (create_config.py names)
    SUBSETS: tuple[str, ...] = ("all_apoe", "eur")


class Apoe:
    """APOE genotype settings."""
    # genotype column of `FileNames.UKB_PHENO`
    UKB_COL: str = "genotype"
    # prefix of the carrier columns of `FileNames.APOE_EXPOSURE`
    DIPLOTYPE_PREFIX: str = "APOE_"
    # `UKB_COL` values meaning "no genotype", excluded
    MISSING_VALUES: tuple[str, ...] = ("Unknown",)
    # every real genotype `UKB_COL` may hold
    GENOTYPES: tuple[str, ...] = (
        "e2e2",
        "e2e3",
        "e2e4",
        "e3e3",
        "e3e4",
        "e4e4",
    )
    # file label of the meta-analysis pooled per APOE stratum
    STRATA_LABEL: str = "apoe_strata"


class ApoeStratum:
    """Values of `apoe_stratum` (`FileNames.APOE_STRATA`, marvel table).

    The strata follow Thomassen et al. 2026; e42 carriers are in none.
    """
    E44: str = "e44"
    E43: str = "e43"
    E33: str = "e33"
    E22_E32: str = "e22_e32"
    # an unstratified run (all APOE genotypes)
    ALL: str = "all"
    CODES: frozenset[str] = frozenset({E44, E43, E33, E22_E32})
    # stratum -> `Apoe.UKB_COL` values in it (UKB marvel
    # runs, create_config.py); e2e4 is in none
    GENOTYPES: dict[str, tuple[str, ...]] = {
        E44: ("e4e4",),
        E43: ("e3e4",),
        E33: ("e3e3",),
        E22_E32: ("e2e2", "e2e3"),
    }


class Meta:
    """Meta-analysis deduplication preferences (first listed is kept)."""
    GWAS_SOURCE_PREF: tuple[str, ...] = ("summary-stats", "curated")
    # tie-break after `GWAS_SOURCE_PREF`
    SOURCE_DB_PREF: tuple[str, ...] = (
        "manual",
        "finngen",
        "marvel_aou",
        "marvel_ukb",
        "gwas_catalog",
    )


class RunlogOrder:
    """RUN_LOG.md section order per pipeline step.

    Explicit because each step runs in its own process tree (qsub,
    pyjasub, `mamba run`), so log_tools' PPID-based auto-order would
    give every step 10. The Bash job wrappers hard-code the same values
    in `RUNLOG_ORDER` and must be kept in sync.
    """
    APOE_EXPOSURE: int = 5
    GWAS_CAT_PREP: int = 10
    FILTER_GWAS_CAT: int = 20
    BURDEN_EXPOSURE: int = 22
    MARVEL_RESULTS_TABLE: int = 25
    COMPARE_MARVEL_RUNS: int = 27
    MERGE_ASSOCIATIONS: int = 30
    MATCH_VARIANTS: int = 40
    META_ANALYSIS: int = 50
    ARCHIVE_RESULTS: int = 90


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# COLUMN NAMES

class ColumnNames:
    """Column names shared across pipeline tables."""
    ROWIDX: str = "rowidx"
    OUTFILE: str = "outfile"
    GENE: str = "gene"
    OUTCOME: str = "outcome"
    SOURCE: str = "source"
    SOURCE_DB: str = "source_db"
    STATUS: str = "status"
    REASON: str = "reason"
    NOTE: str = "note"
    CHROM: str = "chrom"
    START: str = "start"
    END: str = "end"
    STUDY_ACCESSION: str = "study_accession"
    ANCESTRY: str = "ancestry"
    # harmonised `Ancestry` code derived from ANCESTRY
    ANCESTRY_GROUP: str = "ancestry_group"
    # marvel_results.tsv: marvel `Stratification name` to keep
    STRATIFICATION: str = "stratification"
    P_VALUE: str = "p_value"
    MAF: str = "maf"


class GeneColumns:
    """Columns of the gene list and gene regions (`FileNames.GENE_LIST`)."""
    GENE_CHR: str = "chr"
    ENSEMBL_ID: str = "ensemblid"
    UNIPROT: str = "uniprot"
    # any one ID column is enough as input (see `resolve_gene_table`)
    GENE_ID_COLUMNS: tuple[str, ...] = (ColumnNames.GENE, ENSEMBL_ID, UNIPROT)
    GENE_TABLE_COLUMNS: tuple[str, ...] = (
        ColumnNames.GENE,
        GENE_CHR,
        ColumnNames.START,
        ColumnNames.END,
        ENSEMBL_ID,
        UNIPROT,
    )


class OutcomeColumns:
    """Columns of the outcome list (icd_codes.txt) and its trait mapping."""
    ICD_CODE: str = "code"
    DESCRIPTION: str = "description"
    EFO_ID: str = "efo_id"
    FINNGEN_PHENOCODE: str = "finngen_phenocode"
    TRAIT: str = "trait"
    CHILD_TRAITS: str = "child_traits"
    MAPPED_TRAIT_ID: str = "mapped_trait_id"
    MAPPED_TRAIT: str = "mapped_trait"


class StudyColumns:
    """GWAS study metadata and effect-scale evidence columns."""
    PUBMED_ID: str = "pubmed_id"
    PUB_DATE: str = "pub_date"
    FIRST_AUTHOR: str = "first_author"
    JOURNAL: str = "journal"
    TITLE: str = "title"
    DISEASE_TRAIT: str = "disease_trait"
    SAMPLE_SIZE: str = "sample_size"
    COHORT: str = "cohort"
    # GWAS-SSF `-meta.yaml` fields and the `EffectScale` they imply
    EFFECT_STATISTIC: str = "effect_statistic"
    ANALYSIS_SOFTWARE: str = "analysis_software"
    EFFECT_SCALE_META: str = "effect_scale_meta"
    # `FileNames.STUDY_EFFECT_SCALE` evidence (`functions.infer_effect_scales`)
    EFFECT_SCALE_METHOD: str = "effect_scale_method"
    R_MEDIAN: str = "r_median"
    EFFECT_SCALE_INFERRED: str = "effect_scale_inferred"
    STUDY_EFFECT_SCALE: str = "study_effect_scale"


class ClinVarColumnNames:
    """ClinVar column names"""
    VCV_ACCESSION_COL: str = "vcv_accession"
    VARIATION_ID_COL: str = "variation_id"
    VARIATION_NAME_COL: str = "variation_name"
    GENE_SYMBOL_COL: str = "gene_symbol"
    CANONICAL_SPDI_COL: str = "canonical_spdi"
    ASSEMBLY_COL: str = "assembly"
    CHR_COL: str = GeneColumns.GENE_CHR
    START_COL: str = ColumnNames.START
    STOP_COL: str = "stop"
    POSITION_VCF_COL: str = "position_vcf"
    REFERENCE_ALLELE_COL: str = "reference_allele_vcf"
    ALTERNATE_ALLELE_COL: str = "alternate_allele_vcf"
    SUBMITTED_CLASSIFICATIONS_COL: str = "submitted_classifications"
    CLASSIFICATION_COUNT_COL: str = "classification_count"
    AC_CLASSIFICATION_COL: str = "ac_classification"
    AC_REVIEW_STATUS_COL: str = "ac_review_status"
    VARIANT_TYPE_COL: str = "variant_type"
    RCV_MOLECULAR_CONSEQUENCE_COL: str = "rcv_molecular_consequence"
    RCV_CONDITION_COL: str = "rcv_condition"
    RCV_CONDITION_DB_COL: str = "rcv_condition_db"
    RCV_CONDITION_ID_COL: str = "rcv_condition_id"
    RCV_CLASSIFICATION_COL: str = "rcv_classification"
    RCV_REVIEW_STATUS_COL: str = "rcv_review_status"


class HarmonisedColumns:
    """Core columns of the merged associations table, shared by every source.

    Each source's original columns are kept after the core ones, renamed
    to `RAW_PREFIX + <original name>` so they can never collide with a
    core name.
    """
    GENE: str = ColumnNames.GENE
    SOURCE: str = ColumnNames.SOURCE
    SOURCE_DB: str = ColumnNames.SOURCE_DB
    STUDY_ACCESSION: str = ColumnNames.STUDY_ACCESSION
    OUTCOME: str = ColumnNames.OUTCOME
    EFO_ID: str = OutcomeColumns.EFO_ID
    # efo_id is the queried term; mapped_trait_* the term(s) the study or
    # association is actually annotated with (a child when CHILD_TRAITS)
    CHILD_TRAITS: str = OutcomeColumns.CHILD_TRAITS
    MAPPED_TRAIT_ID: str = OutcomeColumns.MAPPED_TRAIT_ID
    MAPPED_TRAIT: str = OutcomeColumns.MAPPED_TRAIT
    OUTCOME_DESC: str = "outcome_desc"
    TRAIT_LABEL: str = "trait_label"
    # study ancestry as an `Ancestry` code
    ANCESTRY_GROUP: str = ColumnNames.ANCESTRY_GROUP
    # per-study `EffectScale`; set by the marvel loader, else at merge
    STUDY_EFFECT_SCALE: str = StudyColumns.STUDY_EFFECT_SCALE
    CHROM: str = ColumnNames.CHROM
    POS: str = "pos"
    RSID: str = "rsid"
    # canonical chrom:pos:other_allele:effect_allele, left-aligned and
    # trimmed against GRCh38 (see `NormStatus`); the source's own ID is
    # kept as src_variant_id
    VARIANT_ID: str = "variant_id"
    # VARIANT_ID before normalisation (source pos and alleles)
    VARIANT_ID_ORIG: str = "variant_id_orig"
    # outcome of the normalisation, see `NormStatus`
    NORM_STATUS: str = "norm_status"
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
        ANCESTRY_GROUP,
        STUDY_EFFECT_SCALE,
        CHROM,
        POS,
        RSID,
        VARIANT_ID,
        VARIANT_ID_ORIG,
        NORM_STATUS,
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
        ANCESTRY_GROUP,
        STUDY_EFFECT_SCALE,
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
    # chrom/pos/alleles are parsed from `Exposure` in
    # `merge_associations.load_marvel_results` (effect = a2)
    MARVEL: dict[str, str] = {
        HarmonisedColumns.BETA: "Point Estimates",
        HarmonisedColumns.SE: "Standard Error",
        HarmonisedColumns.P_VALUE: "P-values",
        HarmonisedColumns.N: "Samples",
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
    AM_PATHOGENICITY: str = "am_pathogenicity"
    TRI_CLASS: str = "tri_class"
    # pos/a1/a2 before normalisation, and its `NormStatus`
    POS_ORIG: str = "pos_orig"
    A1_ORIG: str = "a1_orig"
    A2_ORIG: str = "a2_orig"
    NORM_STATUS: str = "norm_status"
    # normalised ``chr:pos:a1:a2`` (combine_variants.py); the marvel
    # exposure name of the variant
    VARIANT_ID: str = "variant_id"
    # burden mask lists (burden_exposure.py --mask-lists): exposure name
    # ``<GENE>_<mask>[_fb]``, the new-marvel `category_column`
    MASK: str = "mask"
    # variant label column of the per-gene marvel extraction lists
    MARVEL_ID: str = "ID"
    # ClinVar P/LP rows only: a `ClinVarDirection` value (NA otherwise)
    CLINVAR_DIRECTION: str = "clinvar_direction"
    # `FileNames.SELECTED_VARIANTS` only: figure label (rsID / protein
    # change); not carried into the combined list
    NAME: str = "name"
    # added to the matched output, after the merged-associations columns
    OUT_SOURCE: str = "variant_list_source"
    OUT_GENE: str = "variant_list_gene"
    OUT_A1: str = "variant_list_a1"
    OUT_A2: str = "variant_list_a2"
    OUT_TRI_CLASS: str = "variant_list_tri_class"
    OUT_POS_ORIG: str = "variant_list_pos_orig"
    OUT_A1_ORIG: str = "variant_list_a1_orig"
    OUT_A2_ORIG: str = "variant_list_a2_orig"
    OUT_NORM_STATUS: str = "variant_list_norm_status"
    OUT_CLINVAR_DIRECTION: str = "variant_list_clinvar_direction"
    # "a2" or "a1": which list allele is the GWAS effect allele
    EFFECT_ALLELE_IS: str = "effect_allele_is"
    # "both" (effect + other allele) or "effect_only" (curated rows)
    MATCH_ALLELES: str = "match_alleles"


class VepCsqColumns:
    """Columns of `FileNames.VEP_CSQ` (header written by vep_extract.sh;
    the CSQ ones are the VEP/LOFTEE field names) and the extra columns of
    `FileNames.PTV_VARIANTS`.
    """
    CHROM: str = "chr"
    POS: str = "pos"
    REF: str = "ref"
    ALT: str = "alt"
    AF: str = "AF"
    AC: str = "AC"
    ALLELE: str = "Allele"
    CONSEQUENCE: str = "Consequence"
    IMPACT: str = "IMPACT"
    SYMBOL: str = "SYMBOL"
    GENE_ID: str = "Gene"
    FEATURE: str = "Feature"
    BIOTYPE: str = "BIOTYPE"
    CANONICAL: str = "CANONICAL"
    HGVSC: str = "HGVSc"
    HGVSP: str = "HGVSp"
    LOF: str = "LoF"
    LOF_FILTER: str = "LoF_filter"
    LOF_FLAGS: str = "LoF_flags"
    LOF_INFO: str = "LoF_info"
    # PTV_VARIANTS: the gene_list.txt symbol of the variant
    GENE: str = "gene"

class Ancestry:
    """Harmonised (gnomAD-style) ancestry codes, see
    `functions.harmonise_ancestry`.
    """
    EUR: str = "EUR"
    AFR: str = "AFR"
    AMR: str = "AMR"
    EAS: str = "EAS"
    # South and Central Asian
    CSA: str = "CSA"
    MID: str = "MID"
    OTH: str = "OTH"
    # more than one code, none with >= DOMINANT_FRACTION of the samples
    MULTI: str = "MULTI"
    # not reported
    NR: str = "NR"
    CODES: frozenset[str] = frozenset(
        {EUR, AFR, AMR, EAS, CSA, MID, OTH, MULTI, NR}
    )
    # share of a study's N one code needs to label a multi-ancestry study
    DOMINANT_FRACTION: float = 0.9
    # FinnGen is a Finnish (European) cohort
    FINNGEN: str = EUR
    # GWAS Catalog ancestral category (lower case) -> code; categories
    # not listed map to OTH (warned)
    CATEGORY_MAP: dict[str, str] = {
        "european": EUR,
        "african american or afro-caribbean": AFR,
        "sub-saharan african": AFR,
        "african unspecified": AFR,
        "hispanic or latin american": AMR,
        "native american": AMR,
        "east asian": EAS,
        "south east asian": EAS,
        "south asian": CSA,
        "central asian": CSA,
        "greater middle eastern (middle eastern, north african or persian)": (
            MID
        ),
        "greater middle eastern": MID,
        "asian unspecified": OTH,
        "oceanian": OTH,
        "other": OTH,
        "other admixed ancestry": OTH,
        "nr": NR,
    }
    # one `discovery_ancestry` segment: "<n> <categories> (<countries>)",
    # n and countries optional; countries may hold one nested "(...)"
    SEGMENT_PATTERN: str = r"""
        ^\s*
        (?:(?P<n>\d+|NA)\s+)?
        (?P<categories>.+?)
        (?:\s+\((?P<countries>(?:[^()]|\([^()]*\))*)\))?
        \s*$
    """
    # comma between categories, not inside "(...)"
    CATEGORY_SPLIT_PATTERN: str = r",\s*(?![^()]*\))"


class MetaColumns:
    """Columns derived and written by `meta_analysis.py`, and the columns
    it pools by.
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
    # BETA_A2 for ORIENTED_ALLELE: lower gene function, then flipped for
    # `TherapyDirection.RAISING` genes (therapeutic direction)
    BETA_ORIENTED: str = "beta_oriented"
    # "a2" or "a2_gof_flipped", see `Orientation`; the lower-function
    # step only, the therapy flip is in THERAPY_DIRECTION
    ORIENTATION: str = "orientation"
    ORIENTED_ALLELE: str = "oriented_allele"
    # the gene's `TherapyDirection` (`TherapyDirection.GENES`),
    # written to the meta-analysis and burden files: effects are in the
    # therapeutic direction (figure_utils.load_burden requires it)
    THERAPY_DIRECTION: str = "therapy_direction"
    # per pooled group
    # estimates pooled (k) and the distinct studies among them
    N_ESTIMATES: str = "n_estimates"
    N_STUDIES: str = "n_studies"
    STUDIES: str = "studies"
    # <accession>=<maf> pairs joined with ";" in the order of `studies`;
    # NA when the study reports no frequency
    STUDY_MAF: str = "study_maf"
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
    # "pooled" (over studies) or "stratum" (one study), see `MetaLevel`
    LEVEL: str = "level"
    # burden: distinct variants pooled and their sites (";"-joined)
    N_VARIANTS: str = "n_variants"
    VARIANTS: str = "variants"
    # per row, from `FileNames.APOE_STRATA`: an `ApoeStratum` value and
    # the group of studies (strata + unstratified run) it belongs to
    APOE_STRATUM: str = "apoe_stratum"
    STUDY_GROUP: str = "study_group"
    # columns pooled over; every run is restricted to one `Ancestry` code
    # (`--ancestry`), so one study's pooled and per-ancestry analyses are
    # never pooled together
    KEYS: tuple[str, ...] = (
        VARIANT_SITE,
        HarmonisedColumns.OUTCOME,
        HarmonisedColumns.ANCESTRY_GROUP,
    )
    # ancestry pooled when `--ancestry` is not given (FinnGen counts as
    # EUR, see `Ancestry.FINNGEN`)
    DEFAULT_ANCESTRY: str = Ancestry.EUR
    # unique values joined with ";" per group in the output
    DESCRIBE_COLUMNS: tuple[str, ...] = (
        HarmonisedColumns.ANCESTRY_GROUP,
        VariantListColumns.OUT_GENE,
        VariantListColumns.OUT_SOURCE,
        VariantListColumns.OUT_TRI_CLASS,
        VariantListColumns.OUT_CLINVAR_DIRECTION,
        STUDY_GROUP,
        APOE_STRATUM,
        HarmonisedColumns.RSID,
        ORIENTED_ALLELE,
        ORIENTATION,
        EFFECT_SCALE,
        HarmonisedColumns.STUDY_EFFECT_SCALE,
        HarmonisedColumns.SOURCE,
        HarmonisedColumns.TRAIT_LABEL,
    )


class MarvelColumns:
    """Columns of marvel `{exposure}_results.tsv.gz` files and of the
    per-gene stores built from them (`marvel_results_table.py`).
    """
    METHOD: str = "Model"
    MODEL_NAME: str = "Model name"
    STRATIFICATION_NAME: str = "Stratification name"
    VARIABLE: str = "Variable"
    EXPOSURE: str = "Exposure"
    CASES: str = "Cases"
    SAMPLES: str = "Samples"
    EXPOSED: str = "Exposed"
    NON_EXPOSED: str = "Non-exposed"
    ESTIMATE: str = "Point Estimates"
    SE: str = "Standard Error"
    P_VALUE: str = "P-values"
    # store only: name of the per-variant file a row was read from; marvel
    # names it after the tested exposure, so it tells apart the intercept
    # and covariate rows of different exposures' models
    RESULT_FILE: str = "result_file"
    # store only: full path of that file
    SOURCE_FILE: str = "source_file"
    # one analysis result: the same key in two files is the same analysis
    KEY: tuple[str, ...] = (
        RESULT_FILE,
        METHOD,
        MODEL_NAME,
        STRATIFICATION_NAME,
        VARIABLE,
        EXPOSURE,
    )
    # compared (as numbers) between rows with the same key
    VALUES: tuple[str, ...] = (
        CASES,
        SAMPLES,
        EXPOSED,
        NON_EXPOSED,
        ESTIMATE,
        SE,
        P_VALUE,
    )

class ConditionDirectionColumns:
    """Columns of `FileNames.CLINVAR_CONDITION_DIRECTION`."""
    GENE: str = "gene"
    CONDITION: str = "rcv_condition"
    DIRECTION: str = "direction"

class MarvelCompareColumns:
    """Columns of the compare_marvel_runs.py outputs. A variant key is
    ``chrom:pos:a1:a2`` without ``chr``, alleles upper case.
    """
    OLD_KEY: str = "old_key"
    NEW_KEY: str = "new_key"
    OLD_VARIANT: str = "old_variant"
    NEW_VARIANT: str = "new_variant"
    OLD_GENE: str = "old_gene"
    NEW_GENE: str = "new_gene"
    OLD_SOURCE: str = "old_source"
    NEW_SOURCE: str = "new_source"
    IN_OLD: str = "in_old_list"
    IN_NEW: str = "in_new_list"
    # how an old variant was found in the new list (`MATCH_*`)
    MATCH: str = "match"
    MATCH_EXACT: str = "exact"
    # old = the new variant's form before normalisation (`*_orig`)
    MATCH_ORIG: str = "orig"
    # old a1/a2 = new a2/a1: the counted allele differs, so carriers and
    # effects are not comparable as they are
    MATCH_SWAPPED: str = "swapped"
    MATCH_SWAPPED_ORIG: str = "swapped_orig"
    MATCH_NONE: str = "none"
    NEW_STATUS: str = "new_status"
    NEW_CHUNK: str = "new_chunk"
    NEW_N_CARRIERS: str = "new_n_carriers"
    NEW_N_MISSING: str = "new_n_missing"
    # max old `Exposed` over the overall model_1 rows of the store (NA in
    # most old rows: use the carriers comparison for counts)
    OLD_EXPOSED: str = "old_exposed"
    # carriers comparison, per old carriers column
    N_OLD_SAMPLES: str = "n_old_samples"
    N_NEW_SAMPLES: str = "n_new_samples"
    N_OLD_CARRIERS: str = "n_old_carriers"
    N_OLD_MISSING: str = "n_old_missing"
    N_BOTH: str = "n_both"
    # old carriers that are not carriers now, by reason (`LOST_*`)
    N_LOST: str = "n_lost"
    N_LOST_NON_CARRIER: str = "n_lost_non_carrier"
    N_LOST_MISSING: str = "n_lost_missing"
    N_LOST_NOT_SAMPLED: str = "n_lost_not_sampled"
    N_LOST_NOT_READ: str = "n_lost_not_read"
    # new carriers that were not old carriers
    N_GAINED: str = "n_gained"
    N_GAINED_OLD_MISSING: str = "n_gained_old_missing"
    N_GAINED_NOT_IN_OLD: str = "n_gained_not_in_old"
    LOST_REASON: str = "reason"
    LOST_NON_CARRIER: str = "non_carrier"
    LOST_MISSING: str = "missing"
    LOST_NOT_SAMPLED: str = "not_sampled"
    LOST_NOT_READ: str = "not_read"
    # results comparison
    STORE_GENE: str = "store_gene"
    OUTCOME: str = "outcome"
    MODEL: str = "covariate_model"
    OLD_PREFIX: str = "old_"
    NEW_PREFIX: str = "new_"
    CASES: str = "cases"
    SAMPLES: str = "samples"
    EXPOSED: str = "exposed"
    BETA: str = "beta"
    SE: str = "se"
    P: str = "p"
    BETA_DIFF: str = "beta_diff"
    # (new - old beta) / sqrt(old se^2 + new se^2); not a test, the runs
    # share most samples
    Z_DIFF: str = "z_diff"
    SAME_SIGN: str = "same_sign"
    NEW_REMARKS: str = "new_remarks"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VARIANT HANDLING

class MafStatus:
    """Values of the `maf_status` column."""
    NUMERIC: str = "numeric"
    NOT_REPORTED: str = "not_reported"

class NormStatus:
    """Values of the `norm_status` column (variant-list `norm_status` too)."""
    # pos and/or alleles changed to the left-aligned, trimmed form
    NORMALISED: str = "normalised"
    # already in normalised form (all SNVs, most indels)
    UNCHANGED: str = "unchanged"
    # neither allele matches the reference at pos, left as-is
    REF_MISMATCH: str = "ref_mismatch"
    # only one allele known (curated), left as-is
    EFFECT_ONLY: str = "effect_only"
    # no reference sequence covers the site (outside every gene region)
    NO_SEQUENCE: str = "no_sequence"
    # MNV replaced by its proxy SNV (`Marvel.MNV_PROXIES`); the MNV
    # stays in `pos_orig`/`a1_orig`/`a2_orig` (variant list only)
    MNV_PROXY: str = "mnv_proxy"

class Orientation:
    """Values of the `orientation` column."""
    # effect of the a2 (alt) allele
    A2: str = "a2"
    # GoF-listed (or selected GoF) variant: effect of the a1 allele
    A2_GOF_FLIPPED: str = "a2_gof_flipped"
    # ClinVar variant with a raising condition: effect of the a1 allele
    A2_CLINVAR_RAISING_FLIPPED: str = "a2_clinvar_raising_flipped"

class ClinVarDirection:
    """Values of `direction` in `FileNames.CLINVAR_CONDITION_DIRECTION`
    and of the per-variant `clinvar_direction` column.
    """
    # less gene product or function, LoF (e.g. FHBL, CETP deficiency, any
    # truncating variant)
    LOWERING: str = "lowering"
    # more gene function, GoF (PCSK9 familial hypercholesterolaemia)
    RAISING: str = "raising"
    # qualitatively changed protein, neither less nor more of it (e.g.
    # APOB p.Arg3527Gln, APOE type III, APOA1 amyloidosis)
    ALTERED: str = "altered"
    # per variant only: more than one of lowering/raising/altered
    CONFLICTING: str = "conflicting"
    # no lipid direction (e.g. 'not provided')
    UNKNOWN: str = "unknown"



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MARVEL

class MarvelRun:
    """File suffixes and columns of a MARVELous (TOML) run directory
    (`Paths.MARVEL_RUN`): extract writes ``<chunk>.<suffix>`` per
    genotype file, aggregate/associate ``<prefix>.<suffix>``.
    """
    CARRIERS_SUFFIX: str = ".carriers.tsv.gz"
    VARIANTS_SUFFIX: str = ".variants.tsv.gz"
    SAMPLES_SUFFIX: str = ".samples.tsv.gz"
    SENTINEL_SUFFIX: str = ".SUCCESS"
    RESULTS_SUFFIX: str = ".results.tsv.gz"
    # chunk carriers (long, sparse) and samples
    ID: str = "id"
    VARIANT: str = "variant"
    DOSAGE: str = "dosage"
    # chunk variant summary
    CHROM: str = "chrom"
    POS: str = "pos"
    REF: str = "ref"
    ALT: str = "alt"
    N_CARRIERS: str = "n_carriers"
    N_MISSING: str = "n_missing"
    STATUS: str = "status"
    # statuses whose genotypes were read
    READ_STATUS: tuple[str, ...] = ("found", "swapped")
    # association results
    EXPOSURE: str = "exposure"
    STRATUM: str = "stratum"
    COVARIATE_MODEL: str = "covariate_model"
    OUTCOME: str = "outcome"
    TEST: str = "test"
    TERM: str = "term"
    N_CASES: str = "n_cases"
    N_SAMPLES: str = "n_samples"
    N_EXPOSED: str = "n_exposed"
    ESTIMATE: str = "estimate"
    SE: str = "se"
    P_VALUE: str = "p_value"
    FORMATTED: str = "formatted"
    REMARKS: str = "remarks"
    OVERALL: str = "overall"
    # `FORMATTED` of the strata_ref reference row (term
    # ``<exposure>: <strata_ref>``, NA estimate, n_exposed = non-carriers)
    REFERENCE: str = "reference"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

class MetaLevel:
    """Values of the `level` column of the meta-analysis outputs."""
    # pooled over all studies of the run
    POOLED: str = "pooled"
    # one study (e.g. one APOE stratum of a stratified GWAS)
    STRATUM: str = "stratum"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OTHERS

class TherapyDirection:
    """How a gene's drugs change its function, per gene (`GENES`)."""
    # drugs lower gene function (inhibitors): effects kept as oriented
    LOWERING: str = "lowering"
    # drugs raise gene function: effects flipped by meta_analysis.py
    RAISING: str = "raising"
    GENES: dict[str, str] = {
        "CETP": LOWERING,     # CETP inhibitors (anacetrapib, obicetrapib)
        "HMGCR": LOWERING,    # statins
        "NPC1L1": LOWERING,   # ezetimibe
        "PCSK9": LOWERING,    # PCSK9 mAbs, inclisiran
        "ANGPTL3": LOWERING,  # evinacumab
        "APOB": LOWERING,     # mipomersen
        "PPARA": RAISING,     # fibrates (PPARα agonists)
        "APOA1": RAISING,     # ApoA-I infusion (CSL112)
    }


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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FILE NAMES

class FileNames:
    """File paths, built from `Paths` so they move together."""
    GENE_LIST: Path = Paths.DATA_RAW / "gene_list.txt"
    ICD_CODE_LIST: Path = Paths.DATA_RAW / "icd_codes.txt"
    EFO_UKB_MAPPING: Path = Paths.DATA_RAW / "efo_ukb_master_mapping.tsv"
    FINNGEN_MANIFEST: Path = Paths.DATA_RAW / "finngen_r13_manifest.tsv"
    GWAS_CATALOG_MANUAL_STUDIES: Path = (
        Paths.DATA_RAW / "gwas_catalog_manual_studies.tsv"
    )
    CLINVAR_VARIANTS: Path = Paths.DATA_RAW / "clinvar_variants.tsv"
    VARIANTS_REVIEW_STATUS_SUMMARY: Path = (
        Paths.DATA_PROC / "pah_variants_review_status_summary.tsv"
    )
    PLP_VARIANTS: Path = Paths.DATA_PROC / "plp_variants.tsv"
    # VEP/LOFTEE consequences of the gene_list.txt genes, one row per
    # variant x transcript (vep_extract.sh, Snellius; has UKB AF/AC, so
    # never committed)
    VEP_CSQ: Path = Paths.DATA_TEMP / "vep_lipid_gene_csq.tsv.gz"
    # LOFTEE HC PTVs on the canonical transcript (annotate_ptv.py; has UKB
    # AF/AC, so never committed)
    PTV_VARIANTS: Path = Paths.DATA_PROC / "ptv_variants.tsv.gz"
    # PTV + ClinVar P/LP + GoF variant list, all genes (combine_variants.py;
    # sites only, committed, normalised) and its per-gene marvel
    # extraction lists (`str.format(gene=...)`; normalised and original
    # forms, docs/rap_carrier_extraction.md)
    LIPID_VARIANTS: Path = Paths.DATA_PROC / "lipid_variants.tsv"
    # GoF rows of the old per-gene lists (`GOF_VARIANT_SOURCE`; snapshot
    # before combine_variants.py overwrote them; sites only, committed)
    GOF_VARIANTS: Path = Paths.DATA_RAW / "gof_variants.tsv"
    # AM rows of the old per-gene lists (`AM_VARIANT_SOURCE`, all classes;
    # snapshot as `GOF_VARIANTS`; sites only, committed)
    AM_VARIANTS: Path = Paths.DATA_RAW / "am_variants.tsv"
    # single GoF variants forced into the list and reported one by one
    # (`SELECTED_GOF_VARIANT_SOURCE`; sites and names only, committed)
    SELECTED_VARIANTS: Path = Paths.DATA_RAW / "selected_variants.tsv"
    VARIANT_LIST_TEMPLATE: str = str(Paths.DATA_TEMP / "{gene}_variants.tsv")
    # curated gene x ClinVar condition -> `ClinVarDirection`
    CLINVAR_CONDITION_DIRECTION: Path = (
        Paths.DATA_RAW / "clinvar_condition_direction.tsv"
    )
    # own UKB/AoU association results (marvel), one row per file/outcome
    UKB_PHENO: Path = Paths.DATA_PROC / "lipids_full_pheno.tsv.gz"
    MARVEL_RESULTS: Path = Paths.DATA_RAW / "marvel_results.tsv"
    # pyjasub job array for the per-gene marvel runs (one cnf per gene,
    # written by src/create_config.py)
    MARVEL_TASKS: Path = Paths.DATA_RAW / "marvel_tasks.tsv"
    # per-variant marvel run of the `SELECTED_VARIANTS` only (until the
    # next full per-variant run); its rows replace the store's
    # (`marvel_results_table.py --replace`)
    MARVEL_SELECTED_TASKS: Path = Paths.DATA_RAW / "marvel_selected_tasks.tsv"
    # UKB carrier burden (burden_exposure.py): per gene the 0/1 exposure
    # file (`{suffix}` "" or `Burden.FALLBACK_SUFFIX`), the
    # sites/carriers summary and the old marvel (10039b6) job array
    BURDEN_EXPOSURE_TEMPLATE: str = str(
        Paths.DATA_TEMP / "{gene}_burden_exposure{suffix}.tsv.gz"
    )
    BURDEN_EXPOSURE_SUMMARY: Path = (
        Paths.OUTPUT / "burden_exposure_summary.tsv.gz"
    )
    # the same masks as a long variant list for new marvel (one row per
    # site and mask, category `VariantListColumns.MASK`; `{suffix}` as
    # `BURDEN_EXPOSURE_TEMPLATE`; sites only, committed)
    BURDEN_MASK_VARIANTS_TEMPLATE: str = str(
        Paths.DATA_PROC / "lipid_mask_variants{suffix}.tsv.gz"
    )
    MARVEL_BURDEN_TASKS: Path = Paths.DATA_RAW / "marvel_burden_tasks.tsv"
    # marvel run of APOE diplotype -> outcomes: its own job array, so its
    # results never enter marvel_results.tsv as variants
    MARVEL_APOE_TASKS: Path = Paths.DATA_RAW / "marvel_apoe_tasks.tsv"
    # marvel exposure file of that run (apoe_exposure.py): ID column plus
    # one 0/1 carrier column per APOE diplotype
    APOE_EXPOSURE: Path = Paths.DATA_PROC / "apoe_diplotype.tsv.gz"
    # per-gene store of all marvel results (in `Paths.MARVEL_STORE`)
    MARVEL_STORE_TEMPLATE: str = "{gene}_results.tsv.gz"
    # loose per-variant marvel result files in a gene's outdir
    MARVEL_LOOSE_GLOB: str = "*_results.tsv.gz"
    # tar of an outdir's loose files (`marvel_results_table.py --archive`)
    MARVEL_ARCHIVE_TEMPLATE: str = "per_variant_results_{stamp}.tar"
    # old per-gene wide carriers files (`f.eid` + one column per variant),
    # as in marvel_tasks.tsv; copied from Myriad for compare_marvel_runs.py
    OLD_CARRIERS_TEMPLATE: str = str(
        Paths.DATA_TEMP / "{gene}_variant_extraction.tsv.gz"
    )
    # `output.prefix` of the burden and per-variant runs in
    # `Paths.MARVEL_RUN` (config/marvel_config{,_variant}.toml)
    MARVEL_BURDEN_PREFIX: str = "lipid_vep_plink_marvel_test"
    MARVEL_VARIANT_PREFIX: str = "lipid_vep_plink_marvel_variant"
    # curated study accession -> study group and APOE stratum
    APOE_STRATA: Path = Paths.DATA_RAW / "apoe_strata.tsv"
    # curated outcome x study exclusions, applied before the recency cap
    STUDY_OUTCOME_REVIEW: Path = Paths.DATA_RAW / "study_outcome_review.tsv"
    TASKS_FILE: Path = Paths.DATA_TEMP / "tasks.tsv"
    # (study, outcome) labels for the per-study filter outfiles
    STUDY_OUTCOMES_FILE: Path = Paths.DATA_TEMP / "study_outcomes.tsv"
    # flanked gene regions, frozen at prep time for the filter tasks
    GENE_REGIONS_FILE: Path = Paths.DATA_TEMP / "gene_regions.tsv"
    STUDY_DISCOVERY_LOG: Path = Paths.DATA_TEMP / "study_discovery_log.tsv.gz"
    MERGED_ASSOCIATIONS: Path = (
        Paths.OUTPUT / "merged_associations.tsv.gz"
    )
    # per-study effect scale: metadata, inference and final call
    STUDY_EFFECT_SCALE: Path = (
        Paths.OUTPUT / "study_effect_scale.tsv.gz"
    )
    # merged-associations rows matching a (non-AM) gene variant-list entry
    MATCHED_VARIANTS: Path = Paths.OUTPUT / "matched_variants.tsv.gz"
    # marvel gene-burden rows of the merged associations (burden_exposure.py
    # masks), written by match_variants.py for meta_analysis --ukb-burden
    MATCHED_BURDEN: Path = Paths.OUTPUT / "matched_burden.tsv.gz"
    # IVW meta-analysis per `Ancestry` code; `{suffix}` is "" or
    # "_<label>" (`meta_analysis.py --label`)
    META_ANALYSIS_TEMPLATE: str = "meta_{ancestry}{suffix}.tsv.gz"
    # gene-level burden (IVW over the oriented variant effects)
    BURDEN_TEMPLATE: str = "burden_{ancestry}{suffix}.tsv.gz"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIGURES

class FigureColumns:
    """Columns the figure scripts add to the result rows."""
    # odds ratio and its 95% CI
    OR: str = "odds_ratio"
    LB: str = "or_lower"
    UB: str = "or_upper"
    # y coordinate (`figure_utils.set_y`)
    Y: str = "y_axis"
    # per-row marker shape, colour and size
    MARKER: str = "marker"
    COLOUR: str = "colour"
    SIZE: str = "size"
    # 95% CI of the beta (lipid outcomes, `figure_utils.add_beta_ci`)
    BETA_LB: str = "beta_lower"
    BETA_UB: str = "beta_upper"
    # side-table texts: row name, OR (95% CI), beta (95% CI), p-value
    ROW_NAME: str = "row_name"
    OR_TEXT: str = "or_text"
    BETA_TEXT: str = "beta_text"
    P_TEXT: str = "p_text"
    # UKB carriers / cases (binary) or carriers / N (lipids)
    # (`figure_utils.add_carrier_text`)
    CARRIER_TEXT: str = "carrier_text"
    # row order within a group
    ORDER: str = "order"


class FigureNames:
    """Readable names and plotting order shared by the figure scripts."""
    # outcome key -> name, in plotting order
    OUTCOMES: dict[str, str] = {
        "ascvd": "ASCVD",
        "alzheimers_dementia": "Alzheimer's disease",
        "all_cause_dementia": "All-cause dementia",
        "vascular_dementia": "Vascular dementia",
        "frontotemporal_dementia": "Frontotemporal dementia",
    }
    OUTCOME_RANK: dict[str, int] = {
        name: i for i, name in enumerate(OUTCOMES)
    }
    # lipid outcome key (`Const.LIPID_OUTCOMES`) -> name with the UKB
    # unit, in plotting order
    LIPIDS: dict[str, str] = {
        "hdl_c": "HDL-C (mmol/L)",
        "apoa": "ApoA1 (g/L)",
        "tg": "Triglycerides (mmol/L)",
        "ldl_c": "LDL-C (mmol/L)",
        "apob": "ApoB (g/L)",
    }
    LIPID_RANK: dict[str, int] = {
        name: i for i, name in enumerate(LIPIDS)
    }
    # APOE strata in plotting order, `ApoeStratum.ALL` = all genotypes
    STRATUM_ORDER: tuple[str, ...] = (
        ApoeStratum.ALL,
        ApoeStratum.E44,
        ApoeStratum.E43,
        ApoeStratum.E33,
        ApoeStratum.E22_E32,
    )
    STRATA: dict[str, str] = {
        ApoeStratum.ALL: "All genotypes",
        ApoeStratum.E44: "ε4/ε4",
        ApoeStratum.E43: "ε4/ε3",
        ApoeStratum.E33: "ε3/ε3",
        ApoeStratum.E22_E32: "ε2/ε2 + ε3/ε2",
    }
    UKB: str = "UK Biobank"
    POOLED: str = "Pooled (IVW)"
    # forest x label and side-table headers
    OR_LABEL: str = "Odds ratio (95% CI)"
    OR_HEADER: str = "OR (95% CI)"
    BETA_LABEL: str = "Beta (95% CI), native units"
    # gene figures: effects oriented by `TherapyDirection.GENES`
    # (figure_utils.load_burden)
    THERAPY_SUFFIX: str = "therapeutic direction"
    OR_LABEL_THERAPY: str = f"{OR_LABEL}, {THERAPY_SUFFIX}"
    BETA_LABEL_THERAPY: str = f"{BETA_LABEL}, {THERAPY_SUFFIX}"
    # genes plotted first (at the top) in multi-gene figures, the others
    # follow alphabetically (figure_utils.ordered_genes)
    FIRST_GENES: tuple[str, ...] = ("CETP",)
    BETA_HEADER: str = "Beta (95% CI)"
    P_HEADER: str = "P-value"
    CARRIERS_HEADER: str = "Carriers / Cases"
    CARRIERS_N_HEADER: str = "Carriers / N"
    SOURCE_HEADER: str = "Source"
    # legend titles
    SIGNIFICANCE_TITLE: str = "Significance"
    OUTCOME_TITLE: str = "Outcomes"
    LIPID_TITLE: str = "Lipids"
    VARIANT_SET_TITLE: str = "Variant set"
    # variant set (`Burden.VARIANT_SETS` key) -> name, in
    # plotting order
    VARIANT_SETS: dict[str, str] = {
        "gof": "GoF",
        "am": "AM",
        "ptv": "PTV",
        "clinvar": "ClinVar",
        "lof": "PTV + ClinVar",
        "ptv_am": "PTV + AM",
        "am_clinvar": "AM + ClinVar",
        "ptv_clinvar_am": "PTV + ClinVar + AM",
    }
    VARIANT_SET_RANK: dict[str, int] = {
        name: i for i, name in enumerate(VARIANT_SETS)
    }
    # main-analysis figures: a full file name without suffix, or, ending
    # in '_', the start of one; every other figure goes to
    # `Paths.FIGURES_SENSITIVITY` (`figure_utils.save`)
    MAIN_FIGURES: tuple[str, ...] = (
        "forest_cohort_burden_eur_controls",
        "forest_cohort_burden_eur_dementia",
        "forest_variant_sets_cohort_burden_eur_",
        "scatter_ascvd_dementia_cohort_burden_eur_",
        "forest_cohort_variants_CETP",
        "forest_apoe_genotype_EUR",
        # selected_variants_forest.py, one figure per selected GoF variant
        "forest_selected_gof_eur_",
    )

class FigureStyle:
    """Sizes, colours, markers and forest layout of the figure scripts.

    Sizes as in cox_forest.py: font sizes and line widths in points,
    lengths in cm.
    """
    CM: float = 1 / 2.54
    TITLE_SIZE: float = 3.5
    LAB_SIZE: float = 3
    LWD: float = 0.5
    AX_LAB_SZ: float = 2.7
    STEXT_SIZE: float = 2.7
    WIDTH_CM: float = 9.0
    CM_PER_Y: float = 0.07
    # pooled estimate vs single study / stratum
    POOLED_COLOUR: str = "black"
    # pooled forest: marker colour per outcome key, from the APOE
    # genotype colours (apoe_genotype_forest.py); others `POOLED_COLOUR`
    OUTCOME_COLOURS: dict[str, str] = {
        "alzheimers_dementia": "#67a9cf",
        "vascular_dementia": "#ef8a62",
        "frontotemporal_dementia": "#8073ac",
        "all_cause_dementia": "#b2182b",
        "ascvd": "#35978f",
    }
    # pooled forest, lipid panel: marker colour per lipid outcome key
    LIPID_COLOURS: dict[str, str] = {
        "ldl_c": "#1b7837",
        "apob": "#a6dba0",
        "hdl_c": "#c51b7d",
        "apoa": "#f1b6da",
        "tg": "#e08214",
    }
    # variant-set forest: marker colour per variant set (Okabe-Ito; the
    # main PTV + ClinVar set black)
    VARIANT_SET_COLOURS: dict[str, str] = {
        "gof": "#D55E00",
        "am": "#0072B2",
        "ptv": "#009E73",
        "clinvar": "#CC79A7",
        "lof": "#000000",
        "ptv_am": "#56B4E9",
        "am_clinvar": "#E69F00",
        "ptv_clinvar_am": "#882255",
    }
    # selected-variants forest, all variants in one figure: marker colour
    # per selected GoF variant, in variant-site order (Okabe-Ito)
    SELECTED_VARIANT_COLOURS: tuple[str, ...] = (
        "#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9",
    )
    STUDY_COLOUR: str = "#bdbdbd"
    POOLED_SIZE: float = 14
    STUDY_SIZE: float = 9
    # marker size of a forest with one kind of estimate
    MARKER_SIZE: float = 9
    # significance -> marker shape, and the matching heatmap glyph
    P_NOMINAL: float = 0.05
    MARKER_NS: str = "o"
    MARKER_NOMINAL: str = "s"
    MARKER_STRICT: str = "D"
    GLYPH_NOMINAL: str = "■"
    GLYPH_STRICT: str = "◆"
    # forest layout: panel widths (forest, three side tables), height
    # without the rows (cm; with and without the significance legend), top
    # margin (cm), y padding around the rows
    FOREST_WIDTH_RATIOS: tuple[float, ...] = (1.5, 0.5, 0.7, 0.35)
    FOREST_BASE_HEIGHT_CM: float = 1.75
    # space below the forest axis (cm): ticks, x label and the titled
    # significance legend
    FOREST_BOTTOM_CM: float = 1.15
    FOREST_BASE_HEIGHT_NO_LEGEND_CM: float = 1.1
    FOREST_TOP_CM: float = 0.35
    FOREST_Y_PAD: float = 3
    # forests with side tables in a grid (`figure_utils.table_grid`): y
    # padding above the first row (top of the axis) and below the last
    # one, rows being 2 apart and groups 4; forest width, space for the
    # y tick labels left of it and the gap between panel rows (cm)
    TABLE_Y_PAD_TOP: float = 1.5
    TABLE_Y_PAD_BOTTOM: float = 2
    TABLE_FOREST_CM: float = 3.2
    TABLE_LABEL_CM: float = 1.0
    TABLE_ROW_GAP_CM: float = 1.1
    # default odds-ratio axis limit (`--max-or`)
    MAX_OR: float = 20.0
    # plot_misc ForestPlot / plot_table keyword arguments
    SCATTER_KWARGS: dict[str, object] = {
        "edgecolors": "black",
        "linewidth": 0.3,
    }
    CI_KWARGS: dict[str, object] = {
        "zorder": 1,
        "solid_capstyle": "round",
        "linestyle": "-",
    }
    TABLE_NEGATIVE_PADDING: float = 1
    # significance legend below the forest, its left edge at the forest
    # axis (`figure_utils.add_legend`); height of an extra titled legend
    # (cm)
    LEGEND_ROW_CM: float = 0.4
    LEGEND_KWARGS: dict[str, object] = {
        "loc": "lower left",
        "ncol": 3,
        "frameon": False,
        "fontsize": STEXT_SIZE,
        "title_fontproperties": {"size": STEXT_SIZE, "weight": "bold"},
        "alignment": "left",
        "handletextpad": 0.2,
        "columnspacing": 1.0,
    }
