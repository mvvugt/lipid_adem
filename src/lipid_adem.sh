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

# [myriad] fixed-effect IVW meta-analysis of the matched variants
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --group-by variant
