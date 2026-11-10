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

# marvel 0.5.1 (aftermath b2a948d): worktree + env as in
# docs/marvel_migration_handoff.md, "Snellius to-do" step 1
readonly MARVEL_HASH="b2a948d"
readonly MARVEL_ENV="marvel_${MARVEL_HASH}"
readonly MARVEL_SRC="${HOME}/software/marvel_${MARVEL_HASH}"
readonly SLURM_ARRAY="${MARVEL_SRC}/resources/workflows/slurm_array.sh"
# extract chunks + the final (aggregate + associate) runs on them
readonly MARVEL_RUN="${ROOT}/data/temp/marvel"
# APOE diplotype runs (associate only, no chunks)
readonly MARVEL_APOE_RUN="${ROOT}/data/temp/marvel_apoe"
# one row per run, written by create_config.py:
# analysis, subset, stage (final|associate), prefix, config
readonly MARVEL_RUNS="${ROOT}/data/raw/marvel_runs.tsv"


# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Submit the marvel runs of one analysis in MARVEL_RUNS.
#
# stage final: slurm_array.sh -s final on the extract chunks in
# MARVEL_RUN. stage associate: marvelous associate into MARVEL_APOE_RUN.
# Jobs of one stage share a job name and run one at a time
# (--dependency=singleton): they share an output dir, its
# aggregate/associate logs and the RUN_LOG.md script ID of slurm_array.sh
# (log_tools race, docs/log_tools_runlog_race_handoff.md).
#
# Parameters
# ----------
#   $1 - analysis : analysis column value (variant, burden, burden_fb,
#                   apoe).
#   $2 - cpus     : cores per job, also marvelous --n-jobs.
#   $3 - mem      : sbatch --mem, e.g. 16G.
#   $4 - walltime : sbatch --time, e.g. 04:00:00.
#
# Returns
# -------
#   0 on success, 1 on an unknown stage or no run of the analysis.
#
# Outputs
# -------
#   One SLURM job per run; logs in MARVEL_RUN/two_source/logs or
#   MARVEL_APOE_RUN/logs (mv_<stage>_<prefix>_<jobid>.log).
#
# Example
# -------
#   submit_marvel_runs burden 8 16G 04:00:00
# -----------------------------------------------------------------------
submit_marvel_runs() {
    local analysis="${1:?Error: analysis required}"
    local cpus="${2:?Error: cpus required}"
    local mem="${3:?Error: mem required}"
    local walltime="${4:?Error: walltime required}"
    local run_analysis subset stage prefix config log_dir
    local n_runs=0
    while IFS=$'\t' read -r run_analysis subset stage prefix config; do
        if [[ "${run_analysis}" != "${analysis}" ]]; then
            continue
        fi
        n_runs=$(( n_runs + 1 ))
        echo "[info] ${analysis} ${subset}: ${stage} ${config}"
        case "${stage}" in
            final)
                log_dir="${MARVEL_RUN}/two_source/logs"
                mkdir -p "${log_dir}"
                sbatch --partition=rome --cpus-per-task="${cpus}"          \
                    --mem="${mem}" --time="${walltime}"                    \
                    --job-name=mv_final --dependency=singleton             \
                    --output="${log_dir}/mv_final_${prefix}_%j.log"        \
                    --wrap "mamba run --no-capture-output -n ${MARVEL_ENV} \
                        ${SLURM_ARRAY} -c ${config} -o ${MARVEL_RUN} \
                        -g ${MARVEL_RUN}/two_source/geno_all.txt \
                        -s final -n ${cpus} -r ${ROOT}"
                ;;
            associate)
                log_dir="${MARVEL_APOE_RUN}/logs"
                mkdir -p "${log_dir}"
                sbatch --partition=rome --cpus-per-task="${cpus}"          \
                    --mem="${mem}" --time="${walltime}"                    \
                    --job-name=mv_associate --dependency=singleton         \
                    --output="${log_dir}/mv_associate_${prefix}_%j.log"    \
                    --wrap "mamba run --no-capture-output -n ${MARVEL_ENV} \
                        marvelous associate ${config} \
                        --outdir ${MARVEL_APOE_RUN} --n-jobs ${cpus}"
                ;;
            *)
                echo "[error] ${MARVEL_RUNS}: unknown stage ${stage}" >&2
                return 1
                ;;
        esac
    done < <(tail -n +2 "${MARVEL_RUNS}")
    if (( n_runs == 0 )); then
        echo "[error] ${MARVEL_RUNS}: no run of ${analysis}" >&2
        return 1
    fi
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PHENOTYPES
# TODO add the commands that build the phenotype files here

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

# Issues found with validation/check_pheno.py in cetp_marvel's
# pheno_cov.tsv.gz (2026-10-26); fix in the outcome build, then rebuild:
# - <outcome>_incident for the dementias: prevalent cases coded 0
#   (counted as controls); should be NA
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
# VARIANT ANNOTATION

