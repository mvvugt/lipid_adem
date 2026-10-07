## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-10-07 09:24:40
- commit: `7e1dc83` (dirty)

Δ vs previous run (was `7e96ca6`):
stage `write_tasks`:
```diff
@@ -1,3 +1,2 @@
 [info]  2026-10-07 09:24:40 wrote 124 tasks (311 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
-[info]  2026-10-06 14:18:30 archived /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs -> /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs_20261005_150736
-[info]  2026-10-06 14:18:30 wrote 2634 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz
+[info]  2026-10-07 09:24:40 wrote 2636 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz
```

Output:
```text
[info]  2026-10-07 09:21:46 9 genes, 84 icd codes
[stage] 2026-10-07 09:21:46 resolve_genes
[stage] 2026-10-07 09:21:46 resolve_efo
[info]  2026-10-07 09:21:47 trait ids checked: 21, obsolete replaced: 0
[info]  2026-10-07 09:21:47 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-07 09:21:47 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-07 09:21:47 finngen_manual
[info]  2026-10-07 09:21:52 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/study_outcome_review.tsv: 673 outcome x study exclusions for 10 outcomes
[info]  2026-10-07 09:21:52 catalog studies with aou, ukb excluded for every outcome
[info]  2026-10-07 09:21:52 all_cause_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 alzheimers_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 coronary_heart_disease: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 frontotemporal_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 hf: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 parkinsons_disease_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 stroke: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 sudden_cardiac_death: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 09:21:52 vascular_dementia: own results for finngen; catalog studies with these cohorts excluded
[stage] 2026-10-07 09:21:52 discover_gwas
[info]  2026-10-07 09:22:01 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, finngen, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 09:22:01 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 09:22:01 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 09:22:14 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, finngen, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 09:22:14 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 09:22:15 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 09:22:16 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:18 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:19 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:19 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:24 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, finngen, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 09:22:25 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 09:22:25 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 09:22:28 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:28 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:28 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:30 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 4 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:22:35 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 09:22:35 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 dropped by review -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 09:22:38 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 09:22:38 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 09:22:38 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 09:23:14 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 72 dropped by review -> 7 with full sumstats -> 7 included, 2 included with blank cohort
[info]  2026-10-07 09:23:16 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 60 dropped by review -> 9 with full sumstats -> 9 included, 3 included with blank cohort
[info]  2026-10-07 09:23:44 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 74 dropped by review -> 16 with full sumstats -> 16 included, 5 included with blank cohort
[info]  2026-10-07 09:23:45 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-07 09:23:46 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-07 09:24:03 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, finngen, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 09:24:04 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 09:24:05 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 09:24:08 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, finngen, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 09:24:08 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 09:24:09 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 09:24:19 MONDO_0005252 (exact): 77 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 12 dropped by review -> 18 with full sumstats -> 16 included, 0 included with blank cohort
[info]  2026-10-07 09:24:20 MONDO_0005252 (exact): 77 studies -> 34 dropped for cohort overlap (aou, ukb) -> 13 dropped by review -> 20 with full sumstats -> 17 included, 0 included with blank cohort
[info]  2026-10-07 09:24:26 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 09:24:27 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 09:24:27 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 09:24:29 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 09:24:30 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 09:24:30 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 09:24:32 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:24:32 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 09:24:37 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 09:24:37 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 09:24:38 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 09:24:40 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-10-07 09:24:40 write_tasks
[info]  2026-10-07 09:24:40 wrote 124 tasks (311 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-10-07 09:24:40 wrote 2636 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/4_1791205029/run_job_array.job --task-id 1 --step 10`)
- first run: 2026-09-21 22:58:26
- last run: 2026-10-05 14:06:19
- commit: `5693f61`
- status: failed

