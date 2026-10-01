## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-30 15:22:55
- commit: `578bffb`

Output:
```text
[info]  2026-09-30 15:15:22 9 genes, 50 icd codes
[stage] 2026-09-30 15:15:22 resolve_genes
[stage] 2026-09-30 15:15:22 resolve_efo
[info]  2026-09-30 15:15:25 trait ids checked: 24, obsolete replaced: 0
[info]  2026-09-30 15:15:25 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
[info]  2026-09-30 15:15:25 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
[info]  2026-09-30 15:15:25 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-09-30 15:15:25 discover_gwas
[info]  2026-09-30 15:15:59 EFO_0003913 (exact): 56 studies -> 44 with full sumstats -> 10 included
[info]  2026-09-30 15:18:05 EFO_0004611 (exact): 742 studies -> 337 with full sumstats -> 10 included
[info]  2026-09-30 15:19:43 EFO_0004612 (exact): 718 studies -> 261 with full sumstats -> 10 included
[info]  2026-09-30 15:20:02 EFO_0004614 (exact): 126 studies -> 72 with full sumstats -> 10 included
[info]  2026-09-30 15:20:21 EFO_0004615 (exact): 128 studies -> 75 with full sumstats -> 10 included
[info]  2026-09-30 15:20:23 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-30 15:20:25 EFO_0008584 (exact): 2 studies -> 2 with full sumstats -> 2 included
[info]  2026-09-30 15:20:27 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-30 15:20:33 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 3 with full sumstats -> 3 included
[info]  2026-09-30 15:20:35 MONDO_0004781 (exact): 11 studies -> 6 with full sumstats -> 6 included
[info]  2026-09-30 15:21:18 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 41 with full sumstats -> 19 included
[info]  2026-09-30 15:21:47 MONDO_0005010 (exact): 207 studies -> 69 with full sumstats -> 10 included
[info]  2026-09-30 15:22:05 MONDO_0005098 (exact): 134 studies -> 65 with full sumstats -> 10 included
[info]  2026-09-30 15:22:08 MONDO_0005099 (exact): 19 studies -> 12 with full sumstats -> 10 included
[info]  2026-09-30 15:22:20 MONDO_0005252 (exact): 77 studies -> 57 with full sumstats -> 10 included
[info]  2026-09-30 15:22:30 MONDO_0005267 (exact): 58 studies -> 48 with full sumstats -> 10 included
[info]  2026-09-30 15:22:38 MONDO_0005294 (exact): 55 studies -> 44 with full sumstats -> 10 included
[info]  2026-09-30 15:22:43 MONDO_0005311 (exact): 34 studies -> 28 with full sumstats -> 10 included
[info]  2026-09-30 15:22:46 MONDO_0005394 (exact): 10 studies -> 6 with full sumstats -> 6 included
[info]  2026-09-30 15:22:48 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-30 15:22:53 MONDO_0013792 (exact): 30 studies -> 17 with full sumstats -> 10 included
[info]  2026-09-30 15:22:54 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-09-30 15:22:54 finngen_manual
[stage] 2026-09-30 15:22:55 write_tasks
[info]  2026-09-30 15:22:55 wrote 183 tasks (205 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-30 15:22:55 archived /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs -> /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs_20260930_103110
[info]  2026-09-30 15:22:55 wrote 2983 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/1_1790778601/run_job_array.job --task-id 161 --step 10`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-30 18:52:53
- commit: `578bffb`

Output:
```text
[info]  2026-09-30 17:38:23 rows 161-170 of 172, 9 gene regions
[info]  2026-09-30 17:38:43 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90450001-GCST90451000/GCST90450877/GCST90450877.tsv.gz @ 9 regions -> 259 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 17:38:55 GCST90450877: 259 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90450877_result.tsv.gz
[info]  2026-09-30 17:39:15 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90450001-GCST90451000/GCST90450919/GCST90450919.tsv.gz @ 9 regions -> 259 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 17:39:21 GCST90450919: 259 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90450919_result.tsv.gz
[info]  2026-09-30 17:39:34 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90854001-GCST90855000/GCST90854259/GCST90854259.tsv.gz @ 9 regions -> 0 rows with MAF < 0.01 (raw scan)
[warn]  2026-09-30 17:39:34 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90854001-GCST90855000/GCST90854259/GCST90854259.tsv.gz: 0 rows -- 1289 in region, 0 missing frequency, none with MAF < 0.01
[info]  2026-09-30 17:39:38 GCST90854259: 0 rows over 0 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90854259_result.tsv.gz
[info]  2026-09-30 17:44:03 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451517/GCST90451517.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 17:44:04 GCST90451517: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451517_result.tsv.gz
[info]  2026-09-30 17:49:07 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451514/GCST90451514.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 17:49:07 GCST90451514: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451514_result.tsv.gz
[info]  2026-09-30 17:56:57 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451463/GCST90451463.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 17:57:02 GCST90451463: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451463_result.tsv.gz
[info]  2026-09-30 18:07:18 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451460/GCST90451460.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 18:07:19 GCST90451460: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451460_result.tsv.gz
[info]  2026-09-30 18:28:22 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451456/GCST90451456.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 18:28:22 GCST90451456: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451456_result.tsv.gz
[info]  2026-09-30 18:45:16 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451429/GCST90451429.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 18:45:17 GCST90451429: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451429_result.tsv.gz
[info]  2026-09-30 18:52:53 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90451001-GCST90452000/GCST90451427/GCST90451427.tsv.gz @ 9 regions -> 14539 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 18:52:53 GCST90451427: 14539 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90451427_result.tsv.gz

```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-09-30 18:52:54
- commit: `578bffb`

