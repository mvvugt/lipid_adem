# annotated_eur_unoriented

Sensitivity analysis of `annotated_eur` without orientation by gene function: there are no GoF or ClinVar-raising flips, so the effects are those of the a2 allele.

## Script and command

- `src/meta_analysis.py`, from the `VARIANT_SETS` loop in `src/lipid_adem.sh`: the same command as `annotated_eur`, plus `--no-orient` and `--label annotated_eur_unoriented<_set>`.
- Figures: `burden_forest.py --label annotated_eur_unoriented<_set>`, `variant_sets_forest.py --gene CETP`.

## Inputs

- The same as `annotated_eur`.

## Choices

- The same as `annotated_eur`, without the flips.
- For the LoF sets nothing is flipped, so these files equal the oriented run.

## Results and interpretation

- **LoF sets:** identical to `annotated_eur` (status redundant).
- **GoF set:** the CETP rs1800777 estimates are mirrored. Alzheimer's 0.93 (vs 1.07 oriented) shows that the orientation is applied.
- **Keep only `_gof`** if this sensitivity analysis is reported.
