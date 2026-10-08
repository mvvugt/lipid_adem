#!/usr/bin/env python3
"""
Build the marvel exposure file of APOE genotype from the UKB phenotype file.

The APOE genotype column of `FileNames.UKB_PHENO` (the column the
stratified marvel runs stratify on) becomes one exposure column per
genotype present, other than the reference:

- ``1``: the participant has that genotype;
- ``0``: the participant has the reference genotype (e.g. e3/e3);
- ``NA``: any other genotype, or no genotype.

marvel drops rows with a missing exposure per test, so each column's
estimate is that genotype versus the reference, in the same samples,
outcomes and covariate models as the gene runs. Writes
`FileNames.APOE_EXPOSURE` (ID column plus the genotype columns), the
``carriers`` file of `FileNames.MARVEL_APOE_TASKS`.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import Constants, FileNames, Paths, RunlogOrder

_PREFIX: str = "APOE_"
_UNSAFE = re.compile(r"[^0-9A-Za-z]+")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _column_name(genotype: str) -> str:
    """Exposure column name of one genotype.

    Parameters
    ----------
    genotype : `str`
        Genotype value as in the phenotype file, e.g. ``"e3/e4"``.

    Returns
    -------
    name : `str`
        `_PREFIX` plus the value with every run of non-alphanumeric
        characters replaced by ``_``, e.g. ``"APOE_e3_e4"``.
    """
    return _PREFIX + _UNSAFE.sub("_", genotype).strip("_")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apoe_indicators(
    genotypes: pd.Series, reference: str
) -> pd.DataFrame:
    """One 1/0/NA column per non-reference genotype.

    Parameters
    ----------
    genotypes : `pd.Series`
        Genotype per participant, as strings; missing values allowed.
    reference : `str`
        Reference genotype value.

    Returns
    -------
    indicators : `pd.DataFrame`
        Same index as `genotypes`, `Int64` columns named by
        `_column_name`, in sorted genotype order.

    Raises
    ------
    ValueError
        If `reference` does not occur, there is no other genotype, or
        two genotypes give the same column name.
    """
    values = genotypes.astype("string").str.strip()
    present = sorted(set(values.dropna()) - {""})
    if reference not in present:
        raise ValueError(
            f"reference {reference!r} not among the genotypes {present}"
        )
    others = [value for value in present if value != reference]
    if not others:
        raise ValueError(f"no genotype other than {reference!r}")
    names = [_column_name(value) for value in others]
    if len(set(names)) != len(names):
        raise ValueError(f"genotypes {others} give clashing names {names}")
    is_reference = (values == reference).fillna(False)
    indicators = pd.DataFrame(index=genotypes.index)
    for value, name in zip(others, names):
        is_value = (values == value).fillna(False)
        column = pd.Series(pd.NA, index=genotypes.index, dtype="Int64")
        column[is_reference] = 0
        column[is_value] = 1
        indicators[name] = column
    return indicators


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apoe_exposure(
    column: str = Constants.UKB_APOE_COLUMN,
    reference: str = Constants.UKB_APOE_REFERENCE,
    pheno: Path = FileNames.UKB_PHENO,
    out: Path = FileNames.APOE_EXPOSURE,
) -> None:
    """Read the genotype column, build the indicators and write them.

    Parameters
    ----------
    column : `str`, optional, default: `Constants.UKB_APOE_COLUMN`
        APOE genotype column of `pheno`.
    reference : `str`, optional, default: `Constants.UKB_APOE_REFERENCE`
        Reference genotype value of that column.
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
    n_missing = int(table[column].isna().sum())
    if n_missing:
        log_warn(f"{n_missing} participants without a genotype: NA")

    log_stage("indicators")
    indicators = apoe_indicators(table[column], reference)
    for name in indicators.columns:
        tested = indicators[name].notna()
        log_info(
            f"{name}: {int((indicators[name] == 1).sum())} vs "
            f"{int((indicators[name] == 0).sum())} reference "
            f"({reference}); {int((~tested).sum())} NA"
        )

    log_stage("write")
    out.parent.mkdir(parents=True, exist_ok=True)
    exposure = pd.concat([table[[id_column]], indicators], axis=1)
    functions.write_table_atomic(exposure, out)
    log_info(f"wrote {len(exposure)} rows to {out}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Marvel exposure file of APOE genotype (each genotype vs the "
            "reference) from the UKB phenotype file."
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
        "--reference",
        default=Constants.UKB_APOE_REFERENCE,
        help="reference genotype value of that column (default: %(default)s)",
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
        apoe_exposure(
            args.column, args.reference, pheno=args.pheno, out=args.out
        )


if __name__ == "__main__":
    main()