Output:
```text
[info]  2026-10-05 14:06:09 rows 1-8 of 8, 9 gene regions
[warn]  2026-10-05 14:06:10 GCST010480: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST010001-GCST011000/GCST010480/JapaneseMetaAnalysis.tar.gz: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['JapaneseMetaAnalysis/JapaneseMetaAnalysisInfo.txt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000777\x000001750\x000001750\x0000000001467\x0013724433036\x00026547\x00 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ustar  \x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00# This file contains a short description of the columns in the'])
[warn]  2026-10-05 14:06:11 GCST010479: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST010001-GCST011000/GCST010479/TransethnicMetaAnalysis.tar.gz: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['TransethnicMetaAnalysis/TransethnicMetaAnalysisStat.txt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000777\x000001750\x000001750\x0005001355031\x0013242440402\x00030052\x00 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ustar  \x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MarkerName', 'Chromosome', 'Position', 'EA', 'NEA', 'EAF', 'Nsample', 'Ncohort', 'Effects', 'beta_0', 'se_0', 'chisq_association', 'ndf_association', 'P-value_association', 'chisq_ancestry_het', 'ndf_ancestry_het', 'P-value_ancestry_het', 'chisq_residual_het', 'ndf_residual_het', 'P-value_residual_het', 'lnBF', 'Comments'])
[warn]  2026-10-05 14:06:12 GCST90128466: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128466/GCST90128466_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:13 GCST90128462: expected one *.h.tsv.gz in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128462/harmonised, found []; falling back to raw file
[warn]  2026-10-05 14:06:13 GCST90128462: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128462/GCST90128462_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:15 GCST90128459: expected one *.h.tsv.gz in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128459/harmonised, found []; falling back to raw file
[warn]  2026-10-05 14:06:15 GCST90128459: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128459/GCST90128459_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:16 GCST90128456: expected one *.h.tsv.gz in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128456/harmonised, found []; falling back to raw file
[warn]  2026-10-05 14:06:16 GCST90128456: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128456/GCST90128456_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:17 GCST009020: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST009001-GCST010000/GCST009020/GRACE_StageI.txt: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['CHR BP Effect_Allele NonEffect_Allele FREQ_Effect_Allele OR SE P rsID'])
[warn]  2026-10-05 14:06:19 GCST009019: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST009001-GCST010000/GCST009019/GRACEStageI_dbGAP.txt: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['CHR', 'Position', 'Effect_Allele', 'NonEffect_Allele', 'Beta', 'SE', 'P', 'Direction', 'rsID'])

--- error output (raw) ---
[info]  2026-10-05 14:06:09 rows 1-8 of 8, 9 gene regions
[warn]  2026-10-05 14:06:10 GCST010480: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST010001-GCST011000/GCST010480/JapaneseMetaAnalysis.tar.gz: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['JapaneseMetaAnalysis/JapaneseMetaAnalysisInfo.txt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000777\x000001750\x000001750\x0000000001467\x0013724433036\x00026547\x00 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ustar  \x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00# This file contains a short description of the columns in the'])
[warn]  2026-10-05 14:06:11 GCST010479: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST010001-GCST011000/GCST010479/TransethnicMetaAnalysis.tar.gz: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['TransethnicMetaAnalysis/TransethnicMetaAnalysisStat.txt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000777\x000001750\x000001750\x0005001355031\x0013242440402\x00030052\x00 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ustar  \x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00cardiovasculardis\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MarkerName', 'Chromosome', 'Position', 'EA', 'NEA', 'EAF', 'Nsample', 'Ncohort', 'Effects', 'beta_0', 'se_0', 'chisq_association', 'ndf_association', 'P-value_association', 'chisq_ancestry_het', 'ndf_ancestry_het', 'P-value_ancestry_het', 'chisq_residual_het', 'ndf_residual_het', 'P-value_residual_het', 'lnBF', 'Comments'])
[warn]  2026-10-05 14:06:12 GCST90128466: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128466/GCST90128466_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:13 GCST90128462: expected one *.h.tsv.gz in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128462/harmonised, found []; falling back to raw file
[warn]  2026-10-05 14:06:13 GCST90128462: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128462/GCST90128462_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:15 GCST90128459: expected one *.h.tsv.gz in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128459/harmonised, found []; falling back to raw file
[warn]  2026-10-05 14:06:15 GCST90128459: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128459/GCST90128459_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:16 GCST90128456: expected one *.h.tsv.gz in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128456/harmonised, found []; falling back to raw file
[warn]  2026-10-05 14:06:16 GCST90128456: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90128001-GCST90129000/GCST90128456/GCST90128456_buildGRCh38.tsv: missing column(s) ['effect_allele_frequency']; header: ['chromosome', 'base_pair_location', 'effect_allele', 'beta', 'standard_error', 'p_value'])
[warn]  2026-10-05 14:06:17 GCST009020: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST009001-GCST010000/GCST009020/GRACE_StageI.txt: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['CHR BP Effect_Allele NonEffect_Allele FREQ_Effect_Allele OR SE P rsID'])
[warn]  2026-10-05 14:06:19 GCST009019: column mismatch, no outfile written (http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST009001-GCST010000/GCST009019/GRACEStageI_dbGAP.txt: missing column(s) ['chromosome', 'base_pair_location', 'effect_allele_frequency']; header: ['CHR', 'Position', 'Effect_Allele', 'NonEffect_Allele', 'Beta', 'SE', 'P', 'Direction', 'rsID'])
Traceback (most recent call last):
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 382, in main
    run_task(args.tasks_file, args.task_id, args.step)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 329, in run_task
    raise RuntimeError("; ".join(errors))
RuntimeError: 8 row(s) with a column mismatch, fix source/columns: GCST010480, GCST010479, GCST90128466, GCST90128462, GCST90128459, GCST90128456, GCST009020, GCST009019

```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-10-05 14:06:19
- commit: `5693f61`
- status: failed