Output:
```text
[info]  2026-09-30 17:37:42 task 161: rows 161-170

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-09-30 22:35:04
- commit: `578bffb`

Output:
```text
[info]  2026-09-30 21:07:46 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
[info]  2026-09-30 21:07:46 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
[stage] 2026-09-30 21:07:46 load_sumstats
[info]  2026-09-30 21:07:49 summary-stats: 183 files, 596410 rows incl. one copy per outcome (0 missing)
[info]  2026-09-30 21:07:53 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-09-30 21:07:53 fetch_curated
[info]  2026-09-30 21:17:03 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
[info]  2026-09-30 21:17:13 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-09-30 21:20:13 EFO_0004614 (exact): 2375 fetched; in region: CETP=21 ANGPTL3=4 APOA1=10 APOB=6 APOE=10
[info]  2026-09-30 21:22:16 EFO_0004615 (exact): 1772 fetched; in region: CETP=6 HMGCR=1 NPC1L1=1 PCSK9=14 APOA1=2 APOB=24 APOE=22
[info]  2026-09-30 21:23:16 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
[info]  2026-09-30 21:23:18 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-09-30 21:23:22 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[info]  2026-09-30 21:23:27 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-09-30 21:23:52 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-09-30 21:23:58 MONDO_0005311 (exact): 74 fetched; in region: CETP=1
[info]  2026-09-30 21:24:05 MONDO_0005294 (exact): 92 fetched; in region: none
[info]  2026-09-30 21:24:41 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
[info]  2026-09-30 21:24:43 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-09-30 21:24:50 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-09-30 21:29:33 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14
[info]  2026-09-30 22:07:03 EFO_0004612 (exact): 25386 fetched; in region: CETP=145 PCSK9=3 ANGPTL3=4 PPARA=1 APOA1=19 APOB=31 APOE=36
[info]  2026-09-30 22:33:33 EFO_0004611 (exact): 18417 fetched; in region: CETP=33 HMGCR=24 NPC1L1=15 PCSK9=75 ANGPTL3=5 PPARA=2 APOA1=4 APOB=60 APOE=79
[info]  2026-09-30 22:33:49 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-09-30 22:33:53 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-09-30 22:33:56 EFO ids with 0 curated associations: 4
[stage] 2026-09-30 22:33:56 gene_burden
[info]  2026-09-30 22:33:56 Open Targets disease ids: 32 (from 23 outcome ids)
[info]  2026-09-30 22:33:57 curated MAF: numeric=23 not_reported=1036
[info]  2026-09-30 22:33:57 gene-burden rows: CETP=135 HMGCR=7 NPC1L1=52 PCSK9=168 ANGPTL3=91 APOA1=61 APOB=207 APOE=2 (1 genes with 0)
[info]  2026-09-30 22:33:59 duplicate variants flagged: 308 rows
[stage] 2026-09-30 22:33:59 write
[info]  2026-09-30 22:34:52 wrote 598192 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-09-30 22:35:32
- commit: `578bffb`

Output:
```text
[info]  2026-09-30 21:07:43 using root directory: /home/rmgpmva/projects/lipid_adem

```

## [40] match_variants (`/home/rmgpmva/projects/lipid_adem/src/match_variants.py`)
- first run: 2026-10-01 09:59:12
- last run: 2026-10-01 09:59:12
- commit: `74dae41` (dirty)

