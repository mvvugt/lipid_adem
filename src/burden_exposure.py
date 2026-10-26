#!/usr/bin/env python3
"""
Build the UKB carrier-burden exposures and the old marvel (10039b6) run
files for them (Snellius).

Per gene, the listed variants (`lipid_variants.tsv`) are collapsed into
0/1 carrier columns `<GENE>_<mask>` (`Constants.BURDEN_MASK_*`): a sample
is 1 when it carries any of the mask's sites, else 0 (a missing call
counts as non-carrier and is counted in the summary). Carriers come from
the old wide carriers files (`FileNames.OLD_CARRIERS_TEMPLATE`, `f.eid`
plus one dosage column per variant), read in chunks and only for the
listed variants.

- lof: PTV + ClinVar sites that are not raising; lof_directed: lof
  without the ClinVar-only sites lacking a lowering direction; gof: GoF +
  ClinVar raising sites (the sites `meta_analysis.orient` flips).
- `<GENE>_<mask>_fb` (`Constants.BURDEN_FALLBACK_SUFFIX`): the same masks
  without the sites the preferred studies (`Constants.
  BURDEN_PREFER_STUDIES`, Thomassen) have for `Constants.
  BURDEN_FALLBACK_OUTCOME` in `matched_variants.tsv.gz`; written to their
  own file and tested against that outcome only.
- A column whose carrier fraction is above `Constants.
  BURDEN_SWAP_FRACTION` (or that matches the list with a1/a2 swapped)
  counts the other allele: carriers are then the samples with dosage
  below 2 - threshold.
- Sites with a MAF above `--max-maf` are left out.

Writes per gene `FileNames.BURDEN_EXPOSURE_TEMPLATE` (main and fallback),
one cnf per gene x subset x file (`Paths.MARVEL_BURDEN_CONFIG`, format of
marvel 10039b6 as in validation/configs/A), the job-array file
`FileNames.MARVEL_BURDEN_TASKS` (columns as `marvel_tasks.tsv`, run with
src/marvel_burden.sh) and the summary `FileNames.BURDEN_EXPOSURE_SUMMARY`.
The exposure files are individual-level: never commit them.

Requires log_tools installed (pip install log_tools) for RUN_LOG.md
logging. Does not import `functions` (biomed_api is not needed here).
"""
from __future__ import annotations


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

from compare_marvel_runs import (
    _join_unique,
    _write_table_atomic,
    key_from_id,
    match_to_new,
    variant_key,
)
from project_constants import (
    ApoeStratum,
    ClinVarDirection,
    ColumnNames,
    Constants,
    FileNames,
    HarmonisedColumns,
    MarvelCompareColumns,
    Paths,
    RunlogOrder,
    VariantListColumns,
)

