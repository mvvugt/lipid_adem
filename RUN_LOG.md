## [10] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene HMGCR --study-accession F5_DEMENTIA --chrom 5 --start 75332606 --end 75370339 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/HMGCR_F5_DEMENTIA_result.tsv.gz --source finngen`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-22 17:40:30
- commit: `7afbc49` (dirty)

Output:
```text
[info]  2026-09-22 17:40:24 https://storage.googleapis.com/finngen-public-data-r13/summary_stats/finngen_R13_F5_DEMENTIA.gz @ 5:75332606-75370339 -> 135 rows with MAF < 0.01
[info]  2026-09-22 17:40:27 HMGCR x F5_DEMENTIA: 135 rows -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/HMGCR_F5_DEMENTIA_result.tsv.gz

```

## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-22 17:53:52
- commit: `7afbc49` (dirty)

Δ vs previous run (was `b6ed2fe`):
```diff
@@ -1,62 +1,62 @@
-[info]  2026-09-22 12:57:58 6 genes, 50 icd codes
-[warn]  2026-09-22 12:57:58 No EFO term found for: F02.0A
-[warn]  2026-09-22 12:57:58 No EFO term found for: Unspecified dementia
-[warn]  2026-09-22 12:57:59 No EFO term found for: Delirium superimposed on dementia
-[warn]  2026-09-22 12:57:59 No EFO term found for: Circumscribed brain atrophy
-[warn]  2026-09-22 12:57:59 No EFO term found for: G31.09
-[warn]  2026-09-22 12:57:59 No EFO term found for: Certain current complications following acute myocardial infarction
-[warn]  2026-09-22 12:57:59 No EFO term found for: Vascular dementia of acute onset
-[warn]  2026-09-22 12:57:59 No EFO term found for: Mixed cortical and subcortical vascular dementia
-[warn]  2026-09-22 12:57:59 No EFO term found for: Vascular dementia, unspecified
-[info]  2026-09-22 12:57:59 wrote resolved efo_ids to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/icd_codes.txt
-[info]  2026-09-22 12:58:01 EFO_0000249 -> 0 studies
-[info]  2026-09-22 12:58:01 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:02 EFO_0000712 -> 0 studies
-[info]  2026-09-22 12:58:02 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:03 EFO_0000713 -> 0 studies
-[info]  2026-09-22 12:58:03 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:05 EFO_0001645 -> 0 studies
-[info]  2026-09-22 12:58:05 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:07 EFO_0003144 -> 0 studies
-[info]  2026-09-22 12:58:07 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:08 EFO_0003763 -> 0 studies
-[info]  2026-09-22 12:58:08 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:10 EFO_0003777 -> 0 studies
-[info]  2026-09-22 12:58:10 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:11 EFO_0003875 -> 0 studies
-[info]  2026-09-22 12:58:11 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:21 EFO_0003913 -> 50 studies
-[info]  2026-09-22 12:58:23 50 studies -> 45 with full sumstats -> 10 after cap=10
-[info]  2026-09-22 12:58:25 EFO_0003914 -> 0 studies
-[info]  2026-09-22 12:58:25 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:26 EFO_0004277 -> 0 studies
-[info]  2026-09-22 12:58:26 0 studies -> 0 with full sumstats -> 0 after cap=10
-[info]  2026-09-22 12:58:51 EFO_0004614 -> 124 studies
-[info]  2026-09-22 12:58:52 124 studies -> 99 with full sumstats -> 10 after cap=10
-[info]  2026-09-22 12:59:20 EFO_0004615 -> 127 studies
-[info]  2026-09-22 12:59:21 127 studies -> 102 with full sumstats -> 10 after cap=10
-[info]  2026-09-22 12:59:22 EFO_0005669 -> 0 studies
-[info]  2026-09-22 12:59:22 0 studies -> 0 with full sumstats -> 0 after cap=10
... 85 more line(s) omitted
```

