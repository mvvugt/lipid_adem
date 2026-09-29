## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-28 22:28:55
- commit: `4f133a2`

Output:
```text
[info]  2026-09-28 22:24:19 9 genes, 50 icd codes
[stage] 2026-09-28 22:24:19 resolve_genes
[stage] 2026-09-28 22:24:19 resolve_efo
[warn]  2026-09-28 22:24:19 obsolete trait id EFO_0000249 -> MONDO_0004975
[warn]  2026-09-28 22:24:19 obsolete trait id EFO_0003763 -> MONDO_0011057
[warn]  2026-09-28 22:24:19 obsolete trait id EFO_0003144 -> MONDO_0005252
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0000713 -> MONDO_0005099
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0005669 -> MONDO_0013792
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0004277 -> MONDO_0005394
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0000712 -> MONDO_0005098
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0003914 -> MONDO_0005311
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0003875 -> MONDO_0005294
[warn]  2026-09-28 22:24:20 obsolete trait id EFO_0008583 -> MONDO_0004781
[warn]  2026-09-28 22:24:21 obsolete trait id EFO_0003777 -> MONDO_0005267
[warn]  2026-09-28 22:24:21 obsolete trait id EFO_0001645 -> MONDO_0005010
[info]  2026-09-28 22:24:21 trait ids checked: 24, obsolete replaced: 12
[info]  2026-09-28 22:24:21 wrote resolved efo_ids to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/icd_codes.txt
[stage] 2026-09-28 22:24:21 discover_gwas
[info]  2026-09-28 22:24:30 EFO_0003913 (exact): 56 studies -> 51 with full sumstats -> 10 included
[info]  2026-09-28 22:24:47 EFO_0004614 (exact): 126 studies -> 101 with full sumstats -> 10 included
[info]  2026-09-28 22:25:06 EFO_0004615 (exact): 128 studies -> 103 with full sumstats -> 10 included
[info]  2026-09-28 22:25:08 EFO_0006799 (with child traits, cap per term): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-28 22:25:10 EFO_0008584 (exact): 2 studies -> 2 with full sumstats -> 2 included
[info]  2026-09-28 22:25:13 EFO_0011057 (with child traits, cap per term): 4 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-28 22:25:22 EFO_0022264 (exact): 52 studies -> 51 with full sumstats -> 10 included
[info]  2026-09-28 22:25:29 EFO_0022266 (exact): 52 studies -> 51 with full sumstats -> 10 included
[info]  2026-09-28 22:25:33 MONDO_0004648 (with child traits, cap per term): 15 studies -> 3 with full sumstats -> 3 included
[info]  2026-09-28 22:25:36 MONDO_0004781 (exact): 11 studies -> 10 with full sumstats -> 10 included
[info]  2026-09-28 22:26:12 MONDO_0004975 (with child traits, cap per term): 261 studies -> 50 with full sumstats -> 20 included
[info]  2026-09-28 22:26:44 MONDO_0005010 (exact): 207 studies -> 93 with full sumstats -> 10 included
[info]  2026-09-28 22:27:03 MONDO_0005098 (exact): 134 studies -> 87 with full sumstats -> 10 included
[info]  2026-09-28 22:27:06 MONDO_0005099 (exact): 19 studies -> 12 with full sumstats -> 10 included
[info]  2026-09-28 22:27:17 MONDO_0005252 (exact): 77 studies -> 58 with full sumstats -> 10 included
[info]  2026-09-28 22:27:24 MONDO_0005267 (exact): 58 studies -> 54 with full sumstats -> 10 included
[info]  2026-09-28 22:27:31 MONDO_0005294 (exact): 55 studies -> 47 with full sumstats -> 10 included
[info]  2026-09-28 22:27:37 MONDO_0005311 (exact): 34 studies -> 28 with full sumstats -> 10 included
[info]  2026-09-28 22:27:39 MONDO_0005394 (exact): 10 studies -> 6 with full sumstats -> 6 included
[info]  2026-09-28 22:27:41 MONDO_0008243 (with child traits, cap per term): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-09-28 22:28:48 MONDO_0011057 (with child traits, cap per term): 518 studies -> 305 with full sumstats -> 180 included
[info]  2026-09-28 22:28:54 MONDO_0013792 (exact): 30 studies -> 17 with full sumstats -> 10 included
[info]  2026-09-28 22:28:55 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-09-28 22:28:55 finngen_manual
[stage] 2026-09-28 22:28:55 write_tasks
[info]  2026-09-28 22:28:55 wrote 3492 tasks to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-28 22:28:55 wrote 2145 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene CETP --study-accession GCST90477988 --chrom 16 --start 56951980 --end 56993663 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/CETP_GCST90477988_result.tsv.gz --source gwas_catalog`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-29 09:49:23
- commit: `9ffb828`

