## [5] apoe_exposure (`/home/rmgpmva/projects/lipid_adem/src/apoe_exposure.py`)
- first run: 2026-10-09 09:54:04
- last run: 2026-10-12 12:37:43
- commit: `b31ef30`

Output:
```text
[stage] 2026-10-12 12:37:37 read
[info]  2026-10-12 12:37:37 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/lipids_full_pheno.tsv.gz: 469587 participants; genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[stage] 2026-10-12 12:37:37 indicators
[warn]  2026-10-12 12:37:37 27 participants without a genotype left out
[info]  2026-10-12 12:37:38 APOE_e2e2: 3025 carriers vs 466535 others
[info]  2026-10-12 12:37:38 APOE_e2e3: 57188 carriers vs 412372 others
[info]  2026-10-12 12:37:38 APOE_e2e4: 11672 carriers vs 457888 others
[info]  2026-10-12 12:37:38 APOE_e3e3: 276035 carriers vs 193525 others
[info]  2026-10-12 12:37:38 APOE_e3e4: 110438 carriers vs 359122 others
[info]  2026-10-12 12:37:38 APOE_e4e4: 11202 carriers vs 458358 others
[stage] 2026-10-12 12:37:38 write
[info]  2026-10-12 12:37:42 wrote 469560 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/apoe_diplotype.tsv.gz

```

## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-10-24 10:35:19
- commit: `04d2c6c`

Output:
```text
[info]  2026-10-24 10:20:05 8 genes, 85 icd codes
[stage] 2026-10-24 10:20:05 resolve_genes
[stage] 2026-10-24 10:20:05 resolve_efo
[info]  2026-10-24 10:20:05 trait ids checked: 21, obsolete replaced: 0
[info]  2026-10-24 10:20:05 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-24 10:20:05 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-24 10:20:05 finngen_manual
[info]  2026-10-24 10:20:06 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/study_outcome_review.tsv: 673 outcome x study exclusions for 10 outcomes
[info]  2026-10-24 10:20:06 catalog studies with aou, ukb excluded for every outcome
[info]  2026-10-24 10:20:06 all_cause_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 alzheimers_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 ascvd: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 coronary_heart_disease: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 frontotemporal_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 hf: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 parkinsons_disease_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 stroke: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 sudden_cardiac_death: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-24 10:20:06 vascular_dementia: own results for finngen, ukb; catalog studies with these cohorts excluded
[stage] 2026-10-24 10:20:06 discover_gwas
[info]  2026-10-24 10:22:09 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, finngen, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-24 10:22:10 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-24 10:22:10 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-24 10:24:47 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, finngen, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-24 10:24:47 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-24 10:24:48 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-24 10:24:57 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:25:46 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, finngen, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-24 10:25:46 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-24 10:25:46 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-24 10:26:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:22 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 4 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:26:39 MONDO_0004648 (with child traits, cap per term and 30 total): 16 studies -> 5 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:39 MONDO_0004648 (with child traits, cap per term and 30 total): 16 studies -> 5 dropped for cohort overlap (aou, finngen, ukb) -> 3 dropped by review -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:52 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:52 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:26:53 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-24 10:31:18 MONDO_0004975 (with child traits, cap per term and 30 total): 269 studies -> 44 dropped for cohort overlap (aou, finngen, ukb) -> 72 dropped by review -> 7 with full sumstats -> 7 included, 2 included with blank cohort
[info]  2026-10-24 10:31:20 MONDO_0004975 (with child traits, cap per term and 30 total): 269 studies -> 44 dropped for cohort overlap (aou, finngen, ukb) -> 60 dropped by review -> 9 with full sumstats -> 9 included, 3 included with blank cohort
[info]  2026-10-24 10:33:34 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 74 dropped by review -> 16 with full sumstats -> 16 included, 5 included with blank cohort
[info]  2026-10-24 10:33:35 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-24 10:33:36 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-24 10:34:19 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, finngen, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-24 10:34:20 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-24 10:34:21 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-24 10:34:24 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, finngen, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:24 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:25 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:38 MONDO_0005252 (exact): 77 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 12 dropped by review -> 18 with full sumstats -> 16 included, 0 included with blank cohort
[info]  2026-10-24 10:34:38 MONDO_0005252 (exact): 77 studies -> 34 dropped for cohort overlap (aou, ukb) -> 13 dropped by review -> 20 with full sumstats -> 17 included, 0 included with blank cohort
[info]  2026-10-24 10:34:48 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:48 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:48 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-24 10:34:52 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-24 10:34:52 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-24 10:34:53 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-24 10:34:54 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:34:55 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-24 10:34:59 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-24 10:35:00 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-24 10:35:00 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-24 10:35:01 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-10-24 10:35:02 write_tasks
[info]  2026-10-24 10:35:02 wrote 125 tasks (312 study x outcome rows, 8 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[stage] 2026-10-24 10:35:02 scale_meta
[warn]  2026-10-24 10:35:18 GCST90480807: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90480807)
[warn]  2026-10-24 10:35:18 GCST90477959: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477959)
[warn]  2026-10-24 10:35:18 GCST90477958: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477958)
[warn]  2026-10-24 10:35:18 GCST90246093: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246093)
[warn]  2026-10-24 10:35:18 GCST90399711: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90399711)
[warn]  2026-10-24 10:35:18 GCST90726898: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726898)
[warn]  2026-10-24 10:35:18 GCST90246094: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246094)
[warn]  2026-10-24 10:35:18 GCST90246086: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246086)
[warn]  2026-10-24 10:35:18 GCST90246085: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246085)
[warn]  2026-10-24 10:35:18 GCST90726916: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726916)
[warn]  2026-10-24 10:35:18 GCST90432123: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432123)
[warn]  2026-10-24 10:35:18 GCST90246098: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246098)
[warn]  2026-10-24 10:35:18 GCST90726915: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726915)
[warn]  2026-10-24 10:35:19 GCST90432122: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432122)
[warn]  2026-10-24 10:35:19 GCST90480188: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90480188)
[warn]  2026-10-24 10:35:19 GCST90477978: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477978)
[warn]  2026-10-24 10:35:19 GCST90477977: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477977)
[warn]  2026-10-24 10:35:19 GCST90246096: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246096)
[warn]  2026-10-24 10:35:19 GCST90018650: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018650)
[warn]  2026-10-24 10:35:19 GCST90726750: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726750)
[warn]  2026-10-24 10:35:19 GCST90704648: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90704648)
[warn]  2026-10-24 10:35:19 GCST90727420: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90727420)
[warn]  2026-10-24 10:35:19 GCST90565439: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90565439)
[warn]  2026-10-24 10:35:19 GCST90566388: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90566388)
[warn]  2026-10-24 10:35:19 GCST90276158: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276158)
[warn]  2026-10-24 10:35:19 GCST90276157: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276157)
[warn]  2026-10-24 10:35:19 GCST007511: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST007511)
[warn]  2026-10-24 10:35:19 GCST003452: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST003452)
[warn]  2026-10-24 10:35:19 GCST002245: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST002245)
[warn]  2026-10-24 10:35:19 GCST90861026: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861026)
[warn]  2026-10-24 10:35:19 GCST90861027: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861027)
[warn]  2026-10-24 10:35:19 GCST90861029: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861029)
[warn]  2026-10-24 10:35:19 GCST90861030: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861030)
[warn]  2026-10-24 10:35:19 GCST90476370: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90476370)
[warn]  2026-10-24 10:35:19 GCST90018586: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018586)
[info]  2026-10-24 10:35:19 metadata yaml read for 115 included studies, scale: unknown=115
[info]  2026-10-24 10:35:19 wrote 2655 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

```

## [10] slurm_script
- first run: 2026-10-21 11:53:26
- last run: 2026-10-21 11:53:26
- commit: `e9443d3` (dirty)

Output:
```text
[info]  2026-10-21 11:38:22 using root directory: /home/mvanvugt/projects/lipid_adem
[info]  2026-10-21 11:38:22 VCF directory: /projects/0/aus20644/data/ukbiobank/genetics/b38/lof, pattern: chr{chrom}_merged_vep.vcf.gz
[info]  2026-10-21 11:38:22 gene list: /home/mvanvugt/projects/lipid_adem/data/raw/gene_list.txt
[info]  2026-10-21 11:38:22 working directory (temporary): /scratch-local/mvanvugt.28412845/tmp.rj01qmYBde/task_1
[info]  2026-10-21 11:38:22 results will be moved to on success: /home/mvanvugt/projects/lipid_adem/data/temp
[info]  2026-10-21 11:38:22 bcftools 1.18
[info]  2026-10-21 11:38:22 8 genes in /home/mvanvugt/projects/lipid_adem/data/raw/gene_list.txt
[info]  2026-10-21 11:38:22 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:39:51 CETP (ENSG00000087237, chr16:56961980-56983663): 6848 rows
[info]  2026-10-21 11:39:52 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr5_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:41:35 HMGCR (ENSG00000113161, chr5:75342606-75360339): 20751 rows
[info]  2026-10-21 11:41:44 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr7_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:44:10 NPC1L1 (ENSG00000015520, chr7:44513450-44541259): 9909 rows
[info]  2026-10-21 11:44:10 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:45:43 PCSK9 (ENSG00000169174, chr1:55039838-55063581): 15046 rows
[info]  2026-10-21 11:46:33 ANGPTL3 (ENSG00000132855, chr1:62597567-62604814): 2406 rows
[info]  2026-10-21 11:46:34 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr22_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:47:17 PPARA (ENSG00000186951, chr22:46198384-46235377): 2982 rows
[info]  2026-10-21 11:47:18 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr11_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:47:50 APOA1 (ENSG00000118137, chr11:116834677-116842065): 2805 rows
[info]  2026-10-21 11:47:51 /projects/0/aus20644/data/ukbiobank/genetics/b38/lof/chr2_merged_vep.vcf.gz: 377567 samples
[info]  2026-10-21 11:53:24 APOB (ENSG00000084674, chr2:21001305-21044075): 18416 rows
[info]  2026-10-21 11:53:26 8 genes written to /scratch-local/mvanvugt.28412845/tmp.rj01qmYBde/task_1/vep_lipid_gene_csq.tsv.gz

```

