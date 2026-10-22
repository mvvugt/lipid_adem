#!/usr/bin/env bash
# Shared bash helpers for this project


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GENERAL

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run a command in a mamba env without capturing its output.
#
# Parameters
# ----------
#   $1 - mamba_env : Name of the mamba/conda environment to run in.
#   $@ - command   : Command (and its arguments) to run inside that env.
#
# Returns
# -------
#   The wrapped command's exit code. Logs via `log_error` on failure
#   (non-zero exit).
#
# Example
# -------
#   run_mamba merit_py39 pyjasub -h
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
run_mamba() {
    local mamba_env="${1:?Error: mamba env required}"
    shift
    local exit_code=0
    mamba run --no-capture-output -n "$mamba_env" "$@" || exit_code="$?"
    if [[ "$exit_code" -ne 0 ]]; then
        log_error "run_mamba: '$*' failed in env '$mamba_env' (exit ${exit_code})"
    fi
    return "$exit_code"
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VEP VCF FUNCTIONS

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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
