#!/bin/bash -l
#$ -N gwas_cat_prep
#$ -o src/logs/gwas_cat_prep.log
#$ -j y
#$ -l h_rt=00:30:00
#$ -l mem=2G
#$ -wd /myriadfs/home/rmgpmva/projects/lipid_adem


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
USAGE=$(cat <<EOF
====== lipid_adem_prep ======

Prepare GWAS catalog extraction by mapping traits (ICD) to EFO, reolving gene
regions, discovering GWAS catalog studies, and writing the job-array file for 
actual extraction.

USAGE: $(basename "$0") [-r ROOT] [-t TMP_DIR] [-v]

EOF
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SETUP

. shflags

DEFINE_string 'root' \
    '.' \
    'Root directory of the lipid_adem repo' 'r'
DEFINE_string 'tmp_dir' \
    '' \
    'Override the base dir for the temporary working dir (default: $TMPDIR)' 't'
DEFINE_boolean 'verbose' false 'Print more output' 'v'

FLAGS_HELP="$USAGE"

FLAGS "$@" || exit $?
eval set -- "${FLAGS_ARGV}"

# *** IMPORTANT *** - This must be done after shflags has finished
VERBOSE_TO_STDERR=1
. bh_init.sh

echo_prog_name "$0"
info_msg "SGE job ID: ${JOB_ID:-n/a} | name: ${JOB_NAME:-n/a} | node: ${HOSTNAME:-n/a}"
set_verbose_arg

ROOT="${FLAGS_root}"

export RUNLOG_ROOT="${ROOT}"
RUNLOG_SCRIPT_ID="$(basename "$0" .sh)"
export RUNLOG_SCRIPT_ID
# shellcheck disable=SC1090  # resolved at runtime via console script
source "$(runlog-setup-path)"
runlog_setup

set -euo pipefail

_combined_exit_trap() {
    local exit_code="$?"
    _runlog_teardown "${exit_code}"
    ( exit "${exit_code}" )
    clean_exit
}
trap '_combined_exit_trap' EXIT


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHECKS

check_dir_readable "${ROOT}"
log_info "using root directory: ${ROOT}"
log_info "running on node: $(hostname), job id: ${JOB_ID:-NA}"

module load python3/3.9


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# START

# NOTE use run_mamba
"${ROOT}/src/gwas_cat_prep.py"