## [10] slurm_script_extract_task1
- first run: 2026-10-22 03:17:59
- last run: 2026-10-22 04:43:47
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:43:45 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:43:45 stage: extract
[info]  2026-10-22 04:43:45 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:43:45 node: tcn4.local.snellius.surf.nl, job id: 28455323, task: 1
[info]  2026-10-22 04:43:45 task 1: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr1.vcf.gz
[info]  2026-10-22 04:43:47 extract vep_chr1.vcf.gz: finished

```

## [10] slurm_script_extract_task2
- first run: 2026-10-22 03:17:58
- last run: 2026-10-22 04:43:12
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:43:09 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:43:09 stage: extract
[info]  2026-10-22 04:43:09 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:43:09 node: tcn4.local.snellius.surf.nl, job id: 28455324, task: 2
[info]  2026-10-22 04:43:09 task 2: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr11.vcf.gz
[info]  2026-10-22 04:43:12 extract vep_chr11.vcf.gz: finished

```

## [10] slurm_script_extract_task3
- first run: 2026-10-22 03:17:57
- last run: 2026-10-22 04:48:21
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:48:19 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:48:19 stage: extract
[info]  2026-10-22 04:48:19 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:48:19 node: tcn4.local.snellius.surf.nl, job id: 28455325, task: 3
[info]  2026-10-22 04:48:19 task 3: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr2.vcf.gz
[info]  2026-10-22 04:48:21 extract vep_chr2.vcf.gz: finished

```

## [10] slurm_script_extract_task4
- first run: 2026-10-22 03:37:57
- last run: 2026-10-22 04:43:13
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:43:11 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:43:11 stage: extract
[info]  2026-10-22 04:43:11 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:43:11 node: tcn6.local.snellius.surf.nl, job id: 28455326, task: 4
[info]  2026-10-22 04:43:11 task 4: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr19.vcf.gz
[info]  2026-10-22 04:43:13 extract vep_chr19.vcf.gz: finished

```

## [10] slurm_script_extract_task5
- first run: 2026-10-22 03:18:01
- last run: 2026-10-22 04:44:22
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:44:19 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:44:19 stage: extract
[info]  2026-10-22 04:44:19 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:44:19 node: tcn4.local.snellius.surf.nl, job id: 28455327, task: 5
[info]  2026-10-22 04:44:19 task 5: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr16.vcf.gz
[info]  2026-10-22 04:44:21 extract vep_chr16.vcf.gz: finished

```

## [10] slurm_script_extract_task6
- first run: 2026-10-22 03:17:58
- last run: 2026-10-22 04:43:13
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:43:10 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:43:10 stage: extract
[info]  2026-10-22 04:43:10 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:43:10 node: tcn17.local.snellius.surf.nl, job id: 28455328, task: 6
[info]  2026-10-22 04:43:10 task 6: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr5.vcf.gz
[info]  2026-10-22 04:43:12 extract vep_chr5.vcf.gz: finished

```

## [10] slurm_script_extract_task7
- first run: 2026-10-22 04:30:10
- last run: 2026-10-22 04:42:39
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:36 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:42:36 stage: extract
[info]  2026-10-22 04:42:36 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:36 node: tcn20.local.snellius.surf.nl, job id: 28455329, task: 7
[info]  2026-10-22 04:42:36 task 7: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr7.vcf.gz
[info]  2026-10-22 04:42:38 extract vep_chr7.vcf.gz: finished

```

## [10] slurm_script_extract_task8
- first run: 2026-10-22 04:30:44
- last run: 2026-10-22 04:42:48
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:36 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:42:36 stage: extract
[info]  2026-10-22 04:42:36 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:36 node: tcn24.local.snellius.surf.nl, job id: 28455321, task: 8
[info]  2026-10-22 04:42:36 task 8: /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr22.vcf.gz
[info]  2026-10-22 04:42:48 extract vep_chr22.vcf.gz: finished

```

## [10] slurm_script_final_task1
- first run: 2026-10-22 04:37:33
- last run: 2026-10-22 04:51:38
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:48:53 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 04:48:53 stage: final
[info]  2026-10-22 04:48:53 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:48:53 node: tcn4.local.snellius.surf.nl, job id: 28455322, task: 1
[info]  2026-10-22 04:49:25 aggregate: finished
[info]  2026-10-22 04:51:38 associate: finished

```

## [10] slurm_script_step2_CETP_compare
- first run: 2026-10-24 22:16:32
- last run: 2026-10-24 22:16:32
- commit: `6fc4384` (dirty)
- status: failed

Output:
```text
[error] 2026-10-24 22:16:32 -s/--step must look like step4 or step4_small, not 'step2_CETP'
--- error output (raw) ---


```

## [10] slurm_script_step2_PCSK9_compare
- first run: 2026-10-24 22:16:34
- last run: 2026-10-26 11:32:16
- commit: `fdddf24` (dirty)

Output:
```text
[info]  2026-10-26 11:32:04 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step2_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-26 11:32:04 working directory (temporary): /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1
[warn]  2026-10-26 11:32:04 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-26 11:32:04 manifest: 6 file(s) in /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1/step2_PCSK9.compare.md5
[warn]  2026-10-26 11:32:16 step2_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step2_PCSK9/summary.tsv.gz
[info]  2026-10-26 11:32:16 *** END ***

```

## [10] slurm_script_step2_old
- first run: 2026-10-24 11:01:37
- last run: 2026-10-24 17:15:11
- commit: `6fc4384` (dirty)

Output:
```text
[info]  2026-10-24 15:36:25 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step2; mode: old; env: marvel_old
[info]  2026-10-24 15:36:25 working directory (temporary): /scratch-local/mvanvugt.28545065/tmp.TgMXLqNqxG/task_1
[info]  2026-10-24 15:36:25 manifest: 8 file(s) in /scratch-local/mvanvugt.28545065/tmp.TgMXLqNqxG/task_1/step2.old.md5
[info]  2026-10-24 17:15:11 *** END ***

```

## [10] slurm_script_vep_prep_task1
- first run: 2026-10-22 04:22:14
- last run: 2026-10-22 04:43:05
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:01 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:01 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:01 task 1: chr 1, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr1.vcf.gz
[info]  2026-10-22 04:43:05 chr 1: 0

```

## [10] slurm_script_vep_prep_task2
- first run: 2026-10-22 04:22:17
- last run: 2026-10-22 04:42:32
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:02 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:02 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:02 task 2: chr 11, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr11_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr11.vcf.gz
[info]  2026-10-22 04:42:32 chr 11: 18

```

## [10] slurm_script_vep_prep_task3
- first run: 2026-10-22 04:22:15
- last run: 2026-10-22 04:47:45
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:02 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:02 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:03 task 3: chr 2, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr2_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr2.vcf.gz
[info]  2026-10-22 04:47:45 chr 2: 178

```

## [10] slurm_script_vep_prep_task4
- first run: 2026-10-22 04:22:19
- last run: 2026-10-22 04:42:39
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:02 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:02 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:03 task 4: chr 19, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr19_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr19.vcf.gz
[info]  2026-10-22 04:42:39 chr 19: 8

```

## [10] slurm_script_vep_prep_task5
- first run: 2026-10-22 04:22:14
- last run: 2026-10-22 04:43:36
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:02 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:02 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:03 task 5: chr 16, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr16.vcf.gz
[info]  2026-10-22 04:43:36 chr 16: 58

```

## [10] slurm_script_vep_prep_task6
- first run: 2026-10-22 04:22:26
- last run: 2026-10-22 04:42:29
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:03 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:03 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:04 task 6: chr 5, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr5_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr5.vcf.gz
[info]  2026-10-22 04:42:28 chr 5: 0

```

## [10] slurm_script_vep_prep_task7
- first run: 2026-10-22 04:22:22
- last run: 2026-10-22 04:42:06
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:02 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:02 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:03 task 7: chr 7, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr7_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr7.vcf.gz
[info]  2026-10-22 04:42:05 chr 7: no VEP fallback variants; header-only chunk
[info]  2026-10-22 04:42:06 chr 7: 0

```

## [10] slurm_script_vep_prep_task8
- first run: 2026-10-22 04:22:13
- last run: 2026-10-22 04:42:08
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:42:03 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:42:03 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:42:04 task 8: chr 22, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr22_merged_vep.vcf.gz -> /home/mvanvugt/projects/lipid_adem/data/temp/marvel/two_source/vep/vep_chr22.vcf.gz
[info]  2026-10-22 04:42:07 chr 22: no VEP fallback variants; header-only chunk
[info]  2026-10-22 04:42:07 chr 22: 0

```

## [10] submit_two_source_submit_task1
- first run: 2026-10-21 21:41:00
- last run: 2026-10-22 04:41:12
- commit: `461486d` (dirty)

Output:
```text
[info]  2026-10-22 04:41:01 env: /home/mvanvugt/mambaforge/envs/marvel
[info]  2026-10-22 04:41:01 stage: submit; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 04:41:09 5 plink gene VCF(s); chromosomes: 1 11 2 19 16 5 7 22
[info]  2026-10-22 04:41:12 submitted: J1 28455319, J2 28455320, J3 28455321, J4 28455322

