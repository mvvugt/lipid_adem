#!/bin/bash

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pyjasub task-script wrapper for per-gene marvel association runs

# Parameters
# ----------
#   $1 - ja_file  : Path to data/raw/marvel_tasks.tsv (pyjasub job-array
#                   file, one row per gene: rowidx, gene, carriers, outdir).
#   $2 - tmp_loc  : Temp/scratch location; each gene is staged in a
#                   subdirectory and only moved to `outdir` on success.
#   $3 - step     : Number of rows (genes) this task processes.
#   $4 - task_id  : First row to process (1-based, excluding header).
#
# Environment
# -----------
#   MARVEL_ENV    : mamba env with marvel (commit eed4510, branch
#                   annotation) installed; default `marvel`.
#
# Returns
# -------
#   0 on success, 1 if any gene failed (the other genes still run).
# -----------------------------------------------------------------------

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export RUNLOG_ROOT="${REPO_ROOT}"
# shellcheck source=/dev/null
. "${REPO_ROOT}/src/functions.sh"
# shellcheck disable=SC2034  # read by runlog_setup (setup.sh)
RUNLOG_SCRIPT_ID="marvel_assoc_job"
# shellcheck disable=SC2034  # read by runlog_setup (setup.sh)
RUNLOG_ORDER=50
# shellcheck disable=SC1090
source "$(runlog-setup-path)"
runlog_setup
# Enable strict mode only after sourcing external code (see
# merge_associations.sh).
set -Eeuo pipefail

readonly MARVEL_ENV="${MARVEL_ENV:-marvel}"
readonly BASE_CONFIG="${REPO_ROOT}/config/marvel_assoc.cnf"
# marvelous exits 0 even when the pipeline fails (main() drops the
# return code), so success is read from its log instead
readonly DRY_RUN_OK="Configuration is valid!"
readonly RUN_OK="MARVELous Pipeline Completed Successfully"
STAGE_DIR=""

# Chain the staging cleanup with runlog's teardown (writes RUN_LOG.md) -
# bash keeps only the last-set EXIT trap.
_exit_trap() {
    local exit_code="$?"
    if [[ -n "${STAGE_DIR}" ]]; then
        rm -rf "${STAGE_DIR}"
    fi
    _runlog_teardown "${exit_code}"
}
trap '_exit_trap' EXIT

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
log_info "marvel env=$MARVEL_ENV" no-record

if [[ -z "$JA" ]] || [[ ! -r "$JA" ]]; then
    log_error "'$JA' job array file not given or is not readable"
    exit 1
fi

if [[ -z "$TMP_LOC" ]]; then
    log_error "temp location not given"
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

if [[ ! -r "$BASE_CONFIG" ]]; then
    log_error "marvel config not readable: $BASE_CONFIG"
    exit 1
fi


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCTIONS

# -----------------------------------------------------------------------
# Print the gene, carriers and outdir of job-array rows, tab-separated.
#
# Parameters
# ----------
#   $1 - ja_file : Job-array file with a header holding `rowidx`, `gene`,
#                  `carriers` and `outdir`.
#   $2 - first   : First `rowidx` to print.
#   $3 - last    : Last `rowidx` to print.
#
# Returns
# -------
#   0 on success, 1 if a required column is missing.
#
# Outputs
# -------
#   One `gene<TAB>carriers<TAB>outdir` line per row on stdout.
# -----------------------------------------------------------------------
read_task_rows() {
    local ja_file="${1:?Error: ja_file required}"
    local first="${2:?Error: first required}"
    local last="${3:?Error: last required}"
    awk -F'\t' -v OFS='\t' -v first="$first" -v last="$last" '
        NR == 1 {
            for (i = 1; i <= NF; i++) col[$i] = i
            if (!("rowidx" in col) || !("gene" in col) ||
                !("carriers" in col) || !("outdir" in col)) exit 1
            next
        }
        $col["rowidx"] >= first && $col["rowidx"] <= last {
            print $col["gene"], $col["carriers"], $col["outdir"]
        }
    ' "$ja_file"
}

