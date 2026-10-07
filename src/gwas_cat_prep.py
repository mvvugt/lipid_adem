#!/usr/bin/env python3
"""
Resolves gene coordinates and outcome-to-EFO mappings (persisting any new
lookups back to data/raw/gene_list.txt and data/raw/icd_codes.txt),
discovers GWAS Catalog studies, curated FinnGen phenocodes, and curated
not-yet-API-indexed GWAS Catalog studies per outcome, and writes the
pyjasub job-array file (one row per study) that src/filter_gwas_cat.sh
consumes, with its study-outcome labels and gene regions, plus a
study-discovery audit log listing every discovered study across all
sources with its inclusion status and reason.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

import argparse
import gzip

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
    EffectScale,
    FileNames,
    Paths,
    RunlogOrder,
)


# Display-only per-study metadata columns in the study-discovery audit log,
# between `pubmed_id` and `note`.
META_COLUMNS: list[str] = [
    ColumnNames.PUB_DATE,
    ColumnNames.FIRST_AUTHOR,
    ColumnNames.JOURNAL,
    ColumnNames.TITLE,
    ColumnNames.TRAIT,
    ColumnNames.SAMPLE_SIZE,
    ColumnNames.ANCESTRY,
    ColumnNames.ANCESTRY_GROUP,
    ColumnNames.COHORT,
]
# GWAS-SSF metadata per study, after `META_COLUMNS`; filled for included
# studies only (`_add_scale_meta`)
SCALE_META_COLUMNS: list[str] = [
    ColumnNames.EFFECT_STATISTIC,
    ColumnNames.ANALYSIS_SOFTWARE,
    ColumnNames.EFFECT_SCALE_META,
]
FINNGEN_COHORT: str = "FinnGen R13"
FINNGEN_SOFTWARE: str = "REGENIE (Firth)"
# log_count key for EFO ids whose GWAS Catalog search found no studies
_NO_STUDIES_COUNT_KEY: str = "efo_no_studies"
# discovery query: efo_id, child_traits, excluded cohorts, review
# exclusions (accession, reason)
_QueryKey = tuple[str, bool, frozenset[str], frozenset[tuple[str, str]]]
# audit-log trait-query cells for rows not found by a trait search
_NO_TRAIT_QUERY: dict[str, str] = {
    ColumnNames.CHILD_TRAITS: "",
    ColumnNames.MAPPED_TRAIT_ID: "",
    ColumnNames.MAPPED_TRAIT: "",
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# helpers

def _is_searchable_efo_id(efo_id: str) -> bool:
    """Whether an outcome-table trait ID should be searched.

    Parameters
    ----------
    efo_id : `str`
        Cell from the `efo_id` column of the outcome table.

    Returns
    -------
    searchable : `bool`
        `False` for blank/`NA` cells and for `Constants.EXCLUDED_EFO_IDS`.
    """
    return (
        efo_id not in ("", Constants.NA_STRING)
        and efo_id not in Constants.EXCLUDED_EFO_IDS
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _log_discovery_summary(
    efo_id: str,
    child_traits: bool,
    cohorts: frozenset[str],
    classified: list[dict],
) -> None:
    """Record one summary line for an EFO id's study discovery.

    EFO ids with no studies at all are only counted (see
    `_NO_STUDIES_COUNT_KEY`), so RUN_LOG.md is not filled with
    zero lines.

    Parameters
    ----------
    efo_id : `str`
        EFO ID the studies were discovered for.
    child_traits : `bool`
        Whether child traits were included (cap applied per term).
    cohorts : `frozenset[str]`
        Preferred-cohort keys whose catalog studies were excluded.
    classified : `list[dict]`
        As returned by `functions.discover_studies_with_reasons`.

    Returns
    -------
    `None`
    """
    if not classified:
        log_count(_NO_STUDIES_COUNT_KEY)
        return
    reasons = [record["reason"] for record in classified]
    n_included = reasons.count("included")
    n_eligible = (
        n_included + reasons.count("over_cap") + reasons.count("over_total_cap")
    )
    scope = (
        "with child traits, cap per term and "
        f"{Constants.MAX_STUDIES_PER_CHILD_QUERY} total"
        if child_traits
        else "exact"
    )
    # the overlap check runs before the full-sumstats check (see
    # functions.classify_studies), so it is reported first
    overlap = ""
    blank = ""
    if cohorts:
        n_overlap = sum(
            reason.startswith(Constants.COHORT_OVERLAP_REASON_PREFIX)
            for reason in reasons
        )
        # a blank cohort cannot be checked for overlap, so it is kept
        n_blank = sum(
            record["reason"] == "included" and not record["cohort"]
            for record in classified
        )
        overlap = (
            f" -> {n_overlap} dropped for cohort overlap "
            f"({', '.join(sorted(cohorts))})"
        )
        blank = f", {n_blank} included with blank cohort"
    n_review = sum(
        reason.startswith(Constants.REVIEW_REASON_PREFIX) for reason in reasons
    )
    review = f" -> {n_review} dropped by review" if n_review else ""
    log_info(
        f"{efo_id} ({scope}): {len(classified)} studies{overlap}{review} -> "
        f"{n_eligible} with full sumstats -> {n_included} included{blank}"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _covered_cohorts(
    icd_df: pd.DataFrame,
    studies_by_phenocode: dict[str, list[str]],
    marvel_df: pd.DataFrame,
    review: dict[str, dict[str, str]],
) -> dict[str, frozenset[str]]:
    """Find the preferred cohorts excluded from each outcome's catalog
    studies.

    Parameters
    ----------
    icd_df : `pd.DataFrame`
        The outcome table (`functions.load_icd_table`).
    studies_by_phenocode : `dict[str, list[str]]`
        Curated FinnGen phenocode -> `[phenocode]` if in the manifest,
        else `[]` (`functions.finngen_studies_for_phenocode`).
    marvel_df : `pd.DataFrame`
        From `functions.load_marvel_table`.
    review : `dict[str, dict[str, str]]`
        From `functions.load_study_outcome_review`; a phenocode excluded
        there for an outcome does not count as own FinnGen results.

    Returns
    -------
    covered : `dict[str, frozenset[str]]`
        Outcome -> `Constants.PREFERRED_COHORT_ALIASES` keys:
        `Constants.ALWAYS_EXCLUDED_COHORTS`, ``finngen`` when any of its
        non-excluded phenocodes is in the manifest, plus each marvel
        `cohort` listed for it. Every outcome in `icd_df` is a key.
    """
    # own results only; ALWAYS_EXCLUDED_COHORTS are added on return
    covered: dict[str, set[str]] = {
        outcome: set() for outcome in icd_df[ColumnNames.OUTCOME]
    }
    for outcome, cell in zip(
        icd_df[ColumnNames.OUTCOME], icd_df[ColumnNames.FINNGEN_PHENOCODE]
    ):
        if any(
            studies_by_phenocode[phenocode]
            and phenocode not in review.get(outcome, {})
            for phenocode in functions.finngen_phenocodes_in_cell(cell)
        ):
            covered[outcome].add("finngen")
    for outcome, cohort in zip(marvel_df["outcome"], marvel_df["cohort"]):
        if outcome not in covered:
            log_warn(
                f"{FileNames.MARVEL_RESULTS}: outcome {outcome!r} not in "
                f"{FileNames.ICD_CODE_LIST}, ignored"
            )
            continue
        covered[outcome].add(cohort)
    always = sorted(Constants.ALWAYS_EXCLUDED_COHORTS)
    log_info(
        f"catalog studies with {', '.join(always)} excluded for every outcome"
    )
    for outcome, cohorts in sorted(covered.items()):
        if cohorts:
            log_info(
                f"{outcome}: own results for {', '.join(sorted(cohorts))}; "
                "catalog studies with these cohorts excluded"
            )
    return {
        outcome: frozenset(cohorts | Constants.ALWAYS_EXCLUDED_COHORTS)
        for outcome, cohorts in covered.items()
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def _manual_meta(
    manual_row: pd.Series, pubmed: dict[int, dict]
) -> dict[str, str]:
    """Build audit metadata for a curated (manual) GWAS Catalog study.

    Values curated in the manual table win; blanks in the publication
    columns are filled from PubMed.

    Parameters
    ----------
    manual_row : `pd.Series`
        One row of `functions.load_manual_gwas_catalog_studies()`.
    pubmed : `dict[int, dict]`
        As returned by `functions.pubmed_summaries`.

    Returns
    -------
    meta : `dict[str, str]`
        One value per column in `META_COLUMNS`.
    """
    pid = str(manual_row.get(ColumnNames.PUBMED_ID, ""))
    summary = pubmed.get(int(pid), {}) if pid.isdigit() else {}
    date = summary.get("date")
    fetched = {
        ColumnNames.PUB_DATE: (
            date.strftime("%Y-%m-%d") if date is not None else ""
        ),
        ColumnNames.FIRST_AUTHOR: summary.get("first_author", ""),
        ColumnNames.JOURNAL: summary.get("journal", ""),
        ColumnNames.TITLE: summary.get("title", ""),
    }
    curated = {
        col: functions.clean_cell(manual_row.get(col, ""))
        for col in META_COLUMNS
        if col not in (ColumnNames.TRAIT, ColumnNames.ANCESTRY_GROUP)
    }
    curated[ColumnNames.TRAIT] = functions.clean_cell(
        manual_row.get(ColumnNames.DISEASE_TRAIT, "")
    )
    # free text or an Ancestry code; NR when blank
    curated[ColumnNames.ANCESTRY_GROUP] = functions.harmonise_ancestry(
        curated[ColumnNames.ANCESTRY]
    )
    return {
        col: curated.get(col) or fetched.get(col, "") for col in META_COLUMNS
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _finngen_meta(
    phenocode: str, manifest_df: pd.DataFrame
) -> dict[str, str]:
    """Build audit metadata for a FinnGen phenocode from the manifest.

    Parameters
    ----------
    phenocode : `str`
        Curated FinnGen phenocode (e.g. "G6_ALZHEIMER").
    manifest_df : `pd.DataFrame`
        Manifest table from `functions.load_finngen_manifest`.

    Returns
    -------
    meta : `dict[str, str]`
        One value per column in `META_COLUMNS`; `ancestry_group` is
        always `Ancestry.FINNGEN`, the rest `""` if `phenocode` is not in
        the manifest.
    """
    meta = {col: "" for col in META_COLUMNS}
    meta[ColumnNames.ANCESTRY_GROUP] = Ancestry.FINNGEN
    matches = manifest_df.loc[manifest_df["phenocode"] == phenocode]
    if matches.empty:
        return meta
    row = matches.iloc[0]
    meta[ColumnNames.TRAIT] = functions.clean_cell(row.get("phenotype", ""))
    meta[ColumnNames.SAMPLE_SIZE] = (
        f"{row.get('num_cases', '')} cases, "
        f"{row.get('num_controls', '')} controls"
    )
    meta[ColumnNames.COHORT] = FINNGEN_COHORT
    return meta


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _add_scale_meta(audit_rows: list[dict[str, str]]) -> None:
    """Fill `SCALE_META_COLUMNS` in place on every audit row.

    Included GWAS Catalog and manual studies get their GWAS-SSF metadata
    (`functions.study_meta_yaml`, fetched once per accession); FinnGen
    rows get `Constants.FINNGEN_EFFECT_SCALE`. Other rows are left blank
    (scale `EffectScale.UNKNOWN`), which saves the requests for studies
    that are not analysed.

    Parameters
    ----------
    audit_rows : `list[dict[str, str]]`
        Study-discovery rows with `source`, `study_accession` and
        `status` set.

    Returns
    -------
    `None`
    """
    blank = {
        ColumnNames.EFFECT_STATISTIC: "",
        ColumnNames.ANALYSIS_SOFTWARE: "",
        ColumnNames.EFFECT_SCALE_META: EffectScale.UNKNOWN,
    }
    finngen = {
        **blank,
        ColumnNames.ANALYSIS_SOFTWARE: FINNGEN_SOFTWARE,
        ColumnNames.EFFECT_SCALE_META: Constants.FINNGEN_EFFECT_SCALE,
    }
    fetched: dict[str, dict[str, str]] = {}
    for row in audit_rows:
        accession = row[ColumnNames.STUDY_ACCESSION]
        source = row[ColumnNames.SOURCE]
        if source == "finngen":
            row.update(finngen)
        elif (
            source in ("gwas_catalog", "manual")
            and row[ColumnNames.STATUS] == "included"
        ):
            if accession not in fetched:
                fetched[accession] = functions.study_meta_yaml(accession)
            row.update(fetched[accession])
        else:
            row.update(blank)
    counts: dict[str, int] = {}
    for meta in fetched.values():
        scale = meta[ColumnNames.EFFECT_SCALE_META]
        counts[scale] = counts.get(scale, 0) + 1
    log_info(
        f"metadata yaml read for {len(fetched)} included studies, scale: "
        + ", ".join(f"{k}={n}" for k, n in sorted(counts.items()))
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def build_tasks() -> None:
    """Resolve lookups, discover studies, and write the job-array file.

    Loads `FileNames.GENE_LIST`/`ICD_CODE_LIST`, fills in any missing gene
    columns/cells (symbol, coordinates, Ensembl ID, UniProt; see
    `functions.resolve_gene_table`) and outcome/code-to-EFO mappings
    (persisting the results
    back to those files so reruns skip already-resolved rows; obsolete
    trait IDs are replaced by their current term on every run), discovers
    GWAS Catalog studies per outcome (grouped by the distinct EFO IDs
    under that outcome; child traits included, with the cap per mapped
    term, for `Constants.CHILD_TRAIT_OUTCOMES`), unions in any curated
    not-yet-API-indexed GWAS Catalog accessions for that outcome (see
    data/raw/gwas_catalog_manual_studies.SOURCE.md), validates each
    outcome's curated FinnGen phenocode (if set) against the vendored
    manifest, and writes three tables:

    - `FileNames.TASKS_FILE`: the pyjasub job array, one row per study
      (all genes are filtered in one pass), columns: rowidx,
      study_accession, source, outfile.
    - `FileNames.STUDY_OUTCOMES_FILE`: one row per study x outcome,
      columns: study_accession, source, outcome, efo_id, outfile; used
      by `merge_associations.py` to label each outfile per outcome.
    - `FileNames.GENE_REGIONS_FILE`: the flanked region per gene,
      columns: gene, chrom, start, end; read by the filter tasks.

    Catalog studies listing UKB or AoU (`Constants.ALWAYS_EXCLUDED_COHORTS`)
    or a cohort the outcome has own results for (FinnGen phenocode, or a
    `FileNames.MARVEL_RESULTS` row; see `_covered_cohorts`) are excluded
    for that outcome before the cap, as are the outcome x study rows
    marked ``exclude`` in `FileNames.STUDY_OUTCOME_REVIEW` (reason
    ``review_<reason>``; also applied to manual and FinnGen studies).
    One paper's analyses of one trait share a cap slot
    (`functions.classify_studies`). Curated manual accessions get
    `source` ``manual``.

    Trait IDs in `Constants.EXCLUDED_EFO_IDS` are not searched. Then
    archives any existing pyjasub log dir (`Paths.FILTER_TASK_LOGS`) via
    `functions.archive_dir`, since pyjasub refuses a newer array file.

    Also writes `FileNames.STUDY_DISCOVERY_LOG`, an audit trail of every
    study discovered across all three sources (GWAS Catalog, FinnGen,
    manual), one row each, with its inclusion status and reason (e.g.
    "no_full_sumstats", "over_cap", "over_total_cap",
    "gxe_interaction", "gxg_interaction", "cnv_study",
    "x_chromosome_study", "cohort_overlap_<cohort>",
    "not_found_in_manifest") -- unlike
    `TASKS_FILE`, which only contains the surviving, capped set. Each
    row also carries display-only metadata (`META_COLUMNS`): publication
    date/first author/journal/title from PubMed, and trait, sample size,
    ancestry and cohort from the GWAS Catalog record, the manual table,
    or the FinnGen manifest, so the recency cap can be checked by eye --
    plus `ancestry_group` (`functions.harmonise_ancestry`; FinnGen is
    `Ancestry.FINNGEN`), which `merge_associations.py` carries into the
    merged associations, and the GWAS-SSF effect-scale metadata
    (`SCALE_META_COLUMNS`, included studies only, see `_add_scale_meta`).

    Returns
    -------
    `None`

    Raises
    ------
    FileNotFoundError
        If the gene or ICD/outcome placeholder files have not been filled
        in.
    functions.GeneTableError
        If a gene row cannot be resolved, or its identifiers disagree.
    """
    genes_df = functions.load_gene_table(FileNames.GENE_LIST)
    icd_df = functions.load_icd_table(FileNames.ICD_CODE_LIST)
    log_info(f"{len(genes_df)} genes, {len(icd_df)} icd codes")

    log_stage("resolve_genes")
    genes_before = genes_df.copy()
    genes_df = functions.resolve_gene_table(genes_df)
    if not genes_df.equals(genes_before):
        functions.write_table_atomic(genes_df, FileNames.GENE_LIST)
        log_info(f"wrote resolved gene annotations to {FileNames.GENE_LIST}")

    log_stage("resolve_efo")
    icd_before = icd_df.copy()
    icd_df = functions.resolve_efo_ids(icd_df)
    icd_df = functions.replace_obsolete_trait_ids(icd_df)
    if not icd_df.equals(icd_before):
        functions.write_table_atomic(icd_df, FileNames.ICD_CODE_LIST, sep="\t")
        log_info(f"wrote resolved efo_ids to {FileNames.ICD_CODE_LIST}")
    # after the write-back, so overrides live in code only
    icd_df = functions.apply_outcome_efo_overrides(icd_df)

    Paths.DATA_TEMP.mkdir(parents=True, exist_ok=True)
    Paths.GWAS_FILTERED.mkdir(parents=True, exist_ok=True)

    for efo_id, outcome in sorted(
        {
            (efo_id, outcome)
            for efo_id, outcome in zip(
                icd_df[ColumnNames.EFO_ID], icd_df[ColumnNames.OUTCOME]
            )
            if efo_id in Constants.EXCLUDED_EFO_IDS
        }
    ):
        log_info(f"{efo_id} ({outcome}) in Constants.EXCLUDED_EFO_IDS, skipped")
    # FinnGen is keyed by curated phenocode(s) instead of a live-discovered
    # EFO ID. A cell may list more than one phenocode (comma-separated)
    # when an outcome is curated against several definitional variants of
    # the same disease. Resolved before the GWAS Catalog search, since
    # the cohorts with own results decide which catalog studies are kept.
    log_stage("finngen_manual")
    finngen_manifest_df = functions.load_finngen_manifest()
    manual_studies_df = functions.load_manual_gwas_catalog_studies()
    # One batched PubMed lookup for all curated studies (their GWAS
    # Catalog records 404 until indexed, so PubMed is all we can fetch).
    manual_pubmed = functions.pubmed_summaries(
        manual_studies_df[ColumnNames.PUBMED_ID].tolist()
    )
    distinct_phenocodes = sorted(
        {
            phenocode
            for cell in icd_df[ColumnNames.FINNGEN_PHENOCODE]
            for phenocode in functions.finngen_phenocodes_in_cell(cell)
        }
    )
    studies_by_phenocode = {
        phenocode: functions.finngen_studies_for_phenocode(
            phenocode, finngen_manifest_df
        )
        for phenocode in distinct_phenocodes
    }
    review = functions.load_study_outcome_review()
    covered = _covered_cohorts(
        icd_df, studies_by_phenocode, functions.load_marvel_table(), review
    )

    def _query_key(efo_id: str, outcome: str) -> _QueryKey:
        """Return the discovery query key of an outcome's EFO ID."""
        return (
            efo_id,
            functions.includes_child_traits(outcome),
            covered[outcome],
            frozenset(review.get(outcome, {}).items()),
        )

    # Classify studies once per distinct (efo_id, child_traits, excluded
    # cohorts, review exclusions) key (global dedupe), then union each
    # outcome's accessions from its own distinct efo_ids. These are set
    # per outcome, so the same ID can be classified more than once; the
    # GWAS Catalog is still queried once per (efo_id, child_traits).
    distinct_queries = sorted(
        {
            _query_key(efo_id, outcome)
            for efo_id, outcome in zip(
                icd_df[ColumnNames.EFO_ID], icd_df[ColumnNames.OUTCOME]
            )
            if _is_searchable_efo_id(efo_id)
        },
        key=lambda query: (
            query[0], query[1], sorted(query[2]), sorted(query[3])
        ),
    )
    log_stage("discover_gwas")
    records_by_search: dict[tuple[str, bool], list[dict]] = {}
    classified_by_query: dict[_QueryKey, list[dict]] = {}
    for query in distinct_queries:
        efo_id, child_traits, cohorts, exclusions = query
        if (efo_id, child_traits) not in records_by_search:
            records_by_search[(efo_id, child_traits)] = (
                functions.fetch_gwas_catalog_study_records(
                    efo_id, child_traits
                )
            )
        classified = functions.discover_studies_with_reasons(
            efo_id,
            include_child_traits=child_traits,
            excluded_cohorts=cohorts,
            excluded_accessions=dict(exclusions),
            records=records_by_search[(efo_id, child_traits)],
        )
        classified_by_query[query] = classified
        _log_discovery_summary(efo_id, child_traits, cohorts, classified)
    log_count_summary(
        _NO_STUDIES_COUNT_KEY, label="EFO ids with 0 GWAS Catalog studies"
    )

    study_outcome_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    for outcome, group in icd_df.groupby(ColumnNames.OUTCOME):
        outcome_efo_ids = sorted(
            {e for e in group[ColumnNames.EFO_ID] if _is_searchable_efo_id(e)}
        )
        child_traits = functions.includes_child_traits(outcome)
        accession_to_efo: dict[str, str] = {}
        for efo_id in outcome_efo_ids:
            query = _query_key(efo_id, outcome)
            for record in classified_by_query[query]:
                status = (
                    "included"
                    if record["reason"] == "included"
                    else "excluded"
                )
                audit_rows.append(
                    {
                        ColumnNames.OUTCOME: outcome,
                        ColumnNames.SOURCE: "gwas_catalog",
                        ColumnNames.STUDY_ACCESSION: record["accession_id"],
                        ColumnNames.EFO_ID: efo_id,
                        ColumnNames.CHILD_TRAITS: str(child_traits),
                        ColumnNames.MAPPED_TRAIT_ID: record["mapped_trait_id"],
                        ColumnNames.MAPPED_TRAIT: record["mapped_trait"],
                        ColumnNames.STATUS: status,
                        ColumnNames.REASON: record["reason"],
                        ColumnNames.PUBMED_ID: str(
                            record.get("pubmed_id") or ""
                        ),
                        **{col: record[col] for col in META_COLUMNS},
                        ColumnNames.NOTE: "",
                    }
                )
                if record["reason"] == "included":
                    accession_to_efo.setdefault(
                        record["accession_id"], efo_id
                    )

        # Curated accessions deposited on the FTP server but not yet
        # searchable via the API; source "manual" so the meta-analysis
        # can prefer them (Constants.SOURCE_DB_PREFERENCE)
        outcome_review = review.get(outcome, {})
        manual_accessions = [
            accession
            for accession in functions.manual_studies_for_outcome(
                outcome, manual_studies_df
            )
            if accession not in accession_to_efo
            and accession not in outcome_review
        ]

        outcome_manual_rows = manual_studies_df.loc[
            manual_studies_df[ColumnNames.OUTCOME] == outcome
        ]
        for _, manual_row in outcome_manual_rows.iterrows():
            manual_reason = outcome_review.get(
                manual_row["accession_id"], "included"
            )
            audit_rows.append(
                {
                    ColumnNames.OUTCOME: outcome,
                    ColumnNames.SOURCE: "manual",
                    ColumnNames.STUDY_ACCESSION: manual_row["accession_id"],
                    ColumnNames.EFO_ID: "",
                    **_NO_TRAIT_QUERY,
                    ColumnNames.STATUS: (
                        "included"
                        if manual_reason == "included"
                        else "excluded"
                    ),
                    ColumnNames.REASON: manual_reason,
                    ColumnNames.PUBMED_ID: str(
                        manual_row.get(ColumnNames.PUBMED_ID, "")
                    ),
                    **_manual_meta(manual_row, manual_pubmed),
                    ColumnNames.NOTE: functions.clean_cell(
                        manual_row.get(ColumnNames.NOTE, "")
                    ),
                }
            )

        outcome_phenocodes = sorted(
            {
                phenocode
                for cell in group[ColumnNames.FINNGEN_PHENOCODE]
                for phenocode in functions.finngen_phenocodes_in_cell(cell)
            }
        )
        finngen_accessions: list[str] = []
        for phenocode in outcome_phenocodes:
            found = studies_by_phenocode[phenocode]
            if not found:
                finngen_reason = "not_found_in_manifest"
            else:
                finngen_reason = outcome_review.get(phenocode, "included")
            if finngen_reason == "included":
                finngen_accessions.extend(found)
            audit_rows.append(
                {
                    ColumnNames.OUTCOME: outcome,
                    ColumnNames.SOURCE: "finngen",
                    ColumnNames.STUDY_ACCESSION: phenocode,
                    ColumnNames.EFO_ID: "",
                    **_NO_TRAIT_QUERY,
                    ColumnNames.STATUS: (
                        "included"
                        if finngen_reason == "included"
                        else "excluded"
                    ),
                    ColumnNames.REASON: finngen_reason,
                    ColumnNames.PUBMED_ID: "",
                    **_finngen_meta(phenocode, finngen_manifest_df),
                    ColumnNames.NOTE: "",
                }
            )

        study_sources = (
            [
                (accession, efo_id, "gwas_catalog")
                for accession, efo_id in accession_to_efo.items()
            ]
            + [(accession, "", "manual") for accession in manual_accessions]
            + [(accession, "", "finngen") for accession in finngen_accessions]
        )
        for accession, efo_id, source in study_sources:
            outfile = Paths.GWAS_FILTERED / f"{accession}_result.tsv.gz"
            study_outcome_rows.append(
                {
                    ColumnNames.STUDY_ACCESSION: accession,
                    ColumnNames.SOURCE: source,
                    ColumnNames.OUTCOME: outcome,
                    ColumnNames.EFO_ID: efo_id,
                    ColumnNames.OUTFILE: str(outfile),
                }
            )

    log_stage("write_tasks")
    # One filter task per study (all genes in one pass); a study found
    # under several outcomes is filtered once and labelled per outcome
    # from STUDY_OUTCOMES_FILE at merge time.
    study_outcomes_df = pd.DataFrame(
        study_outcome_rows,
        columns=[
            ColumnNames.STUDY_ACCESSION,
            ColumnNames.SOURCE,
            ColumnNames.OUTCOME,
            ColumnNames.EFO_ID,
            ColumnNames.OUTFILE,
        ],
    )
    tasks_df = study_outcomes_df.drop_duplicates(subset=[ColumnNames.OUTFILE])[
        [ColumnNames.STUDY_ACCESSION, ColumnNames.SOURCE, ColumnNames.OUTFILE]
    ]
    tasks_df.insert(0, ColumnNames.ROWIDX, range(1, len(tasks_df) + 1))
    region_rows: list[dict[str, str | int]] = []
    for _, gene_row in genes_df.iterrows():
        region = functions.gene_row_region(
            gene_row, Constants.GENE_COORD_FLANK_BP
        )
        region_rows.append(
            {
                ColumnNames.GENE: gene_row[ColumnNames.GENE],
                ColumnNames.CHROM: region.chrom,
                ColumnNames.START: region.start,
                ColumnNames.END: region.end,
            }
        )
    regions_df = pd.DataFrame(
        region_rows,
        columns=[
            ColumnNames.GENE,
            ColumnNames.CHROM,
            ColumnNames.START,
            ColumnNames.END,
        ],
    )
    functions.write_table_atomic(regions_df, FileNames.GENE_REGIONS_FILE)
    functions.write_table_atomic(
        study_outcomes_df, FileNames.STUDY_OUTCOMES_FILE
    )
    functions.write_table_atomic(tasks_df, FileNames.TASKS_FILE)

    log_info(
        f"wrote {len(tasks_df)} tasks ({len(study_outcomes_df)} study x "
        f"outcome rows, {len(regions_df)} gene regions) to "
        f"{FileNames.TASKS_FILE}"
    )

    # pyjasub errors if the job-array file is newer than an existing log dir
    functions.archive_dir(Paths.FILTER_TASK_LOGS)

    log_stage("scale_meta")
    _add_scale_meta(audit_rows)
    audit_header = [
        ColumnNames.OUTCOME,
        ColumnNames.SOURCE,
        ColumnNames.STUDY_ACCESSION,
        ColumnNames.EFO_ID,
        ColumnNames.CHILD_TRAITS,
        ColumnNames.MAPPED_TRAIT_ID,
        ColumnNames.MAPPED_TRAIT,
        ColumnNames.STATUS,
        ColumnNames.REASON,
        ColumnNames.PUBMED_ID,
        *META_COLUMNS,
        *SCALE_META_COLUMNS,
        ColumnNames.NOTE,
    ]
    audit_tmp = FileNames.STUDY_DISCOVERY_LOG.with_suffix(".tmp")
    with gzip.open(audit_tmp, "wt") as handle:
        handle.write("\t".join(audit_header) + "\n")
        for row in audit_rows:
            handle.write(
                "\t".join(str(row[col]) for col in audit_header) + "\n"
            )
    audit_tmp.replace(FileNames.STUDY_DISCOVERY_LOG)

    log_info(
        f"wrote {len(audit_rows)} study-discovery rows to "
        f"{FileNames.STUDY_DISCOVERY_LOG}"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    return argparse.ArgumentParser(
        description=(
            "Resolve gene/outcome lookups, discover studies, write the "
            "job-array file."
        )
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

    with runlog_setup(root=Paths.HERE, order=RunlogOrder.GWAS_CAT_PREP):
        build_tasks()


if __name__ == "__main__":
    main()