```

## [10] subset_carriers (`validation/subset_carriers.py --carriers /gpfs/home6/mvanvugt/projects/cetp_marvel/results/output/lipids_variant_carriers_carriers.tsv.gz --output data/temp/validation/step2b/PCSK9_carriers.tsv.gz --region chr1:55038000-55066000 --drop-merged --negative-to-na`)
- first run: 2026-10-26 16:12:11
- last run: 2026-10-26 19:16:12
- commit: `7a3cab3` (dirty)

Δ vs previous run (was `7a3cab3` (dirty)):
```diff
@@ -1,4 +1,4 @@
-[info]  2026-10-26 19:11:39 chr16:56960000-56985000: 426 of 8662 variant columns kept (0 merged names, drop_merged=True)
-[info]  2026-10-26 19:15:31 wrote 469835 rows x 427 columns to data/temp/validation/step2b/CETP_carriers.tsv.gz
-[info]  2026-10-26 19:15:31 negative values written as NA: 44844 cells
-[info]  2026-10-26 19:15:31 value counts over variant cells: {'0': 195904414, '2': 2430237, '1': 1770215, 'NA': 44844}
+[info]  2026-10-26 19:11:39 chr1:55038000-55066000: 539 of 8662 variant columns kept (0 merged names, drop_merged=True)
+[info]  2026-10-26 19:16:12 wrote 469835 rows x 540 columns to data/temp/validation/step2b/PCSK9_carriers.tsv.gz
+[info]  2026-10-26 19:16:12 negative values written as NA: 2665 cells
+[info]  2026-10-26 19:16:12 value counts over variant cells: {'0': 252289475, '2': 754253, '1': 194672, 'NA': 2665}
```

Output:
```text
[info]  2026-10-26 19:11:39 chr1:55038000-55066000: 539 of 8662 variant columns kept (0 merged names, drop_merged=True)
[info]  2026-10-26 19:16:12 wrote 469835 rows x 540 columns to data/temp/validation/step2b/PCSK9_carriers.tsv.gz
[info]  2026-10-26 19:16:12 negative values written as NA: 2665 cells
[info]  2026-10-26 19:16:12 value counts over variant cells: {'0': 252289475, '2': 754253, '1': 194672, 'NA': 2665}

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

## [22] burden_exposure (`/home/mvanvugt/projects/lipid_adem/src/burden_exposure.py`)
- first run: 2026-10-26 11:05:30
- last run: 2026-10-26 17:02:40
- commit: `7a3cab3` (dirty)

