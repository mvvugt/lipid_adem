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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VARIANT ANNOTATION
# TODO annotate variants using GoF and VEP+LOFTEE

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

run_mamba marvel "${ROOT}"/src/annotate_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GWAS LOOKUPS

# [myriad] resolve gene/outcome lookups, discover studies, write job-array file
run_mamba biomed-api "${ROOT}"/src/gwas_cat_prep.py

# [myriad] filter GWAS catalog results to the gene regions
run_mamba biomed-api pyjasub "${ROOT}"/config/filter_task.cnf


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NON-AGGREGATED ANALYSES
# TODO AoU

# [myriad] marvel association per gene
run_mamba marvel "${ROOT}"/src/create_config.py -a
run_mamba biomed-api pyjasub "${ROOT}"/config/marvel_task.cnf

# [myriad] combine all marvel results
# Add --archive to tar the loose files, --refresh to rebuild the stores
run_mamba biomed-api "${ROOT}"/src/marvel_results_table.py --ancestry MULTI


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# APOE GENOTYPE

# [myriad] associate apoe-status (genotype column of the pheno file, vs
# e3e3) with outcomes
run_mamba marvel "${ROOT}"/src/create_config.py -a \
    -t "${ROOT}"/data/raw/marvel_apoe_tasks.tsv
run_mamba biomed-api pyjasub "${ROOT}"/config/marvel_apoe_task.cnf


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MERGE

# [myriad] adds GWAS Catalog associations + Open Targets gene-burden evidence
# and the marvel results listed in marvel_results.tsv with ≥ 5 carriers
qsub "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INTERMEDIATE MATCH

# [myriad] match GWAS lookups to the gene variant lists
run_mamba biomed-api "${ROOT}"/src/match_variants.py
# [myriad] filter GWAS for MAF, keep all marvel, no other variant selection
run_mamba biomed-api "${ROOT}"/src/match_variants.py --region-rare \
    --max-maf 0.01


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

# [myriad] fixed-effect IVW meta-analysis of the matched variants
# TODO why still in here?
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR

# [myriad] main meta-analysis: Thomassen and EUR UKB + FinnGen where Thomassen
# lacks variant
THOMASSEN_STUDIES=(GCST90861026 GCST90861027 GCST90861029 GCST90861030)
FINNGEN_STUDIES=(F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD)
UKB_EUR_GROUPS=(
    marvel_ukb_EUR_{all_cause,alzheimers,vascular,frontotemporal}_dementia
)
UKB_GROUPS=(
    marvel_ukb_MULTI_{all_cause,alzheimers,vascular,frontotemporal}_dementia
)
# UKB accessions are written by marvel_results_table.py:
# marvel_ukb_<MULTI|EUR>_<outcome>, + _<stratum> for the APOE strata
UKB_OUTCOMES=(all_cause alzheimers vascular frontotemporal)
UKB_STUDIES=()
UKB_EUR_STUDIES=()
for outcome in "${UKB_OUTCOMES[@]}"; do
    for stratum in "" _e44 _e43 _e33 _e22_e32; do
        UKB_STUDIES+=("marvel_ukb_MULTI_${outcome}_dementia${stratum}")
        UKB_EUR_STUDIES+=("marvel_ukb_EUR_${outcome}_dementia${stratum}")
    done
done
ARMB_STUDIES=("${UKB_STUDIES[@]}" "${FINNGEN_STUDIES[@]}")
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --studies "${THOMASSEN_STUDIES[@]}" "${UKB_EUR_STUDIES[@]}" \
    "${FINNGEN_STUDIES[@]}" \
    --variant-sources PTV ClinVar GoF landfors_paper --stratified \
    --prefer-groups thomassen \
    --fallback-groups "${UKB_EUR_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
    --label annotated_eur
# [myriad] sensitivity using all UKB samples
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${THOMASSEN_STUDIES[@]}" "${UKB_STUDIES[@]}" \
    "${FINNGEN_STUDIES[@]}" \
    --variant-sources PTV ClinVar GoF landfors_paper --stratified \
    --prefer-groups thomassen \
    --fallback-groups "${UKB_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
    --label maf_filter_all

# [myriad] without the variant lists: every rare variant in the gene region,
# alt-allele effects, NOT oriented by gene function
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --outcomes alzheimers_dementia \
    --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 \
    --region-rare --stratified --label thomassen_ad_region_rare
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${ARMB_STUDIES[@]}" \
    --region-rare --stratified --label armb_dementia_region_rare
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${UKB_STUDIES[@]}" \
    --region-rare --stratified --label ukb_dementia_region_rare


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIGURES

# [local] copy results/output/burden_EUR_*.tsv.gz from Myriad first
# TODO still necessary?
for analysis in lists region_rare; do
    for script in burden_forest burden_apoe_forest burden_heatmap; do
        run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry MULTI \
            --label "armb_dementia_${analysis}"
    done
    for script in burden_forest burden_apoe_forest; do
        run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry EUR \
            --label "thomassen_ad_${analysis}"
    done
done

# [local] main analysis figures
for script in burden_forest burden_apoe_forest sources_forest pooled_forest; do
    run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry EUR \
        --label annotated_eur
    run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry MULTI \
        --label maf_filter_all
done

# [local] APOE genotype vs e3e3 (marvel); rsync results/APOE_genotype{,_eur}
# from Myriad first
run_mamba plot-misc "${ROOT}"/src/apoe_genotype_forest.py
