#!/usr/bin/env python3
"""
Build the marvel exposure file of APOE genotype from the UKB phenotype file.

The APOE genotype column of `FileNames.UKB_PHENO` (the column the
stratified marvel runs stratify on) becomes one integer-coded exposure
column, `Constants.APOE_EXPOSURE_NAME`, with the codes of
`Constants.APOE_GENOTYPE_CODES` (e3e3 = 0). marvel dummy-codes it with
`strata_ref` set to the reference's code (`create_config.py`), so one
regression per outcome and model estimates every genotype versus e3e3,
with the covariates fitted on all genotyped participants.

Participants without a genotype are left out of the file: a blank would
make the column float (``0.0``), which no longer matches `strata_ref`
(``0``). Writes `FileNames.APOE_EXPOSURE` (ID column plus the coded
column), the ``carriers`` file of `FileNames.MARVEL_APOE_TASKS`.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import Constants, FileNames, Paths, RunlogOrder


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apoe_codes(
    genotypes: pd.Series,
    codes: dict[str, int] = Constants.APOE_GENOTYPE_CODES,
    reference: str = Constants.UKB_APOE_REFERENCE,
) -> pd.Series:
    """Integer code per participant's genotype.

    Parameters
    ----------
    genotypes : `pd.Series`
        Genotype per participant, as strings; missing values allowed.
    codes : `dict[str, int]`, optional, default: `Constants.APOE_GENOTYPE_CODES`
        Genotype -> code.
    reference : `str`, optional, default: `Constants.UKB_APOE_REFERENCE`
        Reference genotype; must occur.

    Returns
    -------
    coded : `pd.Series`
        Same index as `genotypes`, `Int64`; missing genotypes are NA.

    Raises
    ------
    ValueError
        If a genotype is not in `codes`, or `reference` does not occur.
    """
    values = genotypes.astype("string").str.strip().replace("", pd.NA)
    present = set(values.dropna())
    unknown = sorted(present - set(codes))
    if unknown:
        raise ValueError(
            f"genotype(s) {unknown} not in the codes {sorted(codes)}"
        )
    if reference not in present:
        raise ValueError(
            f"reference {reference!r} not among the genotypes "
            f"{sorted(present)}"
        )
    return values.map(codes, na_action="ignore").astype("Int64")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apoe_exposure(
    column: str = Constants.UKB_APOE_COLUMN,
    pheno: Path = FileNames.UKB_PHENO,
    out: Path = FileNames.APOE_EXPOSURE,
) -> None:
    """Read the genotype column, code it and write the exposure file.

    Parameters
    ----------
    column : `str`, optional, default: `Constants.UKB_APOE_COLUMN`
        APOE genotype column of `pheno`.
    pheno : `Path`, optional, default: `FileNames.UKB_PHENO`
        UKB phenotype file with `Constants.UKB_ID_COLUMN`.
    out : `Path`, optional, default: `FileNames.APOE_EXPOSURE`
        Exposure file to write (gzipped TSV, written atomically).

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If `pheno` does not exist.
    ValueError
        If `column` is not in `pheno`, or from `apoe_codes`.
    """
    if not pheno.exists():
        raise FileNotFoundError(f"{pheno} not found")
    id_column = Constants.UKB_ID_COLUMN
    header = pd.read_csv(pheno, sep="\t", nrows=0).columns
    missing = [name for name in (id_column, column) if name not in header]
    if missing:
        raise ValueError(f"{pheno}: missing column(s) {missing}")

    log_stage("read")
    table = pd.read_csv(
        pheno, sep="\t", usecols=[id_column, column], dtype={column: str}
    )
    counts = table[column].value_counts(dropna=False)
    log_info(
        f"{pheno}: {len(table)} participants; {column}: "
        + ", ".join(f"{value}={n}" for value, n in counts.items())
    )

    log_stage("code")
    name = Constants.APOE_EXPOSURE_NAME
    table[name] = apoe_codes(table[column])
    log_info(
        f"{name} codes: "
        + ", ".join(
            f"{genotype}={code}"
            for genotype, code in Constants.APOE_GENOTYPE_CODES.items()
        )
        + f"; reference {Constants.UKB_APOE_REFERENCE}"
    )
    no_genotype = table[name].isna()
    if no_genotype.any():
        log_warn(
            f"{int(no_genotype.sum())} participants without a genotype "
            "left out"
        )
    exposure = table.loc[~no_genotype, [id_column, name]].copy()
    exposure[name] = exposure[name].astype("int64")

    log_stage("write")
    out.parent.mkdir(parents=True, exist_ok=True)
    functions.write_table_atomic(exposure, out)
    log_info(f"wrote {len(exposure)} rows to {out}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Marvel exposure file of APOE genotype (one integer-coded "
            "column, e3e3 = 0) from the UKB phenotype file."
        )
    )
    parser.add_argument(
        "--column",
        default=Constants.UKB_APOE_COLUMN,
        help=(
            f"APOE genotype column of {FileNames.UKB_PHENO.name} "
            "(default: %(default)s)"
        ),
    )
    parser.add_argument(
        "--pheno",
        type=Path,
        default=FileNames.UKB_PHENO,
        help="UKB phenotype file (default: %(default)s)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=FileNames.APOE_EXPOSURE,
        help="exposure file to write (default: %(default)s)",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    return parser.parse_args()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.APOE_EXPOSURE):
        apoe_exposure(args.column, pheno=args.pheno, out=args.out)


if __name__ == "__main__":
    main()