Output:
```text
[stage] 2026-10-26 17:00:42 variant sets
[warn]  2026-10-26 17:00:42 5 site(s) both LoF-listed and GoF/raising, in the gof mask only: 1:55044016:T:A, 1:55044016:T:G, 1:55052400:T:C, 1:55057395:A:T, 1:55059525:T:C
[info]  2026-10-26 17:00:42 ANGPTL3: 554 listed sites; gof 0, am 493, ptv 56, clinvar 12, clinvar_directed 12, lof 62, lof_directed 62, ptv_am 549, am_clinvar 504, am_clinvar_directed 504, ptv_clinvar_am 554, ptv_clinvar_am_directed 554
[info]  2026-10-26 17:00:42 CETP: 502 listed sites; gof 1, am 439, ptv 58, clinvar 10, clinvar_directed 10, lof 62, lof_directed 62, ptv_am 497, am_clinvar 449, am_clinvar_directed 449, ptv_clinvar_am 501, ptv_clinvar_am_directed 501
[info]  2026-10-26 17:00:42 HMGCR: 2668 listed sites; gof 0, am 2623, ptv 39, clinvar 7, clinvar_directed 6, lof 45, lof_directed 44, ptv_am 2662, am_clinvar 2630, am_clinvar_directed 2629, ptv_clinvar_am 2668, ptv_clinvar_am_directed 2667
[info]  2026-10-26 17:00:42 NPC1L1: 2603 listed sites; gof 0, am 2507, ptv 96, clinvar 0, clinvar_directed 0, lof 96, lof_directed 96, ptv_am 2603, am_clinvar 2507, am_clinvar_directed 2507, ptv_clinvar_am 2603, ptv_clinvar_am_directed 2603
[info]  2026-10-26 17:00:42 PCSK9: 831 listed sites; gof 29, am 732, ptv 68, clinvar 2, clinvar_directed 2, lof 70, lof_directed 70, ptv_am 800, am_clinvar 734, am_clinvar_directed 734, ptv_clinvar_am 802, ptv_clinvar_am_directed 802
[info]  2026-10-26 17:00:42 PPARA: 1566 listed sites; gof 0, am 1543, ptv 23, clinvar 0, clinvar_directed 0, lof 23, lof_directed 23, ptv_am 1566, am_clinvar 1543, am_clinvar_directed 1543, ptv_clinvar_am 1566, ptv_clinvar_am_directed 1566
[info]  2026-10-26 17:00:42 CETP: 1 sites in preferred studies
[info]  2026-10-26 17:00:43 genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[info]  2026-10-26 17:00:43 population: eur_unrelated=328588, eur_related=64495, nan=56362, sas_related=9394, afr_related=9141, oth_related=1607
[stage] 2026-10-26 17:00:43 CETP
[info]  2026-10-26 17:00:43 CETP_variant_extraction.tsv.gz: 668 columns, 1 not a variant (ID, merged names), 195 repeated, 273 hold a listed site (93 sites)
[info]  2026-10-26 17:00:50 CETP: 469835 samples
[info]  2026-10-26 17:00:51 CETP_gof: 1 of 1 sites, 34836 carriers
[info]  2026-10-26 17:00:51 CETP_gof_fb: 1 of 1 sites, 34836 carriers
[info]  2026-10-26 17:00:51 CETP_am: 34 of 439 sites, 496 carriers
[info]  2026-10-26 17:00:51 CETP_am_fb: 34 of 439 sites, 496 carriers
[info]  2026-10-26 17:00:51 CETP_ptv: 58 of 58 sites, 473 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_fb: 58 of 58 sites, 473 carriers
[info]  2026-10-26 17:00:51 CETP_clinvar: 6 of 10 sites, 47 carriers
[info]  2026-10-26 17:00:51 CETP_clinvar_fb: 6 of 10 sites, 47 carriers
[info]  2026-10-26 17:00:51 CETP_clinvar_directed: 6 of 10 sites, 47 carriers
[info]  2026-10-26 17:00:51 CETP_clinvar_directed_fb: 6 of 10 sites, 47 carriers
[info]  2026-10-26 17:00:51 CETP_lof: 58 of 62 sites, 473 carriers
[info]  2026-10-26 17:00:51 CETP_lof_fb: 58 of 62 sites, 473 carriers
[info]  2026-10-26 17:00:51 CETP_lof_directed: 58 of 62 sites, 473 carriers
[info]  2026-10-26 17:00:51 CETP_lof_directed_fb: 58 of 62 sites, 473 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_am: 92 of 497 sites, 948 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_am_fb: 92 of 497 sites, 948 carriers
[info]  2026-10-26 17:00:51 CETP_am_clinvar: 40 of 449 sites, 543 carriers
[info]  2026-10-26 17:00:51 CETP_am_clinvar_fb: 40 of 449 sites, 543 carriers
[info]  2026-10-26 17:00:51 CETP_am_clinvar_directed: 40 of 449 sites, 543 carriers
[info]  2026-10-26 17:00:51 CETP_am_clinvar_directed_fb: 40 of 449 sites, 543 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_clinvar_am: 92 of 501 sites, 948 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_clinvar_am_fb: 92 of 501 sites, 948 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_clinvar_am_directed: 92 of 501 sites, 948 carriers
[info]  2026-10-26 17:00:51 CETP_ptv_clinvar_am_directed_fb: 92 of 501 sites, 948 carriers
[info]  2026-10-26 17:00:55 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_burden_exposure.tsv.gz
[info]  2026-10-26 17:00:59 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_burden_exposure_fb.tsv.gz
[info]  2026-10-26 17:01:00 CETP_all_apoe: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/CETP_all_apoe.cnf
[info]  2026-10-26 17:01:04 CETP_eur: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/CETP_eur.cnf
[info]  2026-10-26 17:01:04 CETP_all_apoe_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/CETP_all_apoe_fb.cnf
[info]  2026-10-26 17:01:04 CETP_eur_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/CETP_eur_fb.cnf
[stage] 2026-10-26 17:01:04 HMGCR
[info]  2026-10-26 17:01:04 HMGCR_variant_extraction.tsv.gz: 715 columns, 1 not a variant (ID, merged names), 282 repeated, 444 hold a listed site (170 sites)
[info]  2026-10-26 17:01:14 HMGCR: 469835 samples
[warn]  2026-10-26 17:01:15 HMGCR_gof: no carriers (0 sites), not written
[warn]  2026-10-26 17:01:15 HMGCR_gof_fb: no carriers (0 sites), not written
[info]  2026-10-26 17:01:15 HMGCR_am: 128 of 2623 sites, 320 carriers
[info]  2026-10-26 17:01:15 HMGCR_am_fb: 128 of 2623 sites, 320 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv: 39 of 39 sites, 77 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_fb: 39 of 39 sites, 77 carriers
[info]  2026-10-26 17:01:15 HMGCR_clinvar: 4 of 7 sites, 13 carriers
[info]  2026-10-26 17:01:15 HMGCR_clinvar_fb: 4 of 7 sites, 13 carriers
[info]  2026-10-26 17:01:15 HMGCR_clinvar_directed: 3 of 6 sites, 9 carriers
[info]  2026-10-26 17:01:15 HMGCR_clinvar_directed_fb: 3 of 6 sites, 9 carriers
[info]  2026-10-26 17:01:15 HMGCR_lof: 42 of 45 sites, 85 carriers
[info]  2026-10-26 17:01:15 HMGCR_lof_fb: 42 of 45 sites, 85 carriers
[info]  2026-10-26 17:01:15 HMGCR_lof_directed: 41 of 44 sites, 81 carriers
[info]  2026-10-26 17:01:15 HMGCR_lof_directed_fb: 41 of 44 sites, 81 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_am: 167 of 2662 sites, 397 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_am_fb: 167 of 2662 sites, 397 carriers
[info]  2026-10-26 17:01:15 HMGCR_am_clinvar: 132 of 2630 sites, 333 carriers
[info]  2026-10-26 17:01:15 HMGCR_am_clinvar_fb: 132 of 2630 sites, 333 carriers
[info]  2026-10-26 17:01:15 HMGCR_am_clinvar_directed: 131 of 2629 sites, 329 carriers
[info]  2026-10-26 17:01:15 HMGCR_am_clinvar_directed_fb: 131 of 2629 sites, 329 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_clinvar_am: 170 of 2668 sites, 405 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_clinvar_am_fb: 170 of 2668 sites, 405 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_clinvar_am_directed: 169 of 2667 sites, 401 carriers
[info]  2026-10-26 17:01:15 HMGCR_ptv_clinvar_am_directed_fb: 169 of 2667 sites, 401 carriers
[info]  2026-10-26 17:01:19 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_burden_exposure.tsv.gz
[info]  2026-10-26 17:01:22 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_burden_exposure_fb.tsv.gz
[info]  2026-10-26 17:01:22 HMGCR_all_apoe: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/HMGCR_all_apoe.cnf
[info]  2026-10-26 17:01:22 HMGCR_eur: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/HMGCR_eur.cnf
[info]  2026-10-26 17:01:22 HMGCR_all_apoe_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/HMGCR_all_apoe_fb.cnf
[info]  2026-10-26 17:01:22 HMGCR_eur_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/HMGCR_eur_fb.cnf
[stage] 2026-10-26 17:01:22 NPC1L1
[info]  2026-10-26 17:01:23 NPC1L1_variant_extraction.tsv.gz: 1262 columns, 1 not a variant (ID, merged names), 236 repeated, 501 hold a listed site (267 sites)
[info]  2026-10-26 17:01:40 NPC1L1: 469835 samples
[warn]  2026-10-26 17:01:41 NPC1L1_gof: no carriers (0 sites), not written
[warn]  2026-10-26 17:01:41 NPC1L1_gof_fb: no carriers (0 sites), not written
[info]  2026-10-26 17:01:41 NPC1L1_am: 174 of 2507 sites, 1748 carriers
[info]  2026-10-26 17:01:41 NPC1L1_am_fb: 174 of 2507 sites, 1748 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv: 93 of 96 sites, 669 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_fb: 93 of 96 sites, 669 carriers
[warn]  2026-10-26 17:01:41 NPC1L1_clinvar: no carriers (0 sites), not written
[warn]  2026-10-26 17:01:41 NPC1L1_clinvar_fb: no carriers (0 sites), not written
[warn]  2026-10-26 17:01:41 NPC1L1_clinvar_directed: no carriers (0 sites), not written
[warn]  2026-10-26 17:01:41 NPC1L1_clinvar_directed_fb: no carriers (0 sites), not written
[info]  2026-10-26 17:01:41 NPC1L1_lof: 93 of 96 sites, 669 carriers
[info]  2026-10-26 17:01:41 NPC1L1_lof_fb: 93 of 96 sites, 669 carriers
[info]  2026-10-26 17:01:41 NPC1L1_lof_directed: 93 of 96 sites, 669 carriers
[info]  2026-10-26 17:01:41 NPC1L1_lof_directed_fb: 93 of 96 sites, 669 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_am: 267 of 2603 sites, 2412 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_am_fb: 267 of 2603 sites, 2412 carriers
[info]  2026-10-26 17:01:41 NPC1L1_am_clinvar: 174 of 2507 sites, 1748 carriers
[info]  2026-10-26 17:01:41 NPC1L1_am_clinvar_fb: 174 of 2507 sites, 1748 carriers
[info]  2026-10-26 17:01:41 NPC1L1_am_clinvar_directed: 174 of 2507 sites, 1748 carriers
[info]  2026-10-26 17:01:41 NPC1L1_am_clinvar_directed_fb: 174 of 2507 sites, 1748 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_clinvar_am: 267 of 2603 sites, 2412 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_clinvar_am_fb: 267 of 2603 sites, 2412 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_clinvar_am_directed: 267 of 2603 sites, 2412 carriers
[info]  2026-10-26 17:01:41 NPC1L1_ptv_clinvar_am_directed_fb: 267 of 2603 sites, 2412 carriers
[info]  2026-10-26 17:01:44 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_burden_exposure.tsv.gz
[info]  2026-10-26 17:01:48 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_burden_exposure_fb.tsv.gz
[info]  2026-10-26 17:01:48 NPC1L1_all_apoe: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/NPC1L1_all_apoe.cnf
[info]  2026-10-26 17:01:48 NPC1L1_eur: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/NPC1L1_eur.cnf
[info]  2026-10-26 17:01:48 NPC1L1_all_apoe_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/NPC1L1_all_apoe_fb.cnf
[info]  2026-10-26 17:01:48 NPC1L1_eur_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/NPC1L1_eur_fb.cnf
[stage] 2026-10-26 17:01:48 PCSK9
[info]  2026-10-26 17:01:48 PCSK9_variant_extraction.tsv.gz: 1048 columns, 1 not a variant (ID, merged names), 425 repeated, 515 hold a listed site (131 sites)
[info]  2026-10-26 17:02:04 PCSK9: 469835 samples
[info]  2026-10-26 17:02:04 PCSK9_gof: 14 of 29 sites, 953 carriers
[info]  2026-10-26 17:02:04 PCSK9_gof_fb: 14 of 29 sites, 953 carriers
[info]  2026-10-26 17:02:04 PCSK9_am: 49 of 732 sites, 590 carriers
[info]  2026-10-26 17:02:04 PCSK9_am_fb: 49 of 732 sites, 590 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv: 68 of 68 sites, 937 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_fb: 68 of 68 sites, 937 carriers
[warn]  2026-10-26 17:02:04 PCSK9_clinvar: no carriers (2 sites), not written
[warn]  2026-10-26 17:02:04 PCSK9_clinvar_fb: no carriers (2 sites), not written
[warn]  2026-10-26 17:02:04 PCSK9_clinvar_directed: no carriers (2 sites), not written
[warn]  2026-10-26 17:02:04 PCSK9_clinvar_directed_fb: no carriers (2 sites), not written
[info]  2026-10-26 17:02:04 PCSK9_lof: 68 of 70 sites, 937 carriers
[info]  2026-10-26 17:02:04 PCSK9_lof_fb: 68 of 70 sites, 937 carriers
[info]  2026-10-26 17:02:04 PCSK9_lof_directed: 68 of 70 sites, 937 carriers
[info]  2026-10-26 17:02:04 PCSK9_lof_directed_fb: 68 of 70 sites, 937 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_am: 117 of 800 sites, 1521 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_am_fb: 117 of 800 sites, 1521 carriers
[info]  2026-10-26 17:02:04 PCSK9_am_clinvar: 49 of 734 sites, 590 carriers
[info]  2026-10-26 17:02:04 PCSK9_am_clinvar_fb: 49 of 734 sites, 590 carriers
[info]  2026-10-26 17:02:04 PCSK9_am_clinvar_directed: 49 of 734 sites, 590 carriers
[info]  2026-10-26 17:02:04 PCSK9_am_clinvar_directed_fb: 49 of 734 sites, 590 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_clinvar_am: 117 of 802 sites, 1521 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_clinvar_am_fb: 117 of 802 sites, 1521 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_clinvar_am_directed: 117 of 802 sites, 1521 carriers
[info]  2026-10-26 17:02:04 PCSK9_ptv_clinvar_am_directed_fb: 117 of 802 sites, 1521 carriers
[info]  2026-10-26 17:02:08 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_burden_exposure.tsv.gz
[info]  2026-10-26 17:02:11 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_burden_exposure_fb.tsv.gz
[info]  2026-10-26 17:02:11 PCSK9_all_apoe: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PCSK9_all_apoe.cnf
[info]  2026-10-26 17:02:11 PCSK9_eur: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PCSK9_eur.cnf
[info]  2026-10-26 17:02:11 PCSK9_all_apoe_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PCSK9_all_apoe_fb.cnf
[info]  2026-10-26 17:02:11 PCSK9_eur_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PCSK9_eur_fb.cnf
[stage] 2026-10-26 17:02:11 ANGPTL3
[info]  2026-10-26 17:02:11 ANGPTL3_variant_extraction.tsv.gz: 325 columns, 1 not a variant (ID, merged names), 4 repeated, 94 hold a listed site (90 sites)
[info]  2026-10-26 17:02:14 ANGPTL3: 469835 samples
[warn]  2026-10-26 17:02:14 ANGPTL3_gof: no carriers (0 sites), not written
[warn]  2026-10-26 17:02:14 ANGPTL3_gof_fb: no carriers (0 sites), not written
[info]  2026-10-26 17:02:14 ANGPTL3_am: 36 of 493 sites, 648 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_am_fb: 36 of 493 sites, 648 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_ptv: 54 of 56 sites, 974 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_ptv_fb: 54 of 56 sites, 974 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_clinvar: 6 of 12 sites, 769 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_clinvar_fb: 6 of 12 sites, 769 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_clinvar_directed: 6 of 12 sites, 769 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_clinvar_directed_fb: 6 of 12 sites, 769 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_lof: 54 of 62 sites, 974 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_lof_fb: 54 of 62 sites, 974 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_lof_directed: 54 of 62 sites, 974 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_lof_directed_fb: 54 of 62 sites, 974 carriers
[info]  2026-10-26 17:02:14 ANGPTL3_ptv_am: 90 of 549 sites, 1621 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_ptv_am_fb: 90 of 549 sites, 1621 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_am_clinvar: 42 of 504 sites, 1416 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_am_clinvar_fb: 42 of 504 sites, 1416 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_am_clinvar_directed: 42 of 504 sites, 1416 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_am_clinvar_directed_fb: 42 of 504 sites, 1416 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_ptv_clinvar_am: 90 of 554 sites, 1621 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_ptv_clinvar_am_fb: 90 of 554 sites, 1621 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_ptv_clinvar_am_directed: 90 of 554 sites, 1621 carriers
[info]  2026-10-26 17:02:15 ANGPTL3_ptv_clinvar_am_directed_fb: 90 of 554 sites, 1621 carriers
[info]  2026-10-26 17:02:18 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_burden_exposure.tsv.gz
[info]  2026-10-26 17:02:22 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_burden_exposure_fb.tsv.gz
[info]  2026-10-26 17:02:22 ANGPTL3_all_apoe: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/ANGPTL3_all_apoe.cnf
[info]  2026-10-26 17:02:22 ANGPTL3_eur: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/ANGPTL3_eur.cnf
[info]  2026-10-26 17:02:22 ANGPTL3_all_apoe_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/ANGPTL3_all_apoe_fb.cnf
[info]  2026-10-26 17:02:22 ANGPTL3_eur_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/ANGPTL3_eur_fb.cnf
[stage] 2026-10-26 17:02:22 PPARA
[info]  2026-10-26 17:02:22 PPARA_variant_extraction.tsv.gz: 344 columns, 1 not a variant (ID, merged names), 43 repeated, 161 hold a listed site (124 sites)
[info]  2026-10-26 17:02:26 PPARA: 469835 samples
[warn]  2026-10-26 17:02:27 PPARA_gof: no carriers (0 sites), not written
[warn]  2026-10-26 17:02:27 PPARA_gof_fb: no carriers (0 sites), not written
[info]  2026-10-26 17:02:27 PPARA_am: 102 of 1543 sites, 1135 carriers
[info]  2026-10-26 17:02:27 PPARA_am_fb: 102 of 1543 sites, 1135 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv: 22 of 23 sites, 73 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_fb: 22 of 23 sites, 73 carriers
[warn]  2026-10-26 17:02:27 PPARA_clinvar: no carriers (0 sites), not written
[warn]  2026-10-26 17:02:27 PPARA_clinvar_fb: no carriers (0 sites), not written
[warn]  2026-10-26 17:02:27 PPARA_clinvar_directed: no carriers (0 sites), not written
[warn]  2026-10-26 17:02:27 PPARA_clinvar_directed_fb: no carriers (0 sites), not written
[info]  2026-10-26 17:02:27 PPARA_lof: 22 of 23 sites, 73 carriers
[info]  2026-10-26 17:02:27 PPARA_lof_fb: 22 of 23 sites, 73 carriers
[info]  2026-10-26 17:02:27 PPARA_lof_directed: 22 of 23 sites, 73 carriers
[info]  2026-10-26 17:02:27 PPARA_lof_directed_fb: 22 of 23 sites, 73 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_am: 124 of 1566 sites, 1208 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_am_fb: 124 of 1566 sites, 1208 carriers
[info]  2026-10-26 17:02:27 PPARA_am_clinvar: 102 of 1543 sites, 1135 carriers
[info]  2026-10-26 17:02:27 PPARA_am_clinvar_fb: 102 of 1543 sites, 1135 carriers
[info]  2026-10-26 17:02:27 PPARA_am_clinvar_directed: 102 of 1543 sites, 1135 carriers
[info]  2026-10-26 17:02:27 PPARA_am_clinvar_directed_fb: 102 of 1543 sites, 1135 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_clinvar_am: 124 of 1566 sites, 1208 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_clinvar_am_fb: 124 of 1566 sites, 1208 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_clinvar_am_directed: 124 of 1566 sites, 1208 carriers
[info]  2026-10-26 17:02:27 PPARA_ptv_clinvar_am_directed_fb: 124 of 1566 sites, 1208 carriers
[info]  2026-10-26 17:02:30 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_burden_exposure.tsv.gz
[info]  2026-10-26 17:02:33 wrote 469835 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_burden_exposure_fb.tsv.gz
[info]  2026-10-26 17:02:33 PPARA_all_apoe: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PPARA_all_apoe.cnf
[info]  2026-10-26 17:02:33 PPARA_eur: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PPARA_eur.cnf
[info]  2026-10-26 17:02:33 PPARA_all_apoe_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PPARA_all_apoe_fb.cnf
[info]  2026-10-26 17:02:33 PPARA_eur_fb: /gpfs/home6/mvanvugt/projects/lipid_adem/config/marvel_burden/PPARA_eur_fb.cnf
[info]  2026-10-26 17:02:39 wrote 24 job-array rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv
[info]  2026-10-26 17:02:39 wrote 144 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/burden_exposure_summary.tsv.gz

```

