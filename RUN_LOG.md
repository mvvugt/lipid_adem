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

## [24] apoe_exposure (`/home/rmgpmva/projects/lipid_adem/src/apoe_exposure.py`)
- first run: 2026-10-09 09:54:04
- last run: 2026-10-09 12:04:31
- commit: `4f02218`

Output:
```text
[stage] 2026-10-09 12:04:16 read
[info]  2026-10-09 12:04:16 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/lipids_full_pheno.tsv.gz: 469587 participants; genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[stage] 2026-10-09 12:04:16 code
[info]  2026-10-09 12:04:17 APOE_genotype codes: e3e3=0, e2e2=1, e2e3=2, e2e4=3, e3e4=4, e4e4=5; reference e3e3
[warn]  2026-10-09 12:04:17 27 participants without a genotype left out
[stage] 2026-10-09 12:04:17 write
[info]  2026-10-09 12:04:25 wrote 469560 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOE_genotype_exposure.tsv.gz

```

## [25] marvel_results_table (`/home/rmgpmva/projects/lipid_adem/src/marvel_results_table.py --ancestry MULTI`)
- first run: 2026-10-08 09:54:25
- last run: 2026-10-12 08:11:12
- commit: `64b20ef` (dirty)

Output:
```text
[stage] 2026-10-12 08:08:26 compare
[info]  2026-10-12 08:08:26 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_tasks.tsv: 18 rows, 6 genes
[info]  2026-10-12 08:08:28 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP: 667 loose result files
[info]  2026-10-12 08:08:32 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP_all_apoe: 667 loose result files
[info]  2026-10-12 08:08:35 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP_eur: 667 loose result files
[info]  2026-10-12 08:08:45 CETP: 874437 loose rows, 443555 new, 430882 already in the store
[warn]  2026-10-12 08:08:45 CETP: 443555 rows added to CETP_results.tsv.gz (675 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44; Variable: all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-12 08:08:48 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR: 714 loose result files
[info]  2026-10-12 08:08:51 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR_all_apoe: 714 loose result files
[info]  2026-10-12 08:08:55 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR_eur: 714 loose result files
[info]  2026-10-12 08:09:06 HMGCR: 936054 loose rows, 474810 new, 461244 already in the store
[warn]  2026-10-12 08:09:06 HMGCR: 474810 rows added to HMGCR_results.tsv.gz (722 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44; Variable: all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[warn]  2026-10-12 08:09:06 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1: outdir not found, skipped
[warn]  2026-10-12 08:09:06 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1_all_apoe: outdir not found, skipped
[warn]  2026-10-12 08:09:06 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1_eur: outdir not found, skipped
[info]  2026-10-12 08:09:06 NPC1L1: no loose result files, store unchanged
[info]  2026-10-12 08:09:06 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9: no loose result files
[warn]  2026-10-12 08:09:06 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9_all_apoe: outdir not found, skipped
[warn]  2026-10-12 08:09:06 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9_eur: outdir not found, skipped
[info]  2026-10-12 08:09:06 PCSK9: no loose result files, store unchanged
[info]  2026-10-12 08:09:07 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3: 324 loose result files
[info]  2026-10-12 08:09:09 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3_all_apoe: 324 loose result files
[info]  2026-10-12 08:09:10 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3_eur: 324 loose result files
[info]  2026-10-12 08:09:15 ANGPTL3: 424764 loose rows, 215460 new, 209304 already in the store
[warn]  2026-10-12 08:09:15 ANGPTL3: 215460 rows added to ANGPTL3_results.tsv.gz (332 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44; Variable: all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-12 08:09:16 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA: 343 loose result files
[info]  2026-10-12 08:09:18 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA_all_apoe: 343 loose result files
[info]  2026-10-12 08:09:19 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA_eur: 343 loose result files
[info]  2026-10-12 08:09:24 PPARA: 449673 loose rows, 228095 new, 221578 already in the store
[warn]  2026-10-12 08:09:24 PPARA: 228095 rows added to PPARA_results.tsv.gz (351 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44; Variable: all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[stage] 2026-10-12 08:09:24 write_stores
[info]  2026-10-12 08:09:50 CETP: wrote 874437 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/CETP_results.tsv.gz
[info]  2026-10-12 08:10:20 HMGCR: wrote 936054 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/HMGCR_results.tsv.gz
[info]  2026-10-12 08:10:34 ANGPTL3: wrote 424764 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/ANGPTL3_results.tsv.gz
[info]  2026-10-12 08:10:47 PPARA: wrote 449673 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/PPARA_results.tsv.gz
[stage] 2026-10-12 08:10:47 marvel_table
[warn]  2026-10-12 08:10:47 no store yet for: NPC1L1
[info]  2026-10-12 08:10:48 ANGPTL3: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-12 08:10:51 CETP: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-12 08:10:54 HMGCR: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-12 08:10:54 PCSK9: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-12 08:10:56 PPARA: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-12 08:10:57 wrote 164 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-10-12 08:11:04 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/apoe_strata.tsv: 20 marvel rows added

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-12 08:34:59
- commit: `64b20ef` (dirty)

Output:
```text
[stage] 2026-10-12 08:17:02 load_sumstats
[info]  2026-10-12 08:17:04 summary-stats: 124 files, 593027 rows incl. one copy per outcome (0 missing)
[info]  2026-10-12 08:17:09 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-12 08:17:09 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-12 08:17:09 marvel
[info]  2026-10-12 08:17:10 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:10 marvel ukb all_cause_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:10 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:10 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:10 marvel ukb alzheimers_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:10 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:10 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 2619 rows -> 287 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 2332 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 2619 rows -> 287 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 2332 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2619 rows -> 287 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2332 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 2619 rows -> 287 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 2332 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 2340 rows -> 256 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb all_cause_dementia: 2084 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 2340 rows -> 256 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb alzheimers_dementia: 2084 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2340 rows -> 256 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:11 marvel ukb vascular_dementia: 2084 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2340 rows -> 256 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2084 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 2448 rows -> 268 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 2180 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 2448 rows -> 268 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 2180 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 2448 rows -> 268 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 2180 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2448 rows -> 268 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2180 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 2538 rows -> 278 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 2260 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 2538 rows -> 278 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 2260 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 2538 rows -> 278 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 2260 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2538 rows -> 278 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2260 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 2664 rows -> 292 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb all_cause_dementia: 2372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 2664 rows -> 292 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb alzheimers_dementia: 2372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 2664 rows -> 292 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb vascular_dementia: 2372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2664 rows -> 292 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:12 marvel ukb frontotemporal_dementia: 2372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 2529 rows -> 277 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 2252 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 2529 rows -> 277 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 2252 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 2529 rows -> 277 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 2252 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 2529 rows -> 277 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 2252 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 2547 rows -> 279 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 2268 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 2547 rows -> 279 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 2268 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 2547 rows -> 279 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 2268 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 2547 rows -> 279 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 2268 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 2475 rows -> 271 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb all_cause_dementia: 2204 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 2475 rows -> 271 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb alzheimers_dementia: 2204 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 2475 rows -> 271 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb vascular_dementia: 2204 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 2475 rows -> 271 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-12 08:17:13 marvel ukb frontotemporal_dementia: 2204 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:16 marvel ukb all_cause_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:16 marvel ukb all_cause_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:16 marvel ukb all_cause_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb alzheimers_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb alzheimers_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb alzheimers_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb vascular_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb vascular_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb vascular_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb frontotemporal_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb frontotemporal_dementia: 4707 rows -> 367 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb frontotemporal_dementia: 4340 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb all_cause_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb all_cause_dementia: 5310 rows -> 420 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb all_cause_dementia: 4890 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb alzheimers_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb alzheimers_dementia: 5310 rows -> 420 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb alzheimers_dementia: 4890 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb vascular_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb vascular_dementia: 5310 rows -> 420 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb vascular_dementia: 4890 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:17 marvel ukb frontotemporal_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb frontotemporal_dementia: 5310 rows -> 420 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:17 marvel ukb frontotemporal_dementia: 4890 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb all_cause_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb all_cause_dementia: 4779 rows -> 377 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb all_cause_dementia: 4402 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb alzheimers_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb alzheimers_dementia: 4779 rows -> 377 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb alzheimers_dementia: 4402 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb vascular_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb vascular_dementia: 4779 rows -> 377 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb vascular_dementia: 4402 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb frontotemporal_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb frontotemporal_dementia: 4779 rows -> 377 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb frontotemporal_dementia: 4402 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb all_cause_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb all_cause_dementia: 4734 rows -> 362 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb all_cause_dementia: 4372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb alzheimers_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb alzheimers_dementia: 4734 rows -> 362 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb alzheimers_dementia: 4372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:18 marvel ukb vascular_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb vascular_dementia: 4734 rows -> 362 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:18 marvel ukb vascular_dementia: 4372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:19 marvel ukb frontotemporal_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb frontotemporal_dementia: 4734 rows -> 362 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb frontotemporal_dementia: 4372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:19 marvel ukb all_cause_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb all_cause_dementia: 4833 rows -> 383 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb all_cause_dementia: 4450 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:19 marvel ukb alzheimers_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb alzheimers_dementia: 4833 rows -> 383 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb alzheimers_dementia: 4450 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:19 marvel ukb vascular_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb vascular_dementia: 4833 rows -> 383 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb vascular_dementia: 4450 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:19 marvel ukb frontotemporal_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb frontotemporal_dementia: 4833 rows -> 383 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb frontotemporal_dementia: 4450 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:19 marvel ukb all_cause_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb all_cause_dementia: 5076 rows -> 395 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:19 marvel ukb all_cause_dementia: 4681 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb alzheimers_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb alzheimers_dementia: 5076 rows -> 395 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb alzheimers_dementia: 4681 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb vascular_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb vascular_dementia: 5076 rows -> 395 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb vascular_dementia: 4681 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb frontotemporal_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb frontotemporal_dementia: 5076 rows -> 395 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb frontotemporal_dementia: 4681 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb all_cause_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb all_cause_dementia: 5409 rows -> 426 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb all_cause_dementia: 4983 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb alzheimers_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb alzheimers_dementia: 5409 rows -> 426 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb alzheimers_dementia: 4983 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb vascular_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb vascular_dementia: 5409 rows -> 426 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb vascular_dementia: 4983 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:20 marvel ukb frontotemporal_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb frontotemporal_dementia: 5409 rows -> 426 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:20 marvel ukb frontotemporal_dementia: 4983 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb all_cause_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb all_cause_dementia: 5004 rows -> 394 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb all_cause_dementia: 4610 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb alzheimers_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb alzheimers_dementia: 5004 rows -> 394 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb alzheimers_dementia: 4610 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb vascular_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb vascular_dementia: 5004 rows -> 394 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb vascular_dementia: 4610 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb frontotemporal_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb frontotemporal_dementia: 5004 rows -> 394 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb frontotemporal_dementia: 4610 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb all_cause_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb all_cause_dementia: 4968 rows -> 385 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb all_cause_dementia: 4583 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb alzheimers_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb alzheimers_dementia: 4968 rows -> 385 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb alzheimers_dementia: 4583 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:21 marvel ukb vascular_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb vascular_dementia: 4968 rows -> 385 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:21 marvel ukb vascular_dementia: 4583 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:22 marvel ukb frontotemporal_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb frontotemporal_dementia: 4968 rows -> 385 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb frontotemporal_dementia: 4583 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:22 marvel ukb all_cause_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb all_cause_dementia: 4995 rows -> 391 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb all_cause_dementia: 4604 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:22 marvel ukb alzheimers_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb alzheimers_dementia: 4995 rows -> 391 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb alzheimers_dementia: 4604 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:22 marvel ukb vascular_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb vascular_dementia: 4995 rows -> 391 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb vascular_dementia: 4604 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:22 marvel ukb frontotemporal_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb frontotemporal_dementia: 4995 rows -> 391 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-12 08:17:22 marvel ukb frontotemporal_dementia: 4604 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:25 marvel ukb all_cause_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:25 marvel ukb all_cause_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:25 marvel ukb all_cause_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb alzheimers_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb alzheimers_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb alzheimers_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb vascular_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb vascular_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb vascular_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb frontotemporal_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb frontotemporal_dementia: 5976 rows -> 387 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb frontotemporal_dementia: 5589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb all_cause_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb all_cause_dementia: 6156 rows -> 402 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb all_cause_dementia: 5754 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb alzheimers_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb alzheimers_dementia: 6156 rows -> 402 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb alzheimers_dementia: 5754 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb vascular_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb vascular_dementia: 6156 rows -> 402 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb vascular_dementia: 5754 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:26 marvel ukb frontotemporal_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb frontotemporal_dementia: 6156 rows -> 402 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:26 marvel ukb frontotemporal_dementia: 5754 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:27 marvel ukb all_cause_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb all_cause_dementia: 5553 rows -> 377 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb all_cause_dementia: 5176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:27 marvel ukb alzheimers_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb alzheimers_dementia: 5553 rows -> 377 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb alzheimers_dementia: 5176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:27 marvel ukb vascular_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb vascular_dementia: 5553 rows -> 377 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb vascular_dementia: 5176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:27 marvel ukb frontotemporal_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb frontotemporal_dementia: 5553 rows -> 377 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb frontotemporal_dementia: 5176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:27 marvel ukb all_cause_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb all_cause_dementia: 5751 rows -> 381 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb all_cause_dementia: 5370 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:27 marvel ukb alzheimers_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb alzheimers_dementia: 5751 rows -> 381 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:27 marvel ukb alzheimers_dementia: 5370 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:28 marvel ukb vascular_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb vascular_dementia: 5751 rows -> 381 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb vascular_dementia: 5370 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:28 marvel ukb frontotemporal_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb frontotemporal_dementia: 5751 rows -> 381 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb frontotemporal_dementia: 5370 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:28 marvel ukb all_cause_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb all_cause_dementia: 5733 rows -> 382 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb all_cause_dementia: 5351 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:28 marvel ukb alzheimers_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb alzheimers_dementia: 5733 rows -> 382 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb alzheimers_dementia: 5351 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:28 marvel ukb vascular_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb vascular_dementia: 5733 rows -> 382 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb vascular_dementia: 5351 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:28 marvel ukb frontotemporal_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb frontotemporal_dementia: 5733 rows -> 382 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:28 marvel ukb frontotemporal_dementia: 5351 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb all_cause_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb all_cause_dementia: 6165 rows -> 403 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb all_cause_dementia: 5762 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb alzheimers_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb alzheimers_dementia: 6165 rows -> 403 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb alzheimers_dementia: 5762 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb vascular_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb vascular_dementia: 6165 rows -> 403 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb vascular_dementia: 5762 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb frontotemporal_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb frontotemporal_dementia: 6165 rows -> 403 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb frontotemporal_dementia: 5762 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb all_cause_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb all_cause_dementia: 6201 rows -> 407 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb all_cause_dementia: 5794 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb alzheimers_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb alzheimers_dementia: 6201 rows -> 407 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:29 marvel ukb alzheimers_dementia: 5794 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:29 marvel ukb vascular_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb vascular_dementia: 6201 rows -> 407 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb vascular_dementia: 5794 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:30 marvel ukb frontotemporal_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb frontotemporal_dementia: 6201 rows -> 407 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb frontotemporal_dementia: 5794 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:30 marvel ukb all_cause_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb all_cause_dementia: 5706 rows -> 389 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb all_cause_dementia: 5317 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:30 marvel ukb alzheimers_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb alzheimers_dementia: 5706 rows -> 389 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb alzheimers_dementia: 5317 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:30 marvel ukb vascular_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb vascular_dementia: 5706 rows -> 389 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb vascular_dementia: 5317 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:30 marvel ukb frontotemporal_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb frontotemporal_dementia: 5706 rows -> 389 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb frontotemporal_dementia: 5317 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:30 marvel ukb all_cause_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb all_cause_dementia: 5940 rows -> 394 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:30 marvel ukb all_cause_dementia: 5546 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:31 marvel ukb alzheimers_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb alzheimers_dementia: 5940 rows -> 394 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb alzheimers_dementia: 5546 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:31 marvel ukb vascular_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb vascular_dementia: 5940 rows -> 394 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb vascular_dementia: 5546 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:31 marvel ukb frontotemporal_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb frontotemporal_dementia: 5940 rows -> 394 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb frontotemporal_dementia: 5546 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:31 marvel ukb all_cause_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb all_cause_dementia: 5832 rows -> 393 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb all_cause_dementia: 5439 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:31 marvel ukb alzheimers_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb alzheimers_dementia: 5832 rows -> 393 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb alzheimers_dementia: 5439 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:31 marvel ukb vascular_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb vascular_dementia: 5832 rows -> 393 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:31 marvel ukb vascular_dementia: 5439 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:32 marvel ukb frontotemporal_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb frontotemporal_dementia: 5832 rows -> 393 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb frontotemporal_dementia: 5439 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:32 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb all_cause_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:32 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb alzheimers_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:32 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb vascular_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:32 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb frontotemporal_dementia: 2394 rows -> 262 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-12 08:17:32 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:33 marvel ukb all_cause_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:33 marvel ukb all_cause_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:33 marvel ukb all_cause_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:33 marvel ukb alzheimers_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:33 marvel ukb alzheimers_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:33 marvel ukb alzheimers_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:33 marvel ukb vascular_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 1854 rows -> 175 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 2871 rows -> 278 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 2593 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 2871 rows -> 278 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 2593 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 2871 rows -> 278 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 2593 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 2871 rows -> 278 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 2593 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 2142 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 1938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 2142 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 1938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 2142 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 1938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 2142 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb frontotemporal_dementia: 1938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 1809 rows -> 170 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb all_cause_dementia: 1639 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 1809 rows -> 170 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb alzheimers_dementia: 1639 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 1809 rows -> 170 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:34 marvel ukb vascular_dementia: 1639 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 1809 rows -> 170 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 1639 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 2439 rows -> 233 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 2206 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 2439 rows -> 233 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 2206 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 2439 rows -> 233 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 2206 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 2439 rows -> 233 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 2206 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 2115 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 1911 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 2115 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 1911 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 2115 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 1911 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 2115 rows -> 204 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb frontotemporal_dementia: 1911 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 2916 rows -> 283 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb all_cause_dementia: 2633 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 2916 rows -> 283 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb alzheimers_dementia: 2633 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 2916 rows -> 283 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:35 marvel ukb vascular_dementia: 2633 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 2916 rows -> 283 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 2633 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 2358 rows -> 227 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 2131 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 2358 rows -> 227 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 2131 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 2358 rows -> 227 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 2131 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 2358 rows -> 227 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 2131 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 2061 rows -> 198 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 1863 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 2061 rows -> 198 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 1863 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 2061 rows -> 198 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 1863 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 2061 rows -> 198 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb frontotemporal_dementia: 1863 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 2565 rows -> 244 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb all_cause_dementia: 2321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 2565 rows -> 244 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb alzheimers_dementia: 2321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 2565 rows -> 244 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:36 marvel ukb vascular_dementia: 2321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-12 08:17:37 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:37 marvel ukb frontotemporal_dementia: 2565 rows -> 244 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-12 08:17:37 marvel ukb frontotemporal_dementia: 2321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-10-12 08:17:37 fetch_curated
[info]  2026-10-12 08:18:33 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1
[info]  2026-10-12 08:18:35 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-12 08:18:39 MONDO_0013792 (exact): 42 fetched; in region: none
[info]  2026-10-12 08:18:43 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-12 08:19:04 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-12 08:19:24 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6
[info]  2026-10-12 08:19:27 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-12 08:19:33 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-12 08:23:46 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3
[info]  2026-10-12 08:23:53 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-12 08:23:55 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-12 08:23:57 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-12 08:32:27 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1
[info]  2026-10-12 08:32:39 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-12 08:32:45 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-12 08:32:49 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-12 08:32:53 EFO ids with 0 curated associations: 4
[stage] 2026-10-12 08:32:53 gene_burden
[info]  2026-10-12 08:32:53 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-12 08:32:53 curated MAF: numeric=58 not_reported=28
[info]  2026-10-12 08:32:53 curated: 54 rows dropped from studies excluded for cohort overlap
[info]  2026-10-12 08:32:53 gene-burden rows: none (8 genes with 0)
[info]  2026-10-12 08:32:56 ancestry: 0 rows of studies not in the discovery log labelled NR
[info]  2026-10-12 08:32:56 ancestry: curated EAS=21
[info]  2026-10-12 08:32:56 ancestry: curated EUR=26
[info]  2026-10-12 08:32:56 ancestry: curated MULTI=21
[info]  2026-10-12 08:32:56 ancestry: curated NR=18
[info]  2026-10-12 08:32:56 ancestry: summary-stats AFR=159854
[info]  2026-10-12 08:32:56 ancestry: summary-stats AMR=73617
[info]  2026-10-12 08:32:56 ancestry: summary-stats CSA=43677
[info]  2026-10-12 08:32:56 ancestry: summary-stats EAS=45135
[info]  2026-10-12 08:32:56 ancestry: summary-stats EUR=163477
[info]  2026-10-12 08:32:56 ancestry: summary-stats MULTI=153469
[info]  2026-10-12 08:32:56 ancestry: summary-stats NR=5898
[stage] 2026-10-12 08:32:56 effect_scale
[info]  2026-10-12 08:33:18 wrote 155 studies to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-12 08:33:18 study effect scale: linear=2, log_or=97, unknown=56
[stage] 2026-10-12 08:33:18 normalise
[info]  2026-10-12 08:33:19 normalisation: summary-stats rows unchanged=601863 no_sequence=40564 ref_mismatch=2699 normalised=1
[info]  2026-10-12 08:33:19 normalisation: curated rows effect_only=86
[stage] 2026-10-12 08:33:19 ensembl_check
[info]  2026-10-12 08:33:19 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:19 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:20 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:20 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:20 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:20 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:20 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:21 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-12 08:33:24 Ensembl check: 22077 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-12 08:33:25 summary-stats rows: alleles match=480761 flipped=135502 not_found=18560 mismatch=9836 strand_flip=468; rsid same=521285 no_source_rsid=60935 rsid_only=41315 different=3032
[info]  2026-10-12 08:33:25 curated rows: alleles match=33 flipped=28 effect_unknown=25; rsid same=86
[info]  2026-10-12 08:33:26 duplicate variants flagged: 2862 rows
[stage] 2026-10-12 08:33:26 write
[info]  2026-10-12 08:34:37 wrote 645213 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-12 08:36:08
- commit: `64b20ef` (dirty)

