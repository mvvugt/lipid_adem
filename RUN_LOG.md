## [3] create_config (`src/create_config.py`)
- first run: 2026-11-10 10:20:45
- last run: 2026-11-10 21:52:07
- commit: `e141a61` (dirty)

Output:
```text
[info]  2026-11-10 21:52:05 variant list: 9207 of 9227 rows, genes ANGPTL3, APOA1, APOB, CETP, HMGCR, NPC1L1, PCSK9, PPARA (excluded APOE)
[info]  2026-11-10 21:52:07 genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[info]  2026-11-10 21:52:07 population: eur_unrelated=328588, eur_related=64495, nan=56362, sas_related=9394, afr_related=9141, oth_related=1607
[info]  2026-11-10 21:52:07 variant (all): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/variant_all.toml
[info]  2026-11-10 21:52:07 variant (all_apoe): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/variant_all_apoe.toml
[info]  2026-11-10 21:52:07 variant (eur): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/variant_eur.toml
[info]  2026-11-10 21:52:07 burden (all_apoe): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/burden_all_apoe.toml
[info]  2026-11-10 21:52:07 burden (eur): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/burden_eur.toml
[info]  2026-11-10 21:52:07 burden_fb (all_apoe): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/burden_fb_all_apoe.toml
[info]  2026-11-10 21:52:07 burden_fb (eur): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/burden_fb_eur.toml
[info]  2026-11-10 21:52:07 apoe (all): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/apoe_all.toml
[info]  2026-11-10 21:52:07 apoe (eur_overall): /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel/apoe_eur_overall.toml
[info]  2026-11-10 21:52:07 run table: /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_runs.tsv (9 runs)

```

## [5] apoe_exposure (`/home/mvanvugt/projects/lipid_adem/src/apoe_exposure.py`)
- first run: 2026-10-09 09:54:04
- last run: 2026-10-27 00:20:43
- commit: `244d529` (dirty)

Output:
```text
[stage] 2026-10-27 00:20:37 read
[info]  2026-10-27 00:20:39 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipids_full_pheno.tsv.gz: 469587 participants; genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[stage] 2026-10-27 00:20:39 indicators
[warn]  2026-10-27 00:20:39 27 participants without a genotype left out
[info]  2026-10-27 00:20:40 APOE_e2e2: 3025 carriers vs 466535 others
[info]  2026-10-27 00:20:40 APOE_e2e3: 57188 carriers vs 412372 others
[info]  2026-10-27 00:20:40 APOE_e2e4: 11672 carriers vs 457888 others
[info]  2026-10-27 00:20:40 APOE_e3e3: 276035 carriers vs 193525 others
[info]  2026-10-27 00:20:40 APOE_e3e4: 110438 carriers vs 359122 others
[info]  2026-10-27 00:20:40 APOE_e4e4: 11202 carriers vs 458358 others
[stage] 2026-10-27 00:20:40 write
[info]  2026-10-27 00:20:43 wrote 469560 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/apoe_diplotype.tsv.gz

```

## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-10-24 10:35:19
- commit: `04d2c6c`

Output:
```text
[info]  2026-10-24 10:20:05 8 genes, 85 icd codes
[stage] 2026-10-24 10:20:05 resolve_genes
[stage] 2026-10-24 10:20:05 resolve_efo
[info]  2026-10-24 10:20:05 trait ids checked: 21, obsolete replaced: 0
[info]  2026-10-24 10:20:05 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-24 10:20:05 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-24 10:20:05 finngen_manual
[info]  2026-10-24 10:20:06 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/study_outcome_review.tsv: 673 outcome x study exclusions for 10 outcomes
[info]  2026-10-24 10:20:06 catalog studies with aou, ukb excluded for every outcome
[info]  2026-10-24 10:20:06 all_cause_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 alzheimers_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 ascvd: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 coronary_heart_disease: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 frontotemporal_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 hf: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 parkinsons_disease_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 stroke: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 sudden_cardiac_death: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 vascular_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[stage] 2026-10-24 10:20:06 discover_gwas
[info]  2026-10-24 10:22:09 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, finngen, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-24 10:22:10 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-24 10:22:10 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-24 10:24:47 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, finngen, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-24 10:24:47 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-24 10:24:48 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-24 10:24:57 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:46 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, finngen, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-24 10:25:46 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-24 10:25:46 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-24 10:26:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:22 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 4 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:39 MONDO_0004648 (with child traits, cap per term and 30 total): 16 studies -> 5 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:39 MONDO_0004648 (with child traits, cap per term and 30 total): 16 studies -> 5 dropped for cohort overlap (aou, finngen, ukb) -> 3 dropped by review -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:52 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:52 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:53 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:31:18 MONDO_0004975 (with child traits, cap per term and 30 total): 269 studies -> 44 dropped for cohort overlap (aou, finngen, ukb) -> 72 dropped by review -> 7 with full sumstats -> 7 included, 2 included with blank cohort
[info]  2026-10-24 10:31:20 MONDO_0004975 (with child traits, cap per term and 30 total): 269 studies -> 44 dropped for cohort overlap (aou, finngen, ukb) -> 60 dropped by review -> 9 with full sumstats -> 9 included, 3 included with blank cohort
[info]  2026-10-24 10:33:34 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 74 dropped by review -> 16 with full sumstats -> 16 included, 5 included with blank cohort
[info]  2026-10-24 10:33:35 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-24 10:33:36 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-24 10:34:19 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, finngen, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-24 10:34:20 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-24 10:34:21 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-24 10:34:24 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, finngen, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:24 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:25 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:38 MONDO_0005252 (exact): 77 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 12 dropped by review -> 18 with full sumstats -> 16 included, 0 included with blank cohort
[info]  2026-10-24 10:34:38 MONDO_0005252 (exact): 77 studies -> 34 dropped for cohort overlap (aou, ukb) -> 13 dropped by review -> 20 with full sumstats -> 17 included, 0 included with blank cohort
[info]  2026-10-24 10:34:48 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:48 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:48 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:52 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-24 10:34:52 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-24 10:34:53 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-24 10:34:54 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:34:55 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:34:59 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-24 10:35:00 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-24 10:35:00 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-24 10:35:01 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-10-24 10:35:02 write_tasks
[info]  2026-10-24 10:35:02 wrote 125 tasks (312 study x outcome rows, 8 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[stage] 2026-10-24 10:35:02 scale_meta
[warn]  2026-10-24 10:35:18 GCST90480807: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90480807)
[warn]  2026-10-24 10:35:18 GCST90477959: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477959)
[warn]  2026-10-24 10:35:18 GCST90477958: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477958)
[warn]  2026-10-24 10:35:18 GCST90246093: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246093)
[warn]  2026-10-24 10:35:18 GCST90399711: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90399711)
[warn]  2026-10-24 10:35:18 GCST90726898: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726898)
[warn]  2026-10-24 10:35:18 GCST90246094: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246094)
[warn]  2026-10-24 10:35:18 GCST90246086: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246086)
[warn]  2026-10-24 10:35:18 GCST90246085: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246085)
[warn]  2026-10-24 10:35:18 GCST90726916: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726916)
[warn]  2026-10-24 10:35:18 GCST90432123: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432123)
[warn]  2026-10-24 10:35:18 GCST90246098: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246098)
[warn]  2026-10-24 10:35:18 GCST90726915: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726915)
[warn]  2026-10-24 10:35:19 GCST90432122: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432122)
[warn]  2026-10-24 10:35:19 GCST90480188: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90480188)
[warn]  2026-10-24 10:35:19 GCST90477978: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477978)
[warn]  2026-10-24 10:35:19 GCST90477977: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477977)
[warn]  2026-10-24 10:35:19 GCST90246096: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246096)
[warn]  2026-10-24 10:35:19 GCST90018650: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018650)
[warn]  2026-10-24 10:35:19 GCST90726750: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726750)
[warn]  2026-10-24 10:35:19 GCST90704648: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90704648)
[warn]  2026-10-24 10:35:19 GCST90727420: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90727420)
[warn]  2026-10-24 10:35:19 GCST90565439: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90565439)
[warn]  2026-10-24 10:35:19 GCST90566388: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90566388)
[warn]  2026-10-24 10:35:19 GCST90276158: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276158)
[warn]  2026-10-24 10:35:19 GCST90276157: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276157)
[warn]  2026-10-24 10:35:19 GCST007511: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST007511)
[warn]  2026-10-24 10:35:19 GCST003452: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST003452)
[warn]  2026-10-24 10:35:19 GCST002245: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST002245)
[warn]  2026-10-24 10:35:19 GCST90861026: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861026)
[warn]  2026-10-24 10:35:19 GCST90861027: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861027)
[warn]  2026-10-24 10:35:19 GCST90861029: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861029)
[warn]  2026-10-24 10:35:19 GCST90861030: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861030)
[warn]  2026-10-24 10:35:19 GCST90476370: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90476370)
[warn]  2026-10-24 10:35:19 GCST90018586: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018586)
[info]  2026-10-24 10:35:19 metadata yaml read for 115 included studies, scale: unknown=115
[info]  2026-10-24 10:35:19 wrote 2655 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [10] slurm_array_final_task1
- first run: 2026-11-10 16:01:03
- last run: 2026-11-11 19:20:30
- commit: `25d4593` (dirty)

Output:
```text
[info]  2026-11-11 19:12:37 config: /home/mvanvugt/projects/lipid_adem/config/marvel/burden_fb_eur.toml
[info]  2026-11-11 19:12:37 stage: final
[info]  2026-11-11 19:12:37 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-11 19:12:37 node: tcn10.local.snellius.surf.nl, job id: 29134223, task: 1
[info]  2026-11-11 19:16:36 aggregate: finished
[info]  2026-11-11 19:20:29 associate: finished

```

## [10] slurm_script
- first run: 2026-10-21 11:53:26
- last run: 2026-10-21 11:53:26
- commit: `e9443d3` (dirty)

Output:
```text
[info]  2026-10-21 11:38:22 using root directory: /home/mvanvugt/projects/lipid_adem
[info]  2026-10-21 11:38:22 VCF directory: /projects/0/aus20644/data/ukbiobank/genetics/b38/lof, pattern: chr{chrom}_merged_vep.vcf.gz
[info]  2026-10-21 11:38:22 gene list: /home/mvanvugt/projects/lipid_adem/data/raw/gene_list.txt
[info]  2026-10-21 11:38:22 working directory (temporary): /scratch-local/mvanvugt.28412845/tmp.rj01qmYBde/task_1
[info]  2026-10-21 11:38:22 results will be moved to on success: /home/mvanvugt/projects/lipid_adem/data/temp
[info]  2026-10-21 11:38:22 bcftools 1.18
[info]  2026-10-21 11:38:22 8 genes in /home/mvanvugt/projects/lipid_adem/data/raw/gene_list.txt
[info]  2026-10-21 11:38:22 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:39:51 CETP (ENSG00000087237, chr16:56961980-56983663): 6848 rows
[info]  2026-10-21 11:39:52 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr5_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:41:35 HMGCR (ENSG00000113161, chr5:75342606-75360339): 20751 rows
[info]  2026-10-21 11:41:44 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr7_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:44:10 NPC1L1 (ENSG00000015520, chr7:44513450-44541259): 9909 rows
[info]  2026-10-21 11:44:10 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:45:43 PCSK9 (ENSG00000169174, chr1:55039838-55063581): 15046 rows
[info]  2026-10-21 11:46:33 ANGPTL3 (ENSG00000132855, chr1:62597567-62604814): 2406 rows
[info]  2026-10-21 11:46:34 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr22_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:47:17 PPARA (ENSG00000186951, chr22:46198384-46235377): 2982 rows
[info]  2026-10-21 11:47:18 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr11_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:47:50 APOA1 (ENSG00000118137, chr11:116834677-116842065): 2805 rows
[info]  2026-10-21 11:47:51 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr2_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:53:24 APOB (ENSG00000084674, chr2:21001305-21044075): 18416 rows
[info]  2026-10-21 11:53:26 8 genes written to /scratch-local/mvanvugt.28412845/tmp.rj01qmYBde/task_1/vep_lipid_gene_csq.tsv.gz

```

## [10] slurm_script_extract_task1
- first run: 2026-10-22 03:17:59
- last run: 2026-11-10 10:10:18
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:10:10 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 10:10:10 stage: extract
[info]  2026-11-10 10:10:10 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:10:10 node: tcn8.local.snellius.surf.nl, job id: 29058738, task: 1
[info]  2026-11-10 10:10:10 task 1: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr1.vcf.gz
[info]  2026-11-10 10:10:18 extract vep_chr1.vcf.gz: finished

```

## [10] slurm_script_extract_task2
- first run: 2026-10-22 03:17:58
- last run: 2026-11-10 10:09:23
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:09:13 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 10:09:13 stage: extract
[info]  2026-11-10 10:09:13 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:09:13 node: tcn21.local.snellius.surf.nl, job id: 29058739, task: 2
[info]  2026-11-10 10:09:13 task 2: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr11.vcf.gz
[info]  2026-11-10 10:09:23 extract vep_chr11.vcf.gz: finished

```

## [10] slurm_script_extract_task3
- first run: 2026-10-22 03:17:57
- last run: 2026-11-10 10:14:27
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:14:11 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 10:14:11 stage: extract
[info]  2026-11-10 10:14:11 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:14:11 node: tcn8.local.snellius.surf.nl, job id: 29058740, task: 3
[info]  2026-11-10 10:14:11 task 3: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr2.vcf.gz
[info]  2026-11-10 10:14:27 extract vep_chr2.vcf.gz: finished

```

## [10] slurm_script_extract_task4
- first run: 2026-10-22 03:37:57
- last run: 2026-11-10 10:09:23
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:09:12 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 10:09:12 stage: extract
[info]  2026-11-10 10:09:12 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:09:12 node: tcn21.local.snellius.surf.nl, job id: 29058741, task: 4
[info]  2026-11-10 10:09:12 task 4: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr19.vcf.gz
[info]  2026-11-10 10:09:23 extract vep_chr19.vcf.gz: finished

```

## [10] slurm_script_extract_task5
- first run: 2026-10-22 03:18:01
- last run: 2026-11-10 10:10:21
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:10:11 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 10:10:11 stage: extract
[info]  2026-11-10 10:10:11 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:10:11 node: tcn11.local.snellius.surf.nl, job id: 29058742, task: 5
[info]  2026-11-10 10:10:11 task 5: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr16.vcf.gz
[info]  2026-11-10 10:10:21 extract vep_chr16.vcf.gz: finished

```

## [10] slurm_script_extract_task6
- first run: 2026-10-22 03:17:58
- last run: 2026-11-03 16:50:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:49:57 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:49:57 stage: extract
[info]  2026-11-03 16:49:57 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:49:57 node: tcn64.local.snellius.surf.nl, job id: 28876278, task: 6
[info]  2026-11-03 16:49:57 task 6: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr5.vcf.gz
[info]  2026-11-03 16:50:07 extract vep_chr5.vcf.gz: finished

```

## [10] slurm_script_extract_task7
- first run: 2026-10-22 04:30:10
- last run: 2026-11-03 16:50:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:50:11 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:50:11 stage: extract
[info]  2026-11-03 16:50:11 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:50:11 node: tcn100.local.snellius.surf.nl, job id: 28876279, task: 7
[info]  2026-11-03 16:50:11 task 7: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr7.vcf.gz
[info]  2026-11-03 16:50:19 extract vep_chr7.vcf.gz: finished

```

## [10] slurm_script_extract_task8
- first run: 2026-10-22 04:30:44
- last run: 2026-11-10 10:09:23
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:09:12 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 10:09:12 stage: extract
[info]  2026-11-10 10:09:12 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:09:12 node: tcn21.local.snellius.surf.nl, job id: 29058736, task: 8
[info]  2026-11-10 10:09:12 task 8: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr22.vcf.gz
[info]  2026-11-10 10:09:22 extract vep_chr22.vcf.gz: finished

```

## [10] slurm_script_f1a3a8a_bin_vs_ref_CETP_compare
- first run: 2026-11-03 19:29:01
- last run: 2026-11-03 19:29:01
- commit: `23ebede` (dirty)
- status: failed

Output:
```text
[error] 2026-11-03 19:28:59 -s/--step must look like step4 or step2_CETP, not 'f1a3a8a_bin_vs_ref_CETP'
--- error output (raw) ---


```

## [10] slurm_script_final_task1
- first run: 2026-10-22 04:37:33
- last run: 2026-11-10 11:48:28
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 11:45:16 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-11-10 11:45:17 stage: final
[info]  2026-11-10 11:45:17 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 11:45:17 node: tcn33.local.snellius.surf.nl, job id: 29062224, task: 1
[info]  2026-11-10 11:45:57 aggregate: finished
[info]  2026-11-10 11:48:28 associate: finished

```

## [10] slurm_script_step10_bin_vs_8a_CETP_compare
- first run: 2026-11-02 23:33:41
- last run: 2026-11-02 23:37:13
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 23:37:06 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_bin_vs_8a_CETP; mode: compare; env: prot_misc
[info]  2026-11-02 23:37:06 working directory (temporary): /scratch-local/mvanvugt.28852480/tmp.C0ICJuGnJt/task_1
[warn]  2026-11-02 23:37:06 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 23:37:06 manifest: 3 file(s) in /scratch-local/mvanvugt.28852480/tmp.C0ICJuGnJt/task_1/step10_bin_vs_8a_CETP.compare.md5
[info]  2026-11-02 23:37:13 step10_bin_vs_8a_CETP: GATE PASS
[info]  2026-11-02 23:37:13 *** END ***

```

## [10] slurm_script_step10_dos_vs_bin_all7_compare
- first run: 2026-11-02 23:52:12
- last run: 2026-11-02 23:52:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 23:52:03 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_dos_vs_bin_all7; mode: compare; env: prot_misc
[info]  2026-11-02 23:52:03 working directory (temporary): /scratch-local/mvanvugt.28852813/tmp.fzvufOx8Lu/task_1
[warn]  2026-11-02 23:52:03 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 23:52:03 manifest: 3 file(s) in /scratch-local/mvanvugt.28852813/tmp.fzvufOx8Lu/task_1/step10_dos_vs_bin_all7.compare.md5
[info]  2026-11-02 23:52:11 step10_dos_vs_bin_all7: GATE PASS
[info]  2026-11-02 23:52:11 *** END ***

```