## [25] marvel_results_table (`/home/mvanvugt/projects/lipid_adem/src/marvel_results_table.py --ancestry MULTI --tasks /home/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv --refresh`)
- first run: 2026-10-08 09:54:25
- last run: 2026-10-26 17:42:21
- commit: `7a3cab3` (dirty)

Output:
```text
[stage] 2026-10-26 17:42:15 compare
[info]  2026-10-26 17:42:15 /home/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv: 24 rows, 6 genes
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_all_apoe: 12 loose result files
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur: 12 loose result files
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_all_apoe_fb: 12 loose result files
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur_fb: 12 loose result files
[info]  2026-10-26 17:42:16 CETP: refreshed, 14520 rows
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_all_apoe: 11 loose result files
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_eur: 11 loose result files
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_all_apoe_fb: 11 loose result files
[info]  2026-10-26 17:42:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_eur_fb: 11 loose result files
[info]  2026-10-26 17:42:17 HMGCR: refreshed, 12680 rows
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_all_apoe: 9 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_eur: 9 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_all_apoe_fb: 9 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_eur_fb: 9 loose result files
[info]  2026-10-26 17:42:17 NPC1L1: refreshed, 10890 rows
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_all_apoe: 10 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_eur: 10 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_all_apoe_fb: 10 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_eur_fb: 10 loose result files
[info]  2026-10-26 17:42:17 PCSK9: refreshed, 12100 rows
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_all_apoe: 11 loose result files
[info]  2026-10-26 17:42:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_eur: 11 loose result files
[info]  2026-10-26 17:42:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_all_apoe_fb: 11 loose result files
[info]  2026-10-26 17:42:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_eur_fb: 11 loose result files
[info]  2026-10-26 17:42:18 ANGPTL3: refreshed, 13310 rows
[info]  2026-10-26 17:42:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_all_apoe: 9 loose result files
[info]  2026-10-26 17:42:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_eur: 9 loose result files
[info]  2026-10-26 17:42:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_all_apoe_fb: 9 loose result files
[info]  2026-10-26 17:42:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_eur_fb: 9 loose result files
[info]  2026-10-26 17:42:18 PPARA: refreshed, 10890 rows
[stage] 2026-10-26 17:42:18 write_stores
[info]  2026-10-26 17:42:18 CETP: old store kept as CETP_results.20261026_174215.tsv.gz
[info]  2026-10-26 17:42:19 CETP: wrote 14520 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/CETP_results.tsv.gz
[info]  2026-10-26 17:42:19 HMGCR: old store kept as HMGCR_results.20261026_174215.tsv.gz
[info]  2026-10-26 17:42:19 HMGCR: wrote 12680 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/HMGCR_results.tsv.gz
[info]  2026-10-26 17:42:19 NPC1L1: old store kept as NPC1L1_results.20261026_174215.tsv.gz
[info]  2026-10-26 17:42:19 NPC1L1: wrote 10890 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/NPC1L1_results.tsv.gz
[info]  2026-10-26 17:42:19 PCSK9: old store kept as PCSK9_results.20261026_174215.tsv.gz
[info]  2026-10-26 17:42:19 PCSK9: wrote 12100 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/PCSK9_results.tsv.gz
[info]  2026-10-26 17:42:20 ANGPTL3: old store kept as ANGPTL3_results.20261026_174215.tsv.gz
[info]  2026-10-26 17:42:20 ANGPTL3: wrote 13310 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/ANGPTL3_results.tsv.gz
[info]  2026-10-26 17:42:20 PPARA: old store kept as PPARA_results.20261026_174215.tsv.gz
[info]  2026-10-26 17:42:20 PPARA: wrote 10890 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/PPARA_results.tsv.gz
[stage] 2026-10-26 17:42:20 marvel_table
[info]  2026-10-26 17:42:21 wrote 600 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-10-26 17:42:21 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: all marvel strata already listed

```

## [28] compare_results (`/gpfs/home6/mvanvugt/projects/lipid_adem/validation/compare_results.py --left validation/PCSK9_PTV_results.tsv.gz --left-format old --right data/temp/validation/step2/PCSK9 --right-format old --exposures PCSK9 PTV --all-models --left-outcome-map Apolipoprotein A=Apolipoprotein A_i0 Apolipoprotein B=Apolipoprotein B_i0 HDL cholesterol=HDL cholesterol_i0 LDL direct=LDL direct_i0 Triglycerides=Triglycerides_i0 alzheimers_algo=alzheimers_disease_algo alzheimers_algo_prevalent=alzheimers_disease_algo_prevalent alzheimers_algo_incident=alzheimers_disease_algo_incident --outcomes Apolipoprotein A_i0 Apolipoprotein B_i0 HDL cholesterol_i0 LDL direct_i0 Triglycerides_i0 ascvd_ii vascular_dementia_algo frontotemporal_dementia_algo all_cause_dementia_algo alzheimers_disease_algo all_cause_dementia_combined alzheimers_disease_combined ascvd_ii_prevalent ascvd_ii_incident vascular_dementia_algo_prevalent vascular_dementia_algo_incident frontotemporal_dementia_algo_prevalent frontotemporal_dementia_algo_incident all_cause_dementia_algo_prevalent all_cause_dementia_algo_incident alzheimers_disease_algo_prevalent alzheimers_disease_algo_incident all_cause_dementia_combined_prevalent all_cause_dementia_combined_incident alzheimers_disease_combined_prevalent alzheimers_disease_combined_incident --out-dir /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1`)
- first run: 2026-10-26 11:32:16
- last run: 2026-10-26 11:32:16
- commit: `fdddf24` (dirty)

