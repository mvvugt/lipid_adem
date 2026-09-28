## [10] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene APOE --study-accession GCST90079974 --chrom 19 --start 44893787 --end 44919396 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/APOE_GCST90079974_result.tsv.gz --source gwas_catalog`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-28 12:06:46
- commit: `f5fc276` (dirty)

Δ vs previous run (was `f5fc276` (dirty)):
```diff
@@ -1,2 +1,2 @@
-[info]  2026-09-28 12:03:12 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90079001-GCST90080000/GCST90079974/harmonised/34662886-GCST90079974-EFO_0008584.h.tsv.gz @ 2:20991305-21054075 -> 119 rows with MAF < 0.01 (raw scan)
-[info]  2026-09-28 12:03:12 APOB x GCST90079974: 119 rows -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/APOB_GCST90079974_result.tsv.gz
+[info]  2026-09-28 12:06:46 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90079001-GCST90080000/GCST90079974/harmonised/34662886-GCST90079974-EFO_0008584.h.tsv.gz @ 19:44893787-44919396 -> 15 rows with MAF < 0.01 (raw scan)
+[info]  2026-09-28 12:06:46 APOE x GCST90079974: 15 rows -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/APOE_GCST90079974_result.tsv.gz
```

Output:
```text
[info]  2026-09-28 12:06:46 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90079001-GCST90080000/GCST90079974/harmonised/34662886-GCST90079974-EFO_0008584.h.tsv.gz @ 19:44893787-44919396 -> 15 rows with MAF < 0.01 (raw scan)
[info]  2026-09-28 12:06:46 APOE x GCST90079974: 15 rows -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/APOE_GCST90079974_result.tsv.gz

```

## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-23 17:44:37
- commit: `2e7f9f6`

Output:
```text
[info]  2026-09-23 17:42:38 9 genes, 50 icd codes
[info]  2026-09-23 17:42:40 EFO_0000249 -> 0 studies
[info]  2026-09-23 17:42:40 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:41 EFO_0000712 -> 0 studies
[info]  2026-09-23 17:42:41 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:43 EFO_0000713 -> 0 studies
[info]  2026-09-23 17:42:43 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:45 EFO_0001645 -> 0 studies
[info]  2026-09-23 17:42:45 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:46 EFO_0003144 -> 0 studies
[info]  2026-09-23 17:42:46 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:47 EFO_0003763 -> 0 studies
[info]  2026-09-23 17:42:47 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:49 EFO_0003777 -> 0 studies
[info]  2026-09-23 17:42:49 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:50 EFO_0003875 -> 0 studies
[info]  2026-09-23 17:42:50 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:43:03 EFO_0003913 -> 50 studies
[info]  2026-09-23 17:43:04 50 studies -> 45 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:43:05 EFO_0003914 -> 0 studies
[info]  2026-09-23 17:43:05 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:43:07 EFO_0004277 -> 0 studies
[info]  2026-09-23 17:43:07 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:43:30 EFO_0004614 -> 124 studies
[info]  2026-09-23 17:43:31 124 studies -> 99 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:43:58 EFO_0004615 -> 127 studies
[info]  2026-09-23 17:43:59 127 studies -> 102 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:44:00 EFO_0005669 -> 0 studies
[info]  2026-09-23 17:44:00 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:02 EFO_0006799 -> 1 studies
[info]  2026-09-23 17:44:02 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:04 EFO_0008583 -> 0 studies
[info]  2026-09-23 17:44:04 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:05 EFO_0008584 -> 2 studies
[info]  2026-09-23 17:44:05 2 studies -> 2 with full sumstats -> 2 included after cap=10
[info]  2026-09-23 17:44:07 EFO_0011057 -> 1 studies
[info]  2026-09-23 17:44:08 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:17 EFO_0022264 -> 52 studies
[info]  2026-09-23 17:44:17 52 studies -> 51 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:44:28 EFO_0022266 -> 52 studies
[info]  2026-09-23 17:44:28 52 studies -> 51 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:44:30 MONDO_0000914 -> 0 studies
[info]  2026-09-23 17:44:30 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:33 MONDO_0004648 -> 15 studies
[info]  2026-09-23 17:44:34 15 studies -> 3 with full sumstats -> 3 included after cap=10
[info]  2026-09-23 17:44:35 MONDO_0008243 -> 1 studies
[info]  2026-09-23 17:44:35 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:37 MONDO_0043224 -> 0 studies
[info]  2026-09-23 17:44:37 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:37 wrote 675 tasks to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-23 17:44:37 wrote 458 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv

```

## [10] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-09-28 11:17:55
- commit: `f5fc276` (dirty)

