#!/bin/bash -l
#$ -N merge_associations
#$ -o /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/merge_associations.log
#$ -j y
#$ -l h_rt=02:00:00
#$ -l mem=4G
#$ -wd /myriadfs/home/rmgpmva/projects/lipid_adem
#
# NOTE on cost: single-core, serial job. Myriad bills per core with a 1G/core
# default allowance, so mem=4G is billed as 4 cores. Accepted here: the
# curated GWAS Catalog download for one EFO ID is held fully in memory.
#
# NOTE on output: merge_associations.py writes results/output/
# final_results.tsv atomically itself (functions.write_table_atomic), so this
# wrapper does not use bh_init.sh's MOVE_FROM/MOVE_TO working-dir pattern.
#
# Submit after the pyjasub filter array, held until all its tasks finish:
#   qsub -hold_jid <filter job> merge_associations.sh -r /path/to/project

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
USAGE=$(cat <<EOF
====== merge_associations ======

Myriad (SGE) job wrapper for merge_associations.py: gathers the filtered
sumstats listed in data/temp/tasks.tsv, adds curated GWAS Catalog
associations and Open Targets gene-burden evidence, and writes
results/output/final_results.tsv.

USAGE: $(basename "$0") [-r ROOT] [-v]

EOF
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Setup

# shellcheck disable=SC1091  # shflags is on PATH at runtime
. shflags

DEFINE_string 'root' \
    '/myriadfs/home/rmgpmva/projects/lipid_adem' \
    'Root directory of the project' 'r'
# shellcheck disable=SC2034  # FLAGS_verbose read by bh_init.sh
DEFINE_boolean 'verbose' false 'Print more output' 'v'

FLAGS_HELP="$USAGE"

# parse arguments
FLAGS "$@" || exit $?
eval set -- "${FLAGS_ARGV}"

# *** IMPORTANT *** - This must be done after shflags has finished
# shellcheck disable=SC2034  # read by bh_init.sh
VERBOSE_TO_STDERR=1
# shellcheck disable=SC1091  # bh_init.sh is on PATH at runtime
. bh_init.sh

echo_prog_name "$0"
info_msg "SGE job ID: ${JOB_ID:-n/a} | name: ${JOB_NAME:-n/a}" \
    "| node: ${HOSTNAME:-n/a} | slots: ${NSLOTS:-n/a}"
set_verbose_arg

ROOT="${FLAGS_root}"
TASKS_FILE="${ROOT}/data/temp/tasks.tsv"

export RUNLOG_ROOT="${ROOT}"
# shellcheck disable=SC1090  # resolved at runtime via console script
source "$(runlog-setup-path)"
runlog_setup

# fail if any command fails
set -euo pipefail

# Chain runlog's teardown (writes RUN_LOG.md) with bh_init.sh's clean_exit -
# bash keeps only the last-set EXIT trap, and clean_exit's own exit-code
# capture must see the real exit code, hence the subshell.
_combined_exit_trap() {
    local exit_code="$?"
    _runlog_teardown "${exit_code}"
    ( exit "${exit_code}" )
    clean_exit
}
trap '_combined_exit_trap' EXIT

# shellcheck source=/dev/null
. "${ROOT}/src/functions.sh"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### CHECKS ###

check_dir_readable "${ROOT}"
if [[ ! -r "${TASKS_FILE}" ]]; then
    log_error "tasks file not found or not readable: ${TASKS_FILE}"
    exit 1
fi

log_info "using root directory: ${ROOT}"
log_info "tasks file: ${TASKS_FILE}"
log_info "running on node: $(hostname), job id: ${JOB_ID:-NA}"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### START ###

run_mamba biomed-api "${ROOT}/src/merge_associations.py"

log_info "*** END ***"
