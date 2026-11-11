#!/usr/bin/env python3
"""
Build the UKB carrier-burden mask lists for new marvel and, after the
marvel burden runs, the burden summary (Snellius).

Per gene, the listed variants (`lipid_variants.tsv`) are assigned to the
masks `<GENE>_<mask>` (`Burden.VARIANT_SETS`); marvel makes each a 0/1
exposure: a sample is 1 when it carries any of the mask's sites.

- gof: GoF + ClinVar raising sites (the sites `meta_analysis.orient`
  flips); every other mask: the sites of its sources (PTV, ClinVar, AM;
  lof = PTV + ClinVar) that are not GoF/raising. The masks with ClinVar
  also get a directed form (`Burden.DIRECTED_MASKS`, e.g.
  lof_directed): without the ClinVar-only sites lacking a lowering
  direction. `SelectedGoF` sites (`VariantSource.SELECTED_GOF`)
  are in no mask.
- `<GENE>_<mask>_fb` (`Burden.FALLBACK_SUFFIX`): the same masks
  without the sites the preferred studies (`Burden.PREFER_STUDIES`,
  Thomassen) have for `Burden.FALLBACK_OUTCOME` in
  `matched_variants.tsv.gz`; written to their own list and tested
  against that outcome only.

`--mask-lists` writes `FileNames.BURDEN_MASK_VARIANTS_TEMPLATE` (main and
fallback; sites only, committed). `--summary` writes
`FileNames.BURDEN_EXPOSURE_SUMMARY`: per mask the listed and the read
sites, carriers and missing calls of the `Burden.SUMMARY_SUBSET` burden
runs (`Paths.MARVEL_RUN`; read by meta_analysis.py and figure_utils.py).

Requires log_tools installed (pip install log_tools) for RUN_LOG.md
logging. Does not import `functions` (biomed_api is not needed here).
"""
from __future__ import annotations


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

import argparse
from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

from variant_keys import (
    _join_unique,
    _write_table_atomic,
    key_from_id,
    variant_key,
)
from project_constants import (
    Burden,
    ClinVarDirection,
    ColumnNames,
    Const,
    FileNames,
    HarmonisedColumns,
    MarvelCompareColumns,
    MarvelRun,
    Paths,
    RunlogOrder,
    VariantListColumns,
    VariantSource,
)

