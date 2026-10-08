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
    DATA_PROC: Path = HERE / "data" / "processed"
    GWAS_FILTERED: Path = DATA_TEMP / "gwas_filtered"
    # gzipped JSON per Ensembl overlap window / rsid lookup; delete a file
    # to refetch it
    ENSEMBL_CACHE: Path = DATA_TEMP / "ensembl_cache"
    RESULTS_OUTPUT: Path = HERE / "results" / "output"
    # per-gene marvel result stores (`marvel_results_table.py`)
    MARVEL_STORE: Path = HERE / "results" / "marvel"
    RESULTS_FIGURES: Path = HERE / "results" / "figures"
    LOGS: Path = HERE / "logs"
    # must match `log_dir` in config/filter_task.cnf
    FILTER_TASK_LOGS: Path = HERE / "src" / "logs" / "filter_task_logs"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Effect scales

class EffectScale:
    """Values of `effect_scale_meta` and `study_effect_scale`: the scale
    of a study's betas for a binary outcome.
    """
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
# Constants

class Constants:
    """Pipeline thresholds and external API endpoints (gwas_cat.md)."""
    # MAF cutoff of the filter step and the curated associations; `None`
    # keeps every in-region row whatever its frequency (also rows without
    # one), since listed variants can be common in some ancestries.
    # match_variants.py keeps only the listed variants.
    MAF_THRESHOLD: float | None = None
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
    # variant-list source of the ClinVar P/LP entries; in the per-gene
    # lists it is replaced by `FileNames.PLP_VARIANTS`
    CLINVAR_VARIANT_SOURCE: str = "ClinVar"
    # assembly suffix of the P/LP coordinate columns used for matching
    PLP_ASSEMBLY_SUFFIX: str = "_grch38"
    # pseudo variant-list source of `match_variants.py --region-rare`: every
    # rare GWAS variant in the gene region, a1 = GRCh38 ref, a2 = alt
    REGION_VARIANT_SOURCE: str = "region_rare"
    # default MAF threshold (exclusive) of `--region-rare`
    REGION_MAX_MAF: float = 0.01
    # APOE e4 (p.Cys130Arg, rs429358) and e2 (p.Arg176Cys, rs7412) as
    # `variant_site`; they define APOE-stratified GWAS, so any run that
    # holds them is repeated without them (APOE_SENSITIVITY_LABEL)
    APOE_ISOFORM_SITES: tuple[str, ...] = (
        "19:44908684:T:C",
        "19:44908822:C:T",
    )
    APOE_SENSITIVITY_LABEL: str = "no_apoe_e2e4"
    # burden sensitivity: ClinVar-only variants without a lowering/raising
    # direction left out
    DIRECTED_BURDEN_LABEL: str = "directed_only"
    # file label of the meta-analysis pooled per APOE stratum
    APOE_STRATA_LABEL: str = "apoe_strata"
    # ClinVar `rcv_molecular_consequence` values that make a P/LP variant
    # `lowering` whatever its conditions
    TRUNCATING_CONSEQUENCES: frozenset[str] = frozenset(
        {
            "frameshift variant",
            "nonsense",
            "splice acceptor variant",
            "splice donor variant",
        }
    )
    # meta-analysis dedupe: per study/outcome/variant the first source here
    # is kept (rows from other sources go last)
    GWAS_SOURCE_PREFERENCE: tuple[str, ...] = ("summary-stats", "curated")
    # meta-analysis tie-break after GWAS_SOURCE_PREFERENCE: per study/
    # outcome/variant (and between identical copies) the first source_db
    # here is kept (others go last)
    SOURCE_DB_PREFERENCE: tuple[str, ...] = (
        "manual",
        "finngen",
        "marvel_aou",
        "marvel_ukb",
        "gwas_catalog",
    )
    # preferred cohort key -> GWAS Catalog `cohort` tokens (lower case) it
    # matches; a catalog study listing a cohort is excluded for every
    # outcome that has that cohort's own results (FinnGen phenocode or
    # marvel_results.tsv row)
    PREFERRED_COHORT_ALIASES: dict[str, frozenset[str]] = {
        "finngen": frozenset({"finngen"}),
        "ukb": frozenset({"ukb", "ukbb", "uk biobank"}),
        "aou": frozenset({"aou", "all of us", "allofus"}),
    }
    # cohorts excluded from catalog studies for every outcome, whether or
    # not own (marvel) results exist yet
    ALWAYS_EXCLUDED_COHORTS: frozenset[str] = frozenset({"ukb", "aou"})
    # catalog reason prefix for a study_outcome_review.tsv exclusion
    REVIEW_REASON_PREFIX: str = "review_"
    # study_outcome_review.tsv `status` the pipeline acts on; any other
    # value (keep, proposed_exclude, copied audit statuses) is ignored
    REVIEW_EXCLUDE_STATUS: str = "exclude"
    # separators between cohorts in a GWAS Catalog `cohort` cell
    COHORT_SPLIT_PATTERN: str = r"[;|,]"
    # catalog reason prefix for a cohort-overlap exclusion, + cohort key
    COHORT_OVERLAP_REASON_PREFIX: str = "cohort_overlap_"
    # marvel `Exposure` naming a single variant (chr:pos:a1:a2, a2
    # counted); any other exposure is a gene-level (burden) result
    MARVEL_VARIANT_PATTERN: str = (
        r"^(?:chr)?(?P<chrom>[0-9XYMT]+):(?P<pos>\d+):"
        r"(?P<a1>[ACGT]+):(?P<a2>[ACGT]+)$"
    )
    # source_db of marvel rows, + cohort key
    MARVEL_SOURCE_DB_PREFIX: str = "marvel_"
    # marvel `Stratification name` kept when marvel_results.tsv leaves
    # `stratification` blank
    MARVEL_DEFAULT_STRATIFICATION: str = "overall"
    # marvel `Exposure` naming a gene-level carrier mask, e.g. "CETP PTV"
    MARVEL_GENE_MASK_PATTERN: str = r"^(?P<gene>\S+)\s+(?P<mask>\S.*)$"
    # marvel `Model` (regression method) -> `EffectScale`; other methods
    # are `EffectScale.UNKNOWN`
    MARVEL_METHOD_SCALE: dict[str, str] = {
        "GLM-Binom": EffectScale.LOG_OR,
        "OLS": EffectScale.LINEAR,
        "Cox": EffectScale.LOG_HR,
    }
    # marvel rows with fewer exposed (carriers) are dropped at merge
    MARVEL_MIN_CARRIERS: int = 5
    # UKB marvel `Variable` -> `outcome` in icd_codes.txt; `_combined`
    # (algorithm + ICD) where UKB has it, else `_algo`. Other variables
    # are left out of marvel_results.tsv
    MARVEL_UKB_OUTCOMES: dict[str, str] = {
        "all_cause_dementia_combined": "all_cause_dementia",
        "alzheimers_disease_combined": "alzheimers_dementia",
        "vascular_dementia_algo": "vascular_dementia",
        "frontotemporal_dementia_algo": "frontotemporal_dementia",
    }
    # effect-scale inference (`functions.infer_effect_scales`): median of
    # r = SE * sqrt(2f(1-f)N) over a study's variants with MAF above
    # EFFECT_SCALE_MIN_MAF; log-OR gives r = 1/sqrt(phi(1-phi)) >= 2,
    # a linear 0/1 outcome r = sqrt(phi(1-phi)) <= 0.5 (phi: case
    # fraction), so the cut-off sits in between
    EFFECT_SCALE_CUTOFF: float = 1.0
    EFFECT_SCALE_MIN_MAF: float = 0.01
    # fewer usable variants than this: inferred scale unknown
    EFFECT_SCALE_MIN_VARIANTS: int = 20
    # GWAS-SSF `analysis_software` (lower-case substring) -> `EffectScale`;
    # REGENIE is left out: logistic with Firth or linear, both common
    SOFTWARE_EFFECT_SCALE: dict[str, str] = {
        "saige": EffectScale.LOG_OR,
        "plink": EffectScale.LOG_OR,
        "snptest": EffectScale.LOG_OR,
        "bolt": EffectScale.LINEAR,
        "fastgwa": EffectScale.LINEAR,
    }
    # GWAS-SSF `effect_statistic` (lower case) -> `EffectScale`; "beta"
    # is not listed, it is used for both log-OR and linear effects
    EFFECT_STATISTIC_SCALE: dict[str, str] = {
        "odds_ratio": EffectScale.LOG_OR,
        "hazard_ratio": EffectScale.LOG_HR,
    }
    # FinnGen R13 binary endpoints: REGENIE with Firth correction
    FINNGEN_EFFECT_SCALE: str = EffectScale.LOG_OR
    # sumstats effect allele of a gene-burden mask row (e.g. UKB exome
    # "M1.0001", "M3.singleton"; other allele "ref"); kept whatever its
    # MAF and turned into a gene-burden row at merge
    BURDEN_MASK_ALLELE_PATTERN: str = r"^M\d+\.(?:\d+|singleton)$"
    # `Name` of a burden mask row, e.g. "PCSK9(ENSG00000169174).GENE.M1.01"
    BURDEN_NAME_PATTERN: str = (
        r"^(?P<gene>[^(]+)\((?P<ensembl_id>ENSG\d+)\)\.GENE\.(?P<mask>.+)$"
    )
    # bp added on both sides of a gene region when fetching its reference
    # sequence, so indels can be left-aligned past the region edge
    INDEL_NORM_PAD_BP: int = 500
    # ClinVar pathogenicity
    PATHOGENIC_CLASSIFICATIONS: frozenset[str] = frozenset(
        {"Pathogenic", "Likely pathogenic", "Pathogenic/Likely pathogenic"}
    )
    CONFLICTING_CLASSIFICATION_LABEL: str = (
        "Conflicting classifications of pathogenicity"
    )
    PATHOGENIC_TERM: str = "pathogenic"
    REVIEW_STATUS_CORE: str = "reviewed by expert panel"
    REVIEW_STATUS_STRICTNESS_ORDER: tuple[str, ...] = (
        "no assertion criteria provided",
        "criteria provided, single submitter",
        "criteria provided, multiple submitters, no conflicts",
    )


