#!/usr/bin/env python3
"""
Store the new marvel association results of each run and list them in
`data/raw/marvel_results.tsv`.

Each run of `data/raw/marvel_runs.tsv` (`create_config.py`) except the
APOE diplotype runs (`Marvel.APOE_ANALYSIS`, read by
`apoe_genotype_forest.py`) wrote ``<prefix>.results.tsv.gz`` into the run
directory (`Paths.MARVEL_RUN`, `slurm_array.sh -s final`). Every one must
exist. It is copied unchanged (new marvel columns) to its store
`results/marvel/<prefix>_results.tsv.gz`:

- no store yet: the copy is written;
- a store with the same content: left as is;
- a store with other content: kept with a time stamp in its name
  (warned), then the copy is written.

`marvel_results.tsv` then gets one row per store, outcome
(`Marvel.UKB_OUTCOMES`) and stratum for `--model` (a `covariate_model`).
Its non-UKB rows are kept. The stratum gives each row's ancestry and
APOE stratum (`parse_stratification`): ``overall`` and an `ApoeStratum`
code (e.g. ``e44``) are `--ancestry` samples, an `Ancestry` code
(``EUR``) and ``<ancestry>_<stratum>`` (``EUR_e44``) that ancestry
(`create_config.py` subsets). APOE-stratified runs are added to
`data/raw/apoe_strata.tsv` when they are missing there, so
`meta_analysis.py` pools them per stratum. `merge_associations.py` reads
the stores under the old marvel column names
(`functions.read_marvel_results`).
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import gzip
import hashlib
import os
import shutil
from datetime import datetime
from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    Ancestry,
    ApoeStratum,
    ColumnNames,
    FileNames,
    Marvel,
    MarvelRun,
    MetaColumns,
    Paths,
    RunlogOrder,
)


# cohort key of these runs (`Gwas.COHORT_ALIASES`)
_COHORT: str = "ukb"
_DEFAULT_MODEL: str = Marvel.DEFAULT_MODEL
_STAMP_FORMAT: str = "%Y%m%d_%H%M%S"
# bytes read per step when hashing a results file
_HASH_BLOCK: int = 1 << 20


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# runs and stores

def read_runs(path: Path) -> list[str]:
    """Prefixes of the runs to store (all but the APOE diplotype runs).

    Parameters
    ----------
    path : `Path`
        `FileNames.MARVEL_RUNS` (columns `MarvelRun.RUNS_*`).

    Returns
    -------
    prefixes : `list[str]`
        `MarvelRun.RUNS_PREFIX` of the runs, in file order.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    ValueError
        If a column is missing or a kept run is not a final-stage run.
    """
    functions.require_file(path, "marvel runs table (create_config.py)")
    runs = pd.read_csv(path, sep="\t", dtype=str)
    needed = [
        MarvelRun.RUNS_ANALYSIS, MarvelRun.RUNS_STAGE, MarvelRun.RUNS_PREFIX,
    ]
    missing = [col for col in needed if col not in runs.columns]
    if missing:
        raise ValueError(f"{path}: missing column(s) {missing}")
    runs = runs[runs[MarvelRun.RUNS_ANALYSIS] != Marvel.APOE_ANALYSIS]
    other = runs[runs[MarvelRun.RUNS_STAGE] != MarvelRun.STAGE_FINAL]
    if not other.empty:
        raise ValueError(
            f"{path}: run(s) {other[MarvelRun.RUNS_PREFIX].tolist()} are "
            f"not stage {MarvelRun.STAGE_FINAL!r}"
        )
    log_info(f"{path}: {len(runs)} runs to store")
    return runs[MarvelRun.RUNS_PREFIX].tolist()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def content_hash(path: Path) -> str:
    """SHA-256 of the decompressed content of a gzipped file.

    The gzip header holds a time stamp, so equal results can differ in
    their bytes; the content does not.

    Parameters
    ----------
    path : `Path`
        A gzipped file.

    Returns
    -------
    digest : `str`
        Hex digest.
    """
    digest = hashlib.sha256()
    with gzip.open(path, "rb") as handle:
        for block in iter(lambda: handle.read(_HASH_BLOCK), b""):
            digest.update(block)
    return digest.hexdigest()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _free_path(path: Path) -> Path:
    """Return `path`, or `path` with ``_1``, ``_2``, ... if it is taken.

    Parameters
    ----------
    path : `Path`
        Wanted path; the counter goes before the (double) suffix.

    Returns
    -------
    free : `Path`
        A path that does not exist.
    """
    if not path.exists():
        return path
    stem, dot, suffixes = path.name.partition(".")
    counter = 1
    while True:
        candidate = path.with_name(f"{stem}_{counter}{dot}{suffixes}")
        if not candidate.exists():
            return candidate
        counter += 1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def store_run(source: Path, store: Path, stamp: str) -> None:
    """Copy a run's results to its store; keep a differing store aside.

    The copy goes to a temporary file next to `store` first and is then
    moved into place, so an interrupted run never leaves half a store.

    Parameters
    ----------
    source : `Path`
        ``<prefix>.results.tsv.gz`` in the run directory.
    store : `Path`
        Its store (`FileNames.MARVEL_RUN_STORE_TEMPLATE`).
    stamp : `str`
        Time stamp for the backup name of a replaced store.

    Returns
    -------
    `None`
    """
    if store.exists():
        if content_hash(store) == content_hash(source):
            log_info(f"{store.name}: unchanged")
            return
        backup = _free_path(
            store.with_name(store.name.replace(".tsv.gz", f".{stamp}.tsv.gz"))
        )
        store.rename(backup)
        log_warn(
            f"{store.name}: other results; old store kept as {backup.name}"
        )
    store.parent.mkdir(parents=True, exist_ok=True)
    tmp = store.with_name(f".{store.name}.tmp")
    try:
        shutil.copyfile(source, tmp)
        os.replace(tmp, store)
    finally:
        tmp.unlink(missing_ok=True)
    log_info(f"{store.name}: written from {source}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def store_runs(
    prefixes: list[str], run_dir: Path, store_dir: Path, stamp: str
) -> dict[str, Path]:
    """Store every run's results (`store_run`).

    Parameters
    ----------
    prefixes : `list[str]`
        From `read_runs`.
    run_dir : `Path`
        Directory with the ``<prefix>.results.tsv.gz`` files.
    store_dir : `Path`
        Directory of the stores.
    stamp : `str`
        Time stamp for the backup name of a replaced store.

    Returns
    -------
    stores : `dict[str, Path]`
        Prefix -> its store.

    Raises
    ------
    FileNotFoundError
        If any run has no results file; then nothing is stored.
    """
    sources = {
        prefix: run_dir / f"{prefix}{MarvelRun.RESULTS_SUFFIX}"
        for prefix in prefixes
    }
    missing = sorted(
        str(path) for path in sources.values() if not path.exists()
    )
    if missing:
        raise FileNotFoundError(
            f"{len(missing)} run(s) without results, nothing stored: "
            + ", ".join(missing)
        )
    stores: dict[str, Path] = {}
    for prefix, source in sources.items():
        store = store_dir / FileNames.MARVEL_RUN_STORE_TEMPLATE.format(
            prefix=prefix
        )
        store_run(source, store, stamp)
        stores[prefix] = store
    return stores


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# marvel_results.tsv and apoe_strata.tsv

def parse_stratification(
    name: str, ancestry: str
) -> tuple[str, str] | None:
    """Ancestry and APOE stratum of a marvel `Stratification name`.

    Parameters
    ----------
    name : `str`
        ``overall``, an `ApoeStratum` code (``e44``), an `Ancestry` code
        (``EUR``) or ``<ancestry>_<stratum>`` (``EUR_e44``), as written by
        `create_config.py`.
    ancestry : `str`
        `Ancestry` code of the runs without an ancestry in the name.

    Returns
    -------
    parsed : `tuple[str, str]` or `None`
        (`Ancestry` code, `ApoeStratum` code or ``""`` when unstratified);
        `None` for any other name.
    """
    if name == Marvel.DEFAULT_STRAT:
        return ancestry, ""
    if name in ApoeStratum.CODES:
        return ancestry, name
    if name in Ancestry.CODES:
        return name, ""
    prefix, _, stratum = name.partition(Marvel.ANCESTRY_SEP)
    if prefix in Ancestry.CODES and stratum in ApoeStratum.CODES:
        return prefix, stratum
    return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def build_marvel_table(
    stores: dict[str, Path], model: str, ancestry: str
) -> pd.DataFrame:
    """List each store's outcomes and strata for one covariate model.

    Parameters
    ----------
    stores : `dict[str, Path]`
        Run prefix -> its store.
    model : `str`
        marvel `covariate_model` to use.
    ancestry : `str`
        `Ancestry` code of the runs without an ancestry in their
        stratum name (`parse_stratification`).

    Returns
    -------
    table : `pd.DataFrame`
        `marvel_results.tsv` rows (cohort, outcome, path, variable,
        model, ancestry, stratification, apoe_stratum, note = run
        prefix). A stratum `parse_stratification` cannot read is left
        out (warned), as it would share the overall run's study
        accession.
    """
    rows: list[dict[str, str]] = []
    for prefix, path in stores.items():
        store = pd.read_csv(
            path,
            sep="\t",
            dtype=str,
            usecols=[
                MarvelRun.COVARIATE_MODEL, MarvelRun.STRATUM, MarvelRun.OUTCOME,
            ],
        )
        store = store[store[MarvelRun.COVARIATE_MODEL] == model]
        if store.empty:
            log_warn(f"{prefix}: no rows for model {model!r} in {path.name}")
            continue
        pairs = store[
            [MarvelRun.OUTCOME, MarvelRun.STRATUM]
        ].drop_duplicates()
        unmapped = sorted(
            set(pairs[MarvelRun.OUTCOME]) - set(Marvel.UKB_OUTCOMES)
        )
        if unmapped:
            log_info(
                f"{prefix}: outcomes not in Marvel.UKB_OUTCOMES, "
                f"left out: {', '.join(unmapped)}"
            )
        for variable, stratification in pairs.itertuples(index=False):
            outcome = Marvel.UKB_OUTCOMES.get(variable)
            if outcome is None:
                continue
            parsed = parse_stratification(stratification, ancestry)
            if parsed is None:
                log_warn(
                    f"{prefix}: stratum {stratification!r} is neither "
                    "an ancestry nor an APOE stratum, left out"
                )
                continue
            row_ancestry, stratum = parsed
            rows.append(
                {
                    "cohort": _COHORT,
                    "outcome": outcome,
                    "path": str(path),
                    "variable": variable,
                    "model": model,
                    ColumnNames.ANCESTRY: row_ancestry,
                    ColumnNames.STRATIFICATION: stratification,
                    MetaColumns.APOE_STRATUM: stratum,
                    ColumnNames.NOTE: prefix,
                }
            )
    return pd.DataFrame(rows)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_marvel_table(table: pd.DataFrame) -> None:
    """Replace the UKB rows of `marvel_results.tsv`, keep the others.

    Parameters
    ----------
    table : `pd.DataFrame`
        From `build_marvel_table`.

    Returns
    -------
    `None`
    """
    current = functions.load_marvel_table(FileNames.MARVEL_RESULTS)
    kept = current[current["cohort"] != _COHORT]
    if not kept.empty:
        log_info(f"{FileNames.MARVEL_RESULTS}: {len(kept)} other rows kept")
    out = pd.concat([kept, table], ignore_index=True)[current.columns]
    functions.write_table_atomic(out, FileNames.MARVEL_RESULTS)
    log_info(f"wrote {len(out)} rows to {FileNames.MARVEL_RESULTS}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_apoe_strata(table: pd.DataFrame) -> None:
    """Add missing APOE-stratum study rows to `apoe_strata.tsv`.

    Per ancestry and outcome with stratified rows, the study group
    ``marvel_ukb_<ancestry>_<outcome>`` gets its unstratified run
    (`ApoeStratum.ALL`) and each stratum (accession + ``_<stratum>``,
    as in `merge_associations._marvel_identity`). Listed accessions are
    never changed; a listed one with another group or stratum is warned
    about.

    Parameters
    ----------
    table : `pd.DataFrame`
        From `build_marvel_table`.

    Returns
    -------
    `None`
    """
    stratified = table[table[MetaColumns.APOE_STRATUM] != ""]
    if stratified.empty:
        log_info("no APOE-stratified marvel rows, apoe_strata.tsv unchanged")
        return
    accession = ColumnNames.STUDY_ACCESSION
    wanted: list[dict[str, str]] = []
    for (ancestry, outcome), rows in stratified.groupby(
        [ColumnNames.ANCESTRY, "outcome"]
    ):
        group = f"{Marvel.SOURCE_DB_PREFIX}{_COHORT}_{ancestry}_" + (
            outcome
        )
        wanted.append(
            {
                accession: group,
                MetaColumns.STUDY_GROUP: group,
                MetaColumns.APOE_STRATUM: ApoeStratum.ALL,
            }
        )
        for stratum in sorted(rows[MetaColumns.APOE_STRATUM].unique()):
            wanted.append(
                {
                    accession: f"{group}_{stratum}",
                    MetaColumns.STUDY_GROUP: group,
                    MetaColumns.APOE_STRATUM: stratum,
                }
            )
    wanted_df = pd.DataFrame(wanted)

    path = FileNames.APOE_STRATA
    if path.exists():
        current = pd.read_csv(path, sep="\t", dtype=str).fillna("")
    else:
        current = pd.DataFrame(columns=list(wanted_df.columns))
    listed = current.set_index(accession)
    new_rows: list[dict[str, str]] = []
    for row in wanted_df.to_dict("records"):
        if row[accession] not in listed.index:
            new_rows.append(row)
            continue
        entry = listed.loc[row[accession]]
        if (
            entry[MetaColumns.STUDY_GROUP] != row[MetaColumns.STUDY_GROUP]
            or entry[MetaColumns.APOE_STRATUM]
            != row[MetaColumns.APOE_STRATUM]
        ):
            log_warn(
                f"{path}: {row[accession]} listed as "
                f"{entry[MetaColumns.STUDY_GROUP]}/"
                f"{entry[MetaColumns.APOE_STRATUM]}, not "
                f"{row[MetaColumns.STUDY_GROUP]}/"
                f"{row[MetaColumns.APOE_STRATUM]}; left as is"
            )
    if not new_rows:
        log_info(f"{path}: all marvel strata already listed")
        return
    out = pd.concat([current, pd.DataFrame(new_rows)], ignore_index=True)
    functions.write_table_atomic(out.fillna(""), path)
    log_info(f"{path}: {len(new_rows)} marvel rows added")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main

def marvel_results_table(
    ancestry: str,
    model: str = _DEFAULT_MODEL,
    runs: Path = FileNames.MARVEL_RUNS,
    run_dir: Path = Paths.MARVEL_RUN,
    store_dir: Path = Paths.MARVEL_STORE,
) -> None:
    """Store each run's results, then update marvel_results.tsv and strata.

    Parameters
    ----------
    ancestry : `str`
        `Ancestry` code of the runs without an ancestry in their stratum
        name (all samples: ``MULTI``).
    model : `str`, optional, default: `"adjusted"`
        marvel `covariate_model` listed in `marvel_results.tsv`.
    runs : `Path`, optional, default: `FileNames.MARVEL_RUNS`
        The runs table of `create_config.py`.
    run_dir : `Path`, optional, default: `Paths.MARVEL_RUN`
        Directory with the runs' ``<prefix>.results.tsv.gz``.
    store_dir : `Path`, optional, default: `Paths.MARVEL_STORE`
        Directory of the stores.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If `runs` or a run's results file does not exist; then nothing
        is written.
    """
    stamp = datetime.now().strftime(_STAMP_FORMAT)
    log_stage("store_runs")
    stores = store_runs(read_runs(runs), run_dir, store_dir, stamp)
    log_stage("marvel_table")
    table = build_marvel_table(stores, model, ancestry)
    write_marvel_table(table)
    add_apoe_strata(table)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Store the new marvel results per run and list them in "
            "marvel_results.tsv."
        )
    )
    parser.add_argument(
        "--ancestry",
        required=True,
        type=str.upper,
        choices=sorted(Ancestry.CODES),
        help=(
            "ancestry code of the runs whose stratum name has no "
            "ancestry (overall, e44, ...): all samples, MULTI"
        ),
    )
    parser.add_argument(
        "--model",
        default=_DEFAULT_MODEL,
        help="marvel `covariate_model` to list (default: %(default)s)",
    )
    parser.add_argument(
        "--runs",
        type=Path,
        default=FileNames.MARVEL_RUNS,
        help="runs table of create_config.py (default: %(default)s)",
    )
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=Paths.MARVEL_RUN,
        help=(
            "directory with the runs' <prefix>.results.tsv.gz "
            "(default: %(default)s)"
        ),
    )
    parser.add_argument(
        "--store-dir",
        type=Path,
        default=Paths.MARVEL_STORE,
        help="directory of the stores (default: %(default)s)",
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

    with runlog_setup(
        root=Paths.HERE, order=RunlogOrder.MARVEL_RESULTS_TABLE
    ):
        marvel_results_table(
            args.ancestry,
            model=args.model,
            runs=args.runs,
            run_dir=args.run_dir,
            store_dir=args.store_dir,
        )


if __name__ == "__main__":
    main()
