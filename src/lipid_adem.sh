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
# TODO annotate variants using ClinVar, GoF, and VEP+LOFTEE

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

# [myriad] filter GWAS catalog results for MAF
run_mamba biomed-api pyjasub "${ROOT}"/config/filter_task.cnf

# [myriad] adds GWAS Catalog associations + Open Targets gene-burden evidence
qsub "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NON-AGGREGATED ANALYSES
# TODO analyse variants in UKB and AoU


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
# burden_*_directed_only (without ClinVar altered/conflicting/unknown)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --outcomes alzheimers_dementia \
    --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 \
    --variant-sources PTV ClinVar --stratified \
    --label thomassen_ad_ptv_clinvar