class RunlogOrder:
    """RUN_LOG.md section order per pipeline step.

    Explicit because each step runs in its own process tree (qsub,
    pyjasub, `mamba run`), so log_tools' PPID-based auto-order would
    give every step 10. The Bash job wrappers hard-code the same values
    in `RUNLOG_ORDER` and must be kept in sync.
    """
    GWAS_CAT_PREP: int = 10
    FILTER_GWAS_CAT: int = 20
    MARVEL_RESULTS_TABLE: int = 25
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
    # harmonised `Ancestry` code derived from ANCESTRY
    ANCESTRY_GROUP: str = "ancestry_group"
    COHORT: str = "cohort"
    # marvel_results.tsv: marvel `Stratification name` to keep
    STRATIFICATION: str = "stratification"
    # GWAS-SSF `-meta.yaml` fields and the `EffectScale` they imply
    EFFECT_STATISTIC: str = "effect_statistic"
    ANALYSIS_SOFTWARE: str = "analysis_software"
    EFFECT_SCALE_META: str = "effect_scale_meta"
    # `FileNames.STUDY_EFFECT_SCALE` evidence: marvel method scale, median
    # of SE*sqrt(2f(1-f)N), the scale it implies, and the final per-study
    # `EffectScale` (`functions.infer_effect_scales`)
    EFFECT_SCALE_METHOD: str = "effect_scale_method"
    R_MEDIAN: str = "r_median"
    EFFECT_SCALE_INFERRED: str = "effect_scale_inferred"
    STUDY_EFFECT_SCALE: str = "study_effect_scale"
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


