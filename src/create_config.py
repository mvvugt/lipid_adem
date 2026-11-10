#!/usr/bin/env python3
"""
Write the new marvel (0.5.1) TOML configs, one per analysis x UKB subset,
and the run table `src/lipid_adem.sh` loops over.

Analyses (docs/marvel_migration_handoff.md, "Plan"):

- ``variant``: one exposure per variant, additive dosage, on
  `FileNames.MARVEL_VARIANTS` (`FileNames.LIPID_VARIANTS` minus
  `Const.EXCLUDED_GENES`, written here); subsets all, all_apoe, eur.
- ``burden`` / ``burden_fb``: the burden_exposure.py ``--mask-lists``
  lists (`FileNames.BURDEN_MASK_VARIANTS_TEMPLATE`), carrier of any site
  per mask; subsets `Burden.SUBSETS`.
- ``apoe``: the 0/1 diplotype columns of `FileNames.APOE_EXPOSURE` as
  ``input.exposures`` (associate only); subsets all, eur_overall.

``variant`` and ``burden*`` run with ``slurm_array.sh -s final`` on the
extract chunks in `Paths.MARVEL_RUN`; ``apoe`` with ``marvelous
associate``. The run table holds the stage per row.

Requires log_tools installed (pip install log_tools) for RUN_LOG.md logging.
"""
from __future__ import annotations


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info
from log_tools.setup import runlog_setup