## [10] slurm_script_step10_dos_vs_bin_compare
- first run: 2026-11-02 23:35:52
- last run: 2026-11-02 23:47:08
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 23:46:59 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_dos_vs_bin; mode: compare; env: prot_misc
[info]  2026-11-02 23:46:59 working directory (temporary): /scratch-local/mvanvugt.28852693/tmp.yA4HGSqVGJ/task_1
[warn]  2026-11-02 23:46:59 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 23:46:59 manifest: 3 file(s) in /scratch-local/mvanvugt.28852693/tmp.yA4HGSqVGJ/task_1/step10_dos_vs_bin.compare.md5
[warn]  2026-11-02 23:47:08 step10_dos_vs_bin: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step10_dos_vs_bin/summary.tsv.gz
[info]  2026-11-02 23:47:08 *** END ***

```

## [10] slurm_script_step10_masks_vs_old_compare
- first run: 2026-11-02 17:29:48
- last run: 2026-11-02 17:29:48
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 17:29:44 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_masks_vs_old; mode: compare; env: prot_misc
[info]  2026-11-02 17:29:44 working directory (temporary): /scratch-local/mvanvugt.28846072/tmp.JBgzLF5xO0/task_1
[warn]  2026-11-02 17:29:44 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 17:29:44 manifest: 385 file(s) in /scratch-local/mvanvugt.28846072/tmp.JBgzLF5xO0/task_1/step10_masks_vs_old.compare.md5
[warn]  2026-11-02 17:29:48 step10_masks_vs_old: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step10_masks_vs_old/summary.tsv.gz
[info]  2026-11-02 17:29:48 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_bin_vs_ref_CETP_compare
- first run: 2026-11-04 09:20:16
- last run: 2026-11-04 13:28:47
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 13:28:35 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_bin_vs_ref_CETP; mode: compare; env: prot_misc
[info]  2026-11-04 13:28:36 working directory (temporary): /scratch-local/mvanvugt.28888611/tmp.JdzO2zMb9W/task_1
[warn]  2026-11-04 13:28:36 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 13:28:36 manifest: 3 file(s) in /scratch-local/mvanvugt.28888611/tmp.JdzO2zMb9W/task_1/step11_f1a3a8a_bin_vs_ref_CETP.compare.md5
[info]  2026-11-04 13:28:47 step11_f1a3a8a_bin_vs_ref_CETP: GATE PASS
[info]  2026-11-04 13:28:47 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_bin_vs_ref_PCSK9_compare
- first run: 2026-11-04 09:18:04
- last run: 2026-11-04 13:29:49
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 13:29:38 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_bin_vs_ref_PCSK9; mode: compare; env: prot_misc
[info]  2026-11-04 13:29:38 working directory (temporary): /scratch-local/mvanvugt.28888990/tmp.2fpwhCFhuy/task_1
[warn]  2026-11-04 13:29:38 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 13:29:38 manifest: 3 file(s) in /scratch-local/mvanvugt.28888990/tmp.2fpwhCFhuy/task_1/step11_f1a3a8a_bin_vs_ref_PCSK9.compare.md5
[info]  2026-11-04 13:29:48 step11_f1a3a8a_bin_vs_ref_PCSK9: GATE PASS
[info]  2026-11-04 13:29:48 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_masks_vs_ref_compare
- first run: 2026-11-04 10:37:30
- last run: 2026-11-04 10:37:30
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 10:37:25 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_masks_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 10:37:25 working directory (temporary): /scratch-local/mvanvugt.28889039/tmp.ibpyWVtBz4/task_1
[warn]  2026-11-04 10:37:25 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 10:37:25 manifest: 2 file(s) in /scratch-local/mvanvugt.28889039/tmp.ibpyWVtBz4/task_1/step11_f1a3a8a_burden_masks_vs_ref.compare.md5
[info]  2026-11-04 10:37:30 step11_f1a3a8a_burden_masks_vs_ref: GATE PASS
[info]  2026-11-04 10:37:30 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_nj1_compare
- first run: 2026-11-04 12:23:05
- last run: 2026-11-04 12:23:05
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 12:23:01 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_nj1; mode: compare; env: prot_misc
[info]  2026-11-04 12:23:01 working directory (temporary): /scratch-local/mvanvugt.28891395/tmp.TOSLlCNFIS/task_1
[warn]  2026-11-04 12:23:01 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 12:23:01 manifest: 2 file(s) in /scratch-local/mvanvugt.28891395/tmp.TOSLlCNFIS/task_1/step11_f1a3a8a_burden_nj1.compare.md5
[info]  2026-11-04 12:23:05 step11_f1a3a8a_burden_nj1: GATE PASS
[info]  2026-11-04 12:23:05 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_nj8_compare
- first run: 2026-11-04 12:23:34
- last run: 2026-11-04 12:23:34
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 12:23:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_nj8; mode: compare; env: prot_misc
[info]  2026-11-04 12:23:32 working directory (temporary): /scratch-local/mvanvugt.28891396/tmp.IPeEJ0KWm5/task_1
[warn]  2026-11-04 12:23:32 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 12:23:32 manifest: 2 file(s) in /scratch-local/mvanvugt.28891396/tmp.IPeEJ0KWm5/task_1/step11_f1a3a8a_burden_nj8.compare.md5
[info]  2026-11-04 12:23:34 step11_f1a3a8a_burden_nj8: GATE PASS
[info]  2026-11-04 12:23:34 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_vs_ref_compare
- first run: 2026-11-04 10:39:22
- last run: 2026-11-04 13:30:40
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 13:30:37 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 13:30:37 working directory (temporary): /scratch-local/mvanvugt.28889069/tmp.63kM3aQxCF/task_1
[warn]  2026-11-04 13:30:37 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 13:30:37 manifest: 2 file(s) in /scratch-local/mvanvugt.28889069/tmp.63kM3aQxCF/task_1/step11_f1a3a8a_burden_vs_ref.compare.md5
[warn]  2026-11-04 13:30:39 step11_f1a3a8a_burden_vs_ref: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step11_f1a3a8a_burden_vs_ref/summary.tsv.gz
[info]  2026-11-04 13:30:39 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_variant_bin_vs_ref_compare
- first run: 2026-11-04 15:31:05
- last run: 2026-11-04 15:31:05
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 15:30:49 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_variant_bin_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 15:30:49 working directory (temporary): /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1
[warn]  2026-11-04 15:30:49 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 15:30:49 manifest: 2 file(s) in /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1/step11_f1a3a8a_variant_bin_vs_ref.compare.md5
[info]  2026-11-04 15:31:05 step11_f1a3a8a_variant_bin_vs_ref: GATE PASS
[info]  2026-11-04 15:31:05 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_variant_dos_vs_ref_compare
- first run: 2026-11-04 10:38:36
- last run: 2026-11-04 10:38:36
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 10:38:27 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_variant_dos_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 10:38:27 working directory (temporary): /scratch-local/mvanvugt.28889040/tmp.UKk0WqQYUd/task_1
[warn]  2026-11-04 10:38:27 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 10:38:27 manifest: 2 file(s) in /scratch-local/mvanvugt.28889040/tmp.UKk0WqQYUd/task_1/step11_f1a3a8a_variant_dos_vs_ref.compare.md5
[warn]  2026-11-04 10:38:36 step11_f1a3a8a_variant_dos_vs_ref: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step11_f1a3a8a_variant_dos_vs_ref/summary.tsv.gz
[info]  2026-11-04 10:38:36 *** END ***

```

## [10] slurm_script_step2_CETP_compare
- first run: 2026-10-24 22:16:32
- last run: 2026-10-24 22:16:32
- commit: `6fc4384` (dirty)
- status: failed

Output:
```text
[error] 2026-10-24 22:16:32 -s/--step must look like step4 or step4_small, not 'step2_CETP'
--- error output (raw) ---


```

## [10] slurm_script_step2_PCSK9_compare
- first run: 2026-10-24 22:16:34
- last run: 2026-10-26 11:32:16
- commit: `fdddf24` (dirty)

Output:
```text
[info]  2026-10-26 11:32:04 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step2_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-26 11:32:04 working directory (temporary): /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1
[warn]  2026-10-26 11:32:04 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-26 11:32:04 manifest: 6 file(s) in /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1/step2_PCSK9.compare.md5
[warn]  2026-10-26 11:32:16 step2_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step2_PCSK9/summary.tsv.gz
[info]  2026-10-26 11:32:16 *** END ***

```

## [10] slurm_script_step2_old
- first run: 2026-10-24 11:01:37
- last run: 2026-10-24 17:15:11
- commit: `6fc4384` (dirty)

Output:
```text
[info]  2026-10-24 15:36:25 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step2; mode: old; env: marvel_old
[info]  2026-10-24 15:36:25 working directory (temporary): /scratch-local/mvanvugt.28545065/tmp.TgMXLqNqxG/task_1
[info]  2026-10-24 15:36:25 manifest: 8 file(s) in /scratch-local/mvanvugt.28545065/tmp.TgMXLqNqxG/task_1/step2.old.md5
[info]  2026-10-24 17:15:11 *** END ***

```

## [10] slurm_script_step2b_old
- first run: 2026-10-26 23:28:20
- last run: 2026-10-26 23:28:20
- commit: `ab86ef1` (dirty)

Output:
```text
[info]  2026-10-26 19:27:52 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step2b; mode: old; env: marvel_old
[info]  2026-10-26 19:27:52 working directory (temporary): /scratch-local/mvanvugt.28602694/tmp.pVG9y9aFJh/task_1
[info]  2026-10-26 19:27:52 manifest: 8 file(s) in /scratch-local/mvanvugt.28602694/tmp.pVG9y9aFJh/task_1/step2b.old.md5
[info]  2026-10-26 23:28:20 *** END ***

```

## [10] slurm_script_step4_CETP_config
- first run: 2026-10-27 09:54:15
- last run: 2026-10-27 09:54:15
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:54:07 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_CETP; mode: config; env: marvel_old
[info]  2026-10-27 09:54:07 working directory (temporary): /scratch-local/mvanvugt.28614790/tmp.2rK6j6Kjdk/task_1
[info]  2026-10-27 09:54:07 manifest: 2 file(s) in /scratch-local/mvanvugt.28614790/tmp.2rK6j6Kjdk/task_1/step4_CETP.config.md5
[info]  2026-10-27 09:54:15 *** END ***

```

## [10] slurm_script_step4_CETP_old
- first run: 2026-10-28 02:53:35
- last run: 2026-10-28 02:53:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 10:23:47 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_CETP; mode: old; env: marvel_old
[info]  2026-10-27 10:23:47 working directory (temporary): /scratch-local/mvanvugt.28615314/tmp.RdHJ8C8uPK/task_1
[info]  2026-10-27 10:23:47 manifest: 5 file(s) in /scratch-local/mvanvugt.28615314/tmp.RdHJ8C8uPK/task_1/step4_CETP.old.md5
[info]  2026-10-28 02:53:35 *** END ***

```

## [10] slurm_script_step4_PCSK9_config
- first run: 2026-10-28 11:42:40
- last run: 2026-10-28 11:42:40
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 11:42:31 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_PCSK9; mode: config; env: marvel_old
[info]  2026-10-28 11:42:31 working directory (temporary): /scratch-local/mvanvugt.28654376/tmp.CWFWvJLLrQ/task_1
[info]  2026-10-28 11:42:31 manifest: 2 file(s) in /scratch-local/mvanvugt.28654376/tmp.CWFWvJLLrQ/task_1/step4_PCSK9.config.md5
[info]  2026-10-28 11:42:40 *** END ***

```

## [10] slurm_script_step4_PCSK9_old
- first run: 2026-10-29 17:21:35
- last run: 2026-10-29 17:21:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 11:44:19 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_PCSK9; mode: old; env: marvel_old
[info]  2026-10-28 11:44:19 working directory (temporary): /scratch-local/mvanvugt.28654523/tmp.zcsKrQKsDe/task_1
[info]  2026-10-28 11:44:19 manifest: 5 file(s) in /scratch-local/mvanvugt.28654523/tmp.zcsKrQKsDe/task_1/step4_PCSK9.old.md5
[info]  2026-10-29 17:21:35 *** END ***

```

## [10] slurm_script_step4_vs_a_CETP_compare
- first run: 2026-10-28 11:45:12
- last run: 2026-10-28 22:44:45
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 22:44:29 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_vs_a_CETP; mode: compare; env: prot_misc
[info]  2026-10-28 22:44:29 working directory (temporary): /scratch-local/mvanvugt.28683290/tmp.s1T1OXE2AF/task_1
[warn]  2026-10-28 22:44:29 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-28 22:44:31 manifest: 2190 file(s) in /scratch-local/mvanvugt.28683290/tmp.s1T1OXE2AF/task_1/step4_vs_a_CETP.compare.md5
[warn]  2026-10-28 22:44:45 step4_vs_a_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4_vs_a_CETP/summary.tsv.gz
[info]  2026-10-28 22:44:45 *** END ***

```

## [10] slurm_script_step4_vs_a_PCSK9_compare
- first run: 2026-10-28 22:44:51
- last run: 2026-10-28 22:44:51
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 22:44:29 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_vs_a_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-28 22:44:29 working directory (temporary): /scratch-local/mvanvugt.28683291/tmp.hN6teY3V8g/task_1
[warn]  2026-10-28 22:44:29 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-28 22:44:32 manifest: 3176 file(s) in /scratch-local/mvanvugt.28683291/tmp.hN6teY3V8g/task_1/step4_vs_a_PCSK9.compare.md5
[warn]  2026-10-28 22:44:51 step4_vs_a_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4_vs_a_PCSK9/summary.tsv.gz
[info]  2026-10-28 22:44:51 *** END ***

```

## [10] slurm_script_step4_vs_b_CETP_compare
- first run: 2026-10-28 09:58:18
- last run: 2026-10-28 09:58:18
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 09:58:01 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_vs_b_CETP; mode: compare; env: prot_misc
[info]  2026-10-28 09:58:01 working directory (temporary): /scratch-local/mvanvugt.28651086/tmp.Sve3WE1lGy/task_1
[warn]  2026-10-28 09:58:01 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-28 09:58:02 manifest: 1337 file(s) in /scratch-local/mvanvugt.28651086/tmp.Sve3WE1lGy/task_1/step4_vs_b_CETP.compare.md5
[warn]  2026-10-28 09:58:18 step4_vs_b_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4_vs_b_CETP/summary.tsv.gz
[info]  2026-10-28 09:58:18 *** END ***

```

## [10] slurm_script_step4b7_CETP_config
- first run: 2026-10-28 16:34:07
- last run: 2026-10-28 16:34:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:34:00 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_CETP; mode: config; env: marvel_old
[info]  2026-10-28 16:34:00 working directory (temporary): /scratch-local/mvanvugt.28667929/tmp.Q3ws3wp1rM/task_1
[info]  2026-10-28 16:34:00 manifest: 2 file(s) in /scratch-local/mvanvugt.28667929/tmp.Q3ws3wp1rM/task_1/step4b7_CETP.config.md5
[info]  2026-10-28 16:34:07 *** END ***

```

## [10] slurm_script_step4b7_CETP_old
- first run: 2026-10-29 06:16:51
- last run: 2026-10-29 06:16:51
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:36:24 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_CETP; mode: old; env: marvel_old
[info]  2026-10-28 16:36:24 working directory (temporary): /scratch-local/mvanvugt.28668051/tmp.8e5CuQGf1L/task_1
[info]  2026-10-28 16:36:24 manifest: 5 file(s) in /scratch-local/mvanvugt.28668051/tmp.8e5CuQGf1L/task_1/step4b7_CETP.old.md5
[info]  2026-10-29 06:16:51 *** END ***

```

## [10] slurm_script_step4b7_PCSK9_config
- first run: 2026-10-28 16:34:06
- last run: 2026-10-28 16:34:06
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:33:58 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_PCSK9; mode: config; env: marvel_old
[info]  2026-10-28 16:33:58 working directory (temporary): /scratch-local/mvanvugt.28667930/tmp.K5EnrdW8LE/task_1
[info]  2026-10-28 16:33:58 manifest: 2 file(s) in /scratch-local/mvanvugt.28667930/tmp.K5EnrdW8LE/task_1/step4b7_PCSK9.config.md5
[info]  2026-10-28 16:34:06 *** END ***

```

## [10] slurm_script_step4b7_PCSK9_old
- first run: 2026-10-29 18:19:29
- last run: 2026-10-29 18:19:29
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:36:27 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_PCSK9; mode: old; env: marvel_old
[info]  2026-10-28 16:36:27 working directory (temporary): /scratch-local/mvanvugt.28668052/tmp.jfqGkzR0dz/task_1
[info]  2026-10-28 16:36:27 manifest: 5 file(s) in /scratch-local/mvanvugt.28668052/tmp.jfqGkzR0dz/task_1/step4b7_PCSK9.old.md5
[info]  2026-10-29 18:19:29 *** END ***

```

## [10] slurm_script_step4b7_vs_b_CETP_compare
- first run: 2026-10-29 21:48:47
- last run: 2026-10-29 21:48:47
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 21:48:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_vs_b_CETP; mode: compare; env: prot_misc
[info]  2026-10-29 21:48:32 working directory (temporary): /scratch-local/mvanvugt.28743058/tmp.CJeQrBbl1L/task_1
[warn]  2026-10-29 21:48:32 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-29 21:48:33 manifest: 1337 file(s) in /scratch-local/mvanvugt.28743058/tmp.CJeQrBbl1L/task_1/step4b7_vs_b_CETP.compare.md5
[warn]  2026-10-29 21:48:47 step4b7_vs_b_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4b7_vs_b_CETP/summary.tsv.gz
[info]  2026-10-29 21:48:47 *** END ***

```

