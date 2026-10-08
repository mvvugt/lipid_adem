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

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-07 16:59:58
- commit: `e68eb48` (dirty)

Output:
```text
[stage] 2026-10-07 14:03:11 load_sumstats
[info]  2026-10-07 14:03:12 summary-stats: 124 files, 593027 rows incl. one copy per outcome (0 missing)
[info]  2026-10-07 14:03:17 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-07 14:03:17 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-07 14:03:17 marvel
[info]  2026-10-07 14:03:17 no own results listed in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_results.tsv
[stage] 2026-10-07 14:03:17 fetch_curated
[info]  2026-10-07 14:04:21 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1 APOE=1
[info]  2026-10-07 14:04:24 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-07 14:04:28 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[info]  2026-10-07 14:04:32 MONDO_0005394 (exact): 41 fetched; in region: APOE=1
[info]  2026-10-07 14:04:55 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-07 14:05:17 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6 APOE=5
[info]  2026-10-07 14:05:20 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-07 14:05:26 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-07 14:10:25 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3 APOE=23
[info]  2026-10-07 14:10:33 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-07 14:10:34 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-07 14:10:36 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-07 14:18:53 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=246
[info]  2026-10-07 14:19:05 MONDO_0004648 (with child traits): 120 fetched; in region: APOE=6
[info]  2026-10-07 14:19:13 EFO_0006799 (with child traits): 40 fetched; in region: APOE=3
[info]  2026-10-07 14:19:18 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-07 14:19:22 EFO ids with 0 curated associations: 4
[stage] 2026-10-07 14:19:22 gene_burden
[info]  2026-10-07 14:19:22 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-07 14:19:23 curated MAF: numeric=226 not_reported=260
[info]  2026-10-07 14:19:23 curated: 253 rows dropped from studies excluded for cohort overlap
[info]  2026-10-07 14:19:23 gene-burden rows: none (9 genes with 0)
[info]  2026-10-07 14:19:24 ancestry: 2 rows of studies not in the discovery log labelled NR
[info]  2026-10-07 14:19:24 ancestry: curated AFR=28
[info]  2026-10-07 14:19:24 ancestry: curated AMR=8
[info]  2026-10-07 14:19:24 ancestry: curated EAS=34
[info]  2026-10-07 14:19:24 ancestry: curated EUR=196
[info]  2026-10-07 14:19:24 ancestry: curated MULTI=182
[info]  2026-10-07 14:19:24 ancestry: curated NR=38
[info]  2026-10-07 14:19:24 ancestry: summary-stats AFR=159854
[info]  2026-10-07 14:19:24 ancestry: summary-stats AMR=73617
[info]  2026-10-07 14:19:24 ancestry: summary-stats CSA=43677
[info]  2026-10-07 14:19:24 ancestry: summary-stats EAS=45135
[info]  2026-10-07 14:19:24 ancestry: summary-stats EUR=137357
[info]  2026-10-07 14:19:24 ancestry: summary-stats MULTI=127489
[info]  2026-10-07 14:19:24 ancestry: summary-stats NR=5898
[stage] 2026-10-07 14:19:24 effect_scale
[info]  2026-10-07 14:19:26 wrote 182 studies to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-07 14:19:26 study effect scale: linear=2, log_or=57, unknown=123
[stage] 2026-10-07 14:19:26 normalise
[info]  2026-10-07 14:19:27 normalisation: summary-stats rows unchanged=589956 ref_mismatch=3070 normalised=1
[info]  2026-10-07 14:19:27 normalisation: curated rows effect_only=486
[stage] 2026-10-07 14:19:27 ensembl_check
[info]  2026-10-07 14:19:27 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:27 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:28 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:28 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:28 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:28 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:28 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:29 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-07 14:19:29 APOE: 11244 Ensembl variants in 19:44893787-44919396 (0 windows fetched, rest cached)
[warn]  2026-10-07 14:20:39 Ensembl variation rs407444: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:29:17 Ensembl variation rs145449362: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:29:54 Ensembl variation rs145449362: HTTP 500, retry 2/3 in 60s
[warn]  2026-10-07 14:32:06 Ensembl variation rs78060355: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:37:48 Ensembl variation rs35617436: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:39:02 Ensembl variation rs58555027: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:44:25 Ensembl variation rs113013240: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:49:07 Ensembl variation rs139579141: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:50:43 Ensembl variation rs3816069: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:52:36 Ensembl variation rs1702003: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:56:30 Ensembl variation rs78052945: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:57:39 Ensembl variation rs77402806: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 14:58:55 Ensembl variation rs77402806: HTTP 500, retry 2/3 in 60s
[warn]  2026-10-07 15:09:02 Ensembl variation rs111628602: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 15:09:38 Ensembl variation rs111628602: HTTP 500, retry 2/3 in 60s
[warn]  2026-10-07 15:15:04 Ensembl variation rs146834124: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 15:28:13 Ensembl variation rs192243749: HTTP 500, retry 1/3 in 30s
[warn]  2026-10-07 15:28:51 Ensembl variation rs192243749: HTTP 500, retry 2/3 in 60s
[warn]  2026-10-07 16:37:50 Ensembl variation rs136002: HTTP 500, retry 1/3 in 30s
[info]  2026-10-07 16:59:14 Ensembl check: 20674 unique variant rows checked, 803 rsids fetched via the variation endpoint
[info]  2026-10-07 16:59:14 summary-stats rows: alleles match=454054 flipped=136621 mismatch=1625 strand_flip=520 not_found=207; rsid same=559073 no_source_rsid=27153 different=3326 rsid_only=3268
[info]  2026-10-07 16:59:14 curated rows: alleles match=226 effect_unknown=138 flipped=118 strand_flip=2 mismatch=2; rsid same=482 different=4
[info]  2026-10-07 16:59:15 duplicate variants flagged: 766 rows
[stage] 2026-10-07 16:59:15 write
[info]  2026-10-07 16:59:58 wrote 593513 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-07 16:59:59
- commit: `e68eb48` (dirty)

Output:
```text
[info]  2026-10-07 14:03:03 using root directory: /home/rmgpmva/projects/lipid_adem

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
- last run: 2026-10-06 16:45:25
- commit: `10eb57b`

