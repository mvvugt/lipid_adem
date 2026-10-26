#!/usr/bin/env bash
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SETUP
#
# REFERENCE OUTLINE ONLY -- do not run end-to-end.
set -euo pipefail

case "$(uname)" in
    Linux)
        ROOT="${HOME}/projects/lipid_adem"
        ;;
    Darwin)
        ROOT="${HOME}/Documents/work.nosync/projects/lipid_adem"
        ;;
    *)
        echo "Unknown system"
        ;;
esac

# shellcheck source=/dev/null
. "${ROOT}"/src/functions.sh
# Every cluster step runs on Snellius (ROOT = ~/projects/lipid_adem); only
# the ClinVar query and the figures run locally
# TODO after the validation (validation/HANDOFF.md) passes: move the marvel
# runs (MARVEL_ENV=marvel_old, 10039b6) to the validated marvel version


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INPUTS
# Not in git (data/ is ignored); copy to the same paths on Snellius:
# - [local -> snellius] data/raw/: gene_list.txt, icd_codes.txt,
#   efo_ukb_master_mapping.tsv, finngen_r13_manifest.tsv,
#   gwas_catalog_manual_studies.tsv, study_outcome_review.tsv,
#   clinvar_variants.tsv (ClinVar query below), clinvar_condition_direction
#   .tsv, gof_variants.tsv, am_variants.tsv, apoe_strata.tsv,
#   marvel_tasks.tsv and marvel_apoe_tasks.tsv, each with its SOURCE.md
# - [snellius, present] data/processed/lipids_full_pheno.tsv.gz and
#   pheno_cov.tsv.gz (PHENOTYPES), data/temp/<GENE>_variant_extraction
#   .tsv.gz (CARRIER EXTRACTION), the VEP VCFs (VARIANT ANNOTATION)
# Rebuilt on Snellius, not copied: data/temp/{tasks,study_outcomes,
# gene_regions}.tsv (gwas_cat_prep.py), the filtered sumstats, the marvel
# outdirs and stores (results/<GENE>, results/marvel_burden, results/marvel),
# data/raw/marvel_results.tsv and everything in results/output
# [snellius] the curated task files hold Myriad paths: point them at ROOT
sed -i "s#/myriadfs/home/rmgpmva/projects/lipid_adem#${ROOT}#g" \
    "${ROOT}"/data/raw/marvel_tasks.tsv "${ROOT}"/data/raw/marvel_apoe_tasks.tsv


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PHENOTYPES
# TODO not in this repo yet: add the commands that build the phenotype
# files here. Every analysis below reads them.
#
# Files read (2026-10-26):
# - data/processed/lipids_full_pheno.tsv.gz: FileNames.UKB_PHENO
#   (create_config.py, apoe_exposure.py, burden_exposure.py),
#   config/marvel_config.toml and all config/marvel{,_burden} cnfs
# - data/processed/pheno_cov.tsv.gz: config/marvel_config_variant.toml
#   only. Same IDs (502166) and counts as cetp_marvel's pheno_cov.tsv.gz
#   (checked 2026-10-26); lipids_full_pheno.tsv.gz is it restricted to
#   469587 IDs (the IDs with genotypes). Burden and per-variant runs share
#   a run directory; kept as is, since marvel keeps only IDs in the
#   exposure file
#
# CHECK EVERY TIME a phenotype file is rebuilt or copied, or before a
# marvel run (gz md5 differs on gzip metadata alone, so compare the
# uncompressed content):
#   gzip -dc <file> | md5sum
#   validation/check_pheno.py <old file> <new file>   # IDs, n, cases
# - the files the configs read agree in IDs and outcome counts, and the
#   md5 of each is noted with the run
# - burden and per-variant results of one run have the same sample n
#   per outcome (e.g. LDL direct_i0); if not, point both tomls at
#   lipids_full_pheno.tsv.gz
# - check_pheno.py does not compare covariates (Sex, age, PCs); for
#   those diff the uncompressed files
# - cetp_marvel/data/processed/pheno_cov.tsv.gz: validation step 2
#   (old_pheno_cov.tsv.gz there = the 2026-02-06 version, A's input)
#
# Issues found with validation/check_pheno.py in cetp_marvel's
# pheno_cov.tsv.gz (2026-10-26); fix in the outcome build, then rebuild:
# - <outcome>_incident for the dementias: prevalent cases coded 0
#   (counted as controls); should be NA, as in the 02-06 file and in
#   ascvd_ii_incident
# - ascvd_ii_incident misses ~11k cases: incident + prevalent = 63253, but
#   ascvd_ii = 74254 (02-06 file: 50644 + 21239 = 71883, consistent).
#   Likely the 2026-02-10 outcome update reached ascvd_ii but not the
#   incident column (censoring date or sources)
# - binary outcomes have no NAs any more (~15k were NA on 02-06): check
#   this is intended
# The analyses below use only the overall outcomes (ascvd_ii,
# *_dementia_{algo,combined}, lipids _i0), not _incident/_prevalent, so
# they are not affected. Checked 2026-10-26: lipids_full_pheno.tsv.gz
# (469587 IDs) is a subset of the current pheno_cov.tsv.gz (withdrawals +
# 02-10 outcomes in), has no _incident/_prevalent columns, and its counts
# equal the validation step 2 rerun. cetp_marvel's lipids_full_pheno copy
# (no lipid columns) is not read by any config.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# APOE DIPLOTYPE
# Needs only the phenotype file, so it runs first. Each diplotype (e3e3
# included) vs all other diplotypes.