Output:
```text
[info]  2026-10-05 14:06:06 task 1: rows 1-10
[error] 2026-10-05 14:06:19 run_mamba: '/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/4_1791205029/run_job_array.job --task-id 1 --step 10' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-10-05 14:06:06 repo root=/myriadfs/home/rmgpmva/projects/lipid_adem
[info]  2026-10-05 14:06:06 === /myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.sh ===
[info]  2026-10-05 14:06:06 started at Mon  5 Oct 14:06:06 BST 2026
[info]  2026-10-05 14:06:06 hostname=node-d00b-007.myriad.ucl.ac.uk
[info]  2026-10-05 14:06:06 job array file=/myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/4_1791205029/run_job_array.job
[info]  2026-10-05 14:06:06 temp location=/myriadfs/home/rmgpmva/Scratch/lipid_adem/filter_task_tmp
[info]  2026-10-05 14:06:06 step=10
[info]  2026-10-05 14:06:06 task 1: rows 1-10
[info]  2026-10-05 14:06:09 rows 1-8 of 8, 9 gene regions

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-06 14:48:07
- commit: `7e96ca6`

Output:
```text
[stage] 2026-10-06 14:25:34 load_sumstats
[info]  2026-10-06 14:25:35 summary-stats: 124 files, 312227 rows incl. one copy per outcome (0 missing)
[info]  2026-10-06 14:25:38 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-06 14:25:38 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-06 14:25:38 marvel
[info]  2026-10-06 14:25:38 no own results listed in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_results.tsv
[stage] 2026-10-06 14:25:38 fetch_curated
[info]  2026-10-06 14:26:59 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
[info]  2026-10-06 14:27:02 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-06 14:27:07 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[info]  2026-10-06 14:27:11 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-06 14:27:35 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-06 14:28:00 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
[info]  2026-10-06 14:28:02 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-06 14:28:09 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-06 14:35:18 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14
[info]  2026-10-06 14:35:33 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-06 14:35:35 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-06 14:35:37 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-06 14:47:16 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
[info]  2026-10-06 14:47:26 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-06 14:47:33 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-06 14:47:37 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-06 14:47:40 EFO ids with 0 curated associations: 4
[stage] 2026-10-06 14:47:40 gene_burden
[info]  2026-10-06 14:47:40 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-06 14:47:41 curated MAF: numeric=4 not_reported=260
[info]  2026-10-06 14:47:41 curated: 218 rows dropped from studies excluded for cohort overlap
[info]  2026-10-06 14:47:41 gene-burden rows: none (9 genes with 0)
[info]  2026-10-06 14:47:41 ancestry: 2 rows of studies not in the discovery log labelled NR
[info]  2026-10-06 14:47:41 ancestry: curated AFR=14
[info]  2026-10-06 14:47:41 ancestry: curated EAS=18
[info]  2026-10-06 14:47:41 ancestry: curated EUR=72
[info]  2026-10-06 14:47:41 ancestry: curated MULTI=156
[info]  2026-10-06 14:47:41 ancestry: curated NR=4
[info]  2026-10-06 14:47:41 ancestry: summary-stats AFR=89935
[info]  2026-10-06 14:47:41 ancestry: summary-stats AMR=44204
[info]  2026-10-06 14:47:41 ancestry: summary-stats CSA=39174
[info]  2026-10-06 14:47:41 ancestry: summary-stats EAS=11338
[info]  2026-10-06 14:47:41 ancestry: summary-stats EUR=72391
[info]  2026-10-06 14:47:41 ancestry: summary-stats MULTI=54948
[info]  2026-10-06 14:47:41 ancestry: summary-stats NR=237
[stage] 2026-10-06 14:47:41 normalise
[info]  2026-10-06 14:47:42 normalisation: summary-stats rows unchanged=312224 ref_mismatch=3
[info]  2026-10-06 14:47:42 normalisation: curated rows effect_only=264
[stage] 2026-10-06 14:47:42 ensembl_check
[info]  2026-10-06 14:47:42 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:42 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:42 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:42 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:43 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:43 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:43 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:43 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:44 APOE: 11244 Ensembl variants in 19:44893787-44919396 (0 windows fetched, rest cached)
[info]  2026-10-06 14:47:44 Ensembl check: 13872 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-06 14:47:44 summary-stats rows: alleles match=244379 flipped=67737 mismatch=57 not_found=54; rsid same=308594 no_source_rsid=3195 different=384
[info]  2026-10-06 14:47:44 curated rows: alleles effect_unknown=130 match=122 flipped=8 strand_flip=2 mismatch=2; rsid same=260 different=4
[info]  2026-10-06 14:47:45 duplicate variants flagged: 202 rows
[stage] 2026-10-06 14:47:45 write
[info]  2026-10-06 14:48:07 wrote 312491 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-06 14:48:08
- commit: `7e96ca6`