# -----------------------------------------------------------------------
# Write a gene's marvel config: [ExpInput] + the shared config + the
# per-task [Options] paths.
#
# Parameters
# ----------
#   $1 - carriers  : Path to the gene's marvel carriers file.
#   $2 - stage_dir : Staging directory for marvel's tmp/checkpoint dirs.
#   $3 - out_cnf   : Path of the config to write.
#
# Returns
# -------
#   0 on success, non-zero on failure.
#
# Outputs
# -------
#   Writes `out_cnf`. marvel's parser reopens a repeated section, so the
#   second [Options] block adds to the one in the shared config.
# -----------------------------------------------------------------------
write_task_config() {
    local carriers="${1:?Error: carriers required}"
    local stage_dir="${2:?Error: stage_dir required}"
    local out_cnf="${3:?Error: out_cnf required}"
    {
        printf '[ExpInput]\ncarriers\t%s\n\n' "$carriers"
        cat "$BASE_CONFIG"
        printf '\n[Options]\n'
        printf 'tmp_dir\t%s\n' "${stage_dir}/tmp"
        printf 'checkpoint_dir\t%s\n' "${stage_dir}/checkpoint"
    } > "$out_cnf"
}

# -----------------------------------------------------------------------
# Run marvel for one gene in a staging dir; move the results to `outdir`
# only when the run finished successfully.
#
# Parameters
# ----------
#   $1 - gene     : Gene symbol (used in log lines and staging dir name).
#   $2 - carriers : Path to the gene's marvel carriers file.
#   $3 - outdir   : Final results directory; skipped when it exists.
#
# Returns
# -------
#   0 on success or skip, 1 on failure.
#
# Outputs
# -------
#   `outdir` with marvel's `{exposure}_results.tsv.gz` and baseline
#   files, plus `marvel.log` and the `marvel.cnf` used.
# -----------------------------------------------------------------------
run_gene() {
    local gene="${1:?Error: gene required}"
    local carriers="${2:?Error: carriers required}"
    local outdir="${3:?Error: outdir required}"
    local out_stage
    if [[ -d "$outdir" ]]; then
        log_info "${gene}: ${outdir} exists, skipping" no-record
        return 0
    fi
    if [[ ! -r "$carriers" ]]; then
        log_error "${gene}: carriers file not readable: ${carriers}"
        return 1
    fi
    STAGE_DIR="$(mktemp -d "${TMP_LOC}/marvel_${gene}_XXXXXX")"
    out_stage="${STAGE_DIR}/out"
    mkdir -p "$out_stage"
    write_task_config "$carriers" "$STAGE_DIR" "${out_stage}/marvel.cnf"
    log_info "${gene}: dry run" no-record
    run_mamba "$MARVEL_ENV" marvelous "${out_stage}/marvel.cnf" --dry-run \
        --log-file "${STAGE_DIR}/dry_run.log" || true
    if ! grep -qF "$DRY_RUN_OK" "${STAGE_DIR}/dry_run.log"; then
        log_error "${gene}: config check failed, see marvel output above"
        rm -rf "$STAGE_DIR"
        STAGE_DIR=""
        return 1
    fi
    log_info "${gene}: association run" no-record
    run_mamba "$MARVEL_ENV" marvelous "${out_stage}/marvel.cnf" -v \
        --outpath "$out_stage" --log-file "${out_stage}/marvel.log" || true
    if ! grep -qF "$RUN_OK" "${out_stage}/marvel.log"; then
        log_error "${gene}: marvel run failed, see marvel output above"
        rm -rf "$STAGE_DIR"
        STAGE_DIR=""
        return 1
    fi
    # move next to outdir (a copy across filesystems), then rename, so
    # outdir never holds a partial run
    mkdir -p "$(dirname "$outdir")"
    rm -rf "${outdir}.partial"
    if ! mv "$out_stage" "${outdir}.partial" \
        || ! mv "${outdir}.partial" "$outdir"; then
        log_error "${gene}: could not move results to ${outdir}"
        return 1
    fi
    rm -rf "$STAGE_DIR"
    STAGE_DIR=""
    log_info "${gene}: results in ${outdir}"
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# START

LAST=$(( IDX + STEP - 1 ))
log_info "task ${IDX}: rows ${IDX}-${LAST}"
mkdir -p "$TMP_LOC"

if ! ROWS="$(read_task_rows "$JA" "$IDX" "$LAST")"; then
    log_error "'$JA' lacks rowidx/gene/carriers/outdir columns"
    exit 1
fi

N_FAILED=0
while IFS=$'\t' read -r gene carriers outdir; do
    if [[ -z "$gene" ]]; then
        log_info "task ${IDX}: no job-array row in ${IDX}-${LAST}" no-record
        continue
    fi
    if ! run_gene "$gene" "$carriers" "$outdir"; then
        N_FAILED=$(( N_FAILED + 1 ))
    fi
done <<< "$ROWS"

log_info "ended at $(date)" no-record
if (( N_FAILED > 0 )); then
    log_error "task ${IDX}: ${N_FAILED} gene(s) failed, rerun to retry"
    exit 1
fi
log_info "*** END ***" no-record