## [10] slurm_script_step4b7_vs_b_PCSK9_compare
- first run: 2026-10-29 21:48:52
- last run: 2026-10-29 21:48:52
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 21:48:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_vs_b_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-29 21:48:32 working directory (temporary): /scratch-local/mvanvugt.28743065/tmp.JuTg2Spfs1/task_1
[warn]  2026-10-29 21:48:32 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-29 21:48:33 manifest: 2097 file(s) in /scratch-local/mvanvugt.28743065/tmp.JuTg2Spfs1/task_1/step4b7_vs_b_PCSK9.compare.md5
[warn]  2026-10-29 21:48:52 step4b7_vs_b_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4b7_vs_b_PCSK9/summary.tsv.gz
[info]  2026-10-29 21:48:52 *** END ***

```

## [10] slurm_script_step4na_CETP_config
- first run: 2026-10-27 09:54:15
- last run: 2026-10-27 09:54:15
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:54:07 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_CETP; mode: config; env: marvel_old
[info]  2026-10-27 09:54:07 working directory (temporary): /scratch-local/mvanvugt.28614791/tmp.NVBbAmSir7/task_1
[info]  2026-10-27 09:54:07 manifest: 2 file(s) in /scratch-local/mvanvugt.28614791/tmp.NVBbAmSir7/task_1/step4na_CETP.config.md5
[info]  2026-10-27 09:54:15 *** END ***

```

## [10] slurm_script_step4na_CETP_old
- first run: 2026-10-28 08:21:54
- last run: 2026-10-28 08:21:54
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 10:23:45 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_CETP; mode: old; env: marvel_old
[info]  2026-10-27 10:23:45 working directory (temporary): /scratch-local/mvanvugt.28615315/tmp.7uQq74sD8p/task_1
[info]  2026-10-27 10:23:45 manifest: 5 file(s) in /scratch-local/mvanvugt.28615315/tmp.7uQq74sD8p/task_1/step4na_CETP.old.md5
[info]  2026-10-28 08:21:54 *** END ***

```

## [10] slurm_script_step4na_PCSK9_config
- first run: 2026-10-27 09:54:15
- last run: 2026-10-27 09:54:15
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:54:08 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_PCSK9; mode: config; env: marvel_old
[info]  2026-10-27 09:54:08 working directory (temporary): /scratch-local/mvanvugt.28614792/tmp.sQvZBYt9HY/task_1
[info]  2026-10-27 09:54:08 manifest: 2 file(s) in /scratch-local/mvanvugt.28614792/tmp.sQvZBYt9HY/task_1/step4na_PCSK9.config.md5
[info]  2026-10-27 09:54:14 *** END ***

```

## [10] slurm_script_step4na_PCSK9_old
- first run: 2026-10-28 22:17:35
- last run: 2026-10-28 22:17:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 10:23:46 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_PCSK9; mode: old; env: marvel_old
[info]  2026-10-27 10:23:46 working directory (temporary): /scratch-local/mvanvugt.28615316/tmp.S0hdwC58m6/task_1
[info]  2026-10-27 10:23:46 manifest: 5 file(s) in /scratch-local/mvanvugt.28615316/tmp.S0hdwC58m6/task_1/step4na_PCSK9.old.md5
[info]  2026-10-28 22:17:35 *** END ***

```

## [10] slurm_script_step6_CETP_new
- first run: 2026-10-30 01:56:49
- last run: 2026-10-30 01:56:49
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:17:20 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_CETP; mode: new; env: marvel_new
[info]  2026-10-29 23:17:20 working directory (temporary): /scratch-local/mvanvugt.28746645/tmp.ntDfjzeWc1/task_1
[info]  2026-10-29 23:17:21 manifest: 3 file(s) in /scratch-local/mvanvugt.28746645/tmp.ntDfjzeWc1/task_1/step6_CETP.new.md5
[info]  2026-10-30 01:56:49 step6_CETP: marvelous associate done, output to data/temp/validation/step6/CETP
[info]  2026-10-30 01:56:49 *** END ***

```

## [10] slurm_script_step6_PCSK9_new
- first run: 2026-10-30 03:31:28
- last run: 2026-10-30 03:31:28
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:17:20 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_PCSK9; mode: new; env: marvel_new
[info]  2026-10-29 23:17:20 working directory (temporary): /scratch-local/mvanvugt.28746647/tmp.laIYpkhjir/task_1
[info]  2026-10-29 23:17:20 manifest: 3 file(s) in /scratch-local/mvanvugt.28746647/tmp.laIYpkhjir/task_1/step6_PCSK9.new.md5
[info]  2026-10-30 03:31:27 step6_PCSK9: marvelous associate done, output to data/temp/validation/step6/PCSK9
[info]  2026-10-30 03:31:27 *** END ***

```

## [10] slurm_script_step6_vs_bna_CETP_compare
- first run: 2026-10-30 08:06:56
- last run: 2026-10-30 08:06:56
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 08:06:45 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_vs_bna_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 08:06:45 working directory (temporary): /scratch-local/mvanvugt.28763720/tmp.xR59DBQRrG/task_1
[warn]  2026-10-30 08:06:45 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 08:06:46 manifest: 1337 file(s) in /scratch-local/mvanvugt.28763720/tmp.xR59DBQRrG/task_1/step6_vs_bna_CETP.compare.md5
[warn]  2026-10-30 08:06:55 step6_vs_bna_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step6_vs_bna_CETP/summary.tsv.gz
[info]  2026-10-30 08:06:55 *** END ***

```

## [10] slurm_script_step6_vs_bna_PCSK9_compare
- first run: 2026-10-30 08:06:59
- last run: 2026-10-30 08:06:59
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 08:06:44 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_vs_bna_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 08:06:44 working directory (temporary): /scratch-local/mvanvugt.28763721/tmp.4yZBP8yeFZ/task_1
[warn]  2026-10-30 08:06:44 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 08:06:46 manifest: 2097 file(s) in /scratch-local/mvanvugt.28763721/tmp.4yZBP8yeFZ/task_1/step6_vs_bna_PCSK9.compare.md5
[warn]  2026-10-30 08:06:59 step6_vs_bna_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step6_vs_bna_PCSK9/summary.tsv.gz
[info]  2026-10-30 08:06:59 *** END ***

```

## [10] slurm_script_step6b_CETP_new
- first run: 2026-10-30 02:42:52
- last run: 2026-10-30 02:42:52
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:53:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_CETP; mode: new; env: marvel_new
[info]  2026-10-29 23:53:32 working directory (temporary): /scratch-local/mvanvugt.28750274/tmp.LkQEXyT2he/task_1
[info]  2026-10-29 23:53:32 manifest: 3 file(s) in /scratch-local/mvanvugt.28750274/tmp.LkQEXyT2he/task_1/step6b_CETP.new.md5
[info]  2026-10-30 02:42:51 step6b_CETP: marvelous associate done, output to data/temp/validation/step6b/CETP
[info]  2026-10-30 02:42:51 *** END ***

```

## [10] slurm_script_step6b_PCSK9_new
- first run: 2026-10-30 04:22:13
- last run: 2026-10-30 04:22:13
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:53:23 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_PCSK9; mode: new; env: marvel_new
[info]  2026-10-29 23:53:23 working directory (temporary): /scratch-local/mvanvugt.28750287/tmp.XSKg8ozTJV/task_1
[info]  2026-10-29 23:53:23 manifest: 3 file(s) in /scratch-local/mvanvugt.28750287/tmp.XSKg8ozTJV/task_1/step6b_PCSK9.new.md5
[info]  2026-10-30 04:22:13 step6b_PCSK9: marvelous associate done, output to data/temp/validation/step6b/PCSK9
[info]  2026-10-30 04:22:13 *** END ***

```

## [10] slurm_script_step6b_vs_6_CETP_compare
- first run: 2026-10-30 08:05:12
- last run: 2026-10-30 12:36:37
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 12:36:34 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_vs_6_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 12:36:34 working directory (temporary): /scratch-local/mvanvugt.28771697/tmp.0W1y7WfBU4/task_1
[warn]  2026-10-30 12:36:34 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 12:36:34 manifest: 3 file(s) in /scratch-local/mvanvugt.28771697/tmp.0W1y7WfBU4/task_1/step6b_vs_6_CETP.compare.md5
[info]  2026-10-30 12:36:37 step6b_vs_6_CETP: GATE PASS
[info]  2026-10-30 12:36:37 *** END ***

```

## [10] slurm_script_step6b_vs_6_PCSK9_compare
- first run: 2026-10-30 08:10:06
- last run: 2026-10-30 12:34:53
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 12:34:49 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_vs_6_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 12:34:49 working directory (temporary): /scratch-local/mvanvugt.28771656/tmp.NN6T0eJ4T2/task_1
[warn]  2026-10-30 12:34:49 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 12:34:49 manifest: 3 file(s) in /scratch-local/mvanvugt.28771656/tmp.NN6T0eJ4T2/task_1/step6b_vs_6_PCSK9.compare.md5
[info]  2026-10-30 12:34:53 step6b_vs_6_PCSK9: GATE PASS
[info]  2026-10-30 12:34:53 *** END ***

```

## [10] slurm_script_step7_CETP_run
- first run: 2026-10-30 13:33:34
- last run: 2026-10-30 14:03:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 13:46:04 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_CETP; mode: run; env: marvel_new
[info]  2026-10-30 13:46:04 working directory (temporary): /scratch-local/mvanvugt.28773614/tmp.d8esNH2H3p/task_1
[info]  2026-10-30 13:46:04 manifest: 4 file(s) in /scratch-local/mvanvugt.28773614/tmp.d8esNH2H3p/task_1/step7_CETP.run.md5
[info]  2026-10-30 14:03:18 step7_CETP: marvelous run done, output to data/temp/validation/step7/CETP
[info]  2026-10-30 14:03:18 *** END ***

```

## [10] slurm_script_step7_PCSK9_run
- first run: 2026-10-30 13:54:37
- last run: 2026-10-30 13:54:37
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 13:33:27 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_PCSK9; mode: run; env: marvel_new
[info]  2026-10-30 13:33:27 working directory (temporary): /scratch-local/mvanvugt.28773218/tmp.kYE0UXsPXC/task_1
[info]  2026-10-30 13:33:27 manifest: 4 file(s) in /scratch-local/mvanvugt.28773218/tmp.kYE0UXsPXC/task_1/step7_PCSK9.run.md5
[info]  2026-10-30 13:54:37 step7_PCSK9: marvelous run done, output to data/temp/validation/step7/PCSK9
[info]  2026-10-30 13:54:37 *** END ***

```

## [10] slurm_script_step7_vs_6b_all_CETP_compare
- first run: 2026-10-30 14:16:19
- last run: 2026-10-30 14:16:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:16:16 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_all_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 14:16:16 working directory (temporary): /scratch-local/mvanvugt.28774465/tmp.CoRYxNTqjJ/task_1
[warn]  2026-10-30 14:16:16 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:16:16 manifest: 3 file(s) in /scratch-local/mvanvugt.28774465/tmp.CoRYxNTqjJ/task_1/step7_vs_6b_all_CETP.compare.md5
[info]  2026-10-30 14:16:18 step7_vs_6b_all_CETP: GATE PASS
[info]  2026-10-30 14:16:18 *** END ***

```

## [10] slurm_script_step7_vs_6b_all_PCSK9_compare
- first run: 2026-10-30 14:17:33
- last run: 2026-10-30 14:17:33
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:17:31 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_all_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 14:17:31 working directory (temporary): /scratch-local/mvanvugt.28774518/tmp.ZrFhEWv4dO/task_1
[warn]  2026-10-30 14:17:31 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:17:31 manifest: 3 file(s) in /scratch-local/mvanvugt.28774518/tmp.ZrFhEWv4dO/task_1/step7_vs_6b_all_PCSK9.compare.md5
[info]  2026-10-30 14:17:33 step7_vs_6b_all_PCSK9: GATE PASS
[info]  2026-10-30 14:17:33 *** END ***

```

## [10] slurm_script_step7_vs_6b_same_CETP_compare
- first run: 2026-10-30 14:08:36
- last run: 2026-10-30 14:08:36
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:08:34 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_same_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 14:08:34 working directory (temporary): /scratch-local/mvanvugt.28774267/tmp.FNiplcnPZV/task_1
[warn]  2026-10-30 14:08:34 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:08:34 manifest: 3 file(s) in /scratch-local/mvanvugt.28774267/tmp.FNiplcnPZV/task_1/step7_vs_6b_same_CETP.compare.md5
[info]  2026-10-30 14:08:36 step7_vs_6b_same_CETP: GATE PASS
[info]  2026-10-30 14:08:36 *** END ***

```

## [10] slurm_script_step7_vs_6b_same_PCSK9_compare
- first run: 2026-10-30 14:15:40
- last run: 2026-10-30 14:15:40
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:15:37 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_same_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 14:15:37 working directory (temporary): /scratch-local/mvanvugt.28774449/tmp.5Fm74vvc08/task_1
[warn]  2026-10-30 14:15:37 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:15:37 manifest: 3 file(s) in /scratch-local/mvanvugt.28774449/tmp.5Fm74vvc08/task_1/step7_vs_6b_same_PCSK9.compare.md5
[info]  2026-10-30 14:15:40 step7_vs_6b_same_PCSK9: GATE PASS
[info]  2026-10-30 14:15:40 *** END ***

```

## [10] slurm_script_step8a_chr1
- first run: 2026-10-30 16:09:12
- last run: 2026-10-30 16:09:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:08:31 keys: validation/configs/step8/8a_chr1.keys.txt; vcf: /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz; summary: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a/vep_chr1.variants.tsv.gz
[info]  2026-10-30 16:08:32 14 key(s) on chr1 (FASTA 1);
[info]  2026-10-30 16:09:12 0 matching record(s)
[info]  2026-10-30 16:09:12 all 14 key(s) agree with marvel

```

## [10] slurm_script_step8a_chr16
- first run: 2026-10-30 16:06:07
- last run: 2026-10-30 16:06:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:05:46 keys: validation/configs/step8/8a_chr16.keys.txt; vcf: /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz; summary: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a/vep_chr16.variants.tsv.gz
[info]  2026-10-30 16:05:46 4 key(s) on chr16 (FASTA 16);
[info]  2026-10-30 16:06:06 0 matching record(s)
[info]  2026-10-30 16:06:06 all 4 key(s) agree with marvel

```

## [10] slurm_script_step8a_vs_7_CETP_compare
- first run: 2026-10-30 16:25:33
- last run: 2026-10-30 16:25:33
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:25:30 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step8a_vs_7_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 16:25:30 working directory (temporary): /scratch-local/mvanvugt.28777684/tmp.cdwAvIi6mQ/task_1
[warn]  2026-10-30 16:25:30 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 16:25:30 manifest: 3 file(s) in /scratch-local/mvanvugt.28777684/tmp.cdwAvIi6mQ/task_1/step8a_vs_7_CETP.compare.md5
[info]  2026-10-30 16:25:32 step8a_vs_7_CETP: GATE PASS
[info]  2026-10-30 16:25:32 *** END ***

```

## [10] slurm_script_step8a_vs_7_PCSK9_compare
- first run: 2026-10-30 16:15:12
- last run: 2026-10-30 16:15:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:15:10 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step8a_vs_7_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 16:15:10 working directory (temporary): /scratch-local/mvanvugt.28777539/tmp.1Xg11vOrX7/task_1
[warn]  2026-10-30 16:15:10 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 16:15:10 manifest: 3 file(s) in /scratch-local/mvanvugt.28777539/tmp.1Xg11vOrX7/task_1/step8a_vs_7_PCSK9.compare.md5
[info]  2026-10-30 16:15:12 step8a_vs_7_PCSK9: GATE PASS
[info]  2026-10-30 16:15:12 *** END ***

```

## [10] slurm_script_step8b_chr1
- first run: 2026-10-30 16:13:09
- last run: 2026-10-30 16:13:09
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:11:10 keys: validation/configs/step8/8b_chr1.keys.txt; vcf: /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz; summary: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8b/vep_chr1.variants.tsv.gz
[info]  2026-10-30 16:11:11 86 key(s) on chr1 (FASTA 1);
[info]  2026-10-30 16:13:09 72 matching record(s)
[info]  2026-10-30 16:13:09 all 86 key(s) agree with marvel

```

## [10] slurm_script_step8b_vs_6b_PCSK9_compare
- first run: 2026-10-30 16:21:46
- last run: 2026-10-30 16:21:46
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:21:43 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step8b_vs_6b_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 16:21:43 working directory (temporary): /scratch-local/mvanvugt.28777599/tmp.oL7I9ElN4Y/task_1
[warn]  2026-10-30 16:21:43 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 16:21:43 manifest: 3 file(s) in /scratch-local/mvanvugt.28777599/tmp.oL7I9ElN4Y/task_1/step8b_vs_6b_PCSK9.compare.md5
[warn]  2026-10-30 16:21:46 step8b_vs_6b_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step8b_vs_6b_PCSK9/summary.tsv.gz
[info]  2026-10-30 16:21:46 *** END ***

```

## [10] slurm_script_step9_PCSK9_run
- first run: 2026-10-30 17:42:43
- last run: 2026-10-30 17:42:43
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 17:40:39 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_PCSK9; mode: run; env: marvel_new
[info]  2026-10-30 17:40:39 working directory (temporary): /scratch-local/mvanvugt.28779479/tmp.oc8isLBK7f/task_1
[info]  2026-10-30 17:40:39 manifest: 4 file(s) in /scratch-local/mvanvugt.28779479/tmp.oc8isLBK7f/task_1/step9_PCSK9.run.md5
[info]  2026-10-30 17:42:43 step9_PCSK9: marvelous run done, output to data/temp/validation/step9/PCSK9
[info]  2026-10-30 17:42:43 *** END ***

```