Output:
```text
[stage] 2026-10-01 09:58:41 load_variant_lists
[info]  2026-10-01 09:58:41 6 variant lists, 30561 rows: ANGPTL3_variants.tsv, CETP_variants.tsv, HMGCR_variants.tsv, NPC1L1_variants.tsv, PCSK9_variants.tsv, PPARA_variants.tsv
[info]  2026-10-01 09:58:41 28539 rows with source in ['AM'] skipped
[info]  2026-10-01 09:58:41 1125 duplicate rows removed
[info]  2026-10-01 09:58:41 ANGPTL3 ClinVar: 22 rows, 12 without alleles, 10 outside gene region
[info]  2026-10-01 09:58:41 ANGPTL3 PTV: 57 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 CETP ClinVar: 317 rows, 9 without alleles, 6 outside gene region
[info]  2026-10-01 09:58:41 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 CETP PTV: 61 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 CETP landfors_paper: 94 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 HMGCR ClinVar: 9 rows, 1 without alleles, 1 outside gene region
[info]  2026-10-01 09:58:41 HMGCR PTV: 40 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 NPC1L1 ClinVar: 9 rows, 9 without alleles, 9 outside gene region
[info]  2026-10-01 09:58:41 NPC1L1 PTV: 102 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 PCSK9 ClinVar: 23 rows, 6 without alleles, 5 outside gene region
[info]  2026-10-01 09:58:41 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 PCSK9 PTV: 85 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 09:58:41 PPARA ClinVar: 33 rows, 33 without alleles, 33 outside gene region
[info]  2026-10-01 09:58:41 PPARA PTV: 26 rows, 0 without alleles, 0 outside gene region
[stage] 2026-10-01 09:58:41 load_gwas
[info]  2026-10-01 09:59:08 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv.gz: 598192 rows, 597469 variant-level (summary-stats, curated)
[info]  2026-10-01 09:59:10 summary-stats: 973 rows without chrom/pos or effect allele, cannot be matched
[info]  2026-10-01 09:59:10 curated: 420 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-01 09:59:11 match
[info]  2026-10-01 09:59:11 ANGPTL3 ClinVar: 10 variants, 0 matched, GWAS rows: none
[info]  2026-10-01 09:59:11 ANGPTL3 PTV: 57 variants, 9 matched, GWAS rows: summary-stats=255
[info]  2026-10-01 09:59:11 CETP ClinVar: 308 variants, 140 matched, GWAS rows: summary-stats=5300 curated=32
[info]  2026-10-01 09:59:11 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=12 curated=5
[info]  2026-10-01 09:59:11 CETP PTV: 61 variants, 17 matched, GWAS rows: summary-stats=343
[info]  2026-10-01 09:59:11 CETP landfors_paper: 94 variants, 23 matched, GWAS rows: summary-stats=531
[info]  2026-10-01 09:59:11 HMGCR ClinVar: 8 variants, 0 matched, GWAS rows: none
[info]  2026-10-01 09:59:11 HMGCR PTV: 40 variants, 1 matched, GWAS rows: summary-stats=6
[info]  2026-10-01 09:59:11 NPC1L1 PTV: 102 variants, 22 matched, GWAS rows: summary-stats=337
[info]  2026-10-01 09:59:11 PCSK9 ClinVar: 17 variants, 3 matched, GWAS rows: summary-stats=38
[info]  2026-10-01 09:59:11 PCSK9 GoF: 18 variants, 8 matched, GWAS rows: summary-stats=287
[info]  2026-10-01 09:59:11 PCSK9 PTV: 85 variants, 18 matched, GWAS rows: summary-stats=358 curated=3
[info]  2026-10-01 09:59:11 PPARA PTV: 26 variants, 2 matched, GWAS rows: summary-stats=25
[info]  2026-10-01 09:59:11 no ensembl_variant_id column: a1-vs-Ensembl-ref check skipped
[stage] 2026-10-01 09:59:11 write
[info]  2026-10-01 09:59:12 wrote 7532 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz

```

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --group-by variant`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-01 10:26:24
- commit: `f98a0d0`

Output:
```text
[info]  2026-10-01 10:26:15 grouping variant: variant_site, outcome
[stage] 2026-10-01 10:26:15 load_matched
[info]  2026-10-01 10:26:15 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz: 7532 rows, 217 variants
[stage] 2026-10-01 10:26:15 prepare_effects
[info]  2026-10-01 10:26:15 3 rows dropped: no beta or odds ratio
[info]  2026-10-01 10:26:15 6 rows dropped: no SE and p missing, 0 or 1
[info]  2026-10-01 10:26:15 7523 usable rows, 663 with SE derived from p
[stage] 2026-10-01 10:26:15 orient
[info]  2026-10-01 10:26:15 114 variants oriented as ldl_lowering
[info]  2026-10-01 10:26:15 98 variants oriented as a2
[info]  2026-10-01 10:26:15 4 variants oriented as a2_gof_flipped
[stage] 2026-10-01 10:26:15 dedupe
[info]  2026-10-01 10:26:15 617 duplicate rows removed
[stage] 2026-10-01 10:26:15 meta_analyse
[info]  2026-10-01 10:26:18 1237 groups, 1034 pooling more than one estimate
[stage] 2026-10-01 10:26:18 write
[info]  2026-10-01 10:26:18 wrote 1237 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_variant.tsv.gz

```
