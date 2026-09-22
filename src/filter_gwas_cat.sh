#!/bin/bash
set -Euo pipefail

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pyjasub task-script wrapper for GWAS catalog extraction

# Parameters
# ----------
#   $1 - ja_file  : Path to data/temp/tasks.tsv (pyjasub job-array file).
#   $2 - tmp_loc  : Temp/scratch location (unused here -- filter_task.py
#                   writes straight to each row's `outfile` column).
#   $3 - step     : Step size (unused -- one row per task).
#   $4 - task_id  : Row number to process (1-based, excluding header).
#
# Returns
# -------
#   0 on success, non-zero on failure (propagated from filter_task.py).
# -----------------------------------------------------------------------

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export RUNLOG_ROOT="${REPO_ROOT}"
# shellcheck source=/dev/null
. "${REPO_ROOT}/src/functions.sh"
# shellcheck disable=SC1090
source "$(runlog-setup-path)"
runlog_setup

log_info "repo root=$REPO_ROOT"
log_info "=== $0 ==="
log_info "started at $(date)"
log_info "hostname=${HOSTNAME:-$(hostname)}"

JA="$1"
TMP_LOC="$2"
STEP="$3"
IDX="${4:?Error: task id argument required}"

log_info "job array file=$JA"
log_info "temp location=$TMP_LOC"
log_info "step=$STEP"

if [[ -z "$JA" ]] || [[ ! -r "$JA" ]]; then
    log_error "'$JA' job array file not given or is not readable"
    exit 1
fi

# tasks.tsv columns: rowidx gene study_accession efo_id outcome chrom
# start end outfile source
PULL_LINE=$(( IDX + 1 ))
LINE=$(sed -n "${PULL_LINE}p" "$JA")

if [[ -z "$LINE" ]]; then
    log_error "no row $IDX (line $PULL_LINE) found in $JA"
    exit 1
fi

IFS=$'\t' read -r ROW_IDX GENE STUDY_ACCESSION EFO_ID OUTCOME CHROM START END \
    OUTFILE SOURCE <<< "$LINE"

if [[ "$IDX" -ne "$ROW_IDX" ]]; then
    log_error "idx (task_id) [${IDX}] != rowidx [${ROW_IDX}]"
    exit 1
fi

log_info "gene=$GENE study_accession=$STUDY_ACCESSION outfile=$OUTFILE source=$SOURCE"

run_mamba biomed-api "${REPO_ROOT}/src/filter_gwas_cat.py" \
    --gene "$GENE" \
    --study-accession "$STUDY_ACCESSION" \
    --chrom "$CHROM" \
    --start "$START" \
    --end "$END" \
    --outfile "$OUTFILE" \
    --source "$SOURCE"

log_info "ended at $(date)"
log_info "*** END ***"
