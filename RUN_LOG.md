## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-10-02 08:25:29
- last run: 2026-10-02 08:25:29
- commit: `9f8d050`

Output:
```text
[info]  2026-10-02 08:20:47 9 genes, 84 icd codes
[stage] 2026-10-02 08:20:47 resolve_genes
[stage] 2026-10-02 08:20:47 resolve_efo
[warn]  2026-10-02 08:20:48 No EFO term found for: Certain current complications following acute myocardial infarction
[warn]  2026-10-02 08:20:49 obsolete trait id EFO_0003763 -> MONDO_0011057
[warn]  2026-10-02 08:20:49 obsolete trait id EFO_0000713 -> MONDO_0005099
[warn]  2026-10-02 08:20:49 obsolete trait id EFO_0005669 -> MONDO_0013792
[warn]  2026-10-02 08:20:50 obsolete trait id EFO_0004277 -> MONDO_0005394
[warn]  2026-10-02 08:20:50 obsolete trait id EFO_0000712 -> MONDO_0005098
[warn]  2026-10-02 08:20:50 obsolete trait id EFO_0008583 -> MONDO_0004781
[warn]  2026-10-02 08:20:50 obsolete trait id EFO_0003777 -> MONDO_0005267
[warn]  2026-10-02 08:20:50 obsolete trait id EFO_0001645 -> MONDO_0005010
[warn]  2026-10-02 08:20:50 obsolete trait id EFO_0003144 -> MONDO_0005252
[info]  2026-10-02 08:20:50 trait ids checked: 30, obsolete replaced: 9
[info]  2026-10-02 08:20:57 wrote resolved efo_ids to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/icd_codes.txt
[info]  2026-10-02 08:20:57 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-02 08:20:57 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-02 08:20:57 finngen_manual
[info]  2026-10-02 08:20:57 all_cause_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 alzheimers_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 coronary_heart_disease: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 frontotemporal_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 hf: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 parkinsons_disease_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 stroke: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-02 08:20:57 vascular_dementia: own results for finngen; catalog studies with these cohorts excluded
[stage] 2026-10-02 08:20:57 discover_gwas
[info]  2026-10-02 08:21:05 EFO_0003913 (exact): 56 studies -> 44 with full sumstats -> 10 included
[info]  2026-10-02 08:21:12 EFO_0003913 (exact): 56 studies -> 42 with full sumstats -> 10 included, 2 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:21:21 EFO_0004269 (exact): 76 studies -> 46 with full sumstats -> 10 included
[info]  2026-10-02 08:21:23 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included
[info]  2026-10-02 08:21:25 EFO_0008584 (exact): 2 studies -> 2 with full sumstats -> 2 included
[info]  2026-10-02 08:21:26 EFO_0008584 (exact): 2 studies -> 2 with full sumstats -> 2 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:21:30 EFO_0009492 (exact): 21 studies -> 18 with full sumstats -> 10 included
[info]  2026-10-02 08:21:33 EFO_0009493 (exact): 10 studies -> 9 with full sumstats -> 9 included
[info]  2026-10-02 08:21:35 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 with full sumstats -> 0 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:21:39 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 3 with full sumstats -> 3 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:21:42 MONDO_0004781 (exact): 11 studies -> 6 with full sumstats -> 6 included
[info]  2026-10-02 08:21:44 MONDO_0004781 (exact): 11 studies -> 6 with full sumstats -> 6 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:22:19 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 31 with full sumstats -> 17 included, 12 dropped for cohort overlap (finngen), 5 included with blank cohort
[info]  2026-10-02 08:22:44 MONDO_0005010 (exact): 207 studies -> 69 with full sumstats -> 10 included
[info]  2026-10-02 08:23:11 MONDO_0005010 (exact): 207 studies -> 69 with full sumstats -> 10 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:23:28 MONDO_0005098 (exact): 134 studies -> 65 with full sumstats -> 10 included
[info]  2026-10-02 08:23:45 MONDO_0005098 (exact): 134 studies -> 61 with full sumstats -> 10 included, 4 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:23:48 MONDO_0005099 (exact): 19 studies -> 12 with full sumstats -> 10 included
[info]  2026-10-02 08:23:51 MONDO_0005099 (exact): 19 studies -> 11 with full sumstats -> 10 included, 1 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:24:01 MONDO_0005252 (exact): 77 studies -> 57 with full sumstats -> 10 included
[info]  2026-10-02 08:24:12 MONDO_0005252 (exact): 77 studies -> 46 with full sumstats -> 10 included, 12 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:24:19 MONDO_0005267 (exact): 58 studies -> 48 with full sumstats -> 10 included
[info]  2026-10-02 08:24:27 MONDO_0005267 (exact): 58 studies -> 48 with full sumstats -> 10 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:24:30 MONDO_0005394 (exact): 10 studies -> 6 with full sumstats -> 6 included
[info]  2026-10-02 08:24:33 MONDO_0005394 (exact): 10 studies -> 6 with full sumstats -> 6 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:24:34 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 with full sumstats -> 0 included, 0 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:24:39 MONDO_0013792 (exact): 30 studies -> 17 with full sumstats -> 10 included
[info]  2026-10-02 08:24:44 MONDO_0013792 (exact): 30 studies -> 16 with full sumstats -> 10 included, 2 dropped for cohort overlap (finngen), 0 included with blank cohort
[info]  2026-10-02 08:24:46 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-10-02 08:24:46 write_tasks
[info]  2026-10-02 08:25:16 wrote 154 tasks (387 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-10-02 08:25:24 wrote 2633 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [20] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs/3_1790934491/run_job_array.job --task-id 1 --step 10`)
- first run: 2026-10-02 10:52:11
- last run: 2026-10-02 10:52:11
- commit: `9f8d050`

