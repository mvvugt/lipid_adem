#!/usr/bin/env bash
# FLAGS_TRUE and the bh_init.sh helpers are defined at run time:
# shellcheck disable=SC2154
#SBATCH --job-name=mv_two_source
#SBATCH --output=%x_%A_%a.log
#SBATCH --partition=rome
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:30:00
#
# MARVELous extraction from two sources on SLURM (Snellius):
#   plink : per-gene VCFs of all individuals (recoded from PLINK)
#   vep   : per-chromosome VEP VCFs of a subset of the individuals, not
#           normalised (multiallelic records, indels not left-aligned)
# Every variant is read from plink when plink has it, else from vep.
#
# Run --stage submit (default) on the login node. It submits:
#   J1 slurm_array.sh extract, one task per plink gene VCF
#   J2 this script --stage vep_prep, one task per chromosome
#      (afterok:J1): the variants J1 did not read, cut from the VEP VCF,
#      split and left-aligned
#   J3 slurm_array.sh extract, one task per prepared VEP chunk
#      (aftercorr:J2: task i starts as soon as prep task i is done)
#   J4 slurm_array.sh --stage final, aggregate + associate (afterok:J3)
#
# NOTE on resources: the #SBATCH lines above are for J2 (vep_prep); the
# submit stage passes every job's resources on the sbatch command line.
# Shared "rome" jobs are billed in 1/8th-node increments.
#
# NOTE on the environment: marvelous and python come from the mamba/conda
# env -e/--env (name or prefix; default marvel), not from the caller's
# PATH. Its bin/ is put first on PATH and every job is submitted with
# --export=ALL, so the jobs need no activation. -i/--image replaces it.
#
# NOTE on outputs: marvelous writes straight into -o/--output (atomic,
# .SUCCESS last). Prepared VEP chunks are written to a temporary name in
# --prep_dir and moved into place, so a failed task leaves nothing.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
USAGE=$(cat <<EOF
====== submit_two_source.sh ======

Extract variants with MARVELous from PLINK gene VCFs (all individuals)
with a VEP VCF fallback (a subset of the individuals). Run on the login
node; it submits four dependent jobs (see the header of this script).

    ./submit_two_source.sh -c config.toml -p plink_gene_vcfs.txt \\
        -P '/path/to/vep/chr{chrom}.vep.vcf.gz' -R ref.fa \\
        -o /path/to/run_outdir -a /path/to/slurm_array.sh [--dry_run]

-c: start from config.toml next to this script (fill its <PLACEHOLDER>s).
-p: one gene VCF per line (indexed). -P: the VEP path with {chrom}, which
is replaced by each chromosome of the variant list without "chr" (e.g.
1, X). marvelous and python come from the mamba env -e (default marvel;
or -i IMAGE.sif); bcftools >= 1.10 from --modules or that env. The
FASTA may name contigs 1 or chr1, independent of the VEP files.

USAGE: $(basename "$0") -c CONFIG -p PLINK_LIST -P VEP_PATTERN -R FASTA
           -o OUTPUT -a SLURM_ARRAY [-d PREP_DIR] [--pad N]
           [-e ENV] [-i IMAGE.sif] [-b BIND] [--modules "MOD ..."]
           [--dry_run] [-r ROOT] [-t TMP_DIR] [-v]

EOF
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Setup

# shellcheck disable=SC1091  # shflags is found on PATH at run time
. shflags

DEFINE_string 'root' \
    '.' \
    'Root directory of the project (home of RUN_LOG.md)' 'r'
DEFINE_string 'output' \
    '<RUN_OUTDIR>' \
    'Run output directory shared by every job (marvelous --outdir)' 'o'
# tmp_dir is read by bh_init.sh; $TMPDIR in the help text is literal.
# shellcheck disable=SC2034,SC2016
DEFINE_string 'tmp_dir' \
    '' \
    'Base dir for the temporary work dir (default: $TMPDIR, set by SLURM)' 't'
DEFINE_boolean 'verbose' false 'Print more output (marvelous -v)' 'v'
DEFINE_string 'stage' 'submit' 'Stage to run: submit or vep_prep' 's'
DEFINE_string 'config' '<CONFIG.toml>' 'MARVELous TOML run config' 'c'
DEFINE_string 'plink_list' \
    '<PLINK_GENE_VCF_LIST.txt>' \
    'File with one PLINK-derived gene VCF per line' 'p'
DEFINE_string 'vep_pattern' \
    '<VEP_DIR>/chr{chrom}.vep.vcf.gz' \
    'VEP VCF path; {chrom} = list chromosome without chr' 'P'
DEFINE_string 'fasta' '<REFERENCE.fa>' 'Reference FASTA (+ .fai)' 'R'
DEFINE_string 'prep_dir' \
    '' \
    'Dir for prepared VEP chunks (default: OUTPUT/two_source/vep)' 'd'
DEFINE_integer 'pad' 250 'bp around each VEP target (un-normalised indels)' 'x'
DEFINE_string 'slurm_array' \
    '<MARVEL_REPO>/resources/workflows/slurm_array.sh' \
    'Path to slurm_array.sh (extract and final jobs)' 'a'
DEFINE_string 'env' 'marvel' 'Mamba/conda env (name or prefix) with marvel' 'e'
DEFINE_string 'image' '' 'Apptainer .sif to run marvelous/python in' 'i'
DEFINE_string 'bind' '' 'Extra Apptainer binds (data dirs), comma separated' 'b'
DEFINE_string 'modules' \
    '' \
    'Modules for vep_prep, space separated (e.g. 2023 BCFtools/1.18-...)' 'm'
DEFINE_string 'partition' 'rome' 'SLURM partition for every job' 'q'
DEFINE_integer 'max_parallel' 50 'Max concurrent array tasks' 'j'
DEFINE_string 'extract_time' '01:00:00' 'Walltime per extract task' 'T'
DEFINE_string 'extract_mem' '4G' 'Memory per extract task' 'M'
DEFINE_string 'prep_time' '00:30:00' 'Walltime per vep_prep task' 'u'
DEFINE_string 'prep_mem' '2G' 'Memory per vep_prep task' 'U'
DEFINE_integer 'final_cpus' 4 'Cores (and --n_jobs) of the final job' 'n'
DEFINE_string 'final_mem' '16G' 'Memory of the final job' 'N'
DEFINE_string 'final_time' '04:00:00' 'Walltime of the final job' 'W'
DEFINE_boolean 'dry_run' false 'Print the sbatch commands, submit nothing' 'D'

FLAGS_HELP="$USAGE"

# parse arguments
FLAGS "$@" || exit $?
eval set -- "${FLAGS_ARGV}"

# *** IMPORTANT *** - This must be done after shflags has finished
# shellcheck disable=SC2034  # read by bh_init.sh
VERBOSE_TO_STDERR=1
# shellcheck disable=SC1091  # bh_init.sh is found on PATH at run time
. bh_init.sh

echo_prog_name "$0"
info_msg "SLURM job ID: ${SLURM_JOB_ID:-n/a} | name: ${SLURM_JOB_NAME:-n/a}" \
    "| node: ${SLURM_JOB_NODELIST:-n/a} | cpus: ${SLURM_CPUS_PER_TASK:-n/a}" \
    "| mem: ${SLURM_MEM_PER_NODE:-n/a}"
set_verbose_arg

ROOT="${FLAGS_root}"
OUTPUT="${FLAGS_output}"

# SLURM sets SLURM_ARRAY_TASK_ID only for array jobs; default to 1.
TASK_ID="${SLURM_ARRAY_TASK_ID:-1}"

# RUN_LOG.md only when log_tools is installed.
RUNLOG_ENABLED=1
RUNLOG_SETUP="$(runlog-setup-path 2> /dev/null || true)"
if [[ -n "${RUNLOG_SETUP}" ]] && [[ -f "${RUNLOG_SETUP}" ]]; then
    export RUNLOG_ROOT="${ROOT}"
    RUNLOG_SCRIPT_ID="$(basename "$0" .sh)_${FLAGS_stage}_task${TASK_ID}"
    export RUNLOG_SCRIPT_ID
    # shellcheck disable=SC1090  # resolved at runtime via console script
    source "${RUNLOG_SETUP}"
    runlog_setup
    RUNLOG_ENABLED=0
fi

# fail if any command fails
set -euo pipefail

# Chain runlog's teardown (when enabled) with bh_init.sh's clean_exit
# (removes the temporary working dir); clean_exit must see the real exit
# code, hence the subshell. set +e and trap - ERR: otherwise errexit or
# bh_init.sh's error trap would fire on that failing subshell, exit 1
# and skip clean_exit.
_combined_exit_trap() {
    local exit_code="$?"
    set +e
    trap - ERR
    if [[ "${RUNLOG_ENABLED}" -eq 0 ]]; then
        _runlog_teardown "${exit_code}"
    fi
    ( exit "${exit_code}" )
    clean_exit
}
trap '_combined_exit_trap' EXIT


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

# Fallback logging when neither bh_init.sh nor log_tools defines it.
if ! declare -F log_info > /dev/null; then
    log_info() { echo "[info]  $(date '+%Y-%m-%d %H:%M:%S') $*"; }
fi
if ! declare -F log_warn > /dev/null; then
    log_warn() { echo "[warn]  $(date '+%Y-%m-%d %H:%M:%S') $*" >&2; }
fi
if ! declare -F log_error > /dev/null; then
    log_error() { echo "[error] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2; }
fi
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Return the absolute path of an existing file.
#
# Parameters
# ----------
#   $1 - path : Existing file.
#
# Returns
# -------
#   0 on success, 1 if the directory does not exist.
#
# Outputs
# -------
#   The absolute path on stdout.
# -----------------------------------------------------------------------
abs_path() {
    local path="${1:?Error: path required}"
    local dir
    dir="$(cd "$(dirname "${path}")" && pwd)" || return 1
    echo "${dir}/$(basename "${path}")"
}
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Resolve a mamba/conda env (name or prefix) to the prefix that holds
# marvelous and python, and set ENV_PREFIX. Call it as an if condition:
# bh_init.sh's error trap does not fire there (it would inside $(...)).
#
# Parameters
# ----------
#   $1 - env : Env prefix (a directory) or name (via mamba/conda env list).
#
# Returns
# -------
#   0 on success, 1 when marvelous or python is not in the env.
#
# Outputs
# -------
#   Sets ENV_PREFIX to the absolute prefix.
# -----------------------------------------------------------------------
resolve_env() {
    local env="${1:?Error: env required}"
    local prefix="" tool
    if [[ -d "${env}" ]]; then
        prefix="$(cd "${env}" && pwd)"
    else
        for tool in mamba conda; do
            if command -v "${tool}" > /dev/null 2>&1; then
                # rows: name [*] prefix
                prefix="$("${tool}" env list 2> /dev/null \
                    | awk -v n="${env}" '$1 == n { print $NF; exit }')"
                if [[ -n "${prefix}" ]]; then
                    break
                fi
            fi
        done
    fi
    if [[ -z "${prefix}" ]] || [[ ! -x "${prefix}/bin/marvelous" ]] \
        || [[ ! -x "${prefix}/bin/python" ]]; then
        log_error "marvelous not found in env '${env}'" \
            "(expected <prefix>/bin/marvelous and bin/python)"
        return 1
    fi
    ENV_PREFIX="${prefix}"
}
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test that a VCF/BCF has a .tbi or .csi index.
#
# Parameters
# ----------
#   $1 - vcf : VCF/BCF path.
#
# Returns
# -------
#   0 when an index exists, 1 otherwise.
# -----------------------------------------------------------------------
has_index() {
    local vcf="${1:?Error: vcf required}"
    [[ -f "${vcf}.tbi" ]] || [[ -f "${vcf}.csi" ]]
}
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run the embedded Python helper (with the installed marvel package) and
# write its stdout to a file.
#
# NOTE: never redirect the output of a *function* call
# (`func > file`): when bh_init.sh's error trap exits inside it, bash
# still holds a copy of the runlog fifo and _runlog_teardown waits for
# tee forever (the job hangs until its walltime). Redirect the external
# command inside the function instead, as here.
#
# Modes:
#   chroms CONFIG PLINK_LIST
#       Chromosome labels of the variant list (no "chr", list order of
#       first appearance), one per line. Fails when a plink chunk name is
#       a vep_chr<label> name.
#   fallback CONFIG PLINK_LIST OUTDIR LABEL
#       "pos<TAB>ref<TAB>alt" of the listed variants on chromosome LABEL
#       that no plink chunk read (status not in EXTRACT_READ_STATUS).
#       Fails when a variant was read by more than one plink chunk or a
#       plink chunk summary is missing. Logs per-category counts.
#
# Parameters
# ----------
#   $1 - out : File for the helper's stdout.
#   $@ - mode and its arguments (see above).
#
# Returns
# -------
#   0 on success, 1 on a runtime error, 2 on bad input.
#
# Outputs
# -------
#   See the modes above (written to out); log messages on stderr.
# -----------------------------------------------------------------------
run_helper() {
    local out="${1:?Error: out required}"
    shift
    "${PYTHON[@]}" - "$@" > "${out}" <<'PY'
"""Two-source helper: chromosome labels and the VEP fallback list."""

from __future__ import annotations

import sys
from pathlib import Path

from marvel.config import load_config
from marvel.constants import (
    EXTRACT_OUTPUTS,
    EXTRACT_READ_STATUS,
    EXTRACT_SUMMARY_COLUMNS,
)
from marvel.extraction.model import normalise_chrom
from marvel.io import read_tsv_gz
from marvel.stages.extract import chunk_name, chunk_output, read_variant_table

VEP_CHUNK = "vep_chr{label}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _fail(message: str, code: int = 1) -> None:
    """Print an error and exit with ``code``."""
    print(f"[error] {message}", file=sys.stderr)
    raise SystemExit(code)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _label(chrom: str) -> str:
    """Return a list chromosome without a ``chr`` prefix (any case)."""
    name = str(chrom).strip()
    return name[3:] if name.lower().startswith("chr") else name


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _variants(config_path: str):
    """Return the config and its variant list (as marvel reads it)."""
    config = load_config(config_path)
    inp = config.input
    table = read_variant_table(
        inp.variants,
        variant_column=inp.variant_column,
        chrom_column=inp.chrom_column,
        pos_column=inp.pos_column,
        ref_column=inp.ref_column,
        alt_column=inp.alt_column,
        category_column=config.extract.category_column,
        file_sep=config.options.file_sep,
        var_sep=config.options.var_sep,
    )
    if table.empty:
        _fail(f"variant list {inp.variants} is empty", 2)
    return config, table


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _plink_chunks(plink_list: str) -> list[str]:
    """Return the chunk names of the plink gene VCFs (non-empty lines)."""
    lines = Path(plink_list).read_text().splitlines()
    return [chunk_name(line.strip()) for line in lines if line.strip()]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def chroms(config_path: str, plink_list: str) -> None:
    """Print the chromosome labels; refuse chunk name clashes."""
    config, table = _variants(config_path)
    labels = list(dict.fromkeys(table[config.input.chrom_column].map(_label)))
    plink = _plink_chunks(plink_list)
    if len(set(plink)) != len(plink):
        _fail(f"duplicate chunk names in {plink_list}", 2)
    clash = set(plink) & {VEP_CHUNK.format(label=lab) for lab in labels}
    if clash:
        _fail(f"plink chunk names clash with VEP chunks: {sorted(clash)}", 2)
    print("\n".join(labels))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fallback(config_path: str, plink_list: str, outdir: str, label: str):
    """Print pos/ref/alt of this chromosome's variants plink did not read."""
    config, table = _variants(config_path)
    inp = config.input
    read_by: dict[str, str] = {}
    twice: dict[str, list[str]] = {}
    for chunk in _plink_chunks(plink_list):
        path = chunk_output(outdir, chunk, EXTRACT_OUTPUTS.variants)
        if not path.is_file():
            _fail(f"plink chunk summary missing: {path} (did J1 finish?)")
        summary = read_tsv_gz(
            path, str_columns=(EXTRACT_SUMMARY_COLUMNS.variant,)
        )
        status = summary[EXTRACT_SUMMARY_COLUMNS.status]
        for variant in summary.loc[
            status.isin(EXTRACT_READ_STATUS), EXTRACT_SUMMARY_COLUMNS.variant
        ]:
            if variant in read_by:
                twice.setdefault(variant, [read_by[variant]]).append(chunk)
            read_by[variant] = chunk
    if twice:
        pairs: dict[str, list[str]] = {}
        for variant, chunks in twice.items():
            pairs.setdefault(" + ".join(chunks), []).append(variant)
        for chunks, variants in pairs.items():
            print(
                f"[error] {chunks}: {len(variants)} variant(s), e.g. "
                f"{sorted(variants)[:3]}",
                file=sys.stderr,
            )
        _fail(
            f"{len(twice)} variant(s) read by more than one plink gene VCF "
            "(same file twice, temp_ + normalised copy, or overlapping "
            "gene ranges?); remove one chunk per pair above from the list"
        )
    on_chrom = table[
        table[inp.chrom_column].map(normalise_chrom) == normalise_chrom(label)
    ].drop_duplicates(subset=inp.variant_column)
    todo = on_chrom[~on_chrom[inp.variant_column].isin(read_by)]
    category = config.extract.category_column
    if category is not None:
        for name, group in on_chrom.groupby(category, sort=False):
            n_vep = int((~group[inp.variant_column].isin(read_by)).sum())
            mixed = " (mixed sources)" if 0 < n_vep < len(group) else ""
            print(
                f"[info]  chr {label} {category} {name}: "
                f"{len(group) - n_vep} plink, {n_vep} vep fallback{mixed}",
                file=sys.stderr,
            )
    print(
        f"[info]  chr {label}: {len(on_chrom)} listed, {len(todo)} for VEP",
        file=sys.stderr,
    )
    columns = [inp.pos_column, inp.ref_column, inp.alt_column]
    for row in todo[columns].itertuples(index=False, name=None):
        print("\t".join(str(x) for x in row))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MODES = {"chroms": (chroms, 2), "fallback": (fallback, 4)}
if len(sys.argv) < 2 or sys.argv[1] not in MODES:
    _fail(f"usage: helper {{{'|'.join(MODES)}}} ARGS", 2)
func, n_args = MODES[sys.argv[1]]
if len(sys.argv) != n_args + 2:
    _fail(f"helper {sys.argv[1]} takes {n_args} arguments", 2)
func(*sys.argv[2:])
PY
}
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Submit (or print) one sbatch command and echo its job ID.
#
# Parameters
# ----------
#   $1 - fake_id : Job ID to echo with --dry_run.
#   $@ - args    : sbatch arguments (without --parsable).
#
# Returns
# -------
#   0 on success, the sbatch exit code otherwise.
#
# Outputs
# -------
#   The job ID on stdout; the command on stderr.
# -----------------------------------------------------------------------
submit() {
    local fake_id="${1:?Error: fake_id required}"
    shift
    local out=""
    echo "sbatch --parsable $*" >&2
    if [[ "${FLAGS_dry_run}" -eq "${FLAGS_TRUE}" ]]; then
        echo "${fake_id}"
        return 0
    fi
    out="$(sbatch --parsable "$@")"
    # --parsable prints "jobid[;cluster]"
    echo "${out%%;*}"
}
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Submit stage: check inputs, write the chunk lists to
# OUTPUT/two_source/ and submit J1 -> J2 -> J3 -> J4.
#
# Parameters
# ----------
#   None.
#
# Returns
# -------
#   0 on success, otherwise the failing exit code. Exits 2 on bad
#   input (exit, not return: bh_init.sh's error trap would turn a
#   returned 2 into exit 1).
# -----------------------------------------------------------------------
run_submit() {
    local -a labels=() missing=() common=() passthru=() array_opts=()
    local -a prep_opts=()
    local label vep geno n_plink n_chrom j1 j2 j3 j4
    local run_dir="${OUTPUT}/two_source"
    local log_dir="${run_dir}/logs"
    local slurm_array path
    if [[ ! -f "${FLAGS_slurm_array}" ]]; then
        log_error "slurm_array.sh not found: ${FLAGS_slurm_array}"
        exit 2
    fi
    slurm_array="$(abs_path "${FLAGS_slurm_array}")"
    mkdir -p "${PREP_DIR}" "${log_dir}"
    # via a file: set -e does not see a failing process substitution
    run_helper "${run_dir}/chroms.txt" chroms "${CONFIG}" "${PLINK_LIST}"
    mapfile -t labels < "${run_dir}/chroms.txt"
    n_chrom="${#labels[@]}"
    # plink list: absolute paths, every file indexed
    : > "${run_dir}/geno_plink.txt"
    while IFS= read -r geno || [[ -n "${geno}" ]]; do
        if [[ -z "${geno}" ]]; then
            continue
        fi
        if ! has_index "${geno}"; then
            missing+=("${geno}")
            continue
        fi
        path="$(abs_path "${geno}")"
        echo "${path}" >> "${run_dir}/geno_plink.txt"
    done < "${PLINK_LIST}"
    # vep: one input per chromosome, prepared chunk names predicted
    : > "${run_dir}/geno_vep.txt"
    for label in "${labels[@]}"; do
        vep="${FLAGS_vep_pattern//\{chrom\}/${label}}"
        if [[ ! -f "${vep}" ]] || ! has_index "${vep}"; then
            missing+=("${vep}")
        fi
        echo "${PREP_DIR}/vep_chr${label}.vcf.gz" >> "${run_dir}/geno_vep.txt"
    done
    if (( ${#missing[@]} > 0 )); then
        log_error "missing file or .tbi/.csi index: ${missing[*]}"
        exit 2
    fi
    cat "${run_dir}/geno_plink.txt" "${run_dir}/geno_vep.txt" \
        > "${run_dir}/geno_all.txt"
    n_plink="$(grep -c . "${run_dir}/geno_plink.txt" || true)"
    if (( n_plink == 0 )); then
        log_error "no gene VCFs in ${PLINK_LIST}"
        exit 2
    fi
    log_info "${n_plink} plink gene VCF(s); chromosomes: ${labels[*]}"
    # --export=ALL: jobs inherit PATH with the env's bin/ first
    common=(--partition="${FLAGS_partition}" --kill-on-invalid-dep=yes
        --export=ALL)
    passthru=(-c "${CONFIG}" -o "${OUTPUT}")
    if [[ -n "${FLAGS_image}" ]]; then
        passthru+=(-i "${FLAGS_image}")
    fi
    if [[ -n "${FLAGS_bind}" ]]; then
        passthru+=(-b "${FLAGS_bind}")
    fi
    if [[ "${FLAGS_verbose}" -eq "${FLAGS_TRUE}" ]]; then
        passthru+=(-v)
    fi
    # empty values are not passed: non-GNU getopt drops them
    prep_opts=(-p "${PLINK_LIST}" -P "${FLAGS_vep_pattern}" -R "${FASTA}"
        -d "${PREP_DIR}" -x "${FLAGS_pad}")
    if [[ -n "${FLAGS_modules}" ]]; then
        prep_opts+=(-m "${FLAGS_modules}")
    fi
    if [[ -n "${ENV_PREFIX}" ]]; then
        prep_opts+=(-e "${ENV_PREFIX}")
    fi
    array_opts=(--cpus-per-task=1 --time="${FLAGS_extract_time}"
        --mem="${FLAGS_extract_mem}" --output="${log_dir}/%x_%A_%a.log")
    j1="$(submit J1 "${common[@]}" "${array_opts[@]}" \
        --job-name=mv_plink --array="1-${n_plink}%${FLAGS_max_parallel}" \
        "${slurm_array}" "${passthru[@]}" -g "${run_dir}/geno_plink.txt")"
    j2="$(submit J2 "${common[@]}" --cpus-per-task=1 \
        --time="${FLAGS_prep_time}" --mem="${FLAGS_prep_mem}" \
        --output="${log_dir}/%x_%A_%a.log" --job-name=mv_vep_prep \
        --array="1-${n_chrom}%${FLAGS_max_parallel}" \
        --dependency="afterok:${j1}" \
        "${SELF}" -s vep_prep "${passthru[@]}" "${prep_opts[@]}")"
    j3="$(submit J3 "${common[@]}" "${array_opts[@]}" \
        --job-name=mv_vep --array="1-${n_chrom}%${FLAGS_max_parallel}" \
        --dependency="aftercorr:${j2}" \
        "${slurm_array}" "${passthru[@]}" -g "${run_dir}/geno_vep.txt")"
    j4="$(submit J4 "${common[@]}" --cpus-per-task="${FLAGS_final_cpus}" \
        --time="${FLAGS_final_time}" --mem="${FLAGS_final_mem}" \
        --output="${log_dir}/%x_%j.log" --job-name=mv_final \
        --dependency="afterok:${j3}" \
        "${slurm_array}" "${passthru[@]}" -g "${run_dir}/geno_all.txt" \
        -s final -n "${FLAGS_final_cpus}")"
    printf '%s\t%s\n' stage job_id plink_extract "${j1}" vep_prep "${j2}" \
        vep_extract "${j3}" final "${j4}" > "${run_dir}/jobs.tsv"
    log_info "submitted: J1 ${j1}, J2 ${j2}, J3 ${j3}, J4 ${j4}" \
        "(${run_dir}/jobs.tsv)"
}
# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vep_prep stage: for chromosome line TASK_ID of OUTPUT/two_source/
# chroms.txt, write PREP_DIR/vep_chr<label>.vcf.gz (+ .tbi) holding only
# the listed variants the plink chunks did not read, split into
# biallelic records and left-aligned. A header-only VCF when there are
# none, so the matching J3 task still has a file.
#
# Parameters
# ----------
#   None.
#
# Returns
# -------
#   0 on success, otherwise the failing exit code. Exits 2 on bad
#   input (exit, not return: bh_init.sh's error trap would turn a
#   returned 2 into exit 1).
#
# Outputs
# -------
#   PREP_DIR/vep_chr<label>.vcf.gz and its .tbi.
# -----------------------------------------------------------------------
run_vep_prep() {
    local label vep contig fa_contig name n_todo contigs
    local work="${WORKING_DIR}/task_${TASK_ID}"
    local final tmp
    label="$(sed -n "${TASK_ID}p" "${OUTPUT}/two_source/chroms.txt")"
    if [[ -z "${label}" ]]; then
        log_error "task ${TASK_ID}: no such line in chroms.txt"
        exit 2
    fi
    vep="${FLAGS_vep_pattern//\{chrom\}/${label}}"
    final="${PREP_DIR}/vep_chr${label}.vcf.gz"
    tmp="${PREP_DIR}/.vep_chr${label}.${SLURM_JOB_ID:-$$}.tmp.vcf.gz"
    mkdir -p "${work}" "${PREP_DIR}"
    if [[ -n "${FLAGS_modules}" ]]; then
        # module scripts are not written for set -u
        set +u
        # shellcheck disable=SC2086  # one word per module
        module load ${FLAGS_modules}
        set -u
    fi
    log_info "task ${TASK_ID}: chr ${label}, ${vep} -> ${final}"
    run_helper "${work}/todo.tsv" fallback "${CONFIG}" "${PLINK_LIST}" \
        "${OUTPUT}" "${label}"
    n_todo="$(grep -c . "${work}/todo.tsv" || true)"
    # contig as the VEP file spells it (index only)
    contigs="$(tabix -l "${vep}")"
    contig=""
    while IFS= read -r name; do
        if [[ "${name#[cC][hH][rR]}" == "${label}" ]]; then
            contig="${name}"
            break
        fi
    done <<< "${contigs}"
    # contig as the FASTA spells it (Ensembl 1 vs UCSC chr1); norm runs
    # on FASTA names, the chunk keeps the VEP names
    fa_contig="$(awk -v l="${label}" '{ n = $1; sub(/^[cC][hH][rR]/, "", n) }
        n == l { print $1; exit }' "${FASTA}.fai")"
    if [[ -n "${contig}" ]] && [[ -z "${fa_contig}" ]]; then
        log_error "chr ${label} not in ${FASTA}.fai"
        exit 2
    fi
    if (( n_todo == 0 )) || [[ -z "${contig}" ]]; then
        if [[ -z "${contig}" ]]; then
            log_warn "chr ${label} not in ${vep}; writing an empty chunk"
        fi
        log_info "chr ${label}: no VEP fallback variants; header-only chunk"
        bcftools view --no-version -h "${vep}" \
            | bcftools view --no-version -Oz -o "${tmp}"
    else
        # padded, merged regions (un-normalised indels sit to the right)
        awk -v c="${contig}" -v pad="${FLAGS_pad}" 'BEGIN { OFS = "\t" }
            { s = $1 - pad; if (s < 1) s = 1; print c, s, $1 + pad }' \
            "${work}/todo.tsv" | sort -k2,2n \
            | awk 'BEGIN { OFS = "\t" }
                NR == 1 { c = $1; s = $2; e = $3; next }
                $2 <= e + 1 { if ($3 > e) e = $3; next }
                { print c, s, e; s = $2; e = $3 }
                END { if (NR) print c, s, e }' > "${work}/regions.tsv"
        # IDs in both allele orders (marvel reads swapped records too)
        awk -v c="${contig}" '{ print c ":" $1 ":" $2 ":" $3;
            print c ":" $1 ":" $3 ":" $2 }' "${work}/todo.tsv" \
            > "${work}/ids.txt"
        printf '%s\t%s\n' "${contig}" "${fa_contig}" > "${work}/to_fa.txt"
        printf '%s\t%s\n' "${fa_contig}" "${contig}" > "${work}/to_vep.txt"
        bcftools view --no-version -R "${work}/regions.tsv" -Ou "${vep}" \
            | bcftools annotate --no-version -x INFO \
                --rename-chrs "${work}/to_fa.txt" -Ou \
            | bcftools annotate --no-version -x '^FORMAT/GT' -Ou \
            | bcftools norm --no-version -m -any -f "${FASTA}" \
                --check-ref w -Ou \
            | bcftools annotate --no-version \
                --rename-chrs "${work}/to_vep.txt" -Ou \
            | bcftools norm --no-version -d exact -Ou \
            | bcftools annotate --no-version \
                --set-id '%CHROM:%POS:%REF:%ALT' -Ou \
            | bcftools view --no-version -i "ID=@${work}/ids.txt" -Ou \
            | bcftools sort -T "${work}" -Oz -o "${tmp}"
    fi
    # separate index call: --write-index=tbi needs bcftools >= 1.19
    bcftools index --tbi --force "${tmp}"
    # index first: a chunk without its index is never left in place
    mv -f "${tmp}.tbi" "${final}.tbi"
    mv -f "${tmp}" "${final}"
    log_info "chr ${label}: $(bcftools index -n "${final}" || echo NA)" \
        "record(s)" \
        "for ${n_todo} fallback variant(s)"
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### CHECKS ###

if [[ "${FLAGS_stage}" != "submit" ]] \
    && [[ "${FLAGS_stage}" != "vep_prep" ]]; then
    log_error "-s/--stage must be submit or vep_prep, not '${FLAGS_stage}'"
    exit 2
fi
for f in "${FLAGS_config}" "${FLAGS_plink_list}" "${FLAGS_fasta}" \
    "${FLAGS_fasta}.fai"; do
    if [[ ! -f "${f}" ]]; then
        log_error "file not found: ${f}"
        exit 2
    fi
done
if [[ "${FLAGS_vep_pattern}" != *"{chrom}"* ]]; then
    log_error "-P/--vep_pattern must contain {chrom}"
    exit 2
fi
check_dir_readable "${ROOT}"
mkdir -p "${OUTPUT}"
check_dir_writable "${OUTPUT}"
# Absolute paths: the jobs run elsewhere and in Apptainer binds.
CONFIG="$(abs_path "${FLAGS_config}")"
PLINK_LIST="$(abs_path "${FLAGS_plink_list}")"
FASTA="$(abs_path "${FLAGS_fasta}")"
OUTPUT="$(cd "${OUTPUT}" && pwd)"
PREP_DIR="${FLAGS_prep_dir:-${OUTPUT}/two_source/vep}"
mkdir -p "${PREP_DIR}"
PREP_DIR="$(cd "${PREP_DIR}" && pwd)"
SELF="$(abs_path "$0")"
ENV_PREFIX=""
if [[ -n "${FLAGS_image}" ]]; then
    PYTHON=(apptainer exec --cleanenv
        --bind "$(dirname "${CONFIG}"),${OUTPUT}${FLAGS_bind:+,${FLAGS_bind}}"
        "${FLAGS_image}" python)
else
    if ! resolve_env "${FLAGS_env}"; then
        exit 2
    fi
    # first on PATH for this script and (via --export=ALL) every job;
    # python by full path, so a later module load cannot shadow it
    PATH="${ENV_PREFIX}/bin:${PATH}"
    export PATH
    PYTHON=("${ENV_PREFIX}/bin/python")
    log_info "env: ${ENV_PREFIX}"
fi
log_info "stage: ${FLAGS_stage}; config: ${CONFIG}; output: ${OUTPUT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### START ###

if [[ "${FLAGS_stage}" == "submit" ]]; then
    run_submit
else
    run_vep_prep
fi