Output:
```text
[info]  2026-10-26 11:32:06 PCSK9_PTV_results.tsv.gz: 1472 rows, 128 kept
[info]  2026-10-26 11:32:06 left: 104 rows, 1 keys, outcomes ['Apolipoprotein A_i0', 'Apolipoprotein B_i0', 'HDL cholesterol_i0', 'LDL direct_i0', 'Triglycerides_i0', 'all_cause_dementia_algo', 'all_cause_dementia_algo_incident', 'all_cause_dementia_algo_prevalent', 'all_cause_dementia_combined', 'all_cause_dementia_combined_incident', 'all_cause_dementia_combined_prevalent', 'alzheimers_disease_algo', 'alzheimers_disease_algo_incident', 'alzheimers_disease_algo_prevalent', 'alzheimers_disease_combined', 'alzheimers_disease_combined_incident', 'alzheimers_disease_combined_prevalent', 'ascvd_ii', 'ascvd_ii_incident', 'ascvd_ii_prevalent', 'frontotemporal_dementia_algo', 'frontotemporal_dementia_algo_incident', 'frontotemporal_dementia_algo_prevalent', 'vascular_dementia_algo', 'vascular_dementia_algo_incident', 'vascular_dementia_algo_prevalent'], models ['model_1', 'model_2', 'model_3', 'model_4']
[info]  2026-10-26 11:32:06 PCSK9_PTV_results.tsv.gz: 1196 rows, 104 kept
[info]  2026-10-26 11:32:06 right: 104 rows, 1 keys, outcomes ['Apolipoprotein A_i0', 'Apolipoprotein B_i0', 'HDL cholesterol_i0', 'LDL direct_i0', 'Triglycerides_i0', 'all_cause_dementia_algo', 'all_cause_dementia_algo_incident', 'all_cause_dementia_algo_prevalent', 'all_cause_dementia_combined', 'all_cause_dementia_combined_incident', 'all_cause_dementia_combined_prevalent', 'alzheimers_disease_algo', 'alzheimers_disease_algo_incident', 'alzheimers_disease_algo_prevalent', 'alzheimers_disease_combined', 'alzheimers_disease_combined_incident', 'alzheimers_disease_combined_prevalent', 'ascvd_ii', 'ascvd_ii_incident', 'ascvd_ii_prevalent', 'frontotemporal_dementia_algo', 'frontotemporal_dementia_algo_incident', 'frontotemporal_dementia_algo_prevalent', 'vascular_dementia_algo', 'vascular_dementia_algo_incident', 'vascular_dementia_algo_prevalent'], models ['model_1', 'model_2', 'model_3', 'model_4']
[info]  2026-10-26 11:32:06 rows per class: {'differs_counts': 104}
[warn]  2026-10-26 11:32:06 GATE FAIL: 104 row(s) in ['differs_counts', 'differs_estimate', 'swapped', 'only_left', 'only_right']
[info]  2026-10-26 11:32:06 wrote 104 rows to /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1/rows.tsv.gz
[info]  2026-10-26 11:32:07 wrote 728 rows to /scratch-local/mvanvugt.28588171/tmp.AFopqM1cxT/task_1/summary.tsv.gz

```

## [30] merge_associations (`/home/mvanvugt/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-26 18:30:39
- commit: `7a3cab3` (dirty)

Output:
```text
[stage] 2026-10-26 17:44:22 load_sumstats
[warn]  2026-10-26 17:44:24 1 outfiles listed in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/study_outcomes.tsv do not exist yet, skipped (first: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/gwas_filtered/I9_CVD_HARD_result.tsv.gz)
[info]  2026-10-26 17:44:24 summary-stats: 124 files, 593027 rows incl. one copy per outcome (1 missing)
[info]  2026-10-26 17:44:30 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-26 17:44:30 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-26 17:44:30 marvel
[info]  2026-10-26 17:44:30 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb alzheimers_dementia: 198 rows -> 0 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb vascular_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:30 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:30 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 5 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 10 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 188 rows -> 0 variant rows, 12 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 198 rows -> 0 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 2 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 196 rows -> 0 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 2 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 196 rows -> 0 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 198 rows -> 0 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 5 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 10 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 188 rows -> 0 variant rows, 12 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:31 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 198 rows -> 0 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 2 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 196 rows -> 0 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 1 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 98 rows -> 0 variant rows, 10 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 176 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 4 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 212 rows -> 0 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apoa: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apob: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb tg: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 87 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 174 rows -> 0 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 81 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 3 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 87 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:32 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 4 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 212 rows -> 0 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 97 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 97 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 194 rows -> 0 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 194 rows -> 0 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 97 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 4 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 212 rows -> 0 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apoa: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apob: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb tg: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 87 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 174 rows -> 0 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 81 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 18 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 3 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 87 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 10 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 206 rows -> 0 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 11 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 97 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 97 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:33 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 106 rows -> 0 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 194 rows -> 0 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apoa: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apob: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb tg: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 194 rows -> 0 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 5 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 103 rows -> 0 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 11 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 97 rows -> 0 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 108 rows -> 0 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 97 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 4 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 194 rows -> 0 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 2 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 97 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apoa: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apob: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb tg: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 10 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 188 rows -> 0 variant rows, 12 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 6 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 6 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apoa: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apob: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb tg: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apoa: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb apob: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb tg: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:34 marvel ukb all_cause_dementia: 1 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 89 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 20 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 160 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 4 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 4 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apoa: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apob: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb tg: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 18 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 144 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apoa: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apob: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb tg: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 2 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 97 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 4 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 194 rows -> 0 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 5 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 5 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 99 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apoa: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apob: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb tg: 59 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 10 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 188 rows -> 0 variant rows, 12 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 6 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 6 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 88 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 5 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 94 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 88 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apoa: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apob: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb tg: 83 rows -> 0 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apoa: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apob: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb tg: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 1 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 89 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 20 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 160 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 4 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 4 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 9 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apoa: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:35 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:35 marvel ukb apob: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb tg: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 36 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 18 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 18 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 18 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 rows -> 0 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:36 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:36 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 18 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 144 rows -> 0 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 3 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 180 rows -> 0 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 3 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 87 rows -> 0 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:37 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 180 rows -> 0 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 4 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 10 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 174 rows -> 0 variant rows, 14 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 87 rows -> 0 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 10 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 2 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 178 rows -> 0 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 4 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 87 rows -> 0 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 174 rows -> 0 variant rows, 14 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 1 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 10 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 180 rows -> 0 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 4 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apoa: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb apob: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb tg: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 18 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 9 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:38 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 1 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 89 rows -> 0 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 8 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 172 rows -> 0 variant rows, 12 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 4 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 10 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 80 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 2 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 178 rows -> 0 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 87 rows -> 0 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 4 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apoa: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apob: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb tg: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb tg: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 4 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 86 rows -> 0 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 8 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 172 rows -> 0 variant rows, 12 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 160 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 10 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 80 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 10 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 80 rows -> 0 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 90 rows -> 0 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 80 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apoa: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apob: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb hdl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ldl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb tg: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb tg: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb tg: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb all_cause_dementia: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 54 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 108 rows -> 0 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb alzheimers_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 51 rows -> 0 variant rows, 3 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb vascular_dementia: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 6 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 48 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb frontotemporal_dementia: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb ascvd: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:39 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:39 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 18 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 144 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 162 rows -> 0 variant rows, 18 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apoa: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apob: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 54 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 108 rows -> 0 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 96 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 51 rows -> 0 variant rows, 3 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 6 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 48 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 27 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 54 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 48 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:40 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:40 marvel ukb alzheimers_dementia: 6 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb alzheimers_dementia: 156 rows -> 0 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb vascular_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb vascular_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb apoa: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb apoa: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb apob: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb apob: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb hdl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb hdl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb ldl_c: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb ldl_c: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb tg: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb tg: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb all_cause_dementia: 3 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb all_cause_dementia: 78 rows -> 0 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb all_cause_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb alzheimers_dementia: 18 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb alzheimers_dementia: 144 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb alzheimers_dementia: 144 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb vascular_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb vascular_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb vascular_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb frontotemporal_dementia: 9 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb frontotemporal_dementia: 72 rows -> 0 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb frontotemporal_dementia: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-26 17:44:41 marvel ukb ascvd: 81 rows -> 0 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-26 17:44:41 marvel ukb ascvd: 72 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-10-26 17:44:41 fetch_curated
[info]  2026-10-26 17:46:11 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1
[info]  2026-10-26 17:46:13 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-26 17:46:17 MONDO_0013792 (exact): 42 fetched; in region: none
[info]  2026-10-26 17:46:22 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-26 17:46:58 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-26 17:47:26 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6
[info]  2026-10-26 17:47:29 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-26 17:47:37 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-26 18:03:06 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3
[info]  2026-10-26 18:03:18 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-26 18:03:19 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-26 18:03:20 EFO_0009493 (exact): 3 fetched; in region: none
[warn]  2026-10-26 18:18:43 GWAS Catalog associations MONDO_0004975: ConnectionError, retry 1/3 in 30s
[info]  2026-10-26 18:29:13 MONDO_0004975 (with child traits): 7102 fetched; in region: APOB=1
[info]  2026-10-26 18:29:24 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-26 18:29:28 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-26 18:29:31 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-26 18:29:32 EFO ids with 0 curated associations: 4
[stage] 2026-10-26 18:29:32 gene_burden
[info]  2026-10-26 18:29:32 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-26 18:29:33 curated MAF: numeric=58 not_reported=28
[info]  2026-10-26 18:29:33 curated: 54 rows dropped from studies excluded for cohort overlap
[info]  2026-10-26 18:29:33 gene-burden rows: none (8 genes with 0)
[info]  2026-10-26 18:29:36 ancestry: 0 rows of studies not in the discovery log labelled NR
[info]  2026-10-26 18:29:36 ancestry: curated EAS=21
[info]  2026-10-26 18:29:36 ancestry: curated EUR=26
[info]  2026-10-26 18:29:36 ancestry: curated MULTI=21
[info]  2026-10-26 18:29:36 ancestry: curated NR=18
[info]  2026-10-26 18:29:36 ancestry: gene-burden EUR=2661
[info]  2026-10-26 18:29:36 ancestry: gene-burden MULTI=2718
[info]  2026-10-26 18:29:36 ancestry: summary-stats AFR=159854
[info]  2026-10-26 18:29:36 ancestry: summary-stats AMR=73617
[info]  2026-10-26 18:29:36 ancestry: summary-stats CSA=43677
[info]  2026-10-26 18:29:36 ancestry: summary-stats EAS=45135
[info]  2026-10-26 18:29:36 ancestry: summary-stats EUR=137357
[info]  2026-10-26 18:29:36 ancestry: summary-stats MULTI=127489
[info]  2026-10-26 18:29:36 ancestry: summary-stats NR=5898
[stage] 2026-10-26 18:29:37 effect_scale
[info]  2026-10-26 18:29:38 wrote 215 studies to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-26 18:29:39 study effect scale: linear=52, log_or=111, unknown=52
[stage] 2026-10-26 18:29:39 normalise
[info]  2026-10-26 18:29:40 normalisation: summary-stats rows unchanged=549763 no_sequence=40564 ref_mismatch=2699 normalised=1
[info]  2026-10-26 18:29:40 normalisation: curated rows effect_only=86
[stage] 2026-10-26 18:29:40 ensembl_check
[info]  2026-10-26 18:29:40 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:40 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:41 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:41 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:41 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:41 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:42 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:42 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-26 18:29:44 Ensembl check: 20584 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-26 18:29:45 summary-stats rows: alleles match=451797 flipped=135502 mismatch=3024 not_found=2236 strand_flip=468; rsid same=521285 rsid_only=41315 no_source_rsid=25159 different=3032
[info]  2026-10-26 18:29:45 curated rows: alleles match=33 flipped=28 effect_unknown=25; rsid same=86
[info]  2026-10-26 18:29:47 duplicate variants flagged: 766 rows
[stage] 2026-10-26 18:29:47 write
[info]  2026-10-26 18:30:39 wrote 598492 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-26 18:30:40
- commit: `7a3cab3` (dirty)

Output:
```text
[info]  2026-10-26 17:44:19 using root directory: /home/mvanvugt/projects/lipid_adem

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
- last run: 2026-10-26 12:39:42
- commit: `8a9b6e7`