Output:
```text
[stage] 2026-10-06 16:45:11 load_variant_lists
[info]  2026-10-06 16:45:11 6 variant lists, 30561 rows: ANGPTL3_variants.tsv, CETP_variants.tsv, HMGCR_variants.tsv, NPC1L1_variants.tsv, PCSK9_variants.tsv, PPARA_variants.tsv
[info]  2026-10-06 16:45:11 28539 rows with source in ['AM'] skipped
[info]  2026-10-06 16:45:11 414 ClinVar rows of the lists dropped, replaced by /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/plp_variants.tsv
[info]  2026-10-06 16:45:11 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/plp_variants.tsv: 2106 rows; /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-10-06 16:45:11 2 P/LP rows with ref = alt dropped
[info]  2026-10-06 16:45:11 277 truncating P/LP variants set to lowering, 225 of them against their conditions
[info]  2026-10-06 16:45:11 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-10-06 16:45:11 APOA1 ClinVar P/LP: 15 variants altered
[info]  2026-10-06 16:45:11 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-10-06 16:45:11 APOA1 ClinVar P/LP: 18 variants lowering
[info]  2026-10-06 16:45:11 APOA1 ClinVar P/LP: 4 variants unknown
[info]  2026-10-06 16:45:11 APOB ClinVar P/LP: 18 variants altered
[info]  2026-10-06 16:45:11 APOB ClinVar P/LP: 12 variants conflicting
[info]  2026-10-06 16:45:11 APOB ClinVar P/LP: 235 variants lowering
[info]  2026-10-06 16:45:11 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-10-06 16:45:11 APOE ClinVar P/LP: 24 variants altered
[info]  2026-10-06 16:45:11 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-10-06 16:45:11 APOE ClinVar P/LP: 9 variants unknown
[info]  2026-10-06 16:45:11 CETP ClinVar P/LP: 13 variants lowering
[info]  2026-10-06 16:45:11 HMGCR ClinVar P/LP: 9 variants lowering
[info]  2026-10-06 16:45:11 HMGCR ClinVar P/LP: 1 variants unknown
[info]  2026-10-06 16:45:11 PCSK9 ClinVar P/LP: 8 variants lowering
[info]  2026-10-06 16:45:11 PCSK9 ClinVar P/LP: 42 variants raising
[info]  2026-10-06 16:45:11 PCSK9 ClinVar P/LP: 1 variants unknown
[info]  2026-10-06 16:45:11 1124 duplicate rows removed
[info]  2026-10-06 16:45:11 ANGPTL3 ClinVar: 12 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 ANGPTL3 PTV: 57 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 APOA1 ClinVar: 39 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 APOB ClinVar: 268 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 APOE ClinVar: 36 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 CETP ClinVar: 13 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 CETP PTV: 61 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 CETP landfors_paper: 94 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 HMGCR ClinVar: 10 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 HMGCR PTV: 40 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 NPC1L1 PTV: 102 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 PCSK9 ClinVar: 51 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 PCSK9 PTV: 85 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 PPARA PTV: 26 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-06 16:45:11 normalisation: variant-list rows unchanged=902 normalised=11
[stage] 2026-10-06 16:45:11 load_gwas
[info]  2026-10-06 16:45:23 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz: 312491 rows, 312491 variant-level (summary-stats, curated)
[info]  2026-10-06 16:45:24 curated: 130 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-06 16:45:24 match
[info]  2026-10-06 16:45:25 ANGPTL3 ClinVar: 12 variants, 3 matched, GWAS rows: summary-stats=71
[info]  2026-10-06 16:45:25 ANGPTL3 PTV: 57 variants, 3 matched, GWAS rows: summary-stats=71
[info]  2026-10-06 16:45:25 APOA1 ClinVar: 39 variants, 0 matched, GWAS rows: none
[info]  2026-10-06 16:45:25 APOB ClinVar: 268 variants, 9 matched, GWAS rows: summary-stats=221
[info]  2026-10-06 16:45:25 APOE ClinVar: 36 variants, 13 matched, GWAS rows: summary-stats=420 curated=21
[info]  2026-10-06 16:45:25 CETP ClinVar: 13 variants, 2 matched, GWAS rows: summary-stats=47
[info]  2026-10-06 16:45:25 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=32
[info]  2026-10-06 16:45:25 CETP PTV: 61 variants, 6 matched, GWAS rows: summary-stats=120
[info]  2026-10-06 16:45:25 CETP landfors_paper: 94 variants, 9 matched, GWAS rows: summary-stats=233
[info]  2026-10-06 16:45:25 HMGCR ClinVar: 10 variants, 0 matched, GWAS rows: none
[info]  2026-10-06 16:45:25 HMGCR PTV: 40 variants, 0 matched, GWAS rows: none
[info]  2026-10-06 16:45:25 NPC1L1 PTV: 102 variants, 6 matched, GWAS rows: summary-stats=107
[info]  2026-10-06 16:45:25 PCSK9 ClinVar: 51 variants, 9 matched, GWAS rows: summary-stats=390
[info]  2026-10-06 16:45:25 PCSK9 GoF: 18 variants, 6 matched, GWAS rows: summary-stats=300
[info]  2026-10-06 16:45:25 PCSK9 PTV: 85 variants, 3 matched, GWAS rows: summary-stats=141
[info]  2026-10-06 16:45:25 PPARA PTV: 26 variants, 0 matched, GWAS rows: none
[info]  2026-10-06 16:45:25 a1 vs Ensembl ref: 1936 matched SNV rows checked, 0 where a1 is not the Ensembl ref
[stage] 2026-10-06 16:45:25 write
[info]  2026-10-06 16:45:25 wrote 2174 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz

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
- last run: 2026-10-08 09:03:45
- commit: `c5846ce` (dirty)

Δ vs previous run (was `c5846ce` (dirty)):
```diff
@@ -1,2 +1,2 @@
-[info]  2026-10-07 23:02:28 task 6: rows 6-6
-[info]  2026-10-08 04:11:04 PPARA: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA
+[info]  2026-10-07 23:02:15 task 2: rows 2-2
+[info]  2026-10-08 09:03:45 HMGCR: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR
```

Output:
```text
[info]  2026-10-07 23:02:15 task 2: rows 2-2
[info]  2026-10-08 09:03:45 HMGCR: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR

