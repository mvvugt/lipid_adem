#!/usr/bin/env bash
# Shared bash helpers for this project's scripts


# -----------------------------------------------------------------------
# Run a command in a mamba env without capturing its output.
#
# Parameters
# ----------
#   $1 - mamba_env : Name of the mamba/conda environment to run in.
#   $@ - command   : Command (and its arguments) to run inside that env.
#
# Returns
# -------
#   The wrapped command's exit code.
#
# Example
# -------
#   run_mamba merit_py39 pyjasub -h
# -----------------------------------------------------------------------
run_mamba() {
    local mamba_env="${1:?Error: mamba env required}"
    shift
    mamba run --no-capture-output -n "$mamba_env" "$@"
}
