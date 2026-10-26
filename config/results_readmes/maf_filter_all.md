# maf_filter_all

Sensitivity analysis of `annotated_eur` with all ancestries (MULTI): UKB marvel on all samples, pooled with Thomassen and FinnGen.

## Script and command

- `src/meta_analysis.py`, from the `VARIANT_SETS` loop in `src/lipid_adem.sh` (`[myriad] sensitivity using all UKB samples`):

  ```bash
  meta_analysis.py --ancestry MULTI \
      --studies <THOMASSEN> <LIST_UKB_STUDIES> <LIST_FINNGEN_STUDIES> \
      --variant-sources <set sources> --stratified \
      --prefer-groups thomassen \
      --fallback-groups <LIST_UKB_GROUPS> <LIST_FINNGEN_STUDIES> \
      --label maf_filter_all<_set> --ukb-burden
  ```

- Figures: the same scripts as `annotated_eur`, with `--ancestry MULTI`.

## Inputs

- The same as `annotated_eur`, with the `marvel_ukb_MULTI_*` studies.

## Choices

- The same as `annotated_eur`.
- The UKB burden has no MAF cap now. Check whether the label name `maf_filter_all` still fits.

## Results and interpretation

- **Matches EUR.**
  - PCSK9 ASCVD: 0.81 (PTV) and 0.77 (PTV+AM).
  - CETP PTV+AM Alzheimer's, UKB only: 0.41 (0.15; 1.09); pooled: 1.03.
- **No dementia signal** beyond frontotemporal dementia, which rests on about 1 case (HMGCR 17.6, NPC1L1 6.7).
- The redundant and stale files are as in `annotated_eur`.
