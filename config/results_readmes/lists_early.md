# lists_early

The first list-based runs (2026-10-06 to 10-08). These were per-variant IVW runs with sources PTV, ClinVar, GoF and landfors_paper, and no UKB carrier burden. **Retired:** the current `src/lipid_adem.sh` no longer writes them.

## Script and command

- `src/meta_analysis.py`, from `src/lipid_adem.sh` at commit `2229b2b` (2026-10-08):

  ```bash
  # Thomassen 2026 AD, 4 APOE strata
  meta_analysis.py --ancestry EUR --outcomes alzheimers_dementia \
      --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 \
      --variant-sources PTV ClinVar GoF landfors_paper --stratified \
      --label thomassen_ad_lists
  # UKB + FinnGen R13, 4 dementias
  meta_analysis.py --ancestry MULTI --studies <ARMB_STUDIES> \
      --variant-sources PTV ClinVar GoF landfors_paper --stratified \
      --label armb_dementia_lists
  # UKB only
  meta_analysis.py --ancestry MULTI --studies <UKB_STUDIES> \
      --variant-sources PTV ClinVar GoF landfors_paper --stratified \
      --label ukb_dementia_lists
  ```

- `thomassen_ad_ptv_clinvar*` (2026-10-06): Thomassen AD with PTV + ClinVar only.

## Inputs

- `matched_variants.tsv.gz` as of 2026-10-08, with the old variant lists (old ClinVar: all classes; `landfors_paper` CETP sites).

## Choices

- GoF and ClinVar-raising sites are flipped.
- `_no_apoe_e2e4` and `_directed_only` sensitivity runs.

## Results and interpretation

- **CETP Alzheimer's** in `thomassen_ad_lists`: 1.08 (p = 0.0035); per APOE stratum up to 1.13 (p = 9e-4). Driven by the common GoF site, as in `broad_per_variant`.
- **Replaced by `annotated_eur`** (UKB carrier burden, AM sets).
