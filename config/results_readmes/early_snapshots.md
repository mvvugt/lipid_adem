# early_snapshots

Files from before the labelled pipeline. **Retired.**

## Contents

- **`final_results.tsv[.gz]`** (2026-09-28, 10-02): the first final table of the GWAS Catalog lookups (`gwas_cat_prep.py` / `filter_gwas_cat.py`).
- **`meta_variant.tsv.gz`:** the first per-variant meta-analysis output (test run, commit `d6729b1`, 2026-10-01).
- **`CETP_PTV_results.tsv.gz`:** the cetp_marvel run A (Feb 2026, marvel 10039b6), CETP PTV mask. Used in `validation/`.
  - Alzheimer's OR 0.25 (p = 0.16).
  - 462 exposed overall, 366 in eur_only.
- **`results/figures/*.zip`:** the figure snapshots 261012, 261014 (broad variant selection) and `Archive.zip` (2026-10-24).

## Interpretation

- Kept for the record only.
- The cetp_marvel AM + HC PTV signal (Alzheimer's 0.14) is explained in `docs/reports/results_overview.md`: the old phenotype file. On the current file it is 0.34.