## [10] slurm_script_step9_vs_2_CETP_compare
- first run: 2026-10-30 22:06:20
- last run: 2026-10-30 22:06:20
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:06:17 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 22:06:17 working directory (temporary): /scratch-local/mvanvugt.28783671/tmp.bvmG0vIimr/task_1
[warn]  2026-10-30 22:06:17 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:06:17 manifest: 6 file(s) in /scratch-local/mvanvugt.28783671/tmp.bvmG0vIimr/task_1/step9_vs_2_CETP.compare.md5
[warn]  2026-10-30 22:06:20 step9_vs_2_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step9_vs_2_CETP/summary.tsv.gz
[info]  2026-10-30 22:06:20 *** END ***

```

## [10] slurm_script_step9_vs_2_PCSK9_compare
- first run: 2026-10-30 22:06:20
- last run: 2026-10-30 22:06:20
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:06:17 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 22:06:17 working directory (temporary): /scratch-local/mvanvugt.28783672/tmp.nBODhyoYtl/task_1
[warn]  2026-10-30 22:06:17 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:06:17 manifest: 6 file(s) in /scratch-local/mvanvugt.28783672/tmp.nBODhyoYtl/task_1/step9_vs_2_PCSK9.compare.md5
[warn]  2026-10-30 22:06:20 step9_vs_2_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step9_vs_2_PCSK9/summary.tsv.gz
[info]  2026-10-30 22:06:20 *** END ***

```

## [10] slurm_script_step9_vs_2_m1_CETP_compare
- first run: 2026-10-30 22:10:39
- last run: 2026-10-30 22:10:39
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:10:36 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_m1_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 22:10:36 working directory (temporary): /scratch-local/mvanvugt.28783714/tmp.BupLtZw9dT/task_1
[warn]  2026-10-30 22:10:36 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:10:36 manifest: 6 file(s) in /scratch-local/mvanvugt.28783714/tmp.BupLtZw9dT/task_1/step9_vs_2_m1_CETP.compare.md5
[info]  2026-10-30 22:10:39 step9_vs_2_m1_CETP: GATE PASS
[info]  2026-10-30 22:10:39 *** END ***

```

## [10] slurm_script_step9_vs_2_m1_PCSK9_compare
- first run: 2026-10-30 22:09:12
- last run: 2026-10-30 22:09:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:09:09 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_m1_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 22:09:09 working directory (temporary): /scratch-local/mvanvugt.28783695/tmp.bkNeaaR1OD/task_1
[warn]  2026-10-30 22:09:09 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:09:09 manifest: 6 file(s) in /scratch-local/mvanvugt.28783695/tmp.bkNeaaR1OD/task_1/step9_vs_2_m1_PCSK9.compare.md5
[info]  2026-10-30 22:09:12 step9_vs_2_m1_PCSK9: GATE PASS
[info]  2026-10-30 22:09:12 *** END ***

```

## [10] slurm_script_vep_prep_task1
- first run: 2026-10-22 04:22:14
- last run: 2026-11-10 10:09:38
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:45 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:45 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:46 task 1: chr 1, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr1.vcf.gz
[info]  2026-11-10 10:09:38 chr 1: 0

```

## [10] slurm_script_vep_prep_task2
- first run: 2026-10-22 04:22:17
- last run: 2026-11-10 10:08:18
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:46 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:46 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:47 task 2: chr 11, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr11_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr11.vcf.gz
[info]  2026-11-10 10:08:18 chr 11: 18

```

## [10] slurm_script_vep_prep_task3
- first run: 2026-10-22 04:22:15
- last run: 2026-11-10 10:13:25
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:46 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:46 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:47 task 3: chr 2, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr2_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr2.vcf.gz
[info]  2026-11-10 10:13:25 chr 2: 178

```

## [10] slurm_script_vep_prep_task4
- first run: 2026-10-22 04:22:19
- last run: 2026-11-10 10:08:26
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:46 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:46 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:47 task 4: chr 19, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr19_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr19.vcf.gz
[info]  2026-11-10 10:08:26 chr 19: 8

```

## [10] slurm_script_vep_prep_task5
- first run: 2026-10-22 04:22:14
- last run: 2026-11-10 10:09:14
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:46 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:46 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:46 task 5: chr 16, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr16.vcf.gz
[info]  2026-11-10 10:09:14 chr 16: 0

```

## [10] slurm_script_vep_prep_task6
- first run: 2026-10-22 04:22:26
- last run: 2026-11-10 10:09:08
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:47 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:47 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:48 task 6: chr 5, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr5_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr5.vcf.gz
[info]  2026-11-10 10:09:08 chr 5: 0

```

## [10] slurm_script_vep_prep_task7
- first run: 2026-10-22 04:22:22
- last run: 2026-11-10 10:09:39
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:47 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:47 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:49 task 7: chr 7, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr7_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr7.vcf.gz
[info]  2026-11-10 10:09:39 chr 7: 0

```

## [10] slurm_script_vep_prep_task8
- first run: 2026-10-22 04:22:13
- last run: 2026-11-10 10:08:36
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:07:48 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:07:48 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:07:50 task 8: chr 22, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr22_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr22.vcf.gz
[info]  2026-11-10 10:08:36 chr 22: 0

```

## [10] submit_two_source_submit_task1
- first run: 2026-10-21 21:41:00
- last run: 2026-11-10 10:05:37
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 10:05:24 env: /home/mvanvugt/mambaforge/envs/marvel_b2a948d
[info]  2026-11-10 10:05:24 stage: submit; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-11-10 10:05:33 5 plink gene VCF(s); chromosomes: 1 11 2 19 16 5 7 22
[info]  2026-11-10 10:05:37 submitted: J1 29058733, J2 29058734, J3 29058736, J4 29058745

```

## [10] subset_carriers (`validation/subset_carriers.py --carriers /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variant_extraction.tsv.gz --output /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/PCSK9_carriers.tsv.gz --region chr1:1-999999999 --drop-merged --negative-to-na --binary`)
- first run: 2026-10-26 16:12:11
- last run: 2026-10-29 23:50:53
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:36:35 chr1:1-999999999: 1047 of 1047 variant columns kept (0 merged names, drop_merged=True)
[info]  2026-10-29 23:50:52 wrote 469835 rows x 1048 columns to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/PCSK9_carriers.tsv.gz
[info]  2026-10-29 23:50:52 negative values written as NA: 2834 cells
[info]  2026-10-29 23:50:52 binary coding (> 0.5): 18 variant columns had values > 1, 1029 keys written to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/PCSK9_carriers.no_dose2.txt
[info]  2026-10-29 23:50:52 value counts over variant cells: {'0': 490839574, '1': 1074837, 'NA': 2834}

```

## [20] filter_gwas_cat (`/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /home/mvanvugt/projects/lipid_adem/data/temp/tasks.tsv --task-id 116 --step 1`)
- first run: 2026-09-21 22:58:26
- last run: 2026-10-27 13:37:06
- commit: `23ebede` (dirty)
- status: failed

Output:
```text
[info]  2026-10-27 13:37:06 rows 116-116 of 125, 8 gene regions

--- error output (raw) ---
[info]  2026-10-27 13:37:06 rows 116-116 of 125, 8 gene regions
Traceback (most recent call last):
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 385, in main
    run_task(args.tasks_file, args.task_id, args.step)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 308, in run_task
    run_filter(accession, source, outfile, regions, manifest_df)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 222, in run_filter
    filtered = _run_filter_finngen(study_accession, regions, manifest_df)
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 160, in _run_filter_finngen
    return functions.filter_sumstats_regions(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        tabix_source=url,
        ^^^^^^^^^^^^^^^^^
    ...<5 lines>...
        transform_to_maf=True,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/gpfs/home6/mvanvugt/projects/lipid_adem/src/functions.py", line 3410, in filter_sumstats_regions
    import pysam
ModuleNotFoundError: No module named 'pysam'
```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-10-27 13:37:07
- commit: `23ebede` (dirty)
- status: failed

Output:
```text
[info]  2026-10-27 13:37:03 task 116: rows 116-116
[error] 2026-10-27 13:37:06 run_mamba: '/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /home/mvanvugt/projects/lipid_adem/data/temp/tasks.tsv --task-id 116 --step 1' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-10-27 13:37:03 repo root=/home/mvanvugt/projects/lipid_adem
[info]  2026-10-27 13:37:03 === /home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.sh ===
[info]  2026-10-27 13:37:03 started at Tue Oct 27 13:37:03 CET 2026
[info]  2026-10-27 13:37:03 hostname=tcn36
[info]  2026-10-27 13:37:03 job array file=/home/mvanvugt/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-10-27 13:37:03 temp location=/scratch-local/mvanvugt.28623635
[info]  2026-10-27 13:37:03 step=1
[info]  2026-10-27 13:37:03 task 116: rows 116-116
[info]  2026-10-27 13:37:06 rows 116-116 of 125, 8 gene regions
```

## [20] var-annot (`/home/mvanvugt/mambaforge/envs/var_annot/bin/var-annot run --config /home/mvanvugt/projects/lipid_adem/config/var_annot.toml --force`)
- first run: 2026-11-11 14:21:25
- last run: 2026-11-11 22:48:06
- commit: `b030d0d` (dirty)

Δ vs previous run (was `25d4593` (dirty)):
```diff
@@ -1,6 +1,6 @@
-[info]  2026-11-11 22:14:18 config: /home/mvanvugt/software/var_annot/fn5_reruns/configs/lip_ac_rescue.toml
+[info]  2026-11-11 22:47:59 config: /home/mvanvugt/projects/lipid_adem/config/var_annot.toml
 [info]  2026-11-11 22:47:59 Reading ClinVar export /home/mvanvugt/projects/lipid_adem/data/raw/clinvar_variants.tsv
-[info]  2026-11-11 22:14:20 ClinVar: 313818 rows read, 14606 kept after classification and condition filters
+[info]  2026-11-11 22:48:01 ClinVar: 313818 rows read, 9922 kept after classification and condition filters
 [info]  2026-11-11 22:48:01 ClinVar APOB: 3 rows dropped (blank_assembly)
 [info]  2026-11-11 22:48:01 ClinVar: review stars from ac_review_status
 [info]  2026-11-11 22:48:01 ClinVar ANGPTL3: 23 rows dropped (no_vcf_coordinates)
@@ -12,7 +12,33 @@
 [info]  2026-11-11 22:48:01 ClinVar NPC1L1: 24 rows dropped (no_vcf_coordinates)
 [info]  2026-11-11 22:48:01 ClinVar PCSK9: 13 rows dropped (no_vcf_coordinates)
 [info]  2026-11-11 22:48:01 ClinVar PPARA: 82 rows dropped (no_vcf_coordinates)
-[warn]  2026-11-11 22:14:20 ClinVar: 80 kept rows are 'Conflicting classifications of pathogenicity' overall with a 0-star condition record (rcv_review_status); min_review_stars uses ac_review_status in ac mode (1 star for Conflicting), so use classification_column = "rcv_classification" with min_review_stars = 1 to drop them
-[info]  2026-11-11 22:14:20 ClinVar: 2136 rows, 391 unique variants
-[info]  2026-11-11 22:14:20 normalisation: unchanged=2136
-[info]  2026-11-11 22:14:20 Wrote 2136 rows to /home/mvanvugt/projects/lipid_adem/data/processed/fn5_reruns/lip_ac_rescue.tsv.gz
+[info]  2026-11-11 22:48:01 ClinVar: 1680 rows, 336 unique variants
+[info]  2026-11-11 22:48:01 Reading VEP TSV /home/mvanvugt/projects/lipid_adem/data/temp/vep_lipid_gene_csq.tsv.gz
+[info]  2026-11-11 22:48:01 VEP: 79163 variant x transcript rows read
+[info]  2026-11-11 22:48:01 VEP: 16068 rows pass transcript rule canonical
+[info]  2026-11-11 22:48:01 VEP set PTV: 527 rows
+[info]  2026-11-11 22:48:01 Reading AlphaMissense /projects/0/aus20644/data/resources/annotations/AlphaMissense_hg38.sorted.tsv.bgz
+[info]  2026-11-11 22:48:01 AM CETP: 439 sites kept (UniProt P11597)
+[info]  2026-11-11 22:48:01 AM HMGCR: 2623 sites kept (UniProt P04035)
+[info]  2026-11-11 22:48:02 AM NPC1L1: 2507 sites kept (UniProt Q9UHC9)
+[info]  2026-11-11 22:48:02 AM PCSK9: 737 sites kept (UniProt Q8NBP7)
+[info]  2026-11-11 22:48:02 AM ANGPTL3: 493 sites kept (UniProt Q9Y5C1)
+[info]  2026-11-11 22:48:02 AM PPARA: 1543 sites kept (UniProt Q07869)
+[info]  2026-11-11 22:48:02 AM APOA1: 536 sites kept (UniProt P02647)
+[info]  2026-11-11 22:48:02 AM APOB: 2952 sites kept (UniProt P04114)
+[info]  2026-11-11 22:48:02 AM: 11830 rows (likely_pathogenic)
+[info]  2026-11-11 22:48:02 Reading GoFcards /projects/0/aus20644/data/resources/annotations/gofcards_hg38.tsv.bgz
+[info]  2026-11-11 22:48:02 GoF CETP: 1 reports
+[info]  2026-11-11 22:48:02 GoF HMGCR: 0 reports
+[info]  2026-11-11 22:48:02 GoF NPC1L1: 0 reports
+[info]  2026-11-11 22:48:02 GoF PCSK9: 46 reports
+[info]  2026-11-11 22:48:02 GoF ANGPTL3: 0 reports
+[info]  2026-11-11 22:48:02 GoF PPARA: 0 reports
+[info]  2026-11-11 22:48:02 GoF APOA1: 1 reports
... 7 more line(s) omitted
```

Output:
```text
[info]  2026-11-11 22:47:59 config: /home/mvanvugt/projects/lipid_adem/config/var_annot.toml
[info]  2026-11-11 22:47:59 Reading ClinVar export /home/mvanvugt/projects/lipid_adem/data/raw/clinvar_variants.tsv
[info]  2026-11-11 22:48:01 ClinVar: 313818 rows read, 9922 kept after classification and condition filters
[info]  2026-11-11 22:48:01 ClinVar APOB: 3 rows dropped (blank_assembly)
[info]  2026-11-11 22:48:01 ClinVar: review stars from ac_review_status
[info]  2026-11-11 22:48:01 ClinVar ANGPTL3: 23 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar APOA1: 24 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar APOB: 22 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar APOE: 5 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar CETP: 21 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar HMGCR: 6 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar NPC1L1: 24 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar PCSK9: 13 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar PPARA: 82 rows dropped (no_vcf_coordinates)
[info]  2026-11-11 22:48:01 ClinVar: 1680 rows, 336 unique variants
[info]  2026-11-11 22:48:01 Reading VEP TSV /home/mvanvugt/projects/lipid_adem/data/temp/vep_lipid_gene_csq.tsv.gz
[info]  2026-11-11 22:48:01 VEP: 79163 variant x transcript rows read
[info]  2026-11-11 22:48:01 VEP: 16068 rows pass transcript rule canonical
[info]  2026-11-11 22:48:01 VEP set PTV: 527 rows
[info]  2026-11-11 22:48:01 Reading AlphaMissense /projects/0/aus20644/data/resources/annotations/AlphaMissense_hg38.sorted.tsv.bgz
[info]  2026-11-11 22:48:01 AM CETP: 439 sites kept (UniProt P11597)
[info]  2026-11-11 22:48:01 AM HMGCR: 2623 sites kept (UniProt P04035)
[info]  2026-11-11 22:48:02 AM NPC1L1: 2507 sites kept (UniProt Q9UHC9)
[info]  2026-11-11 22:48:02 AM PCSK9: 737 sites kept (UniProt Q8NBP7)
[info]  2026-11-11 22:48:02 AM ANGPTL3: 493 sites kept (UniProt Q9Y5C1)
[info]  2026-11-11 22:48:02 AM PPARA: 1543 sites kept (UniProt Q07869)
[info]  2026-11-11 22:48:02 AM APOA1: 536 sites kept (UniProt P02647)
[info]  2026-11-11 22:48:02 AM APOB: 2952 sites kept (UniProt P04114)
[info]  2026-11-11 22:48:02 AM: 11830 rows (likely_pathogenic)
[info]  2026-11-11 22:48:02 Reading GoFcards /projects/0/aus20644/data/resources/annotations/gofcards_hg38.tsv.bgz
[info]  2026-11-11 22:48:02 GoF CETP: 1 reports
[info]  2026-11-11 22:48:02 GoF HMGCR: 0 reports
[info]  2026-11-11 22:48:02 GoF NPC1L1: 0 reports
[info]  2026-11-11 22:48:02 GoF PCSK9: 46 reports
[info]  2026-11-11 22:48:02 GoF ANGPTL3: 0 reports
[info]  2026-11-11 22:48:02 GoF PPARA: 0 reports
[info]  2026-11-11 22:48:02 GoF APOA1: 1 reports
[info]  2026-11-11 22:48:02 GoF APOB: 0 reports
[info]  2026-11-11 22:48:02 GoF: 48 rows
[info]  2026-11-11 22:48:03 normalisation: unchanged=1680
[info]  2026-11-11 22:48:03 normalisation: normalised=18 unchanged=509
[info]  2026-11-11 22:48:05 normalisation: unchanged=11830
[info]  2026-11-11 22:48:05 normalisation: unchanged=48
[info]  2026-11-11 22:48:05 Wrote 14085 rows to /home/mvanvugt/projects/lipid_adem/data/processed/lipid_annotated_variants.tsv.gz

```

## [22] burden_exposure (`/home/mvanvugt/projects/lipid_adem/src/burden_exposure.py --summary`)
- first run: 2026-10-26 11:05:30
- last run: 2026-11-11 19:21:47
- commit: `25d4593` (dirty)

