## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-10-07 10:52:52
- commit: `648f324`

Output:
```text
[info]  2026-10-07 10:49:37 9 genes, 84 icd codes
[stage] 2026-10-07 10:49:37 resolve_genes
[stage] 2026-10-07 10:49:37 resolve_efo
[info]  2026-10-07 10:49:38 trait ids checked: 21, obsolete replaced: 0
[info]  2026-10-07 10:49:38 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-07 10:49:38 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-07 10:49:38 finngen_manual
[info]  2026-10-07 10:49:41 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/study_outcome_review.tsv: 673 outcome x study exclusions for 10 outcomes
[info]  2026-10-07 10:49:41 catalog studies with aou, ukb excluded for every outcome
[info]  2026-10-07 10:49:41 all_cause_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 alzheimers_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 coronary_heart_disease: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 frontotemporal_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 hf: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 parkinsons_disease_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 stroke: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 sudden_cardiac_death: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 vascular_dementia: own results for finngen; catalog studies with these cohorts excluded
[stage] 2026-10-07 10:49:41 discover_gwas
[info]  2026-10-07 10:49:48 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, finngen, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 10:49:49 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 10:49:49 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 10:49:58 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, finngen, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 10:49:59 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 10:49:59 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 10:50:01 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:04 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:07 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, finngen, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 10:50:08 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 10:50:08 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 10:50:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:11 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:11 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:13 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 4 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:17 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:18 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 dropped by review -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:20 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:21 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:21 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:56 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 72 dropped by review -> 7 with full sumstats -> 7 included, 2 included with blank cohort
[info]  2026-10-07 10:50:59 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 60 dropped by review -> 9 with full sumstats -> 9 included, 3 included with blank cohort
[info]  2026-10-07 10:51:27 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 74 dropped by review -> 16 with full sumstats -> 16 included, 5 included with blank cohort
[info]  2026-10-07 10:51:28 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-07 10:51:29 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-07 10:51:47 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, finngen, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 10:51:47 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 10:51:48 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 10:51:52 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, finngen, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:51:52 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:51:52 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:03 MONDO_0005252 (exact): 77 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 12 dropped by review -> 18 with full sumstats -> 16 included, 0 included with blank cohort
[info]  2026-10-07 10:52:04 MONDO_0005252 (exact): 77 studies -> 34 dropped for cohort overlap (aou, ukb) -> 13 dropped by review -> 20 with full sumstats -> 17 included, 0 included with blank cohort
[info]  2026-10-07 10:52:11 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:12 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:12 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:15 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 10:52:15 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 10:52:16 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 10:52:18 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:52:18 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:52:23 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 10:52:23 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 10:52:24 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 10:52:25 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-10-07 10:52:25 write_tasks
[info]  2026-10-07 10:52:31 wrote 124 tasks (311 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-10-07 10:52:31 archived /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs -> /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs_20261007_092533
[stage] 2026-10-07 10:52:31 scale_meta
[warn]  2026-10-07 10:52:46 GCST90477959: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477959)
[warn]  2026-10-07 10:52:46 GCST90477958: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477958)
[warn]  2026-10-07 10:52:46 GCST90246093: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246093)
[warn]  2026-10-07 10:52:46 GCST90399712: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90399712)
[warn]  2026-10-07 10:52:46 GCST90399711: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90399711)
[warn]  2026-10-07 10:52:46 GCST90726898: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726898)
[warn]  2026-10-07 10:52:46 GCST90246094: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246094)
[warn]  2026-10-07 10:52:46 GCST90246086: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246086)
[warn]  2026-10-07 10:52:46 GCST90246085: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246085)
[warn]  2026-10-07 10:52:46 GCST90726916: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726916)
[warn]  2026-10-07 10:52:47 GCST90432123: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432123)
[warn]  2026-10-07 10:52:47 GCST90246098: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246098)
[warn]  2026-10-07 10:52:47 GCST90726915: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726915)
[warn]  2026-10-07 10:52:47 GCST90432122: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432122)
[warn]  2026-10-07 10:52:47 GCST90480188: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90480188)
[warn]  2026-10-07 10:52:47 GCST90477978: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477978)
[warn]  2026-10-07 10:52:47 GCST90477977: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477977)
[warn]  2026-10-07 10:52:48 GCST90246096: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246096)
[warn]  2026-10-07 10:52:48 GCST90018650: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018650)
[warn]  2026-10-07 10:52:48 GCST90726750: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726750)
[warn]  2026-10-07 10:52:48 GCST90704648: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90704648)
[warn]  2026-10-07 10:52:48 GCST90727420: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90727420)
[warn]  2026-10-07 10:52:48 GCST90565439: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90565439)
[warn]  2026-10-07 10:52:48 GCST90566388: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90566388)
[warn]  2026-10-07 10:52:48 GCST90276158: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276158)
[warn]  2026-10-07 10:52:48 GCST90276157: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276157)
[warn]  2026-10-07 10:52:48 GCST007511: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST007511)
[warn]  2026-10-07 10:52:48 GCST003452: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST003452)
[warn]  2026-10-07 10:52:48 GCST002245: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST002245)
[warn]  2026-10-07 10:52:48 GCST90861026: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861026)
[warn]  2026-10-07 10:52:48 GCST90861027: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861027)
[warn]  2026-10-07 10:52:48 GCST90861029: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861029)
[warn]  2026-10-07 10:52:48 GCST90861030: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861030)
[warn]  2026-10-07 10:52:48 GCST90476370: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90476370)
[warn]  2026-10-07 10:52:48 GCST90018586: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018586)
[info]  2026-10-07 10:52:48 metadata yaml read for 115 included studies, scale: unknown=115
[info]  2026-10-07 10:52:49 wrote 2636 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/4_1791376591/run_job_array.job --task-id 1 --step 10`)
- first run: 2026-09-21 22:58:26
- last run: 2026-10-07 13:43:01
- commit: `43baa0f`

