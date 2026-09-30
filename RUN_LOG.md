## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-30 08:16:05
- commit: `a361304`

Output:
```text
[info]  2026-09-30 07:58:21 9 genes, 50 icd codes
[stage] 2026-09-30 07:58:21 resolve_genes
[stage] 2026-09-30 07:58:21 resolve_efo
[info]  2026-09-30 07:58:23 trait ids checked: 24, obsolete replaced: 0
[info]  2026-09-30 07:58:23 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
[info]  2026-09-30 07:58:23 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
[info]  2026-09-30 07:58:23 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-09-30 07:58:23 discover_gwas
[info]  2026-09-30 07:59:26 EFO_0003913 (exact): 56 studies -> 44 with full sumstats -> 10 included
[info]  2026-09-30 08:06:37 EFO_0004611 (exact): 742 studies -> 337 with full sumstats -> 10 included
[info]  2026-09-30 08:08:33 EFO_0004612 (exact): 718 studies -> 261 with full sumstats -> 10 included
[info]  2026-09-30 08:08:52 EFO_0004614 (exact): 126 studies -> 72 with full sumstats -> 10 included
[info]  2026-09-30 08:09:19 EFO_0004615 (exact): 128 studies -> 75 with full sumstats -> 10 included
[info]  2026-09-30 08:09:21 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-30 08:09:24 EFO_0008584 (exact): 2 studies -> 2 with full sumstats -> 2 included
[info]  2026-09-30 08:09:29 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-30 08:09:39 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 3 with full sumstats -> 3 included
[info]  2026-09-30 08:09:47 MONDO_0004781 (exact): 11 studies -> 6 with full sumstats -> 6 included
[info]  2026-09-30 08:12:11 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 47 with full sumstats -> 20 included
[info]  2026-09-30 08:14:25 MONDO_0005010 (exact): 207 studies -> 69 with full sumstats -> 10 included
[info]  2026-09-30 08:15:19 MONDO_0005098 (exact): 134 studies -> 65 with full sumstats -> 10 included
[info]  2026-09-30 08:15:23 MONDO_0005099 (exact): 19 studies -> 12 with full sumstats -> 10 included
[info]  2026-09-30 08:15:34 MONDO_0005252 (exact): 77 studies -> 57 with full sumstats -> 10 included
[info]  2026-09-30 08:15:41 MONDO_0005267 (exact): 58 studies -> 48 with full sumstats -> 10 included
[info]  2026-09-30 08:15:48 MONDO_0005294 (exact): 55 studies -> 44 with full sumstats -> 10 included
[info]  2026-09-30 08:15:54 MONDO_0005311 (exact): 34 studies -> 28 with full sumstats -> 10 included
[info]  2026-09-30 08:15:56 MONDO_0005394 (exact): 10 studies -> 6 with full sumstats -> 6 included
[info]  2026-09-30 08:15:58 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-30 08:16:03 MONDO_0013792 (exact): 30 studies -> 17 with full sumstats -> 10 included
[info]  2026-09-30 08:16:04 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-09-30 08:16:04 finngen_manual
[stage] 2026-09-30 08:16:05 write_tasks
[info]  2026-09-30 08:16:05 wrote 184 tasks (207 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-30 08:16:05 wrote 2983 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/2_1790758974/run_job_array.job --task-id 11 --step 10`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-30 10:09:41
- commit: `a361304`

Output:
```text
[info]  2026-09-30 10:08:31 rows 11-14 of 14, 9 gene regions
[info]  2026-09-30 10:08:37 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90668001-GCST90669000/GCST90668074/GCST90668074.tsv.gz @ 9 regions -> 0 rows with MAF < 0.01 (raw scan)
[info]  2026-09-30 10:08:46 GCST90668074: 0 rows over 0 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90668074_result.tsv.gz
[info]  2026-09-30 10:08:59 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473578/harmonised/GCST90473578.h.tsv.gz @ 9 regions -> 10525 rows with MAF < 0.01
[info]  2026-09-30 10:09:08 GCST90473578: 10525 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473578_result.tsv.gz
[info]  2026-09-30 10:09:15 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473577/harmonised/GCST90473577.h.tsv.gz @ 9 regions -> 1739 rows with MAF < 0.01
[info]  2026-09-30 10:09:21 GCST90473577: 1739 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473577_result.tsv.gz
[info]  2026-09-30 10:09:28 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473553/harmonised/GCST90473553.h.tsv.gz @ 9 regions -> 1047 rows with MAF < 0.01
[info]  2026-09-30 10:09:35 GCST90473553: 1047 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473553_result.tsv.gz

```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-09-30 09:10:37
- commit: `a361304`
- status: failed