Output:
```text
[info]  2026-10-02 10:52:04 rows 1-10 of 11, 9 gene regions
[info]  2026-10-02 10:52:04 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90692001-GCST90693000/GCST90692207/harmonised/GCST90692207.h.tsv.gz @ 9 regions -> 1401 rows with MAF < 0.01
[info]  2026-10-02 10:52:04 GCST90692207: 1401 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90692207_result.tsv.gz
[info]  2026-10-02 10:52:05 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90692001-GCST90693000/GCST90692142/harmonised/GCST90692142.h.tsv.gz @ 9 regions -> 1405 rows with MAF < 0.01
[info]  2026-10-02 10:52:05 GCST90692142: 1405 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90692142_result.tsv.gz
[info]  2026-10-02 10:52:06 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90691001-GCST90692000/GCST90691702/harmonised/GCST90691702.h.tsv.gz @ 9 regions -> 1401 rows with MAF < 0.01
[info]  2026-10-02 10:52:06 GCST90691702: 1401 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90691702_result.tsv.gz
[info]  2026-10-02 10:52:07 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90691001-GCST90692000/GCST90691608/harmonised/GCST90691608.h.tsv.gz @ 9 regions -> 1405 rows with MAF < 0.01
[info]  2026-10-02 10:52:07 GCST90691608: 1405 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90691608_result.tsv.gz
[info]  2026-10-02 10:52:08 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473534/harmonised/GCST90473534.h.tsv.gz @ 9 regions -> 1054 rows with MAF < 0.01
[info]  2026-10-02 10:52:08 GCST90473534: 1054 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473534_result.tsv.gz
[info]  2026-10-02 10:52:08 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473533/harmonised/GCST90473533.h.tsv.gz @ 9 regions -> 10569 rows with MAF < 0.01
[info]  2026-10-02 10:52:08 GCST90473533: 10569 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473533_result.tsv.gz
[info]  2026-10-02 10:52:09 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90473001-GCST90474000/GCST90473528/harmonised/GCST90473528.h.tsv.gz @ 9 regions -> 317 rows with MAF < 0.01
[info]  2026-10-02 10:52:09 GCST90473528: 317 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90473528_result.tsv.gz
[info]  2026-10-02 10:52:09 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90726001-GCST90727000/GCST90726685/harmonised/GCST90726685.h.tsv.gz @ 9 regions -> 978 rows with MAF < 0.01
[info]  2026-10-02 10:52:09 GCST90726685: 978 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90726685_result.tsv.gz
[info]  2026-10-02 10:52:10 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90692001-GCST90693000/GCST90692406/harmonised/GCST90692406.h.tsv.gz @ 9 regions -> 1702 rows with MAF < 0.01
[info]  2026-10-02 10:52:10 GCST90692406: 1702 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90692406_result.tsv.gz
[info]  2026-10-02 10:52:11 http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90432001-GCST90433000/GCST90432123/harmonised/GCST90432123.h.tsv.gz @ 9 regions -> 1281 rows with MAF < 0.01
[info]  2026-10-02 10:52:11 GCST90432123: 1281 rows over 9 genes -> /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/GCST90432123_result.tsv.gz

```