Output:
```text
[stage] 2026-11-11 19:20:58 summary lipid_burden_all_apoe
[info]  2026-11-11 19:20:58 lipid_burden_all_apoe.variants.tsv.gz: 1078 of 9136 sites read (found, swapped)
[warn]  2026-11-11 19:21:22 lipid_burden_all_apoe: no site read for PCSK9_clinvar, PCSK9_clinvar_directed
[stage] 2026-11-11 19:21:22 summary lipid_burden_fb_all_apoe
[info]  2026-11-11 19:21:22 lipid_burden_fb_all_apoe.variants.tsv.gz: 1077 of 9135 sites read (found, swapped)
[warn]  2026-11-11 19:21:47 lipid_burden_fb_all_apoe: no site read for PCSK9_clinvar_fb, PCSK9_clinvar_directed_fb
[info]  2026-11-11 19:21:47 wrote 167 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/burden_exposure_summary.tsv.gz

```

## [25] marvel_results_table (`src/marvel_results_table.py --ancestry MULTI`)
- first run: 2026-10-08 09:54:25
- last run: 2026-11-11 19:25:54
- commit: `25d4593` (dirty)

Output:
```text
[stage] 2026-11-11 19:25:46 store_runs
[info]  2026-11-11 19:25:47 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_runs.tsv: 7 runs to store
[info]  2026-11-11 19:25:47 lipid_variant_all_results.tsv.gz: unchanged
[info]  2026-11-11 19:25:48 lipid_variant_all_apoe_results.tsv.gz: unchanged
[info]  2026-11-11 19:25:49 lipid_variant_eur_results.tsv.gz: unchanged
[info]  2026-11-11 19:25:49 lipid_burden_all_apoe_results.tsv.gz: unchanged
[info]  2026-11-11 19:25:49 lipid_burden_eur_results.tsv.gz: unchanged
[warn]  2026-11-11 19:25:49 lipid_burden_fb_all_apoe_results.tsv.gz: other results; old store kept as lipid_burden_fb_all_apoe_results.20261111_192546.tsv.gz
[info]  2026-11-11 19:25:49 lipid_burden_fb_all_apoe_results.tsv.gz: written from /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel/lipid_burden_fb_all_apoe.results.tsv.gz
[warn]  2026-11-11 19:25:49 lipid_burden_fb_eur_results.tsv.gz: other results; old store kept as lipid_burden_fb_eur_results.20261111_192546.tsv.gz
[info]  2026-11-11 19:25:49 lipid_burden_fb_eur_results.tsv.gz: written from /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel/lipid_burden_fb_eur.results.tsv.gz
[stage] 2026-11-11 19:25:49 marvel_table
[info]  2026-11-11 19:25:50 lipid_variant_all: outcomes not in Marvel.UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-11-11 19:25:51 lipid_variant_all_apoe: outcomes not in Marvel.UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-11-11 19:25:53 lipid_variant_eur: outcomes not in Marvel.UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-11-11 19:25:53 wrote 210 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-11-11 19:25:53 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: all marvel strata already listed

```

## [27] compare_marvel_runs (`src/compare_marvel_runs.py --genes CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA`)
- first run: 2026-11-02 14:56:55
- last run: 2026-11-11 09:55:27
- commit: `e141a61` (dirty)

Output:
```text
[stage] 2026-11-11 09:53:57 variant lists
[warn]  2026-11-11 09:53:57 CETP: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv; NA
[info]  2026-11-11 09:53:57 CETP: 508 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv
[warn]  2026-11-11 09:53:57 HMGCR: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv; NA
[info]  2026-11-11 09:53:57 HMGCR: 2668 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[warn]  2026-11-11 09:53:57 NPC1L1: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv; NA
[info]  2026-11-11 09:53:57 NPC1L1: 2606 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[warn]  2026-11-11 09:53:57 PCSK9: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv; NA
[info]  2026-11-11 09:53:57 PCSK9: 831 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[warn]  2026-11-11 09:53:57 ANGPTL3: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv; NA
[info]  2026-11-11 09:53:57 ANGPTL3: 556 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[warn]  2026-11-11 09:53:57 PPARA: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv; NA
[info]  2026-11-11 09:53:57 PPARA: 1567 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv
[info]  2026-11-11 09:54:04 9158 variants in new list /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-11-11 09:54:09 CETP: 11328 overall variant rows in CETP_results.tsv.gz
[info]  2026-11-11 09:54:14 HMGCR: 10368 overall variant rows in HMGCR_results.tsv.gz
[info]  2026-11-11 09:54:21 NPC1L1: 24600 overall variant rows in NPC1L1_results.tsv.gz
[info]  2026-11-11 09:54:27 PCSK9: 14928 overall variant rows in PCSK9_results.tsv.gz
[info]  2026-11-11 09:54:29 ANGPTL3: 7680 overall variant rows in ANGPTL3_results.tsv.gz
[info]  2026-11-11 09:54:31 PPARA: 7200 overall variant rows in PPARA_results.tsv.gz
[info]  2026-11-11 09:54:31 chunk ukb_ANGPTL3_chr1_plink: 224 variant(s) read, 469835 samples
[info]  2026-11-11 09:54:33 chunk ukb_CETP_chr16_plink: 95 variant(s) read, 469835 samples
[info]  2026-11-11 09:54:34 chunk ukb_HMGCR_chr5_plink: 170 variant(s) read, 469835 samples
[info]  2026-11-11 09:54:34 chunk ukb_NPC1L1_chr7_plink: 270 variant(s) read, 469835 samples
[info]  2026-11-11 09:54:34 chunk ukb_PPARA_chr22_plink: 125 variant(s) read, 469835 samples
[info]  2026-11-11 09:54:35 chunk vep_chr1: 0 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:35 chunk vep_chr11: 18 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:35 chunk vep_chr16: 0 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:35 chunk vep_chr19: 8 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:36 chunk vep_chr2: 178 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:36 chunk vep_chr22: 0 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:36 chunk vep_chr5: 0 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:36 chunk vep_chr7: 0 variant(s) read, 377567 samples
[info]  2026-11-11 09:54:37 variant lists: 8736 old, 9168 new, old matched by {'exact': 8726, 'orig': 10}, 432 new only
[info]  2026-11-11 09:54:37 new extract status: {'not_found': 6649, 'allele_mismatch': 1420, 'found': 1098, 'indel_swap_blocked': 1}
[info]  2026-11-11 09:54:37 wrote 9168 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_comparison/variant_lists.tsv.gz
[stage] 2026-11-11 09:54:37 carriers
[info]  2026-11-11 09:54:38 CETP: 472 variant column(s) in CETP_variant_extraction.tsv.gz, 95 in the new list
[info]  2026-11-11 09:54:42 CETP: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-11 09:54:42 HMGCR: 432 variant column(s) in HMGCR_variant_extraction.tsv.gz, 170 in the new list
[info]  2026-11-11 09:54:48 HMGCR: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-11 09:54:48 NPC1L1: 1025 variant column(s) in NPC1L1_variant_extraction.tsv.gz, 267 in the new list
[info]  2026-11-11 09:55:03 NPC1L1: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-11 09:55:03 PCSK9: 622 variant column(s) in PCSK9_variant_extraction.tsv.gz, 131 in the new list
[info]  2026-11-11 09:55:12 PCSK9: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-11 09:55:12 ANGPTL3: 320 variant column(s) in ANGPTL3_variant_extraction.tsv.gz, 91 in the new list
[info]  2026-11-11 09:55:16 ANGPTL3: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-11 09:55:16 PPARA: 300 variant column(s) in PPARA_variant_extraction.tsv.gz, 124 in the new list
[info]  2026-11-11 09:55:20 PPARA: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-11 09:55:20 CETP: 95 variant(s), 0 with lost carriers; totals {'n_old_carriers': 504011, 'n_both': 504011, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-11 09:55:20 HMGCR: 170 variant(s), 0 with lost carriers; totals {'n_old_carriers': 406, 'n_both': 406, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-11 09:55:20 NPC1L1: 267 variant(s), 0 with lost carriers; totals {'n_old_carriers': 2423, 'n_both': 2423, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-11 09:55:20 PCSK9: 131 variant(s), 0 with lost carriers; totals {'n_old_carriers': 2491, 'n_both': 2491, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-11 09:55:20 ANGPTL3: 91 variant(s), 0 with lost carriers; totals {'n_old_carriers': 1672, 'n_both': 1672, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-11 09:55:20 PPARA: 124 variant(s), 0 with lost carriers; totals {'n_old_carriers': 1208, 'n_both': 1208, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-11 09:55:20 wrote 878 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_comparison/carriers.tsv.gz
[info]  2026-11-11 09:55:20 wrote 0 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_comparison/lost_carriers.tsv.gz
[stage] 2026-11-11 09:55:20 results
[info]  2026-11-11 09:55:20 0 strata_ref reference row(s) dropped
[info]  2026-11-11 09:55:23 219312 new overall variant rows in lipid_variant_all.results.tsv.gz
[info]  2026-11-11 09:55:23 results adjusted: 10203 joined rows, 7117 same sign, 111 with |z_diff| > 2; 118 old only, 99120 new only
[info]  2026-11-11 09:55:23 results unadjusted: 10213 joined rows, 6842 same sign, 105 with |z_diff| > 2; 108 old only, 99120 new only
[info]  2026-11-11 09:55:26 wrote 219312 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_comparison/results.tsv.gz

```

## [28] compare_results (`/gpfs/home6/mvanvugt/projects/lipid_adem/validation/compare_results.py --left validation/ref/61e2d7b/step10_variant_bin.results.tsv.gz --left-format new --right /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/f1a3a8a_variant_bin.results.tsv.gz --right-format new --rtol 1e-6 --out-dir /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1`)
- first run: 2026-10-26 11:32:16
- last run: 2026-11-04 15:31:04
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 15:30:56 step10_variant_bin.results.tsv.gz: 678395 rows, 244190 kept
[warn]  2026-11-04 15:30:56 left: 24398 duplicate key/outcome/model row(s), first kept
[info]  2026-11-04 15:30:56 left: 219792 rows, 9158 keys, outcomes ['Apolipoprotein A_i0', 'Apolipoprotein B_i0', 'HDL cholesterol_i0', 'LDL direct_i0', 'Triglycerides_i0', 'all_cause_dementia_algo', 'all_cause_dementia_combined', 'alzheimers_disease_algo', 'alzheimers_disease_combined', 'ascvd_ii', 'frontotemporal_dementia_algo', 'vascular_dementia_algo'], models ['adjusted', 'unadjusted']
[info]  2026-11-04 15:31:00 f1a3a8a_variant_bin.results.tsv.gz: 678395 rows, 244190 kept
[warn]  2026-11-04 15:31:00 right: 24398 duplicate key/outcome/model row(s), first kept
[info]  2026-11-04 15:31:00 right: 219792 rows, 9158 keys, outcomes ['Apolipoprotein A_i0', 'Apolipoprotein B_i0', 'HDL cholesterol_i0', 'LDL direct_i0', 'Triglycerides_i0', 'all_cause_dementia_algo', 'all_cause_dementia_combined', 'alzheimers_disease_algo', 'alzheimers_disease_combined', 'ascvd_ii', 'frontotemporal_dementia_algo', 'vascular_dementia_algo'], models ['adjusted', 'unadjusted']
[info]  2026-11-04 15:31:00 rows per class: {'identical': 219792}
[info]  2026-11-04 15:31:00 GATE PASS
[info]  2026-11-04 15:31:04 wrote 219792 rows to /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1/rows.tsv.gz
[info]  2026-11-04 15:31:04 wrote 168 rows to /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1/summary.tsv.gz

```

## [29] compare_carriers (`validation/compare_carriers.py --old-carriers /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/{gene}_carriers.tsv.gz --run-dir /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a --new-list validation/configs/validation_variants.tsv --genes CETP PCSK9 --out-dir validation/results/step8_carriers_8a --lost-out /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a_lost_carriers.tsv.gz`)
- first run: 2026-10-30 14:05:37
- last run: 2026-10-30 16:04:05
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:03:49 148 variants in new list validation/configs/validation_variants.tsv
[info]  2026-10-30 16:03:50 chunk ukb_CETP_chr16_plink: 58 variant(s) read, 469835 samples
[info]  2026-10-30 16:03:50 chunk ukb_PCSK9_chr1_plink: 72 variant(s) read, 469835 samples
[info]  2026-10-30 16:03:51 chunk vep_chr1: 0 variant(s) read, 377567 samples
[info]  2026-10-30 16:03:51 chunk vep_chr16: 0 variant(s) read, 377567 samples
[info]  2026-10-30 16:03:51 CETP: 472 variant column(s) in CETP_carriers.tsv.gz, 58 in the new list
[info]  2026-10-30 16:03:56 CETP: chunk ukb_CETP_chr16_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 CETP: chunk ukb_PCSK9_chr1_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 CETP: chunk vep_chr1: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 CETP: chunk vep_chr16: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 wrote 58 rows to validation/results/step8_carriers_8a/CETP.carriers.tsv.gz
[info]  2026-10-30 16:03:56 CETP: 58 compared key(s), 58 identical; match {'exact': 58}; 0 read key(s) without an old column
[info]  2026-10-30 16:03:56 CETP: carrier changes (summed over keys) {'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0, 'n_gained': 0, 'n_gained_old_missing': 0, 'n_gained_not_in_old': 0}
[info]  2026-10-30 16:03:56 PCSK9: 622 variant column(s) in PCSK9_carriers.tsv.gz, 72 in the new list
[info]  2026-10-30 16:04:04 PCSK9: chunk ukb_CETP_chr16_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:04 PCSK9: chunk ukb_PCSK9_chr1_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:05 PCSK9: chunk vep_chr1: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:05 PCSK9: chunk vep_chr16: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:05 wrote 72 rows to validation/results/step8_carriers_8a/PCSK9.carriers.tsv.gz
[info]  2026-10-30 16:04:05 PCSK9: 72 compared key(s), 72 identical; match {'exact': 72}; 0 read key(s) without an old column
[info]  2026-10-30 16:04:05 PCSK9: carrier changes (summed over keys) {'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0, 'n_gained': 0, 'n_gained_old_missing': 0, 'n_gained_not_in_old': 0}
[info]  2026-10-30 16:04:05 wrote 0 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a_lost_carriers.tsv.gz
[info]  2026-10-30 16:04:05 lost carrier IDs (individual-level) in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a_lost_carriers.tsv.gz

```

## [30] merge_associations (`/home/mvanvugt/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-11-11 20:05:16
- commit: `25d4593` (dirty)