Output:
```text
[info]  2026-09-30 09:10:32 task 41: rows 41-50
[error] 2026-09-30 09:10:37 run_mamba: '/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/1_1790753607/run_job_array.job --task-id 41 --step 10' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-09-30 09:10:32 repo root=/myriadfs/home/rmgpmva/projects/lipid_adem
[info]  2026-09-30 09:10:32 === /myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.sh ===
[info]  2026-09-30 09:10:32 started at Wed 30 Sep 09:10:32 BST 2026
[info]  2026-09-30 09:10:32 hostname=node-t00a-001.myriad.ucl.ac.uk
[info]  2026-09-30 09:10:32 job array file=/myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/1_1790753607/run_job_array.job
[info]  2026-09-30 09:10:32 temp location=/myriadfs/home/rmgpmva/Scratch/lipid_adem/filter_task_tmp
[info]  2026-09-30 09:10:32 step=10
[info]  2026-09-30 09:10:32 task 41: rows 41-50
[info]  2026-09-30 09:10:35 rows 41-50 of 73, 9 gene regions
[debug] 2026-09-30 09:10:35 header columns: chrom=0 pos=1 maf=6
[debug] 2026-09-30 09:10:35 CETP @ 16:56951980-56993663 -> 1302 rows
[debug] 2026-09-30 09:10:35 HMGCR @ 5:75332606-75370339 -> 984 rows
[debug] 2026-09-30 09:10:35 NPC1L1 @ 7:44503450-44551259 -> 1277 rows
[debug] 2026-09-30 09:10:35 PCSK9 @ 1:55029838-55073581 -> 1199 rows
[debug] 2026-09-30 09:10:35 ANGPTL3 @ 1:62587567-62614814 -> 647 rows
[debug] 2026-09-30 09:10:35 PPARA @ 22:46188384-46245377 -> 1691 rows
[debug] 2026-09-30 09:10:35 APOA1 @ 11:116824677-116852065 -> 835 rows
[debug] 2026-09-30 09:10:35 APOB @ 2:20991305-21054075 -> 1666 rows
[debug] 2026-09-30 09:10:35 APOE @ 19:44893787-44919396 -> 924 rows
[info]  2026-09-30 09:10:35 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473533/harmonised/GCST90473533.h.tsv.gz @ 9 regions -> 10525 rows with MAF < 0.01
[info]  2026-09-30 09:10:35 GCST90473533: 10525 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473533_result.tsv.gz
[debug] 2026-09-30 09:10:36 header columns: chrom=0 pos=1 maf=6
[debug] 2026-09-30 09:10:36 CETP @ 16:56951980-56993663 -> 41 rows
[debug] 2026-09-30 09:10:36 HMGCR @ 5:75332606-75370339 -> 52 rows
[debug] 2026-09-30 09:10:36 NPC1L1 @ 7:44503450-44551259 -> 20 rows
[debug] 2026-09-30 09:10:36 PCSK9 @ 1:55029838-55073581 -> 30 rows
[debug] 2026-09-30 09:10:36 ANGPTL3 @ 1:62587567-62614814 -> 24 rows
[debug] 2026-09-30 09:10:36 PPARA @ 22:46188384-46245377 -> 50 rows
[debug] 2026-09-30 09:10:36 APOA1 @ 11:116824677-116852065 -> 39 rows
[debug] 2026-09-30 09:10:36 APOB @ 2:20991305-21054075 -> 34 rows
[debug] 2026-09-30 09:10:36 APOE @ 19:44893787-44919396 -> 24 rows
[info]  2026-09-30 09:10:36 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473528/harmonised/GCST90473528.h.tsv.gz @ 9 regions -> 314 rows with MAF < 0.01
[info]  2026-09-30 09:10:36 GCST90473528: 314 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473528_result.tsv.gz
[debug] 2026-09-30 09:10:36 header columns: chrom=0 pos=1 maf=6
[debug] 2026-09-30 09:10:36 CETP @ 16:56951980-56993663 -> 260 rows
[debug] 2026-09-30 09:10:36 HMGCR @ 5:75332606-75370339 -> 172 rows
[debug] 2026-09-30 09:10:36 NPC1L1 @ 7:44503450-44551259 -> 166 rows
[debug] 2026-09-30 09:10:36 PCSK9 @ 1:55029838-55073581 -> 210 rows

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-09-30 14:07:34
- commit: `081c98b`

Δ vs previous run (was `a361304`):
- error resolved
```diff
@@ -1,2 +1,2 @@
-[info]  2026-09-30 10:35:58 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
-[info]  2026-09-30 10:35:58 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
+[info]  2026-09-30 12:50:23 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
+[info]  2026-09-30 12:50:23 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
```
stage `load_sumstats`:
```diff
@@ -1,2 +1,2 @@
-[info]  2026-09-30 10:36:00 summary-stats: 184 files, 426693 rows incl. one copy per outcome (0 missing)
-[info]  2026-09-30 10:36:02 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
+[info]  2026-09-30 12:50:25 summary-stats: 184 files, 426693 rows incl. one copy per outcome (0 missing)
+[info]  2026-09-30 12:50:26 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
```
stage `fetch_curated`:
```diff
@@ -1,15 +1,20 @@
-[info]  2026-09-30 10:51:37 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
-[info]  2026-09-30 10:51:54 MONDO_0004648 (with child traits): 120 fetched; in region: none
-[info]  2026-09-30 10:56:35 EFO_0004614 (exact): 2375 fetched; in region: CETP=21 ANGPTL3=4 APOA1=10 APOB=6 APOE=10
-[info]  2026-09-30 11:00:05 EFO_0004615 (exact): 1772 fetched; in region: CETP=6 HMGCR=1 NPC1L1=1 PCSK9=14 APOA1=2 APOB=24 APOE=22
-[info]  2026-09-30 11:01:44 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
-[info]  2026-09-30 11:01:47 MONDO_0005099 (exact): 15 fetched; in region: none
-[info]  2026-09-30 11:01:53 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
-[info]  2026-09-30 11:01:59 MONDO_0005394 (exact): 41 fetched; in region: none
-[info]  2026-09-30 11:02:39 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
-[info]  2026-09-30 11:02:48 MONDO_0005311 (exact): 74 fetched; in region: CETP=1
-[info]  2026-09-30 11:03:00 MONDO_0005294 (exact): 92 fetched; in region: none
-[info]  2026-09-30 11:03:39 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
-[info]  2026-09-30 11:03:42 MONDO_0004781 (exact): 17 fetched; in region: none
-[info]  2026-09-30 11:03:50 MONDO_0005267 (exact): 55 fetched; in region: none
-[info]  2026-09-30 11:11:16 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14
+[info]  2026-09-30 13:01:13 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
+[info]  2026-09-30 13:01:23 MONDO_0004648 (with child traits): 120 fetched; in region: none
+[info]  2026-09-30 13:05:09 EFO_0004614 (exact): 2375 fetched; in region: CETP=21 ANGPTL3=4 APOA1=10 APOB=6 APOE=10
+[info]  2026-09-30 13:07:20 EFO_0004615 (exact): 1772 fetched; in region: CETP=6 HMGCR=1 NPC1L1=1 PCSK9=14 APOA1=2 APOB=24 APOE=22
+[info]  2026-09-30 13:08:35 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
+[info]  2026-09-30 13:08:38 MONDO_0005099 (exact): 15 fetched; in region: none
+[info]  2026-09-30 13:08:43 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
+[info]  2026-09-30 13:08:47 MONDO_0005394 (exact): 41 fetched; in region: none
+[info]  2026-09-30 13:09:14 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
+[info]  2026-09-30 13:09:21 MONDO_0005311 (exact): 74 fetched; in region: CETP=1
+[info]  2026-09-30 13:09:30 MONDO_0005294 (exact): 92 fetched; in region: none
+[info]  2026-09-30 13:09:54 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
+[info]  2026-09-30 13:09:57 MONDO_0004781 (exact): 17 fetched; in region: none
+[info]  2026-09-30 13:10:03 MONDO_0005267 (exact): 55 fetched; in region: none
+[info]  2026-09-30 13:15:00 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14
+[info]  2026-09-30 13:44:52 EFO_0004612 (exact): 25386 fetched; in region: CETP=145 PCSK9=3 ANGPTL3=4 PPARA=1 APOA1=19 APOB=31 APOE=36
+[info]  2026-09-30 14:06:49 EFO_0004611 (exact): 18417 fetched; in region: CETP=33 HMGCR=24 NPC1L1=15 PCSK9=75 ANGPTL3=5 PPARA=2 APOA1=4 APOB=60 APOE=79
+[info]  2026-09-30 14:06:54 EFO_0006799 (with child traits): 40 fetched; in region: none
+[info]  2026-09-30 14:06:57 EFO_0011057 (with child traits): 26 fetched; in region: none
+[info]  2026-09-30 14:07:00 EFO ids with 0 curated associations: 4
```

Output:
```text
[info]  2026-09-30 12:50:23 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
[info]  2026-09-30 12:50:23 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
[stage] 2026-09-30 12:50:23 load_sumstats
[info]  2026-09-30 12:50:25 summary-stats: 184 files, 426693 rows incl. one copy per outcome (0 missing)
[info]  2026-09-30 12:50:26 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-09-30 12:50:26 fetch_curated
[info]  2026-09-30 13:01:13 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
[info]  2026-09-30 13:01:23 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-09-30 13:05:09 EFO_0004614 (exact): 2375 fetched; in region: CETP=21 ANGPTL3=4 APOA1=10 APOB=6 APOE=10
[info]  2026-09-30 13:07:20 EFO_0004615 (exact): 1772 fetched; in region: CETP=6 HMGCR=1 NPC1L1=1 PCSK9=14 APOA1=2 APOB=24 APOE=22
[info]  2026-09-30 13:08:35 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
[info]  2026-09-30 13:08:38 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-09-30 13:08:43 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[info]  2026-09-30 13:08:47 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-09-30 13:09:14 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-09-30 13:09:21 MONDO_0005311 (exact): 74 fetched; in region: CETP=1
[info]  2026-09-30 13:09:30 MONDO_0005294 (exact): 92 fetched; in region: none
[info]  2026-09-30 13:09:54 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
[info]  2026-09-30 13:09:57 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-09-30 13:10:03 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-09-30 13:15:00 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14
[info]  2026-09-30 13:44:52 EFO_0004612 (exact): 25386 fetched; in region: CETP=145 PCSK9=3 ANGPTL3=4 PPARA=1 APOA1=19 APOB=31 APOE=36
[info]  2026-09-30 14:06:49 EFO_0004611 (exact): 18417 fetched; in region: CETP=33 HMGCR=24 NPC1L1=15 PCSK9=75 ANGPTL3=5 PPARA=2 APOA1=4 APOB=60 APOE=79
[info]  2026-09-30 14:06:54 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-09-30 14:06:57 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-09-30 14:07:00 EFO ids with 0 curated associations: 4
[stage] 2026-09-30 14:07:00 gene_burden
[info]  2026-09-30 14:07:00 Open Targets disease ids: 32 (from 23 outcome ids)
[info]  2026-09-30 14:07:01 curated MAF: numeric=23 not_reported=1036
[info]  2026-09-30 14:07:01 gene-burden rows: CETP=135 HMGCR=7 NPC1L1=52 PCSK9=168 ANGPTL3=91 APOA1=61 APOB=207 APOE=2 (1 genes with 0)
[stage] 2026-09-30 14:07:02 write
[info]  2026-09-30 14:07:34 wrote 428475 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-09-30 11:30:47
- commit: `a361304`
- status: failed

