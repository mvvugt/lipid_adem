# region_rare

Variant-list-free check: every rare variant (MAF < 1%) in each gene region, with effects of the GRCh38 alt allele. **Not oriented by gene function.** Rare variants are taken as independent.

## Script and command

- `src/meta_analysis.py --region-rare --stratified`, three runs in `src/lipid_adem.sh`:
  - `thomassen_ad_region_rare`: EUR, Thomassen AD (GCST90861026/27/29/30).
  - `armb_dementia_region_rare`: MULTI, UKB (+ APOE strata) and FinnGen dementias.
  - `ukb_dementia_region_rare`: MULTI, UKB only.
- Figures: `burden_forest.py`, `burden_apoe_forest.py`, `burden_heatmap.py` (`--label <run>`).

## Inputs

- `results/output/matched_region_variants.tsv.gz`.

## Choices

- No variant lists and no orientation, so the gene estimate mixes variants that raise and lower function.
- `_apoe_strata`: pooled per APOE stratum.

## Results and interpretation

- **Estimates sit near 1** (e.g. Thomassen AD: CETP 1.02, p = 0.047; APOB 1.01), as expected when the effects of variants in both directions average out.
- One outlier: PPARA in one APOE stratum, 1.32 (p = 3e-8). It needs a per-variant check before any interpretation.
- **Use only as a negative-control style check.** It is not evidence for a drug-target effect.
