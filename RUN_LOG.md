## [10] filter_gwas_cat (`/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene CETP --study-accession GCST90841019 --chrom 16 --start 56951980 --end 56993663 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/CETP_GCST90841019_result.tsv`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-21 22:58:26
- commit: `a557eec` (dirty)
- status: failed

Output:
```text
Traceback (most recent call last):
  File "/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 134, in main
    run_filter(
    ~~~~~~~~~~^
        gene=args.gene,
        ^^^^^^^^^^^^^^^
    ...<4 lines>...
        outfile=args.outfile,
        ^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 88, in run_filter
    filtered = functions.filter_sumstats_region(
        tabix_source=tabix_source,
    ...<2 lines>...
        maf_threshold=Constants.MAF_THRESHOLD,
    )
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 442, in filter_sumstats_region
    with pysam.TabixFile(tabix_source) as tabix_file:
         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "pysam/libctabix.pyx", line 348, in pysam.libctabix.TabixFile.__cinit__
  File "pysam/libctabix.pyx", line 389, in pysam.libctabix.TabixFile._open
OSError: could not open file `https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90841019/harmonised/GCST90841019.h.tsv.gz`

--- error output (raw) ---
Traceback (most recent call last):
  File "/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 134, in main
    run_filter(
    ~~~~~~~~~~^
        gene=args.gene,
        ^^^^^^^^^^^^^^^
    ...<4 lines>...
        outfile=args.outfile,
        ^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 88, in run_filter
    filtered = functions.filter_sumstats_region(
        tabix_source=tabix_source,
    ...<2 lines>...
        maf_threshold=Constants.MAF_THRESHOLD,
    )
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 442, in filter_sumstats_region
    with pysam.TabixFile(tabix_source) as tabix_file:
         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "pysam/libctabix.pyx", line 348, in pysam.libctabix.TabixFile.__cinit__
  File "pysam/libctabix.pyx", line 389, in pysam.libctabix.TabixFile._open
OSError: could not open file `https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90841019/harmonised/GCST90841019.h.tsv.gz`

```

## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-21 22:51:36
- commit: `a557eec` (dirty)

Output:
```text
[info]  2026-09-21 22:50:14 6 genes, 28 icd codes
[info]  2026-09-21 22:50:14 mapped Dementia in Alzheimer disease -> EFO:1001870
[info]  2026-09-21 22:50:14 mapped Vascular dementia -> MONDO:0004648
[info]  2026-09-21 22:50:14 mapped Dementia in Pick disease -> MONDO:0008243
[warn]  2026-09-21 22:50:14 No EFO term found for: F02.0A
[warn]  2026-09-21 22:50:14 No EFO term found for: Unspecified dementia
[warn]  2026-09-21 22:50:14 No EFO term found for: Delirium superimposed on dementia
[info]  2026-09-21 22:50:15 mapped Alzheimer disease -> MONDO:0004975
[warn]  2026-09-21 22:50:15 No EFO term found for: Circumscribed brain atrophy
[warn]  2026-09-21 22:50:15 No EFO term found for: G31.09
[info]  2026-09-21 22:50:15 mapped Progressive vascular leukoencephalopathy -> MONDO:0008641
[info]  2026-09-21 22:50:15 mapped Dementia in Alzheimer disease with early onset -> MONDO:0015140
[warn]  2026-09-21 22:50:15 No EFO term found for: F00.0A
[info]  2026-09-21 22:50:15 mapped Dementia in Alzheimer disease with late onset -> EFO:1001870
[warn]  2026-09-21 22:50:16 No EFO term found for: F00.1A
[warn]  2026-09-21 22:50:16 No EFO term found for: Dementia in Alzheimer disease, atypical or mixed type
[warn]  2026-09-21 22:50:16 No EFO term found for: F00.2A
[warn]  2026-09-21 22:50:16 No EFO term found for: Dementia in Alzheimer disease, unspecified
[warn]  2026-09-21 22:50:16 No EFO term found for: F00.9A
[info]  2026-09-21 22:50:17 mapped Alzheimer disease with early onset -> EFO:0022957
[info]  2026-09-21 22:50:17 mapped Alzheimer disease with late onset -> EFO:1001870
[info]  2026-09-21 22:50:17 mapped Other Alzheimer disease -> EFO:0009268
[warn]  2026-09-21 22:50:17 No EFO term found for: Alzheimer disease, unspecified
[info]  2026-09-21 22:50:17 mapped Angina pectoris -> EFO:0003913
[info]  2026-09-21 22:50:17 mapped Acute myocardial infarction -> MONDO:0004781
[info]  2026-09-21 22:50:17 mapped Subsequent myocardial infarction -> EFO:0008584
[warn]  2026-09-21 22:50:18 No EFO term found for: Certain current complications following acute myocardial infarction
[warn]  2026-09-21 22:50:18 No EFO term found for: Other acute ischaemic heart diseases
[warn]  2026-09-21 22:50:18 No EFO term found for: Chronic ischaemic heart disease
[info]  2026-09-21 22:50:18 wrote resolved efo_ids to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/icd_codes.txt
[info]  2026-09-21 22:50:27 EFO_0003913 -> 50 studies
[info]  2026-09-21 22:50:29 EFO_0008584 -> 2 studies
[info]  2026-09-21 22:50:38 EFO_0009268 -> 55 studies
[info]  2026-09-21 22:50:39 EFO_0022957 -> 1 studies
[info]  2026-09-21 22:50:44 EFO_1001870 -> 16 studies
[info]  2026-09-21 22:50:48 MONDO_0004648 -> 15 studies
[info]  2026-09-21 22:50:50 MONDO_0004781 -> 8 studies
[info]  2026-09-21 22:51:30 MONDO_0004975 -> 240 studies
[info]  2026-09-21 22:51:32 MONDO_0008243 -> 1 studies
[info]  2026-09-21 22:51:33 MONDO_0008641 -> 0 studies
[info]  2026-09-21 22:51:35 MONDO_0015140 -> 0 studies
[info]  2026-09-21 22:51:36 NA -> 0 studies
[info]  2026-09-21 22:51:36 wrote 2406 tasks to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv

```