Output:
```text
[stage] 2026-11-11 19:26:31 load_sumstats
[info]  2026-11-11 19:26:32 summary-stats: 125 files, 595475 rows incl. one copy per outcome (0 missing)
[info]  2026-11-11 19:26:39 MONDO_0011057 (all_cause_dementia) in Gwas.EXCLUDED_EFO_IDS, skipped
[info]  2026-11-11 19:26:39 MONDO_0011057 (vascular_dementia) in Gwas.EXCLUDED_EFO_IDS, skipped
[stage] 2026-11-11 19:26:39 marvel
[info]  2026-11-11 19:26:40 marvel ukb ascvd: 7056 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb ascvd: 61 rows with SE > 30.0 (separation) dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb ascvd: 10301 rows -> 8293 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb ascvd: 2008 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:40 marvel ukb all_cause_dementia: 7056 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb all_cause_dementia: 156 rows with SE > 30.0 (separation) dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb all_cause_dementia: 10206 rows -> 8198 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb all_cause_dementia: 2008 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:40 marvel ukb alzheimers_dementia: 7056 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb alzheimers_dementia: 194 rows with SE > 30.0 (separation) dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb alzheimers_dementia: 10168 rows -> 8160 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb alzheimers_dementia: 2008 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:40 marvel ukb vascular_dementia: 7056 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb vascular_dementia: 217 rows with SE > 30.0 (separation) dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb vascular_dementia: 10145 rows -> 8137 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb vascular_dementia: 2008 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:40 marvel ukb frontotemporal_dementia: 7056 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb frontotemporal_dementia: 239 rows with SE > 30.0 (separation) dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb frontotemporal_dementia: 10123 rows -> 8115 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:40 marvel ukb frontotemporal_dementia: 2008 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:41 marvel ukb apoa: 6498 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb apoa: 10208 rows -> 8416 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb apoa: 1792 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:41 marvel ukb apob: 6669 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb apob: 10237 rows -> 8397 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb apob: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:41 marvel ukb hdl_c: 6498 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb hdl_c: 10216 rows -> 8416 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb hdl_c: 1800 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:41 marvel ukb ldl_c: 6903 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb ldl_c: 10291 rows -> 8371 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb ldl_c: 1920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:41 marvel ukb tg: 6894 rows with < 5 exposed dropped (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb tg: 10292 rows -> 8372 variant rows, 0 gene-burden rows (lipid_variant_all_results.tsv.gz)
[info]  2026-11-11 19:26:41 marvel ukb tg: 1920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:44 marvel ukb ascvd: 756 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb ascvd: 5 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb ascvd: 9217 rows -> 9049 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb ascvd: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:44 marvel ukb all_cause_dementia: 756 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb all_cause_dementia: 7 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb all_cause_dementia: 9215 rows -> 9047 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb all_cause_dementia: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:44 marvel ukb alzheimers_dementia: 756 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:44 marvel ukb alzheimers_dementia: 10 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb alzheimers_dementia: 9212 rows -> 9044 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb alzheimers_dementia: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:45 marvel ukb vascular_dementia: 756 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb vascular_dementia: 16 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb vascular_dementia: 9206 rows -> 9038 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb vascular_dementia: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:45 marvel ukb frontotemporal_dementia: 756 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb frontotemporal_dementia: 18 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb frontotemporal_dementia: 9204 rows -> 9036 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb frontotemporal_dementia: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:45 marvel ukb apoa: 738 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb apoa: 9208 rows -> 9056 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:45 marvel ukb apoa: 152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:46 marvel ukb apob: 738 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:46 marvel ukb apob: 9224 rows -> 9056 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:46 marvel ukb apob: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:46 marvel ukb hdl_c: 738 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:46 marvel ukb hdl_c: 9208 rows -> 9056 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:46 marvel ukb hdl_c: 152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:46 marvel ukb ldl_c: 747 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:46 marvel ukb ldl_c: 9223 rows -> 9055 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:46 marvel ukb ldl_c: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:47 marvel ukb tg: 747 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb tg: 9223 rows -> 9055 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb tg: 168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:47 marvel ukb ascvd: 3402 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb ascvd: 16 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb ascvd: 9488 rows -> 8744 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb ascvd: 744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:47 marvel ukb all_cause_dementia: 3402 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb all_cause_dementia: 48 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb all_cause_dementia: 9456 rows -> 8712 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb all_cause_dementia: 744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:47 marvel ukb alzheimers_dementia: 3402 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:47 marvel ukb alzheimers_dementia: 63 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb alzheimers_dementia: 9441 rows -> 8697 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb alzheimers_dementia: 744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:48 marvel ukb vascular_dementia: 3402 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb vascular_dementia: 75 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb vascular_dementia: 9429 rows -> 8685 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb vascular_dementia: 744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:48 marvel ukb frontotemporal_dementia: 3402 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb frontotemporal_dementia: 89 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb frontotemporal_dementia: 9415 rows -> 8671 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb frontotemporal_dementia: 744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:48 marvel ukb apoa: 3168 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb apoa: 9426 rows -> 8786 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:48 marvel ukb apoa: 640 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:49 marvel ukb apob: 3186 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:49 marvel ukb apob: 9488 rows -> 8784 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:49 marvel ukb apob: 704 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:49 marvel ukb hdl_c: 3168 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:49 marvel ukb hdl_c: 9426 rows -> 8786 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:49 marvel ukb hdl_c: 640 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:49 marvel ukb ldl_c: 3294 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:49 marvel ukb ldl_c: 9484 rows -> 8772 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:49 marvel ukb ldl_c: 712 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:50 marvel ukb tg: 3285 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb tg: 9493 rows -> 8773 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb tg: 720 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:50 marvel ukb ascvd: 5643 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb ascvd: 43 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb ascvd: 9852 rows -> 8468 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb ascvd: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:50 marvel ukb all_cause_dementia: 5643 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb all_cause_dementia: 122 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb all_cause_dementia: 9773 rows -> 8389 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb all_cause_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:50 marvel ukb alzheimers_dementia: 5643 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb alzheimers_dementia: 154 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb alzheimers_dementia: 9741 rows -> 8357 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:50 marvel ukb alzheimers_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:51 marvel ukb vascular_dementia: 5643 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb vascular_dementia: 155 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb vascular_dementia: 9740 rows -> 8356 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb vascular_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:51 marvel ukb frontotemporal_dementia: 5643 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb frontotemporal_dementia: 165 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb frontotemporal_dementia: 9730 rows -> 8346 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb frontotemporal_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:51 marvel ukb apoa: 5175 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb apoa: 9835 rows -> 8563 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:51 marvel ukb apoa: 1272 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:52 marvel ukb apob: 5292 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:52 marvel ukb apob: 9862 rows -> 8550 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:52 marvel ukb apob: 1312 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:52 marvel ukb hdl_c: 5166 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:52 marvel ukb hdl_c: 9860 rows -> 8564 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:52 marvel ukb hdl_c: 1296 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:52 marvel ukb ldl_c: 5544 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:52 marvel ukb ldl_c: 9850 rows -> 8522 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:52 marvel ukb ldl_c: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:52 marvel ukb tg: 5526 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb tg: 9860 rows -> 8524 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb tg: 1336 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:53 marvel ukb ascvd: 2529 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb ascvd: 8 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb ascvd: 9313 rows -> 8849 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb ascvd: 464 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:53 marvel ukb all_cause_dementia: 2529 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb all_cause_dementia: 42 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb all_cause_dementia: 9279 rows -> 8815 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb all_cause_dementia: 464 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:53 marvel ukb alzheimers_dementia: 2529 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb alzheimers_dementia: 48 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb alzheimers_dementia: 9273 rows -> 8809 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:53 marvel ukb alzheimers_dementia: 464 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:54 marvel ukb vascular_dementia: 2529 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb vascular_dementia: 53 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb vascular_dementia: 9268 rows -> 8804 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb vascular_dementia: 464 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:54 marvel ukb frontotemporal_dementia: 2529 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb frontotemporal_dementia: 54 rows with SE > 30.0 (separation) dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb frontotemporal_dementia: 9267 rows -> 8803 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb frontotemporal_dementia: 464 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:54 marvel ukb apoa: 2295 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb apoa: 9307 rows -> 8883 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:54 marvel ukb apoa: 424 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:55 marvel ukb apob: 2304 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:55 marvel ukb apob: 9330 rows -> 8882 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:55 marvel ukb apob: 448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:55 marvel ukb hdl_c: 2304 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:55 marvel ukb hdl_c: 9306 rows -> 8882 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:55 marvel ukb hdl_c: 424 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:55 marvel ukb ldl_c: 2439 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:55 marvel ukb ldl_c: 9323 rows -> 8867 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:55 marvel ukb ldl_c: 456 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:55 marvel ukb tg: 2439 rows with < 5 exposed dropped (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:56 marvel ukb tg: 9323 rows -> 8867 variant rows, 0 gene-burden rows (lipid_variant_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:26:56 marvel ukb tg: 456 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:59 marvel ukb ascvd: 5445 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:26:59 marvel ukb ascvd: 46 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:26:59 marvel ukb ascvd: 10167 rows -> 8487 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:26:59 marvel ukb ascvd: 1680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:26:59 marvel ukb all_cause_dementia: 5445 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:26:59 marvel ukb all_cause_dementia: 135 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:26:59 marvel ukb all_cause_dementia: 10078 rows -> 8398 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:26:59 marvel ukb all_cause_dementia: 1680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:00 marvel ukb alzheimers_dementia: 5445 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb alzheimers_dementia: 163 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb alzheimers_dementia: 10050 rows -> 8370 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb alzheimers_dementia: 1680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:00 marvel ukb vascular_dementia: 5445 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb vascular_dementia: 182 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb vascular_dementia: 10031 rows -> 8351 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb vascular_dementia: 1680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:00 marvel ukb frontotemporal_dementia: 5445 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb frontotemporal_dementia: 199 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb frontotemporal_dementia: 10014 rows -> 8334 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:00 marvel ukb frontotemporal_dementia: 1680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:00 marvel ukb apoa: 5058 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:01 marvel ukb apoa: 10120 rows -> 8576 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:01 marvel ukb apoa: 1544 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:01 marvel ukb apob: 5094 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:01 marvel ukb apob: 10116 rows -> 8572 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:01 marvel ukb apob: 1544 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:01 marvel ukb hdl_c: 5058 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:01 marvel ukb hdl_c: 10128 rows -> 8576 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:01 marvel ukb hdl_c: 1552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:02 marvel ukb ldl_c: 5337 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb ldl_c: 10169 rows -> 8545 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb ldl_c: 1624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:02 marvel ukb tg: 5328 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb tg: 10170 rows -> 8546 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb tg: 1624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:02 marvel ukb ascvd: 684 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb ascvd: 4 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb ascvd: 9186 rows -> 9058 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:02 marvel ukb ascvd: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:03 marvel ukb all_cause_dementia: 684 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb all_cause_dementia: 8 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb all_cause_dementia: 9182 rows -> 9054 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb all_cause_dementia: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:03 marvel ukb alzheimers_dementia: 684 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb alzheimers_dementia: 10 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb alzheimers_dementia: 9180 rows -> 9052 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb alzheimers_dementia: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:03 marvel ukb vascular_dementia: 684 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb vascular_dementia: 9179 rows -> 9051 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:03 marvel ukb vascular_dementia: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:04 marvel ukb frontotemporal_dementia: 684 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb frontotemporal_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb frontotemporal_dementia: 9177 rows -> 9049 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb frontotemporal_dementia: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:04 marvel ukb apoa: 675 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb apoa: 9175 rows -> 9063 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb apoa: 112 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:04 marvel ukb apob: 666 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb apob: 9192 rows -> 9064 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:04 marvel ukb apob: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:05 marvel ukb hdl_c: 675 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:05 marvel ukb hdl_c: 9175 rows -> 9063 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:05 marvel ukb hdl_c: 112 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:05 marvel ukb ldl_c: 675 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:05 marvel ukb ldl_c: 9191 rows -> 9063 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:05 marvel ukb ldl_c: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:05 marvel ukb tg: 675 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:05 marvel ukb tg: 9191 rows -> 9063 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:05 marvel ukb tg: 128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:06 marvel ukb ascvd: 2817 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb ascvd: 12 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb ascvd: 9397 rows -> 8813 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb ascvd: 584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:06 marvel ukb all_cause_dementia: 2817 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb all_cause_dementia: 36 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb all_cause_dementia: 9373 rows -> 8789 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb all_cause_dementia: 584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:06 marvel ukb alzheimers_dementia: 2817 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb alzheimers_dementia: 47 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb alzheimers_dementia: 9362 rows -> 8778 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:06 marvel ukb alzheimers_dementia: 584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:07 marvel ukb vascular_dementia: 2817 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:07 marvel ukb vascular_dementia: 57 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:07 marvel ukb vascular_dementia: 9352 rows -> 8768 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:07 marvel ukb vascular_dementia: 584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:07 marvel ukb frontotemporal_dementia: 2817 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:07 marvel ukb frontotemporal_dementia: 69 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:07 marvel ukb frontotemporal_dementia: 9340 rows -> 8756 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:07 marvel ukb frontotemporal_dementia: 584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:07 marvel ukb apoa: 2637 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:08 marvel ukb apoa: 9357 rows -> 8845 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:08 marvel ukb apoa: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:08 marvel ukb apob: 2637 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:08 marvel ukb apob: 9397 rows -> 8845 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:08 marvel ukb apob: 552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:08 marvel ukb hdl_c: 2637 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:08 marvel ukb hdl_c: 9357 rows -> 8845 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:08 marvel ukb hdl_c: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:08 marvel ukb ldl_c: 2745 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb ldl_c: 9393 rows -> 8833 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb ldl_c: 560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:09 marvel ukb tg: 2736 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb tg: 9402 rows -> 8834 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb tg: 568 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:09 marvel ukb ascvd: 4428 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb ascvd: 34 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb ascvd: 9764 rows -> 8612 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb ascvd: 1152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:09 marvel ukb all_cause_dementia: 4428 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:09 marvel ukb all_cause_dementia: 103 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb all_cause_dementia: 9695 rows -> 8543 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb all_cause_dementia: 1152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:10 marvel ukb alzheimers_dementia: 4428 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb alzheimers_dementia: 128 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb alzheimers_dementia: 9670 rows -> 8518 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb alzheimers_dementia: 1152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:10 marvel ukb vascular_dementia: 4428 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb vascular_dementia: 128 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb vascular_dementia: 9670 rows -> 8518 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:10 marvel ukb vascular_dementia: 1152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:11 marvel ukb frontotemporal_dementia: 4428 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb frontotemporal_dementia: 136 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb frontotemporal_dementia: 9662 rows -> 8510 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb frontotemporal_dementia: 1152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:11 marvel ukb apoa: 4068 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb apoa: 9750 rows -> 8686 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb apoa: 1064 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:11 marvel ukb apob: 4077 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb apob: 9789 rows -> 8685 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:11 marvel ukb apob: 1104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:12 marvel ukb hdl_c: 4077 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:12 marvel ukb hdl_c: 9765 rows -> 8685 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:12 marvel ukb hdl_c: 1080 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:12 marvel ukb ldl_c: 4338 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:12 marvel ukb ldl_c: 9776 rows -> 8656 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:12 marvel ukb ldl_c: 1120 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:12 marvel ukb tg: 4320 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:12 marvel ukb tg: 9786 rows -> 8658 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:12 marvel ukb tg: 1128 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:13 marvel ukb ascvd: 1998 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb ascvd: 7 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb ascvd: 9309 rows -> 8909 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb ascvd: 400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:13 marvel ukb all_cause_dementia: 1998 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb all_cause_dementia: 37 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb all_cause_dementia: 9279 rows -> 8879 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb all_cause_dementia: 400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:13 marvel ukb alzheimers_dementia: 1998 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb alzheimers_dementia: 43 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb alzheimers_dementia: 9273 rows -> 8873 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:13 marvel ukb alzheimers_dementia: 400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:14 marvel ukb vascular_dementia: 1998 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb vascular_dementia: 46 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb vascular_dementia: 9270 rows -> 8870 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb vascular_dementia: 400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:14 marvel ukb frontotemporal_dementia: 1998 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb frontotemporal_dementia: 46 rows with SE > 30.0 (separation) dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb frontotemporal_dementia: 9270 rows -> 8870 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb frontotemporal_dementia: 400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:14 marvel ukb apoa: 1863 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb apoa: 9291 rows -> 8931 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:14 marvel ukb apoa: 360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:15 marvel ukb apob: 1818 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:15 marvel ukb apob: 9320 rows -> 8936 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:15 marvel ukb apob: 384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:15 marvel ukb hdl_c: 1872 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:15 marvel ukb hdl_c: 9290 rows -> 8930 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:15 marvel ukb hdl_c: 360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:15 marvel ukb ldl_c: 1953 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:15 marvel ukb ldl_c: 9313 rows -> 8921 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:15 marvel ukb ldl_c: 392 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb tg: 1953 rows with < 5 exposed dropped (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb tg: 9313 rows -> 8921 variant rows, 0 gene-burden rows (lipid_variant_eur_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb tg: 392 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 lipid_burden_all_apoe_results.tsv.gz: 7880 strata_ref reference row(s) dropped
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 724 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 10 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 563 rows -> 0 variant rows, 67 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 36 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 689 rows -> 0 variant rows, 65 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 716 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 18 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 630 rows -> 0 variant rows, 54 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb all_cause_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 724 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 560 rows -> 0 variant rows, 64 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 16 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 686 rows -> 0 variant rows, 62 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 45 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 684 rows -> 0 variant rows, 36 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 40 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 608 rows -> 0 variant rows, 32 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb alzheimers_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 16 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 722 rows -> 0 variant rows, 66 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 42 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 531 rows -> 0 variant rows, 35 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 36 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 29 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 673 rows -> 0 variant rows, 49 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 26 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 703 rows -> 0 variant rows, 55 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 52 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 596 rows -> 0 variant rows, 20 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb vascular_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 41 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 697 rows -> 0 variant rows, 41 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 61 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 512 rows -> 0 variant rows, 16 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 36 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 71 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 631 rows -> 0 variant rows, 7 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 47 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 682 rows -> 0 variant rows, 34 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 65 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 583 rows -> 0 variant rows, 7 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb frontotemporal_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 8 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 565 rows -> 0 variant rows, 69 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 36 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 6 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 696 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:16 marvel ukb ascvd: 2 rows with SE > 30.0 (separation) dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ascvd: 646 rows -> 0 variant rows, 70 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ascvd: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apoa: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apoa: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 573 rows -> 0 variant rows, 77 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apoa: 54 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 668 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apoa: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apoa: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apoa: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apob: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apob: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 573 rows -> 0 variant rows, 77 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apob: 18 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 704 rows -> 0 variant rows, 80 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apob: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb apob: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb apob: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 573 rows -> 0 variant rows, 77 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 54 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 668 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb hdl_c: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 573 rows -> 0 variant rows, 77 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 18 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 704 rows -> 0 variant rows, 80 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb ldl_c: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb tg: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb tg: 45 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 573 rows -> 0 variant rows, 77 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb tg: 18 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 704 rows -> 0 variant rows, 80 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb tg: 9 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb tg: 90 rows with < 5 exposed dropped (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb tg: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 lipid_burden_eur_results.tsv.gz: 7880 strata_ref reference row(s) dropped
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 724 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 10 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 554 rows -> 0 variant rows, 66 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 36 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 688 rows -> 0 variant rows, 64 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 716 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 20 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 628 rows -> 0 variant rows, 52 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:17 marvel ukb all_cause_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:17 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 724 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 551 rows -> 0 variant rows, 63 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 20 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 682 rows -> 0 variant rows, 58 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 45 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 684 rows -> 0 variant rows, 36 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 51 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 597 rows -> 0 variant rows, 21 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb alzheimers_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 19 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 719 rows -> 0 variant rows, 63 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 41 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 523 rows -> 0 variant rows, 35 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 36 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 33 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 669 rows -> 0 variant rows, 45 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 29 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 700 rows -> 0 variant rows, 52 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 53 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 595 rows -> 0 variant rows, 19 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb vascular_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 42 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 696 rows -> 0 variant rows, 40 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 60 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 504 rows -> 0 variant rows, 16 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 36 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 71 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 631 rows -> 0 variant rows, 7 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 50 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 679 rows -> 0 variant rows, 31 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 65 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 583 rows -> 0 variant rows, 7 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb frontotemporal_dementia: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 8 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 556 rows -> 0 variant rows, 68 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 36 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 6 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 696 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 2 rows with SE > 30.0 (separation) dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 646 rows -> 0 variant rows, 70 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ascvd: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apoa: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apoa: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 564 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apoa: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 668 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apoa: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apoa: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apoa: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apob: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apob: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 564 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apob: 18 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 704 rows -> 0 variant rows, 80 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apob: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb apob: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb apob: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 564 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 668 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb hdl_c: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 564 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 18 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 704 rows -> 0 variant rows, 80 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:18 marvel ukb ldl_c: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb tg: 738 rows -> 0 variant rows, 82 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb tg: 54 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 564 rows -> 0 variant rows, 76 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb tg: 18 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 704 rows -> 0 variant rows, 80 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 624 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb tg: 9 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 729 rows -> 0 variant rows, 81 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb tg: 90 rows with < 5 exposed dropped (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 648 rows -> 0 variant rows, 72 gene-burden rows (lipid_burden_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb tg: 576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 lipid_burden_fb_all_apoe_results.tsv.gz: 780 strata_ref reference row(s) dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 715 rows -> 0 variant rows, 67 gene-burden rows (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 45 rows with < 5 exposed dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 551 rows -> 0 variant rows, 63 gene-burden rows (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 16 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 677 rows -> 0 variant rows, 61 gene-burden rows (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 616 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 9 rows with < 5 exposed dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 45 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 675 rows -> 0 variant rows, 35 gene-burden rows (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 640 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 90 rows with < 5 exposed dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 40 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 599 rows -> 0 variant rows, 31 gene-burden rows (lipid_burden_fb_all_apoe_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 568 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 lipid_burden_fb_eur_results.tsv.gz: 780 strata_ref reference row(s) dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 715 rows -> 0 variant rows, 67 gene-burden rows (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 54 rows with < 5 exposed dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 13 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 542 rows -> 0 variant rows, 62 gene-burden rows (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 480 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 20 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 673 rows -> 0 variant rows, 57 gene-burden rows (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 616 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 9 rows with < 5 exposed dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 45 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 675 rows -> 0 variant rows, 35 gene-burden rows (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 640 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 90 rows with < 5 exposed dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 51 rows with SE > 30.0 (separation) dropped (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 588 rows -> 0 variant rows, 20 gene-burden rows (lipid_burden_fb_eur_results.tsv.gz)
[info]  2026-11-11 19:27:19 marvel ukb alzheimers_dementia: 568 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-11-11 19:27:19 fetch_curated
[info]  2026-11-11 19:28:47 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1
[info]  2026-11-11 19:28:48 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-11-11 19:28:53 MONDO_0013792 (exact): 42 fetched; in region: none
[info]  2026-11-11 19:28:57 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-11-11 19:29:21 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-11-11 19:29:42 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6
[info]  2026-11-11 19:29:44 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-11-11 19:29:49 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-11-11 19:35:22 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3
[info]  2026-11-11 19:35:30 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-11-11 19:35:31 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-11-11 19:35:32 EFO_0009493 (exact): 3 fetched; in region: none
[warn]  2026-11-11 19:52:01 GWAS Catalog associations MONDO_0004975: ConnectionError, retry 1/3 in 30s
[info]  2026-11-11 20:02:54 MONDO_0004975 (with child traits): 7149 fetched; in region: APOB=1
[info]  2026-11-11 20:03:03 MONDO_0004648 (with child traits): 117 fetched; in region: none
[info]  2026-11-11 20:03:07 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-11-11 20:03:09 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-11-11 20:03:10 EFO ids with 0 curated associations: 4
[stage] 2026-11-11 20:03:10 gene_burden
[info]  2026-11-11 20:03:10 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-11-11 20:03:11 curated MAF: numeric=58 not_reported=28
[info]  2026-11-11 20:03:11 curated: 54 rows dropped from studies excluded for cohort overlap
[info]  2026-11-11 20:03:11 gene-burden rows: none (8 genes with 0)
[info]  2026-11-11 20:03:15 ancestry: 0 rows of studies not in the discovery log labelled NR
[info]  2026-11-11 20:03:16 ancestry: curated EAS=21
[info]  2026-11-11 20:03:16 ancestry: curated EUR=26
[info]  2026-11-11 20:03:16 ancestry: curated MULTI=21
[info]  2026-11-11 20:03:16 ancestry: curated NR=18
[info]  2026-11-11 20:03:16 ancestry: gene-burden EUR=3440
[info]  2026-11-11 20:03:16 ancestry: gene-burden MULTI=3497
[info]  2026-11-11 20:03:16 ancestry: summary-stats AFR=159854
[info]  2026-11-11 20:03:16 ancestry: summary-stats AMR=73617
[info]  2026-11-11 20:03:16 ancestry: summary-stats CSA=43677
[info]  2026-11-11 20:03:16 ancestry: summary-stats EAS=45135
[info]  2026-11-11 20:03:16 ancestry: summary-stats EUR=578357
[info]  2026-11-11 20:03:16 ancestry: summary-stats MULTI=561366
[info]  2026-11-11 20:03:16 ancestry: summary-stats NR=5898
[stage] 2026-11-11 20:03:16 effect_scale
[info]  2026-11-11 20:03:19 wrote 216 studies to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-11-11 20:03:20 study effect scale: linear=52, log_or=112, unknown=52
[stage] 2026-11-11 20:03:20 normalise
[info]  2026-11-11 20:03:24 normalisation: summary-stats rows unchanged=1424640 no_sequence=40564 ref_mismatch=2699 normalised=1
[info]  2026-11-11 20:03:24 normalisation: curated rows effect_only=86
[stage] 2026-11-11 20:03:25 ensembl_check
[info]  2026-11-11 20:03:25 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:25 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:25 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:25 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:26 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:26 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:26 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:26 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-11-11 20:03:29 Ensembl check: 29714 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-11-11 20:03:33 summary-stats rows: alleles match=564740 not_found=553524 mismatch=213266 flipped=135906 strand_flip=468; rsid same=523657 no_source_rsid=346376 rsid_only=41315 different=3032
[info]  2026-11-11 20:03:33 curated rows: alleles match=33 flipped=28 effect_unknown=25; rsid same=86
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_all_cause_dementia: 88% of 8398 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_all_cause_dementia_e22_e32: 87% of 8879 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_all_cause_dementia_e33: 88% of 8543 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_all_cause_dementia_e43: 87% of 8789 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_all_cause_dementia_e44: 86% of 9054 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_alzheimers_dementia: 88% of 8370 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_alzheimers_dementia_e22_e32: 87% of 8873 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_alzheimers_dementia_e33: 88% of 8518 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_alzheimers_dementia_e43: 87% of 8778 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_alzheimers_dementia_e44: 86% of 9052 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apoa: 87% of 8576 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apoa_e22_e32: 87% of 8931 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apoa_e33: 87% of 8686 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apoa_e43: 87% of 8845 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apoa_e44: 86% of 9063 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apob: 87% of 8572 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apob_e22_e32: 87% of 8936 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apob_e33: 87% of 8685 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apob_e43: 87% of 8845 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_apob_e44: 86% of 9064 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ascvd: 87% of 8487 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ascvd_e22_e32: 87% of 8909 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ascvd_e33: 87% of 8612 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ascvd_e43: 87% of 8813 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ascvd_e44: 86% of 9058 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_frontotemporal_dementia: 89% of 8334 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_frontotemporal_dementia_e22_e32: 87% of 8870 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_frontotemporal_dementia_e33: 88% of 8510 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_frontotemporal_dementia_e43: 88% of 8756 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_frontotemporal_dementia_e44: 86% of 9049 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_hdl_c: 87% of 8576 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_hdl_c_e22_e32: 87% of 8930 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_hdl_c_e33: 87% of 8685 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_hdl_c_e43: 87% of 8845 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_hdl_c_e44: 86% of 9063 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ldl_c: 87% of 8545 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ldl_c_e22_e32: 87% of 8921 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ldl_c_e33: 87% of 8656 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ldl_c_e43: 87% of 8833 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_ldl_c_e44: 86% of 9063 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_tg: 87% of 8546 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_tg_e22_e32: 87% of 8921 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_tg_e33: 87% of 8658 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_tg_e43: 87% of 8834 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_tg_e44: 86% of 9063 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_vascular_dementia: 88% of 8351 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_vascular_dementia_e22_e32: 87% of 8870 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_vascular_dementia_e33: 88% of 8518 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_vascular_dementia_e43: 87% of 8768 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_EUR_vascular_dementia_e44: 86% of 9051 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_all_cause_dementia: 89% of 8198 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_all_cause_dementia_e22_e32: 88% of 8815 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_all_cause_dementia_e33: 89% of 8389 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_all_cause_dementia_e43: 88% of 8712 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_all_cause_dementia_e44: 86% of 9047 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_alzheimers_dementia: 89% of 8160 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_alzheimers_dementia_e22_e32: 88% of 8809 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_alzheimers_dementia_e33: 89% of 8357 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_alzheimers_dementia_e43: 88% of 8697 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_alzheimers_dementia_e44: 86% of 9044 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apoa: 88% of 8416 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apoa_e22_e32: 87% of 8883 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apoa_e33: 88% of 8563 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apoa_e43: 87% of 8786 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apoa_e44: 86% of 9056 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apob: 88% of 8397 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apob_e22_e32: 87% of 8882 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apob_e33: 88% of 8550 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apob_e43: 87% of 8784 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_apob_e44: 86% of 9056 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ascvd: 88% of 8293 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ascvd_e22_e32: 87% of 8849 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ascvd_e33: 88% of 8468 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ascvd_e43: 87% of 8744 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ascvd_e44: 86% of 9049 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_frontotemporal_dementia: 90% of 8115 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_frontotemporal_dementia_e22_e32: 88% of 8803 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_frontotemporal_dementia_e33: 89% of 8346 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_frontotemporal_dementia_e43: 88% of 8671 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_frontotemporal_dementia_e44: 86% of 9036 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_hdl_c: 88% of 8416 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_hdl_c_e22_e32: 87% of 8882 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_hdl_c_e33: 88% of 8564 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_hdl_c_e43: 87% of 8786 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_hdl_c_e44: 86% of 9056 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ldl_c: 88% of 8371 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ldl_c_e22_e32: 87% of 8867 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ldl_c_e33: 88% of 8522 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ldl_c_e43: 87% of 8772 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_ldl_c_e44: 86% of 9055 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_tg: 88% of 8372 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_tg_e22_e32: 87% of 8867 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_tg_e33: 88% of 8524 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_tg_e43: 87% of 8773 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_tg_e44: 86% of 9055 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_vascular_dementia: 90% of 8137 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_vascular_dementia_e22_e32: 88% of 8804 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_vascular_dementia_e33: 89% of 8356 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_vascular_dementia_e43: 88% of 8685 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-11-11 20:03:33 summary-stats marvel_ukb_MULTI_vascular_dementia_e44: 86% of 9038 rows not_found/mismatch in Ensembl (GRCh37 file?)
[info]  2026-11-11 20:03:37 duplicate variants flagged: 766 rows
[stage] 2026-11-11 20:03:37 write
[info]  2026-11-11 20:05:15 wrote 1474927 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-11-11 20:05:17
- commit: `25d4593` (dirty)

Output:
```text
[info]  2026-11-11 19:26:27 using root directory: /home/mvanvugt/projects/lipid_adem

