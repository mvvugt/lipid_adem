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
# Obtain publicly available results

# [myriad] resolve gene/outcome lookups, discover studies, write job-array file
run_mamba biomed-api "${ROOT}"/src/gwas_cat_prep.py

# [myriad] filter GWAS catalog results for MAF
# runlog run --id filter_gwas_cat --order 21 --root "$ROOT" --                     \
#     bash -c 'source "$0" && run_mamba "$@"' "$ROOT"/src/utils/functions.sh     \
run_mamba biomed-api pyjasub "${ROOT}"/config/filter_task.cnf

# [myriad] adds GWAS Catalog associations + Open Targets gene-burden evidence
run_mamba biomed-api "${ROOT}"/src/merge_associations.py