_C = MarvelCompareColumns
_VL = VariantListColumns
_HC = HarmonisedColumns
# pandas renames repeated header names to `<name>.<n>`
_DUPLICATE_SUFFIX = re.compile(r"\.\d+$")
_MASKS: tuple[str, ...] = (
    Constants.BURDEN_MASK_LOF,
    Constants.BURDEN_MASK_LOF_DIRECTED,
    Constants.BURDEN_MASK_GOF,
)
_SWAPPED_MATCHES = frozenset({_C.MATCH_SWAPPED, _C.MATCH_SWAPPED_ORIG})
# summary columns
_S_GENE = "gene"
_S_EXPOSURE = "exposure"
_S_LISTED = "n_sites_listed"
_S_FOUND = "n_sites_in_carriers"
_S_KEPT = "n_sites_kept"
_S_SWAPPED = "n_sites_swapped"
_S_MAF = "n_sites_above_max_maf"
_S_CARRIERS = "n_carriers"
_S_MISSING = "n_noncarriers_with_missing_call"
_S_SAMPLES = "n_samples"
_S_SITES = "sites"
# job-array columns (as marvel_tasks.tsv; src/marvel_assoc.sh)
_TASK_COLUMNS: tuple[str, ...] = (
    ColumnNames.ROWIDX, ColumnNames.GENE, "carriers", "outdir", "config",
    "subset",
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data containers

@dataclass
class Carriers:
    """Per-column carriers of one wide carriers file.

    Attributes
    ----------
    ids : `np.ndarray`
        Sample IDs in file order.
    alt : `dict` [`str`, `np.ndarray`]
        Column -> bool, dosage above the carrier threshold.
    ref : `dict` [`str`, `np.ndarray`]
        Column -> bool, dosage below 2 - threshold (carrier of the other
        allele).
    missing : `dict` [`str`, `np.ndarray`]
        Column -> bool, missing call.
    dosage_sum : `dict` [`str`, `float`]
        Column -> sum of the called dosages.
    """
    ids: np.ndarray
    alt: dict[str, np.ndarray] = field(default_factory=dict)
    ref: dict[str, np.ndarray] = field(default_factory=dict)
    missing: dict[str, np.ndarray] = field(default_factory=dict)
    dosage_sum: dict[str, float] = field(default_factory=dict)


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
    is_clinvar = source == Constants.CLINVAR_VARIANT_SOURCE
    known = source.isin([
        Constants.PTV_VARIANT_SOURCE,
        Constants.CLINVAR_VARIANT_SOURCE,
        Constants.GOF_VARIANT_SOURCE,
    ])
    if (~known).any():
        log_warn(
            f"{int((~known).sum())} rows of other sources "
            f"({_join_unique(source[~known])}) in no mask"
        )
    table["_gof"] = (source == Constants.GOF_VARIANT_SOURCE) | (
        is_clinvar & (direction == ClinVarDirection.RAISING)
    )
    table["_lof"] = known & ~table["_gof"]
    table["_clear"] = (known & ~is_clinvar) | (
        is_clinvar & (direction == ClinVarDirection.LOWERING)
    )
    sites = table.groupby([_VL.GENE, _C.NEW_KEY], as_index=False).agg(
        orig_key=("orig_key", "first"),
        _gof=("_gof", "any"),
        _lof=("_lof", "any"),
        _clear=("_clear", "any"),
    )
    # a site is flipped as a whole by orient() when any row is GoF/raising
    both = sites["_gof"] & sites["_lof"]
    if both.any():
        log_warn(
            f"{int(both.sum())} site(s) both LoF-listed and GoF/raising, "
            "in the gof mask only: "
            + ", ".join(sites.loc[both, _C.NEW_KEY])
        )
    sites[Constants.BURDEN_MASK_GOF] = sites["_gof"]
    sites[Constants.BURDEN_MASK_LOF] = sites["_lof"] & ~sites["_gof"]
    sites[Constants.BURDEN_MASK_LOF_DIRECTED] = (
        sites[Constants.BURDEN_MASK_LOF] & sites["_clear"]
    )
    sites = sites.rename(columns={_VL.GENE: _S_GENE}).drop(
        columns=["_gof", "_lof", "_clear"]
    )
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
    keys = variant_key(
        matched[_HC.CHROM], matched[_HC.POS], matched[_VL.OUT_A1],
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
# carriers

def carrier_columns(path: Path, sites: pd.DataFrame) -> pd.DataFrame:
    """Find the columns of a carriers file that hold listed sites.

    Parameters
    ----------
    path : `Path`
        Wide carriers file.
    sites : `pd.DataFrame`
        `read_sites` rows of one gene.

    Returns
    -------
    columns : `pd.DataFrame`
        `column` (header name), `_C.NEW_KEY`, `_C.MATCH`; repeated names
        (``<name>.<n>``) and columns that are not a variant are logged.
    """
    header = pd.Series(
        pd.read_csv(path, sep="\t", nrows=0).columns, dtype="string"
    )
    base = header.str.replace(_DUPLICATE_SUFFIX, "", regex=True)
    repeated = (base != header) & base.isin(header)
    names = header.where(~repeated, base)
    cols = pd.DataFrame({"column": header, "_key": key_from_id(names)})
    n_unparsed = int(cols["_key"].isna().sum())
    cols = cols.dropna(subset=["_key"])
    found = match_to_new(cols["_key"], sites)
    found = found.rename(columns={_C.OLD_KEY: "_key"})
    cols = cols.merge(found, on="_key", how="left").drop(columns="_key")
    cols = cols[cols[_C.NEW_KEY].notna()].reset_index(drop=True)
    log_info(
        f"{path.name}: {len(header)} columns, {n_unparsed} not a variant "
        f"(ID, merged names), {int(repeated.sum())} repeated, "
        f"{len(cols)} hold a listed site "
        f"({cols[_C.NEW_KEY].nunique()} sites)"
    )
    return cols


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stream_carriers(
    path: Path,
    columns: list[str],
    id_column: str,
    threshold: float,
    chunk_rows: int,
) -> Carriers:
    """Read some columns of a wide carriers file in chunks.

    Parameters
    ----------
    path : `Path`
        Wide carriers file: `id_column` plus one dosage column per variant.
    columns : `list` [`str`]
        Variant columns to read.
    id_column : `str`
        Sample ID column.
    threshold : `float`
        A dosage above it is a carrier (below 2 - it, of the other allele).
    chunk_rows : `int`
        Rows read at a time.

    Returns
    -------
    carriers : `Carriers`
        Sample IDs and per column the alt/ref carrier and missing flags.

    Raises
    ------
    ValueError
        If `id_column` is not in the file.
    """
    header = pd.read_csv(path, sep="\t", nrows=0).columns
    if id_column not in header:
        raise ValueError(f"{path}: no ID column {id_column!r}")
    dtypes = {col: "float32" for col in columns}
    dtypes[id_column] = str
    reader = pd.read_csv(
        path, sep="\t", usecols=[id_column, *columns], dtype=dtypes,
        chunksize=chunk_rows,
    )
    ids: list[np.ndarray] = []
    parts: dict[str, list[np.ndarray]] = {col: [] for col in columns}
    sums = dict.fromkeys(columns, 0.0)
    for part in reader:
        ids.append(part[id_column].str.strip().to_numpy())
        for col in columns:
            values = part[col].to_numpy()
            parts[col].append(values)
            sums[col] += float(np.nansum(values))
    carriers = Carriers(
        ids=np.concatenate(ids) if ids else np.array([], dtype=object),
        dosage_sum=sums,
    )
    for col in columns:
        values = (
            np.concatenate(parts[col]) if parts[col]
            else np.array([], dtype="float32")
        )
        carriers.alt[col] = values > threshold
        carriers.ref[col] = values < 2 - threshold
        carriers.missing[col] = np.isnan(values)
        parts[col] = []
    return carriers


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def site_carriers(
    gene: str,
    columns: pd.DataFrame,
    carriers: Carriers,
    max_maf: float,
) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray], set[str],
           set[str]]:
    """Orient each column and collapse it per listed site.

    Parameters
    ----------
    gene : `str`
        Gene (log lines).
    columns : `pd.DataFrame`
        `carrier_columns` output.
    carriers : `Carriers`
        `stream_carriers` output for those columns.
    max_maf : `float`
        Sites with a higher MAF are left out.

    Returns
    -------
    carrier : `dict` [`str`, `np.ndarray`]
        Site key -> bool, carrier of the listed a2 in any of its columns.
    missing : `dict` [`str`, `np.ndarray`]
        Site key -> bool, missing call in any of its columns.
    swapped : `set` [`str`]
        Sites with a column read as the other allele.
    above_maf : `set` [`str`]
        Sites left out for their MAF.
    """
    n_samples = len(carriers.ids)
    carrier: dict[str, np.ndarray] = {}
    missing: dict[str, np.ndarray] = {}
    swapped: set[str] = set()
    above_maf: set[str] = set()
    for row in columns.itertuples(index=False):
        col = row.column
        key = getattr(row, _C.NEW_KEY)
        called = int((~carriers.missing[col]).sum())
        alt_freq = carriers.dosage_sum[col] / (2 * called) if called else 0.0
        if min(alt_freq, 1 - alt_freq) > max_maf:
            above_maf.add(key)
            continue
        is_swapped = getattr(row, _C.MATCH) in _SWAPPED_MATCHES
        flags = carriers.ref[col] if is_swapped else carriers.alt[col]
        fraction = flags.sum() / n_samples if n_samples else 0.0
        if fraction > Constants.BURDEN_SWAP_FRACTION:
            is_swapped = not is_swapped
            flags = carriers.ref[col] if is_swapped else carriers.alt[col]
            log_warn(
                f"{gene}: {col} has {fraction:.1%} carriers, read as the "
                "other allele"
            )
        if is_swapped:
            swapped.add(key)
        carrier[key] = carrier.get(key, np.zeros(n_samples, bool)) | flags
        missing[key] = (
            missing.get(key, np.zeros(n_samples, bool))
            | carriers.missing[col]
        )
    for key in above_maf:
        carrier.pop(key, None)
        missing.pop(key, None)
    if above_maf:
        log_warn(
            f"{gene}: {len(above_maf)} site(s) with MAF > {max_maf} left "
            f"out: {', '.join(sorted(above_maf))}"
        )
    return carrier, missing, swapped, above_maf


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def collapse_masks(
    gene: str,
    sites: pd.DataFrame,
    carrier: dict[str, np.ndarray],
    missing: dict[str, np.ndarray],
    swapped: set[str],
    above_maf: set[str],
    prefer: set[str],
    n_samples: int,
) -> tuple[dict[str, np.ndarray], list[dict]]:
    """Collapse the sites of each mask into one 0/1 exposure.

    Parameters
    ----------
    gene : `str`
        Gene of the masks.
    sites : `pd.DataFrame`
        `read_sites` rows of the gene.
    carrier, missing, swapped, above_maf
        `site_carriers` output.
    prefer : `set` [`str`]
        Sites of the preferred studies (`read_prefer_sites`), left out of
        the fallback exposures.
    n_samples : `int`
        Samples in the carriers file.

    Returns
    -------
    exposures : `dict` [`str`, `np.ndarray`]
        Exposure name (`<GENE>_<mask>[_fb]`) -> int8 0/1; masks without a
        carrier are left out (warned).
    summary : `list` [`dict`]
        One summary row per exposure, also the left-out ones.
    """
    exposures: dict[str, np.ndarray] = {}
    summary: list[dict] = []
    for mask in _MASKS:
        listed = set(sites.loc[sites[mask], _C.NEW_KEY])
        for suffix, keys in (
            ("", listed),
            (Constants.BURDEN_FALLBACK_SUFFIX, listed - prefer),
        ):
            name = f"{gene}_{mask}{suffix}"
            found = keys & (set(carrier) | above_maf)
            kept = sorted(keys & set(carrier))
            any_carrier = np.zeros(n_samples, bool)
            any_missing = np.zeros(n_samples, bool)
            for key in kept:
                any_carrier |= carrier[key]
                any_missing |= missing[key]
            n_carriers = int(any_carrier.sum())
            summary.append({
                _S_GENE: gene,
                _S_EXPOSURE: name,
                _S_LISTED: len(keys),
                _S_FOUND: len(found),
                _S_KEPT: len(kept),
                _S_SWAPPED: len(set(kept) & swapped),
                _S_MAF: len(keys & above_maf),
                _S_CARRIERS: n_carriers,
                _S_MISSING: int((any_missing & ~any_carrier).sum()),
                _S_SAMPLES: n_samples,
                _S_SITES: ";".join(kept),
            })
            if n_carriers == 0:
                log_warn(f"{name}: no carriers ({len(keys)} sites), not "
                         "written")
                continue
            exposures[name] = any_carrier.astype("int8")
            log_info(
                f"{name}: {len(kept)} of {len(keys)} sites, {n_carriers} "
                "carriers"
            )
    return exposures, summary


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# marvel 10039b6 run files

