#!/usr/bin/env python3
"""
Build the marvel exposure file of APOE diplotype from the UKB phenotype file.

The APOE genotype column of `FileNames.UKB_PHENO` (the column the
stratified marvel runs stratify on) becomes one carrier column per
diplotype in `Constants.APOE_GENOTYPES`, e3e3 included:

- ``1``: the participant has that diplotype;
- ``0``: the participant has any other diplotype.

Each column is tested as its own exposure, so each estimate is that
diplotype versus all other diplotypes (not versus e3e3), in the same
samples, outcomes and covariate models. There are no missing values, so
marvel's listwise deletion and missingness filter keep everyone.
Participants without a genotype (`Constants.APOE_MISSING_VALUES`, blanks)
are left out of the file. Writes `FileNames.APOE_EXPOSURE` (ID column plus
the carrier columns, `Constants.APOE_DIPLOTYPE_PREFIX` + diplotype), the
``carriers`` file of `FileNames.MARVEL_APOE_TASKS`.
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
def apoe_indicators(
    genotypes: pd.Series,
    diplotypes: tuple[str, ...] = Constants.APOE_GENOTYPES,
    prefix: str = Constants.APOE_DIPLOTYPE_PREFIX,
) -> pd.DataFrame:
    """One 0/1 carrier column per diplotype.

    Parameters
    ----------
    genotypes : `pd.Series`
        Diplotype per participant, as strings, without missing values.
    diplotypes : `tuple[str, ...]`, optional, default: `Constants.APOE_GENOTYPES`
        Every diplotype `genotypes` may hold; one column each, in this
        order.
    prefix : `str`, optional, default: `Constants.APOE_DIPLOTYPE_PREFIX`
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
    if genotypes.isna().any():
        raise ValueError(f"{int(genotypes.isna().sum())} missing genotypes")
    values = genotypes.astype(str).str.strip()
    unknown = sorted(set(values) - set(diplotypes))
    if unknown:
        raise ValueError(
            f"genotype(s) {unknown} not in the diplotypes {list(diplotypes)}"
        )
    absent = [value for value in diplotypes if not (values == value).any()]
    if absent:
        raise ValueError(f"no carriers of diplotype(s) {absent}")
    indicators = pd.DataFrame(index=genotypes.index)
    for value in diplotypes:
        indicators[prefix + value] = (values == value).astype("int64")
    return indicators


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apoe_exposure(
    column: str = Constants.UKB_APOE_COLUMN,
    pheno: Path = FileNames.UKB_PHENO,
    out: Path = FileNames.APOE_EXPOSURE,
) -> None:
    """Read the genotype column, build the indicators and write them.

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
        If `column` is not in `pheno`, or from `apoe_indicators`.
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

    log_stage("indicators")
    values = table[column].str.strip()
    no_genotype = values.isna() | values.isin(
        ["", *Constants.APOE_MISSING_VALUES]
    )
    if no_genotype.any():
        log_warn(
            f"{int(no_genotype.sum())} participants without a genotype "
            "left out"
        )
    table = table.loc[~no_genotype]
    indicators = apoe_indicators(values.loc[~no_genotype])
    for name in indicators.columns:
        log_info(
            f"{name}: {int(indicators[name].sum())} carriers vs "
            f"{int((indicators[name] == 0).sum())} others"
        )
    exposure = pd.concat([table[[id_column]], indicators], axis=1)

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