Output:
```text
[info]  2026-09-30 10:35:57 using root directory: /home/rmgpmva/projects/lipid_adem
[error] 2026-09-30 11:30:47 run_mamba: '/home/rmgpmva/projects/lipid_adem/src/merge_associations.py' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-09-30 10:35:57 using root directory: /home/rmgpmva/projects/lipid_adem
[info]  2026-09-30 10:35:57 study-outcomes file: /home/rmgpmva/projects/lipid_adem/data/temp/study_outcomes.tsv
[info]  2026-09-30 10:35:57 running on node: node-t00a-001.myriad.ucl.ac.uk, job id: 23026
[info]  2026-09-30 10:35:58 hdl_cholesterol: efo_id EFO_0022264 -> EFO_0004612
[info]  2026-09-30 10:35:58 ldl_cholesterol: efo_id EFO_0022266 -> EFO_0004611
[stage] 2026-09-30 10:35:58 load_sumstats
[info]  2026-09-30 10:36:00 summary-stats: 184 files, 426693 rows incl. one copy per outcome (0 missing)
[info]  2026-09-30 10:36:02 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-09-30 10:36:02 fetch_curated
[debug] 2026-09-30 10:51:37 MONDO_0004975 -> 7069 curated associations fetched
[info]  2026-09-30 10:51:37 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
[debug] 2026-09-30 10:51:54 MONDO_0004648 -> 120 curated associations fetched
[info]  2026-09-30 10:51:54 MONDO_0004648 (with child traits): 120 fetched; in region: none
[debug] 2026-09-30 10:51:56 MONDO_0008243 -> 0 curated associations fetched
[debug] 2026-09-30 10:56:35 EFO_0004614 -> 2375 curated associations fetched
[info]  2026-09-30 10:56:35 EFO_0004614 (exact): 2375 fetched; in region: CETP=21 ANGPTL3=4 APOA1=10 APOB=6 APOE=10
[debug] 2026-09-30 11:00:05 EFO_0004615 -> 1772 curated associations fetched
[info]  2026-09-30 11:00:05 EFO_0004615 (exact): 1772 fetched; in region: CETP=6 HMGCR=1 NPC1L1=1 PCSK9=14 APOA1=2 APOB=24 APOE=22
[debug] 2026-09-30 11:01:44 MONDO_0005252 -> 892 curated associations fetched
[info]  2026-09-30 11:01:44 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
[debug] 2026-09-30 11:01:47 MONDO_0005099 -> 15 curated associations fetched
[info]  2026-09-30 11:01:47 MONDO_0005099 (exact): 15 fetched; in region: none
[debug] 2026-09-30 11:01:53 MONDO_0013792 -> 42 curated associations fetched
[info]  2026-09-30 11:01:53 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[debug] 2026-09-30 11:01:59 MONDO_0005394 -> 41 curated associations fetched
[info]  2026-09-30 11:01:59 MONDO_0005394 (exact): 41 fetched; in region: none
[debug] 2026-09-30 11:02:39 MONDO_0005098 -> 327 curated associations fetched
[info]  2026-09-30 11:02:39 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[debug] 2026-09-30 11:02:48 MONDO_0005311 -> 74 curated associations fetched
[info]  2026-09-30 11:02:48 MONDO_0005311 (exact): 74 fetched; in region: CETP=1
[debug] 2026-09-30 11:03:00 MONDO_0005294 -> 92 curated associations fetched
[info]  2026-09-30 11:03:00 MONDO_0005294 (exact): 92 fetched; in region: none
[debug] 2026-09-30 11:03:39 EFO_0003913 -> 320 curated associations fetched
[info]  2026-09-30 11:03:39 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
[debug] 2026-09-30 11:03:42 MONDO_0004781 -> 17 curated associations fetched
[info]  2026-09-30 11:03:42 MONDO_0004781 (exact): 17 fetched; in region: none
[debug] 2026-09-30 11:03:44 EFO_0008584 -> 0 curated associations fetched
[debug] 2026-09-30 11:03:50 MONDO_0005267 -> 55 curated associations fetched
[info]  2026-09-30 11:03:50 MONDO_0005267 (exact): 55 fetched; in region: none
[debug] 2026-09-30 11:11:16 MONDO_0005010 -> 3913 curated associations fetched
[info]  2026-09-30 11:11:16 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14

```