Output:
```text
[info]  2026-09-22 17:52:04 6 genes, 50 icd codes
[warn]  2026-09-22 17:52:04 No EFO term found for: F02.0A
[warn]  2026-09-22 17:52:04 No EFO term found for: Unspecified dementia
[warn]  2026-09-22 17:52:04 No EFO term found for: Delirium superimposed on dementia
[warn]  2026-09-22 17:52:04 No EFO term found for: Circumscribed brain atrophy
[warn]  2026-09-22 17:52:05 No EFO term found for: G31.09
[warn]  2026-09-22 17:52:05 No EFO term found for: Certain current complications following acute myocardial infarction
[warn]  2026-09-22 17:52:05 No EFO term found for: Vascular dementia of acute onset
[warn]  2026-09-22 17:52:05 No EFO term found for: Mixed cortical and subcortical vascular dementia
[warn]  2026-09-22 17:52:05 No EFO term found for: Vascular dementia, unspecified
[info]  2026-09-22 17:52:08 wrote resolved efo_ids to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/icd_codes.txt
[info]  2026-09-22 17:52:09 EFO_0000249 -> 0 studies
[info]  2026-09-22 17:52:09 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:11 EFO_0000712 -> 0 studies
[info]  2026-09-22 17:52:11 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:12 EFO_0000713 -> 0 studies
[info]  2026-09-22 17:52:12 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:14 EFO_0001645 -> 0 studies
[info]  2026-09-22 17:52:14 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:15 EFO_0003144 -> 0 studies
[info]  2026-09-22 17:52:15 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:17 EFO_0003763 -> 0 studies
[info]  2026-09-22 17:52:17 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:18 EFO_0003777 -> 0 studies
[info]  2026-09-22 17:52:18 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:20 EFO_0003875 -> 0 studies
[info]  2026-09-22 17:52:20 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:26 EFO_0003913 -> 50 studies
[info]  2026-09-22 17:52:28 50 studies -> 45 with full sumstats -> 10 after cap=10
[info]  2026-09-22 17:52:30 EFO_0003914 -> 0 studies
[info]  2026-09-22 17:52:30 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:31 EFO_0004277 -> 0 studies
[info]  2026-09-22 17:52:31 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:52:50 EFO_0004614 -> 124 studies
[info]  2026-09-22 17:52:50 124 studies -> 99 with full sumstats -> 10 after cap=10
[info]  2026-09-22 17:53:08 EFO_0004615 -> 127 studies
[info]  2026-09-22 17:53:09 127 studies -> 102 with full sumstats -> 10 after cap=10
[info]  2026-09-22 17:53:11 EFO_0005669 -> 0 studies
[info]  2026-09-22 17:53:11 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:12 EFO_0006799 -> 1 studies
[info]  2026-09-22 17:53:12 1 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:14 EFO_0008583 -> 0 studies
[info]  2026-09-22 17:53:14 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:15 EFO_0008584 -> 2 studies
[info]  2026-09-22 17:53:16 2 studies -> 2 with full sumstats -> 2 after cap=10
[info]  2026-09-22 17:53:17 EFO_0011057 -> 1 studies
[info]  2026-09-22 17:53:17 1 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:24 EFO_0022264 -> 52 studies
[info]  2026-09-22 17:53:25 52 studies -> 51 with full sumstats -> 10 after cap=10
[info]  2026-09-22 17:53:34 EFO_0022266 -> 52 studies
[info]  2026-09-22 17:53:34 52 studies -> 51 with full sumstats -> 10 after cap=10
[info]  2026-09-22 17:53:36 MONDO_0000914 -> 0 studies
[info]  2026-09-22 17:53:36 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:39 MONDO_0004648 -> 15 studies
[info]  2026-09-22 17:53:39 15 studies -> 3 with full sumstats -> 3 after cap=10
[info]  2026-09-22 17:53:40 MONDO_0008243 -> 1 studies
[info]  2026-09-22 17:53:40 1 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:42 MONDO_0043224 -> 0 studies
[info]  2026-09-22 17:53:42 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:43 NA -> 0 studies
[info]  2026-09-22 17:53:43 0 studies -> 0 with full sumstats -> 0 after cap=10
[info]  2026-09-22 17:53:49 wrote 450 tasks to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv

```

## [10] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-09-22 15:48:03
- commit: `7afbc49`

Output:
```text
[info]  2026-09-22 15:36:43 EFO_0000249 -> 0 curated associations in region
[info]  2026-09-22 15:37:00 MONDO_0004648 -> 0 curated associations in region
[info]  2026-09-22 15:42:23 EFO_0004614 -> 21 curated associations in region
[info]  2026-09-22 15:42:23 CETP -> 0 gene-burden evidence rows
[info]  2026-09-22 15:42:25 EFO_0000249 -> 0 curated associations in region
[info]  2026-09-22 15:42:41 MONDO_0004648 -> 0 curated associations in region
[info]  2026-09-22 15:48:02 EFO_0004614 -> 0 curated associations in region
[info]  2026-09-22 15:48:03 HMGCR -> 0 gene-burden evidence rows
[info]  2026-09-22 15:48:03 wrote 3110 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv

```