Output:
```text
[info]  2026-10-06 14:25:32 using root directory: /home/rmgpmva/projects/lipid_adem

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

Δ vs previous run (was `7e96ca6` (dirty)):
- error resolved
```diff
@@ -4,3 +4,13 @@
 [info]  2026-10-06 17:16:22 950 of those are rescued from a Conflicting classification because submitted_classifications contains a pathogenic-tier term
 [info]  2026-10-06 17:16:22 Kept 14070 rows after filtering
 [info]  2026-10-06 17:16:22 950 rows carry a review_flag
+[info]  2026-10-06 17:16:22 Review-status scope-reduction summary:
+                                                                                                                         scope  n_unique_variants  n_variants_removed_cumulative  n_variants_removed_this_step
+                                                                                     All review statuses (every tier included)                431                              0                             0
+Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts + criteria provided, single submitter                311                            120                           120
+                                      Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts                 59                            372                           252
+                                                                                             Include: reviewed by expert panel                 24                            407                            35
+[info]  2026-10-06 17:16:22 Wrote review-status summary to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/pah_variants_review_status_summary.tsv
+[info]  2026-10-06 17:16:22 Widened 4212 assembly-duplicated rows into 2106 variant/condition rows
+[info]  2026-10-06 17:16:22 431 unique variants identified
+[info]  2026-10-06 17:16:22 Writing 2106 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/plp_variants.tsv
```

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