Output:
```text
[info]  2026-09-28 11:07:42 EFO_0000249 -> 0 curated associations fetched
[info]  2026-09-28 11:07:42 EFO_0000249 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:07:42 EFO_0000249 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 -> 120 curated associations fetched
[info]  2026-09-28 11:07:56 MONDO_0004648 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:07:56 MONDO_0004648 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 -> 0 curated associations fetched
[info]  2026-09-28 11:07:57 MONDO_0008243 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:07:57 MONDO_0008243 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 -> 0 curated associations fetched
[info]  2026-09-28 11:07:59 EFO_0003763 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:07:59 EFO_0003763 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 -> 2375 curated associations fetched
[info]  2026-09-28 11:12:28 EFO_0004614 / CETP -> 21 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / ANGPTL3 -> 4 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / APOA1 -> 10 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / APOB -> 6 curated associations in region
[info]  2026-09-28 11:12:28 EFO_0004614 / APOE -> 10 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 -> 1772 curated associations fetched
[info]  2026-09-28 11:15:47 EFO_0004615 / CETP -> 6 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / HMGCR -> 1 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / NPC1L1 -> 1 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / PCSK9 -> 14 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / APOA1 -> 2 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / APOB -> 24 curated associations in region
[info]  2026-09-28 11:15:47 EFO_0004615 / APOE -> 22 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 -> 0 curated associations fetched
[info]  2026-09-28 11:15:48 EFO_0003144 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:48 EFO_0003144 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 -> 0 curated associations fetched
[info]  2026-09-28 11:15:49 EFO_0000713 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:49 EFO_0000713 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 -> 0 curated associations fetched
[info]  2026-09-28 11:15:51 EFO_0005669 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:51 EFO_0005669 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 -> 0 curated associations fetched
[info]  2026-09-28 11:15:52 EFO_0004277 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:52 EFO_0004277 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 -> 0 curated associations fetched
[info]  2026-09-28 11:15:54 EFO_0000712 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:54 EFO_0000712 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 -> 0 curated associations fetched
[info]  2026-09-28 11:15:55 EFO_0003914 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:55 EFO_0003914 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 -> 0 curated associations fetched
[info]  2026-09-28 11:15:57 EFO_0003875 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:15:57 EFO_0003875 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 -> 320 curated associations fetched
[info]  2026-09-28 11:16:38 EFO_0003913 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / PCSK9 -> 2 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / APOB -> 3 curated associations in region
[info]  2026-09-28 11:16:38 EFO_0003913 / APOE -> 4 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 -> 0 curated associations fetched
[info]  2026-09-28 11:16:39 EFO_0008583 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:16:39 EFO_0008583 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 -> 0 curated associations fetched
[info]  2026-09-28 11:16:41 EFO_0008584 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:16:41 EFO_0008584 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 -> 0 curated associations fetched
[info]  2026-09-28 11:16:42 EFO_0003777 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:16:42 EFO_0003777 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 -> 0 curated associations fetched
[info]  2026-09-28 11:16:44 EFO_0001645 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:16:44 EFO_0001645 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 -> 316 curated associations fetched
[info]  2026-09-28 11:17:23 EFO_0022264 / CETP -> 1 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / APOA1 -> 1 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / APOB -> 1 curated associations in region
[info]  2026-09-28 11:17:23 EFO_0022264 / APOE -> 3 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 -> 151 curated associations fetched
[info]  2026-09-28 11:17:42 EFO_0022266 / CETP -> 1 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / HMGCR -> 1 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / NPC1L1 -> 1 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:17:42 EFO_0022266 / APOE -> 3 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 -> 40 curated associations fetched
[info]  2026-09-28 11:17:47 EFO_0006799 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:17:47 EFO_0006799 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 -> 14 curated associations fetched
[info]  2026-09-28 11:17:50 EFO_0011057 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:17:50 EFO_0011057 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 -> 0 curated associations fetched
[info]  2026-09-28 11:17:51 MONDO_0043224 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:17:51 MONDO_0043224 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 -> 0 curated associations fetched
[info]  2026-09-28 11:17:53 MONDO_0000914 / CETP -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / HMGCR -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / NPC1L1 -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / PCSK9 -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / ANGPTL3 -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / PPARA -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / APOA1 -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / APOB -> 0 curated associations in region
[info]  2026-09-28 11:17:53 MONDO_0000914 / APOE -> 0 curated associations in region
[info]  2026-09-28 11:17:53 CETP -> 0 gene-burden evidence rows
[info]  2026-09-28 11:17:53 HMGCR -> 0 gene-burden evidence rows
[info]  2026-09-28 11:17:53 NPC1L1 -> 0 gene-burden evidence rows
[info]  2026-09-28 11:17:54 PCSK9 -> 4 gene-burden evidence rows
[info]  2026-09-28 11:17:54 ANGPTL3 -> 5 gene-burden evidence rows
[info]  2026-09-28 11:17:54 PPARA -> 0 gene-burden evidence rows
[info]  2026-09-28 11:17:54 APOA1 -> 0 gene-burden evidence rows
[info]  2026-09-28 11:17:55 APOB -> 7 gene-burden evidence rows
[info]  2026-09-28 11:17:55 APOE -> 0 gene-burden evidence rows
[info]  2026-09-28 11:17:55 wrote 4037 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv

```