Δ vs previous run (was `9ffb828`):
- error resolved
```diff
@@ -1,23 +1,2 @@
-Traceback (most recent call last):
-  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 244, in main
-    run_filter(
-    ~~~~~~~~~~^
-        gene=args.gene,
-        ^^^^^^^^^^^^^^^
-    ...<5 lines>...
-        source=args.source,
-        ^^^^^^^^^^^^^^^^^^^
-    )
-    ^
-  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 195, in run_filter
-    filtered = _run_filter_gwas_catalog(
-        gene, study_accession, region, outfile
-    )
-  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 70, in _run_filter_gwas_catalog
-    location = functions.study_summary_stats_location(study_accession)
-  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 1656, in study_summary_stats_location
-    response.raise_for_status()
-    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
-  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/models.py", line 1167, in raise_for_status
-    raise HTTPError(http_error_msg, response=self)
-requests.exceptions.HTTPError: 500 Server Error:  for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477989
+[info]  2026-09-29 09:49:23 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90477001-GCST90478000/GCST90477988/GCST90477988.tsv.gz @ 16:56951980-56993663 -> 0 rows with MAF < 0.01 (raw scan)
+[info]  2026-09-29 09:49:23 CETP x GCST90477988: 0 rows -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/CETP_GCST90477988_result.tsv.gz
```

Output:
```text
[info]  2026-09-29 09:49:23 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90477001-GCST90478000/GCST90477988/GCST90477988.tsv.gz @ 16:56951980-56993663 -> 0 rows with MAF < 0.01 (raw scan)
[info]  2026-09-29 09:49:23 CETP x GCST90477988: 0 rows -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/CETP_GCST90477988_result.tsv.gz

```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-09-29 09:38:53
- commit: `9ffb828`
- status: failed

Output:
```text
[info]  2026-09-29 09:38:19 task 119: gene=CETP study_accession=GCST90477989 source=gwas_catalog
[error] 2026-09-29 09:38:51 run_mamba: '/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene CETP --study-accession GCST90477989 --chrom 16 --start 56951980 --end 56993663 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/CETP_GCST90477989_result.tsv.gz --source gwas_catalog' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-09-29 09:38:19 repo root=/myriadfs/home/rmgpmva/projects/lipid_adem
[info]  2026-09-29 09:38:19 === /myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.sh ===
[info]  2026-09-29 09:38:19 started at Tue 29 Sep 09:38:19 BST 2026
[info]  2026-09-29 09:38:19 hostname=node-b00a-007.myriad.ucl.ac.uk
[info]  2026-09-29 09:38:19 job array file=/myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/1_1790631293/run_job_array.job
[info]  2026-09-29 09:38:19 temp location=/myriadfs/home/rmgpmva/Scratch/lipid_adem/filter_task_tmp
[info]  2026-09-29 09:38:19 step=1
[info]  2026-09-29 09:38:19 task 119: gene=CETP study_accession=GCST90477989 source=gwas_catalog
[info]  2026-09-29 09:38:19 outfile=/myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/CETP_GCST90477989_result.tsv.gz

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