Output:
```text
[stage] 2026-10-26 12:39:08 load_variant_lists
[info]  2026-10-26 12:39:08 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/lipid_variants.tsv: 882 rows
[info]  2026-10-26 12:39:08 0 duplicate rows removed
[info]  2026-10-26 12:39:08 ANGPTL3 ClinVar: 12 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 ANGPTL3 PTV: 56 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 APOA1 ClinVar: 33 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 APOA1 PTV: 15 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 APOB ClinVar: 236 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 APOB PTV: 172 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 APOE ClinVar: 20 rows, 0 without alleles, 20 outside gene region
[info]  2026-10-26 12:39:08 CETP ClinVar: 10 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 CETP PTV: 58 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 HMGCR ClinVar: 7 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 HMGCR PTV: 39 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 NPC1L1 PTV: 96 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 PCSK9 ClinVar: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 PCSK9 PTV: 68 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 PPARA PTV: 23 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-26 12:39:08 normalisation: variant-list rows unchanged=862 no_sequence=20
[stage] 2026-10-26 12:39:08 load_gwas
[info]  2026-10-26 12:39:38 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz: 594167 rows, 593113 variant-level (summary-stats, curated)
[info]  2026-10-26 12:39:38 wrote 1054 marvel gene-burden rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_burden.tsv.gz
[info]  2026-10-26 12:39:40 curated: 25 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-26 12:39:41 match
[info]  2026-10-26 12:39:41 ANGPTL3 ClinVar: 12 variants, 3 matched, GWAS rows: summary-stats=71
[info]  2026-10-26 12:39:41 ANGPTL3 PTV: 56 variants, 3 matched, GWAS rows: summary-stats=71
[info]  2026-10-26 12:39:41 APOA1 ClinVar: 33 variants, 0 matched, GWAS rows: none
[info]  2026-10-26 12:39:41 APOA1 PTV: 15 variants, 0 matched, GWAS rows: none
[info]  2026-10-26 12:39:42 APOB ClinVar: 236 variants, 3 matched, GWAS rows: summary-stats=137
[info]  2026-10-26 12:39:42 APOB PTV: 172 variants, 0 matched, GWAS rows: none
[info]  2026-10-26 12:39:42 APOE ClinVar: 20 variants, 1 matched, GWAS rows: summary-stats=16
[info]  2026-10-26 12:39:42 CETP ClinVar: 10 variants, 2 matched, GWAS rows: summary-stats=47
[info]  2026-10-26 12:39:42 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=205
[info]  2026-10-26 12:39:42 CETP PTV: 58 variants, 6 matched, GWAS rows: summary-stats=120
[info]  2026-10-26 12:39:42 HMGCR ClinVar: 7 variants, 0 matched, GWAS rows: none
[info]  2026-10-26 12:39:42 HMGCR PTV: 39 variants, 0 matched, GWAS rows: none
[info]  2026-10-26 12:39:42 NPC1L1 PTV: 96 variants, 6 matched, GWAS rows: summary-stats=107
[info]  2026-10-26 12:39:42 PCSK9 ClinVar: 18 variants, 1 matched, GWAS rows: summary-stats=64
[info]  2026-10-26 12:39:42 PCSK9 GoF: 18 variants, 6 matched, GWAS rows: summary-stats=410
[info]  2026-10-26 12:39:42 PCSK9 PTV: 68 variants, 3 matched, GWAS rows: summary-stats=141
[info]  2026-10-26 12:39:42 PPARA PTV: 23 variants, 0 matched, GWAS rows: none
[info]  2026-10-26 12:39:42 a1 vs Ensembl ref: 1163 matched SNV rows checked, 0 where a1 is not the Ensembl ref
[stage] 2026-10-26 12:39:42 write
[info]  2026-10-26 12:39:42 wrote 1389 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_variants.tsv.gz

```

## [50] annotate_variants (`/Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/src/annotate_variants.py`)
- first run: 2026-10-06 17:13:43
- last run: 2026-10-16 13:14:40
- commit: `c91df4d` (dirty)

Output:
```text
[info]  2026-10-16 13:14:39 Reading ClinVar variants from /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
[info]  2026-10-16 13:14:39 Read 313818 rows
[info]  2026-10-16 13:14:39 9922 rows have an aggregate P/LP ac_classification; 3 of them without an assembly dropped
[info]  2026-10-16 13:14:39 Kept 9919 rows after filtering
[info]  2026-10-16 13:14:39 Review-status scope-reduction summary:
                                                                                                                         scope  n_unique_variants  n_variants_removed_cumulative  n_variants_removed_this_step
                                                                                     All review statuses (every tier included)                549                              0                             0
Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts + criteria provided, single submitter                482                             67                            67
                                      Include: reviewed by expert panel + criteria provided, multiple submitters, no conflicts                249                            300                           233
                                                                                             Include: reviewed by expert panel                218                            331                            31
[info]  2026-10-16 13:14:39 Wrote review-status summary to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/pah_variants_review_status_summary.tsv
[info]  2026-10-16 13:14:39 Widened 3648 assembly-duplicated rows into 1900 variant/condition rows
[info]  2026-10-16 13:14:39 549 unique variants identified
[info]  2026-10-16 13:14:39 Writing 1900 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/processed/plp_variants.tsv

```

## [50] marvel_assoc_job
- first run: 2026-10-07 13:49:03
- last run: 2026-10-26 17:41:17
- commit: `7a3cab3` (dirty)

Output:
```text
[info]  2026-10-26 17:13:21 task 2: rows 2-2
[info]  2026-10-26 17:41:16 CETP: results in /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur

```

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --ancestry MULTI --studies marvel_ukb_MULTI_all_cause_dementia marvel_ukb_MULTI_all_cause_dementia_e44 marvel_ukb_MULTI_all_cause_dementia_e43 marvel_ukb_MULTI_all_cause_dementia_e33 marvel_ukb_MULTI_all_cause_dementia_e22_e32 marvel_ukb_MULTI_alzheimers_dementia marvel_ukb_MULTI_alzheimers_dementia_e44 marvel_ukb_MULTI_alzheimers_dementia_e43 marvel_ukb_MULTI_alzheimers_dementia_e33 marvel_ukb_MULTI_alzheimers_dementia_e22_e32 marvel_ukb_MULTI_vascular_dementia marvel_ukb_MULTI_vascular_dementia_e44 marvel_ukb_MULTI_vascular_dementia_e43 marvel_ukb_MULTI_vascular_dementia_e33 marvel_ukb_MULTI_vascular_dementia_e22_e32 marvel_ukb_MULTI_frontotemporal_dementia marvel_ukb_MULTI_frontotemporal_dementia_e44 marvel_ukb_MULTI_frontotemporal_dementia_e43 marvel_ukb_MULTI_frontotemporal_dementia_e33 marvel_ukb_MULTI_frontotemporal_dementia_e22_e32 --region-rare --stratified --label ukb_dementia_region_rare`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-26 12:50:20
- commit: `8a9b6e7`

Output:
```text
[info]  2026-10-26 12:47:55 ancestry MULTI, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-26 12:47:55 load_matched
[info]  2026-10-26 12:48:09 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz: 347357 rows, 10047 variants
[info]  2026-10-26 12:48:09 20375 rows of excluded gene(s) APOE dropped
[info]  2026-10-26 12:48:11 326982 of 326982 rows kept (MULTI pools every ancestry) (all: AFR=87047, AMR=42782, CSA=36051, EAS=10748, EUR=81062, MULTI=69061, NR=231)
[info]  2026-10-26 12:48:11 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32: 15631 of 326982 rows kept
[info]  2026-10-26 12:48:11 MULTI: 15631 rows pooled across ancestries (MULTI=15631), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
[stage] 2026-10-26 12:48:11 effect_scale
[stage] 2026-10-26 12:48:11 prepare_effects
[info]  2026-10-26 12:48:11 15631 usable rows, 0 with SE derived from p
[stage] 2026-10-26 12:48:11 resolve_ambiguous
[stage] 2026-10-26 12:48:11 orient
[info]  2026-10-26 12:48:11 1821 variants oriented as a2
[stage] 2026-10-26 12:48:11 apoe_strata
[info]  2026-10-26 12:48:11 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/apoe_strata.tsv: 104 studies with an APOE stratum entry
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_all_cause_dementia, stratum e33: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_all_cause_dementia, stratum e43: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_all_cause_dementia, stratum e44: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_vascular_dementia, stratum all: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_vascular_dementia, stratum e33: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_vascular_dementia, stratum e43: 1 studies
[info]  2026-10-26 12:48:11 study group marvel_ukb_MULTI_vascular_dementia, stratum e44: 1 studies
[stage] 2026-10-26 12:48:11 pooled_run
[info]  2026-10-26 12:48:11 pooled run, study group marvel_ukb_MULTI_all_cause_dementia: unstratified run, strata left out
[info]  2026-10-26 12:48:11 pooled run, study group marvel_ukb_MULTI_alzheimers_dementia: unstratified run, strata left out
[info]  2026-10-26 12:48:11 pooled run, study group marvel_ukb_MULTI_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-10-26 12:48:11 pooled run, study group marvel_ukb_MULTI_vascular_dementia: unstratified run, strata left out
[stage] 2026-10-26 12:48:11 dedupe
[info]  2026-10-26 12:48:11 0 duplicate rows removed
[info]  2026-10-26 12:48:11 0 estimates removed as copies of another study
[stage] 2026-10-26 12:48:11 meta_analyse
[info]  2026-10-26 12:48:40 6877 groups, 0 pooling more than one estimate
[info]  2026-10-26 12:49:09 6877 groups, 0 pooling more than one estimate
[stage] 2026-10-26 12:49:09 gene_burden
[info]  2026-10-26 12:49:09 gene burden: 24 pooled and 24 per-study rows
[stage] 2026-10-26 12:49:09 write
[info]  2026-10-26 12:49:10 wrote 13754 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare.tsv.gz
[info]  2026-10-26 12:49:10 wrote 48 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare.tsv.gz
[stage] 2026-10-26 12:49:10 apoe_strata_run
[info]  2026-10-26 12:49:10 8754 rows from APOE strata: pooled per stratum
[stage] 2026-10-26 12:49:10 dedupe
[info]  2026-10-26 12:49:10 0 duplicate rows removed
[info]  2026-10-26 12:49:10 0 estimates removed as copies of another study
[stage] 2026-10-26 12:49:10 meta_analyse
[info]  2026-10-26 12:49:44 8754 groups, 0 pooling more than one estimate
[info]  2026-10-26 12:50:19 8754 groups, 0 pooling more than one estimate
[stage] 2026-10-26 12:50:19 gene_burden
[info]  2026-10-26 12:50:19 gene burden: 96 pooled and 96 per-study rows
[stage] 2026-10-26 12:50:19 write
[info]  2026-10-26 12:50:20 wrote 17508 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare_apoe_strata.tsv.gz
[info]  2026-10-26 12:50:20 wrote 192 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare_apoe_strata.tsv.gz