# [snellius] VEP/LOFTEE consequences per gene, region read from the
# indexed per-chromosome VEP VCFs (-p pattern with {chrom})
LOF_DIR="/projects/0/aus20644/data/ukbiobank/genetics/b38/lof"
sbatch "${ROOT}"/src/vep_extract.sh -r "${ROOT}" -o "${ROOT}"/data/temp        \
    -d "${LOF_DIR}" -g "${ROOT}"/data/raw/gene_list.txt                        \
    -p "chr{chrom}_merged_vep.vcf.gz" -v

# [snellius] LOFTEE HC PTVs on the canonical transcript
run_mamba biomed-api "${ROOT}"/src/annotate_ptv.py

# [local] query ClinVar for all variants in the curated genes
mapfile -t genes < <(cut -f1 "${ROOT}/data/raw/gene_list.txt")
runlog run --id clinvar_filter --order 40 --root "${ROOT}" --                  \
    mamba run --no-capture-output -n clinvar-build                             \
    clinvar-filter                                                             \
    "${HOME}/Documents/work.nosync/data/clinvar/clinvar_vcv.db"                \
    --rcv-db "${HOME}/Documents/work.nosync/data/clinvar/clinvar_rcv.db"       \
    -g "${genes[@]}"                                                           \
    -o "${ROOT}/data/raw/clinvar_variants.tsv"                                 \
    -vvv

# [snellius] annotate clinvar variants
run_mamba biomed-api "${ROOT}"/src/annotate_clinvar.py

# [snellius] combine PTV + ClinVar + GoF normalised against GRCh38
run_mamba biomed-api "${ROOT}"/src/combine_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CARRIER EXTRACTION

# TODO RAP extraction not implemented: plan in docs/rap_carrier_extraction.md