Output:
```text
[info]  2026-10-07 13:42:22 rows 1-3 of 3, 9 gene regions
[info]  2026-10-07 13:42:25 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90476001-GCST90477000/GCST90476595/harmonised/GCST90476595.h.tsv.gz @ 9 regions -> 5086 rows (no MAF filter)
[info]  2026-10-07 13:42:26 GCST90476595: 5086 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90476595_result.tsv.gz
[info]  2026-10-07 13:42:29 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90476001-GCST90477000/GCST90476594/harmonised/GCST90476594.h.tsv.gz @ 9 regions -> 3682 rows (no MAF filter)
[info]  2026-10-07 13:42:36 GCST90476594: 3682 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90476594_result.tsv.gz
[info]  2026-10-07 13:42:41 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90018001-GCST90019000/GCST90018650/harmonised/GCST90018650.h.tsv.gz @ 9 regions -> 1496 rows (no MAF filter)
[info]  2026-10-07 13:42:50 GCST90018650: 1496 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90018650_result.tsv.gz

```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-10-07 13:43:27
- commit: `43baa0f`

Output:
```text
[info]  2026-10-07 13:41:55 task 1: rows 1-10

```

## [24] apoe_exposure (`/home/rmgpmva/projects/lipid_adem/src/apoe_exposure.py --column genotype --reference e3e3`)
- first run: 2026-10-09 09:54:04
- last run: 2026-10-09 10:05:09
- commit: `1f6ca38`

Output:
```text
[stage] 2026-10-09 10:05:02 read
[info]  2026-10-09 10:05:03 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/lipids_full_pheno.tsv.gz: 469587 participants; genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[stage] 2026-10-09 10:05:03 indicators
[info]  2026-10-09 10:05:04 APOE_Unknown: 27 vs 276035 reference (e3e3); 193525 NA
[info]  2026-10-09 10:05:04 APOE_e2e2: 3025 vs 276035 reference (e3e3); 190527 NA
[info]  2026-10-09 10:05:04 APOE_e2e3: 57188 vs 276035 reference (e3e3); 136364 NA
[info]  2026-10-09 10:05:04 APOE_e2e4: 11672 vs 276035 reference (e3e3); 181880 NA
[info]  2026-10-09 10:05:04 APOE_e3e4: 110438 vs 276035 reference (e3e3); 83114 NA
[info]  2026-10-09 10:05:04 APOE_e4e4: 11202 vs 276035 reference (e3e3); 182350 NA
[stage] 2026-10-09 10:05:04 write
[info]  2026-10-09 10:05:07 wrote 469587 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOE_genotype_exposure.tsv.gz

```

