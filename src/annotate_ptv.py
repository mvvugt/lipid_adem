#!/usr/bin/env python3
"""annotate_ptv

Extract the protein-truncating variants (PTVs) of the gene_list.txt genes
from the VEP/LOFTEE consequences written by `vep_extract.sh`: LOFTEE
high-confidence (`LoF` = HC) on the canonical transcript of the gene.
No frequency filter is applied; the UKB AF/AC are kept as information.
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

from pathlib import Path

import pandas as pd

import functions
from log_tools.emitter import log_info, log_warn
from log_tools.setup import runlog_setup
from project_constants import (
    ColumnNames,
    Constants,
    FileNames,
    Paths,
    VepCsqColumns,
)

# columns of `FileNames.PTV_VARIANTS`, in output order
PTV_COLUMNS: list[str] = [
    VepCsqColumns.CHROM,
    VepCsqColumns.POS,
    VepCsqColumns.REF,
    VepCsqColumns.ALT,
    VepCsqColumns.GENE,
    VepCsqColumns.GENE_ID,
    VepCsqColumns.FEATURE,
    VepCsqColumns.CONSEQUENCE,
    VepCsqColumns.HGVSC,
    VepCsqColumns.HGVSP,
    VepCsqColumns.LOF_FLAGS,
    VepCsqColumns.LOF_INFO,
    VepCsqColumns.AF,
    VepCsqColumns.AC,
]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# read


def read_gene_list(path: Path) -> pd.DataFrame:
    """Read the gene symbols and Ensembl gene IDs of the gene list.

    Parameters
    ----------
    path : `Path`
        Path to `gene_list.txt`.

    Returns
    -------
    genes : `pd.DataFrame`
        Columns `gene` and `ensemblid`.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"gene list not found: {path}")
    genes = pd.read_csv(path, sep="\t", dtype=str)
    return genes[[ColumnNames.GENE, ColumnNames.ENSEMBL_ID]]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_vep_csq(path: Path) -> pd.DataFrame:
    """Read the VEP/LOFTEE consequences, one row per variant x transcript.

    Parameters
    ----------
    path : `Path`
        Path to the `vep_extract.sh` output.

    Returns
    -------
    csq : `pd.DataFrame`
        All columns as strings; bcftools' "." for a missing value is NA.

    Raises
    ------
    FileNotFoundError
        If `path` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"VEP consequence file not found: {path} (run vep_extract.sh "
            "on Snellius and copy it here)"
        )
    log_info(f"Reading VEP consequences from {path}")
    csq = pd.read_csv(path, sep="\t", dtype=str, na_values=["."])
    log_info(f"Read {len(csq)} variant x transcript rows")
    return csq


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# filter


def filter_ptv(csq: pd.DataFrame, genes: pd.DataFrame) -> pd.DataFrame:
    """Keep the LOFTEE HC variants on the canonical transcript per gene.

    A row is kept if its `Gene` is the Ensembl ID of a gene_list.txt gene,
    `CANONICAL` is `Constants.VEP_CANONICAL` and `LoF` is
    `Constants.LOFTEE_KEEP`. Rows with a multiallelic ALT are dropped
    (warned); vep_extract.sh expects biallelic records.

    Parameters
    ----------
    csq : `pd.DataFrame`
        As returned by `read_vep_csq`.
    genes : `pd.DataFrame`
        As returned by `read_gene_list`.

    Returns
    -------
    ptv : `pd.DataFrame`
        One row per site and gene, `PTV_COLUMNS`. Per gene the sites, the
        kept and the dropped sites are logged, and genes without any row.
    """
    vc = VepCsqColumns
    multi = csq[vc.ALT].str.contains(",", na=False)
    if multi.any():
        log_warn(f"{int(multi.sum())} rows with a multiallelic ALT dropped")
    csq = csq.loc[~multi]
    gene_ids = dict(zip(genes[ColumnNames.ENSEMBL_ID], genes[ColumnNames.GENE]))
    csq = csq.loc[csq[vc.GENE_ID].isin(gene_ids)].copy()
    csq[vc.GENE] = csq[vc.GENE_ID].map(gene_ids)

    keep = (csq[vc.CANONICAL] == Constants.VEP_CANONICAL) & (
        csq[vc.LOF] == Constants.LOFTEE_KEEP
    )
    site = [vc.CHROM, vc.POS, vc.REF, vc.ALT, vc.GENE]
    ptv = csq.loc[keep, PTV_COLUMNS].drop_duplicates(subset=site)

    for gene in genes[ColumnNames.GENE]:
        n_sites = len(csq.loc[csq[vc.GENE] == gene, site].drop_duplicates())
        n_kept = int((ptv[vc.GENE] == gene).sum())
        if n_sites == 0:
            log_warn(f"{gene}: no VEP rows (no VCF on Snellius?)")
            continue
        log_info(
            f"{gene}: {n_sites} sites, {n_kept} LoF={Constants.LOFTEE_KEEP} "
            f"on the canonical transcript kept, {n_sites - n_kept} dropped"
        )
    return ptv.reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main

if __name__ == "__main__":
    with runlog_setup(order=51, root=Paths.HERE):
        gene_list = read_gene_list(FileNames.GENE_LIST)
        vep_csq = read_vep_csq(FileNames.VEP_CSQ)
        ptv_variants = filter_ptv(vep_csq, gene_list)

        FileNames.PTV_VARIANTS.parent.mkdir(parents=True, exist_ok=True)
        functions.write_table_atomic(ptv_variants, FileNames.PTV_VARIANTS)
        log_info(
            f"Wrote {len(ptv_variants)} PTVs to {FileNames.PTV_VARIANTS}"
        )
