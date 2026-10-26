#!/usr/bin/env python3
"""combine_variants

Combine the PTVs, the ClinVar P/LP, and the GoF and AlphaMissense P/LP
variants of the old per-gene lists (`data/raw/gof_variants.tsv`,
`data/raw/am_variants.tsv`) into one variant list, left-aligned and
trimmed against GRCh38, and split per gene. Original and normalised variant ID
(chr:pos:alleles) are kept.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS

from __future__ import annotations

from pathlib import Path

import pandas as pd

import functions
from log_tools.emitter import log_info, log_warn
from log_tools.setup import runlog_setup
from project_constants import (
    ClinVarColumnNames,
    ClinVarDirection,
    ColumnNames,
    ConditionDirectionColumns,
    Constants,
    FileNames,
    Paths,
    VariantListColumns,
    VepCsqColumns,
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS

# helper column of `load_plp_variants`, dropped before returning
_CONSEQUENCE_KEY: str = "_consequence"
# columns of the combined list, in output order (the columns of the old
# per-gene lists, plus `clinvar_direction` and the normalisation columns)
LIST_COLUMNS: list[str] = [
    VariantListColumns.VARIANT_ID, VariantListColumns.CHROM,
    VariantListColumns.POS, VariantListColumns.A1, VariantListColumns.A2,
    VariantListColumns.SOURCE, VariantListColumns.GENE,
    VariantListColumns.AM_PATHOGENICITY, VariantListColumns.TRI_CLASS,
    VariantListColumns.CLINVAR_DIRECTION, VariantListColumns.POS_ORIG,
    VariantListColumns.A1_ORIG, VariantListColumns.A2_ORIG,
    VariantListColumns.NORM_STATUS,
]
# columns of the per-gene marvel extraction lists
MARVEL_COLUMNS: list[str] = [
    VariantListColumns.MARVEL_ID, VariantListColumns.CHROM,
    VariantListColumns.POS, VariantListColumns.A1, VariantListColumns.A2,
    VariantListColumns.GENE,
]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _collapse_direction(directions: pd.Series) -> str:
    """Combine the condition directions of one variant into one value.

    Parameters
    ----------
    directions : `pd.Series`
        `ClinVarDirection` values of the variant's conditions.

    Returns
    -------
    direction : `str`
        `lowering`, `raising` or `altered` when only that one occurs among
        the known directions, `conflicting` when more than one occurs,
        else `unknown`.
    """
    known = set(directions) & {
        ClinVarDirection.LOWERING,
        ClinVarDirection.RAISING,
        ClinVarDirection.ALTERED,
    }
    if len(known) > 1:
        return ClinVarDirection.CONFLICTING
    if len(known) == 1:
        return known.pop()
    return ClinVarDirection.UNKNOWN


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_plp_variants() -> pd.DataFrame:
    """Read the ClinVar P/LP list as variant-list rows with a direction.

    The GRCh38 coordinates are used (`Constants.PLP_ASSEMBLY_SUFFIX`).
    Each row's condition gets its direction from
    `FileNames.CLINVAR_CONDITION_DIRECTION`; conditions missing there are
    `unknown` (warned). The directions are combined per variant by
    `_collapse_direction`, except that a variant with a consequence in
    `Constants.TRUNCATING_CONSEQUENCES` is always `lowering` (less gene
    product, whatever the conditions say).

    Returns
    -------
    plp : `pd.DataFrame`
        One row per variant, with the `VariantListColumns` `chr`, `pos`,
        `a1` (reference), `a2` (alternate), `source`
        (`Constants.CLINVAR_VARIANT_SOURCE`), `gene` and
        `clinvar_direction`, as strings.

    Raises
    ------
    FileNotFoundError
        If the P/LP list or the condition-direction table does not exist.
    """
    for path in (FileNames.PLP_VARIANTS, FileNames.CLINVAR_CONDITION_DIRECTION):
        if not path.exists():
            raise FileNotFoundError(f"{path} not found")
    cv = ClinVarColumnNames
    cd = ConditionDirectionColumns
    vc = VariantListColumns
    suffix = Constants.PLP_ASSEMBLY_SUFFIX
    plp = pd.read_csv(FileNames.PLP_VARIANTS, sep="\t", dtype=str)
    directions = pd.read_csv(
        FileNames.CLINVAR_CONDITION_DIRECTION, sep="\t", dtype=str
    )
    log_info(
        f"{FileNames.PLP_VARIANTS}: {len(plp)} rows; "
        f"{FileNames.CLINVAR_CONDITION_DIRECTION}: {len(directions)} rows"
    )

    variants = pd.DataFrame(
        {
            vc.CHROM: pd.to_numeric(
                plp[f"{cv.CHR_COL}{suffix}"], errors="coerce"
            ).astype("Int64"),
            vc.POS: pd.to_numeric(
                plp[f"{cv.POSITION_VCF_COL}{suffix}"], errors="coerce"
            ).astype("Int64"),
            vc.A1: plp[f"{cv.REFERENCE_ALLELE_COL}{suffix}"],
            vc.A2: plp[f"{cv.ALTERNATE_ALLELE_COL}{suffix}"],
            vc.SOURCE: Constants.CLINVAR_VARIANT_SOURCE,
            vc.GENE: plp[cv.GENE_SYMBOL_COL],
            cd.CONDITION: plp[cv.RCV_CONDITION_COL],
            _CONSEQUENCE_KEY: plp[cv.RCV_MOLECULAR_CONSEQUENCE_COL],
        }
    )
    variants[vc.CHROM] = variants[vc.CHROM].astype("string")
    variants[vc.POS] = variants[vc.POS].astype("string")
    # reference records (e.g. APOE3 isoform "c.388=") are not variants
    is_ref = variants[vc.A1].notna() & (variants[vc.A1] == variants[vc.A2])
    log_info(f"{int(is_ref.sum())} P/LP rows with ref = alt dropped")
    variants = variants.loc[~is_ref].merge(
        directions.rename(columns={cd.GENE: vc.GENE}),
        on=[vc.GENE, cd.CONDITION],
        how="left",
    )
    missing = variants.loc[
        variants[cd.DIRECTION].isna(), [vc.GENE, cd.CONDITION]
    ].drop_duplicates()
    for gene, condition in missing.itertuples(index=False):
        log_warn(
            f"{gene} condition '{condition}' not in "
            f"{FileNames.CLINVAR_CONDITION_DIRECTION}: counted as unknown"
        )
    variants[cd.DIRECTION] = variants[cd.DIRECTION].fillna(
        ClinVarDirection.UNKNOWN
    )

    site = [vc.CHROM, vc.POS, vc.A1, vc.A2, vc.SOURCE, vc.GENE]
    collapsed = (
        variants.groupby(site, dropna=False, sort=True)[cd.DIRECTION]
        .agg(_collapse_direction)
        .rename(vc.CLINVAR_DIRECTION)
        .reset_index()
    )
    truncating = (
        variants[_CONSEQUENCE_KEY]
        .isin(Constants.TRUNCATING_CONSEQUENCES)
        .groupby([variants[col] for col in site], dropna=False, sort=True)
        .any()
        .to_numpy()
    )
    overruled = truncating & (
        collapsed[vc.CLINVAR_DIRECTION] != ClinVarDirection.LOWERING
    )
    log_info(
        f"{int(truncating.sum())} truncating P/LP variants set to "
        f"{ClinVarDirection.LOWERING}, {int(overruled.sum())} of them "
        "against their conditions"
    )
    collapsed.loc[truncating, vc.CLINVAR_DIRECTION] = ClinVarDirection.LOWERING
    counts = collapsed.groupby(
        [vc.GENE, vc.CLINVAR_DIRECTION], sort=True
    ).size()
    for (gene, direction), n in counts.items():
        log_info(f"{gene} ClinVar P/LP: {n} variants {direction}")
    return collapsed


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_ptv_variants(path: Path = FileNames.PTV_VARIANTS) -> pd.DataFrame:
    """Read the PTV list as variant-list rows.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.PTV_VARIANTS`
        The `annotate_ptv.py` output.

    Returns
    -------
    ptv : `pd.DataFrame`
        One row per site, with the `VariantListColumns` `chr`, `pos`, `a1`
        (reference), `a2` (alternate), `source`
        (`Constants.PTV_VARIANT_SOURCE`) and `gene`, as strings. The AF/AC
        columns are not carried over.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist (run annotate_ptv.py first).
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found: run annotate_ptv.py first")
    vc = VariantListColumns
    pc = VepCsqColumns
    ptv = pd.read_csv(path, sep="\t", dtype=str)
    log_info(f"{path}: {len(ptv)} PTVs")
    return pd.DataFrame(
        {
            vc.CHROM: ptv[pc.CHROM],
            vc.POS: ptv[pc.POS],
            vc.A1: ptv[pc.REF],
            vc.A2: ptv[pc.ALT],
            vc.SOURCE: Constants.PTV_VARIANT_SOURCE,
            vc.GENE: ptv[pc.GENE],
        }
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_gof_variants(path: Path = FileNames.GOF_VARIANTS) -> pd.DataFrame:
    """Read the GoF list as variant-list rows.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.GOF_VARIANTS`
        The GoF rows of the old per-gene lists (`chr`, `pos`, `a1`, `a2`,
        `source`, `gene`, ...).

    Returns
    -------
    gof : `pd.DataFrame`
        The rows with `source` `Constants.GOF_VARIANT_SOURCE`, with the
        `VariantListColumns` `chr`, `pos`, `a1`, `a2`, `source` and `gene`,
        as strings.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    ValueError
        If `path` has rows of another source.
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found (see its SOURCE.md)")
    vc = VariantListColumns
    gof = pd.read_csv(path, sep="\t", dtype=str)
    other = sorted(set(gof[vc.SOURCE]) - {Constants.GOF_VARIANT_SOURCE})
    if other:
        raise ValueError(f"{path}: sources other than GoF: {other}")
    log_info(f"{path}: {len(gof)} GoF variants")
    return gof[[vc.CHROM, vc.POS, vc.A1, vc.A2, vc.SOURCE, vc.GENE]]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_am_variants(path: Path = FileNames.AM_VARIANTS) -> pd.DataFrame:
    """Read the AlphaMissense list as variant-list rows of the kept classes.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.AM_VARIANTS`
        The AM rows of the old per-gene lists (`chr`, `pos`, `a1`, `a2`,
        `source`, `gene`, `am_pathogenicity`, `tri_class`).

    Returns
    -------
    am : `pd.DataFrame`
        The rows with `source` `Constants.AM_VARIANT_SOURCE` and a
        `tri_class` in `Constants.AM_KEEP_CLASSES`, with the
        `VariantListColumns` `chr`, `pos`, `a1`, `a2`, `source`, `gene`,
        `am_pathogenicity` and `tri_class`, as strings. Rows per class
        are logged.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    ValueError
        If `path` has rows of another source.
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found (see its SOURCE.md)")
    vc = VariantListColumns
    am = pd.read_csv(path, sep="\t", dtype=str)
    other = sorted(set(am[vc.SOURCE]) - {Constants.AM_VARIANT_SOURCE})
    if other:
        raise ValueError(f"{path}: sources other than AM: {other}")
    for tri_class, n in am[vc.TRI_CLASS].value_counts(dropna=False).items():
        log_info(f"{path}: {n} AM variants of class {tri_class}")
    am = am.loc[am[vc.TRI_CLASS].isin(Constants.AM_KEEP_CLASSES)]
    log_info(
        f"{path}: {len(am)} AM variants kept "
        f"({', '.join(Constants.AM_KEEP_CLASSES)})"
    )
    return am[[
        vc.CHROM, vc.POS, vc.A1, vc.A2, vc.SOURCE, vc.GENE,
        vc.AM_PATHOGENICITY, vc.TRI_CLASS,
    ]]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_gene_regions(
    path: Path = FileNames.GENE_LIST,
) -> dict[str, functions.GeneRegion]:
    """Read the gene regions of the gene list, flanked.

    Parameters
    ----------
    path : `Path`, optional, default: `FileNames.GENE_LIST`
        Gene list with `gene`, `chr`, `start` and `end` columns.

    Returns
    -------
    regions : `dict[str, functions.GeneRegion]`
        Gene -> region, `Constants.GENE_COORD_FLANK_BP` added on both
        sides; chrom without a "chr" prefix.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"gene list not found: {path}")
    cn = ColumnNames
    flank = Constants.GENE_COORD_FLANK_BP
    genes = pd.read_csv(path, sep="\t", dtype=str)
    return {
        gene: functions.GeneRegion(
            chrom=chrom.removeprefix("chr"),
            start=max(1, int(start) - flank),
            end=int(end) + flank,
        )
        for gene, chrom, start, end in zip(
            genes[cn.GENE], genes[cn.GENE_CHR], genes[cn.START], genes[cn.END]
        )
    }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def normalise_list(
    variants: pd.DataFrame, regions: dict[str, functions.GeneRegion]
) -> pd.DataFrame:
    """Left-align and trim the list entries against GRCh38.

    Uses `functions.normalise_variant` (as `match_variants.py` and the
    merged associations), with `a1` as other and `a2` as effect allele.
    Sites outside every region, or whose alleles do not fit the reference,
    are kept as given (see `NormStatus`).

    Parameters
    ----------
    variants : `pd.DataFrame`
        Variant-list rows with `chr` (``chr`` prefix), `pos`, `a1`, `a2`.
    regions : `dict[str, functions.GeneRegion]`
        From `read_gene_regions`; their reference sequences are fetched
        (or read from the Ensembl cache).

    Returns
    -------
    normalised : `pd.DataFrame`
        `variants` with `pos`, `a1`, `a2` normalised, the values before in
        `pos_orig`/`a1_orig`/`a2_orig`, `norm_status`, and `variant_id`
        (``chr:pos:a1:a2``, normalised). Counts per source and status, and
        rows where `a2` rather than `a1` is the reference, are logged.

    Raises
    ------
    ReaderError
        If a reference sequence cannot be fetched from Ensembl.
    """
    vc = VariantListColumns
    normalised = variants.copy()
    normalised[vc.POS_ORIG] = normalised[vc.POS]
    normalised[vc.A1_ORIG] = normalised[vc.A1]
    normalised[vc.A2_ORIG] = normalised[vc.A2]
    sequences = functions.region_sequences(regions)
    results = [
        functions.normalise_variant(chrom, pos, a2, a1, sequences)
        for chrom, pos, a1, a2 in zip(
            normalised[vc.CHROM],
            normalised[vc.POS],
            normalised[vc.A1],
            normalised[vc.A2],
        )
    ]
    normalised[vc.POS] = [str(result.pos) for result in results]
    normalised[vc.A2] = [result.effect for result in results]
    normalised[vc.A1] = [result.other for result in results]
    normalised[vc.NORM_STATUS] = [result.status for result in results]
    normalised[vc.VARIANT_ID] = (
        normalised[vc.CHROM]
        + ":"
        + normalised[vc.POS]
        + ":"
        + normalised[vc.A1]
        + ":"
        + normalised[vc.A2]
    )

    counts = normalised.groupby([vc.SOURCE, vc.NORM_STATUS], sort=True).size()
    for (source, status), n in counts.items():
        log_info(f"normalisation {source}: {status}={n}")
    n_a2_ref = sum(result.effect_is_ref is True for result in results)
    if n_a2_ref:
        log_warn(
            f"{n_a2_ref} rows where a2, not a1, is the GRCh38 reference "
            "allele"
        )
    return normalised


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def combine_lists(
    ptv: pd.DataFrame,
    plp: pd.DataFrame,
    gof: pd.DataFrame,
    am: pd.DataFrame,
    regions: dict[str, functions.GeneRegion],
) -> pd.DataFrame:
    """Stack the PTV, P/LP, GoF and AM rows into one normalised list.

    `chr` gets a "chr" prefix (as in the old per-gene lists);
    `am_pathogenicity` and `tri_class` are NA except for the AM rows. Rows
    without a GRCh38 chr, pos or both alleles are dropped (warned per gene
    and source), as they cannot be matched or extracted. The rest is normalised
    by `normalise_list`; rows that become the same site, gene and source
    keep the first (warned). A site in several sources keeps one row per
    source.

    Parameters
    ----------
    ptv : `pd.DataFrame`
        From `load_ptv_variants`.
    plp : `pd.DataFrame`
        From `load_plp_variants`.
    gof : `pd.DataFrame`
        From `load_gof_variants`.
    am : `pd.DataFrame`
        From `load_am_variants`.
    regions : `dict[str, functions.GeneRegion]`
        From `read_gene_regions`.

    Returns
    -------
    variants : `pd.DataFrame`
        `LIST_COLUMNS`, sorted by gene, chr, pos, a1, a2 and source,
        without duplicate rows. Rows per gene and source, and the sites in
        several sources, are logged.
    """
    vc = VariantListColumns
    variants = pd.concat([ptv, plp, gof, am], ignore_index=True)
    chrom = variants[vc.CHROM].astype("string").str.removeprefix("chr")
    variants[vc.CHROM] = "chr" + chrom
    for column in LIST_COLUMNS:
        if column not in variants.columns:
            variants[column] = pd.NA
    placed = variants[[vc.CHROM, vc.POS, vc.A1, vc.A2]].notna().all(axis=1)
    for (gene, source), n in (
        variants.loc[~placed].groupby([vc.GENE, vc.SOURCE]).size().items()
    ):
        log_warn(f"{gene} {source}: {n} rows without GRCh38 chr/pos/alleles")
    variants = variants.loc[placed].drop_duplicates()
    variants = normalise_list(variants.reset_index(drop=True), regions)
    variants = variants[LIST_COLUMNS]

    site = [vc.CHROM, vc.POS, vc.A1, vc.A2, vc.GENE]
    same = variants.duplicated(subset=site + [vc.SOURCE])
    for row in variants.loc[same].itertuples(index=False):
        log_warn(
            f"{row.gene} {row.source}: {row.variant_id} (from "
            f"{row.pos_orig}:{row.a1_orig}:{row.a2_orig}) is already in "
            "the list after normalisation, dropped"
        )
    variants = variants.loc[~same]
    variants = variants.assign(
        _pos=pd.to_numeric(variants[vc.POS], errors="coerce")
    )
    variants = (
        variants.sort_values([vc.GENE, vc.CHROM, "_pos", vc.A1, vc.A2, vc.SOURCE])
        .drop(columns="_pos")
        .reset_index(drop=True)
    )

    n_sources = variants.groupby(site, dropna=False)[vc.SOURCE].nunique()
    log_info(f"{int((n_sources > 1).sum())} sites are in several sources")
    counts = variants.groupby([vc.GENE, vc.SOURCE], sort=True).size()
    for (gene, source), n in counts.items():
        log_info(f"{gene} {source}: {n} variants")
    return variants


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def marvel_rows(variants: pd.DataFrame) -> pd.DataFrame:
    """Turn the list into marvel extraction rows, both forms per site.

    A site in both sources is extracted once. Each site gets a row with
    its normalised form (`ID` = `variant_id`) and, when the original form
    differs, a row with that (`ID` = `variant_id` +
    `Constants.ORIG_ID_SUFFIX`).

    Parameters
    ----------
    variants : `pd.DataFrame`
        From `combine_lists`.

    Returns
    -------
    rows : `pd.DataFrame`
        `MARVEL_COLUMNS`, sorted by gene, position and `ID`. The number of
        sites and of extra original-form rows is logged.
    """
    vc = VariantListColumns
    sites = variants.drop_duplicates(subset=[vc.VARIANT_ID, vc.GENE])
    normalised = sites.assign(**{vc.MARVEL_ID: sites[vc.VARIANT_ID]})
    changed = (
        (sites[vc.POS] != sites[vc.POS_ORIG])
        | (sites[vc.A1] != sites[vc.A1_ORIG])
        | (sites[vc.A2] != sites[vc.A2_ORIG])
    )
    original = sites.loc[changed]
    original = original.assign(
        **{
            vc.MARVEL_ID: original[vc.VARIANT_ID] + Constants.ORIG_ID_SUFFIX,
            vc.POS: original[vc.POS_ORIG],
            vc.A1: original[vc.A1_ORIG],
            vc.A2: original[vc.A2_ORIG],
        }
    )
    rows = pd.concat([normalised, original], ignore_index=True)
    rows = rows.assign(_pos=pd.to_numeric(rows[vc.POS], errors="coerce"))
    rows = (
        rows.sort_values([vc.GENE, "_pos", vc.MARVEL_ID])
        .reset_index(drop=True)[MARVEL_COLUMNS]
    )
    log_info(
        f"marvel lists: {len(sites)} sites, {int(changed.sum())} with an "
        "extra original-form row"
    )
    return rows


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_gene_lists(variants: pd.DataFrame) -> None:
    """Write one marvel extraction list per gene, overwriting the old lists.

    Parameters
    ----------
    variants : `pd.DataFrame`
        From `combine_lists`.

    Returns
    -------
    `None`
        Writes the `marvel_rows` of each gene to
        `FileNames.VARIANT_LIST_TEMPLATE` (atomic).
    """
    rows = marvel_rows(variants)
    for gene, gene_rows in rows.groupby(VariantListColumns.GENE, sort=True):
        path = Path(FileNames.VARIANT_LIST_TEMPLATE.format(gene=gene))
        path.parent.mkdir(parents=True, exist_ok=True)
        functions.write_table_atomic(gene_rows, path)
        log_info(f"Wrote {len(gene_rows)} rows to {path}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main

if __name__ == "__main__":
    with runlog_setup(order=55, root=Paths.HERE):
        lipid_variants = combine_lists(
            load_ptv_variants(),
            load_plp_variants(),
            load_gof_variants(),
            load_am_variants(),
            read_gene_regions(),
        )
        FileNames.LIPID_VARIANTS.parent.mkdir(parents=True, exist_ok=True)
        functions.write_table_atomic(lipid_variants, FileNames.LIPID_VARIANTS)
        log_info(
            f"Wrote {len(lipid_variants)} rows to {FileNames.LIPID_VARIANTS}"
        )
        write_gene_lists(lipid_variants)