_C = MarvelCompareColumns
_VL = VariantListColumns
_HC = HarmonisedColumns
# every variant set (`Burden.VARIANT_SETS`), each followed by
# its directed form when it has one
_MASKS: tuple[str, ...] = tuple(
    mask
    for base in Burden.VARIANT_SETS
    for mask in (base, Burden.DIRECTED_MASKS.get(base))
    if mask is not None
)
# variant-list sources of lower gene function (all non-gof sets)
_LOF_SOURCES: tuple[str, ...] = (
    VariantSource.PTV,
    VariantSource.CLINVAR,
    VariantSource.AM,
)
# variant ID column of the --exclude-sites file (as marvel's
# `<prefix>.variants.tsv.gz`)
_EXCLUDE_COLUMN = "variant"
# summary columns (`write_summary`)
_S_GENE = "gene"
_S_EXPOSURE = "exposure"
_S_LISTED = "n_sites_listed"
_S_READ = "n_sites_read"
_S_CARRIERS = "n_carriers"
_S_MISSING = "n_missing"
_S_SAMPLES = "n_samples"
_S_SITES = "sites"
_SUMMARY_COLUMNS: tuple[str, ...] = (
    _S_GENE, _S_EXPOSURE, _S_LISTED, _S_READ, _S_CARRIERS, _S_MISSING,
    _S_SAMPLES, _S_SITES,
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# variant sets

def read_sites(path: Path, genes: list[str]) -> pd.DataFrame:
    """Assign the listed sites of the genes to the burden masks.

    Parameters
    ----------
    path : `Path`
        `lipid_variants.tsv` (one row per site and source list).
    genes : `list` [`str`]
        Genes to keep.

    Returns
    -------
    sites : `pd.DataFrame`
        One row per gene and site: `gene`, `_C.NEW_KEY`, `orig_key` (the
        form before normalisation), and one bool column per mask in
        `_MASKS`.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"variant list not found: {path}")
    table = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False)
    table = table[table[_VL.GENE].isin(genes)].copy()
    table[_C.NEW_KEY] = variant_key(
        table[_VL.CHROM], table[_VL.POS], table[_VL.A1], table[_VL.A2]
    )
    table["orig_key"] = variant_key(
        table[_VL.CHROM], table[_VL.POS_ORIG], table[_VL.A1_ORIG],
        table[_VL.A2_ORIG],
    )
    table = table.dropna(subset=[_C.NEW_KEY])
    source = table[_VL.SOURCE]
    direction = table[_VL.CLINVAR_DIRECTION]
    is_clinvar = source == VariantSource.CLINVAR
    # selected single GoF variants are reported one by one, never in a
    # mask (a site also listed as GoF stays in the gof mask)
    is_selected = source == VariantSource.SELECTED_GOF
    if is_selected.any():
        log_info(
            f"{int(is_selected.sum())} "
            f"{VariantSource.SELECTED_GOF} rows in no mask"
        )
    known = is_selected | source.isin(
        [VariantSource.GOF, *_LOF_SOURCES]
    )
    if (~known).any():
        log_warn(
            f"{int((~known).sum())} rows of other sources "
            f"({_join_unique(source[~known])}) in no mask"
        )
    table["_gof"] = (source == VariantSource.GOF) | (
        is_clinvar & (direction == ClinVarDirection.RAISING)
    )
    # per lower-function source: the site is listed there (not raising)
    for list_source in _LOF_SOURCES:
        table[f"_in_{list_source}"] = (
            (source == list_source) & ~table["_gof"]
        )
    table["_clinvar_lowering"] = is_clinvar & (
        direction == ClinVarDirection.LOWERING
    )
    flags = [
        "_gof", "_clinvar_lowering",
        *(f"_in_{list_source}" for list_source in _LOF_SOURCES),
    ]
    sites = table.groupby([_VL.GENE, _C.NEW_KEY], as_index=False).agg(
        orig_key=("orig_key", "first"),
        **{flag: (flag, "any") for flag in flags},
    )
    # a site is flipped as a whole by orient() when any row is GoF/raising
    any_lof = sites[[f"_in_{s}" for s in _LOF_SOURCES]].any(axis=1)
    both = sites["_gof"] & any_lof
    if both.any():
        log_warn(
            f"{int(both.sum())} site(s) both LoF-listed and GoF/raising, "
            "in the gof mask only: "
            + ", ".join(sites.loc[both, _C.NEW_KEY])
        )
    for mask, mask_sources in Burden.VARIANT_SETS.items():
        if mask == Burden.MASK_GOF:
            sites[mask] = sites["_gof"]
            continue
        in_mask = sites[[f"_in_{s}" for s in mask_sources]].any(axis=1)
        sites[mask] = in_mask & ~sites["_gof"]
        directed = Burden.DIRECTED_MASKS.get(mask)
        if directed is None:
            continue
        # clear direction: in a source other than ClinVar, or ClinVar
        # lowering
        clear = sites["_clinvar_lowering"].copy()
        for list_source in mask_sources:
            if list_source != VariantSource.CLINVAR:
                clear |= sites[f"_in_{list_source}"]
        sites[directed] = sites[mask] & clear
    sites = sites.rename(columns={_VL.GENE: _S_GENE}).drop(columns=flags)
    for gene, part in sites.groupby(_S_GENE):
        log_info(
            f"{gene}: {len(part)} listed sites; "
            + ", ".join(f"{mask} {int(part[mask].sum())}" for mask in _MASKS)
        )
    return sites


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_prefer_sites(
    path: Path, studies: list[str], outcome: str
) -> dict[str, set[str]]:
    """Read the sites the preferred studies have for one outcome.

    Parameters
    ----------
    path : `Path`
        `matched_variants.tsv.gz` (match_variants.py).
    studies : `list` [`str`]
        Preferred study accessions (any APOE stratum).
    outcome : `str`
        Outcome of the fallback exposures.

    Returns
    -------
    sites : `dict` [`str`, `set` [`str`]]
        Variant-list gene -> ``chrom:pos:a1:a2`` keys of the variant-list
        entry (as `meta_analysis` `variant_site`).

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found: run match_variants.py first"
        )
    columns = [
        _HC.STUDY_ACCESSION, _HC.OUTCOME, _VL.OUT_GENE, _HC.CHROM, _HC.POS,
        _VL.OUT_A1, _VL.OUT_A2,
    ]
    matched = pd.read_csv(path, sep="\t", usecols=columns, dtype=str)
    matched = matched[
        matched[_HC.STUDY_ACCESSION].isin(studies)
        & (matched[_HC.OUTCOME] == outcome)
    ]
    if matched.empty:
        log_warn(
            f"{path.name}: no {outcome} rows of {', '.join(studies)}: "
            "fallback exposures equal the main ones"
        )
    # the matched table writes pos as float (``56983407.0``): back to an
    # integer, or the keys never equal the variant-list keys
    pos = pd.to_numeric(matched[_HC.POS], errors="coerce").astype("Int64")
    keys = variant_key(
        matched[_HC.CHROM], pos.astype("string"), matched[_VL.OUT_A1],
        matched[_VL.OUT_A2],
    )
    sites: dict[str, set[str]] = {}
    for gene, key in zip(matched[_VL.OUT_GENE], keys):
        if pd.notna(key):
            sites.setdefault(gene, set()).add(str(key))
    for gene, keys_of_gene in sorted(sites.items()):
        log_info(f"{gene}: {len(keys_of_gene)} sites in preferred studies")
    return sites


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mask_list(
    path: Path,
    sites: pd.DataFrame,
    prefer: dict[str, set[str]],
    fallback: bool,
) -> pd.DataFrame:
    """Build the burden masks as a long variant list for new marvel.

    Parameters
    ----------
    path : `Path`
        `lipid_variants.tsv`, for the site spelling of the list (new
        marvel's variant IDs must match the extraction chunks).
    sites : `pd.DataFrame`
        `read_sites` output.
    prefer : `dict` [`str`, `set` [`str`]]
        `read_prefer_sites` output.
    fallback : `bool`
        `True`: the `_fb` masks (`listed - prefer`);
        `False`: the main masks.

    Returns
    -------
    masks : `pd.DataFrame`
        One row per site and mask: `chr`, `pos`, `a1`, `a2` (first
        spelling in `path`), `gene`, `VariantListColumns.MASK`
        (``<GENE>_<mask>[_fb]``), in gene, mask and list order.

    Notes
    -----
    No carrier-fraction swap and no MAF filter (the old carrier path
    had both). Missing calls follow marvel's `max_gene_missing`.
    """
    detail = [_VL.CHROM, _VL.POS, _VL.A1, _VL.A2]
    table = pd.read_csv(
        path, sep="\t", dtype=str, keep_default_na=False,
        usecols=[*detail, _VL.GENE],
    )
    table[_C.NEW_KEY] = variant_key(
        table[_VL.CHROM], table[_VL.POS], table[_VL.A1], table[_VL.A2]
    )
    spelling = table.dropna(subset=[_C.NEW_KEY]).drop_duplicates(
        subset=[_VL.GENE, _C.NEW_KEY]
    )
    suffix = Burden.FALLBACK_SUFFIX if fallback else ""
    parts: list[pd.DataFrame] = []
    for gene, gene_sites in sites.groupby(_S_GENE, sort=False):
        gene_spelling = spelling[spelling[_VL.GENE] == gene]
        left_out = prefer.get(gene, set()) if fallback else set()
        for mask in _MASKS:
            keys = set(gene_sites.loc[gene_sites[mask], _C.NEW_KEY])
            keys -= left_out
            rows = gene_spelling[gene_spelling[_C.NEW_KEY].isin(keys)]
            if len(rows) != len(keys):
                raise ValueError(
                    f"{gene}_{mask}: {len(keys)} sites but {len(rows)} "
                    f"spellings in {path}"
                )
            if rows.empty:
                log_warn(f"{gene}_{mask}{suffix}: no sites, not listed")
                continue
            rows = rows[[*detail, _VL.GENE]].copy()
            rows[_VL.MASK] = f"{gene}_{mask}{suffix}"
            parts.append(rows)
            log_info(f"{gene}_{mask}{suffix}: {len(rows)} sites")
    if not parts:
        raise ValueError("no mask has a site")
    return pd.concat(parts, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_exclude_sites(path: Path) -> set[str]:
    """Read the sites to leave out of the mask lists.

    Parameters
    ----------
    path : `Path`
        Tab-separated, with a `_EXCLUDE_COLUMN` column of marvel variant
        IDs (``chr:pos:a1:a2``, e.g. rows of a marvel
        ``<prefix>.variants.tsv.gz``); other columns are ignored.

    Returns
    -------
    keys : `set` [`str`]
        Variant keys (`variant_key` form).

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    ValueError
        If `path` has no `_EXCLUDE_COLUMN` column, or an ID is not a
        variant.
    """
    if not path.exists():
        raise FileNotFoundError(f"exclude-sites file not found: {path}")
    table = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False)
    if _EXCLUDE_COLUMN not in table.columns:
        raise ValueError(
            f"{path}: no {_EXCLUDE_COLUMN!r} column; found "
            f"{list(table.columns)}"
        )
    keys = key_from_id(table[_EXCLUDE_COLUMN])
    if keys.isna().any():
        bad = table.loc[keys.isna(), _EXCLUDE_COLUMN]
        raise ValueError(f"{path}: not a variant ID: {_join_unique(bad)}")
    log_info(f"{path.name}: {keys.nunique()} site(s) to exclude")
    return set(keys)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_mask_lists(
    genes: list[str],
    variants: Path,
    matched: Path,
    prefer_studies: list[str] | None = None,
    exclude: Path | None = None,
    template: str = FileNames.BURDEN_MASK_VARIANTS_TEMPLATE,
) -> None:
    """Write the main and `_fb` mask lists for new marvel.

    Parameters
    ----------
    genes : `list` [`str`]
        Genes.
    variants : `Path`
        `lipid_variants.tsv`.
    matched : `Path`
        `matched_variants.tsv.gz`, for the preferred studies' sites.
    prefer_studies : `list` [`str`] or `NoneType`, optional
        Preferred study accessions; default
        `Burden.PREFER_STUDIES`.
    exclude : `Path` or `NoneType`, optional
        `read_exclude_sites` file: sites left out of every mask (e.g.
        indels that marvel matches as swapped to a different indel).
    template : `str`, optional
        Output path with ``{suffix}`` (`FileNames.
        BURDEN_MASK_VARIANTS_TEMPLATE`).

    Returns
    -------
    `None`
    """
    studies = list(prefer_studies or Burden.PREFER_STUDIES)
    log_stage("variant sets")
    sites = read_sites(variants, genes)
    if exclude is not None:
        keys = read_exclude_sites(exclude)
        drop = sites[_C.NEW_KEY].isin(keys)
        unlisted = keys - set(sites[_C.NEW_KEY])
        if unlisted:
            log_warn(
                f"{len(unlisted)} excluded site(s) not listed for these "
                f"genes: {', '.join(sorted(unlisted))}"
            )
        log_info(
            f"excluded {int(drop.sum())} listed site(s): "
            + ", ".join(sites.loc[drop, _C.NEW_KEY])
        )
        sites = sites[~drop]
    prefer = read_prefer_sites(
        matched, studies, Burden.FALLBACK_OUTCOME
    )
    for fallback in (False, True):
        log_stage("fallback mask list" if fallback else "mask list")
        suffix = Burden.FALLBACK_SUFFIX if fallback else ""
        masks = mask_list(variants, sites, prefer, fallback)
        _write_table_atomic(masks, Path(template.format(suffix=suffix)))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# summary of the marvel burden runs

