#!/usr/bin/env python3
"""
Build the binary exposure file of APOE diplotype for UKB participants with one
column per diplotype against all other diplotypes.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    Apoe,
    FileNames,
    Paths,
    RunlogOrder,
    Ukb,
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# APOE HANDLING

def apoe_indicators(
    genotypes: pd.Series,
    diplotypes: tuple[str, ...] = Apoe.GENOTYPES,
    prefix: str = Apoe.DIPLOTYPE_PREFIX,
) -> pd.DataFrame:
    """One 0/1 carrier column per diplotype.

    Parameters
    ----------
    genotypes : `pd.Series`
        Diplotype per participant, as strings, without missing values.
    diplotypes : `tuple[str, ...]`, default: `Apoe.GENOTYPES`
        Every diplotype `genotypes` may hold; one column each, in this
        order.
    prefix : `str`, default: `Apoe.DIPLOTYPE_PREFIX`
        Column name prefix, e.g. ``APOE_`` gives ``APOE_e4e4``.

    Returns
    -------
    indicators : `pd.DataFrame`
        Same index as `genotypes`, one `int64` column per diplotype:
        1 for that diplotype, 0 for any other.

    Raises
    ------
    ValueError
        If `genotypes` has missing values or a value not in `diplotypes`,
        or a diplotype has no carriers.
    """
    # check for missingness
    if genotypes.isna().any():
        raise ValueError(f"{int(genotypes.isna().sum())} missing genotypes")
    # check for unknown values
    values = genotypes.astype(str).str.strip()
    unknown = sorted(set(values) - set(diplotypes))
    if unknown:
        raise ValueError(
            f"genotype(s) {unknown} not in the diplotypes {list(diplotypes)}"
        )
    # check for absent diplotypes
    absent = [value for value in diplotypes if not (values == value).any()]
    if absent:
        raise ValueError(f"no carriers of diplotype(s) {absent}")
    # create binary column per diplotype
    indicators = pd.DataFrame(index=genotypes.index)
    for value in diplotypes:
        indicators[prefix + value] = (values == value).astype("int64")
    return indicators


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apoe_exposure(
    column: str = Apoe.UKB_COL,
    pheno: Path = FileNames.UKB_PHENO,
    out: Path = FileNames.APOE_EXPOSURE,
) -> None:
    """Read the genotype column, build the indicators and write them.

    Parameters
    ----------
    column : `str`, optional, default: `Apoe.UKB_COL`
        APOE genotype column of `pheno`.
    pheno : `Path`, optional, default: `FileNames.UKB_PHENO`
        UKB phenotype file with `Ukb.ID_COL`.
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
        If `column` is not in `pheno`, or from `apoe_indicators`.
    """
    functions.require_file(pheno)
    # check missing columns
    id_column = Ukb.ID_COL
    header = pd.read_csv(pheno, sep="\t", nrows=0).columns
    missing = [name for name in (id_column, column) if name not in header]
    if missing:
        raise ValueError(f"{pheno}: missing column(s) {missing}")
    # read the file with required columns only
    log_stage("read")
    table = pd.read_csv(
        pheno, sep="\t", usecols=[id_column, column], dtype={column: str}
    )
    # log diplotype counts
    counts = table[column].value_counts(dropna=False)
    log_info(
        f"{pheno}: {len(table)} participants; {column}: "
        + ", ".join(f"{value}={n}" for value, n in counts.items())
    )
    # extract diplotype values and check for missingness
    log_stage("indicators")
    values = table[column].str.strip()
    no_genotype = values.isna() | values.isin(
        ["", *Apoe.MISSING_VALUES]
    )
    if no_genotype.any():
        log_warn(
            f"{int(no_genotype.sum())} participants without a genotype "
            "left out"
        )
    # clean up and create binary columns per diplotype
    table = table.loc[~no_genotype]
    indicators = apoe_indicators(values.loc[~no_genotype])
    # create new file and log
    for name in indicators.columns:
        log_info(
            f"{name}: {int(indicators[name].sum())} carriers vs "
            f"{int((indicators[name] == 0).sum())} others"
        )
    exposure = pd.concat([table[[id_column]], indicators], axis=1)
    # write output file
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
            "Marvel exposure file of APOE diplotype (one 0/1 carrier "
            "column per diplotype, 0 = any other) from the UKB phenotype "
            "file."
        )
    )
    parser.add_argument(
        "--column",
        default=Apoe.UKB_COL,
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
# ENTRY POINT

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.APOE_EXPOSURE):
        apoe_exposure(args.column, pheno=args.pheno, out=args.out)


if __name__ == "__main__":
    main()
