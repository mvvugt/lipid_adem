#!/usr/bin/env bash
#SBATCH --job-name=vep_extract
#SBATCH --output=%x.log
#SBATCH --partition=rome
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=02:00:00
#
# NOTE on cost: 1 core on the "rome" shared partition, the smallest billable
# unit. bcftools reads only each gene's region of the indexed per-chr VCF;
# +fill-tags reads the genotypes there to compute AF/AC, which sets the run
# time, not the memory.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
USAGE=$(cat <<EOF
====== vep_extract ======

Extract the VEP/LOFTEE consequences of the gene_list.txt genes from the
per-chromosome VEP-annotated VCFs (one row per variant x transcript of the
gene's Ensembl ID, read from the gene's start-end region) into one TSV,
with AF/AC computed from the genotypes:

    sbatch vep_extract.sh -r <root> -o <root>/data/raw -d <vcf_dir> -v

The VCF of a gene is <vcf_dir>/<pattern>, with {chrom} (and {gene}, if
used) replaced from gene_list.txt; it must be indexed (.tbi/.csi). A gene
without a VCF, or whose chromosome is not in it, is skipped (warned). A
sites-only VCF gives AF/AC ".". Writes vep_lipid_gene_csq.tsv.gz to OUTPUT
(stage-then-move). The file holds cohort AF/AC: do not commit it. Needs
bcftools with the split-vep and fill-tags plugins (BCFTOOLS_PLUGINS) and
log_tools.

USAGE: $(basename "$0") [-r ROOT] [-o OUTPUT] [-d VCF_DIR] [-g GENE_LIST]
       [-p PATTERN] [-t TMP_DIR] [-v]

EOF
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Setup

. shflags

DEFINE_string 'root' \
    '.' \
    'Root directory of the project' 'r'
DEFINE_string 'output' \
    './output' \
    'Directory that finished results are moved to on successful completion' 'o'
DEFINE_string 'vcf_dir' \
    '' \
    'Directory with the per-chromosome VEP-annotated VCFs (.vcf.gz, indexed)' 'd'
DEFINE_string 'gene_list' \
    '' \
    'Gene list with gene, chr, start, end and ensemblid columns (default: <root>/data/raw/gene_list.txt)' 'g'
DEFINE_string 'pattern' \
    'ukb_chr{chrom}_vep.vcf.gz' \
    'VCF file name pattern; {chrom} (and {gene}) are filled in per gene' 'p'
# shellcheck disable=SC2034,SC2016  # FLAGS_tmp_dir read by bh_init.sh; literal $TMPDIR
DEFINE_string 'tmp_dir' \
    '' \
    'Override the base dir for the temporary working dir (default: $TMPDIR, which SLURM already sets)' 't'
# shellcheck disable=SC2034  # FLAGS_verbose read by bh_init.sh
DEFINE_boolean 'verbose' false 'Print more output' 'v'

FLAGS_HELP="$USAGE"

# parse arguments
FLAGS "$@" || exit $?
eval set -- "${FLAGS_ARGV}"

# *** IMPORTANT *** - This must be done after shflags has finished
# shellcheck disable=SC2034  # read by bh_init.sh
VERBOSE_TO_STDERR=1
. bh_init.sh

echo_prog_name "$0"
info_msg "SLURM job ID: ${SLURM_JOB_ID:-n/a} | name: ${SLURM_JOB_NAME:-n/a} | node: ${SLURM_JOB_NODELIST:-n/a} | cpus: ${SLURM_CPUS_PER_TASK:-n/a} | mem: ${SLURM_MEM_PER_NODE:-n/a}"
set_verbose_arg

ROOT="${FLAGS_root}"
OUTPUT="${FLAGS_output}"
VCF_DIR="${FLAGS_vcf_dir}"
GENE_LIST="${FLAGS_gene_list:-${ROOT}/data/raw/gene_list.txt}"
PATTERN="${FLAGS_pattern}"
TASK_ID="${SLURM_ARRAY_TASK_ID:-1}"

export RUNLOG_ROOT="${ROOT}"
RUNLOG_SCRIPT_ID="$(basename "$0" .sh)"
export RUNLOG_SCRIPT_ID
# shellcheck disable=SC1090  # resolved at runtime via console script
source "$(runlog-setup-path)"
runlog_setup

# fail if any command fails
set -euo pipefail

# Chain runlog's teardown (writes RUN_LOG.md) with bh_init.sh's clean_exit
# (moves MOVE_FROM/MOVE_TO into OUTPUT); see template_snellius.sh.
_combined_exit_trap() {
    local exit_code="$?"
    set +e
    _runlog_teardown "${exit_code}"
    ( exit "${exit_code}" )
    clean_exit
}
trap '_combined_exit_trap' EXIT

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### CHECKS ###

if [[ -z "${VCF_DIR}" ]]; then
    log_error "no VCF directory: give -d <vcf_dir>"
    exit 1
fi
check_dir_readable "${ROOT}"
check_dir_readable "${VCF_DIR}"
check_file_readable "${GENE_LIST}"
mkdir -p "${OUTPUT}"
check_dir_writable "${OUTPUT}"
if ! command -v bcftools > /dev/null; then
    log_error "bcftools not on PATH (module load the bcftools module first)"
    exit 1
fi
# the plugins are found through BCFTOOLS_PLUGINS (or the build's default)
if ! PLUGINS="$(bcftools plugin -l 2>&1)"; then
    log_error "bcftools plugin -l failed: ${PLUGINS}"
    exit 1
fi
for plugin in split-vep fill-tags; do
    if ! grep -Eq "(^|[^[:alnum:]_-])${plugin}([.]so)?([^[:alnum:]_-]|$)" \
            <<< "${PLUGINS}"; then
        log_error "bcftools plugin ${plugin} not found; set BCFTOOLS_PLUGINS" \
            "to the plugins directory (now: '${BCFTOOLS_PLUGINS:-unset}')"
        exit 1
    fi
done

TASK_WORKING_DIR="${WORKING_DIR}/task_${TASK_ID}"
mkdir -p "${TASK_WORKING_DIR}"

log_info "using root directory: ${ROOT}"
log_info "VCF directory: ${VCF_DIR}, pattern: ${PATTERN}"
log_info "gene list: ${GENE_LIST}"
log_info "working directory (temporary): ${TASK_WORKING_DIR}"
log_info "results will be moved to on success: ${OUTPUT}"
log_info "$(bcftools --version | head -n 1)"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Print the gene, chr, start, end and ensemblid columns of the gene list
# (by header name), tab-separated, without the header.
#
# Parameters
# ----------
#   $1 - gene_list : Path to the gene list (tab-separated, with header).
#
# Returns
# -------
#   0 on success, 1 if a column is missing or a start/end is not a number
#   (the reason on stderr).
#
# Outputs
# -------
#   One "gene<TAB>chr<TAB>start<TAB>end<TAB>ensemblid" line per gene on
#   stdout.
# -----------------------------------------------------------------------
gene_rows() {
    local gene_list="${1:?Error: gene_list required}"
    awk -F'\t' -v OFS='\t' '
        NR == 1 {
            n = split("gene chr start end ensemblid", need, " ")
            for (i = 1; i <= NF; i++) col[$i] = i
            for (i = 1; i <= n; i++) {
                if (!(need[i] in col)) {
                    print "gene list has no column " need[i] > "/dev/stderr"
                    bad = 1
                }
            }
            if (bad) exit 1
            next
        }
        $col["start"] !~ /^[0-9]+$/ || $col["end"] !~ /^[0-9]+$/ {
            print "gene list line " NR ": start/end not a number" \
                > "/dev/stderr"
            bad = 1
            exit 1
        }
        {
            print $col["gene"], $col["chr"], $col["start"], $col["end"],
                $col["ensemblid"]
        }
        END { if (bad) exit 1 }
    ' "${gene_list}"
}

# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check a VEP VCF once: index, the CSQ fields used, and the samples.
#
# Parameters
# ----------
#   $1 - vcf_file : VEP-annotated VCF.
#
# Returns
# -------
#   0 if usable, 1 otherwise (the reason is logged).
#
# Outputs
# -------
#   Writes <TASK_WORKING_DIR>/<vcf name>.contigs (contigs with records)
#   and sets N_SAMPLES[vcf_file].
# -----------------------------------------------------------------------
check_vcf() {
    local vcf_file="${1:?Error: vcf_file required}"
    local contigs fields field
    contigs="${TASK_WORKING_DIR}/$(basename "${vcf_file}").contigs"
    local -a missing=()
    if ! bcftools index -s "${vcf_file}" > "${contigs}" 2> /dev/null; then
        log_error "${vcf_file}: no index; run bcftools index -t on it"
        return 1
    fi
    if ! fields="$(bcftools +split-vep -l "${vcf_file}" 2>&1)"; then
        log_error "${vcf_file}: no VEP CSQ header (${fields})"
        return 1
    fi
    for field in ${CSQ_FIELDS}; do
        if ! cut -f2 <<< "${fields}" | grep -qx -- "${field}"; then
            missing+=("${field}")
        fi
    done
    if (( ${#missing[@]} > 0 )); then
        log_error "${vcf_file}: CSQ lacks ${missing[*]} (LoF* need the" \
            "LOFTEE plugin; CANONICAL needs VEP --canonical)"
        return 1
    fi
    N_SAMPLES["${vcf_file}"]="$(bcftools query -l "${vcf_file}" | wc -l)"
    if (( N_SAMPLES["${vcf_file}"] == 0 )); then
        log_warn "${vcf_file}: sites-only, AF/AC written as '.'"
    else
        log_info "${vcf_file}: ${N_SAMPLES["${vcf_file}"]} samples"
    fi
}

# -----------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write the consequences of one gene's Ensembl ID in its region, one line
# per variant x transcript, with AF/AC computed from the genotypes (or "."
# for a sites-only VCF).
#
# Parameters
# ----------
#   $1 - vcf_file  : Indexed VEP-annotated VCF of the gene's chromosome.
#   $2 - region    : contig:start-end to read.
#   $3 - ensemblid : Ensembl gene ID to keep (CSQ `Gene` field).
#   $4 - n_samples : Number of samples in the VCF.
#
# Returns
# -------
#   0 on success, non-zero if bcftools fails.
#
# Outputs
# -------
#   Tab-separated rows (no header) on stdout, columns as CSQ_HEADER.
# -----------------------------------------------------------------------
extract_gene() {
    local vcf_file="${1:?Error: vcf_file required}"
    local region="${2:?Error: region required}"
    local ensemblid="${3:?Error: ensemblid required}"
    local n_samples="${4:?Error: n_samples required}"
    local counts='%AF\t%AC'
    local format
    if (( n_samples == 0 )); then
        counts='.\t.'
    fi
    format="%CHROM\\t%POS\\t%REF\\t%ALT\\t${counts}"
    format+='\t%Allele\t%Consequence\t%IMPACT\t%SYMBOL\t%Gene\t%Feature'
    format+='\t%BIOTYPE\t%CANONICAL\t%HGVSc\t%HGVSp\t%LoF\t%LoF_filter'
    format+='\t%LoF_flags\t%LoF_info\n'
    if (( n_samples == 0 )); then
        bcftools view -r "${region}" -Ou "${vcf_file}" \
            | bcftools +split-vep - -d -i "Gene=\"${ensemblid}\"" \
                -f "${format}"
    else
        bcftools view -r "${region}" -Ou "${vcf_file}" \
            | bcftools +fill-tags - -Ou -- -t AF,AC \
            | bcftools +split-vep - -d -i "Gene=\"${ensemblid}\"" \
                -f "${format}"
    fi
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### START ###

# column names read by annotate_ptv.py (project_constants.VepCsqColumns)
# the CSQ fields read (check_vcf), and the column names read by
# annotate_ptv.py (project_constants.VepCsqColumns)
readonly CSQ_FIELDS="Allele Consequence IMPACT SYMBOL Gene Feature BIOTYPE \
CANONICAL HGVSc HGVSp LoF LoF_filter LoF_flags LoF_info"
readonly CSQ_HEADER="chr pos ref alt AF AC ${CSQ_FIELDS}"
OUT_TSV="${TASK_WORKING_DIR}/vep_lipid_gene_csq.tsv"
tr -s ' ' '\t' <<< "${CSQ_HEADER}" > "${OUT_TSV}"

# read the gene list first, so a bad list stops the job here
GENE_ROWS="${TASK_WORKING_DIR}/gene_rows.tsv"
if ! gene_rows "${GENE_LIST}" > "${GENE_ROWS}"; then
    log_error "${GENE_LIST}: cannot read the gene list (see above)"
    exit 1
fi
mapfile -t GENES < "${GENE_ROWS}"
if (( ${#GENES[@]} == 0 )); then
    log_error "${GENE_LIST}: no genes"
    exit 1
fi
log_info "${#GENES[@]} genes in ${GENE_LIST}"

declare -A N_SAMPLES=()
n_genes=0
for gene_row in "${GENES[@]}"; do
    IFS=$'\t' read -r gene chrom start end ensemblid <<< "${gene_row}"
    chrom="${chrom#chr}"
    vcf_name="${PATTERN//\{chrom\}/${chrom}}"
    vcf_name="${vcf_name//\{gene\}/${gene}}"
    vcf_file="${VCF_DIR}/${vcf_name}"
    if [[ ! -r "${vcf_file}" ]]; then
        log_warn "${gene}: ${vcf_file} not found, skipped"
        continue
    fi
    # each per-chr VCF is checked once; an unusable VCF stops the job
    if [[ -z "${N_SAMPLES["${vcf_file}"]:-}" ]]; then
        check_vcf "${vcf_file}"
    fi
    # the contig as the VCF names it ("chr16" or "16")
    contigs="${TASK_WORKING_DIR}/$(basename "${vcf_file}").contigs"
    if grep -qx -- "chr${chrom}" "${contigs}"; then
        contig="chr${chrom}"
    elif grep -qx -- "${chrom}" "${contigs}"; then
        contig="${chrom}"
    else
        log_warn "${gene}: no chr${chrom} records in ${vcf_file}, skipped"
        continue
    fi
    region="${contig}:${start}-${end}"
    n_before="$(wc -l < "${OUT_TSV}")"
    extract_gene "${vcf_file}" "${region}" "${ensemblid}" \
        "${N_SAMPLES["${vcf_file}"]}" >> "${OUT_TSV}"
    n_after="$(wc -l < "${OUT_TSV}")"
    log_info "${gene} (${ensemblid}, ${region}): $((n_after - n_before)) rows"
    n_genes=$((n_genes + 1))
done

if (( n_genes == 0 )); then
    log_error "no VCF found for any gene in ${GENE_LIST}"
    exit 1
fi
gzip "${OUT_TSV}"
log_info "${n_genes} genes written to ${OUT_TSV}.gz"

MOVE_FROM+=("${OUT_TSV}.gz")
MOVE_TO+=("${OUTPUT}/vep_lipid_gene_csq.tsv.gz")