def summary_prefixes(
    runs: Path, subset: str = Burden.SUMMARY_SUBSET
) -> dict[str, str]:
    """Return the run prefix of the main and the `_fb` burden analysis.

    Parameters
    ----------
    runs : `Path`
        `FileNames.MARVEL_RUNS` (create_config.py).
    subset : `str`, optional, default: `Burden.SUMMARY_SUBSET`
        UKB subset whose runs are summarised.

    Returns
    -------
    prefixes : `dict` [`str`, `str`]
        Mask-list suffix (``""`` or `Burden.FALLBACK_SUFFIX`) -> run
        prefix.

    Raises
    ------
    FileNotFoundError
        If `runs` does not exist.
    ValueError
        If an analysis has not exactly one run for `subset`.
    """
    if not runs.exists():
        raise FileNotFoundError(f"{runs} not found: run create_config.py")
    table = pd.read_csv(runs, sep="\t", dtype=str, keep_default_na=False)
    prefixes: dict[str, str] = {}
    for suffix in ("", Burden.FALLBACK_SUFFIX):
        analysis = f"{Burden.ANALYSIS}{suffix}"
        rows = table[
            (table[MarvelRun.RUNS_ANALYSIS] == analysis)
            & (table[MarvelRun.RUNS_SUBSET] == subset)
        ]
        if len(rows) != 1:
            raise ValueError(
                f"{runs}: {len(rows)} runs of {analysis} {subset}, "
                "expected 1"
            )
        prefixes[suffix] = rows[MarvelRun.RUNS_PREFIX].iloc[0]
    return prefixes


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_run_sites(path: Path) -> set[str]:
    """Return the keys of the sites a marvel run read.

    Parameters
    ----------
    path : `Path`
        ``<prefix>.variants.tsv.gz`` (marvel aggregate): one row per
        variant-list ID with its `MarvelRun.STATUS`.

    Returns
    -------
    keys : `set` [`str`]
        ``chrom:pos:a1:a2`` keys (`variant_key`) of the sites with a
        status in `MarvelRun.READ_STATUS`.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found: run the burden runs")
    columns = [
        MarvelRun.CHROM, MarvelRun.POS, MarvelRun.REF, MarvelRun.ALT,
        MarvelRun.STATUS,
    ]
    table = pd.read_csv(
        path, sep="\t", dtype=str, usecols=columns, keep_default_na=False
    )
    read = table[table[MarvelRun.STATUS].isin(MarvelRun.READ_STATUS)]
    keys = variant_key(
        read[MarvelRun.CHROM], read[MarvelRun.POS], read[MarvelRun.REF],
        read[MarvelRun.ALT],
    )
    log_info(
        f"{path.name}: {len(read)} of {len(table)} sites read "
        f"({', '.join(MarvelRun.READ_STATUS)})"
    )
    return set(keys.dropna())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def count_carriers(
    path: Path, chunksize: int = Burden.SUMMARY_CHUNK_ROWS
) -> pd.DataFrame:
    """Count the carriers and missing calls per exposure of a marvel run.

    Reads the long exposure table in chunks of `chunksize` rows, only
    its category and exposure columns.

    Parameters
    ----------
    path : `Path`
        ``<prefix>.exposures.tsv.gz`` (marvel aggregate, long: ``id,
        category, exposure``; dense or sparse).
    chunksize : `int`, optional, default: `Burden.SUMMARY_CHUNK_ROWS`
        Rows per chunk.

    Returns
    -------
    counts : `pd.DataFrame`
        Index category (``<GENE>_<mask>[_fb]``); columns `_S_CARRIERS`
        (exposure above 0) and `_S_MISSING` (exposure NA).

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found: run the burden runs")
    columns = [MarvelRun.AGG_CATEGORY, MarvelRun.AGG_EXPOSURE]
    carriers = pd.Series(dtype="int64")
    missing = pd.Series(dtype="int64")
    reader = pd.read_csv(
        path, sep="\t", usecols=columns, chunksize=chunksize,
        dtype={MarvelRun.AGG_CATEGORY: "category"},
        na_values=[Const.NA],
    )
    with reader:
        for chunk in reader:
            value = pd.to_numeric(chunk[MarvelRun.AGG_EXPOSURE])
            group = chunk[MarvelRun.AGG_CATEGORY].astype(str)
            carriers = carriers.add(
                (value > 0).groupby(group).sum(), fill_value=0
            )
            missing = missing.add(
                value.isna().groupby(group).sum(), fill_value=0
            )
    counts = pd.DataFrame({_S_CARRIERS: carriers, _S_MISSING: missing})
    return counts.fillna(0).astype("int64")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def count_samples(path: Path) -> int:
    """Return the number of samples of a marvel run.

    Parameters
    ----------
    path : `Path`
        ``<prefix>.samples.tsv.gz`` (marvel aggregate, one ``id`` per
        row).

    Returns
    -------
    n_samples : `int`

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found: run the burden runs")
    return len(pd.read_csv(path, sep="\t", usecols=[MarvelRun.ID],
                           dtype=str))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mask_summary(
    masks: pd.DataFrame,
    read: set[str],
    counts: pd.DataFrame,
    n_samples: int,
) -> pd.DataFrame:
    """Summarise one mask list against what its marvel run read.

    Parameters
    ----------
    masks : `pd.DataFrame`
        Mask list (`mask_list` output): `chr`, `pos`, `a1`, `a2`, `gene`,
        `VariantListColumns.MASK`.
    read : `set` [`str`]
        `read_run_sites` output.
    counts : `pd.DataFrame`
        `count_carriers` output.
    n_samples : `int`
        `count_samples` output.

    Returns
    -------
    summary : `pd.DataFrame`
        One row per mask, in list order: `_S_GENE`, `_S_EXPOSURE`,
        `_S_LISTED`, `_S_READ`, `_S_CARRIERS`, `_S_MISSING`,
        `_S_SAMPLES`, `_S_SITES` (the read sites joined by ``;``, in
        list order). A mask absent from `counts` has 0 carriers.
    """
    keys = variant_key(
        masks[_VL.CHROM], masks[_VL.POS], masks[_VL.A1], masks[_VL.A2]
    )
    is_read = keys.isin(read)
    rows: list[dict] = []
    for mask, idx in masks.groupby(_VL.MASK, sort=False).groups.items():
        mask_keys = keys.loc[idx]
        kept = mask_keys[is_read.loc[idx]]
        rows.append({
            _S_GENE: masks.loc[idx[0], _VL.GENE],
            _S_EXPOSURE: mask,
            _S_LISTED: len(mask_keys),
            _S_READ: len(kept),
            _S_CARRIERS: int(counts[_S_CARRIERS].get(mask, 0)),
            _S_MISSING: int(counts[_S_MISSING].get(mask, 0)),
            _S_SAMPLES: n_samples,
            _S_SITES: ";".join(kept),
        })
    return pd.DataFrame(rows, columns=list(_SUMMARY_COLUMNS))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_summary(
    runs: Path = FileNames.MARVEL_RUNS,
    run_dir: Path = Paths.MARVEL_RUN,
    template: str = FileNames.BURDEN_MASK_VARIANTS_TEMPLATE,
    summary_path: Path = FileNames.BURDEN_EXPOSURE_SUMMARY,
    chunksize: int = Burden.SUMMARY_CHUNK_ROWS,
) -> None:
    """Write the burden summary from the main and `_fb` marvel runs.

    Per mask: the listed sites, the sites marvel read, the carriers and
    missing calls, from the `Burden.SUMMARY_SUBSET` runs (which sites are
    read does not depend on the subset).

    Parameters
    ----------
    runs : `Path`, optional, default: `FileNames.MARVEL_RUNS`
        Run table, for the two prefixes (`summary_prefixes`).
    run_dir : `Path`, optional, default: `Paths.MARVEL_RUN`
        Directory with the ``<prefix>.<suffix>`` aggregate outputs.
    template : `str`, optional
        Mask lists with ``{suffix}`` (`FileNames.
        BURDEN_MASK_VARIANTS_TEMPLATE`).
    summary_path : `Path`, optional
        Output (`FileNames.BURDEN_EXPOSURE_SUMMARY`).
    chunksize : `int`, optional, default: `Burden.SUMMARY_CHUNK_ROWS`
        Rows per chunk of the exposure tables.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If a mask list or run output does not exist.
    """
    parts: list[pd.DataFrame] = []
    for suffix, prefix in summary_prefixes(runs).items():
        log_stage(f"summary {prefix}")
        masks_path = Path(template.format(suffix=suffix))
        if not masks_path.exists():
            raise FileNotFoundError(
                f"{masks_path} not found: run --mask-lists"
            )
        masks = pd.read_csv(
            masks_path, sep="\t", dtype=str, keep_default_na=False
        )
        part = mask_summary(
            masks,
            read_run_sites(run_dir / f"{prefix}{MarvelRun.VARIANTS_SUFFIX}"),
            count_carriers(
                run_dir / f"{prefix}{MarvelRun.EXPOSURES_SUFFIX}", chunksize
            ),
            count_samples(run_dir / f"{prefix}{MarvelRun.SAMPLES_SUFFIX}"),
        )
        none_read = part[part[_S_READ] == 0]
        if not none_read.empty:
            log_warn(
                f"{prefix}: no site read for "
                + ", ".join(none_read[_S_EXPOSURE])
            )
        parts.append(part)
    _write_table_atomic(pd.concat(parts, ignore_index=True), summary_path)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Write the burden mask lists for new marvel (--mask-lists) or, "
            "after the marvel burden runs, the burden summary (--summary)."
        )
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--mask-lists",
        action="store_true",
        help="write the mask lists "
        f"({FileNames.BURDEN_MASK_VARIANTS_TEMPLATE}, main and fallback)",
    )
    mode.add_argument(
        "--summary",
        action="store_true",
        help="write the summary of the burden runs "
        f"({FileNames.BURDEN_EXPOSURE_SUMMARY})",
    )
    parser.add_argument(
        "--genes",
        nargs="+",
        help=(
            "with --mask-lists: genes (default: the genes of --variants "
            f"minus {', '.join(Const.EXCLUDED_GENES)})"
        ),
    )
    parser.add_argument(
        "--variants",
        type=Path,
        default=FileNames.LIPID_VARIANTS,
        help="with --mask-lists: variant list (default: %(default)s)",
    )
    parser.add_argument(
        "--matched",
        type=Path,
        default=FileNames.MATCHED_VARIANTS,
        help="with --mask-lists: matched variants, for the preferred "
        "studies' sites (default: %(default)s)",
    )
    parser.add_argument(
        "--prefer-studies",
        nargs="+",
        default=list(Burden.PREFER_STUDIES),
        help="with --mask-lists: preferred study accessions "
        "(default: %(default)s)",
    )
    parser.add_argument(
        "--exclude-sites",
        type=Path,
        help="with --mask-lists: TSV with a 'variant' column (marvel IDs) "
        "of sites left out of every mask",
    )
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=Paths.MARVEL_RUN,
        help="with --summary: directory of the marvel run outputs "
        "(default: %(default)s)",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def default_genes(variants: Path) -> list[str]:
    """Return the genes of the variant list minus `Const.EXCLUDED_GENES`.

    The same gene rule as the per-variant list of create_config.py.

    Parameters
    ----------
    variants : `Path`
        Variant list with a `ColumnNames.GENE` column
        (`FileNames.LIPID_VARIANTS`).

    Returns
    -------
    genes : `list` of `str`
        Genes in order of first appearance.

    Raises
    ------
    ValueError
        If an excluded gene is not in `variants` (misspelled constant).
    """
    genes = pd.read_csv(
        variants, sep="\t", dtype=str, usecols=[ColumnNames.GENE],
        keep_default_na=False,
    )[ColumnNames.GENE]
    excluded = set(Const.EXCLUDED_GENES)
    unknown = sorted(excluded - set(genes))
    if unknown:
        raise ValueError(
            f"{variants}: no variants of excluded gene(s) {unknown}"
        )
    return [g for g in dict.fromkeys(genes) if g not in excluded]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    args = parser.parse_args()
    if args.exclude_sites is not None and not args.mask_lists:
        parser.error("--exclude-sites needs --mask-lists")
    if args.mask_lists and args.genes is None:
        args.genes = default_genes(args.variants)
    return args


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.BURDEN_EXPOSURE):
        if args.summary:
            write_summary(run_dir=args.run_dir)
            return
        write_mask_lists(
            args.genes,
            args.variants,
            args.matched,
            prefer_studies=args.prefer_studies,
            exclude=args.exclude_sites,
        )


if __name__ == "__main__":
    main()
