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

# [myriad] once all marvel tasks finished: loose per-variant results into
# per-gene stores (results/marvel/<GENE>_results.tsv.gz; new rows warned,
# conflicting rows stop the run), then marvel_results.tsv (+ apoe_strata.tsv
# for stratified runs). --ancestry MULTI: the phenotype file holds all UKB
# ancestries (468,993 samples). Add --archive to tar the loose files,
# --refresh to rebuild the stores (old ones kept)
run_mamba biomed-api "${ROOT}"/src/marvel_results_table.py --ancestry MULTI


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MERGE

# [myriad] adds GWAS Catalog associations + Open Targets gene-burden evidence
# and the marvel results listed in marvel_results.tsv (rows with < 5 carriers
# dropped); rerun merge and match after every marvel_results_table.py run
qsub "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INTERMEDIATE MATCH

# [myriad] match GWAS lookups to the gene variant lists
run_mamba biomed-api "${ROOT}"/src/match_variants.py
# [myriad] no variant lists: every GWAS/marvel row in its gene region with
# MAF < 1% (marvel rows have no MAF, all kept), a1 = GRCh38 ref, a2 = alt;
# writes matched_region_variants.tsv.gz (input of meta --region-rare)
run_mamba biomed-api "${ROOT}"/src/match_variants.py --region-rare \
    --max-maf 0.01


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

# [myriad] fixed-effect IVW meta-analysis of the matched variants, one
# ancestry group per run (default EUR; --ancestry MULTI pools every
# ancestry together, so restrict it with --studies)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR

# [myriad] first analysis: Thomassen 2026 AD, the 4 disjoint APOE strata
# (e44, e43, e33, e22+e32), all non-AM list variants (PTV, ClinVar, GoF,
# landfors_paper; *_lists); pooled and per stratum, plus gene burden.
# ClinVar = P/LP list (annotate_variants.py); GoF and ClinVar raising
# variants flipped (data/raw/clinvar_condition_direction.tsv);
# sensitivity files: *_no_apoe_e2e4 (without APOE e2/e4) and
# burden_*_directed_only (without ClinVar altered/conflicting/unknown).
# Strata per study: data/raw/apoe_strata.tsv; outputs: pooled (per study
# group the unstratified run, or else the IVW of its strata) and
# *_apoe_strata (pooled per APOE stratum)
# arm A (common/imputed GWAS)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --outcomes alzheimers_dementia \
    --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 \
    --variant-sources PTV ClinVar GoF landfors_paper --stratified \
    --label thomassen_ad_lists

# arm B (rare variants: own UKB + FinnGen R13; AoU TODO), the 4 dementia
# outcomes, pooled per outcome (input of the forest plots and the gene x
# outcome heatmap). UKB (MULTI) + FinnGen (EUR), so --ancestry MULTI.
# UKB accessions are written by marvel_results_table.py; once the
# APOE-stratified marvel runs exist, add
# marvel_ukb_MULTI_alzheimers_dementia_{e44,e43,e33,e22_e32}
UKB_STUDIES=(
    marvel_ukb_MULTI_{all_cause,alzheimers,vascular,frontotemporal}_dementia
)
ARMB_STUDIES=(
    "${UKB_STUDIES[@]}"
    F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD
)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${ARMB_STUDIES[@]}" \
    --variant-sources PTV ClinVar GoF landfors_paper --stratified \
    --label armb_dementia_lists

# UKB only, the 4 dementia outcomes (sensitivity: without FinnGen)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${UKB_STUDIES[@]}" \
    --variant-sources PTV ClinVar GoF landfors_paper --stratified \
    --label ukb_dementia_lists

# [myriad] the same 3 runs without the variant lists (--region-rare): every
# rare variant in the gene region, alt-allele effects, NOT oriented by gene
# function (lowering and raising variants cancel out)
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
for analysis in lists region_rare; do
    run_mamba plot-misc "${ROOT}"/src/figures.py --ancestry MULTI \
        --forest-label "armb_dementia_${analysis}" \
        --heatmap-label "armb_dementia_${analysis}"
    run_mamba plot-misc "${ROOT}"/src/figures.py --ancestry EUR \
        --forest-label "thomassen_ad_${analysis}"
done

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
