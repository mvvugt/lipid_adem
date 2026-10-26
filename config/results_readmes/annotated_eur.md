# annotated_eur

Main analysis up to 2026-10-26: EUR gene burden, the UKB carrier burden pooled with Thomassen (Alzheimer's) and FinnGen by IVW, one run per variant set.

## Script and command

- `src/meta_analysis.py`, from the `VARIANT_SETS` loop in `src/lipid_adem.sh` (META-ANALYSIS section, `[myriad] main`):

  ```bash
  meta_analysis.py --ancestry EUR \
      --studies <THOMASSEN> <LIST_UKB_EUR_STUDIES> <LIST_FINNGEN_STUDIES> \
      --variant-sources <set sources> --stratified \
      --prefer-groups thomassen \
      --fallback-groups <LIST_UKB_EUR_GROUPS> <LIST_FINNGEN_STUDIES> \
      --label annotated_eur<_set> --ukb-burden
  ```

- Figures: `pooled_forest.py`, `sources_forest.py`, `burden_forest.py` and `burden_apoe_forest.py` (`--label annotated_eur<_set>`), plus `variant_sets_forest.py --gene CETP`.

## Inputs

- `results/output/matched_variants.tsv.gz`: GWAS / FinnGen rows matched to `data/temp/lipid_variants.tsv` (`combine_variants.py`).
- `results/output/matched_burden.tsv.gz`: the UKB marvel carrier-burden rows (`burden_exposure.py` masks, Snellius, `src/logs/burden_exposure_28598864.log`; marvel 10039b6, `marvel_results_table.py`).
- **Studies:**
  - Thomassen 2026 AD: GCST90861026/27/29/30.
  - FinnGen R13: F5_DEMENTIA_INCLAVO, G6_ALZHEIMER, F5_VASCDEM, FTD, I9_CVD_HARD.
  - UKB EUR marvel outcomes: four dementias, ASCVD and five lipids.
- **Phenotype file:** the version after the 10 Feb update (`_combined` outcomes, NA → 0/1).

## Choices

- **Variant sets** (file suffix):

  | Suffix | Set |
  |---|---|
  | none | `lof` = PTV + ClinVar |
  | `_gof` | GoF |
  | `_am` | AM |
  | `_ptv` | PTV |
  | `_ptv_am` | PTV + AM |
  | `_am_clinvar` | AM + ClinVar |
  | `_ptv_clinvar_am` | PTV + ClinVar + AM |

- AM = AlphaMissense P/LP only (`data/raw/am_variants.tsv`, from the old `data/temp/*_variants.tsv`).
- ClinVar = P/LP that do not raise function.
- **Orientation:** effects are for lower gene function. GoF and ClinVar-raising sites are flipped; the UKB GoF burden is negated.
- **`--ukb-burden`:** the UKB gene estimate is the 0/1 carrier burden (all UKB samples, no MAF cap), not the IVW over UKB variants.
- **`--prefer-groups thomassen`:** where Thomassen has the gene and outcome, UKB uses the `_fb` mask, i.e. without Thomassen's sites.
- **`_apoe_strata`:** pooled per APOE stratum (e44, e43, e33, e22+e32).
- **`_directed_only`:** without the ClinVar-only sites that lack a lowering direction.

## Results and interpretation

- **Positive controls pass:**
  - PCSK9: LDL −0.81, ASCVD 0.67 (0.52; 0.88).
  - CETP: HDL +0.39.
  - NPC1L1, ANGPTL3: lipids.
- **HMGCR and PPARA are weak instruments.**
- **No robust dementia effect.**
- **CETP below 1 in UKB** (PTV+AM Alzheimer's 0.34, ~3 carrier cases), but the pooled estimate is 1.04. FinnGen contributes only 1–2 Finnish variants with about 9× the weight.
- **CETP GoF rs1800777:** Alzheimer's 1.07, p = 0.005, driven by one Thomassen stratum. A single common variant.
- **Redundant sets:** `lof` = `ptv` and `ptv_clinvar_am` = `ptv_am`, because ClinVar adds no carriers (follow-up in TODO.md).
- **Stale:** the LoF `_apoe_strata` and `_directed_only` files were not rewritten by the last run.
- Full interpretation: `docs/reports/results_overview.md`.
