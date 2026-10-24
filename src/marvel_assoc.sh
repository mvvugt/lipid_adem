#!/bin/bash

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pyjasub task-script wrapper for per-gene marvel association runs

# Parameters
# ----------
#   $1 - ja_file  : Path to data/raw/marvel_tasks.tsv (pyjasub job-array
#                   file, one row per gene: rowidx, gene, carriers, outdir,
#                   config). The configs are written by
#                   src/create_config.py -a.
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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCTIONS

# -----------------------------------------------------------------------
# Print the gene, carriers, outdir and config of job-array rows,
# tab-separated.
#
# Parameters
# ----------
#   $1 - ja_file : Job-array file with a header holding `rowidx`, `gene`,
#                  `carriers`, `outdir` and `config`.
#   $2 - first   : First `rowidx` to print.
#   $3 - last    : Last `rowidx` to print.
#
# Returns
# -------
#   0 on success, 1 if a required column is missing.
#
# Outputs
# -------
#   One `gene<TAB>carriers<TAB>outdir<TAB>config` line per row on stdout.
# -----------------------------------------------------------------------
read_task_rows() {
    local ja_file="${1:?Error: ja_file required}"
    local first="${2:?Error: first required}"
    local last="${3:?Error: last required}"
    awk -F'\t' -v OFS='\t' -v first="$first" -v last="$last" '
        NR == 1 {
            for (i = 1; i <= NF; i++) col[$i] = i
            if (!("rowidx" in col) || !("gene" in col) ||
                !("carriers" in col) || !("outdir" in col) ||
                !("config" in col)) exit 1
            next
        }
        $col["rowidx"] >= first && $col["rowidx"] <= last {
            print $col["gene"], $col["carriers"], $col["outdir"],
                $col["config"]
        }
    ' "$ja_file"
}

# -----------------------------------------------------------------------
# Copy a marvel log out of the staging dir before it is removed. A failed
# copy only warns, so it never hides the marvel error itself.
#
# Parameters
# ----------
#   $1 - src  : The marvel log in the staging dir.
#   $2 - dest : Where to keep it (its directory is created).
#
# Returns
# -------
#   0 always.
# -----------------------------------------------------------------------
keep_log() {
    local src="${1:?Error: src required}"
    local dest="${2:?Error: dest required}"
    if ! mkdir -p "$(dirname "$dest")" || ! cp "$src" "$dest"; then
        log_warn "could not keep ${src} as ${dest}"
    fi
    return 0
}

# -----------------------------------------------------------------------
# Run marvel for one gene in a staging dir; move the results to `outdir`
# only when the run finished successfully.
#
# Parameters
# ----------
#   $1 - gene     : Gene symbol (used in log lines and staging dir name).
#   $2 - carriers : Path to the gene's marvel carriers file (checked
#                   here; marvel reads it from the config).
#   $3 - outdir   : Final results directory; skipped when it exists.
#   $4 - config   : The gene's marvel config (src/create_config.py).
#
# Returns
# -------
#   0 on success or skip, 1 on failure.
#
# Outputs
# -------
#   `outdir` with marvel's `{exposure}_results.tsv.gz` and baseline
#   files, plus `marvel.log` and a copy of the `marvel.cnf` used.
#   marvel runs inside the staging dir, so the config's relative
#   tmp_dir/checkpoint_dir end up there and are removed with it.
# -----------------------------------------------------------------------
run_gene() {
    local gene="${1:?Error: gene required}"
    local carriers="${2:?Error: carriers required}"
    local outdir="${3:?Error: outdir required}"
    local config="${4:?Error: config required}"
    local out_stage
    if [[ -d "$outdir" ]]; then
        log_info "${gene}: ${outdir} exists, skipping" no-record
        return 0
    fi
    if [[ ! -r "$carriers" ]]; then
        log_error "${gene}: carriers file not readable: ${carriers}"
        return 1
    fi
    if [[ ! -r "$config" ]]; then
        log_error "${gene}: config not readable (run create_config.py -a):"\
            "${config}"
        return 1
    fi
    STAGE_DIR="$(mktemp -d "${TMP_LOC}/marvel_${gene}_XXXXXX")"
    out_stage="${STAGE_DIR}/out"
    mkdir -p "$out_stage"
    cp "$config" "${out_stage}/marvel.cnf"
    log_info "${gene}: dry run" no-record
    # marvelous only logs (console and --log-file) with -v
    ( cd "$STAGE_DIR" && run_mamba "$MARVEL_ENV" marvelous \
        "${out_stage}/marvel.cnf" -v --dry-run \
        --log-file "${STAGE_DIR}/dry_run.log" ) || true
    if ! grep -qsF "$DRY_RUN_OK" "${STAGE_DIR}/dry_run.log"; then
        # old marvel (10039b6) writes errors to --log-file only: keep it
        keep_log "${STAGE_DIR}/dry_run.log" \
            "$(dirname "$outdir")/${gene}.dry_run.failed.log"
        log_error "${gene}: config check failed, see"\
            "$(dirname "$outdir")/${gene}.dry_run.failed.log"
        rm -rf "$STAGE_DIR"
        STAGE_DIR=""
        return 1
    fi
    log_info "${gene}: association run" no-record
    ( cd "$STAGE_DIR" && run_mamba "$MARVEL_ENV" marvelous \
        "${out_stage}/marvel.cnf" -v --outpath "$out_stage" \
        --log-file "${out_stage}/marvel.log" ) || true
    if ! grep -qsF "$RUN_OK" "${out_stage}/marvel.log"; then
        keep_log "${out_stage}/marvel.log" \
            "$(dirname "$outdir")/${gene}.marvel.failed.log"
        log_error "${gene}: marvel run failed, see"\
            "$(dirname "$outdir")/${gene}.marvel.failed.log"
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
    log_error "'$JA' lacks rowidx/gene/carriers/outdir/config columns"
    exit 1
fi

N_FAILED=0
while IFS=$'\t' read -r gene carriers outdir config; do
    if [[ -z "$gene" ]]; then
        log_info "task ${IDX}: no job-array row in ${IDX}-${LAST}" no-record
        continue
    fi
    if ! run_gene "$gene" "$carriers" "$outdir" "$config"; then
        N_FAILED=$(( N_FAILED + 1 ))
    fi
done <<< "$ROWS"

log_info "ended at $(date)" no-record
if (( N_FAILED > 0 )); then
    log_error "task ${IDX}: ${N_FAILED} gene(s) failed, rerun to retry"
    exit 1
fi
log_info "*** END ***" no-record
