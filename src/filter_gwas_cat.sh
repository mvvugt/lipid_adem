#!/bin/bash

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SLURM array-task wrapper for GWAS catalog extraction (src/lipid_adem.sh)

# Parameters
# ----------
#   $1 - ja_file  : Path to data/temp/tasks.tsv (job-array file,
#                   one row per study).
#   $2 - tmp_loc  : Temp/scratch location (unused here -- filter_gwas_cat.py
#                   writes straight to each row's `outfile` column).
#   $3 - step     : Number of rows (studies) this task processes.
#   $4 - task_id  : First row to process (1-based, excluding header).
#
# Returns
# -------
#   0 on success, non-zero on failure (propagated from filter_gwas_cat.py).
# -----------------------------------------------------------------------

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export RUNLOG_ROOT="${REPO_ROOT}"
# shellcheck source=/dev/null
. "${REPO_ROOT}/src/functions.sh"
# shellcheck disable=SC2034  # read by runlog_setup (setup.sh)
RUNLOG_SCRIPT_ID="filter_gwas_cat_job"
# shellcheck disable=SC2034  # read by runlog_setup (setup.sh)
RUNLOG_ORDER=20
# shellcheck disable=SC1090
source "$(runlog-setup-path)"
runlog_setup
# Enable strict mode only after sourcing external code (see
# merge_associations.sh).
set -Eeuo pipefail

# Routine lines are printed only; the one recorded line is the task
# summary below (failures still record via log_error / raw-output tail).
log_info "repo root=$REPO_ROOT" no-record
log_info "=== $0 ===" no-record
log_info "started at $(date)" no-record
log_info "hostname=${HOSTNAME:-$(hostname)}" no-record

JA="$1"
TMP_LOC="$2"
STEP="$3"
IDX="${4:?Error: task id argument required}"

log_info "job array file=$JA" no-record
log_info "temp location=$TMP_LOC" no-record
log_info "step=$STEP" no-record

if [[ -z "$JA" ]] || [[ ! -r "$JA" ]]; then
    log_error "'$JA' job array file not given or is not readable"
    exit 1
fi

if [[ ! "$STEP" =~ ^[1-9][0-9]*$ ]]; then
    log_error "step '$STEP' is not a positive integer"
    exit 1
fi

if [[ ! "$IDX" =~ ^[1-9][0-9]*$ ]]; then
    log_error "task id '$IDX' is not a positive integer"
    exit 1
fi

log_info "task ${IDX}: rows ${IDX}-$(( IDX + STEP - 1 ))"

run_mamba biomed-api "${REPO_ROOT}/src/filter_gwas_cat.py" \
    --tasks-file "$JA" \
    --task-id "$IDX" \
    --step "$STEP"

log_info "ended at $(date)" no-record
log_info "*** END ***" no-record
