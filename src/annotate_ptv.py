#!/usr/bin/env python3
"""annotate_ptv

Extract the protein-truncating variants (PTVs) of the gene_list.txt genes
from the VEP/LOFTEE consequences written by `vep_extract.sh`: LOFTEE
high-confidence (`LoF` = HC) on the canonical transcript of the gene.
No frequency filter is applied; the UKB AF/AC are kept as information.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS

from __future__ import annotations

import pandas as pd

import functions
from log_tools.emitter import log_info, log_warn
from log_tools.setup import runlog_setup
from project_constants import (
    ColumnNames,
    FileNames,
    GeneColumns,
    Paths,
    VariantSource,
    VepCsqColumns,
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS

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
# FILTER PTV


def filter_ptv(csq: pd.DataFrame, genes: pd.DataFrame) -> pd.DataFrame:
    """Keep the LOFTEE HC variants on the canonical transcript per gene.

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
    gene_ids = dict(zip(genes[GeneColumns.ENSEMBL_ID], genes[ColumnNames.GENE]))
    csq = csq.loc[csq[vc.GENE_ID].isin(gene_ids)].copy()
    csq[vc.GENE] = csq[vc.GENE_ID].map(gene_ids)

    keep = (csq[vc.CANONICAL] == VariantSource.VEP_CANONICAL) & (
        csq[vc.LOF] == VariantSource.LOFTEE_KEEP
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
            f"{gene}: {n_sites} sites, {n_kept} "
            f"LoF={VariantSource.LOFTEE_KEEP} on the canonical transcript "
            f"kept, {n_sites - n_kept} dropped"
        )
    return ptv.reset_index(drop=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main

if __name__ == "__main__":
    with runlog_setup(order=51, root=Paths.HERE):
        # read gene_list
        functions.require_file(FileNames.GENE_LIST, "gene list")
        genes = pd.read_csv(FileNames.GENE_LIST, sep="\t", dtype=str)
        gene_list = genes[[ColumnNames.GENE, GeneColumns.ENSEMBL_ID]]
        # read vep_csq file
        functions.require_file(
            FileNames.VEP_CSQ,
            "VEP consequence file",
            "run vep_extract.sh on Snellius and copy it here",
        )
        log_info(f"Reading VEP consequences from {FileNames.VEP_CSQ}")
        vep_csq = pd.read_csv(FileNames.VEP_CSQ, sep="\t", dtype=str, na_values=["."])
        log_info(f"Read {len(vep_csq)} variant x transcript rows")
        ptv_variants = filter_ptv(vep_csq, gene_list)
        # writeannotated PTV
        FileNames.PTV_VARIANTS.parent.mkdir(parents=True, exist_ok=True)
        functions.write_table_atomic(ptv_variants, FileNames.PTV_VARIANTS)
        log_info(
            f"Wrote {len(ptv_variants)} PTVs to {FileNames.PTV_VARIANTS}"
        )