class ClinVarColumnNames:
    """ClinVar column names"""
    VCV_ACCESSION_COL: str = "vcv_accession"
    VARIATION_ID_COL: str = "variation_id"
    VARIATION_NAME_COL: str = "variation_name"
    GENE_SYMBOL_COL: str = "gene_symbol"
    CANONICAL_SPDI_COL: str = "canonical_spdi"
    ASSEMBLY_COL: str = "assembly"
    CHR_COL: str = ColumnNames.GENE_CHR
    START_COL: str = ColumnNames.START
    STOP_COL: str = "stop"
    POSITION_VCF_COL: str = "position_vcf"
    REFERENCE_ALLELE_COL: str = "reference_allele_vcf"
    ALTERNATE_ALLELE_COL: str = "alternate_allele_vcf"
    SUBMITTED_CLASSIFICATIONS_COL: str = "submitted_classifications"
    CLASSIFICATION_COUNT_COL: str = "classification_count"
    VARIANT_TYPE_COL: str = "variant_type"
    RCV_MOLECULAR_CONSEQUENCE_COL: str = "rcv_molecular_consequence"
    RCV_CONDITION_COL: str = "rcv_condition"
    RCV_CONDITION_DB_COL: str = "rcv_condition_db"
    RCV_CONDITION_ID_COL: str = "rcv_condition_id"
    RCV_CLASSIFICATION_COL: str = "rcv_classification"
    RCV_REVIEW_STATUS_COL: str = "rcv_review_status"
    REVIEW_FLAG_COL: str = "review_flag"


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
    EFO_ID: str = ColumnNames.EFO_ID
    # efo_id is the queried term; mapped_trait_* the term(s) the study or
    # association is actually annotated with (a child when CHILD_TRAITS)
    CHILD_TRAITS: str = ColumnNames.CHILD_TRAITS
    MAPPED_TRAIT_ID: str = ColumnNames.MAPPED_TRAIT_ID
    MAPPED_TRAIT: str = ColumnNames.MAPPED_TRAIT
    OUTCOME_DESC: str = "outcome_desc"
    TRAIT_LABEL: str = "trait_label"
    # study ancestry as an `Ancestry` code
    ANCESTRY_GROUP: str = ColumnNames.ANCESTRY_GROUP
    # per-study `EffectScale`; set by the marvel loader, else at merge
    STUDY_EFFECT_SCALE: str = ColumnNames.STUDY_EFFECT_SCALE
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


