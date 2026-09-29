## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-29 11:16:00
- commit: `ad58101` (dirty)

Output:
```text
[info]  2026-09-29 10:19:59 9 genes, 50 icd codes
[stage] 2026-09-29 10:19:59 resolve_genes
[stage] 2026-09-29 10:19:59 resolve_efo
[info]  2026-09-29 10:20:01 trait ids checked: 24, obsolete replaced: 0
[info]  2026-09-29 10:20:01 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-09-29 10:20:01 discover_gwas
[info]  2026-09-29 10:21:49 EFO_0003913 (exact): 56 studies -> 51 with full sumstats -> 10 included
[info]  2026-09-29 10:27:03 EFO_0004614 (exact): 126 studies -> 101 with full sumstats -> 10 included
[info]  2026-09-29 10:30:37 EFO_0004615 (exact): 128 studies -> 103 with full sumstats -> 10 included
[info]  2026-09-29 10:31:03 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-29 10:31:31 EFO_0008584 (exact): 2 studies -> 2 with full sumstats -> 2 included
[info]  2026-09-29 10:33:06 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-29 10:34:43 EFO_0022264 (exact): 52 studies -> 51 with full sumstats -> 10 included
[info]  2026-09-29 10:36:26 EFO_0022266 (exact): 52 studies -> 51 with full sumstats -> 10 included
[info]  2026-09-29 10:37:51 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 3 with full sumstats -> 3 included
[info]  2026-09-29 10:38:17 MONDO_0004781 (exact): 11 studies -> 10 with full sumstats -> 10 included
[info]  2026-09-29 10:48:28 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 50 with full sumstats -> 20 included
[info]  2026-09-29 10:56:53 MONDO_0005010 (exact): 207 studies -> 93 with full sumstats -> 10 included
[info]  2026-09-29 11:02:30 MONDO_0005098 (exact): 134 studies -> 87 with full sumstats -> 10 included
[info]  2026-09-29 11:03:11 MONDO_0005099 (exact): 19 studies -> 12 with full sumstats -> 10 included
[info]  2026-09-29 11:06:01 MONDO_0005252 (exact): 77 studies -> 58 with full sumstats -> 10 included
[info]  2026-09-29 11:08:10 MONDO_0005267 (exact): 58 studies -> 54 with full sumstats -> 10 included
[info]  2026-09-29 11:09:54 MONDO_0005294 (exact): 55 studies -> 47 with full sumstats -> 10 included
[info]  2026-09-29 11:12:03 MONDO_0005311 (exact): 34 studies -> 28 with full sumstats -> 10 included
[info]  2026-09-29 11:12:58 MONDO_0005394 (exact): 10 studies -> 6 with full sumstats -> 6 included
[info]  2026-09-29 11:13:29 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-29 11:14:27 MONDO_0013792 (exact): 30 studies -> 17 with full sumstats -> 10 included
[info]  2026-09-29 11:15:55 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-09-29 11:15:55 finngen_manual
[stage] 2026-09-29 11:15:55 write_tasks
[info]  2026-09-29 11:15:55 wrote 188 tasks (211 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-29 11:15:55 archived /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs -> /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs_20260928_223510
[info]  2026-09-29 11:15:58 wrote 1627 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/3_1790693329/run_job_array.job --task-id 21 --step 10`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-29 16:13:04
- commit: `a97941b`