Output:
```text
[info]  2026-10-12 08:16:21 using root directory: /home/rmgpmva/projects/lipid_adem

```

## [40] clinvar_filter (`mamba run --no-capture-output -n clinvar-build clinvar-filter /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_vcv.db --rcv-db /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_rcv.db -g gene CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA APOA1 APOB APOE -o /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv -vvv`)
- first run: 2026-10-06 17:09:48
- last run: 2026-10-06 17:09:48
- commit: `7e96ca6` (dirty)

Output:
```text
2026-10-06 17:09:48,842 - INFO - Wrote 313818 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
```

## [40] match_variants (`/home/rmgpmva/projects/lipid_adem/src/match_variants.py`)
- first run: 2026-10-01 09:59:12
- last run: 2026-10-12 08:44:45
- commit: `64b20ef` (dirty)

Output:
```text
[stage] 2026-10-12 08:43:58 load_variant_lists
[info]  2026-10-12 08:43:58 6 variant lists, 30561 rows: ANGPTL3_variants.tsv, CETP_variants.tsv, HMGCR_variants.tsv, NPC1L1_variants.tsv, PCSK9_variants.tsv, PPARA_variants.tsv
[info]  2026-10-12 08:43:58 28539 rows with source in ['AM'] skipped
[info]  2026-10-12 08:43:58 414 ClinVar rows of the lists dropped, replaced by /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/plp_variants.tsv
[info]  2026-10-12 08:43:58 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/plp_variants.tsv: 2106 rows; /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-10-12 08:43:58 2 P/LP rows with ref = alt dropped
[info]  2026-10-12 08:43:58 277 truncating P/LP variants set to lowering, 225 of them against their conditions
[info]  2026-10-12 08:43:58 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-10-12 08:43:58 APOA1 ClinVar P/LP: 15 variants altered
[info]  2026-10-12 08:43:58 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-10-12 08:43:58 APOA1 ClinVar P/LP: 18 variants lowering
[info]  2026-10-12 08:43:58 APOA1 ClinVar P/LP: 4 variants unknown
[info]  2026-10-12 08:43:58 APOB ClinVar P/LP: 18 variants altered
[info]  2026-10-12 08:43:58 APOB ClinVar P/LP: 12 variants conflicting
[info]  2026-10-12 08:43:58 APOB ClinVar P/LP: 235 variants lowering
[info]  2026-10-12 08:43:58 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-10-12 08:43:58 APOE ClinVar P/LP: 24 variants altered
[info]  2026-10-12 08:43:58 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-10-12 08:43:58 APOE ClinVar P/LP: 9 variants unknown
[info]  2026-10-12 08:43:58 CETP ClinVar P/LP: 13 variants lowering
[info]  2026-10-12 08:43:58 HMGCR ClinVar P/LP: 9 variants lowering
[info]  2026-10-12 08:43:58 HMGCR ClinVar P/LP: 1 variants unknown
[info]  2026-10-12 08:43:58 PCSK9 ClinVar P/LP: 8 variants lowering
[info]  2026-10-12 08:43:58 PCSK9 ClinVar P/LP: 42 variants raising
[info]  2026-10-12 08:43:58 PCSK9 ClinVar P/LP: 1 variants unknown
[info]  2026-10-12 08:43:58 1124 duplicate rows removed
[info]  2026-10-12 08:43:58 ANGPTL3 ClinVar: 12 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 ANGPTL3 PTV: 57 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 APOA1 ClinVar: 39 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 APOB ClinVar: 268 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 APOE ClinVar: 36 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 CETP ClinVar: 13 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 CETP PTV: 61 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 CETP landfors_paper: 94 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 HMGCR ClinVar: 10 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 HMGCR PTV: 40 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 NPC1L1 PTV: 102 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 PCSK9 ClinVar: 51 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 PCSK9 PTV: 85 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 PPARA PTV: 26 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-12 08:43:58 normalisation: variant-list rows unchanged=902 normalised=11
[stage] 2026-10-12 08:43:58 load_gwas
[info]  2026-10-12 08:44:29 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz: 645213 rows, 645213 variant-level (summary-stats, curated)
[info]  2026-10-12 08:44:31 curated: 25 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-12 08:44:33 match
[info]  2026-10-12 08:44:33 ANGPTL3 ClinVar: 12 variants, 6 matched, GWAS rows: summary-stats=303
[info]  2026-10-12 08:44:33 ANGPTL3 PTV: 57 variants, 55 matched, GWAS rows: summary-stats=2175
[info]  2026-10-12 08:44:33 APOA1 ClinVar: 39 variants, 0 matched, GWAS rows: none
[info]  2026-10-12 08:44:33 APOB ClinVar: 268 variants, 10 matched, GWAS rows: summary-stats=461
[info]  2026-10-12 08:44:33 APOE ClinVar: 36 variants, 13 matched, GWAS rows: summary-stats=962
[info]  2026-10-12 08:44:33 CETP ClinVar: 13 variants, 8 matched, GWAS rows: summary-stats=291
[info]  2026-10-12 08:44:33 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=245
[info]  2026-10-12 08:44:33 CETP PTV: 61 variants, 61 matched, GWAS rows: summary-stats=2196
[info]  2026-10-12 08:44:33 CETP landfors_paper: 94 variants, 94 matched, GWAS rows: summary-stats=3325
[info]  2026-10-12 08:44:33 HMGCR ClinVar: 10 variants, 4 matched, GWAS rows: summary-stats=108
[info]  2026-10-12 08:44:33 HMGCR PTV: 40 variants, 40 matched, GWAS rows: summary-stats=1500
[info]  2026-10-12 08:44:33 NPC1L1 PTV: 102 variants, 6 matched, GWAS rows: summary-stats=107
[info]  2026-10-12 08:44:33 PCSK9 ClinVar: 51 variants, 10 matched, GWAS rows: summary-stats=738 curated=20
[info]  2026-10-12 08:44:33 PCSK9 GoF: 18 variants, 6 matched, GWAS rows: summary-stats=410
[info]  2026-10-12 08:44:33 PCSK9 PTV: 85 variants, 3 matched, GWAS rows: summary-stats=141
[info]  2026-10-12 08:44:33 PPARA PTV: 26 variants, 25 matched, GWAS rows: summary-stats=760
[info]  2026-10-12 08:44:33 a1 vs Ensembl ref: 7180 matched SNV rows checked, 0 where a1 is not the Ensembl ref
[stage] 2026-10-12 08:44:33 write
[info]  2026-10-12 08:44:40 wrote 13742 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz

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
- last run: 2026-10-11 02:15:34
- commit: `64b20ef` (dirty)

Output:
```text
[info]  2026-10-11 02:15:00 task 18: rows 18-18

