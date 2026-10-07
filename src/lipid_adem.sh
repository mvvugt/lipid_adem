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

# [myriad] adds GWAS Catalog associations + Open Targets gene-burden evidence
qsub "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NON-AGGREGATED ANALYSES
# TODO AoU

# [myriad] marvel association per gene
run_mamba marvel pyjasub "${ROOT}"/config/marvel_task.cnf


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INTERMEDIATE MATCH

# [myriad] match GWAS lookups to the gene variant lists
run_mamba biomed-api "${ROOT}"/src/match_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

# [myriad] fixed-effect IVW meta-analysis of the matched variants, one
# ancestry group per run (default EUR; e.g. --ancestry MULTI for pooled)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR

# [myriad] first analysis: Thomassen 2026 AD, the 4 disjoint APOE strata
# (e44, e43, e33, e22+e32), PTV + ClinVar variants; pooled and per stratum,
# plus gene burden. ClinVar = P/LP list (annotate_variants.py), GoF
# (raising) variants flipped (data/raw/clinvar_condition_direction.tsv);
# sensitivity files: *_no_apoe_e2e4 (without APOE e2/e4) and
# burden_*_directed_only (without ClinVar altered/conflicting/unknown).
# Strata per study: data/raw/apoe_strata.tsv; outputs: pooled (per study
# group the unstratified run, or else the IVW of its strata) and
# *_apoe_strata (pooled per APOE stratum)
# arm A (common/imputed GWAS)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --outcomes alzheimers_dementia \
    --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 \
    --variant-sources PTV ClinVar --stratified \
    --label thomassen_ad_ptv_clinvar

# arm B (rare variants: own UKB/AoU, FinnGen R13)
# TODO list the marvel runs in marvel_results.tsv (apoe_stratum column)
# and apoe_strata.tsv first; IDs below are placeholders until then
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --outcomes alzheimers_dementia \
    --studies marvel_{ukb,aou}_EUR_alzheimers_dementia{,_e44,_e43} \
    marvel_{ukb,aou}_EUR_alzheimers_dementia_{e33,e22_e32} G6_ALZHEIMER \
    --variant-sources PTV ClinVar --stratified \
    --label armb_ad_ptv_clinvar

# EAS (pooled only, no APOE strata): arm A = Cao 2026 + K-ROAD WGS
# (independent cohorts), arm B = K-ROAD WGS; both via
# gwas_catalog_manual_studies.tsv, so rerun prep/filter/merge/match first.
# NOTE (2026-10-07): neither has rare PTV/P/LP variants. Deposited
# sumstats are MAF-filtered: Cao MAF >= ~5% (0 rows with MAF < 0.01 in the
# gene regions), K-ROAD MAF >= ~0.7% (12 rows with MAF < 0.01, none in the
# variant lists). Without the MAF filter only common listed variants (e.g.
# APOE e2/e4) can match. Kept in case of re-deposited full sumstats.
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EAS \
    --outcomes alzheimers_dementia \
    --studies GCST90727420 GCST90566388 \
    --variant-sources PTV ClinVar --stratified \
    --label arma_ad_ptv_clinvar

run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EAS \
    --outcomes alzheimers_dementia \
    --studies GCST90566388 \
    --variant-sources PTV ClinVar --stratified \
    --label armb_ad_ptv_clinvar