Δ vs previous run (was `a97941b`):
```diff
@@ -1,22 +1,7 @@
-[info]  2026-09-29 16:06:27 rows 11-20 of 23, 9 gene regions
-[info]  2026-09-29 16:06:31 APOB @ chr2: chromosome not in http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473596/harmonised/GCST90473596.h.tsv.gz -> 0 rows
-[info]  2026-09-29 16:06:31 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473596/harmonised/GCST90473596.h.tsv.gz @ 9 regions -> 8859 rows with MAF < 0.01
-[info]  2026-09-29 16:06:31 GCST90473596: 8859 rows over 8 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473596_result.tsv.gz
-[info]  2026-09-29 16:06:34 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90480001-GCST90481000/GCST90480200/harmonised/GCST90480200.h.tsv.gz @ 9 regions -> 1912 rows with MAF < 0.01
-[info]  2026-09-29 16:06:34 GCST90480200: 1912 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90480200_result.tsv.gz
-[info]  2026-09-29 16:07:20 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90480001-GCST90481000/GCST90480198/GCST90480198.tsv.gz @ 9 regions -> 0 rows with MAF < 0.01 (raw scan)
-[info]  2026-09-29 16:07:20 GCST90480198: 0 rows over 0 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90480198_result.tsv.gz
-[info]  2026-09-29 16:07:27 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90480001-GCST90481000/GCST90480197/harmonised/GCST90480197.h.tsv.gz @ 9 regions -> 1915 rows with MAF < 0.01
-[info]  2026-09-29 16:07:27 GCST90480197: 1915 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90480197_result.tsv.gz
-[info]  2026-09-29 16:07:30 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90478001-GCST90479000/GCST90478009/harmonised/GCST90478009.h.tsv.gz @ 9 regions -> 1674 rows with MAF < 0.01
-[info]  2026-09-29 16:07:30 GCST90478009: 1674 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90478009_result.tsv.gz
-[info]  2026-09-29 16:07:34 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90478001-GCST90479000/GCST90478008/harmonised/GCST90478008.h.tsv.gz @ 9 regions -> 3070 rows with MAF < 0.01
-[info]  2026-09-29 16:07:35 GCST90478008: 3070 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90478008_result.tsv.gz
-[info]  2026-09-29 16:07:38 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90726001-GCST90727000/GCST90726916/harmonised/GCST90726916.h.tsv.gz @ 9 regions -> 977 rows with MAF < 0.01
-[info]  2026-09-29 16:07:38 GCST90726916: 977 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90726916_result.tsv.gz
-[info]  2026-09-29 16:07:41 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90432001-GCST90433000/GCST90432123/harmonised/GCST90432123.h.tsv.gz @ 9 regions -> 1277 rows with MAF < 0.01
-[info]  2026-09-29 16:07:41 GCST90432123: 1277 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90432123_result.tsv.gz
-[warn]  2026-09-29 16:07:41 'base_pair_location' is not in list
-[info]  2026-09-29 16:07:41 GCST90827342: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90827342_result.tsv.gz
-[warn]  2026-09-29 16:07:42 'base_pair_location' is not in list
-[info]  2026-09-29 16:07:42 GCST90826054: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90826054_result.tsv.gz
+[info]  2026-09-29 16:12:25 rows 21-23 of 23, 9 gene regions
+[info]  2026-09-29 16:12:37 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90692001-GCST90693000/GCST90692207/harmonised/GCST90692207.h.tsv.gz @ 9 regions -> 1392 rows with MAF < 0.01
+[info]  2026-09-29 16:12:43 GCST90692207: 1392 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90692207_result.tsv.gz
+[warn]  2026-09-29 16:12:50 'chromosome' is not in list
+[info]  2026-09-29 16:12:55 GCST90103349: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90103349_result.tsv.gz
+[info]  2026-09-29 16:13:04 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90726001-GCST90727000/GCST90726809/harmonised/GCST90726809.h.tsv.gz @ 9 regions -> 977 rows with MAF < 0.01
+[info]  2026-09-29 16:13:04 GCST90726809: 977 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90726809_result.tsv.gz
```