```

## [40] clinvar_filter (`mamba run --no-capture-output -n clinvar-build clinvar-filter /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_vcv.db --rcv-db /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_rcv.db -g gene CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA APOA1 APOB APOE -o /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv -vvv`)
- first run: 2026-10-06 17:09:48
- last run: 2026-10-06 17:09:48
- commit: `7e96ca6` (dirty)

Output:
```text
2026-10-06 17:09:48,842 - INFO - Wrote 313818 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
```

## [40] match_variants (`src/match_variants.py`)
- first run: 2026-10-01 09:59:12
- last run: 2026-11-11 21:58:01
- commit: `25d4593` (dirty)

Output:
```text
[stage] 2026-11-11 21:54:17 load_variant_lists
[info]  2026-11-11 21:54:17 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv: 9227 rows
[info]  2026-11-11 21:54:17 0 duplicate rows removed
[info]  2026-11-11 21:54:17 ANGPTL3 AM: 493 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 ANGPTL3 ClinVar: 12 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 ANGPTL3 PTV: 56 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 APOA1 ClinVar: 33 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 APOA1 PTV: 15 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 APOB ClinVar: 236 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 APOB PTV: 172 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 APOE ClinVar: 20 rows, 0 without alleles, 20 outside gene region
[info]  2026-11-11 21:54:17 CETP AM: 439 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 CETP ClinVar: 10 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 CETP PTV: 58 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 CETP SelectedGoF: 3 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 HMGCR AM: 2623 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 HMGCR ClinVar: 7 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 HMGCR PTV: 39 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 NPC1L1 AM: 2507 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 NPC1L1 PTV: 96 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 PCSK9 AM: 737 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 PCSK9 ClinVar: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 PCSK9 PTV: 68 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 PPARA AM: 1543 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 PPARA PTV: 23 rows, 0 without alleles, 0 outside gene region
[info]  2026-11-11 21:54:17 normalisation: variant-list rows unchanged=9207 no_sequence=20
[stage] 2026-11-11 21:54:17 load_gwas
[info]  2026-11-11 21:55:35 /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz: 1474927 rows, 1467990 variant-level (summary-stats, curated)
[info]  2026-11-11 21:55:37 wrote 6937 marvel gene-burden rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_burden.tsv.gz
[info]  2026-11-11 21:55:49 curated: 25 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-11-11 21:56:22 match
[info]  2026-11-11 21:56:58 ANGPTL3 AM: 493 variants, 493 matched, GWAS rows: summary-stats=48081
[info]  2026-11-11 21:56:58 ANGPTL3 ClinVar: 12 variants, 12 matched, GWAS rows: summary-stats=989
[info]  2026-11-11 21:56:59 ANGPTL3 PTV: 56 variants, 56 matched, GWAS rows: summary-stats=3371
[info]  2026-11-11 21:56:59 APOA1 ClinVar: 33 variants, 33 matched, GWAS rows: summary-stats=3360
[info]  2026-11-11 21:56:59 APOA1 PTV: 15 variants, 15 matched, GWAS rows: summary-stats=1136
[info]  2026-11-11 21:56:59 APOB ClinVar: 236 variants, 236 matched, GWAS rows: summary-stats=22235
[info]  2026-11-11 21:56:59 APOB PTV: 172 variants, 172 matched, GWAS rows: summary-stats=11716
[info]  2026-11-11 21:57:00 APOE ClinVar: 20 variants, 1 matched, GWAS rows: summary-stats=16
[info]  2026-11-11 21:57:00 CETP AM: 439 variants, 439 matched, GWAS rows: summary-stats=42610
[info]  2026-11-11 21:57:00 CETP ClinVar: 10 variants, 10 matched, GWAS rows: summary-stats=823
[info]  2026-11-11 21:57:00 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=306
[info]  2026-11-11 21:57:00 CETP PTV: 58 variants, 58 matched, GWAS rows: summary-stats=3671
[info]  2026-11-11 21:57:00 CETP SelectedGoF: 3 variants, 3 matched, GWAS rows: summary-stats=971
[info]  2026-11-11 21:57:02 HMGCR AM: 2623 variants, 2623 matched, GWAS rows: summary-stats=257449
[info]  2026-11-11 21:57:02 HMGCR ClinVar: 7 variants, 7 matched, GWAS rows: summary-stats=510
[info]  2026-11-11 21:57:02 HMGCR PTV: 39 variants, 39 matched, GWAS rows: summary-stats=2337
[info]  2026-11-11 21:57:03 NPC1L1 AM: 2507 variants, 2507 matched, GWAS rows: summary-stats=244485
[info]  2026-11-11 21:57:03 NPC1L1 PTV: 96 variants, 96 matched, GWAS rows: summary-stats=5983
[info]  2026-11-11 21:57:03 PCSK9 AM: 737 variants, 737 matched, GWAS rows: summary-stats=71723
[info]  2026-11-11 21:57:03 PCSK9 ClinVar: 18 variants, 18 matched, GWAS rows: summary-stats=1726
[info]  2026-11-11 21:57:04 PCSK9 GoF: 18 variants, 18 matched, GWAS rows: summary-stats=1702
[info]  2026-11-11 21:57:04 PCSK9 PTV: 68 variants, 68 matched, GWAS rows: summary-stats=4309
[info]  2026-11-11 21:57:04 PPARA AM: 1543 variants, 1543 matched, GWAS rows: summary-stats=150271
[info]  2026-11-11 21:57:05 PPARA PTV: 23 variants, 23 matched, GWAS rows: summary-stats=1360
[warn]  2026-11-11 21:57:06 a1 vs Ensembl ref: 303510 matched SNV rows checked, 7860 where a1 is not the Ensembl ref (e.g. 1:62598754:AA:A, 1:62598776:-:ATGGATTTGAAAAAT, 1:62604076:-:AAGAAAAGTTTTAAAAATCTGTGAGT)
[stage] 2026-11-11 21:57:06 write
[info]  2026-11-11 21:58:01 wrote 881140 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_variants.tsv.gz

```

## [50] annotate_variants (`/Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/src/annotate_variants.py`)
- first run: 2026-10-06 17:13:43
- last run: 2026-10-16 13:14:40
- commit: `c91df4d` (dirty)

Output:
```text
[info]  2026-10-16 13:14:39 Reading ClinVar variants from /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
[info]  2026-10-16 13:14:39 Read 313818 rows
[info]  2026-10-16 13:14:39 9922 rows have an aggregate P/LP ac_classification; 3 of them without an assembly dropped
[info]  2026-10-16 13:14:39 Kept 9919 rows after filtering
[info]  2026-10-16 13:14:39 Review-status scope-reduction summary:
                                                                                                                         scope  n_unique_variants  n_variants_removed_cumulative  n_variants_removed_this_step
                                                                                     All review statuses (every tier included)                549                              0                             0
Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts + criteria provided, single submitter                482                             67                            67
                                      Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts                249                            300                           233
                                                                                             Include: reviewed by expert panel                218                            331                            31
[info]  2026-10-16 13:14:39 Wrote review-status summary to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/pah_variants_review_status_summary.tsv
[info]  2026-10-16 13:14:39 Widened 3648 assembly-duplicated rows into 1900 variant/condition rows
[info]  2026-10-16 13:14:39 549 unique variants identified
[info]  2026-10-16 13:14:39 Writing 1900 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/plp_variants.tsv

```

## [50] marvel_assoc_job
- first run: 2026-10-07 13:49:03
- last run: 2026-10-29 18:19:29
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:36:27 task 1: rows 1-1
[info]  2026-10-29 18:19:29 PCSK9: results in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step4b7/PCSK9

```

## [50] meta_analysis (`/home/mvanvugt/projects/lipid_adem/src/meta_analysis.py --ancestry MULTI --variant-sources SelectedGoF --stratified --label selected_gof_multi --no-gene-burden --require-expected-scale`)
- first run: 2026-10-01 10:26:24
- last run: 2026-11-11 22:32:19
- commit: `25d4593` (dirty)