# list full-sample vcf-files for some genes; exclude one of the chr1 genes
realpath "${ROOT}"/../cetp_marvel/data/temp/*plink*vcf.gz |
    grep -v PCSK9 > "${ROOT}"/data/raw/plink_gene_vcfs.txt
DATA_DIR="/gpfs/work2/0/aus20644/data"
REF_DIR="${DATA_DIR}/resources/human_genome/b38"
LOF_DIR="${DATA_DIR}/ukbiobank/genetics/b38/lof"

# [snellius] collapse the two forms per variant (no merge on conflict) into
# data/temp/<GENE>_variant_extraction.tsv.gz (read by marvel_tasks.tsv)
# TODO if individual data/temp/<GENE>_variants.tsv doe not exist, but data/processed/lipid_variants does, create the individual files anytime the individual ones are needed (not in marvel itself of course, but before marvel submission e.g.)
"${ROOT}"/src/submit_two_source.sh                                             \
    -c "${ROOT}"/config/marvel_config.toml                                     \
    -p "${ROOT}"/data/raw/plink_gene_vcfs.txt                                  \
    -P "${LOF_DIR}"'/chr{chrom}_merged_vep.vcf.gz'                             \
    -R "${REF_DIR}/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz"             \
    -o "${ROOT}"/data/temp/marvel                                              \
    -o "${MARVEL_RUN}" -a "${SLURM_ARRAY}" -e "${MARVEL_ENV}"                 \
    -m '2023 BCFtools/1.18-GCC-12.3.0'

# [snellius] new marvel TOMLs (config/marvel/<analysis>_<subset>.toml),
# MARVEL_RUNS and the per-variant list (lipid_variants.tsv minus APOE);
# checks the stratum values in the phenotype file. The burden TOMLs read
# the mask lists of burden_exposure.py --mask-lists (UKB CARRIER BURDEN)
run_mamba biomed-api "${ROOT}"/src/create_config.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# APOE DIPLOTYPE
# Each diplotype vs all others; all samples and EUR (overall).

# [snellius] exposure file with binary carrier column per diplotype
run_mamba biomed-api "${ROOT}"/src/apoe_exposure.py

# [snellius] marvelous associate per subset (input.exposures)
submit_marvel_runs apoe 4 16G 04:00:00

# [local] figure on the copies of MARVEL_APOE_RUN/lipid_apoe_*.results.tsv.gz
run_mamba plot-misc "${ROOT}"/src/apoe_genotype_forest.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GWAS LOOKUPS

# [snellius] discover GWAS lookup studies, write job-array file
run_mamba biomed-api "${ROOT}"/src/gwas_cat_prep.py

# [snellius] download sumstats of GWAS catalog for the gene regions
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

# [snellius] marvel per-variant association (additive dosage) on the
# extract chunks; subsets all, all_apoe, eur
submit_marvel_runs variant 32 64G 12:00:00


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MERGE

# [snellius] merge GWAS Catalog, Open Targets gene-burden, and marvel_results.tsv
sbatch "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INTERMEDIATE MATCH

# [snellius] match GWAS lookups to the gene variant lists
run_mamba biomed-api "${ROOT}"/src/match_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UKB CARRIER BURDEN

# [snellius] long mask lists (mask = gene x variant set) for the burden
# TOMLs; genes: lipid_variants.tsv minus APOE. _fb: without the Thomassen
# AD sites of matched_variants.tsv.gz. Needs lipid_variants.tsv and
# matched_variants.tsv.gz
sbatch --partition=rome --cpus-per-task=1 --mem=8G --time=04:00:00          \
    --job-name=burden_exposure --output="${ROOT}"/src/logs/%x_%j.log           \
    --wrap "mamba run --no-capture-output -n prot_misc \
        python ${ROOT}/src/burden_exposure.py --mask-lists"

# [snellius] marvel burden (carrier of any site per mask) on the extract
# chunks; subsets all_apoe, eur; main and _fb
submit_marvel_runs burden 8 16G 04:00:00
submit_marvel_runs burden_fb 8 16G 04:00:00

# [snellius] after all final runs of MARVEL_RUNS (per variant + burden):
# copy each <prefix>.results.tsv.gz to results/marvel/<prefix>_results.tsv.gz
# and list them in marvel_results.tsv; then rerun MERGE and INTERMEDIATE
# MATCH, so matched_variants.tsv.gz and matched_burden.tsv.gz hold both
run_mamba biomed-api "${ROOT}"/src/marvel_results_table.py --ancestry MULTI
# TODO script should be completely linear, here we go back (rerun merge and 
# intermediate match), so please update


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

# [snellius] create variables for meta-analysis
THOMASSEN_STUDIES=(GCST90861026 GCST90861027 GCST90861029 GCST90861030)
FINNGEN_STUDIES=(F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD I9_CVD_HARD)

# create names for UKB and AoU analyses
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

# run per variant set
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
    # [snellius] main: carrier burden per cohort
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
        --studies "${UKB_EUR_STUDIES[@]}" "${AOU_EUR_STUDIES[@]}" \
        --variant-sources "${VARIANT_SOURCES[@]}" --stratified \
        --label "cohort_burden_eur_${variant_set}" --ukb-burden
    # [snellius] main, combine ancestries
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
        --studies "${UKB_STUDIES[@]}" "${AOU_STUDIES[@]}" \
        --variant-sources "${VARIANT_SOURCES[@]}" --stratified \
        --label "cohort_burden_multi_${variant_set}" --ukb-burden
    # [snellius] meta-analyse with Thomassen and FinnGen per-variant estimates;
    # variant priority (high to low): Thomassen -> FinnGen -> UKB (_fb mask)
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
        --studies "${THOMASSEN_STUDIES[@]}" "${UKB_EUR_STUDIES[@]}" \
        "${FINNGEN_STUDIES[@]}" \
        --variant-sources "${VARIANT_SOURCES[@]}" --stratified \
        --prefer-groups thomassen \
        --fallback-groups "${UKB_EUR_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
        --label "pooled_eur_${variant_set}" --ukb-burden
done

# [snellius] CETP GoF variants one by one; flipped as GoF (lower function)
for ancestry in EUR MULTI; do
    run_mamba biomed-api "${ROOT}"/src/meta_analysis.py \
        --ancestry "${ancestry}" --variant-sources SelectedGoF --stratified \
        --label "selected_gof_${ancestry,,}" --no-gene-burden \
        --require-expected-scale
done


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIGURES

# [local] figures of results/output/meta* and burden*. Figures in
# FigureNames.MAIN_FIGURES go to results/figures, the rest to sensitivity

# Only UKB: figure per controls/dementia; estimator per variant set
for panel in controls dementia; do
    run_mamba plot-misc "${ROOT}"/src/cohort_burden_forest.py --ancestry EUR   \
        --label cohort_burden_eur --panel "${panel}"
    run_mamba plot-misc "${ROOT}"/src/cohort_burden_forest.py                  \
        --ancestry MULTI --label cohort_burden_multi --panel "${panel}"
done

# Only UKB: figure per gene; estimator per variant set; binary and lipids
run_mamba plot-misc "${ROOT}"/src/variant_sets_forest.py --ancestry EUR        \
    --label cohort_burden_eur

# CETP UKB burden vs the FinnGen variants
run_mamba plot-misc "${ROOT}"/src/cetp_cohort_variants_forest.py

# Meta: figure per variant set; estimator per source; all binary outcomes
run_mamba plot-misc "${ROOT}"/src/sources_forest.py --ancestry EUR             \
    --label pooled_eur

# CETP GoF: figure per variant; estimator per source; binary and lipids
for ancestry in EUR MULTI; do
    run_mamba plot-misc "${ROOT}"/src/selected_variants_forest.py              \
        --ancestry "${ancestry}" --label "selected_gof_${ancestry,,}"
done

for variant_set in "${VARIANT_SETS[@]}"; do
    # scatter per variant set
    run_mamba plot-misc "${ROOT}"/src/ascvd_dementia_scatter.py                \
        --ancestry EUR --label "cohort_burden_eur_${variant_set}"
    # Only UKB: figure per outcome+variant set; estimator per apoe stratum
    run_mamba plot-misc "${ROOT}"/src/burden_apoe_forest.py --ancestry EUR     \
        --label "cohort_burden_eur_${variant_set}"
    # Meta: figure per variant set; estimator per outcome
    run_mamba plot-misc "${ROOT}"/src/pooled_forest.py --ancestry EUR          \
        --label "pooled_eur_${variant_set}"
done