from project_constants import (
    Apoe,
    ApoeStratum,
    Burden,
    ColumnNames,
    Const,
    FileNames,
    Marvel,
    Paths,
    RunlogOrder,
    Ukb,
    VariantListColumns,
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# settings

# binary outcomes of the per-variant run (old create_config.py), GLM-Binom
VARIANT_BINARY: tuple[str, ...] = (
    "ascvd_ii",
    "all_cause_dementia_algo",
    "all_cause_dementia_combined",
    "alzheimers_disease_algo",
    "alzheimers_disease_combined",
    "vascular_dementia_algo",
    "frontotemporal_dementia_algo",
)
# stage per analysis: `slurm_array.sh -s final` or `marvelous associate`
STAGE_FINAL: str = "final"
STAGE_ASSOCIATE: str = "associate"
# run table columns
RUN_COLUMNS: tuple[str, ...] = (
    "analysis", "subset", "stage", "prefix", "config",
)


@dataclass(frozen=True)
class Analysis:
    """One marvel analysis, written once per subset.

    Attributes
    ----------
    name : `str`
        Analysis name, used in the TOML file name and prefix.
    subsets : `tuple` [`str`, ...]
        Keys of `subset_strata`.
    binary, continuous : `tuple` [`str`, ...]
        Outcome columns tested with GLM-Binom and OLS.
    variants : `Path` or `NoneType`
        ``input.variants`` (aggregate on the extract chunks).
    exposures : `Path` or `NoneType`
        ``input.exposures`` (associate only).
    variant_mode : `str`
        ``extract.variant_mode``.
    category_column : `str` or `NoneType`
        ``extract.category_column`` (one exposure per category).
    strata_ref : `int` or `NoneType`
        ``stratification.strata_ref``.
    """
    name: str
    subsets: tuple[str, ...]
    binary: tuple[str, ...]
    continuous: tuple[str, ...]
    variants: Path | None = None
    exposures: Path | None = None
    variant_mode: str = "binary"
    category_column: str | None = None
    strata_ref: int | None = None

    @property
    def stage(self) -> str:
        """Return the run stage: associate for ``input.exposures``."""
        return STAGE_ASSOCIATE if self.exposures else STAGE_FINAL


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def burden_outcomes(fallback: bool) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Return the binary and continuous outcomes of a burden run.

    As burden_exposure.py `outcome_tests`: `Marvel.UKB_OUTCOMES`, lipids
    (`Const.LIPID_OUTCOMES`) continuous; the fallback run tests
    `Burden.FALLBACK_OUTCOME` only.

    Parameters
    ----------
    fallback : `bool`
        True for the ``_fb`` masks.

    Returns
    -------
    binary, continuous : `tuple` [`str`, ...]
        Outcome columns.
    """
    binary: list[str] = []
    continuous: list[str] = []
    for column, outcome in Marvel.UKB_OUTCOMES.items():
        if fallback and outcome != Burden.FALLBACK_OUTCOME:
            continue
        if outcome in Const.LIPID_OUTCOMES:
            continuous.append(column)
        else:
            binary.append(column)
    return tuple(binary), tuple(continuous)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def analyses() -> tuple[Analysis, ...]:
    """Return the analyses to write.

    Returns
    -------
    analyses : `tuple` [`Analysis`, ...]
        variant, burden, burden_fb and apoe.
    """
    lipids = tuple(
        column for column, outcome in Marvel.UKB_OUTCOMES.items()
        if outcome in Const.LIPID_OUTCOMES
    )
    mask_list = FileNames.BURDEN_MASK_VARIANTS_TEMPLATE
    fb_binary, fb_continuous = burden_outcomes(fallback=True)
    binary, continuous = burden_outcomes(fallback=False)
    return (
        Analysis(
            name="variant",
            subsets=("all", "all_apoe", "eur"),
            binary=VARIANT_BINARY,
            continuous=lipids,
            variants=FileNames.MARVEL_VARIANTS,
            variant_mode="dosage",
        ),
        Analysis(
            name="burden",
            subsets=Burden.SUBSETS,
            binary=binary,
            continuous=continuous,
            variants=Path(mask_list.format(suffix="")),
            category_column=VariantListColumns.MASK,
            strata_ref=0,
        ),
        Analysis(
            name=f"burden{Burden.FALLBACK_SUFFIX}",
            subsets=Burden.SUBSETS,
            binary=fb_binary,
            continuous=fb_continuous,
            variants=Path(mask_list.format(suffix=Burden.FALLBACK_SUFFIX)),
            category_column=VariantListColumns.MASK,
            strata_ref=0,
        ),
        Analysis(
            name="apoe",
            subsets=("all", "eur_overall"),
            binary=VARIANT_BINARY,
            continuous=lipids,
            exposures=FileNames.APOE_EXPOSURE,
        ),
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def subset_strata() -> dict[str, tuple[bool, dict[str, dict[str, tuple]]]]:
    """Return ``stratify_overall`` and the strata of each UKB subset.

    Stratum names are the old cnf ``Stratification name`` values, so the
    downstream APOE strata and study names do not change.

    Returns
    -------
    subsets : `dict`
        Subset -> (``stratify_overall``, stratum name -> column ->
        values). Columns in one stratum are AND-combined; a value list
        means any of them.
    """
    eur = {Ukb.POP_COL: tuple(Ukb.EUR_POPS)}
    apoe = {
        stratum: {Apoe.UKB_COL: tuple(genotypes)}
        for stratum, genotypes in ApoeStratum.GENOTYPES.items()
    }
    sep = Marvel.ANCESTRY_SEP
    return {
        "all": (True, {}),
        "all_apoe": (False, apoe),
        "eur": (False, {"EUR": eur} | {
            f"EUR{sep}{stratum}": eur | criterion
            for stratum, criterion in apoe.items()
        }),
        "eur_overall": (False, {"EUR": eur}),
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_strata(pheno: Path, columns: dict[str, set[str]]) -> None:
    """Check that every listed stratum value occurs in the phenotypes.

    marvel keeps the rows whose value is listed and does not complain
    about a value that never occurs, so a misspelled value would silently
    shrink a stratum.

    Parameters
    ----------
    pheno : `Path`
        Phenotype file of the TOMLs.
    columns : `dict` [`str`, `set` [`str`]]
        Column -> the values listed for it.

    Returns
    -------
    `None`

    Raises
    ------
    ValueError
        If a column or value is missing from `pheno`.
    """
    header = pd.read_csv(pheno, sep="\t", nrows=0).columns
    absent_columns = sorted(set(columns) - set(header))
    if absent_columns:
        raise ValueError(f"{pheno}: no column(s) {absent_columns}")
    table = pd.read_csv(pheno, sep="\t", usecols=sorted(columns), dtype=str)
    for column, values in sorted(columns.items()):
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
def _toml_value(value: object) -> str:
    """Format a scalar or list as a TOML value.

    Parameters
    ----------
    value : `object`
        `str`, `Path`, `bool`, `int`, `float`, or a `list`/`tuple` of them.

    Returns
    -------
    text : `str`
        The TOML value (JSON string escapes are valid TOML).

    Raises
    ------
    TypeError
        For any other type.
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, (str, Path)):
        return json.dumps(str(value))
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(_toml_value(v) for v in value) + "]"
    raise TypeError(f"no TOML format for {type(value).__name__}: {value!r}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _toml_table(header: str, items: dict[str, object]) -> list[str]:
    """Format one TOML table; `None` values are left out.

    Parameters
    ----------
    header : `str`
        Table header, e.g. ``[input]`` or ``[[tests]]``.
    items : `dict` [`str`, `object`]
        Key -> value.

    Returns
    -------
    lines : `list` [`str`]
        Header and ``key = value`` lines, then a blank line.
    """
    lines = [header]
    for key, value in items.items():
        if value is None:
            continue
        name = key if key.isidentifier() else json.dumps(key)
        lines.append(f"{name} = {_toml_value(value)}")
    return lines + [""]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def toml_text(analysis: Analysis, subset: str, pheno: Path) -> str:
    """Return the TOML config of one analysis and subset.

    Parameters
    ----------
    analysis : `Analysis`
        The analysis.
    subset : `str`
        Key of `subset_strata`.
    pheno : `Path`
        Phenotype and covariate file.

    Returns
    -------
    text : `str`
        The TOML file content.
    """
    overall, strata = subset_strata()[subset]
    lines = [
        "# Written by src/create_config.py; do not edit by hand.",
        f"# analysis {analysis.name}, subset {subset}",
        "# geno is set by slurm_array.sh, output.dir by --outdir.",
        "",
    ]
    lines += _toml_table("[input]", {
        "variants": analysis.variants,
        "exposures": analysis.exposures,
        "geno": [],
        "phenotypes": pheno,
        "covariates": pheno,
        "id_column": Ukb.ID_COL,
        "chrom_column": "chr",
        "pos_column": "pos",
        "ref_column": "a1",
        "alt_column": "a2",
    })
    if analysis.exposures is None:
        lines += _toml_table("[extract]", {
            "carrier_threshold": Marvel.CARRIER_THR,
            "min_dosage": 0.0,
            "variant_mode": analysis.variant_mode,
            "category_mode": "any" if analysis.category_column else None,
            "category_column": analysis.category_column,
            "max_gene_missing": 0.25,
            "allow_indel_swap": False,
        })
    tests = (
        [(o, "binary", "GLM-Binom") for o in analysis.binary]
        + [(o, "continuous", "OLS") for o in analysis.continuous]
    )
    for outcome, kind, test in tests:
        lines += _toml_table("[[tests]]", {
            "outcome": outcome, "type": kind, "tests": [test],
        })
    for model, columns in Burden.MODELS.items():
        if columns:
            lines += _toml_table(
                f"[covariates.{Marvel.MODEL_MAP[model]}]",
                {"columns": list(columns)},
            )
    lines += _toml_table("[stratification]", {
        "stratify_overall": overall,
        "strata_ref": analysis.strata_ref,
    })
    for name, filters in strata.items():
        lines += _toml_table("[[strata]]", {"name": name} | {
            column: list(values) for column, values in filters.items()
        })
    lines += _toml_table("[options]", {
        "min_group_size": 1,
        "max_missingness": 0.5,
        "raise_on_error": False,
        "cov_miss_error": True,
        "file_sep": "\t",
        "var_sep": ":",
    })
    lines += _toml_table("[output]", {
        "prefix": run_prefix(analysis.name, subset),
    })
    return "\n".join(lines)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_prefix(analysis: str, subset: str) -> str:
    """Return the marvel output prefix of one analysis and subset.

    Parameters
    ----------
    analysis, subset : `str`
        Analysis and subset names.

    Returns
    -------
    prefix : `str`
        ``lipid_<analysis>_<subset>``.
    """
    return f"lipid_{analysis}_{subset}"


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
def write_variant_list(source: Path, target: Path) -> None:
    """Write the per-variant list: `source` minus the excluded genes.

    Parameters
    ----------
    source : `Path`
        `FileNames.LIPID_VARIANTS`.
    target : `Path`
        `FileNames.MARVEL_VARIANTS` (gzipped TSV).

    Returns
    -------
    `None`

    Raises
    ------
    ValueError
        If an excluded gene is not in `source` (misspelled constant).
    """
    variants = pd.read_csv(source, sep="\t", dtype=str, keep_default_na=False)
    genes = variants[ColumnNames.GENE]
    excluded = set(Const.EXCLUDED_GENES)
    unknown = sorted(excluded - set(genes))
    if unknown:
        raise ValueError(f"{source}: no variants of excluded gene(s) {unknown}")
    kept = variants[~genes.isin(excluded)]
    log_info(
        f"variant list: {len(kept)} of {len(variants)} rows, genes "
        + ", ".join(sorted(set(kept[ColumnNames.GENE])))
        + f" (excluded {', '.join(sorted(excluded))})"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = target.with_suffix(target.suffix + ".tmp")
    kept.to_csv(tmp_path, sep="\t", index=False, compression="gzip")
    tmp_path.replace(target)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_configs(
    pheno: Path,
    config_dir: Path,
    runs: Path,
    check_pheno: bool = True,
) -> pd.DataFrame:
    """Write one TOML per analysis x subset and the run table.

    Parameters
    ----------
    pheno : `Path`
        Phenotype and covariate file of the TOMLs.
    config_dir : `Path`
        Directory of the TOMLs (``<analysis>_<subset>.toml``).
    runs : `Path`
        Run table (`RUN_COLUMNS`).
    check_pheno : `bool`, optional, default: `True`
        Check the stratum values against `pheno` (`check_strata`).

    Returns
    -------
    table : `pd.DataFrame`
        The run table.
    """
    strata = subset_strata()
    todo = [(a, s) for a in analyses() for s in a.subsets]
    if check_pheno:
        columns: dict[str, set[str]] = {}
        for _, subset in todo:
            for filters in strata[subset][1].values():
                for column, values in filters.items():
                    columns.setdefault(column, set()).update(values)
        check_strata(pheno, columns)
    rows = []
    for analysis, subset in todo:
        path = config_dir / f"{analysis.name}_{subset}.toml"
        _write_text_atomic(toml_text(analysis, subset, pheno), path)
        rows.append((
            analysis.name, subset, analysis.stage,
            run_prefix(analysis.name, subset), str(path),
        ))
        log_info(f"{analysis.name} ({subset}): {path}")
    table = pd.DataFrame(rows, columns=list(RUN_COLUMNS))
    runs.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = runs.with_suffix(runs.suffix + ".tmp")
    table.to_csv(tmp_path, sep="\t", index=False)
    tmp_path.replace(runs)
    log_info(f"run table: {runs} ({len(table)} runs)")
    return table


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Write the new marvel TOML configs and run table."
    )
    parser.add_argument(
        "--pheno", type=Path, default=FileNames.UKB_PHENO,
        help="phenotype and covariate file (default: %(default)s)",
    )
    parser.add_argument(
        "--variants", type=Path, default=FileNames.LIPID_VARIANTS,
        help="full variant list (default: %(default)s)",
    )
    parser.add_argument(
        "--config-dir", type=Path, default=Paths.MARVEL_CONFIG,
        help="TOML directory (default: %(default)s)",
    )
    parser.add_argument(
        "--runs", type=Path, default=FileNames.MARVEL_RUNS,
        help="run table (default: %(default)s)",
    )
    parser.add_argument(
        "--no-pheno-check", action="store_true",
        help="do not check the stratum values against --pheno",
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

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.CREATE_CONFIG):
        write_variant_list(args.variants, FileNames.MARVEL_VARIANTS)
        write_configs(
            args.pheno,
            args.config_dir,
            args.runs,
            check_pheno=not args.no_pheno_check,
        )


if __name__ == "__main__":
    main()