Output:
```text
[info]  2026-11-11 22:31:37 ancestry MULTI, pooled by variant_site, outcome, ancestry_group
[stage] 2026-11-11 22:31:37 load_matched
[info]  2026-11-11 22:31:57 /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_variants.tsv.gz: 881140 rows, 9139 variants
[info]  2026-11-11 22:31:57 16 rows of excluded gene(s) APOE dropped
[info]  2026-11-11 22:32:04 881124 of 881124 rows kept (MULTI pools every ancestry) (all: AFR=465, AMR=194, CSA=1370, EAS=204, EUR=441944, MULTI=436923, NR=24)
[info]  2026-11-11 22:32:05 MULTI: 881124 rows pooled across ancestries (AFR=465, AMR=194, CSA=1370, EAS=204, EUR=441944, MULTI=436923, NR=24), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
[stage] 2026-11-11 22:32:05 effect_scale
[warn]  2026-11-11 22:32:05 GCST90276157: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90276158: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apoa: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apoa_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apoa_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apoa_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apoa_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apob: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apob_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apob_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apob_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_apob_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_hdl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_hdl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_hdl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_hdl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_hdl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_ldl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_ldl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_ldl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_ldl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_ldl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_tg: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_tg_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_tg_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_tg_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_EUR_tg_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apoa: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apoa_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apoa_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apoa_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apoa_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apob: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apob_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apob_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apob_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_apob_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_hdl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_hdl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_hdl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_hdl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_hdl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_ldl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_ldl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_ldl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_ldl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_ldl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_tg: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_tg_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_tg_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_tg_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 marvel_ukb_MULTI_tg_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST002245: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST005195: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90014122: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90014123: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90475198: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90475199: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90475933: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90475987: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476370: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476592: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476593: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476594: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476595: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476621: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476622: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90476623: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477866: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477867: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477928: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477929: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477937: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477938: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477939: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477941: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477942: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477943: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477944: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477958: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477959: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477976: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477977: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90477978: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90479542: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90479543: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480131: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480173: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480174: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480187: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480188: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480191: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90480807: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90481154: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-11-11 22:32:05 GCST90481158: effect scale unknown, not log-OR; kept (--require-log-or drops)
[info]  2026-11-11 22:32:05 GCST002245: 8 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST005195: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90014122: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90014123: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90276157: 4 rows on scale linear, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90276158: 8 rows on scale linear, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90475198: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90475199: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90475933: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90475987: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476370: 10 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476592: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476593: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476594: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476595: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476621: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476622: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90476623: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477866: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477867: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477928: 6 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477929: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477937: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477938: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477939: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477941: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477942: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477943: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477944: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477958: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477959: 20 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477976: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477977: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90477978: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90479542: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90479543: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480131: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480173: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480174: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480187: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480188: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480191: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90480807: 18 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90481154: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 GCST90481158: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-11-11 22:32:05 --require-expected-scale: 1187 of 881124 rows of 45 studies dropped
[stage] 2026-11-11 22:32:11 prepare_effects
[info]  2026-11-11 22:32:14 870565 rows dropped: no beta or odds ratio
[info]  2026-11-11 22:32:15 9372 usable rows, 0 with SE derived from p
[stage] 2026-11-11 22:32:15 resolve_ambiguous
[stage] 2026-11-11 22:32:15 orient
[info]  2026-11-11 22:32:15 257 variants oriented as a2
[info]  2026-11-11 22:32:15 13 variants oriented as a2_gof_flipped
[info]  2026-11-11 22:32:15 APOA1, PPARA: flipped to the therapeutic direction (drugs raise gene function)
[info]  2026-11-11 22:32:15 26 ClinVar variants with direction lowering
[info]  2026-11-11 22:32:15 2 ClinVar variants with direction conflicting
[info]  2026-11-11 22:32:15 1 ClinVar variants with direction raising
[info]  2026-11-11 22:32:15 1 ClinVar variants with direction altered
[info]  2026-11-11 22:32:15 variant_list_source in SelectedGoF: 587 of 9372 rows kept
[stage] 2026-11-11 22:32:15 apoe_strata
[info]  2026-11-11 22:32:15 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: 104 studies with an APOE stratum entry
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_all_cause_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_all_cause_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_all_cause_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_all_cause_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_alzheimers_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apoa, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apoa, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apoa, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apoa, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apoa, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apob, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apob, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apob, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apob, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_apob, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ascvd, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ascvd, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ascvd, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ascvd, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ascvd, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_hdl_c, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_hdl_c, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_hdl_c, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_hdl_c, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_hdl_c, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ldl_c, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ldl_c, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ldl_c, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ldl_c, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_ldl_c, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_tg, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_tg, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_tg, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_tg, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_tg, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_vascular_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_vascular_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_vascular_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_EUR_vascular_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_all_cause_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_all_cause_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_all_cause_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_all_cause_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_alzheimers_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apoa, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apoa, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apoa, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apoa, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apoa, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apob, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apob, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apob, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apob, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_apob, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ascvd, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ascvd, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ascvd, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ascvd, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ascvd, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_hdl_c, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_hdl_c, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_hdl_c, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_hdl_c, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_hdl_c, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ldl_c, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ldl_c, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ldl_c, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ldl_c, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_ldl_c, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_tg, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_tg, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_tg, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_tg, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_tg, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_vascular_dementia, stratum all: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_vascular_dementia, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_vascular_dementia, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group marvel_ukb_MULTI_vascular_dementia, stratum e44: 1 studies
[info]  2026-11-11 22:32:15 study group thomassen, stratum e22_e32: 1 studies
[info]  2026-11-11 22:32:15 study group thomassen, stratum e33: 1 studies
[info]  2026-11-11 22:32:15 study group thomassen, stratum e43: 1 studies
[info]  2026-11-11 22:32:15 study group thomassen, stratum e44: 1 studies
[stage] 2026-11-11 22:32:15 pooled_run
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_all_cause_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_alzheimers_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_apoa: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_apob: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_ascvd: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_hdl_c: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_ldl_c: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_tg: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_EUR_vascular_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_all_cause_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_alzheimers_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_apoa: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_apob: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_ascvd: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_hdl_c: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_ldl_c: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_tg: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group marvel_ukb_MULTI_vascular_dementia: unstratified run, strata left out
[info]  2026-11-11 22:32:15 pooled run, study group thomassen: IVW of the strata
[stage] 2026-11-11 22:32:15 dedupe
[info]  2026-11-11 22:32:15 0 duplicate rows removed
[info]  2026-11-11 22:32:15 0 estimates removed as copies of another study
[stage] 2026-11-11 22:32:15 meta_analyse
[info]  2026-11-11 22:32:16 51 groups, 48 pooling more than one estimate
[info]  2026-11-11 22:32:17 347 groups, 0 pooling more than one estimate
[info]  2026-11-11 22:32:17 no gene burden (--no-gene-burden)
[stage] 2026-11-11 22:32:17 write
[info]  2026-11-11 22:32:17 wrote 398 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/meta_MULTI_selected_gof_multi.tsv.gz
[stage] 2026-11-11 22:32:17 apoe_strata_run
[info]  2026-11-11 22:32:17 252 rows from APOE strata: pooled per stratum
[stage] 2026-11-11 22:32:17 dedupe
[info]  2026-11-11 22:32:17 0 duplicate rows removed
[info]  2026-11-11 22:32:17 0 estimates removed as copies of another study
[stage] 2026-11-11 22:32:17 meta_analyse
[info]  2026-11-11 22:32:18 120 groups, 120 pooling more than one estimate
[info]  2026-11-11 22:32:18 252 groups, 0 pooling more than one estimate
[info]  2026-11-11 22:32:18 no gene burden (--no-gene-burden)
[stage] 2026-11-11 22:32:18 write
[info]  2026-11-11 22:32:18 wrote 372 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/meta_MULTI_selected_gof_multi_apoe_strata.tsv.gz

```

## [51] annotate_ptv (`/home/mvanvugt/projects/lipid_adem/src/annotate_ptv.py`)
- first run: 2026-10-21 13:16:22
- last run: 2026-10-21 13:16:22
- commit: `e9443d3` (dirty)

Output:
```text
[info]  2026-10-21 13:16:21 Reading VEP consequences from /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/vep_lipid_gene_csq.tsv.gz
[info]  2026-10-21 13:16:22 Read 79163 variant x transcript rows
[info]  2026-10-21 13:16:22 CETP: 1595 sites, 58 LoF=HC on the canonical transcript kept, 1537 dropped
[info]  2026-10-21 13:16:22 HMGCR: 1554 sites, 39 LoF=HC on the canonical transcript kept, 1515 dropped
[info]  2026-10-21 13:16:22 NPC1L1: 2757 sites, 96 LoF=HC on the canonical transcript kept, 2661 dropped
[info]  2026-10-21 13:16:22 PCSK9: 1651 sites, 68 LoF=HC on the canonical transcript kept, 1583 dropped
[info]  2026-10-21 13:16:22 ANGPTL3: 802 sites, 56 LoF=HC on the canonical transcript kept, 746 dropped
[info]  2026-10-21 13:16:22 PPARA: 772 sites, 23 LoF=HC on the canonical transcript kept, 749 dropped
[info]  2026-10-21 13:16:22 APOA1: 561 sites, 15 LoF=HC on the canonical transcript kept, 546 dropped
[info]  2026-10-21 13:16:22 APOB: 6376 sites, 172 LoF=HC on the canonical transcript kept, 6204 dropped
[info]  2026-10-21 13:16:22 Wrote 527 PTVs to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/ptv_variants.tsv.gz

```

## [55] combine_variants (`src/combine_variants.py`)
- first run: 2026-10-21 13:50:41
- last run: 2026-11-10 09:58:46
- commit: `9368d49` (dirty)

Output:
```text
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/ptv_variants.tsv.gz: 527 PTVs
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/plp_variants.tsv: 1900 rows; /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-11-10 09:58:46 0 P/LP rows with ref = alt dropped
[warn]  2026-11-10 09:58:46 APOE condition 'Alzheimer disease 3, protection against, due to APOE3-Christchurch' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 APOA1 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 ANGPTL3 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 PPARA condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 PCSK9 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 HMGCR condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 NPC1L1 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 CETP condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 APOB condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-11-10 09:58:46 APOE condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[info]  2026-11-10 09:58:46 262 truncating P/LP variants set to lowering, 213 of them against their conditions
[info]  2026-11-10 09:58:46 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-11-10 09:58:46 ANGPTL3 ClinVar P/LP: 2 variants unknown
[info]  2026-11-10 09:58:46 APOA1 ClinVar P/LP: 11 variants altered
[info]  2026-11-10 09:58:46 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-11-10 09:58:46 APOA1 ClinVar P/LP: 16 variants lowering
[info]  2026-11-10 09:58:46 APOA1 ClinVar P/LP: 6 variants unknown
[info]  2026-11-10 09:58:46 APOB ClinVar P/LP: 5 variants altered
[info]  2026-11-10 09:58:46 APOB ClinVar P/LP: 6 variants conflicting
[info]  2026-11-10 09:58:46 APOB ClinVar P/LP: 224 variants lowering
[info]  2026-11-10 09:58:46 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-11-10 09:58:46 APOE ClinVar P/LP: 12 variants altered
[info]  2026-11-10 09:58:46 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-11-10 09:58:46 APOE ClinVar P/LP: 6 variants unknown
[info]  2026-11-10 09:58:46 CETP ClinVar P/LP: 10 variants lowering
[info]  2026-11-10 09:58:46 CETP ClinVar P/LP: 2 variants unknown
[info]  2026-11-10 09:58:46 HMGCR ClinVar P/LP: 6 variants lowering
[info]  2026-11-10 09:58:46 HMGCR ClinVar P/LP: 3 variants unknown
[info]  2026-11-10 09:58:46 NPC1L1 ClinVar P/LP: 2 variants unknown
[info]  2026-11-10 09:58:46 PCSK9 ClinVar P/LP: 2 variants lowering
[info]  2026-11-10 09:58:46 PCSK9 ClinVar P/LP: 16 variants raising
[info]  2026-11-10 09:58:46 PCSK9 ClinVar P/LP: 2 variants unknown
[info]  2026-11-10 09:58:46 PPARA ClinVar P/LP: 2 variants unknown
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/gof_variants.tsv: 47 GoF variants
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 17323 AM variants of class Benign/Likely Benign
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 8342 AM variants of class Pathogenic/Likely pathogenic
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 2874 AM variants of class Uncertain significance
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 8342 AM variants kept (Pathogenic/Likely pathogenic)
[info]  2026-11-10 09:58:46 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/selected_variants.tsv: 3 selected GoF variants
[warn]  2026-11-10 09:58:46 ANGPTL3 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 APOA1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 APOB ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 APOE ClinVar: 1 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 CETP ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 HMGCR ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 NPC1L1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 PCSK9 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-11-10 09:58:46 PPARA ClinVar: 2 rows without GRCh38 chr/pos/alleles
[info]  2026-11-10 09:58:46 normalisation AM: unchanged=8342
[info]  2026-11-10 09:58:46 normalisation ClinVar: no_sequence=20
[info]  2026-11-10 09:58:46 normalisation ClinVar: unchanged=316
[info]  2026-11-10 09:58:46 normalisation GoF: unchanged=19
[info]  2026-11-10 09:58:46 normalisation PTV: normalised=18
[info]  2026-11-10 09:58:46 normalisation PTV: unchanged=509
[info]  2026-11-10 09:58:46 normalisation SelectedGoF: unchanged=3
[info]  2026-11-10 09:58:46 MNV chr1:62597616:CC:GA: 1 rows -> proxy chr1:62597616:C:G
[info]  2026-11-10 09:58:46 67 sites are in several sources
[info]  2026-11-10 09:58:46 ANGPTL3 AM: 493 variants
[info]  2026-11-10 09:58:46 ANGPTL3 ClinVar: 12 variants
[info]  2026-11-10 09:58:46 ANGPTL3 PTV: 56 variants
[info]  2026-11-10 09:58:46 APOA1 ClinVar: 33 variants
[info]  2026-11-10 09:58:46 APOA1 PTV: 15 variants
[info]  2026-11-10 09:58:46 APOB ClinVar: 236 variants
[info]  2026-11-10 09:58:46 APOB PTV: 172 variants
[info]  2026-11-10 09:58:46 APOE ClinVar: 20 variants
[info]  2026-11-10 09:58:46 CETP AM: 439 variants
[info]  2026-11-10 09:58:46 CETP ClinVar: 10 variants
[info]  2026-11-10 09:58:46 CETP GoF: 1 variants
[info]  2026-11-10 09:58:46 CETP PTV: 58 variants
[info]  2026-11-10 09:58:46 CETP SelectedGoF: 3 variants
[info]  2026-11-10 09:58:46 HMGCR AM: 2623 variants
[info]  2026-11-10 09:58:46 HMGCR ClinVar: 7 variants
[info]  2026-11-10 09:58:46 HMGCR PTV: 39 variants
[info]  2026-11-10 09:58:46 NPC1L1 AM: 2507 variants
[info]  2026-11-10 09:58:46 NPC1L1 PTV: 96 variants
[info]  2026-11-10 09:58:46 PCSK9 AM: 737 variants
[info]  2026-11-10 09:58:46 PCSK9 ClinVar: 18 variants
[info]  2026-11-10 09:58:46 PCSK9 GoF: 18 variants
[info]  2026-11-10 09:58:46 PCSK9 PTV: 68 variants
[info]  2026-11-10 09:58:46 PPARA AM: 1543 variants
[info]  2026-11-10 09:58:46 PPARA PTV: 23 variants
[info]  2026-11-10 09:58:46 Wrote 9227 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-11-10 09:58:46 marvel lists: 9158 sites, 17 with an extra original-form row
[info]  2026-11-10 09:58:46 Wrote 556 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 46 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOA1_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 373 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOB_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 20 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOE_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 508 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 2668 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 2606 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 831 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[info]  2026-11-10 09:58:46 Wrote 1567 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv

```

## [90] archive_results (`src/archive_results.py --apply --tag 20261026_myriad`)
- first run: 2026-10-26 22:35:39
- last run: 2026-10-26 21:40:48
- commit: `a14bc5e`

Output:
```text
[stage] 2026-10-26 21:39:34 collect
[info]  2026-10-26 21:39:34 annotated_eur: 20 files (output current 10, output redundant 6, output stale 4)
[info]  2026-10-26 21:39:34 annotated_eur_unoriented: 20 files (output current 4, output redundant 12, output stale 4)
[info]  2026-10-26 21:39:34 broad_per_variant: 18 files (output current 5, output stale 13)
[info]  2026-10-26 21:39:34 early_snapshots: 3 files (output retired 3)
[info]  2026-10-26 21:39:34 lists_early: 24 files (output retired 24)
[info]  2026-10-26 21:39:34 maf_filter_all: 20 files (output current 10, output redundant 6, output stale 4)
[info]  2026-10-26 21:39:34 region_rare: 12 files (output current 12)
[stage] 2026-10-26 21:39:34 archive
[info]  2026-10-26 21:39:34 wrote 117 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/inventory.tsv.gz
[info]  2026-10-26 21:39:34 annotated_eur: 20 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/annotated_eur (output.tar.gz)
[info]  2026-10-26 21:39:34 annotated_eur_unoriented: 20 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/annotated_eur_unoriented (output.tar.gz)
[info]  2026-10-26 21:39:34 broad_per_variant: 18 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/broad_per_variant (output.tar.gz)
[info]  2026-10-26 21:40:01 early_snapshots: 3 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/early_snapshots (plain files)
[info]  2026-10-26 21:40:17 lists_early: 24 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/lists_early (output.tar.gz)
[info]  2026-10-26 21:40:24 maf_filter_all: 20 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/maf_filter_all (output.tar.gz)
[info]  2026-10-26 21:40:36 region_rare: 12 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/region_rare (output.tar.gz)
[info]  2026-10-26 21:40:42 wrote /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/README.md

```