# [snellius] exposure file: one 0/1 carrier column per diplotype
run_mamba biomed-api "${ROOT}"/src/apoe_exposure.py
# [snellius] associate the diplotypes with outcomes (all samples and EUR),
# one job-array row per subset
run_mamba marvel_old "${ROOT}"/src/create_config.py -a \
    -t "${ROOT}"/data/raw/marvel_apoe_tasks.tsv
TASKS="${ROOT}"/data/raw/marvel_apoe_tasks.tsv
N_TASKS=$(( $(wc -l < "${TASKS}") - 1 ))
TASK_LOGS="${ROOT}"/src/logs/marvel_apoe_task_logs
mkdir -p "${TASK_LOGS}"
sbatch --array=1-"${N_TASKS}" --partition=rome --cpus-per-task=1 --mem=16G \
    --time=12:00:00 --job-name=marvel_apoe                                     \
    --output="${TASK_LOGS}"/%x_%A_%a.log                                       \
    --wrap "MARVEL_ENV=marvel_old ${ROOT}/src/marvel_assoc.sh ${TASKS} \
        \${TMPDIR} 1 \${SLURM_ARRAY_TASK_ID}"
# [local] rsync results/APOE_diplotype{,_eur} from Snellius first
run_mamba plot-misc "${ROOT}"/src/apoe_genotype_forest.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VARIANT ANNOTATION

# [snellius] VEP/LOFTEE consequences per gene, region read from the
# indexed per-chromosome VEP VCFs (-p pattern with {chrom})
LOF_DIR="/projects/0/aus20644/data/ukbiobank/genetics/b38/lof"
sbatch "${ROOT}"/src/vep_extract.sh -r "${ROOT}" -o "${ROOT}"/data/temp        \
    -d "${LOF_DIR}" -g "${ROOT}"/data/raw/gene_list.txt                        \
    -p "chr{chrom}_merged_vep.vcf.gz" -v

# [snellius] LOFTEE HC PTVs on the canonical transcript
run_mamba biomed-api "${ROOT}"/src/annotate_ptv.py

# [local] query ClinVar for all variants in the curated genes (the ClinVar
# databases are local); copy data/raw/clinvar_variants.tsv to Snellius
mapfile -t genes < <(cut -f1 "${ROOT}/data/raw/gene_list.txt")
runlog run --id clinvar_filter --order 40 --root "${ROOT}" --                  \
    mamba run --no-capture-output -n clinvar-build                             \
    clinvar-filter                                                             \
    "${HOME}/Documents/work.nosync/data/clinvar/clinvar_vcv.db"                \
    --rcv-db "${HOME}/Documents/work.nosync/data/clinvar/clinvar_rcv.db"       \
    -g "${genes[@]}"                                                           \
    -o "${ROOT}/data/raw/clinvar_variants.tsv"                                 \
    -vvv

# [snellius]
run_mamba marvel_old "${ROOT}"/src/annotate_clinvar.py

# [snellius] combine PTV + ClinVar + GoF normalised against GRCh38; GoF is the
# snapshot data/raw/gof_variants.tsv of the old per-gene lists (see its
# SOURCE.md), which this step overwrites
run_mamba biomed-api "${ROOT}"/src/combine_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CARRIER EXTRACTION