## [25] marvel_results_table (`/home/rmgpmva/projects/lipid_adem/src/marvel_results_table.py --ancestry MULTI`)
- first run: 2026-10-08 09:54:25
- last run: 2026-10-08 09:54:25
- commit: `dbcc753` (dirty)

Output:
```text
[stage] 2026-10-08 09:54:08 compare
[info]  2026-10-08 09:54:08 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_tasks.tsv: 6 rows, 6 genes
[info]  2026-10-08 09:54:10 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP: 667 loose result files
[info]  2026-10-08 09:54:10 CETP: new store, 76038 rows
[info]  2026-10-08 09:54:12 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR: 714 loose result files
[info]  2026-10-08 09:54:13 HMGCR: new store, 81396 rows
[warn]  2026-10-08 09:54:13 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1: outdir not found, skipped
[info]  2026-10-08 09:54:13 NPC1L1: no loose result files, store unchanged
[info]  2026-10-08 09:54:14 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9: 324 loose result files
[info]  2026-10-08 09:54:14 PCSK9: new store, 36936 rows
[info]  2026-10-08 09:54:15 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3: 324 loose result files
[info]  2026-10-08 09:54:15 ANGPTL3: new store, 36936 rows
[info]  2026-10-08 09:54:16 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA: 343 loose result files
[info]  2026-10-08 09:54:16 PPARA: new store, 39102 rows
[stage] 2026-10-08 09:54:16 write_stores
[info]  2026-10-08 09:54:18 CETP: wrote 76038 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/CETP_results.tsv.gz
[info]  2026-10-08 09:54:21 HMGCR: wrote 81396 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/HMGCR_results.tsv.gz
[info]  2026-10-08 09:54:22 PCSK9: wrote 36936 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/PCSK9_results.tsv.gz
[info]  2026-10-08 09:54:23 ANGPTL3: wrote 36936 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/ANGPTL3_results.tsv.gz
[info]  2026-10-08 09:54:24 PPARA: wrote 39102 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/PPARA_results.tsv.gz
[stage] 2026-10-08 09:54:24 marvel_table
[warn]  2026-10-08 09:54:24 no store yet for: NPC1L1
[info]  2026-10-08 09:54:24 ANGPTL3: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-08 09:54:24 CETP: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-08 09:54:24 HMGCR: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-08 09:54:25 PCSK9: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-08 09:54:25 PPARA: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-08 09:54:25 wrote 20 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-10-08 09:54:25 no APOE-stratified marvel rows, apoe_strata.tsv unchanged

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-08 10:50:11
- commit: `dbcc753` (dirty)

Output:
```text
[stage] 2026-10-08 10:34:27 load_sumstats
[info]  2026-10-08 10:34:28 summary-stats: 124 files, 593027 rows incl. one copy per outcome (0 missing)
[info]  2026-10-08 10:34:33 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-08 10:34:33 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-08 10:34:33 marvel
[info]  2026-10-08 10:34:33 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb all_cause_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:33 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb alzheimers_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:33 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb vascular_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:33 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb frontotemporal_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-08 10:34:33 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-08 10:34:34 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:35 marvel ukb all_cause_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb all_cause_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb all_cause_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:35 marvel ukb alzheimers_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb alzheimers_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb alzheimers_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:35 marvel ukb vascular_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb vascular_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb vascular_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-08 10:34:35 marvel ukb frontotemporal_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb frontotemporal_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-08 10:34:35 marvel ukb frontotemporal_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-10-08 10:34:35 fetch_curated
[info]  2026-10-08 10:35:32 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1 APOE=1
[info]  2026-10-08 10:35:34 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-08 10:35:38 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[info]  2026-10-08 10:35:42 MONDO_0005394 (exact): 41 fetched; in region: APOE=1
[info]  2026-10-08 10:36:04 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-08 10:36:27 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6 APOE=5
[info]  2026-10-08 10:36:30 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-08 10:36:36 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-08 10:40:57 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3 APOE=23
[info]  2026-10-08 10:41:05 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-08 10:41:07 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-08 10:41:08 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-08 10:48:46 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=246
[info]  2026-10-08 10:48:55 MONDO_0004648 (with child traits): 120 fetched; in region: APOE=6
[info]  2026-10-08 10:49:02 EFO_0006799 (with child traits): 40 fetched; in region: APOE=3
[info]  2026-10-08 10:49:05 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-08 10:49:08 EFO ids with 0 curated associations: 4
[stage] 2026-10-08 10:49:08 gene_burden
[info]  2026-10-08 10:49:08 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-08 10:49:10 curated MAF: numeric=226 not_reported=260
[info]  2026-10-08 10:49:10 curated: 253 rows dropped from studies excluded for cohort overlap
[info]  2026-10-08 10:49:10 gene-burden rows: none (9 genes with 0)
[info]  2026-10-08 10:49:11 ancestry: 2 rows of studies not in the discovery log labelled NR
[info]  2026-10-08 10:49:12 ancestry: curated AFR=28
[info]  2026-10-08 10:49:12 ancestry: curated AMR=8
[info]  2026-10-08 10:49:12 ancestry: curated EAS=34
[info]  2026-10-08 10:49:12 ancestry: curated EUR=196
[info]  2026-10-08 10:49:12 ancestry: curated MULTI=182
[info]  2026-10-08 10:49:12 ancestry: curated NR=38
[info]  2026-10-08 10:49:12 ancestry: summary-stats AFR=159854
[info]  2026-10-08 10:49:12 ancestry: summary-stats AMR=73617
[info]  2026-10-08 10:49:12 ancestry: summary-stats CSA=43677
[info]  2026-10-08 10:49:12 ancestry: summary-stats EAS=45135
[info]  2026-10-08 10:49:12 ancestry: summary-stats EUR=137357
[info]  2026-10-08 10:49:12 ancestry: summary-stats MULTI=133301
[info]  2026-10-08 10:49:12 ancestry: summary-stats NR=5898
[stage] 2026-10-08 10:49:12 effect_scale
[info]  2026-10-08 10:49:13 wrote 186 studies to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-08 10:49:14 study effect scale: linear=2, log_or=61, unknown=123
[stage] 2026-10-08 10:49:14 normalise
[info]  2026-10-08 10:49:15 normalisation: summary-stats rows unchanged=595768 ref_mismatch=3070 normalised=1
[info]  2026-10-08 10:49:15 normalisation: curated rows effect_only=486
[stage] 2026-10-08 10:49:15 ensembl_check
[info]  2026-10-08 10:49:15 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:15 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:15 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:16 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:16 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:16 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:16 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:17 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:17 APOE: 11244 Ensembl variants in 19:44893787-44919396 (0 windows fetched, rest cached)
[info]  2026-10-08 10:49:19 Ensembl check: 21834 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-08 10:49:19 summary-stats rows: alleles match=457522 flipped=136621 mismatch=2353 not_found=1823 strand_flip=520; rsid same=559073 no_source_rsid=31349 different=3326 rsid_only=3268
[info]  2026-10-08 10:49:19 curated rows: alleles match=226 effect_unknown=138 flipped=118 strand_flip=2 mismatch=2; rsid same=482 different=4
[info]  2026-10-08 10:49:21 duplicate variants flagged: 2862 rows
[stage] 2026-10-08 10:49:21 write
[info]  2026-10-08 10:50:11 wrote 599325 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-08 10:50:12
- commit: `dbcc753` (dirty)