```

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --ancestry MULTI --studies marvel_ukb_MULTI_all_cause_dementia marvel_ukb_MULTI_all_cause_dementia_e44 marvel_ukb_MULTI_all_cause_dementia_e43 marvel_ukb_MULTI_all_cause_dementia_e33 marvel_ukb_MULTI_all_cause_dementia_e22_e32 marvel_ukb_MULTI_alzheimers_dementia marvel_ukb_MULTI_alzheimers_dementia_e44 marvel_ukb_MULTI_alzheimers_dementia_e43 marvel_ukb_MULTI_alzheimers_dementia_e33 marvel_ukb_MULTI_alzheimers_dementia_e22_e32 marvel_ukb_MULTI_vascular_dementia marvel_ukb_MULTI_vascular_dementia_e44 marvel_ukb_MULTI_vascular_dementia_e43 marvel_ukb_MULTI_vascular_dementia_e33 marvel_ukb_MULTI_vascular_dementia_e22_e32 marvel_ukb_MULTI_frontotemporal_dementia marvel_ukb_MULTI_frontotemporal_dementia_e44 marvel_ukb_MULTI_frontotemporal_dementia_e43 marvel_ukb_MULTI_frontotemporal_dementia_e33 marvel_ukb_MULTI_frontotemporal_dementia_e22_e32 --region-rare --stratified --label ukb_dementia_region_rare`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-12 08:55:53
- commit: `64b20ef` (dirty)