Output:
```text
[info]  2026-09-29 16:12:25 rows 21-23 of 23, 9 gene regions
[info]  2026-09-29 16:12:37 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90692001-GCST90693000/GCST90692207/harmonised/GCST90692207.h.tsv.gz @ 9 regions -> 1392 rows with MAF < 0.01
[info]  2026-09-29 16:12:43 GCST90692207: 1392 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90692207_result.tsv.gz
[warn]  2026-09-29 16:12:50 'chromosome' is not in list
[info]  2026-09-29 16:12:55 GCST90103349: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90103349_result.tsv.gz
[info]  2026-09-29 16:13:04 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90726001-GCST90727000/GCST90726809/harmonised/GCST90726809.h.tsv.gz @ 9 regions -> 977 rows with MAF < 0.01
[info]  2026-09-29 16:13:04 GCST90726809: 977 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90726809_result.tsv.gz

```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-09-29 15:32:35
- commit: `115d137`
- status: failed

Output:
```text
[info]  2026-09-29 15:02:19 task 101: rows 101-110
[error] 2026-09-29 15:32:35 run_mamba: '/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/2_1790685109/run_job_array.job --task-id 101 --step 10' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-09-29 15:02:19 repo root=/myriadfs/home/rmgpmva/projects/lipid_adem
[info]  2026-09-29 15:02:19 === /myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.sh ===
[info]  2026-09-29 15:02:19 started at Tue 29 Sep 15:02:19 BST 2026
[info]  2026-09-29 15:02:19 hostname=node-t00a-007.myriad.ucl.ac.uk
[info]  2026-09-29 15:02:19 job array file=/myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/2_1790685109/run_job_array.job
[info]  2026-09-29 15:02:19 temp location=/myriadfs/home/rmgpmva/Scratch/lipid_adem/filter_task_tmp
[info]  2026-09-29 15:02:19 step=10
[info]  2026-09-29 15:02:19 task 101: rows 101-110
[info]  2026-09-29 15:02:20 rows 101-110 of 158, 9 gene regions
[debug] 2026-09-29 15:05:20 header columns: chrom=0 pos=1 maf=6
[debug] 2026-09-29 15:05:21 CETP @ 16:56951980-56993663 -> 236 rows
[debug] 2026-09-29 15:05:21 HMGCR @ 5:75332606-75370339 -> 136 rows
[debug] 2026-09-29 15:05:22 NPC1L1 @ 7:44503450-44551259 -> 147 rows
[debug] 2026-09-29 15:05:22 PCSK9 @ 1:55029838-55073581 -> 158 rows
[debug] 2026-09-29 15:05:22 ANGPTL3 @ 1:62587567-62614814 -> 53 rows
[debug] 2026-09-29 15:05:23 PPARA @ 22:46188384-46245377 -> 139 rows
[debug] 2026-09-29 15:05:23 APOA1 @ 11:116824677-116852065 -> 124 rows
[debug] 2026-09-29 15:05:24 APOB @ 2:20991305-21054075 -> 313 rows
[debug] 2026-09-29 15:05:24 APOE @ 19:44893787-44919396 -> 90 rows
[info]  2026-09-29 15:05:24 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90692001-GCST90693000/GCST90692840/harmonised/GCST90692840.h.tsv.gz @ 9 regions -> 1396 rows with MAF < 0.01
[info]  2026-09-29 15:05:24 GCST90692840: 1396 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90692840_result.tsv.gz
[debug] 2026-09-29 15:16:24 header columns: chrom=1 pos=2 maf=12
[info]  2026-09-29 15:16:25 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90083001-GCST90084000/GCST90083960/GCST90083960_buildGRCh38.tsv.gz @ 9 regions -> 139 rows with MAF < 0.01 (raw scan)
[info]  2026-09-29 15:16:25 GCST90083960: 139 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90083960_result.tsv.gz
[debug] 2026-09-29 15:17:52 header columns: chrom=2 pos=3 maf=10
[info]  2026-09-29 15:17:57 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90079001-GCST90080000/GCST90079974/harmonised/34662886-GCST90079974-EFO_0008584.h.tsv.gz @ 9 regions -> 355 rows with MAF < 0.01 (raw scan)
[info]  2026-09-29 15:17:57 GCST90079974: 355 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90079974_result.tsv.gz
[info]  2026-09-29 15:18:27 GCST90827348: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90827348_result.tsv.gz
[info]  2026-09-29 15:19:57 GCST90827347: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90827347_result.tsv.gz
[info]  2026-09-29 15:20:21 GCST90827346: empty result -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90827346_result.tsv.gz
[debug] 2026-09-29 15:25:48 header columns: chrom=0 pos=1 maf=6
[debug] 2026-09-29 15:25:48 CETP @ 16:56951980-56993663 -> 65 rows
[debug] 2026-09-29 15:25:48 HMGCR @ 5:75332606-75370339 -> 63 rows
[debug] 2026-09-29 15:25:49 NPC1L1 @ 7:44503450-44551259 -> 172 rows
[debug] 2026-09-29 15:25:49 PCSK9 @ 1:55029838-55073581 -> 132 rows
[debug] 2026-09-29 15:25:49 ANGPTL3 @ 1:62587567-62614814 -> 38 rows
[debug] 2026-09-29 15:25:50 PPARA @ 22:46188384-46245377 -> 52 rows
[debug] 2026-09-29 15:25:50 APOA1 @ 11:116824677-116852065 -> 55 rows
[debug] 2026-09-29 15:25:51 APOB @ 2:20991305-21054075 -> 321 rows
[debug] 2026-09-29 15:25:51 APOE @ 19:44893787-44919396 -> 79 rows
[info]  2026-09-29 15:25:51 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90726001-GCST90727000/GCST90726897/harmonised/GCST90726897.h.tsv.gz @ 9 regions -> 977 rows with MAF < 0.01
[info]  2026-09-29 15:25:51 GCST90726897: 977 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90726897_result.tsv.gz
[debug] 2026-09-29 15:32:31 header columns: chrom=2 pos=3 maf=10
[info]  2026-09-29 15:32:35 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90079001-GCST90080000/GCST90079973/harmonised/34662886-GCST90079973-EFO_0008583.h.tsv.gz @ 9 regions -> 353 rows with MAF < 0.01 (raw scan)
[info]  2026-09-29 15:32:35 GCST90079973: 353 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90079973_result.tsv.gz

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-09-28 13:48:15
- commit: `3cbcdce`

Output:
```text
[stage] 2026-09-28 13:36:49 load_sumstats
[info]  2026-09-28 13:36:51 summary-stats: 648 files, 171500 rows (0 missing)
[stage] 2026-09-28 13:36:52 fetch_curated
[info]  2026-09-28 13:37:09 MONDO_0004648: 120 fetched; in region: none
[info]  2026-09-28 13:42:17 EFO_0004614: 2375 fetched; in region: CETP=21 ANGPTL3=4 APOA1=10 APOB=6 APOE=10
[info]  2026-09-28 13:46:05 EFO_0004615: 1772 fetched; in region: CETP=6 HMGCR=1 NPC1L1=1 PCSK9=14 APOA1=2 APOB=24 APOE=22
[info]  2026-09-28 13:46:54 EFO_0003913: 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
[info]  2026-09-28 13:47:39 EFO_0022264: 316 fetched; in region: CETP=1 APOA1=1 APOB=1 APOE=3
[info]  2026-09-28 13:47:59 EFO_0022266: 151 fetched; in region: CETP=1 HMGCR=1 NPC1L1=1 APOE=3
[info]  2026-09-28 13:48:04 EFO_0006799: 40 fetched; in region: none
[info]  2026-09-28 13:48:07 EFO_0011057: 14 fetched; in region: none
[info]  2026-09-28 13:48:10 EFO ids with 0 curated associations: 16
[stage] 2026-09-28 13:48:10 gene_burden
[info]  2026-09-28 13:48:11 gene-burden rows: PCSK9=4 ANGPTL3=5 APOB=7 (6 genes with 0)
[stage] 2026-09-28 13:48:11 write
[info]  2026-09-28 13:48:15 wrote 171658 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv

```
