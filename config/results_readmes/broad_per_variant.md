# broad_per_variant

The earliest meta-analysis: a per-variant IVW of every study matched to the variant lists, then a gene burden as the IVW over the variants. **There is no UKB carrier burden in this run.**

## Script and command

- `src/meta_analysis.py --ancestry EUR`: the first line of the META-ANALYSIS section of `src/lipid_adem.sh`, marked "TODO why still in here?".
- `burden_MULTI*` comes from the earlier `--ancestry MULTI` run (Oct 8).

## Inputs

- `results/output/matched_variants.tsv.gz`: all matched GWAS Catalog, FinnGen and UKB per-variant rows.

## Choices

- All variant-list sources, including the GoF and the common sites.
- Orientation by gene function.
- `_no_apoe_e2e4`: rerun without the APOE e2/e4 sites.
- `_apoe_strata`: pooled per APOE stratum.
- `_directed_only`: without the ClinVar-only sites that lack a direction.

## Results and interpretation

- **CETP:** Alzheimer's 1.06 (p = 1.5e-5), all-cause dementia 1.05 (p = 5.7e-4).
  - Driven by the common GoF site rs1800777 in the GWAS. This is the "earlier CETP effect"; it is not a rare-variant result.
- **APOE** (the `no_apoe_e2e4` runs): all-cause dementia 2.03 (p = 2e-86). This confirms the dementia outcomes are valid.
- **Replaced by the `--ukb-burden` runs** (`annotated_eur`). The `MULTI`, `no_apoe_e2e4` and Oct 24 `directed_only` files are stale.