## [20] filter_gwas_cat_job
- first run: 2026-10-02 10:52:11
- last run: 2026-10-02 10:52:11
- commit: `9f8d050`

Output:
```text
[info]  2026-10-02 10:52:02 task 1: rows 1-10

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-10-02 11:17:42
- last run: 2026-10-02 11:17:42
- commit: `9f8d050`

Output:
```text
[stage] 2026-10-02 10:59:52 load_sumstats
[info]  2026-10-02 10:59:54 summary-stats: 154 files, 734168 rows incl. one copy per outcome (0 missing)
[info]  2026-10-02 11:00:00 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-02 11:00:00 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-02 11:00:00 marvel
[info]  2026-10-02 11:00:00 no own results listed in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_results.tsv
[stage] 2026-10-02 11:00:00 fetch_curated
[info]  2026-10-02 11:01:02 MONDO_0005252 (exact): 892 fetched; in region: CETP=1
[info]  2026-10-02 11:01:04 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-02 11:01:08 MONDO_0013792 (exact): 42 fetched; in region: APOE=1
[info]  2026-10-02 11:01:13 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-02 11:01:36 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-02 11:01:58 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=3 APOE=4
[info]  2026-10-02 11:02:01 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-02 11:02:07 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-02 11:07:02 MONDO_0005010 (exact): 3913 fetched; in region: CETP=3 HMGCR=1 PCSK9=9 APOB=2 APOE=14
[info]  2026-10-02 11:07:10 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-02 11:07:13 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-02 11:07:15 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-02 11:16:11 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1 APOE=179
[info]  2026-10-02 11:16:21 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-02 11:16:27 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-02 11:16:30 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-02 11:16:33 EFO ids with 0 curated associations: 4
[stage] 2026-10-02 11:16:33 gene_burden
[info]  2026-10-02 11:16:33 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-02 11:16:35 curated MAF: numeric=4 not_reported=471
[info]  2026-10-02 11:16:35 curated: 7 rows dropped from studies excluded for cohort overlap
[info]  2026-10-02 11:16:35 gene-burden rows: none (9 genes with 0)
[info]  2026-10-02 11:16:36 ancestry: 2 rows of studies not in the discovery log labelled NR
[info]  2026-10-02 11:16:36 ancestry: curated AFR=14
[info]  2026-10-02 11:16:36 ancestry: curated EAS=18
[info]  2026-10-02 11:16:36 ancestry: curated EUR=132
[info]  2026-10-02 11:16:36 ancestry: curated MULTI=307
[info]  2026-10-02 11:16:36 ancestry: curated NR=4
[info]  2026-10-02 11:16:36 ancestry: summary-stats AFR=65589
[info]  2026-10-02 11:16:36 ancestry: summary-stats AMR=22203
[info]  2026-10-02 11:16:36 ancestry: summary-stats CSA=96330
[info]  2026-10-02 11:16:36 ancestry: summary-stats EAS=616
[info]  2026-10-02 11:16:36 ancestry: summary-stats EUR=502246
[info]  2026-10-02 11:16:36 ancestry: summary-stats MULTI=41632
[info]  2026-10-02 11:16:36 ancestry: summary-stats NR=3650
[info]  2026-10-02 11:16:36 ancestry: summary-stats OTH=1902
[stage] 2026-10-02 11:16:36 ensembl_check
[info]  2026-10-02 11:16:36 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:36 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:36 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:37 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:37 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:37 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:37 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:37 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:37 APOE: 11244 Ensembl variants in 19:44893787-44919396 (0 windows fetched, rest cached)
[info]  2026-10-02 11:16:38 Ensembl check: 24461 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-02 11:16:39 summary-stats rows: alleles match=637609 flipped=52617 mismatch=41698 not_found=2208 strand_flip=36; rsid same=704863 no_source_rsid=19867 different=7230
[info]  2026-10-02 11:16:39 curated rows: alleles match=250 effect_unknown=199 mismatch=12 flipped=10 strand_flip=4; rsid same=467 different=8
[warn]  2026-10-02 11:16:39 summary-stats GCST90083958: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90083959: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90083960: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90083999: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90084014: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90084015: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90084016: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[warn]  2026-10-02 11:16:39 summary-stats GCST90084021: 100% of 417 rows not_found/mismatch in Ensembl (GRCh37 file?)
[info]  2026-10-02 11:16:40 duplicate variants flagged: 794 rows
[stage] 2026-10-02 11:16:40 write
[info]  2026-10-02 11:17:34 wrote 734643 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-10-02 11:18:03
- last run: 2026-10-02 11:18:03
- commit: `9f8d050`