Δ vs previous run (was `64b20ef` (dirty)):
stage `load_matched`:
```diff
@@ -1,6 +1,6 @@
 [info]  2026-10-12 08:54:56 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz: 326167 rows, 9537 variants
 [info]  2026-10-12 08:54:56 20379 rows of excluded gene(s) APOE dropped
 [info]  2026-10-12 08:54:57 305788 of 305788 rows kept (MULTI pools every ancestry) (all: AFR=87047, AMR=42782, CSA=36051, EAS=10748, EUR=69679, MULTI=59250, NR=231)
-[info]  2026-10-12 08:52:32 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32, F5_DEMENTIA_INCLAVO, G6_ALZHEIMER, F5_VASCDEM, FTD: 11524 of 305788 rows kept
+[info]  2026-10-12 08:54:58 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32: 5820 of 305788 rows kept
 [warn]  2026-10-12 08:54:58 no rows with study_accession marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e44
-[info]  2026-10-12 08:52:32 MULTI: 11524 rows pooled across ancestries (EUR=5704, MULTI=5820), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
+[info]  2026-10-12 08:54:58 MULTI: 5820 rows pooled across ancestries (MULTI=5820), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
```
stage `prepare_effects`:
```diff
@@ -1 +1 @@
-[info]  2026-10-12 08:52:32 11524 usable rows, 0 with SE derived from p
+[info]  2026-10-12 08:54:58 5820 usable rows, 0 with SE derived from p
```
stage `orient`:
```diff
@@ -1 +1 @@
-[info]  2026-10-12 08:52:32 2595 variants oriented as a2
+[info]  2026-10-12 08:54:58 1192 variants oriented as a2
```
stage `dedupe`:
```diff
@@ -1,2 +1,2 @@
-[info]  2026-10-12 08:52:32 1060 duplicate rows removed
+[info]  2026-10-12 08:54:58 1052 duplicate rows removed
 [info]  2026-10-12 08:54:58 0 estimates removed as copies of another study
```
stage `meta_analyse`:
```diff
@@ -1,2 +1,2 @@
-[info]  2026-10-12 08:53:19 10380 groups, 84 pooling more than one estimate
-[info]  2026-10-12 08:54:05 10464 groups, 0 pooling more than one estimate
+[info]  2026-10-12 08:55:18 4768 groups, 0 pooling more than one estimate
+[info]  2026-10-12 08:55:37 4768 groups, 0 pooling more than one estimate
```
stage `gene_burden`:
```diff
@@ -1 +1 @@
-[info]  2026-10-12 08:54:05 gene burden: 32 pooled and 48 per-study rows
+[info]  2026-10-12 08:55:38 gene burden: 16 pooled and 16 per-study rows
```
stage `write`:
```diff
@@ -1,2 +1,2 @@
-[info]  2026-10-12 08:54:10 wrote 20844 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_armb_dementia_region_rare.tsv.gz
-[info]  2026-10-12 08:54:15 wrote 80 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_armb_dementia_region_rare.tsv.gz
+[info]  2026-10-12 08:55:40 wrote 9536 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare.tsv.gz
+[info]  2026-10-12 08:55:47 wrote 32 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare.tsv.gz
```