Output:
```text
[info]  2026-10-08 10:34:22 using root directory: /home/rmgpmva/projects/lipid_adem

```

## [40] clinvar_filter (`mamba run --no-capture-output -n clinvar-build clinvar-filter /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_vcv.db --rcv-db /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_rcv.db -g gene CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA APOA1 APOB APOE -o /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv -vvv`)
- first run: 2026-10-06 17:09:48
- last run: 2026-10-06 17:09:48
- commit: `7e96ca6` (dirty)

Output:
```text
2026-10-06 17:09:48,842 - INFO - Wrote 313818 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
```

## [40] match_variants (`/home/rmgpmva/projects/lipid_adem/src/match_variants.py --region-rare --max-maf 0.01`)
- first run: 2026-10-01 09:59:12
- last run: 2026-10-08 11:10:25
- commit: `2229b2b`

Output:
```text
[stage] 2026-10-08 11:09:05 load_gwas
[info]  2026-10-08 11:09:30 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz: 599325 rows, 599325 variant-level (summary-stats, curated)
[info]  2026-10-08 11:09:32 curated: 138 rows without chrom/pos or effect allele, cannot be matched
[info]  2026-10-08 11:09:34 region-rare: 599187 rows, 0 outside their gene region, 271372 with MAF >= 0.01, 9772 without MAF (not marvel) dropped, 5812 marvel rows without MAF kept; 318043 rows kept
[stage] 2026-10-08 11:09:35 build_region_list
[info]  2026-10-08 11:09:35 region-rare list: 9537 sites (4253 duplicates after ref/alt ordering removed), 1 without a known reference allele (alleles in alphabetical order)
[info]  2026-10-08 11:09:35 region-rare list: ANGPTL3 706 sites
[info]  2026-10-08 11:09:35 region-rare list: APOA1 607 sites
[info]  2026-10-08 11:09:35 region-rare list: APOB 1640 sites
[info]  2026-10-08 11:09:35 region-rare list: APOE 614 sites
[info]  2026-10-08 11:09:35 region-rare list: CETP 1367 sites
[info]  2026-10-08 11:09:35 region-rare list: HMGCR 1095 sites
[info]  2026-10-08 11:09:35 region-rare list: NPC1L1 1121 sites
[info]  2026-10-08 11:09:35 region-rare list: PCSK9 1102 sites
[info]  2026-10-08 11:09:35 region-rare list: PPARA 1285 sites
[stage] 2026-10-08 11:09:35 match
[info]  2026-10-08 11:09:36 ANGPTL3 region_rare: 706 variants, 706 matched, GWAS rows: summary-stats=18474
[info]  2026-10-08 11:09:37 APOA1 region_rare: 607 variants, 607 matched, GWAS rows: summary-stats=23493
[info]  2026-10-08 11:09:37 APOB region_rare: 1640 variants, 1640 matched, GWAS rows: summary-stats=63380
[info]  2026-10-08 11:09:37 APOE region_rare: 614 variants, 614 matched, GWAS rows: summary-stats=20375 curated=4
[info]  2026-10-08 11:09:37 CETP region_rare: 1367 variants, 1367 matched, GWAS rows: summary-stats=46812
[info]  2026-10-08 11:09:37 HMGCR region_rare: 1095 variants, 1095 matched, GWAS rows: summary-stats=29351
[info]  2026-10-08 11:09:37 NPC1L1 region_rare: 1121 variants, 1121 matched, GWAS rows: summary-stats=38389
[info]  2026-10-08 11:09:37 PCSK9 region_rare: 1102 variants, 1102 matched, GWAS rows: summary-stats=43783
[info]  2026-10-08 11:09:37 PPARA region_rare: 1285 variants, 1285 matched, GWAS rows: summary-stats=42106
[warn]  2026-10-08 11:09:38 a1 vs Ensembl ref: 304214 matched SNV rows checked, 32 where a1 is not the Ensembl ref (e.g. 1:62598799:AAAA:AAA, 1:62601803:AGGT:AGGTAGGT, 1:62604235:GG:G)
[stage] 2026-10-08 11:09:38 write
[info]  2026-10-08 11:10:24 wrote 326167 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz

```