class MafStatus:
    """Values of the `maf_status` column."""
    NUMERIC: str = "numeric"
    NOT_REPORTED: str = "not_reported"


class NormStatus:
    """Values of the `norm_status` column (variant-list `norm_status` too).

    Variants are left-aligned and trimmed against the GRCh38 reference
    (`functions.normalise_variant`); NA for rows without a site (gene
    burden).
    """
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
    # pos/a1/a2 before normalisation, and its `NormStatus`
    POS_ORIG: str = "pos_orig"
    A1_ORIG: str = "a1_orig"
    A2_ORIG: str = "a2_orig"
    NORM_STATUS: str = "norm_status"
    # ClinVar P/LP rows only: a `ClinVarDirection` value (NA otherwise)
    CLINVAR_DIRECTION: str = "clinvar_direction"
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


class MetaLevel:
    """Values of the `level` column of the meta-analysis outputs."""
    # pooled over all studies of the run
    POOLED: str = "pooled"
    # one study (e.g. one APOE stratum of a stratified GWAS)
    STRATUM: str = "stratum"


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


class Orientation:
    """Values of the `orientation` column."""
    # effect of the a2 (alt) allele
    A2: str = "a2"
    # GoF-listed variant: effect of the a1 allele
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


class ConditionDirectionColumns:
    """Columns of `FileNames.CLINVAR_CONDITION_DIRECTION`."""
    GENE: str = "gene"
    CONDITION: str = "rcv_condition"
    DIRECTION: str = "direction"


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
    CLINVAR_VARIANTS: Path = Paths.DATA_RAW / "clinvar_variants.tsv"
    VARIANTS_REVIEW_STATUS_SUMMARY: Path = (
        Paths.DATA_PROC / "pah_variants_review_status_summary.tsv"
    )
    PLP_VARIANTS: Path = Paths.DATA_PROC / "plp_variants.tsv"
    # curated gene x ClinVar condition -> `ClinVarDirection`
    CLINVAR_CONDITION_DIRECTION: Path = (
        Paths.DATA_RAW / "clinvar_condition_direction.tsv"
    )
    # own UKB/AoU association results (marvel), one row per file/outcome
    UKB_PHENO: Path = Paths.DATA_PROC / "pheno_cov.tsv.gz"
    MARVEL_RESULTS: Path = Paths.DATA_RAW / "marvel_results.tsv"
    # pyjasub job array for the per-gene marvel runs (one cnf per gene,
    # written by src/create_config.py)
    MARVEL_TASKS: Path = Paths.DATA_RAW / "marvel_tasks.tsv"
    # per-gene store of all marvel results (in `Paths.MARVEL_STORE`)
    MARVEL_STORE_TEMPLATE: str = "{gene}_results.tsv.gz"
    # loose per-variant marvel result files in a gene's outdir
    MARVEL_LOOSE_GLOB: str = "*_results.tsv.gz"
    # tar of an outdir's loose files (`marvel_results_table.py --archive`)
    MARVEL_ARCHIVE_TEMPLATE: str = "per_variant_results_{stamp}.tar"
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
        Paths.RESULTS_OUTPUT / "merged_associations.tsv.gz"
    )
    # per-study effect scale: metadata, inference and final call
    STUDY_EFFECT_SCALE: Path = (
        Paths.RESULTS_OUTPUT / "study_effect_scale.tsv.gz"
    )
    # merged-associations rows matching a (non-AM) gene variant-list entry
    MATCHED_VARIANTS: Path = Paths.RESULTS_OUTPUT / "matched_variants.tsv.gz"
    # `match_variants.py --region-rare` output (Constants.REGION_*)
    MATCHED_REGION_VARIANTS: Path = (
        Paths.RESULTS_OUTPUT / "matched_region_variants.tsv.gz"
    )
    # IVW meta-analysis per `Ancestry` code; `{suffix}` is "" or
    # "_<label>" (`meta_analysis.py --label`)
    META_ANALYSIS_TEMPLATE: str = "meta_{ancestry}{suffix}.tsv.gz"
    # gene-level burden (IVW over the oriented variant effects)
    BURDEN_TEMPLATE: str = "burden_{ancestry}{suffix}.tsv.gz"
