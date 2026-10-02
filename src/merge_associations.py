#!/usr/bin/env python3
"""
Gathers filtered sumstats, adds own UKB/AoU (marvel) results, curated GWAS
Catalog associations and Open Targets gene-burden evidence, and writes the
merged associations table.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from log_tools.emitter import (
    log_count,
    log_count_summary,
    log_info,
    log_stage,
    log_warn,
)
from log_tools.setup import runlog_setup

import functions
from project_constants import (
    Ancestry,
    ColumnNames,
    Constants,
    FileNames,
    HarmonisedColumns,
    MafStatus,
    Paths,
    RunlogOrder,
    SourceColumnMaps,
)


# log_count key for EFO ids with no curated associations at all
_NO_CURATED_COUNT_KEY: str = "efo_no_curated"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def load_filter_results(
    outcome_desc: dict[tuple[str, str], str],
    trait_labels: dict[str, str],
    study_traits: dict[str, tuple[str, str]],
) -> pd.DataFrame:
    """Load, label and harmonise the filtered per-study result files.

    Only the `outfile` paths in the current
    `FileNames.STUDY_OUTCOMES_FILE` are read, so stale files left in
    `gwas_filtered/` (from studies bumped past the cap, or the old
    per-gene layout) are ignored. Listed outfiles that do not exist yet
    are skipped with a warning. Each file (one study, all genes) is read
    once; when several rows (outcomes) point to the same file, its rows
    are repeated once per outcome.

    Parameters
    ----------
    outcome_desc : `dict[tuple[str, str], str]`
        `(outcome, efo_id)` -> outcome description in words.
    trait_labels : `dict[str, str]`
        `study_accession` -> the study's trait label.
    study_traits : `dict[str, tuple[str, str]]`
        `study_accession` -> `(mapped_trait_id, mapped_trait)`, the
        terms the GWAS Catalog study is annotated with.

    Returns
    -------
    combined : `pd.DataFrame`
        Harmonised rows (see `functions.harmonise_frame`) with `source`
        set to `"summary-stats"`. Empty if no filtered output files exist.

    Raises
    ------
    FileNotFoundError
        If the study-outcomes file does not exist.
    """
    tasks = functions.load_tasks(FileNames.STUDY_OUTCOMES_FILE)
    frames = []
    missing: list[Path] = []
    n_files = 0
    # groupby(sort=False) keeps the tasks-file order
    for outfile, file_tasks in tasks.groupby(
        ColumnNames.OUTFILE, sort=False
    ):
        result_path = Path(outfile)
        if not result_path.exists():
            missing.append(result_path)
            continue
        n_files += 1
        frame = _read_filtered_file(result_path)
        if frame.empty:
            continue
        for _, task in file_tasks.iterrows():
            labelled = frame.copy()
            outcome = task[ColumnNames.OUTCOME]
            efo_id = task[ColumnNames.EFO_ID]
            accession = task[ColumnNames.STUDY_ACCESSION]
            labelled[ColumnNames.SOURCE] = "summary-stats"
            # from the tasks file, not the outfile, so outfiles filtered
            # before manual studies got their own source are relabelled
            labelled[ColumnNames.SOURCE_DB] = task[ColumnNames.SOURCE]
            labelled[ColumnNames.OUTCOME] = outcome
            labelled[ColumnNames.EFO_ID] = efo_id
            # only trait-searched studies (efo_id set) can use child traits
            labelled[ColumnNames.CHILD_TRAITS] = (
                isinstance(efo_id, str)
                and efo_id != ""
                and functions.includes_child_traits(outcome)
            )
            trait_id, trait = study_traits.get(accession, ("", ""))
            labelled[ColumnNames.MAPPED_TRAIT_ID] = trait_id or pd.NA
            labelled[ColumnNames.MAPPED_TRAIT] = trait or pd.NA
            labelled[HarmonisedColumns.OUTCOME_DESC] = outcome_desc.get(
                (outcome, efo_id), pd.NA
            )
            labelled[HarmonisedColumns.TRAIT_LABEL] = trait_labels.get(
                accession, pd.NA
            )
            frames.append(labelled)

    if missing:
        preview = ", ".join(str(p) for p in missing[:3])
        log_warn(
            f"{len(missing)} outfiles listed in "
            f"{FileNames.STUDY_OUTCOMES_FILE} "
            f"do not exist yet, skipped (first: {preview})"
        )

    n_rows = sum(len(frame) for frame in frames)
    log_info(
        f"summary-stats: {n_files} files, {n_rows} rows incl. one copy "
        f"per outcome ({len(missing)} missing)"
    )
    if not frames:
        return pd.DataFrame()
    harmonised = []
    for frame in frames:
        column_map = (
            SourceColumnMaps.FINNGEN
            if frame[ColumnNames.SOURCE_DB].iloc[0] == "finngen"
            else SourceColumnMaps.GWAS_CATALOG
        )
        harmonised.append(functions.harmonise_frame(frame, column_map))
    return pd.concat(harmonised, ignore_index=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _split_burden_rows(
    summary: pd.DataFrame, ensembl_ids: dict[str, str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Move gene-burden mask rows out of the summary-stats rows.

    Some catalog sumstats files (e.g. UKB exome burden tests) hold one
    row per gene and mask, written like a variant: effect allele the
    mask (e.g. "M1.0001"), other allele "ref", and `Name`
    ``GENE(ENSG...).GENE.<mask>``. Only rows for the region's own gene
    (by Ensembl id) are kept; rows for neighbouring genes in the region
    are dropped.

    Parameters
    ----------
    summary : `pd.DataFrame`
        Harmonised summary-stats rows from `load_filter_results`.
    ensembl_ids : `dict[str, str]`
        Gene symbol -> Ensembl gene id (gene_list.txt).

    Returns
    -------
    variants : `pd.DataFrame`
        `summary` without the mask rows.
    burden : `pd.DataFrame`
        The own-gene mask rows with `source` ``"gene-burden"`` and
        chrom, pos, rsid, alleles, `variant_id` and `maf_status` cleared
        (the mask stays in `src_Name`); empty if there are none.
    """
    hc = HarmonisedColumns
    name_column = hc.RAW_PREFIX + "Name"
    if summary.empty or name_column not in summary.columns:
        return summary, summary.iloc[0:0]
    is_mask = summary[hc.EFFECT_ALLELE].map(functions.is_burden_mask_allele)
    if not is_mask.any():
        return summary, summary.iloc[0:0]
    names = summary.loc[is_mask, name_column].astype("string").str.extract(
        Constants.BURDEN_NAME_PATTERN
    )
    own_gene = names["ensembl_id"] == summary.loc[is_mask, hc.GENE].map(
        ensembl_ids
    )
    own_gene = own_gene.fillna(False).astype(bool)
    burden = summary.loc[is_mask].loc[own_gene].copy()
    burden[hc.SOURCE] = "gene-burden"
    for column in (
        hc.CHROM,
        hc.POS,
        hc.RSID,
        hc.VARIANT_ID,
        hc.EFFECT_ALLELE,
        hc.OTHER_ALLELE,
        hc.MAF_STATUS,
    ):
        burden[column] = pd.NA
    log_info(
        f"summary-stats: {int(is_mask.sum())} burden mask rows -> "
        f"{len(burden)} gene-burden rows, {int((~own_gene).sum())} for "
        "neighbouring genes dropped"
    )
    return summary.loc[~is_mask], burden


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _marvel_identity(
    frame: pd.DataFrame, entry: pd.Series, source: str
) -> pd.DataFrame:
    """Set the identity columns of marvel rows from their table entry.

    Parameters
    ----------
    frame : `pd.DataFrame`
        Marvel result rows, `gene` already set.
    entry : `pd.Series`
        The row of `functions.load_marvel_table` the rows come from.
    source : `str`
        ``"summary-stats"`` (variant rows) or ``"gene-burden"``.

    Returns
    -------
    labelled : `pd.DataFrame`
        `frame` with `source`, `source_db`, `study_accession`
        (``marvel_<cohort>_<ancestry>_<outcome>``, so per-ancestry runs
        of one cohort stay separate studies), `outcome`, `efo_id` (NA),
        `child_traits` (`False`), `trait_label` and `ancestry_group` set.
    """
    cohort = entry["cohort"]
    outcome = entry["outcome"]
    ancestry = entry[ColumnNames.ANCESTRY]
    labelled = frame.copy()
    labelled[ColumnNames.SOURCE] = source
    labelled[ColumnNames.SOURCE_DB] = (
        Constants.MARVEL_SOURCE_DB_PREFIX + cohort
    )
    labelled[ColumnNames.STUDY_ACCESSION] = (
        f"{Constants.MARVEL_SOURCE_DB_PREFIX}{cohort}_{ancestry}_{outcome}"
    )
    labelled[ColumnNames.OUTCOME] = outcome
    labelled[ColumnNames.EFO_ID] = pd.NA
    labelled[ColumnNames.CHILD_TRAITS] = False
    labelled[HarmonisedColumns.TRAIT_LABEL] = entry["variable"]
    labelled[HarmonisedColumns.ANCESTRY_GROUP] = ancestry
    return labelled


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_marvel_results(
    regions: dict[str, functions.GeneRegion],
    marvel_df: pd.DataFrame,
) -> list[pd.DataFrame]:
    """Load and harmonise own UKB/AoU association results (marvel).

    Each entry of `marvel_df` names one marvel results file and the
    `Variable`/`Model` to keep from it. A row whose `Exposure` is a
    variant (``chr:pos:a1:a2``, a2 counted) becomes a ``summary-stats``
    row for every gene region containing it, with effect allele a2 and
    other allele a1. A row whose `Exposure` is a gene in `regions`
    becomes a ``gene-burden`` row for that gene. Other rows are dropped
    (warned).

    Parameters
    ----------
    regions : `dict[str, functions.GeneRegion]`
        Gene symbol -> flanked region.
    marvel_df : `pd.DataFrame`
        From `functions.load_marvel_table`.

    Returns
    -------
    harmonised : `list[pd.DataFrame]`
        Harmonised frames (`functions.harmonise_frame`), `source_db`
        ``marvel_<cohort>`` and `study_accession`
        ``marvel_<cohort>_<ancestry>_<outcome>``. Empty if no entries or
        rows.

    Raises
    ------
    FileNotFoundError
        If a listed results file does not exist.
    ValueError
        If a results file lacks the `Exposure`/`Variable`/`Model` columns.
    """
    hc = HarmonisedColumns
    parts: list[pd.DataFrame] = []
    for _, entry in marvel_df.iterrows():
        path = Path(entry["path"])
        if not path.exists():
            raise FileNotFoundError(
                f"{FileNames.MARVEL_RESULTS}: results file not found: {path}"
            )
        results = pd.read_csv(path, sep="\t", dtype=str)
        missing = [
            col
            for col in ("Exposure", "Variable", "Model")
            if col not in results.columns
        ]
        if missing:
            raise ValueError(f"{path}: missing marvel column(s) {missing}")
        results = results[
            (results["Variable"] == entry["variable"])
            & (results["Model"] == entry["model"])
        ].reset_index(drop=True)

        variant_rows: list[dict] = []
        variant_index: list[int] = []
        burden_index: list[int] = []
        burden_genes: list[str] = []
        n_unplaced = 0
        for index, exposure in results["Exposure"].items():
            variant = functions.parse_marvel_exposure(exposure)
            if variant is None:
                if exposure in regions:
                    burden_index.append(index)
                    burden_genes.append(exposure)
                else:
                    n_unplaced += 1
                continue
            chrom, pos, a1, a2 = variant
            genes = [
                gene
                for gene, region in regions.items()
                if str(region.chrom).removeprefix("chr") == chrom
                and region.start <= pos <= region.end
            ]
            if not genes:
                n_unplaced += 1
            for gene in genes:
                variant_index.append(index)
                variant_rows.append(
                    {
                        hc.GENE: gene,
                        hc.CHROM: chrom,
                        hc.POS: pos,
                        hc.OTHER_ALLELE: a1,
                        hc.EFFECT_ALLELE: a2,
                    }
                )

        if variant_index:
            variants = results.loc[variant_index].reset_index(drop=True)
            parsed = pd.DataFrame(variant_rows)
            variants[ColumnNames.GENE] = parsed[hc.GENE]
            variants = _marvel_identity(variants, entry, "summary-stats")
            parts.append(
                functions.harmonise_frame(
                    variants,
                    SourceColumnMaps.MARVEL,
                    parsed=parsed.drop(columns=hc.GENE),
                )
            )
        if burden_index:
            burden = results.loc[burden_index].reset_index(drop=True)
            burden[ColumnNames.GENE] = burden_genes
            burden = _marvel_identity(burden, entry, "gene-burden")
            parts.append(
                functions.harmonise_frame(
                    burden, SourceColumnMaps.MARVEL, has_variants=False
                )
            )
        log_info(
            f"marvel {entry['cohort']} {entry['outcome']}: "
            f"{len(results)} rows -> {len(variant_index)} variant rows, "
            f"{len(burden_index)} gene-burden rows ({path.name})"
        )
        if n_unplaced:
            log_warn(
                f"marvel {entry['cohort']} {entry['outcome']}: {n_unplaced} "
                "exposures neither a variant in a gene region nor a gene "
                "in gene_list.txt, dropped"
            )
    return parts


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _cohort_overlap_studies(audit: pd.DataFrame) -> set[tuple[str, str]]:
    """List catalog studies excluded per outcome for cohort overlap.

    Parameters
    ----------
    audit : `pd.DataFrame`
        The study-discovery log from `_read_discovery_log`.

    Returns
    -------
    excluded : `set[tuple[str, str]]`
        `(outcome, study_accession)` pairs whose `reason` starts with
        `Constants.COHORT_OVERLAP_REASON_PREFIX`.
    """
    if audit.empty:
        return set()
    overlap = audit[ColumnNames.REASON].str.startswith(
        Constants.COHORT_OVERLAP_REASON_PREFIX
    )
    return set(
        zip(
            audit.loc[overlap, ColumnNames.OUTCOME],
            audit.loc[overlap, ColumnNames.STUDY_ACCESSION],
        )
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _read_filtered_file(path: Path) -> pd.DataFrame:
    """Read one filtered result file, removing stray CRLF carriage returns.

    Files filtered before the CRLF fix in `functions` can carry a
    trailing `"\\r"` on their last column name and values.

    Parameters
    ----------
    path : `Path`
        A filtered result file (`*_result.tsv.gz`).

    Returns
    -------
    frame : `pd.DataFrame`
        The file's rows, with `"\\r"` stripped from the last column.
    """
    frame = pd.read_csv(path, sep="\t", low_memory=False)
    frame.columns = [str(col).rstrip("\r") for col in frame.columns]
    last = frame.columns[-1]
    if frame[last].dtype == object:
        frame[last] = frame[last].str.rstrip("\r")
    return frame


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _outcome_descriptions(
    icd_df: pd.DataFrame,
) -> dict[tuple[str, str], str]:
    """Describe each (outcome, efo_id) pair in words, from the ICD table.

    Parameters
    ----------
    icd_df : `pd.DataFrame`
        The ICD/outcome table from `functions.load_icd_table`.

    Returns
    -------
    descriptions : `dict[tuple[str, str], str]`
        `(outcome, efo_id)` -> unique non-empty `description` values,
        joined with `"; "`, in file order.
    """
    descriptions: dict[tuple[str, str], str] = {}
    grouped = icd_df.groupby(
        [ColumnNames.OUTCOME, ColumnNames.EFO_ID], sort=False
    )
    for key, group in grouped:
        texts = [
            text
            for text in dict.fromkeys(group[ColumnNames.DESCRIPTION])
            if isinstance(text, str) and text.strip()
        ]
        descriptions[key] = "; ".join(texts)
    return descriptions


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _read_discovery_log() -> pd.DataFrame:
    """Read the study-discovery audit log written by `gwas_cat_prep.py`.

    Returns
    -------
    audit : `pd.DataFrame`
        `FileNames.STUDY_DISCOVERY_LOG`, all columns as strings with
        blanks as `""`; empty (warned) if the file does not exist.
    """
    if not FileNames.STUDY_DISCOVERY_LOG.exists():
        log_warn(
            f"{FileNames.STUDY_DISCOVERY_LOG} not found: GWAS Catalog "
            "trait labels and mapped traits left empty (rerun "
            "gwas_cat_prep.py, or gzip an existing uncompressed "
            "study_discovery_log.tsv)"
        )
        return pd.DataFrame()
    return pd.read_csv(
        FileNames.STUDY_DISCOVERY_LOG, sep="\t", dtype=str
    ).fillna("")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_mapped_traits(audit: pd.DataFrame) -> dict[str, tuple[str, str]]:
    """Map each GWAS Catalog study to the terms it is annotated with.

    Parameters
    ----------
    audit : `pd.DataFrame`
        The study-discovery log from `_read_discovery_log`.

    Returns
    -------
    traits : `dict[str, tuple[str, str]]`
        `study_accession` -> `(mapped_trait_id, mapped_trait)`. Empty if
        the log predates these columns (warned; rerun gwas_cat_prep.py).
    """
    columns = (ColumnNames.MAPPED_TRAIT_ID, ColumnNames.MAPPED_TRAIT)
    if audit.empty:
        return {}
    if not all(col in audit.columns for col in columns):
        log_warn(
            f"{FileNames.STUDY_DISCOVERY_LOG} has no mapped-trait columns: "
            "mapped_trait_* left empty (rerun gwas_cat_prep.py)"
        )
        return {}
    traits: dict[str, tuple[str, str]] = {}
    for accession, trait_id, trait in zip(
        audit[ColumnNames.STUDY_ACCESSION], *(audit[col] for col in columns)
    ):
        if trait_id and accession not in traits:
            traits[accession] = (trait_id, trait)
    return traits


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_ancestry(audit: pd.DataFrame) -> dict[str, str]:
    """Map each study in the discovery log to its `Ancestry` code.

    Parameters
    ----------
    audit : `pd.DataFrame`
        The study-discovery log from `_read_discovery_log`.

    Returns
    -------
    ancestry : `dict[str, str]`
        `study_accession` (FinnGen: phenocode) -> `ancestry_group`. A log
        that predates `ancestry_group` is harmonised from its free-text
        `ancestry` column (warned; FinnGen rows then get
        `Ancestry.FINNGEN`). Empty if the log is empty.
    """
    if audit.empty:
        return {}
    if ColumnNames.ANCESTRY_GROUP in audit.columns:
        groups = audit[ColumnNames.ANCESTRY_GROUP]
    else:
        log_warn(
            f"{FileNames.STUDY_DISCOVERY_LOG} has no ancestry_group column: "
            "harmonised from ancestry here (rerun gwas_cat_prep.py)"
        )
        groups = audit[ColumnNames.ANCESTRY].map(functions.harmonise_ancestry)
        groups = groups.where(
            audit[ColumnNames.SOURCE] != "finngen", Ancestry.FINNGEN
        )
    ancestry: dict[str, str] = {}
    for accession, group in zip(audit[ColumnNames.STUDY_ACCESSION], groups):
        if group and accession not in ancestry:
            ancestry[accession] = group
    return ancestry


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _fill_ancestry(
    combined: pd.DataFrame, ancestry: dict[str, str]
) -> pd.DataFrame:
    """Set `ancestry_group` on rows that do not have one yet.

    Parameters
    ----------
    combined : `pd.DataFrame`
        All harmonised rows; marvel rows already carry `ancestry_group`.
    ancestry : `dict[str, str]`
        From `_study_ancestry`.

    Returns
    -------
    filled : `pd.DataFrame`
        `combined` with `ancestry_group` looked up by `study_accession`,
        else `Ancestry.NR` (e.g. curated hits of studies the discovery
        log does not list). Counts per source and code are logged.
    """
    hc = HarmonisedColumns
    filled = combined.copy()
    missing = filled[hc.ANCESTRY_GROUP].isna()
    looked_up = filled.loc[missing, hc.STUDY_ACCESSION].map(ancestry)
    n_unknown = int(looked_up.isna().sum())
    filled.loc[missing, hc.ANCESTRY_GROUP] = looked_up.fillna(Ancestry.NR)
    log_info(
        f"ancestry: {n_unknown} rows of studies not in the discovery log "
        f"labelled {Ancestry.NR}"
    )
    counts = filled.groupby([hc.SOURCE, hc.ANCESTRY_GROUP]).size()
    for (source, group), n in counts.items():
        log_info(f"ancestry: {source} {group}={n}")
    return filled


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _study_trait_labels(audit: pd.DataFrame) -> dict[str, str]:
    """Map each study accession to the trait label its source reports.

    Uses the `trait` column of the study-discovery log, then fills
    FinnGen phenocodes still missing from the `phenotype` column of the
    FinnGen manifest.

    Parameters
    ----------
    audit : `pd.DataFrame`
        The study-discovery log from `_read_discovery_log`.

    Returns
    -------
    labels : `dict[str, str]`
        `study_accession` (or FinnGen phenocode) -> trait label.
    """
    labels: dict[str, str] = {}
    if not audit.empty:
        for accession, trait in zip(
            audit[ColumnNames.STUDY_ACCESSION], audit[ColumnNames.TRAIT]
        ):
            if trait and accession not in labels:
                labels[accession] = trait
    manifest = functions.load_finngen_manifest()
    for phenocode, phenotype in zip(
        manifest["phenocode"], manifest["phenotype"]
    ):
        if phenotype and phenocode not in labels:
            labels[phenocode] = phenotype
    return labels


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _format_counts(counts: dict[str, int]) -> str:
    """Render non-zero counts as ``KEY=n`` pairs, or ``none``.

    Parameters
    ----------
    counts : `dict[str, int]`
        Count per key (e.g. per gene), in display order.

    Returns
    -------
    text : `str`
        Space-separated ``KEY=n`` pairs for keys with a count above 0,
        or ``"none"`` if every count is 0.
    """
    pairs = [f"{key}={n}" for key, n in counts.items() if n > 0]
    return " ".join(pairs) if pairs else "none"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _expand_burden_outcomes(
    evidence: pd.DataFrame,
    disease_ids: dict[str, set[tuple[str, str]]],
    outcome_desc: dict[tuple[str, str], str],
) -> pd.DataFrame:
    """Tag gene-burden evidence rows with the outcomes they belong to.

    Parameters
    ----------
    evidence : `pd.DataFrame`
        Rows from `functions.gene_burden_evidence`.
    disease_ids : `dict[str, set[tuple[str, str]]]`
        From `functions.open_targets_disease_ids`.
    outcome_desc : `dict[tuple[str, str], str]`
        `(outcome, efo_id)` -> outcome description.

    Returns
    -------
    expanded : `pd.DataFrame`
        One row per evidence row and `(outcome, efo_id)` pair it counts
        for (a disease can belong to several outcomes), with `outcome`,
        `efo_id`, `child_traits` and `outcome_desc` set, in outcome then
        `efo_id` order. Empty if `evidence` is empty.
    """
    if evidence.empty:
        return evidence
    pairs = pd.DataFrame.from_records(
        [
            (disease_id, outcome, efo_id)
            for disease_id, matches in disease_ids.items()
            for outcome, efo_id in matches
        ],
        columns=["disease_id", ColumnNames.OUTCOME, ColumnNames.EFO_ID],
    )
    expanded = evidence.merge(pairs, on="disease_id", how="inner")
    expanded = expanded.sort_values(
        [ColumnNames.OUTCOME, ColumnNames.EFO_ID], kind="stable"
    ).reset_index(drop=True)
    expanded[ColumnNames.CHILD_TRAITS] = expanded[ColumnNames.OUTCOME].map(
        functions.includes_child_traits
    )
    expanded[HarmonisedColumns.OUTCOME_DESC] = [
        outcome_desc.get((outcome, efo_id), pd.NA)
        for outcome, efo_id in zip(
            expanded[ColumnNames.OUTCOME], expanded[ColumnNames.EFO_ID]
        )
    ]
    return expanded


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def merge_results() -> None:
    """Merge all evidence sources and write the merged associations table.

    Sources: filtered summary stats (GWAS Catalog, manual, FinnGen), own
    UKB/AoU marvel results (`load_marvel_results`), curated GWAS Catalog
    associations (minus studies excluded for cohort overlap) and Open
    Targets gene burden. Reuses the `efo_id`/`chrom`/`start`/`end` already resolved and
    persisted by `gwas_cat_prep.py` -- no lookups are repeated here.
    Curated associations are downloaded once per unique `efo_id` and
    child-trait setting (the download is gene-independent) and then
    filtered per gene region.

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If the gene or ICD/outcome placeholder files have not been filled in.
    """
    genes_df = functions.load_gene_table(FileNames.GENE_LIST)
    icd_df = functions.load_icd_table(FileNames.ICD_CODE_LIST)
    icd_df = functions.apply_outcome_efo_overrides(icd_df)

    outcome_desc = _outcome_descriptions(icd_df)

    ensembl_ids = dict(
        zip(
            genes_df[ColumnNames.GENE],
            genes_df[ColumnNames.ENSEMBL_ID].fillna("").astype(str).str.strip(),
        )
    )

    log_stage("load_sumstats")
    audit = _read_discovery_log()
    summary, catalog_burden = _split_burden_rows(
        load_filter_results(
            outcome_desc,
            _study_trait_labels(audit),
            _study_mapped_traits(audit),
        ),
        ensembl_ids,
    )
    parts = [summary, catalog_burden]

    excluded = icd_df[ColumnNames.EFO_ID].isin(Constants.EXCLUDED_EFO_IDS)
    for efo_id, outcome in sorted(
        set(
            zip(
                icd_df.loc[excluded, ColumnNames.EFO_ID],
                icd_df.loc[excluded, ColumnNames.OUTCOME],
            )
        )
    ):
        log_info(f"{efo_id} ({outcome}) in Constants.EXCLUDED_EFO_IDS, skipped")
    # excluded ids are dropped for both curated and gene-burden evidence
    outcome_efo_ids = (
        icd_df[
            ~icd_df[ColumnNames.EFO_ID].isin(["", Constants.NA_STRING])
            & ~excluded
        ]
        .groupby(ColumnNames.OUTCOME)[ColumnNames.EFO_ID]
        .unique()
    )

    regions = {
        gene_row[ColumnNames.GENE]: functions.gene_row_region(
            gene_row, Constants.GENE_COORD_FLANK_BP
        )
        for _, gene_row in genes_df.iterrows()
    }
    log_stage("marvel")
    marvel_df = functions.load_marvel_table()
    if marvel_df.empty:
        log_info(f"no own results listed in {FileNames.MARVEL_RESULTS}")
    parts.extend(load_marvel_results(regions, marvel_df))

    # fetch each (efo_id, child_traits) query once and filter it for every
    # gene; only one query's full record list is held in memory at a time
    curated_by_gene_query: dict[tuple[str, str, bool], pd.DataFrame] = {}
    # dict.fromkeys de-duplicates while keeping first-seen order
    unique_queries = list(dict.fromkeys(
        (efo_id, functions.includes_child_traits(outcome))
        for outcome, efo_ids in outcome_efo_ids.items()
        for efo_id in efo_ids
    ))
    log_stage("fetch_curated")
    for efo_id, child_traits in unique_queries:
        records = functions.fetch_curated_associations(
            efo_id, include_child_traits=child_traits
        )
        in_region: dict[str, int] = {}
        for gene, region in regions.items():
            curated = functions.filter_curated_associations(
                records, region, Constants.MAF_THRESHOLD
            )
            in_region[gene] = len(curated)
            curated_by_gene_query[(gene, efo_id, child_traits)] = curated
        # one line per EFO with any associations; empty EFOs only counted
        if records:
            scope = "with child traits" if child_traits else "exact"
            log_info(
                f"{efo_id} ({scope}): {len(records)} fetched; in region: "
                f"{_format_counts(in_region)}"
            )
        else:
            log_count(_NO_CURATED_COUNT_KEY)
        del records
    log_count_summary(
        _NO_CURATED_COUNT_KEY, label="EFO ids with 0 curated associations"
    )

    # assemble in gene -> outcome -> efo_id order so row order is unchanged
    log_stage("gene_burden")
    burden_disease_ids = functions.open_targets_disease_ids(outcome_efo_ids)
    burden_rows: dict[str, int] = {}
    maf_status_counts: dict[str, int] = {
        MafStatus.NUMERIC: 0,
        MafStatus.NOT_REPORTED: 0,
    }
    # curated hits of studies excluded for an outcome (own results for a
    # cohort they include) are dropped for that outcome too
    overlap_studies = _cohort_overlap_studies(audit)
    n_overlap_curated = 0
    for gene in regions:
        for outcome, efo_ids in outcome_efo_ids.items():
            child_traits = functions.includes_child_traits(outcome)
            for efo_id in efo_ids:
                curated = curated_by_gene_query[
                    (gene, efo_id, child_traits)
                ].copy()
                if not curated.empty:
                    curated[ColumnNames.GENE] = gene
                    curated[ColumnNames.OUTCOME] = outcome
                    curated[ColumnNames.EFO_ID] = efo_id
                    curated[ColumnNames.CHILD_TRAITS] = child_traits
                    curated[HarmonisedColumns.OUTCOME_DESC] = (
                        outcome_desc.get((outcome, efo_id), pd.NA)
                    )
                    curated[ColumnNames.SOURCE] = "curated"
                    curated[ColumnNames.SOURCE_DB] = "gwas_catalog"
                    harmonised = functions.harmonise_curated(curated)
                    is_overlap = pd.Series(
                        [
                            (outcome, accession) in overlap_studies
                            for accession in harmonised[
                                HarmonisedColumns.STUDY_ACCESSION
                            ]
                        ],
                        index=harmonised.index,
                        dtype=bool,
                    )
                    n_overlap_curated += int(is_overlap.sum())
                    harmonised = harmonised[~is_overlap]
                    for status, n in (
                        harmonised[HarmonisedColumns.MAF_STATUS]
                        .value_counts()
                        .items()
                    ):
                        maf_status_counts[status] += n
                    parts.append(harmonised)

        ensembl_id = ensembl_ids[gene]
        if ensembl_id in ("", Constants.NA_STRING):
            log_warn(f"{gene}: no Ensembl id, gene-burden skipped")
            burden_rows[gene] = 0
            continue
        burden = _expand_burden_outcomes(
            functions.gene_burden_evidence(ensembl_id, burden_disease_ids),
            burden_disease_ids,
            outcome_desc,
        )
        burden_rows[gene] = len(burden)
        if not burden.empty:
            burden[ColumnNames.GENE] = gene
            burden[ColumnNames.SOURCE] = "gene-burden"
            burden[ColumnNames.SOURCE_DB] = "open_targets"
            parts.append(
                functions.harmonise_frame(
                    burden, SourceColumnMaps.GENE_BURDEN, has_variants=False
                )
            )
    log_info(
        "curated MAF: "
        + " ".join(f"{k}={n}" for k, n in maf_status_counts.items())
    )
    log_info(
        f"curated: {n_overlap_curated} rows dropped from studies excluded "
        "for cohort overlap"
    )
    # plus the burden masks found in catalog sumstats files
    if not catalog_burden.empty:
        for gene, n in catalog_burden[ColumnNames.GENE].value_counts().items():
            burden_rows[gene] = burden_rows.get(gene, 0) + int(n)
    n_zero_genes = sum(1 for n in burden_rows.values() if n == 0)
    log_info(
        f"gene-burden rows: {_format_counts(burden_rows)} "
        f"({n_zero_genes} genes with 0)"
    )

    combined = pd.concat([p for p in parts if not p.empty], ignore_index=True)
    combined = _fill_ancestry(combined, _study_ancestry(audit))
    log_stage("normalise")
    sequences = functions.region_sequences(regions)
    combined = functions.normalise_variants(combined, sequences)
    log_stage("ensembl_check")
    combined = functions.annotate_ensembl_variants(
        combined, regions, sequences
    )
    combined = functions.flag_duplicate_variants(combined)
    log_info(
        f"duplicate variants flagged: "
        f"{int(combined[HarmonisedColumns.DUPLICATE_VARIANT].sum())} rows"
    )

    log_stage("write")
    Paths.RESULTS_OUTPUT.mkdir(parents=True, exist_ok=True)
    functions.write_table_atomic(combined, FileNames.MERGED_ASSOCIATIONS)
    log_info(f"wrote {len(combined)} rows to {FileNames.MERGED_ASSOCIATIONS}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    return argparse.ArgumentParser(
        description="Merge: summary-stats, curated, and gene-burden evidence."
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    return parser.parse_args()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    _parse_cmd_args(parser)

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.MERGE_ASSOCIATIONS):
        merge_results()


if __name__ == "__main__":
    main()