## [50] annotate_variants (`/Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/src/annotate_variants.py`)
- first run: 2026-10-06 17:13:43
- last run: 2026-10-06 17:16:22
- commit: `7e96ca6` (dirty)

Output:
```text
[info]  2026-10-06 17:16:21 Reading ClinVar variants from /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
[info]  2026-10-06 17:16:22 Read 313818 rows
[info]  2026-10-06 17:16:22 13120 rows have a clean LP/P rcv_classification.
[info]  2026-10-06 17:16:22 950 of those are rescued from a Conflicting classification because submitted_classifications contains a pathogenic-tier term
[info]  2026-10-06 17:16:22 Kept 14070 rows after filtering
[info]  2026-10-06 17:16:22 950 rows carry a review_flag
[info]  2026-10-06 17:16:22 Review-status scope-reduction summary:
                                                                                                                         scope  n_unique_variants  n_variants_removed_cumulative  n_variants_removed_this_step
                                                                                     All review statuses (every tier included)                431                              0                             0
Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts + criteria provided, single submitter                311                            120                           120
                                      Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts                 59                            372                           252
                                                                                             Include: reviewed by expert panel                 24                            407                            35
[info]  2026-10-06 17:16:22 Wrote review-status summary to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/pah_variants_review_status_summary.tsv
[info]  2026-10-06 17:16:22 Widened 4212 assembly-duplicated rows into 2106 variant/condition rows
[info]  2026-10-06 17:16:22 431 unique variants identified
[info]  2026-10-06 17:16:22 Writing 2106 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/plp_variants.tsv

```