# TODO not implemented: plan in docs/rap_carrier_extraction.md
# [rap] MARVELous Docker on Swiss Army Knife; extract both forms of each
# variant from the RAP PLINK files (WGS or WES)
# Manual copies:
# - git -> rap: dx upload data/temp/<GENE>_variants.tsv, the extraction
#   cnfs, src/rap_extract.sh and the Docker image tarball (once)
# - rap -> snellius: dx download the <GENE>_carriers.tsv.gz files into
#   data/raw/carriers/; individual-level data: check the UKB approval
#   allows the download, never commit, delete when no longer needed
# [snellius] collapse the two forms per variant (no merge on conflict) into
# data/temp/<GENE>_variant_extraction.tsv.gz (read by marvel_tasks.tsv)
# TODO if individual data/temp/<GENE>_variants.tsv doe not exist, but data/processed/lipid_variants does, create the individual files anytime the individual ones are needed (not in marvel itself of course, but before marvel submission e.g.)
# list full-sample vcf-files for some genes; exclude one of the chr1 genes
realpath "${ROOT}"/../cetp_marvel/data/temp/*plink*vcf.gz |
    grep -v PCSK9 > "${ROOT}"/data/raw/plink_gene_vcfs.txt
DATA_DIR="/gpfs/work2/0/aus20644/data"
REF_DIR="${DATA_DIR}/resources/human_genome/b38"
LOF_DIR="${DATA_DIR}/ukbiobank/genetics/b38/lof"
"${ROOT}"/src/submit_two_source.sh                                             \
    -c "${ROOT}"/config/marvel_config.toml                                     \
    -p "${ROOT}"/data/raw/plink_gene_vcfs.txt                                  \
    -P "${LOF_DIR}"'/chr{chrom}_merged_vep.vcf.gz'                             \
    -R "${REF_DIR}/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz"             \
    -o "${ROOT}"/data/temp/marvel                                              \
    -a "${HOME}"/software/marvel/resources/workflows/slurm_array.sh            \
    -m '2023 BCFtools/1.18-GCC-12.3.0'

# [snellius] per-variant aggregate + associate on the same extract chunks
# (one exposure per variant, prefix lipid_vep_plink_marvel_variant); ~100x
# the tests of the burden run, hence 8 cores and 8 h (estimate)
RUN_DIR="${ROOT}/data/temp/marvel"
sbatch --partition=rome --cpus-per-task=8 --mem=16G --time=08:00:00         \
    --job-name=mv_final_variant                                                \
    --output="${RUN_DIR}/two_source/logs/%x_%j.log"                            \
    "${HOME}"/software/marvel/resources/workflows/slurm_array.sh               \
    -c "${ROOT}"/config/marvel_config_variant.toml -o "${RUN_DIR}"             \
    -g "${RUN_DIR}/two_source/geno_all.txt" -s final -n 8


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GWAS LOOKUPS

# [snellius] resolve gene/outcome lookups, discover studies, write job-array
# file (ascvd: FinnGen I9_CVD_HARD only, efo_id NA in icd_codes.txt)
run_mamba biomed-api "${ROOT}"/src/gwas_cat_prep.py

# [snellius] filter GWAS catalog results to the gene regions (downloads the
# sumstats); each array task does STEP studies and skips those whose outfile
# exists, so a rerun only adds the missing ones
TASKS="${ROOT}"/data/temp/tasks.tsv
STEP=10
N_TASKS=$(( ($(wc -l < "${TASKS}") - 1 + STEP - 1) / STEP ))
TASK_LOGS="${ROOT}"/src/logs/filter_task_logs
mkdir -p "${TASK_LOGS}"
sbatch --array=1-"${N_TASKS}"%20 --partition=rome --cpus-per-task=1        \
    --mem=8G --time=04:00:00 --job-name=filter_gwas_cat                        \
    --output="${TASK_LOGS}"/%x_%A_%a.log                                       \
    --wrap "${ROOT}/src/filter_gwas_cat.sh ${TASKS} \${TMPDIR} ${STEP} \
        \$(( (SLURM_ARRAY_TASK_ID - 1) * ${STEP} + 1 ))"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NON-AGGREGATED ANALYSES
# TODO AoU

# [snellius] marvel per-variant association, one job-array row per gene x
# subset; on Myriad this took up to 48G / 68 h: rerun rows that run out of
# memory or time with more (e.g. --partition=fat_rome --mem=48G
# --time=68:00:00); the stores are built under UKB CARRIER BURDEN
run_mamba marvel_old "${ROOT}"/src/create_config.py -a
TASKS="${ROOT}"/data/raw/marvel_tasks.tsv
N_TASKS=$(( $(wc -l < "${TASKS}") - 1 ))
TASK_LOGS="${ROOT}"/src/logs/marvel_task_logs
mkdir -p "${TASK_LOGS}"
sbatch --array=1-"${N_TASKS}" --partition=rome --cpus-per-task=1 --mem=16G \
    --time=24:00:00 --job-name=marvel_assoc                                    \
    --output="${TASK_LOGS}"/%x_%A_%a.log                                       \
    --wrap "MARVEL_ENV=marvel_old ${ROOT}/src/marvel_assoc.sh ${TASKS} \
        \${TMPDIR} 1 \${SLURM_ARRAY_TASK_ID}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MERGE

# [snellius] adds GWAS Catalog associations + Open Targets gene-burden
# evidence and the marvel results listed in marvel_results.tsv with ≥ 5
# carriers (resources in the script's #SBATCH lines)
sbatch "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INTERMEDIATE MATCH

# [snellius] match GWAS lookups to the gene variant lists
run_mamba biomed-api "${ROOT}"/src/match_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UKB CARRIER BURDEN

# [snellius] 0/1 carrier exposure per gene and mask (<GENE>_lof,
# <GENE>_lof_directed, <GENE>_gof; _fb: without the Thomassen AD sites of
# matched_variants.tsv.gz), the old marvel (10039b6) cnfs and the job array
# data/raw/marvel_burden_tasks.tsv. Needs data/temp/<GENE>_variant_extraction
# .tsv.gz, matched_variants.tsv.gz and lipids_full_pheno.tsv.gz; exposure
# files are individual-level, never commit them.
# <SNELLIUS_ENV>: needs pandas and log_tools (not biomed_api)
sbatch --partition=rome --cpus-per-task=1 --mem=8G --time=04:00:00          \
    --job-name=burden_exposure --output="${ROOT}"/src/logs/%x_%j.log           \
    --wrap "mamba run --no-capture-output -n prot_misc \
        python ${ROOT}/src/burden_exposure.py"
# [snellius] old marvel per job-array row (gene x subset x main/_fb file);
# 16G fits the 1/8-node billing unit of rome
TASKS="${ROOT}"/data/raw/marvel_burden_tasks.tsv
N_TASKS=$(( $(wc -l < "${TASKS}") - 1 ))
TASK_LOGS="${ROOT}"/src/logs/marvel_burden_logs
mkdir -p "${TASK_LOGS}"
sbatch --array=1-"${N_TASKS}" --partition=rome --cpus-per-task=1 --mem=16G \
    --time=04:00:00 --job-name=marvel_burden                                   \
    --output="${TASK_LOGS}"/%x_%A_%a.log                                       \
    --wrap "MARVEL_ENV=marvel_old ${ROOT}/src/marvel_assoc.sh ${TASKS} \
        \${TMPDIR} 1 \${SLURM_ARRAY_TASK_ID}"
# [snellius] per-gene stores of the per-variant (NON-AGGREGATED ANALYSES)
# and burden results, listed in marvel_results.tsv; then rerun MERGE and
# INTERMEDIATE MATCH, so matched_variants.tsv.gz and matched_burden.tsv.gz
# hold both. A store is built from the loose files of the listed task files:
# always list both. Add --refresh on the first Snellius run (Myriad-built
# stores are then kept aside with a time stamp), and only while no loose
# files were archived (--archive)
run_mamba biomed-api "${ROOT}"/src/marvel_results_table.py --ancestry MULTI \
    --tasks "${ROOT}"/data/raw/marvel_tasks.tsv \
    "${ROOT}"/data/raw/marvel_burden_tasks.tsv


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

# [snellius] study accessions; the UKB ones are written by
# marvel_results_table.py: marvel_ukb_<MULTI|EUR>_<outcome>, + _<stratum>
# for the APOE strata
THOMASSEN_STUDIES=(GCST90861026 GCST90861027 GCST90861029 GCST90861030)
FINNGEN_STUDIES=(F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD I9_CVD_HARD)
OUTCOMES=(
    {all_cause,alzheimers,vascular,frontotemporal}_dementia
    ascvd apoa apob hdl_c ldl_c tg
)
UKB_EUR_GROUPS=()
UKB_EUR_STUDIES=()
UKB_STUDIES=()
for outcome in "${OUTCOMES[@]}"; do
    UKB_EUR_GROUPS+=("marvel_ukb_EUR_${outcome}")
    for stratum in "" _e44 _e43 _e33 _e22_e32; do
        UKB_STUDIES+=("marvel_ukb_MULTI_${outcome}${stratum}")
        UKB_EUR_STUDIES+=("marvel_ukb_EUR_${outcome}${stratum}")
    done
done
# TODO AoU: marvel_aou_<EUR|MULTI>_<outcome>[_<stratum>] once its carrier
# burden is in matched_burden.tsv.gz (marvel_results_table.py has the
# cohort hard-coded as ukb)
AOU_EUR_STUDIES=()
AOU_STUDIES=()

# one set of runs per variant set (Constants.BURDEN_VARIANT_SETS);
# --ukb-burden: each cohort's gene estimate is its carrier-burden estimate
# (UKB CARRIER BURDEN, matched_burden.tsv.gz), pooled by IVW over cohorts
VARIANT_SETS=(lof gof am ptv clinvar ptv_am am_clinvar ptv_clinvar_am)
for variant_set in "${VARIANT_SETS[@]}"; do
    case "${variant_set}" in
        lof)            VARIANT_SOURCES=(PTV ClinVar) ;;
        gof)            VARIANT_SOURCES=(GoF) ;;
        am)             VARIANT_SOURCES=(AM) ;;
        ptv)            VARIANT_SOURCES=(PTV) ;;
        clinvar)        VARIANT_SOURCES=(ClinVar) ;;
        ptv_am)         VARIANT_SOURCES=(PTV AM) ;;
        am_clinvar)     VARIANT_SOURCES=(AM ClinVar) ;;
        ptv_clinvar_am) VARIANT_SOURCES=(PTV ClinVar AM) ;;
    esac
    # [snellius] main: carrier burden per cohort (UKB EUR; AoU later)
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
        --studies "${UKB_EUR_STUDIES[@]}" "${AOU_EUR_STUDIES[@]}" \
        --variant-sources "${VARIANT_SOURCES[@]}" --stratified \
        --label "cohort_burden_eur_${variant_set}" --ukb-burden
    # [snellius] main, all ancestries
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
        --studies "${UKB_STUDIES[@]}" "${AOU_STUDIES[@]}" \
        --variant-sources "${VARIANT_SOURCES[@]}" --stratified \
        --label "cohort_burden_multi_${variant_set}" --ukb-burden
    # [snellius] sensitivity: + Thomassen and FinnGen per-variant estimates;
    # UKB and FinnGen add only the variants Thomassen lacks (UKB as the _fb
    # mask)
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
        --studies "${THOMASSEN_STUDIES[@]}" "${UKB_EUR_STUDIES[@]}" \
        "${FINNGEN_STUDIES[@]}" \
        --variant-sources "${VARIANT_SOURCES[@]}" --stratified \
        --prefer-groups thomassen \
        --fallback-groups "${UKB_EUR_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
        --label "pooled_eur_${variant_set}" --ukb-burden
done


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIGURES

# [local] copy results/output/{burden,meta}_*_{cohort_burden,pooled}_*.tsv.gz
# from Snellius first; only FigureNames.MAIN_FIGURES are written to
# results/figures, the rest to results/figures/sensitivity
# [local] main: positive controls (lipids + ASCVD) and dementia, per gene one
# row per variant set (default PTV, AM, PTV + AM)
for panel in controls dementia; do
    run_mamba plot-misc "${ROOT}"/src/cohort_burden_forest.py --ancestry EUR \
        --label cohort_burden_eur --panel "${panel}"
    run_mamba plot-misc "${ROOT}"/src/cohort_burden_forest.py \
        --ancestry MULTI --label cohort_burden_multi --panel "${panel}"
done
# [local] main: CETP UKB burden vs the FinnGen variants (why the pooled
# sensitivity differs)
run_mamba plot-misc "${ROOT}"/src/cetp_cohort_variants_forest.py
for variant_set in "${VARIANT_SETS[@]}"; do
    # [local] main: ASCVD vs dementia odds ratio per gene
    run_mamba plot-misc "${ROOT}"/src/ascvd_dementia_scatter.py \
        --ancestry EUR --label "cohort_burden_eur_${variant_set}"
    # [local] sensitivity: APOE strata of the main analysis, and the pooled
    # UKB + Thomassen + FinnGen analysis (with the lipid panel)
    run_mamba plot-misc "${ROOT}"/src/burden_apoe_forest.py --ancestry EUR \
        --label "cohort_burden_eur_${variant_set}"
    run_mamba plot-misc "${ROOT}"/src/pooled_forest.py --ancestry EUR \
        --label "pooled_eur_${variant_set}"
done