```

## [51] annotate_ptv (`/home/mvanvugt/projects/lipid_adem/src/annotate_ptv.py`)
- first run: 2026-10-21 13:16:22
- last run: 2026-10-21 13:16:22
- commit: `e9443d3` (dirty)

Output:
```text
[info]  2026-10-21 13:16:21 Reading VEP consequences from /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/vep_lipid_gene_csq.tsv.gz
[info]  2026-10-21 13:16:22 Read 79163 variant x transcript rows
[info]  2026-10-21 13:16:22 CETP: 1595 sites, 58 LoF=HC on the canonical transcript kept, 1537 dropped
[info]  2026-10-21 13:16:22 HMGCR: 1554 sites, 39 LoF=HC on the canonical transcript kept, 1515 dropped
[info]  2026-10-21 13:16:22 NPC1L1: 2757 sites, 96 LoF=HC on the canonical transcript kept, 2661 dropped
[info]  2026-10-21 13:16:22 PCSK9: 1651 sites, 68 LoF=HC on the canonical transcript kept, 1583 dropped
[info]  2026-10-21 13:16:22 ANGPTL3: 802 sites, 56 LoF=HC on the canonical transcript kept, 746 dropped
[info]  2026-10-21 13:16:22 PPARA: 772 sites, 23 LoF=HC on the canonical transcript kept, 749 dropped
[info]  2026-10-21 13:16:22 APOA1: 561 sites, 15 LoF=HC on the canonical transcript kept, 546 dropped
[info]  2026-10-21 13:16:22 APOB: 6376 sites, 172 LoF=HC on the canonical transcript kept, 6204 dropped
[info]  2026-10-21 13:16:22 Wrote 527 PTVs to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/ptv_variants.tsv.gz

```

## [55] combine_variants (`/home/rmgpmva/projects/lipid_adem/src/combine_variants.py`)
- first run: 2026-10-21 13:50:41
- last run: 2026-10-24 10:19:52
- commit: `04d2c6c`

Output:
```text
[info]  2026-10-24 10:19:52 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/ptv_variants.tsv.gz: 527 PTVs
[info]  2026-10-24 10:19:52 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/plp_variants.tsv: 1900 rows; /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-10-24 10:19:52 0 P/LP rows with ref = alt dropped
[warn]  2026-10-24 10:19:52 APOE condition 'Alzheimer disease 3, protection against, due to APOE3-Christchurch' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 APOA1 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 ANGPTL3 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 PPARA condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 PCSK9 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 HMGCR condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 NPC1L1 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 CETP condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 APOB condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-24 10:19:52 APOE condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[info]  2026-10-24 10:19:52 262 truncating P/LP variants set to lowering, 213 of them against their conditions
[info]  2026-10-24 10:19:52 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-10-24 10:19:52 ANGPTL3 ClinVar P/LP: 2 variants unknown
[info]  2026-10-24 10:19:52 APOA1 ClinVar P/LP: 11 variants altered
[info]  2026-10-24 10:19:52 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-10-24 10:19:52 APOA1 ClinVar P/LP: 16 variants lowering
[info]  2026-10-24 10:19:52 APOA1 ClinVar P/LP: 6 variants unknown
[info]  2026-10-24 10:19:52 APOB ClinVar P/LP: 5 variants altered
[info]  2026-10-24 10:19:52 APOB ClinVar P/LP: 6 variants conflicting
[info]  2026-10-24 10:19:52 APOB ClinVar P/LP: 224 variants lowering
[info]  2026-10-24 10:19:52 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-10-24 10:19:52 APOE ClinVar P/LP: 12 variants altered
[info]  2026-10-24 10:19:52 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-10-24 10:19:52 APOE ClinVar P/LP: 6 variants unknown
[info]  2026-10-24 10:19:52 CETP ClinVar P/LP: 10 variants lowering
[info]  2026-10-24 10:19:52 CETP ClinVar P/LP: 2 variants unknown
[info]  2026-10-24 10:19:52 HMGCR ClinVar P/LP: 6 variants lowering
[info]  2026-10-24 10:19:52 HMGCR ClinVar P/LP: 3 variants unknown
[info]  2026-10-24 10:19:52 NPC1L1 ClinVar P/LP: 2 variants unknown
[info]  2026-10-24 10:19:52 PCSK9 ClinVar P/LP: 2 variants lowering
[info]  2026-10-24 10:19:52 PCSK9 ClinVar P/LP: 16 variants raising
[info]  2026-10-24 10:19:52 PCSK9 ClinVar P/LP: 2 variants unknown
[info]  2026-10-24 10:19:52 PPARA ClinVar P/LP: 2 variants unknown
[info]  2026-10-24 10:19:52 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/gof_variants.tsv: 47 GoF variants
[warn]  2026-10-24 10:19:52 ANGPTL3 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 APOA1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 APOB ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 APOE ClinVar: 1 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 CETP ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 HMGCR ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 NPC1L1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 PCSK9 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-24 10:19:52 PPARA ClinVar: 2 rows without GRCh38 chr/pos/alleles
[info]  2026-10-24 10:19:52 normalisation ClinVar: no_sequence=20
[info]  2026-10-24 10:19:52 normalisation ClinVar: unchanged=316
[info]  2026-10-24 10:19:52 normalisation GoF: unchanged=19
[info]  2026-10-24 10:19:52 normalisation PTV: normalised=18
[info]  2026-10-24 10:19:52 normalisation PTV: unchanged=509
[info]  2026-10-24 10:19:52 62 sites are in several sources
[info]  2026-10-24 10:19:52 ANGPTL3 ClinVar: 12 variants
[info]  2026-10-24 10:19:52 ANGPTL3 PTV: 56 variants
[info]  2026-10-24 10:19:52 APOA1 ClinVar: 33 variants
[info]  2026-10-24 10:19:52 APOA1 PTV: 15 variants
[info]  2026-10-24 10:19:52 APOB ClinVar: 236 variants
[info]  2026-10-24 10:19:52 APOB PTV: 172 variants
[info]  2026-10-24 10:19:52 APOE ClinVar: 20 variants
[info]  2026-10-24 10:19:52 CETP ClinVar: 10 variants
[info]  2026-10-24 10:19:52 CETP GoF: 1 variants
[info]  2026-10-24 10:19:52 CETP PTV: 58 variants
[info]  2026-10-24 10:19:52 HMGCR ClinVar: 7 variants
[info]  2026-10-24 10:19:52 HMGCR PTV: 39 variants
[info]  2026-10-24 10:19:52 NPC1L1 PTV: 96 variants
[info]  2026-10-24 10:19:52 PCSK9 ClinVar: 18 variants
[info]  2026-10-24 10:19:52 PCSK9 GoF: 18 variants
[info]  2026-10-24 10:19:52 PCSK9 PTV: 68 variants
[info]  2026-10-24 10:19:52 PPARA PTV: 23 variants
[info]  2026-10-24 10:19:52 Wrote 882 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-10-24 10:19:52 marvel lists: 820 sites, 17 with an extra original-form row
[info]  2026-10-24 10:19:52 Wrote 64 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 46 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOA1_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 373 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOB_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 20 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOE_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 67 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/CETP_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 45 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 99 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 99 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[info]  2026-10-24 10:19:52 Wrote 24 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/PPARA_variants.tsv

```