Output:
```text
[info]  2026-10-12 08:54:42 ancestry MULTI, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-12 08:54:42 load_matched
[info]  2026-10-12 08:54:56 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz: 326167 rows, 9537 variants
[info]  2026-10-12 08:54:56 20379 rows of excluded gene(s) APOE dropped
[info]  2026-10-12 08:54:57 305788 of 305788 rows kept (MULTI pools every ancestry) (all: AFR=87047, AMR=42782, CSA=36051, EAS=10748, EUR=69679, MULTI=59250, NR=231)
[info]  2026-10-12 08:54:58 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32: 5820 of 305788 rows kept
[warn]  2026-10-12 08:54:58 no rows with study_accession marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e44
[info]  2026-10-12 08:54:58 MULTI: 5820 rows pooled across ancestries (MULTI=5820), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
[stage] 2026-10-12 08:54:58 effect_scale
[stage] 2026-10-12 08:54:58 prepare_effects
[info]  2026-10-12 08:54:58 5820 usable rows, 0 with SE derived from p
[stage] 2026-10-12 08:54:58 resolve_ambiguous
[stage] 2026-10-12 08:54:58 orient
[info]  2026-10-12 08:54:58 1192 variants oriented as a2
[stage] 2026-10-12 08:54:58 apoe_strata
[info]  2026-10-12 08:54:58 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/apoe_strata.tsv: 44 studies with an APOE stratum entry
[info]  2026-10-12 08:54:58 study group marvel_ukb_MULTI_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-12 08:54:58 study group marvel_ukb_MULTI_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-12 08:54:58 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-12 08:54:58 study group marvel_ukb_MULTI_vascular_dementia, stratum all: 1 studies
[stage] 2026-10-12 08:54:58 pooled_run
[stage] 2026-10-12 08:54:58 dedupe
[info]  2026-10-12 08:54:58 1052 duplicate rows removed
[info]  2026-10-12 08:54:58 0 estimates removed as copies of another study
[stage] 2026-10-12 08:54:58 meta_analyse
[info]  2026-10-12 08:55:18 4768 groups, 0 pooling more than one estimate
[info]  2026-10-12 08:55:37 4768 groups, 0 pooling more than one estimate
[stage] 2026-10-12 08:55:37 gene_burden
[info]  2026-10-12 08:55:38 gene burden: 16 pooled and 16 per-study rows
[stage] 2026-10-12 08:55:38 write
[info]  2026-10-12 08:55:40 wrote 9536 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare.tsv.gz
[info]  2026-10-12 08:55:47 wrote 32 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare.tsv.gz

```