```

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --ancestry EUR --outcomes alzheimers_dementia --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 --variant-sources PTV ClinVar --stratified --label thomassen_ad_ptv_clinvar`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-06 17:56:11
- commit: `10eb57b`

Output:
```text
[info]  2026-10-06 17:56:11 ancestry EUR, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-06 17:56:11 load_matched
[info]  2026-10-06 17:56:11 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz: 2174 rows, 55 variants
[info]  2026-10-06 17:56:11 285 of 2174 rows are EUR (all: AFR=384, AMR=162, CSA=999, EAS=144, EUR=285, MULTI=197, NR=3)
[info]  2026-10-06 17:56:11 study_accession in GCST90861026, GCST90861027, GCST90861029, GCST90861030: 1 of 285 rows kept
[warn]  2026-10-06 17:56:11 no rows with study_accession GCST90861026, GCST90861029, GCST90861030
[info]  2026-10-06 17:56:11 outcome in alzheimers_dementia: 1 of 1 rows kept
[stage] 2026-10-06 17:56:11 prepare_effects
[info]  2026-10-06 17:56:11 1 usable rows, 0 with SE derived from p
[stage] 2026-10-06 17:56:11 resolve_ambiguous
[stage] 2026-10-06 17:56:11 orient
[info]  2026-10-06 17:56:11 1 variants oriented as a2
[info]  2026-10-06 17:56:11 1 ClinVar variants with direction altered
[info]  2026-10-06 17:56:11 variant_list_source in PTV, ClinVar: 1 of 1 rows kept
[warn]  2026-10-06 17:56:11 no rows with variant_list_source PTV
[stage] 2026-10-06 17:56:11 dedupe
[info]  2026-10-06 17:56:11 0 duplicate rows removed
[info]  2026-10-06 17:56:11 0 estimates removed as copies of another study
[stage] 2026-10-06 17:56:11 meta_analyse
[info]  2026-10-06 17:56:11 1 groups, 0 pooling more than one estimate
[info]  2026-10-06 17:56:11 1 groups, 0 pooling more than one estimate
[stage] 2026-10-06 17:56:11 gene_burden
[info]  2026-10-06 17:56:11 gene burden: 1 pooled and 1 per-study rows
[info]  2026-10-06 17:56:11 1 variants are ClinVar only without a lowering/raising direction: burden repeated without them
[info]  2026-10-06 17:56:11 gene burden: 0 pooled and 0 per-study rows
[stage] 2026-10-06 17:56:11 write
[info]  2026-10-06 17:56:11 wrote 2 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_EUR_thomassen_ad_ptv_clinvar.tsv.gz
[info]  2026-10-06 17:56:11 wrote 2 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_EUR_thomassen_ad_ptv_clinvar.tsv.gz
[info]  2026-10-06 17:56:11 wrote 0 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_EUR_thomassen_ad_ptv_clinvar_directed_only.tsv.gz

```