## [50] marvel_assoc_job
- first run: 2026-10-07 13:49:03
- last run: 2026-10-09 10:48:45
- commit: `1f6ca38`

Δ vs previous run (was `1f6ca38`):
```diff
@@ -1,2 +1,2 @@
-[info]  2026-10-09 10:35:27 task 1: rows 1-1
-[info]  2026-10-09 10:42:41 APOE_genotype: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/APOE_genotype
+[info]  2026-10-09 10:41:04 task 2: rows 2-2
+[info]  2026-10-09 10:48:36 APOE_genotype: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/APOE_genotype_eur
```

Output:
```text
[info]  2026-10-09 10:41:04 task 2: rows 2-2
[info]  2026-10-09 10:48:36 APOE_genotype: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/APOE_genotype_eur

```

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --ancestry MULTI --studies marvel_ukb_MULTI_all_cause_dementia marvel_ukb_MULTI_alzheimers_dementia marvel_ukb_MULTI_vascular_dementia marvel_ukb_MULTI_frontotemporal_dementia --region-rare --stratified --label ukb_dementia_region_rare`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-08 11:15:01
- commit: `2229b2b`

Output:
```text
[info]  2026-10-08 11:14:02 ancestry MULTI, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-08 11:14:02 load_matched
[info]  2026-10-08 11:14:19 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz: 326167 rows, 9537 variants
[info]  2026-10-08 11:14:19 326167 of 326167 rows kept (MULTI pools every ancestry) (all: AFR=92393, AMR=45572, CSA=39238, EAS=11434, EUR=74628, MULTI=62665, NR=237)
[info]  2026-10-08 11:14:21 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_frontotemporal_dementia: 5820 of 326167 rows kept
[info]  2026-10-08 11:14:21 MULTI: 5820 rows pooled across ancestries (MULTI=5820), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
[stage] 2026-10-08 11:14:21 effect_scale
[stage] 2026-10-08 11:14:21 prepare_effects
[info]  2026-10-08 11:14:21 5820 usable rows, 0 with SE derived from p
[stage] 2026-10-08 11:14:21 resolve_ambiguous
[stage] 2026-10-08 11:14:21 orient
[info]  2026-10-08 11:14:21 1192 variants oriented as a2
[stage] 2026-10-08 11:14:21 apoe_strata
[info]  2026-10-08 11:14:21 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/apoe_strata.tsv: 4 studies with an APOE stratum entry
[stage] 2026-10-08 11:14:21 pooled_run
[stage] 2026-10-08 11:14:21 dedupe
[info]  2026-10-08 11:14:21 1052 duplicate rows removed
[info]  2026-10-08 11:14:21 0 estimates removed as copies of another study
[stage] 2026-10-08 11:14:21 meta_analyse
[info]  2026-10-08 11:14:41 4768 groups, 0 pooling more than one estimate
[info]  2026-10-08 11:15:01 4768 groups, 0 pooling more than one estimate
[stage] 2026-10-08 11:15:01 gene_burden
[info]  2026-10-08 11:15:01 gene burden: 16 pooled and 16 per-study rows
[stage] 2026-10-08 11:15:01 write
[info]  2026-10-08 11:15:01 wrote 9536 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare.tsv.gz
[info]  2026-10-08 11:15:01 wrote 32 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare.tsv.gz

```