Output:
```text
[info]  2026-10-02 10:59:44 using root directory: /home/rmgpmva/projects/lipid_adem

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
- first run: 2026-10-01 11:50:12
- last run: 2026-10-01 11:50:12
- commit: `d6729b1`

Output:
```text
[stage] 2026-10-01 11:49:37 load_variant_lists
[info]  2026-10-01 11:49:37 6 variant lists, 30561 rows: ANGPTL3_variants.tsv, CETP_variants.tsv, HMGCR_variants.tsv, NPC1L1_variants.tsv, PCSK9_variants.tsv, PPARA_variants.tsv
[info]  2026-10-01 11:49:37 28539 rows with source in ['AM'] skipped
[info]  2026-10-01 11:49:37 1125 duplicate rows removed
[info]  2026-10-01 11:49:37 ANGPTL3 ClinVar: 22 rows, 12 without alleles, 10 outside gene region
[info]  2026-10-01 11:49:37 ANGPTL3 PTV: 57 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 CETP ClinVar: 317 rows, 9 without alleles, 6 outside gene region
[info]  2026-10-01 11:49:37 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 CETP PTV: 61 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 CETP landfors_paper: 94 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 HMGCR ClinVar: 9 rows, 1 without alleles, 1 outside gene region
[info]  2026-10-01 11:49:37 HMGCR PTV: 40 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 NPC1L1 ClinVar: 9 rows, 9 without alleles, 9 outside gene region
[info]  2026-10-01 11:49:37 NPC1L1 PTV: 102 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 PCSK9 ClinVar: 23 rows, 6 without alleles, 5 outside gene region
[info]  2026-10-01 11:49:37 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 PCSK9 PTV: 85 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-01 11:49:37 PPARA ClinVar: 33 rows, 33 without alleles, 33 outside gene region
[info]  2026-10-01 11:49:37 PPARA PTV: 26 rows, 0 without alleles, 0 outside gene region
[stage] 2026-10-01 11:49:37 load_gwas
[info]  2026-10-01 11:50:07 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv.gz: 598209 rows, 597486 variant-level (summary-stats, curated)
[info]  2026-10-01 11:50:09 summary-stats: 973 rows without chrom/pos or effect allele, cannot be matched
[info]  2026-10-01 11:50:09 curated: 420 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-01 11:50:10 match
[info]  2026-10-01 11:50:10 ANGPTL3 ClinVar: 10 variants, 0 matched, GWAS rows: none
[info]  2026-10-01 11:50:10 ANGPTL3 PTV: 57 variants, 9 matched, GWAS rows: summary-stats=255
[info]  2026-10-01 11:50:10 CETP ClinVar: 308 variants, 140 matched, GWAS rows: summary-stats=5300 curated=33
[info]  2026-10-01 11:50:10 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=12 curated=5
[info]  2026-10-01 11:50:10 CETP PTV: 61 variants, 17 matched, GWAS rows: summary-stats=343
[info]  2026-10-01 11:50:10 CETP landfors_paper: 94 variants, 23 matched, GWAS rows: summary-stats=531
[info]  2026-10-01 11:50:11 HMGCR ClinVar: 8 variants, 0 matched, GWAS rows: none
[info]  2026-10-01 11:50:11 HMGCR PTV: 40 variants, 1 matched, GWAS rows: summary-stats=6
[info]  2026-10-01 11:50:11 NPC1L1 PTV: 102 variants, 22 matched, GWAS rows: summary-stats=337
[info]  2026-10-01 11:50:11 PCSK9 ClinVar: 17 variants, 3 matched, GWAS rows: summary-stats=38
[info]  2026-10-01 11:50:11 PCSK9 GoF: 18 variants, 8 matched, GWAS rows: summary-stats=287
[info]  2026-10-01 11:50:11 PCSK9 PTV: 85 variants, 18 matched, GWAS rows: summary-stats=358 curated=10
[info]  2026-10-01 11:50:11 PPARA PTV: 26 variants, 2 matched, GWAS rows: summary-stats=25
[warn]  2026-10-01 11:50:11 a1 vs Ensembl ref: 7540 matched rows checked, 593 where a1 is not the Ensembl ref (e.g. 1:55057476:CACA:CA, 1:62597997:AACTAACTAACT:AACTAACT, 16:56961991:CACA:CA/CACACA)
[stage] 2026-10-01 11:50:11 write
[info]  2026-10-01 11:50:12 wrote 7540 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz

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

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --group-by variant`)
- first run: 2026-10-01 12:01:23
- last run: 2026-10-01 12:01:23
- commit: `d6729b1`

Output:
```text
[info]  2026-10-01 12:01:05 grouping variant: variant_site, outcome
[stage] 2026-10-01 12:01:05 load_matched
[info]  2026-10-01 12:01:05 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz: 7540 rows, 217 variants
[stage] 2026-10-01 12:01:05 prepare_effects
[info]  2026-10-01 12:01:05 3 rows dropped: no beta or odds ratio
[info]  2026-10-01 12:01:05 6 rows dropped: no SE and p missing, 0 or 1
[info]  2026-10-01 12:01:05 7531 usable rows, 671 with SE derived from p
[stage] 2026-10-01 12:01:05 orient
[info]  2026-10-01 12:01:05 114 variants oriented as ldl_lowering
[info]  2026-10-01 12:01:05 98 variants oriented as a2
[info]  2026-10-01 12:01:05 4 variants oriented as a2_gof_flipped
[stage] 2026-10-01 12:01:05 dedupe
[info]  2026-10-01 12:01:05 618 duplicate rows removed
[stage] 2026-10-01 12:01:05 meta_analyse
[info]  2026-10-01 12:01:09 1237 groups, 1034 pooling more than one estimate
[stage] 2026-10-01 12:01:09 write
[info]  2026-10-01 12:01:09 wrote 1237 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_variant.tsv.gz

```