def subset_strata() -> dict[str, dict[str, str]]:
    """Return the stratification of each burden subset.

    Returns
    -------
    strata : `dict` [`str`, `dict` [`str`, `str`]]
        `Constants.BURDEN_SUBSETS` value -> stratification name ->
        criterion (``column=value,value``; ``;`` joins two), as in
        create_config.py.
    """
    pop = (
        f"{Constants.UKB_POPULATION_COLUMN}="
        + ",".join(Constants.UKB_EUR_POPULATIONS)
    )
    apoe = {
        stratum: f"{Constants.UKB_APOE_COLUMN}={','.join(genotypes)}"
        for stratum, genotypes in ApoeStratum.GENOTYPES.items()
    }
    sep = Constants.MARVEL_ANCESTRY_SEP
    strata = {
        "all_apoe": dict(apoe),
        "eur": {"EUR": pop} | {
            f"EUR{sep}{stratum}": f"{pop};{criterion}"
            for stratum, criterion in apoe.items()
        },
    }
    unknown = sorted(set(Constants.BURDEN_SUBSETS) - set(strata))
    if unknown:
        raise ValueError(f"no stratification for subset(s) {unknown}")
    return {subset: strata[subset] for subset in Constants.BURDEN_SUBSETS}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_strata(pheno: Path, strata: dict[str, dict[str, str]]) -> None:
    """Check that every listed stratification value occurs.

    marvel keeps the rows whose value is listed and does not complain
    about a value that never occurs, so a misspelled value would silently
    shrink a stratum (as create_config.py).

    Parameters
    ----------
    pheno : `Path`
        Phenotype file of the cnfs.
    strata : `dict` [`str`, `dict` [`str`, `str`]]
        `subset_strata` output.

    Returns
    -------
    `None`

    Raises
    ------
    ValueError
        If a column or value is missing from `pheno`.
    """
    wanted: dict[str, set[str]] = {}
    for criteria in strata.values():
        for criterion in criteria.values():
            for part in criterion.split(";"):
                column, values = part.split("=", 1)
                wanted.setdefault(column, set()).update(values.split(","))
    header = pd.read_csv(pheno, sep="\t", nrows=0).columns
    absent_columns = sorted(set(wanted) - set(header))
    if absent_columns:
        raise ValueError(f"{pheno}: no column(s) {absent_columns}")
    table = pd.read_csv(pheno, sep="\t", usecols=sorted(wanted), dtype=str)
    for column, values in sorted(wanted.items()):
        present = set(table[column].dropna())
        absent = sorted(values - present)
        if absent:
            raise ValueError(
                f"{pheno}: {column} has no {absent} "
                f"(values: {sorted(present)})"
            )
        log_info(f"{column}: " + ", ".join(
            f"{value}={n}"
            for value, n in table[column].value_counts(dropna=False).items()
        ))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def outcome_tests(fallback: bool) -> tuple[list[str], list[str]]:
    """Return the marvel outcome variables of a burden cnf.

    Parameters
    ----------
    fallback : `bool`
        True for the fallback exposures: `Constants.
        BURDEN_FALLBACK_OUTCOME` only.

    Returns
    -------
    continuous, binary : `list` [`str`]
        `Constants.MARVEL_UKB_OUTCOMES` variables tested with OLS (lipids)
        and with GLM-Binom.
    """
    continuous: list[str] = []
    binary: list[str] = []
    for variable, outcome in Constants.MARVEL_UKB_OUTCOMES.items():
        if fallback and outcome != Constants.BURDEN_FALLBACK_OUTCOME:
            continue
        if outcome in Constants.LIPID_OUTCOMES:
            continuous.append(variable)
        else:
            binary.append(variable)
    return continuous, binary


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cnf_text(
    gene: str,
    exposure_file: Path,
    pheno: Path,
    strata: dict[str, str],
    fallback: bool,
) -> str:
    """Write the text of one marvel 10039b6 association cnf.

    Laid out as validation/configs/A/CETP_step2.cnf. No `exposures`
    option, so every column of `exposure_file` is tested; listwise
    deletion is off (`missingness_strategy False`, as the February runs).

    Parameters
    ----------
    gene : `str`
        `[ExpInput]` label.
    exposure_file : `Path`
        The 0/1 exposure file.
    pheno : `Path`
        Phenotype and covariate file.
    strata : `dict` [`str`, `str`]
        Stratification name -> criterion; marvel adds `overall`.
    fallback : `bool`
        Tests of the fallback exposures (`outcome_tests`).

    Returns
    -------
    text : `str`
        The cnf, tab-separated, ending with a newline.
    """
    continuous, binary = outcome_tests(fallback)
    lines = [
        "[ExpInput]",
        f"{gene}\t{exposure_file}",
        "[PhenoInput]",
        f"phenotypes\t{pheno}",
        f"covariates\t{pheno}",
        "[ConTests]",
        *(f"{variable}\tOLS" for variable in continuous),
        "[CatTests]",
        "[BinTests]",
        *(f"{variable}\tGLM-Binom" for variable in binary),
        "[Covs]",
        *(
            f"{model}\t{';'.join(covs) if covs else 'None'}"
            for model, covs in Constants.BURDEN_MODELS.items()
        ),
        "[Stratification]",
        *(f"{name}\t{criterion}" for name, criterion in strata.items()),
        "[Options]",
        f"id_column\t{Constants.UKB_ID_COLUMN}",
        "raise_on_error\tFalse",
        "missingness_strategy\tFalse",
        "extract_variants\tFalse",
        "association_analysis\tTrue",
    ]
    return "\n".join(lines) + "\n"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _write_text_atomic(text: str, path: Path) -> None:
    """Write a text file atomically (stage-then-move).

    Parameters
    ----------
    text : `str`
        File content.
    path : `Path`
        Destination; its directory is created if needed.

    Returns
    -------
    `None`
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(text)
    tmp_path.replace(path)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_run_files(
    gene: str,
    files: dict[str, Path],
    pheno: Path,
    strata: dict[str, dict[str, str]],
    config_dir: Path,
    out_dir: Path,
) -> list[dict]:
    """Write the cnfs of one gene and return its job-array rows.

    Parameters
    ----------
    gene : `str`
        Gene.
    files : `dict` [`str`, `Path`]
        Exposure-file suffix ("" or the fallback suffix) -> written file.
    pheno : `Path`
        Phenotype and covariate file.
    strata : `dict` [`str`, `dict` [`str`, `str`]]
        `subset_strata` output.
    config_dir, out_dir : `Path`
        Where the cnfs go, and the parent of the marvel outdirs.

    Returns
    -------
    rows : `list` [`dict`]
        One job-array row per subset and file (`_TASK_COLUMNS` without
        the row index).
    """
    rows: list[dict] = []
    for suffix, exposure_file in files.items():
        fallback = suffix == Constants.BURDEN_FALLBACK_SUFFIX
        for subset, subset_strata_ in strata.items():
            name = f"{gene}_{subset}{suffix}"
            config = config_dir / f"{name}.cnf"
            _write_text_atomic(
                cnf_text(gene, exposure_file, pheno, subset_strata_,
                         fallback),
                config,
            )
            rows.append({
                ColumnNames.GENE: gene,
                "carriers": str(exposure_file),
                "outdir": str(out_dir / name),
                "config": str(config),
                "subset": subset,
            })
            log_info(f"{name}: {config}")
    return rows


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main

def burden_exposure(
    genes: list[str],
    variants: Path,
    matched: Path,
    carriers_template: str,
    pheno: Path,
    max_maf: float,
    id_column: str = Constants.UKB_ID_COLUMN,
    prefer_studies: list[str] | None = None,
    config_dir: Path = Paths.MARVEL_BURDEN_CONFIG,
    out_dir: Path = Paths.MARVEL_BURDEN_OUT,
    tasks_path: Path = FileNames.MARVEL_BURDEN_TASKS,
    summary_path: Path = FileNames.BURDEN_EXPOSURE_SUMMARY,
    exposure_template: str = FileNames.BURDEN_EXPOSURE_TEMPLATE,
) -> None:
    """Write the burden exposures, cnfs, job array and summary.

    Parameters
    ----------
    genes : `list` [`str`]
        Genes; a gene without a carriers file is skipped (warned).
    variants : `Path`
        `lipid_variants.tsv`.
    matched : `Path`
        `matched_variants.tsv.gz`, for the preferred studies' sites.
    carriers_template : `str`
        Wide carriers file per gene, with ``{gene}``.
    pheno : `Path`
        Phenotype and covariate file of the cnfs.
    max_maf : `float`
        Sites with a higher MAF are left out.
    id_column : `str`, optional, default: `Constants.UKB_ID_COLUMN`
        Sample ID column of the carriers files (written as is).
    prefer_studies : `list` [`str`] or `NoneType`, optional
        Preferred study accessions; default
        `Constants.BURDEN_PREFER_STUDIES`.
    config_dir, out_dir : `Path`, optional
        Cnf directory and the parent of the marvel outdirs.
    tasks_path, summary_path : `Path`, optional
        Job-array file and summary.
    exposure_template : `str`, optional
        Exposure file per gene, with ``{gene}`` and ``{suffix}``.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If no gene has a carriers file.
    """
    studies = list(prefer_studies or Constants.BURDEN_PREFER_STUDIES)
    log_stage("variant sets")
    sites = read_sites(variants, genes)
    prefer = read_prefer_sites(
        matched, studies, Constants.BURDEN_FALLBACK_OUTCOME
    )
    strata = subset_strata()
    check_strata(pheno, strata)
    summary: list[dict] = []
    task_rows: list[dict] = []
    for gene in genes:
        log_stage(gene)
        path = Path(carriers_template.format(gene=gene))
        if not path.exists():
            log_warn(f"{gene}: no carriers file {path}, skipped")
            continue
        gene_sites = sites[sites[_S_GENE] == gene]
        if gene_sites.empty:
            log_warn(f"{gene}: no listed sites, skipped")
            continue
        columns = carrier_columns(path, gene_sites)
        carriers = stream_carriers(
            path, list(columns["column"]), id_column,
            Constants.MARVEL_CARRIER_THRESHOLD,
            Constants.OLD_CARRIERS_CHUNK_ROWS,
        )
        log_info(f"{gene}: {len(carriers.ids)} samples")
        carrier, missing, swapped, above_maf = site_carriers(
            gene, columns, carriers, max_maf
        )
        exposures, rows = collapse_masks(
            gene, gene_sites, carrier, missing, swapped, above_maf,
            prefer.get(gene, set()), len(carriers.ids),
        )
        summary.extend(rows)
        files: dict[str, Path] = {}
        for suffix in ("", Constants.BURDEN_FALLBACK_SUFFIX):
            names = [
                name for name in exposures
                if name.endswith(Constants.BURDEN_FALLBACK_SUFFIX)
                == bool(suffix)
            ]
            if not names:
                log_warn(f"{gene}: no exposures for file suffix "
                         f"{suffix!r}, not written")
                continue
            table = pd.DataFrame({id_column: carriers.ids})
            for name in names:
                table[name] = exposures[name]
            out = Path(exposure_template.format(gene=gene, suffix=suffix))
            _write_table_atomic(table, out)
            files[suffix] = out
        task_rows.extend(
            write_run_files(gene, files, pheno, strata, config_dir, out_dir)
        )
    if not task_rows:
        raise FileNotFoundError("no gene had a carriers file with carriers")
    tasks = pd.DataFrame(task_rows)
    tasks.insert(0, ColumnNames.ROWIDX, range(1, len(tasks) + 1))
    tasks = tasks[list(_TASK_COLUMNS)]
    tasks_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_tasks = tasks_path.with_suffix(tasks_path.suffix + ".tmp")
    tasks.to_csv(tmp_tasks, sep="\t", index=False)
    tmp_tasks.replace(tasks_path)
    log_info(f"wrote {len(tasks)} job-array rows to {tasks_path}")
    _write_table_atomic(pd.DataFrame(summary), summary_path)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Collapse the UKB carriers per gene and variant set into 0/1 "
            "burden exposures and write the old marvel run files."
        )
    )
    parser.add_argument(
        "--genes",
        nargs="+",
        help=f"genes (default: the genes of {FileNames.MARVEL_TASKS.name})",
    )
    parser.add_argument(
        "--variants",
        type=Path,
        default=FileNames.LIPID_VARIANTS,
        help="variant list (default: %(default)s)",
    )
    parser.add_argument(
        "--matched",
        type=Path,
        default=FileNames.MATCHED_VARIANTS,
        help="matched variants, for the preferred studies' sites "
        "(default: %(default)s)",
    )
    parser.add_argument(
        "--carriers",
        default=FileNames.OLD_CARRIERS_TEMPLATE,
        help="wide carriers files, with {gene} (default: %(default)s)",
    )
    parser.add_argument(
        "--pheno",
        type=Path,
        default=FileNames.UKB_PHENO,
        help="phenotype + covariate file of the cnfs (default: %(default)s)",
    )
    parser.add_argument(
        "--max-maf",
        type=float,
        default=Constants.REGION_MAX_MAF,
        help="leave out sites with a higher MAF (default: %(default)s)",
    )
    parser.add_argument(
        "--prefer-studies",
        nargs="+",
        default=list(Constants.BURDEN_PREFER_STUDIES),
        help="preferred study accessions (default: %(default)s)",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    args = parser.parse_args()
    if "{gene}" not in args.carriers:
        parser.error("--carriers must contain {gene}")
    if not 0 < args.max_maf <= 0.5:
        parser.error("--max-maf must be in (0, 0.5]")
    if args.genes is None:
        tasks = pd.read_csv(FileNames.MARVEL_TASKS, sep="\t", dtype=str)
        args.genes = list(dict.fromkeys(tasks[ColumnNames.GENE]))
    return args


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.BURDEN_EXPOSURE):
        burden_exposure(
            args.genes,
            args.variants,
            args.matched,
            args.carriers,
            args.pheno,
            args.max_maf,
            prefer_studies=args.prefer_studies,
        )


if __name__ == "__main__":
    main()
