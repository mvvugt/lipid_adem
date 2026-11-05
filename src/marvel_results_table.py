#!/usr/bin/env python3
"""
Collect the per-gene marvel association results into one store per gene
and list the stores in `data/raw/marvel_results.tsv`.

marvel writes one `{exposure}_results.tsv.gz` per tested carriers column
into a gene's `outdir` (`data/raw/marvel_tasks.tsv`, `marvel_assoc.sh`).
Those loose files are compared with the gene's store
(`results/marvel/<GENE>_results.tsv.gz`) row by row, on the analysis key
`MarvelColumns.KEY` (result file name, method, model, stratification,
outcome variable, exposure):

- a key not yet in the store is added; additions to an existing store
  are warned about;
- a key already in the store with the same results is skipped;
- a key already in the store with different results is an error: nothing
  is written for any gene.

`--refresh` builds every store anew from the loose files; the old store
is kept, renamed with a time stamp. `--replace` names job-array files
whose loose files win: every store or other loose row from a result file
of the same name is replaced by theirs (old store kept with a time stamp,
as for `--refresh`), e.g. a rerun of a few variants
(`data/raw/marvel_selected_tasks.tsv`). `--archive` packs each outdir's loose
files into a dated tar once they are in the store, checks the tar and
only then deletes them.

`marvel_results.tsv` then gets one row per store, outcome
(`Marvel.UKB_OUTCOMES`) and stratification for `--model`. Its
non-UKB rows are kept. The `Stratification name` gives each row's
ancestry and APOE stratum (`parse_stratification`): ``overall`` and an
`ApoeStratum` code (e.g. ``e44``) are `--ancestry` samples, an `Ancestry`
code (``EUR``) and ``<ancestry>_<stratum>`` (``EUR_e44``) that ancestry
(`create_config.py` subsets). APOE-stratified runs are added to
`data/raw/apoe_strata.tsv` when they are missing there, so
`meta_analysis.py` pools them per stratum.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import os
import tarfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import numpy as np
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
    MarvelColumns,
    MetaColumns,
    Paths,
    RunlogOrder,
)


# cohort key of these runs (`Gwas.COHORT_ALIASES`)
_COHORT: str = "ukb"
_DEFAULT_MODEL: str = Marvel.DEFAULT_MODEL
_STAMP_FORMAT: str = "%Y%m%d_%H%M%S"
# conflicts listed in the error log before the rest is only counted
_MAX_CONFLICTS_SHOWN: int = 20


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data containers

@dataclass
class GeneUpdate:
    """The planned store update of one gene.

    Attributes
    ----------
    gene : `str`
        Gene symbol.
    store_path : `Path`
        The gene's store.
    store : `pd.DataFrame` or `None`
        The new store content, `None` when nothing changes.
    loose_files : `dict[Path, list[Path]]`
        Outdir -> the loose result files read from it.
    n_added : `int`
        Rows new to the store.
    n_same : `int`
        Rows already in the store with the same results.
    conflicts : `pd.DataFrame`
        Keys with different results (empty when none).
    replaces : `bool`
        `store` replaces an existing store (`--refresh`), which is then
        kept aside.
    """
    gene: str
    store_path: Path
    store: pd.DataFrame | None = None
    loose_files: dict[Path, list[Path]] = field(default_factory=dict)
    n_added: int = 0
    n_same: int = 0
    conflicts: pd.DataFrame = field(default_factory=pd.DataFrame)
    replaces: bool = False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# reading

def read_tasks(paths: list[Path]) -> dict[str, list[Path]]:
    """Read the gene outdirs from the marvel job-array files.

    Parameters
    ----------
    paths : `list[Path]`
        `marvel_tasks.tsv`-like files with `gene` and `outdir` (e.g. the
        per-variant and the carrier-burden tasks); a gene may have several
        rows (e.g. a later batch or an APOE-stratified run). Outdirs are
        passed through `rebase_outdir`.

    Returns
    -------
    outdirs : `dict[str, list[Path]]`
        Gene -> its outdirs, in file order.

    Raises
    ------
    FileNotFoundError
        If a file in `paths` does not exist.
    ValueError
        If `gene` or `outdir` is missing.
    """
    outdirs: dict[str, list[Path]] = {}
    for path in paths:
        functions.require_file(path)
        tasks = pd.read_csv(path, sep="\t", dtype=str).fillna("")
        missing = [
            col for col in ("gene", "outdir") if col not in tasks.columns
        ]
        if missing:
            raise ValueError(f"{path}: missing column(s) {missing}")
        for gene, outdir in zip(tasks["gene"], tasks["outdir"]):
            outdirs.setdefault(gene.strip(), []).append(
                rebase_outdir(Path(outdir.strip()))
            )
        log_info(f"{path}: {len(tasks)} rows")
    log_info(f"{len(outdirs)} genes over {len(paths)} task file(s)")
    return outdirs


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rebase_outdir(outdir: Path, root: Path = Paths.HERE) -> Path:
    """Move an outdir written on another cluster under this project root.

    Task files hold absolute paths of the machine that wrote them; when
    the outdirs are copied to the same place inside the project on
    another machine, they are found there.

    Parameters
    ----------
    outdir : `Path`
        Outdir as listed in a task file.
    root : `Path`, optional, default: `Paths.HERE`
        This project's root.

    Returns
    -------
    outdir : `Path`
        `outdir` itself when it exists, is relative, or has no component
        named as `root`; else `root` plus the part after the last such
        component (logged).
    """
    if outdir.exists() or not outdir.is_absolute():
        return outdir
    parts = outdir.parts
    if root.name not in parts:
        return outdir
    last = len(parts) - 1 - parts[::-1].index(root.name)
    rebased = root.joinpath(*parts[last + 1:])
    log_info(f"outdir {outdir} not found here, read as {rebased}")
    return rebased


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_results(path: Path) -> pd.DataFrame:
    """Read a marvel results file or store, keeping every value as text.

    Values are not parsed (``NA`` stays ``NA``), so a store written back
    holds exactly what marvel wrote. A per-variant file gets
    `MarvelColumns.RESULT_FILE` (its name) and `SOURCE_FILE` (its path).

    Parameters
    ----------
    path : `Path`
        A marvel `{exposure}_results.tsv.gz` or a store.

    Returns
    -------
    results : `pd.DataFrame`
        All columns as strings.

    Raises
    ------
    ValueError
        If a `MarvelColumns.KEY` or `MarvelColumns.VALUES` column is
        missing.
    """
    results = pd.read_csv(
        path, sep="\t", dtype=str, keep_default_na=False, na_filter=False
    )
    if MarvelColumns.RESULT_FILE not in results.columns:
        results[MarvelColumns.RESULT_FILE] = path.name
        results[MarvelColumns.SOURCE_FILE] = str(path)
    required = [*MarvelColumns.KEY, *MarvelColumns.VALUES]
    missing = [col for col in required if col not in results.columns]
    if missing:
        raise ValueError(f"{path}: missing marvel column(s) {missing}")
    return results


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_loose(outdirs: list[Path]) -> tuple[pd.DataFrame, dict]:
    """Read the loose per-variant result files of one gene.

    Parameters
    ----------
    outdirs : `list[Path]`
        The gene's outdirs; a missing outdir is warned about and skipped.

    Returns
    -------
    loose : `pd.DataFrame`
        All rows (see `read_results`); empty when there are no loose
        files.
    files : `dict[Path, list[Path]]`
        Outdir -> the files read from it (outdirs without files left out).
    """
    frames: list[pd.DataFrame] = []
    files: dict[Path, list[Path]] = {}
    for outdir in outdirs:
        if not outdir.is_dir():
            log_warn(f"{outdir}: outdir not found, skipped")
            continue
        found = sorted(outdir.glob(FileNames.MARVEL_LOOSE_GLOB))
        if not found:
            log_info(f"{outdir}: no loose result files")
            continue
        files[outdir] = found
        for path in found:
            frames.append(read_results(path))
        log_info(f"{outdir}: {len(found)} loose result files")
    if not frames:
        return pd.DataFrame(), files
    return pd.concat(frames, ignore_index=True), files


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# comparing

def _numeric(frame: pd.DataFrame) -> np.ndarray:
    """Parse the `MarvelColumns.VALUES` columns as floats.

    Parameters
    ----------
    frame : `pd.DataFrame`
        Rows with the value columns as text.

    Returns
    -------
    values : `np.ndarray`
        Shape (rows, value columns); text that is not a number is NaN.
    """
    return np.column_stack(
        [
            pd.to_numeric(frame[col], errors="coerce").to_numpy(dtype=float)
            for col in MarvelColumns.VALUES
        ]
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _same_values(left: pd.DataFrame, right: pd.DataFrame) -> np.ndarray:
    """Check, row by row, whether two aligned frames hold the same results.

    Parameters
    ----------
    left, right : `pd.DataFrame`
        Same length, rows aligned by position.

    Returns
    -------
    same : `np.ndarray`
        Boolean per row: every value column equal as a number, or missing
        (NA) on both sides.
    """
    a = _numeric(left)
    b = _numeric(right)
    equal = (a == b) | (np.isnan(a) & np.isnan(b))
    return equal.all(axis=1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _conflict_table(
    old: pd.DataFrame, new: pd.DataFrame, same: np.ndarray
) -> pd.DataFrame:
    """List the keys whose results differ.

    Parameters
    ----------
    old, new : `pd.DataFrame`
        Aligned rows with the same keys.
    same : `np.ndarray`
        From `_same_values`.

    Returns
    -------
    conflicts : `pd.DataFrame`
        The key columns, then per value column ``<col> old`` and
        ``<col> new``, then both source files.
    """
    differ = ~same
    table = old.loc[differ, list(MarvelColumns.KEY)].reset_index(drop=True)
    for col in MarvelColumns.VALUES:
        table[f"{col} old"] = old.loc[differ, col].to_numpy()
        table[f"{col} new"] = new.loc[differ, col].to_numpy()
    table["file old"] = old.loc[differ, MarvelColumns.SOURCE_FILE].to_numpy()
    table["file new"] = new.loc[differ, MarvelColumns.SOURCE_FILE].to_numpy()
    return table


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dedupe_loose(loose: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Keep one row per key among the loose files.

    The same key in two loose files (e.g. a variant in two batches) is
    fine when the results are the same, and a conflict otherwise.

    Parameters
    ----------
    loose : `pd.DataFrame`
        From `read_loose`.

    Returns
    -------
    unique : `pd.DataFrame`
        The first row of each key.
    conflicts : `pd.DataFrame`
        From `_conflict_table`; empty when none.
    """
    key = list(MarvelColumns.KEY)
    is_repeat = loose.duplicated(key, keep="first")
    unique = loose.loc[~is_repeat]
    if not is_repeat.any():
        return unique.reset_index(drop=True), pd.DataFrame()
    repeats = loose.loc[is_repeat].reset_index(drop=True)
    firsts = repeats[key].merge(unique, on=key, how="left")
    same = _same_values(firsts, repeats)
    return unique.reset_index(drop=True), _conflict_table(
        firsts, repeats, same
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def compare_with_store(
    store: pd.DataFrame, loose: pd.DataFrame
) -> tuple[pd.DataFrame, int, pd.DataFrame]:
    """Split deduped loose rows into new, same and conflicting keys.

    Parameters
    ----------
    store : `pd.DataFrame`
        The current store.
    loose : `pd.DataFrame`
        From `dedupe_loose`.

    Returns
    -------
    added : `pd.DataFrame`
        Loose rows whose key is not in the store.
    n_same : `int`
        Loose rows whose key is in the store with the same results.
    conflicts : `pd.DataFrame`
        From `_conflict_table`; empty when none.
    """
    key = list(MarvelColumns.KEY)
    stored_keys = pd.MultiIndex.from_frame(store[key])
    is_new = ~pd.MultiIndex.from_frame(loose[key]).isin(stored_keys)
    added = loose.loc[is_new].reset_index(drop=True)
    known = loose.loc[~is_new].reset_index(drop=True)
    if known.empty:
        return added, 0, pd.DataFrame()
    old = known[key].merge(store, on=key, how="left")
    same = _same_values(old, known)
    conflicts = (
        _conflict_table(old, known, same) if not same.all() else pd.DataFrame()
    )
    return added, int(same.sum()), conflicts


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _describe_added(added: pd.DataFrame) -> str:
    """Summarise added rows for the log.

    Parameters
    ----------
    added : `pd.DataFrame`
        Rows added to a store.

    Returns
    -------
    summary : `str`
        Counts of exposures and the models, stratifications and outcome
        variables involved.
    """
    mc = MarvelColumns
    parts = [f"{added[mc.EXPOSURE].nunique()} exposures"]
    for col in (mc.MODEL_NAME, mc.STRATIFICATION_NAME, mc.VARIABLE):
        parts.append(f"{col}: {', '.join(sorted(added[col].unique()))}")
    return "; ".join(parts)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _stack(frames: list[pd.DataFrame]) -> pd.DataFrame:
    """Stack the non-empty frames (store, added and replacing rows).

    Parameters
    ----------
    frames : `list[pd.DataFrame]`
        Frames with the store columns; empty ones are skipped.

    Returns
    -------
    stacked : `pd.DataFrame`
        Their rows in order, a fresh index.
    """
    kept = [frame for frame in frames if not frame.empty]
    if not kept:
        return pd.DataFrame()
    return pd.concat(kept, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _read_replacing(
    gene: str, outdirs: list[Path], update: GeneUpdate
) -> tuple[pd.DataFrame, set[str]]:
    """Read the loose files that replace store rows (`--replace`).

    Parameters
    ----------
    gene : `str`
        Gene symbol (log lines).
    outdirs : `list[Path]`
        The gene's outdirs of the `--replace` task files.
    update : `GeneUpdate`
        Gets the files read (`loose_files`) and the conflicts among them.

    Returns
    -------
    replacing : `pd.DataFrame`
        Deduped rows (see `dedupe_loose`); empty when none.
    files : `set[str]`
        Their `MarvelColumns.RESULT_FILE` names: every store or other
        loose row from a file of that name is replaced.
    """
    if not outdirs:
        return pd.DataFrame(), set()
    replacing, files = read_loose(outdirs)
    update.loose_files.update(files)
    if replacing.empty:
        log_info(f"{gene}: no loose files to replace with")
        return replacing, set()
    replacing, update.conflicts = dedupe_loose(replacing)
    names = set(replacing[MarvelColumns.RESULT_FILE])
    log_info(
        f"{gene}: {len(replacing)} rows of {len(names)} result files "
        "replace the rows of the same files"
    )
    return replacing, names


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _drop_files(
    rows: pd.DataFrame, names: set[str], gene: str, what: str
) -> pd.DataFrame:
    """Drop the rows read from the replaced result files.

    Parameters
    ----------
    rows : `pd.DataFrame`
        Store or loose rows with `MarvelColumns.RESULT_FILE`.
    names : `set[str]`
        Replaced result file names.
    gene : `str`
        Gene symbol (log lines).
    what : `str`
        ``store`` or ``loose`` (log lines).

    Returns
    -------
    kept : `pd.DataFrame`
        `rows` without those files' rows.
    """
    if rows.empty or not names:
        return rows
    is_replaced = rows[MarvelColumns.RESULT_FILE].isin(names)
    if is_replaced.any():
        log_info(
            f"{gene}: {int(is_replaced.sum())} {what} rows of "
            f"{rows.loc[is_replaced, MarvelColumns.RESULT_FILE].nunique()} "
            "replaced result files left out"
        )
    return rows.loc[~is_replaced].reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plan_gene(
    gene: str,
    outdirs: list[Path],
    refresh: bool,
    replace_outdirs: list[Path] | None = None,
) -> GeneUpdate:
    """Work out the store update of one gene, without writing anything.

    Parameters
    ----------
    gene : `str`
        Gene symbol.
    outdirs : `list[Path]`
        The gene's outdirs.
    refresh : `bool`
        Ignore the current store and build it from the loose files only.
    replace_outdirs : `list[Path]` or `None`, optional, default: `None`
        Outdirs whose loose files replace, per result file name, the rows
        of the store and of `outdirs` (`--replace`); the old store is
        then kept aside.

    Returns
    -------
    update : `GeneUpdate`
        `store` is `None` when the store does not change.
    """
    store_path = Paths.MARVEL_STORE / FileNames.MARVEL_STORE_TEMPLATE.format(
        gene=gene
    )
    update = GeneUpdate(gene=gene, store_path=store_path)
    loose, update.loose_files = read_loose(outdirs)
    replacing, replaced = _read_replacing(
        gene, replace_outdirs or [], update
    )
    if not update.conflicts.empty:
        return update
    loose = _drop_files(loose, replaced, gene, "loose")
    if loose.empty and replacing.empty:
        log_info(f"{gene}: no loose result files, store unchanged")
        return update
    if not loose.empty:
        loose, update.conflicts = dedupe_loose(loose)
        if not update.conflicts.empty:
            return update

    has_store = store_path.exists() and not refresh
    if not has_store:
        update.store = _stack([loose, replacing])
        update.n_added = len(update.store)
        update.replaces = store_path.exists()
        action = "refreshed" if refresh else "new store"
        log_info(f"{gene}: {action}, {update.n_added} rows")
        return update

    store = read_results(store_path)
    n_repeated = int(store.duplicated(list(MarvelColumns.KEY)).sum())
    if n_repeated:
        raise ValueError(
            f"{store_path}: {n_repeated} repeated keys; rebuild it with "
            "--refresh"
        )
    # replaced rows: changed unless the store already holds exactly the
    # replacing rows for those files
    old = store.loc[store[MarvelColumns.RESULT_FILE].isin(replaced)]
    store = _drop_files(store, replaced, gene, "store")
    replace_changes = False
    if not replacing.empty:
        new, n_same, differ = compare_with_store(old, replacing)
        replace_changes = (
            not new.empty or not differ.empty or n_same != len(old)
        )
        log_info(
            f"{gene}: replaced files {len(old)} store rows -> "
            f"{len(replacing)} rows, "
            + ("changed" if replace_changes else "unchanged")
        )
    if loose.empty:
        added = loose
    else:
        added, update.n_same, update.conflicts = compare_with_store(
            store, loose
        )
    update.n_added = len(added)
    log_info(
        f"{gene}: {len(loose)} loose rows, {update.n_added} new, "
        f"{update.n_same} already in the store"
    )
    if not update.conflicts.empty:
        return update
    if added.empty and not replace_changes:
        return update
    if not added.empty:
        log_warn(
            f"{gene}: {update.n_added} rows added to {store_path.name} "
            f"({_describe_added(added)})"
        )
    if replace_changes:
        log_warn(
            f"{gene}: {len(old)} rows of {len(replaced)} result files in "
            f"{store_path.name} replaced by {len(replacing)} rows "
            f"({_describe_added(replacing)})"
        )
        update.replaces = True
    update.store = _stack([store, added, replacing])
    return update


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _log_conflicts(update: GeneUpdate) -> None:
    """Log the conflicting keys of one gene, old and new values.

    Parameters
    ----------
    update : `GeneUpdate`
        With non-empty `conflicts`.

    Returns
    -------
    `None`
    """
    conflicts = update.conflicts
    log_warn(
        f"{update.gene}: {len(conflicts)} analyses with different results "
        "for the same key (result file, method, model, stratification, "
        "variable, exposure)"
    )
    mc = MarvelColumns
    for _, row in conflicts.head(_MAX_CONFLICTS_SHOWN).iterrows():
        key = " | ".join(row[col] for col in mc.KEY)
        differ = [
            f"{col} {row[f'{col} old']} -> {row[f'{col} new']}"
            for col in mc.VALUES
            if row[f"{col} old"] != row[f"{col} new"]
        ]
        log_warn(
            f"  {key}: {'; '.join(differ)} ({row['file old']} vs "
            f"{row['file new']})"
        )
    if len(conflicts) > _MAX_CONFLICTS_SHOWN:
        log_warn(f"  ... {len(conflicts) - _MAX_CONFLICTS_SHOWN} more")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# writing

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
    name = path.name
    stem, dot, suffixes = name.partition(".")
    counter = 1
    while True:
        candidate = path.with_name(f"{stem}_{counter}{dot}{suffixes}")
        if not candidate.exists():
            return candidate
        counter += 1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_store(update: GeneUpdate, stamp: str) -> None:
    """Write a gene's new store; keep an old one aside when refreshing.

    Parameters
    ----------
    update : `GeneUpdate`
        With `store` set.
    stamp : `str`
        Time stamp for the backup name of a replaced store.

    Returns
    -------
    `None`
    """
    path = update.store_path
    path.parent.mkdir(parents=True, exist_ok=True)
    if update.replaces:
        backup = _free_path(
            path.with_name(path.name.replace(".tsv.gz", f".{stamp}.tsv.gz"))
        )
        path.rename(backup)
        log_info(f"{update.gene}: old store kept as {backup.name}")
    functions.write_table_atomic(update.store, path)
    log_info(f"{update.gene}: wrote {len(update.store)} rows to {path}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def archive_outdir(outdir: Path, files: list[Path], stamp: str) -> Path:
    """Pack loose result files into a tar, check it, then delete them.

    The tar is plain (the files are gzipped already), written under a
    temporary name and renamed only after its member list matched
    `files`; earlier archives are never overwritten.

    Parameters
    ----------
    outdir : `Path`
        The directory holding `files`.
    files : `list[Path]`
        The loose files, all already in the store.
    stamp : `str`
        Time stamp for the archive name.

    Returns
    -------
    archive : `Path`
        The written archive.

    Raises
    ------
    RuntimeError
        If the archive does not hold exactly `files`; nothing is deleted.
    """
    archive = _free_path(
        outdir / FileNames.MARVEL_ARCHIVE_TEMPLATE.format(stamp=stamp)
    )
    tmp = archive.with_name(archive.name + ".tmp")
    with tarfile.open(tmp, "w") as tar:
        for path in files:
            tar.add(path, arcname=path.name)
    with tarfile.open(tmp) as tar:
        stored = set(tar.getnames())
    expected = {path.name for path in files}
    if stored != expected:
        tmp.unlink()
        raise RuntimeError(
            f"{outdir}: archive holds {len(stored)} of {len(expected)} "
            "files, nothing deleted"
        )
    os.replace(tmp, archive)
    for path in files:
        path.unlink()
    log_info(f"{outdir}: {len(files)} loose files archived in {archive.name}")
    return archive


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
    """List each store's outcomes and stratifications for one model.

    Parameters
    ----------
    stores : `dict[str, Path]`
        Gene -> its store.
    model : `str`
        marvel `Model name` to use.
    ancestry : `str`
        `Ancestry` code of the runs without an ancestry in their
        stratification name (`parse_stratification`).

    Returns
    -------
    table : `pd.DataFrame`
        `marvel_results.tsv` rows (cohort, outcome, path, variable,
        model, ancestry, stratification, apoe_stratum, note). A
        stratification `parse_stratification` cannot read is left out
        (warned), as it would share the overall run's study accession.
    """
    mc = MarvelColumns
    rows: list[dict[str, str]] = []
    for gene, path in sorted(stores.items()):
        store = pd.read_csv(
            path,
            sep="\t",
            dtype=str,
            usecols=[mc.MODEL_NAME, mc.STRATIFICATION_NAME, mc.VARIABLE],
        )
        store = store[store[mc.MODEL_NAME] == model]
        if store.empty:
            log_warn(f"{gene}: no rows for model {model!r} in {path.name}")
            continue
        pairs = store[[mc.VARIABLE, mc.STRATIFICATION_NAME]].drop_duplicates()
        unmapped = sorted(
            set(pairs[mc.VARIABLE]) - set(Marvel.UKB_OUTCOMES)
        )
        if unmapped:
            log_info(
                f"{gene}: variables not in Marvel.UKB_OUTCOMES, "
                f"left out: {', '.join(unmapped)}"
            )
        for variable, stratification in pairs.itertuples(index=False):
            outcome = Marvel.UKB_OUTCOMES.get(variable)
            if outcome is None:
                continue
            parsed = parse_stratification(stratification, ancestry)
            if parsed is None:
                log_warn(
                    f"{gene}: stratification {stratification!r} is neither "
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
                    ColumnNames.NOTE: gene,
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
    tasks: list[Path],
    ancestry: str,
    model: str = _DEFAULT_MODEL,
    refresh: bool = False,
    archive: bool = False,
    replace: list[Path] | None = None,
) -> None:
    """Update the per-gene stores, then marvel_results.tsv and strata.

    Parameters
    ----------
    tasks : `list[Path]`
        The marvel job-array files (`gene`, `outdir`), e.g. the
        per-variant and the carrier-burden tasks: a gene's store is built
        from the outdirs of all of them.
    ancestry : `str`
        `Ancestry` code of the runs without an ancestry in their
        stratification name (all samples: ``MULTI``).
    model : `str`, optional, default: `"model_3"`
        marvel `Model name` listed in `marvel_results.tsv`.
    refresh : `bool`, optional, default: `False`
        Build every store anew from the loose files (old stores kept
        with a time stamp).
    archive : `bool`, optional, default: `False`
        Afterwards tar the loose files, check the tar and delete them.
    replace : `list[Path]` or `None`, optional, default: `None`
        Job-array files whose outdirs' loose files replace, per result
        file name, the store rows and the loose rows of `tasks` (e.g. a
        rerun of a few variants); the old store is kept with a time
        stamp.

    Returns
    -------
    `None`

    Raises
    ------
    ValueError
        If any gene has the same analysis with different results; then
        nothing is written.
    """
    stamp = datetime.now().strftime(_STAMP_FORMAT)

    log_stage("compare")
    outdirs = read_tasks(tasks)
    replace_outdirs = read_tasks(replace) if replace else {}
    genes = list(dict.fromkeys([*outdirs, *replace_outdirs]))
    updates = [
        plan_gene(
            gene, outdirs.get(gene, []), refresh,
            replace_outdirs.get(gene, []),
        )
        for gene in genes
    ]
    conflicted = [u for u in updates if not u.conflicts.empty]
    if conflicted:
        for update in conflicted:
            _log_conflicts(update)
        raise ValueError(
            f"{len(conflicted)} genes with conflicting results "
            f"({', '.join(u.gene for u in conflicted)}); nothing written. "
            "Remove the wrong loose files, or rebuild with --refresh"
        )
    if refresh:
        archive_glob = FileNames.MARVEL_ARCHIVE_TEMPLATE.format(stamp="*")
        for update in updates:
            for outdir in [*outdirs.get(update.gene, []),
                           *replace_outdirs.get(update.gene, [])]:
                archives = sorted(outdir.glob(archive_glob))
                if archives:
                    log_warn(
                        f"{update.gene}: --refresh leaves out the rows in "
                        f"{len(archives)} archive(s) in {outdir}"
                    )

    log_stage("write_stores")
    for update in updates:
        if update.store is not None:
            write_store(update, stamp)

    if archive:
        log_stage("archive")
        for update in updates:
            for outdir, files in update.loose_files.items():
                archive_outdir(outdir, files, stamp)

    log_stage("marvel_table")
    stores = {
        u.gene: u.store_path for u in updates if u.store_path.exists()
    }
    missing = sorted(set(genes) - set(stores))
    if missing:
        log_warn(f"no store yet for: {', '.join(missing)}")
    table = build_marvel_table(stores, model, ancestry)
    write_marvel_table(table)
    add_apoe_strata(table)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Collect per-variant marvel results into per-gene stores and "
            "list them in marvel_results.tsv."
        )
    )
    parser.add_argument(
        "--ancestry",
        required=True,
        type=str.upper,
        choices=sorted(Ancestry.CODES),
        help=(
            "ancestry code of the runs whose stratification name has no "
            "ancestry (overall, e44, ...): all samples, MULTI"
        ),
    )
    parser.add_argument(
        "--model",
        default=_DEFAULT_MODEL,
        help="marvel `Model name` to list (default: %(default)s)",
    )
    parser.add_argument(
        "-t",
        "--tasks",
        type=Path,
        nargs="+",
        default=[FileNames.MARVEL_TASKS],
        help=(
            "marvel job-array file(s); with --refresh list every file "
            "whose outdirs belong in the stores (default: %(default)s)"
        ),
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help=(
            "build every store anew from the loose files; the old store "
            "is kept with a time stamp"
        ),
    )
    parser.add_argument(
        "--replace",
        type=Path,
        nargs="+",
        metavar="TASKS",
        help=(
            "job-array file(s) whose loose files replace, per result file "
            "name, the store rows and the --tasks loose rows (old store "
            "kept with a time stamp), e.g. "
            f"{FileNames.MARVEL_SELECTED_TASKS.name}"
        ),
    )
    parser.add_argument(
        "--archive",
        action="store_true",
        help=(
            "tar the loose files once they are in the store, check the "
            "tar, then delete them"
        ),
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
            args.tasks,
            args.ancestry,
            model=args.model,
            refresh=args.refresh,
            archive=args.archive,
            replace=args.replace,
        )


if __name__ == "__main__":
    main()
