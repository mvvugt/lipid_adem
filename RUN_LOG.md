## [5] apoe_exposure (`/home/mvanvugt/projects/lipid_adem/src/apoe_exposure.py`)
- first run: 2026-10-09 09:54:04
- last run: 2026-10-27 00:20:43
- commit: `244d529` (dirty)

Output:
```text
[stage] 2026-10-27 00:20:37 read
[info]  2026-10-27 00:20:39 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipids_full_pheno.tsv.gz: 469587 participants; genotype: e3e3=276035, e3e4=110438, e2e3=57188, e2e4=11672, e4e4=11202, e2e2=3025, Unknown=27
[stage] 2026-10-27 00:20:39 indicators
[warn]  2026-10-27 00:20:39 27 participants without a genotype left out
[info]  2026-10-27 00:20:40 APOE_e2e2: 3025 carriers vs 466535 others
[info]  2026-10-27 00:20:40 APOE_e2e3: 57188 carriers vs 412372 others
[info]  2026-10-27 00:20:40 APOE_e2e4: 11672 carriers vs 457888 others
[info]  2026-10-27 00:20:40 APOE_e3e3: 276035 carriers vs 193525 others
[info]  2026-10-27 00:20:40 APOE_e3e4: 110438 carriers vs 359122 others
[info]  2026-10-27 00:20:40 APOE_e4e4: 11202 carriers vs 458358 others
[stage] 2026-10-27 00:20:40 write
[info]  2026-10-27 00:20:43 wrote 469560 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/apoe_diplotype.tsv.gz

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
- last run: 2026-11-03 16:50:41
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:50:14 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:50:14 stage: extract
[info]  2026-11-03 16:50:14 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:50:14 node: tcn67.local.snellius.surf.nl, job id: 28876273, task: 1
[info]  2026-11-03 16:50:14 task 1: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr1.vcf.gz
[info]  2026-11-03 16:50:41 extract vep_chr1.vcf.gz: finished

```

## [10] slurm_script_extract_task2
- first run: 2026-10-22 03:17:58
- last run: 2026-11-03 16:49:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:49:11 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:49:11 stage: extract
[info]  2026-11-03 16:49:11 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:49:11 node: tcn46.local.snellius.surf.nl, job id: 28876274, task: 2
[info]  2026-11-03 16:49:11 task 2: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr11.vcf.gz
[info]  2026-11-03 16:49:19 extract vep_chr11.vcf.gz: finished

```

## [10] slurm_script_extract_task3
- first run: 2026-10-22 03:17:57
- last run: 2026-11-03 16:54:25
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:54:08 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:54:08 stage: extract
[info]  2026-11-03 16:54:08 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:54:08 node: tcn46.local.snellius.surf.nl, job id: 28876275, task: 3
[info]  2026-11-03 16:54:08 task 3: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr2.vcf.gz
[info]  2026-11-03 16:54:24 extract vep_chr2.vcf.gz: finished

```

## [10] slurm_script_extract_task4
- first run: 2026-10-22 03:37:57
- last run: 2026-11-03 16:49:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:49:11 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:49:11 stage: extract
[info]  2026-11-03 16:49:11 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:49:11 node: tcn65.local.snellius.surf.nl, job id: 28876276, task: 4
[info]  2026-11-03 16:49:11 task 4: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr19.vcf.gz
[info]  2026-11-03 16:49:19 extract vep_chr19.vcf.gz: finished

```

## [10] slurm_script_extract_task5
- first run: 2026-10-22 03:18:01
- last run: 2026-11-03 16:50:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:49:57 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:49:57 stage: extract
[info]  2026-11-03 16:49:57 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:49:57 node: tcn64.local.snellius.surf.nl, job id: 28876277, task: 5
[info]  2026-11-03 16:49:57 task 5: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr16.vcf.gz
[info]  2026-11-03 16:50:07 extract vep_chr16.vcf.gz: finished

```

## [10] slurm_script_extract_task6
- first run: 2026-10-22 03:17:58
- last run: 2026-11-03 16:50:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:49:57 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:49:57 stage: extract
[info]  2026-11-03 16:49:57 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:49:57 node: tcn64.local.snellius.surf.nl, job id: 28876278, task: 6
[info]  2026-11-03 16:49:57 task 6: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr5.vcf.gz
[info]  2026-11-03 16:50:07 extract vep_chr5.vcf.gz: finished

```

## [10] slurm_script_extract_task7
- first run: 2026-10-22 04:30:10
- last run: 2026-11-03 16:50:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:50:11 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:50:11 stage: extract
[info]  2026-11-03 16:50:11 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:50:11 node: tcn100.local.snellius.surf.nl, job id: 28876279, task: 7
[info]  2026-11-03 16:50:11 task 7: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr7.vcf.gz
[info]  2026-11-03 16:50:19 extract vep_chr7.vcf.gz: finished

```

## [10] slurm_script_extract_task8
- first run: 2026-10-22 04:30:44
- last run: 2026-11-03 16:49:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:49:11 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml
[info]  2026-11-03 16:49:11 stage: extract
[info]  2026-11-03 16:49:11 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:49:11 node: tcn100.local.snellius.surf.nl, job id: 28876271, task: 8
[info]  2026-11-03 16:49:11 task 8: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr22.vcf.gz
[info]  2026-11-03 16:49:19 extract vep_chr22.vcf.gz: finished

```

## [10] slurm_script_f1a3a8a_bin_vs_ref_CETP_compare
- first run: 2026-11-03 19:29:01
- last run: 2026-11-03 19:29:01
- commit: `23ebede` (dirty)
- status: failed

Output:
```text
[error] 2026-11-03 19:28:59 -s/--step must look like step4 or step2_CETP, not 'f1a3a8a_bin_vs_ref_CETP'
--- error output (raw) ---


```

## [10] slurm_script_final_task1
- first run: 2026-10-22 04:37:33
- last run: 2026-11-03 19:16:57
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 18:54:25 config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden_masks.toml
[info]  2026-11-03 18:54:25 stage: final
[info]  2026-11-03 18:54:25 output directory: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 18:54:25 node: tcn114.local.snellius.surf.nl, job id: 28879510, task: 1
[info]  2026-11-03 18:58:54 aggregate: finished
[info]  2026-11-03 19:16:57 associate: finished

```

## [10] slurm_script_step10_bin_vs_8a_CETP_compare
- first run: 2026-11-02 23:33:41
- last run: 2026-11-02 23:37:13
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 23:37:06 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_bin_vs_8a_CETP; mode: compare; env: prot_misc
[info]  2026-11-02 23:37:06 working directory (temporary): /scratch-local/mvanvugt.28852480/tmp.C0ICJuGnJt/task_1
[warn]  2026-11-02 23:37:06 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 23:37:06 manifest: 3 file(s) in /scratch-local/mvanvugt.28852480/tmp.C0ICJuGnJt/task_1/step10_bin_vs_8a_CETP.compare.md5
[info]  2026-11-02 23:37:13 step10_bin_vs_8a_CETP: GATE PASS
[info]  2026-11-02 23:37:13 *** END ***

```

## [10] slurm_script_step10_dos_vs_bin_all7_compare
- first run: 2026-11-02 23:52:12
- last run: 2026-11-02 23:52:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 23:52:03 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_dos_vs_bin_all7; mode: compare; env: prot_misc
[info]  2026-11-02 23:52:03 working directory (temporary): /scratch-local/mvanvugt.28852813/tmp.fzvufOx8Lu/task_1
[warn]  2026-11-02 23:52:03 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 23:52:03 manifest: 3 file(s) in /scratch-local/mvanvugt.28852813/tmp.fzvufOx8Lu/task_1/step10_dos_vs_bin_all7.compare.md5
[info]  2026-11-02 23:52:11 step10_dos_vs_bin_all7: GATE PASS
[info]  2026-11-02 23:52:11 *** END ***

```

## [10] slurm_script_step10_dos_vs_bin_compare
- first run: 2026-11-02 23:35:52
- last run: 2026-11-02 23:47:08
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 23:46:59 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_dos_vs_bin; mode: compare; env: prot_misc
[info]  2026-11-02 23:46:59 working directory (temporary): /scratch-local/mvanvugt.28852693/tmp.yA4HGSqVGJ/task_1
[warn]  2026-11-02 23:46:59 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 23:46:59 manifest: 3 file(s) in /scratch-local/mvanvugt.28852693/tmp.yA4HGSqVGJ/task_1/step10_dos_vs_bin.compare.md5
[warn]  2026-11-02 23:47:08 step10_dos_vs_bin: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step10_dos_vs_bin/summary.tsv.gz
[info]  2026-11-02 23:47:08 *** END ***

```

## [10] slurm_script_step10_masks_vs_old_compare
- first run: 2026-11-02 17:29:48
- last run: 2026-11-02 17:29:48
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-02 17:29:44 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step10_masks_vs_old; mode: compare; env: prot_misc
[info]  2026-11-02 17:29:44 working directory (temporary): /scratch-local/mvanvugt.28846072/tmp.JBgzLF5xO0/task_1
[warn]  2026-11-02 17:29:44 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-02 17:29:44 manifest: 385 file(s) in /scratch-local/mvanvugt.28846072/tmp.JBgzLF5xO0/task_1/step10_masks_vs_old.compare.md5
[warn]  2026-11-02 17:29:48 step10_masks_vs_old: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step10_masks_vs_old/summary.tsv.gz
[info]  2026-11-02 17:29:48 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_bin_vs_ref_CETP_compare
- first run: 2026-11-04 09:20:16
- last run: 2026-11-04 13:28:47
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 13:28:35 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_bin_vs_ref_CETP; mode: compare; env: prot_misc
[info]  2026-11-04 13:28:36 working directory (temporary): /scratch-local/mvanvugt.28888611/tmp.JdzO2zMb9W/task_1
[warn]  2026-11-04 13:28:36 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 13:28:36 manifest: 3 file(s) in /scratch-local/mvanvugt.28888611/tmp.JdzO2zMb9W/task_1/step11_f1a3a8a_bin_vs_ref_CETP.compare.md5
[info]  2026-11-04 13:28:47 step11_f1a3a8a_bin_vs_ref_CETP: GATE PASS
[info]  2026-11-04 13:28:47 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_bin_vs_ref_PCSK9_compare
- first run: 2026-11-04 09:18:04
- last run: 2026-11-04 13:29:49
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 13:29:38 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_bin_vs_ref_PCSK9; mode: compare; env: prot_misc
[info]  2026-11-04 13:29:38 working directory (temporary): /scratch-local/mvanvugt.28888990/tmp.2fpwhCFhuy/task_1
[warn]  2026-11-04 13:29:38 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 13:29:38 manifest: 3 file(s) in /scratch-local/mvanvugt.28888990/tmp.2fpwhCFhuy/task_1/step11_f1a3a8a_bin_vs_ref_PCSK9.compare.md5
[info]  2026-11-04 13:29:48 step11_f1a3a8a_bin_vs_ref_PCSK9: GATE PASS
[info]  2026-11-04 13:29:48 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_masks_vs_ref_compare
- first run: 2026-11-04 10:37:30
- last run: 2026-11-04 10:37:30
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 10:37:25 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_masks_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 10:37:25 working directory (temporary): /scratch-local/mvanvugt.28889039/tmp.ibpyWVtBz4/task_1
[warn]  2026-11-04 10:37:25 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 10:37:25 manifest: 2 file(s) in /scratch-local/mvanvugt.28889039/tmp.ibpyWVtBz4/task_1/step11_f1a3a8a_burden_masks_vs_ref.compare.md5
[info]  2026-11-04 10:37:30 step11_f1a3a8a_burden_masks_vs_ref: GATE PASS
[info]  2026-11-04 10:37:30 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_nj1_compare
- first run: 2026-11-04 12:23:05
- last run: 2026-11-04 12:23:05
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 12:23:01 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_nj1; mode: compare; env: prot_misc
[info]  2026-11-04 12:23:01 working directory (temporary): /scratch-local/mvanvugt.28891395/tmp.TOSLlCNFIS/task_1
[warn]  2026-11-04 12:23:01 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 12:23:01 manifest: 2 file(s) in /scratch-local/mvanvugt.28891395/tmp.TOSLlCNFIS/task_1/step11_f1a3a8a_burden_nj1.compare.md5
[info]  2026-11-04 12:23:05 step11_f1a3a8a_burden_nj1: GATE PASS
[info]  2026-11-04 12:23:05 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_nj8_compare
- first run: 2026-11-04 12:23:34
- last run: 2026-11-04 12:23:34
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 12:23:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_nj8; mode: compare; env: prot_misc
[info]  2026-11-04 12:23:32 working directory (temporary): /scratch-local/mvanvugt.28891396/tmp.IPeEJ0KWm5/task_1
[warn]  2026-11-04 12:23:32 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 12:23:32 manifest: 2 file(s) in /scratch-local/mvanvugt.28891396/tmp.IPeEJ0KWm5/task_1/step11_f1a3a8a_burden_nj8.compare.md5
[info]  2026-11-04 12:23:34 step11_f1a3a8a_burden_nj8: GATE PASS
[info]  2026-11-04 12:23:34 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_burden_vs_ref_compare
- first run: 2026-11-04 10:39:22
- last run: 2026-11-04 13:30:40
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 13:30:37 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_burden_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 13:30:37 working directory (temporary): /scratch-local/mvanvugt.28889069/tmp.63kM3aQxCF/task_1
[warn]  2026-11-04 13:30:37 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 13:30:37 manifest: 2 file(s) in /scratch-local/mvanvugt.28889069/tmp.63kM3aQxCF/task_1/step11_f1a3a8a_burden_vs_ref.compare.md5
[warn]  2026-11-04 13:30:39 step11_f1a3a8a_burden_vs_ref: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step11_f1a3a8a_burden_vs_ref/summary.tsv.gz
[info]  2026-11-04 13:30:39 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_variant_bin_vs_ref_compare
- first run: 2026-11-04 15:31:05
- last run: 2026-11-04 15:31:05
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 15:30:49 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_variant_bin_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 15:30:49 working directory (temporary): /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1
[warn]  2026-11-04 15:30:49 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 15:30:49 manifest: 2 file(s) in /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1/step11_f1a3a8a_variant_bin_vs_ref.compare.md5
[info]  2026-11-04 15:31:05 step11_f1a3a8a_variant_bin_vs_ref: GATE PASS
[info]  2026-11-04 15:31:05 *** END ***

```

## [10] slurm_script_step11_f1a3a8a_variant_dos_vs_ref_compare
- first run: 2026-11-04 10:38:36
- last run: 2026-11-04 10:38:36
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 10:38:27 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step11_f1a3a8a_variant_dos_vs_ref; mode: compare; env: prot_misc
[info]  2026-11-04 10:38:27 working directory (temporary): /scratch-local/mvanvugt.28889040/tmp.UKk0WqQYUd/task_1
[warn]  2026-11-04 10:38:27 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-11-04 10:38:27 manifest: 2 file(s) in /scratch-local/mvanvugt.28889040/tmp.UKk0WqQYUd/task_1/step11_f1a3a8a_variant_dos_vs_ref.compare.md5
[warn]  2026-11-04 10:38:36 step11_f1a3a8a_variant_dos_vs_ref: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step11_f1a3a8a_variant_dos_vs_ref/summary.tsv.gz
[info]  2026-11-04 10:38:36 *** END ***

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

## [10] slurm_script_step2b_old
- first run: 2026-10-26 23:28:20
- last run: 2026-10-26 23:28:20
- commit: `ab86ef1` (dirty)

Output:
```text
[info]  2026-10-26 19:27:52 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step2b; mode: old; env: marvel_old
[info]  2026-10-26 19:27:52 working directory (temporary): /scratch-local/mvanvugt.28602694/tmp.pVG9y9aFJh/task_1
[info]  2026-10-26 19:27:52 manifest: 8 file(s) in /scratch-local/mvanvugt.28602694/tmp.pVG9y9aFJh/task_1/step2b.old.md5
[info]  2026-10-26 23:28:20 *** END ***

```

## [10] slurm_script_step4_CETP_config
- first run: 2026-10-27 09:54:15
- last run: 2026-10-27 09:54:15
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:54:07 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_CETP; mode: config; env: marvel_old
[info]  2026-10-27 09:54:07 working directory (temporary): /scratch-local/mvanvugt.28614790/tmp.2rK6j6Kjdk/task_1
[info]  2026-10-27 09:54:07 manifest: 2 file(s) in /scratch-local/mvanvugt.28614790/tmp.2rK6j6Kjdk/task_1/step4_CETP.config.md5
[info]  2026-10-27 09:54:15 *** END ***

```

## [10] slurm_script_step4_CETP_old
- first run: 2026-10-28 02:53:35
- last run: 2026-10-28 02:53:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 10:23:47 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_CETP; mode: old; env: marvel_old
[info]  2026-10-27 10:23:47 working directory (temporary): /scratch-local/mvanvugt.28615314/tmp.RdHJ8C8uPK/task_1
[info]  2026-10-27 10:23:47 manifest: 5 file(s) in /scratch-local/mvanvugt.28615314/tmp.RdHJ8C8uPK/task_1/step4_CETP.old.md5
[info]  2026-10-28 02:53:35 *** END ***

```

## [10] slurm_script_step4_PCSK9_config
- first run: 2026-10-28 11:42:40
- last run: 2026-10-28 11:42:40
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 11:42:31 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_PCSK9; mode: config; env: marvel_old
[info]  2026-10-28 11:42:31 working directory (temporary): /scratch-local/mvanvugt.28654376/tmp.CWFWvJLLrQ/task_1
[info]  2026-10-28 11:42:31 manifest: 2 file(s) in /scratch-local/mvanvugt.28654376/tmp.CWFWvJLLrQ/task_1/step4_PCSK9.config.md5
[info]  2026-10-28 11:42:40 *** END ***

```

## [10] slurm_script_step4_PCSK9_old
- first run: 2026-10-29 17:21:35
- last run: 2026-10-29 17:21:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 11:44:19 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_PCSK9; mode: old; env: marvel_old
[info]  2026-10-28 11:44:19 working directory (temporary): /scratch-local/mvanvugt.28654523/tmp.zcsKrQKsDe/task_1
[info]  2026-10-28 11:44:19 manifest: 5 file(s) in /scratch-local/mvanvugt.28654523/tmp.zcsKrQKsDe/task_1/step4_PCSK9.old.md5
[info]  2026-10-29 17:21:35 *** END ***

```

## [10] slurm_script_step4_vs_a_CETP_compare
- first run: 2026-10-28 11:45:12
- last run: 2026-10-28 22:44:45
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 22:44:29 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_vs_a_CETP; mode: compare; env: prot_misc
[info]  2026-10-28 22:44:29 working directory (temporary): /scratch-local/mvanvugt.28683290/tmp.s1T1OXE2AF/task_1
[warn]  2026-10-28 22:44:29 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-28 22:44:31 manifest: 2190 file(s) in /scratch-local/mvanvugt.28683290/tmp.s1T1OXE2AF/task_1/step4_vs_a_CETP.compare.md5
[warn]  2026-10-28 22:44:45 step4_vs_a_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4_vs_a_CETP/summary.tsv.gz
[info]  2026-10-28 22:44:45 *** END ***

```

## [10] slurm_script_step4_vs_a_PCSK9_compare
- first run: 2026-10-28 22:44:51
- last run: 2026-10-28 22:44:51
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 22:44:29 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_vs_a_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-28 22:44:29 working directory (temporary): /scratch-local/mvanvugt.28683291/tmp.hN6teY3V8g/task_1
[warn]  2026-10-28 22:44:29 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-28 22:44:32 manifest: 3176 file(s) in /scratch-local/mvanvugt.28683291/tmp.hN6teY3V8g/task_1/step4_vs_a_PCSK9.compare.md5
[warn]  2026-10-28 22:44:51 step4_vs_a_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4_vs_a_PCSK9/summary.tsv.gz
[info]  2026-10-28 22:44:51 *** END ***

```

## [10] slurm_script_step4_vs_b_CETP_compare
- first run: 2026-10-28 09:58:18
- last run: 2026-10-28 09:58:18
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 09:58:01 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4_vs_b_CETP; mode: compare; env: prot_misc
[info]  2026-10-28 09:58:01 working directory (temporary): /scratch-local/mvanvugt.28651086/tmp.Sve3WE1lGy/task_1
[warn]  2026-10-28 09:58:01 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-28 09:58:02 manifest: 1337 file(s) in /scratch-local/mvanvugt.28651086/tmp.Sve3WE1lGy/task_1/step4_vs_b_CETP.compare.md5
[warn]  2026-10-28 09:58:18 step4_vs_b_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4_vs_b_CETP/summary.tsv.gz
[info]  2026-10-28 09:58:18 *** END ***

```

## [10] slurm_script_step4b7_CETP_config
- first run: 2026-10-28 16:34:07
- last run: 2026-10-28 16:34:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:34:00 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_CETP; mode: config; env: marvel_old
[info]  2026-10-28 16:34:00 working directory (temporary): /scratch-local/mvanvugt.28667929/tmp.Q3ws3wp1rM/task_1
[info]  2026-10-28 16:34:00 manifest: 2 file(s) in /scratch-local/mvanvugt.28667929/tmp.Q3ws3wp1rM/task_1/step4b7_CETP.config.md5
[info]  2026-10-28 16:34:07 *** END ***

```

## [10] slurm_script_step4b7_CETP_old
- first run: 2026-10-29 06:16:51
- last run: 2026-10-29 06:16:51
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:36:24 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_CETP; mode: old; env: marvel_old
[info]  2026-10-28 16:36:24 working directory (temporary): /scratch-local/mvanvugt.28668051/tmp.8e5CuQGf1L/task_1
[info]  2026-10-28 16:36:24 manifest: 5 file(s) in /scratch-local/mvanvugt.28668051/tmp.8e5CuQGf1L/task_1/step4b7_CETP.old.md5
[info]  2026-10-29 06:16:51 *** END ***

```

## [10] slurm_script_step4b7_PCSK9_config
- first run: 2026-10-28 16:34:06
- last run: 2026-10-28 16:34:06
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:33:58 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_PCSK9; mode: config; env: marvel_old
[info]  2026-10-28 16:33:58 working directory (temporary): /scratch-local/mvanvugt.28667930/tmp.K5EnrdW8LE/task_1
[info]  2026-10-28 16:33:58 manifest: 2 file(s) in /scratch-local/mvanvugt.28667930/tmp.K5EnrdW8LE/task_1/step4b7_PCSK9.config.md5
[info]  2026-10-28 16:34:06 *** END ***

```

## [10] slurm_script_step4b7_PCSK9_old
- first run: 2026-10-29 18:19:29
- last run: 2026-10-29 18:19:29
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:36:27 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_PCSK9; mode: old; env: marvel_old
[info]  2026-10-28 16:36:27 working directory (temporary): /scratch-local/mvanvugt.28668052/tmp.jfqGkzR0dz/task_1
[info]  2026-10-28 16:36:27 manifest: 5 file(s) in /scratch-local/mvanvugt.28668052/tmp.jfqGkzR0dz/task_1/step4b7_PCSK9.old.md5
[info]  2026-10-29 18:19:29 *** END ***

```

## [10] slurm_script_step4b7_vs_b_CETP_compare
- first run: 2026-10-29 21:48:47
- last run: 2026-10-29 21:48:47
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 21:48:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_vs_b_CETP; mode: compare; env: prot_misc
[info]  2026-10-29 21:48:32 working directory (temporary): /scratch-local/mvanvugt.28743058/tmp.CJeQrBbl1L/task_1
[warn]  2026-10-29 21:48:32 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-29 21:48:33 manifest: 1337 file(s) in /scratch-local/mvanvugt.28743058/tmp.CJeQrBbl1L/task_1/step4b7_vs_b_CETP.compare.md5
[warn]  2026-10-29 21:48:47 step4b7_vs_b_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4b7_vs_b_CETP/summary.tsv.gz
[info]  2026-10-29 21:48:47 *** END ***

```

## [10] slurm_script_step4b7_vs_b_PCSK9_compare
- first run: 2026-10-29 21:48:52
- last run: 2026-10-29 21:48:52
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 21:48:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4b7_vs_b_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-29 21:48:32 working directory (temporary): /scratch-local/mvanvugt.28743065/tmp.JuTg2Spfs1/task_1
[warn]  2026-10-29 21:48:32 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-29 21:48:33 manifest: 2097 file(s) in /scratch-local/mvanvugt.28743065/tmp.JuTg2Spfs1/task_1/step4b7_vs_b_PCSK9.compare.md5
[warn]  2026-10-29 21:48:52 step4b7_vs_b_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step4b7_vs_b_PCSK9/summary.tsv.gz
[info]  2026-10-29 21:48:52 *** END ***

```

## [10] slurm_script_step4na_CETP_config
- first run: 2026-10-27 09:54:15
- last run: 2026-10-27 09:54:15
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:54:07 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_CETP; mode: config; env: marvel_old
[info]  2026-10-27 09:54:07 working directory (temporary): /scratch-local/mvanvugt.28614791/tmp.NVBbAmSir7/task_1
[info]  2026-10-27 09:54:07 manifest: 2 file(s) in /scratch-local/mvanvugt.28614791/tmp.NVBbAmSir7/task_1/step4na_CETP.config.md5
[info]  2026-10-27 09:54:15 *** END ***

```

## [10] slurm_script_step4na_CETP_old
- first run: 2026-10-28 08:21:54
- last run: 2026-10-28 08:21:54
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 10:23:45 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_CETP; mode: old; env: marvel_old
[info]  2026-10-27 10:23:45 working directory (temporary): /scratch-local/mvanvugt.28615315/tmp.7uQq74sD8p/task_1
[info]  2026-10-27 10:23:45 manifest: 5 file(s) in /scratch-local/mvanvugt.28615315/tmp.7uQq74sD8p/task_1/step4na_CETP.old.md5
[info]  2026-10-28 08:21:54 *** END ***

```

## [10] slurm_script_step4na_PCSK9_config
- first run: 2026-10-27 09:54:15
- last run: 2026-10-27 09:54:15
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:54:08 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_PCSK9; mode: config; env: marvel_old
[info]  2026-10-27 09:54:08 working directory (temporary): /scratch-local/mvanvugt.28614792/tmp.sQvZBYt9HY/task_1
[info]  2026-10-27 09:54:08 manifest: 2 file(s) in /scratch-local/mvanvugt.28614792/tmp.sQvZBYt9HY/task_1/step4na_PCSK9.config.md5
[info]  2026-10-27 09:54:14 *** END ***

```

## [10] slurm_script_step4na_PCSK9_old
- first run: 2026-10-28 22:17:35
- last run: 2026-10-28 22:17:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 10:23:46 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step4na_PCSK9; mode: old; env: marvel_old
[info]  2026-10-27 10:23:46 working directory (temporary): /scratch-local/mvanvugt.28615316/tmp.S0hdwC58m6/task_1
[info]  2026-10-27 10:23:46 manifest: 5 file(s) in /scratch-local/mvanvugt.28615316/tmp.S0hdwC58m6/task_1/step4na_PCSK9.old.md5
[info]  2026-10-28 22:17:35 *** END ***

```

## [10] slurm_script_step6_CETP_new
- first run: 2026-10-30 01:56:49
- last run: 2026-10-30 01:56:49
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:17:20 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_CETP; mode: new; env: marvel_new
[info]  2026-10-29 23:17:20 working directory (temporary): /scratch-local/mvanvugt.28746645/tmp.ntDfjzeWc1/task_1
[info]  2026-10-29 23:17:21 manifest: 3 file(s) in /scratch-local/mvanvugt.28746645/tmp.ntDfjzeWc1/task_1/step6_CETP.new.md5
[info]  2026-10-30 01:56:49 step6_CETP: marvelous associate done, output to data/temp/validation/step6/CETP
[info]  2026-10-30 01:56:49 *** END ***

```

## [10] slurm_script_step6_PCSK9_new
- first run: 2026-10-30 03:31:28
- last run: 2026-10-30 03:31:28
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:17:20 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_PCSK9; mode: new; env: marvel_new
[info]  2026-10-29 23:17:20 working directory (temporary): /scratch-local/mvanvugt.28746647/tmp.laIYpkhjir/task_1
[info]  2026-10-29 23:17:20 manifest: 3 file(s) in /scratch-local/mvanvugt.28746647/tmp.laIYpkhjir/task_1/step6_PCSK9.new.md5
[info]  2026-10-30 03:31:27 step6_PCSK9: marvelous associate done, output to data/temp/validation/step6/PCSK9
[info]  2026-10-30 03:31:27 *** END ***

```

## [10] slurm_script_step6_vs_bna_CETP_compare
- first run: 2026-10-30 08:06:56
- last run: 2026-10-30 08:06:56
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 08:06:45 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_vs_bna_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 08:06:45 working directory (temporary): /scratch-local/mvanvugt.28763720/tmp.xR59DBQRrG/task_1
[warn]  2026-10-30 08:06:45 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 08:06:46 manifest: 1337 file(s) in /scratch-local/mvanvugt.28763720/tmp.xR59DBQRrG/task_1/step6_vs_bna_CETP.compare.md5
[warn]  2026-10-30 08:06:55 step6_vs_bna_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step6_vs_bna_CETP/summary.tsv.gz
[info]  2026-10-30 08:06:55 *** END ***

```

## [10] slurm_script_step6_vs_bna_PCSK9_compare
- first run: 2026-10-30 08:06:59
- last run: 2026-10-30 08:06:59
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 08:06:44 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6_vs_bna_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 08:06:44 working directory (temporary): /scratch-local/mvanvugt.28763721/tmp.4yZBP8yeFZ/task_1
[warn]  2026-10-30 08:06:44 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 08:06:46 manifest: 2097 file(s) in /scratch-local/mvanvugt.28763721/tmp.4yZBP8yeFZ/task_1/step6_vs_bna_PCSK9.compare.md5
[warn]  2026-10-30 08:06:59 step6_vs_bna_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step6_vs_bna_PCSK9/summary.tsv.gz
[info]  2026-10-30 08:06:59 *** END ***

```

## [10] slurm_script_step6b_CETP_new
- first run: 2026-10-30 02:42:52
- last run: 2026-10-30 02:42:52
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:53:32 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_CETP; mode: new; env: marvel_new
[info]  2026-10-29 23:53:32 working directory (temporary): /scratch-local/mvanvugt.28750274/tmp.LkQEXyT2he/task_1
[info]  2026-10-29 23:53:32 manifest: 3 file(s) in /scratch-local/mvanvugt.28750274/tmp.LkQEXyT2he/task_1/step6b_CETP.new.md5
[info]  2026-10-30 02:42:51 step6b_CETP: marvelous associate done, output to data/temp/validation/step6b/CETP
[info]  2026-10-30 02:42:51 *** END ***

```

## [10] slurm_script_step6b_PCSK9_new
- first run: 2026-10-30 04:22:13
- last run: 2026-10-30 04:22:13
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:53:23 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_PCSK9; mode: new; env: marvel_new
[info]  2026-10-29 23:53:23 working directory (temporary): /scratch-local/mvanvugt.28750287/tmp.XSKg8ozTJV/task_1
[info]  2026-10-29 23:53:23 manifest: 3 file(s) in /scratch-local/mvanvugt.28750287/tmp.XSKg8ozTJV/task_1/step6b_PCSK9.new.md5
[info]  2026-10-30 04:22:13 step6b_PCSK9: marvelous associate done, output to data/temp/validation/step6b/PCSK9
[info]  2026-10-30 04:22:13 *** END ***

```

## [10] slurm_script_step6b_vs_6_CETP_compare
- first run: 2026-10-30 08:05:12
- last run: 2026-10-30 12:36:37
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 12:36:34 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_vs_6_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 12:36:34 working directory (temporary): /scratch-local/mvanvugt.28771697/tmp.0W1y7WfBU4/task_1
[warn]  2026-10-30 12:36:34 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 12:36:34 manifest: 3 file(s) in /scratch-local/mvanvugt.28771697/tmp.0W1y7WfBU4/task_1/step6b_vs_6_CETP.compare.md5
[info]  2026-10-30 12:36:37 step6b_vs_6_CETP: GATE PASS
[info]  2026-10-30 12:36:37 *** END ***

```

## [10] slurm_script_step6b_vs_6_PCSK9_compare
- first run: 2026-10-30 08:10:06
- last run: 2026-10-30 12:34:53
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 12:34:49 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step6b_vs_6_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 12:34:49 working directory (temporary): /scratch-local/mvanvugt.28771656/tmp.NN6T0eJ4T2/task_1
[warn]  2026-10-30 12:34:49 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 12:34:49 manifest: 3 file(s) in /scratch-local/mvanvugt.28771656/tmp.NN6T0eJ4T2/task_1/step6b_vs_6_PCSK9.compare.md5
[info]  2026-10-30 12:34:53 step6b_vs_6_PCSK9: GATE PASS
[info]  2026-10-30 12:34:53 *** END ***

```

## [10] slurm_script_step7_CETP_run
- first run: 2026-10-30 13:33:34
- last run: 2026-10-30 14:03:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 13:46:04 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_CETP; mode: run; env: marvel_new
[info]  2026-10-30 13:46:04 working directory (temporary): /scratch-local/mvanvugt.28773614/tmp.d8esNH2H3p/task_1
[info]  2026-10-30 13:46:04 manifest: 4 file(s) in /scratch-local/mvanvugt.28773614/tmp.d8esNH2H3p/task_1/step7_CETP.run.md5
[info]  2026-10-30 14:03:18 step7_CETP: marvelous run done, output to data/temp/validation/step7/CETP
[info]  2026-10-30 14:03:18 *** END ***

```

## [10] slurm_script_step7_PCSK9_run
- first run: 2026-10-30 13:54:37
- last run: 2026-10-30 13:54:37
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 13:33:27 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_PCSK9; mode: run; env: marvel_new
[info]  2026-10-30 13:33:27 working directory (temporary): /scratch-local/mvanvugt.28773218/tmp.kYE0UXsPXC/task_1
[info]  2026-10-30 13:33:27 manifest: 4 file(s) in /scratch-local/mvanvugt.28773218/tmp.kYE0UXsPXC/task_1/step7_PCSK9.run.md5
[info]  2026-10-30 13:54:37 step7_PCSK9: marvelous run done, output to data/temp/validation/step7/PCSK9
[info]  2026-10-30 13:54:37 *** END ***

```

## [10] slurm_script_step7_vs_6b_all_CETP_compare
- first run: 2026-10-30 14:16:19
- last run: 2026-10-30 14:16:19
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:16:16 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_all_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 14:16:16 working directory (temporary): /scratch-local/mvanvugt.28774465/tmp.CoRYxNTqjJ/task_1
[warn]  2026-10-30 14:16:16 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:16:16 manifest: 3 file(s) in /scratch-local/mvanvugt.28774465/tmp.CoRYxNTqjJ/task_1/step7_vs_6b_all_CETP.compare.md5
[info]  2026-10-30 14:16:18 step7_vs_6b_all_CETP: GATE PASS
[info]  2026-10-30 14:16:18 *** END ***

```

## [10] slurm_script_step7_vs_6b_all_PCSK9_compare
- first run: 2026-10-30 14:17:33
- last run: 2026-10-30 14:17:33
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:17:31 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_all_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 14:17:31 working directory (temporary): /scratch-local/mvanvugt.28774518/tmp.ZrFhEWv4dO/task_1
[warn]  2026-10-30 14:17:31 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:17:31 manifest: 3 file(s) in /scratch-local/mvanvugt.28774518/tmp.ZrFhEWv4dO/task_1/step7_vs_6b_all_PCSK9.compare.md5
[info]  2026-10-30 14:17:33 step7_vs_6b_all_PCSK9: GATE PASS
[info]  2026-10-30 14:17:33 *** END ***

```

## [10] slurm_script_step7_vs_6b_same_CETP_compare
- first run: 2026-10-30 14:08:36
- last run: 2026-10-30 14:08:36
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:08:34 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_same_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 14:08:34 working directory (temporary): /scratch-local/mvanvugt.28774267/tmp.FNiplcnPZV/task_1
[warn]  2026-10-30 14:08:34 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:08:34 manifest: 3 file(s) in /scratch-local/mvanvugt.28774267/tmp.FNiplcnPZV/task_1/step7_vs_6b_same_CETP.compare.md5
[info]  2026-10-30 14:08:36 step7_vs_6b_same_CETP: GATE PASS
[info]  2026-10-30 14:08:36 *** END ***

```

## [10] slurm_script_step7_vs_6b_same_PCSK9_compare
- first run: 2026-10-30 14:15:40
- last run: 2026-10-30 14:15:40
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 14:15:37 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step7_vs_6b_same_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 14:15:37 working directory (temporary): /scratch-local/mvanvugt.28774449/tmp.5Fm74vvc08/task_1
[warn]  2026-10-30 14:15:37 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 14:15:37 manifest: 3 file(s) in /scratch-local/mvanvugt.28774449/tmp.5Fm74vvc08/task_1/step7_vs_6b_same_PCSK9.compare.md5
[info]  2026-10-30 14:15:40 step7_vs_6b_same_PCSK9: GATE PASS
[info]  2026-10-30 14:15:40 *** END ***

```

## [10] slurm_script_step8a_chr1
- first run: 2026-10-30 16:09:12
- last run: 2026-10-30 16:09:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:08:31 keys: validation/configs/step8/8a_chr1.keys.txt; vcf: /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz; summary: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a/vep_chr1.variants.tsv.gz
[info]  2026-10-30 16:08:32 14 key(s) on chr1 (FASTA 1);
[info]  2026-10-30 16:09:12 0 matching record(s)
[info]  2026-10-30 16:09:12 all 14 key(s) agree with marvel

```

## [10] slurm_script_step8a_chr16
- first run: 2026-10-30 16:06:07
- last run: 2026-10-30 16:06:07
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:05:46 keys: validation/configs/step8/8a_chr16.keys.txt; vcf: /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz; summary: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a/vep_chr16.variants.tsv.gz
[info]  2026-10-30 16:05:46 4 key(s) on chr16 (FASTA 16);
[info]  2026-10-30 16:06:06 0 matching record(s)
[info]  2026-10-30 16:06:06 all 4 key(s) agree with marvel

```

## [10] slurm_script_step8a_vs_7_CETP_compare
- first run: 2026-10-30 16:25:33
- last run: 2026-10-30 16:25:33
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:25:30 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step8a_vs_7_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 16:25:30 working directory (temporary): /scratch-local/mvanvugt.28777684/tmp.cdwAvIi6mQ/task_1
[warn]  2026-10-30 16:25:30 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 16:25:30 manifest: 3 file(s) in /scratch-local/mvanvugt.28777684/tmp.cdwAvIi6mQ/task_1/step8a_vs_7_CETP.compare.md5
[info]  2026-10-30 16:25:32 step8a_vs_7_CETP: GATE PASS
[info]  2026-10-30 16:25:32 *** END ***

```

## [10] slurm_script_step8a_vs_7_PCSK9_compare
- first run: 2026-10-30 16:15:12
- last run: 2026-10-30 16:15:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:15:10 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step8a_vs_7_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 16:15:10 working directory (temporary): /scratch-local/mvanvugt.28777539/tmp.1Xg11vOrX7/task_1
[warn]  2026-10-30 16:15:10 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 16:15:10 manifest: 3 file(s) in /scratch-local/mvanvugt.28777539/tmp.1Xg11vOrX7/task_1/step8a_vs_7_PCSK9.compare.md5
[info]  2026-10-30 16:15:12 step8a_vs_7_PCSK9: GATE PASS
[info]  2026-10-30 16:15:12 *** END ***

```

## [10] slurm_script_step8b_chr1
- first run: 2026-10-30 16:13:09
- last run: 2026-10-30 16:13:09
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:11:10 keys: validation/configs/step8/8b_chr1.keys.txt; vcf: /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz; summary: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8b/vep_chr1.variants.tsv.gz
[info]  2026-10-30 16:11:11 86 key(s) on chr1 (FASTA 1);
[info]  2026-10-30 16:13:09 72 matching record(s)
[info]  2026-10-30 16:13:09 all 86 key(s) agree with marvel

```

## [10] slurm_script_step8b_vs_6b_PCSK9_compare
- first run: 2026-10-30 16:21:46
- last run: 2026-10-30 16:21:46
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:21:43 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step8b_vs_6b_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 16:21:43 working directory (temporary): /scratch-local/mvanvugt.28777599/tmp.oL7I9ElN4Y/task_1
[warn]  2026-10-30 16:21:43 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 16:21:43 manifest: 3 file(s) in /scratch-local/mvanvugt.28777599/tmp.oL7I9ElN4Y/task_1/step8b_vs_6b_PCSK9.compare.md5
[warn]  2026-10-30 16:21:46 step8b_vs_6b_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step8b_vs_6b_PCSK9/summary.tsv.gz
[info]  2026-10-30 16:21:46 *** END ***

```

## [10] slurm_script_step9_PCSK9_run
- first run: 2026-10-30 17:42:43
- last run: 2026-10-30 17:42:43
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 17:40:39 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_PCSK9; mode: run; env: marvel_new
[info]  2026-10-30 17:40:39 working directory (temporary): /scratch-local/mvanvugt.28779479/tmp.oc8isLBK7f/task_1
[info]  2026-10-30 17:40:39 manifest: 4 file(s) in /scratch-local/mvanvugt.28779479/tmp.oc8isLBK7f/task_1/step9_PCSK9.run.md5
[info]  2026-10-30 17:42:43 step9_PCSK9: marvelous run done, output to data/temp/validation/step9/PCSK9
[info]  2026-10-30 17:42:43 *** END ***

```

## [10] slurm_script_step9_vs_2_CETP_compare
- first run: 2026-10-30 22:06:20
- last run: 2026-10-30 22:06:20
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:06:17 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 22:06:17 working directory (temporary): /scratch-local/mvanvugt.28783671/tmp.bvmG0vIimr/task_1
[warn]  2026-10-30 22:06:17 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:06:17 manifest: 6 file(s) in /scratch-local/mvanvugt.28783671/tmp.bvmG0vIimr/task_1/step9_vs_2_CETP.compare.md5
[warn]  2026-10-30 22:06:20 step9_vs_2_CETP: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step9_vs_2_CETP/summary.tsv.gz
[info]  2026-10-30 22:06:20 *** END ***

```

## [10] slurm_script_step9_vs_2_PCSK9_compare
- first run: 2026-10-30 22:06:20
- last run: 2026-10-30 22:06:20
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:06:17 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 22:06:17 working directory (temporary): /scratch-local/mvanvugt.28783672/tmp.nBODhyoYtl/task_1
[warn]  2026-10-30 22:06:17 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:06:17 manifest: 6 file(s) in /scratch-local/mvanvugt.28783672/tmp.nBODhyoYtl/task_1/step9_vs_2_PCSK9.compare.md5
[warn]  2026-10-30 22:06:20 step9_vs_2_PCSK9: GATE FAIL, see /gpfs/home6/mvanvugt/projects/lipid_adem/validation/results/step9_vs_2_PCSK9/summary.tsv.gz
[info]  2026-10-30 22:06:20 *** END ***

```

## [10] slurm_script_step9_vs_2_m1_CETP_compare
- first run: 2026-10-30 22:10:39
- last run: 2026-10-30 22:10:39
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:10:36 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_m1_CETP; mode: compare; env: prot_misc
[info]  2026-10-30 22:10:36 working directory (temporary): /scratch-local/mvanvugt.28783714/tmp.BupLtZw9dT/task_1
[warn]  2026-10-30 22:10:36 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:10:36 manifest: 6 file(s) in /scratch-local/mvanvugt.28783714/tmp.BupLtZw9dT/task_1/step9_vs_2_m1_CETP.compare.md5
[info]  2026-10-30 22:10:39 step9_vs_2_m1_CETP: GATE PASS
[info]  2026-10-30 22:10:39 *** END ***

```

## [10] slurm_script_step9_vs_2_m1_PCSK9_compare
- first run: 2026-10-30 22:09:12
- last run: 2026-10-30 22:09:12
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 22:09:09 root: /gpfs/home6/mvanvugt/projects/lipid_adem; step: step9_vs_2_m1_PCSK9; mode: compare; env: prot_misc
[info]  2026-10-30 22:09:09 working directory (temporary): /scratch-local/mvanvugt.28783695/tmp.bkNeaaR1OD/task_1
[warn]  2026-10-30 22:09:09 unknown (no /gpfs/home6/mvanvugt/projects/lipid_adem/validation/envs/prot_misc.commit, run step 0)
[info]  2026-10-30 22:09:09 manifest: 6 file(s) in /scratch-local/mvanvugt.28783695/tmp.bkNeaaR1OD/task_1/step9_vs_2_m1_PCSK9.compare.md5
[info]  2026-10-30 22:09:12 step9_vs_2_m1_PCSK9: GATE PASS
[info]  2026-10-30 22:09:12 *** END ***

```

## [10] slurm_script_vep_prep_task1
- first run: 2026-10-22 04:22:14
- last run: 2026-11-03 16:49:44
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:49 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:49 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 task 1: chr 1, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr1_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr1.vcf.gz
[info]  2026-11-03 16:49:43 chr 1: 0

```

## [10] slurm_script_vep_prep_task2
- first run: 2026-10-22 04:22:17
- last run: 2026-11-03 16:48:28
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:50 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 task 2: chr 11, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr11_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr11.vcf.gz
[info]  2026-11-03 16:48:28 chr 11: 18

```

## [10] slurm_script_vep_prep_task3
- first run: 2026-10-22 04:22:15
- last run: 2026-11-03 16:53:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:50 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:51 task 3: chr 2, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr2_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr2.vcf.gz
[info]  2026-11-03 16:53:34 chr 2: 178

```

## [10] slurm_script_vep_prep_task4
- first run: 2026-10-22 04:22:19
- last run: 2026-11-03 16:48:35
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:50 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:51 task 4: chr 19, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr19_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr19.vcf.gz
[info]  2026-11-03 16:48:35 chr 19: 8

```

## [10] slurm_script_vep_prep_task5
- first run: 2026-10-22 04:22:14
- last run: 2026-11-03 16:49:17
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:50 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:51 task 5: chr 16, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr16_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr16.vcf.gz
[info]  2026-11-03 16:49:17 chr 16: 0

```

## [10] slurm_script_vep_prep_task6
- first run: 2026-10-22 04:22:26
- last run: 2026-11-03 16:49:14
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:50 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:50 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:51 task 6: chr 5, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr5_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr5.vcf.gz
[info]  2026-11-03 16:49:14 chr 5: 0

```

## [10] slurm_script_vep_prep_task7
- first run: 2026-10-22 04:22:22
- last run: 2026-11-03 16:49:44
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:51 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:51 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:53 task 7: chr 7, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr7_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr7.vcf.gz
[info]  2026-11-03 16:49:44 chr 7: 0

```

## [10] slurm_script_vep_prep_task8
- first run: 2026-10-22 04:22:13
- last run: 2026-11-03 16:48:44
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:47:51 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:47:51 stage: vep_prep; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:47:53 task 8: chr 22, /gpfs/work2/0/aus20644/data/ukbiobank/genetics/b38/lof/chr22_merged_vep.vcf.gz -> /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/two_source/vep/vep_chr22.vcf.gz
[info]  2026-11-03 16:48:44 chr 22: 0

```

## [10] submit_two_source_submit_task1
- first run: 2026-10-21 21:41:00
- last run: 2026-11-03 16:45:52
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-03 16:45:38 env: /home/mvanvugt/mambaforge/envs/marvel_f1a3a8a
[info]  2026-11-03 16:45:38 stage: submit; config: /home/mvanvugt/projects/lipid_adem/validation/configs/f1a3a8a/burden.toml; output: /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a
[info]  2026-11-03 16:45:49 5 plink gene VCF(s); chromosomes: 1 11 2 19 16 5 7 22
[info]  2026-11-03 16:45:51 submitted: J1 28876269, J2 28876270, J3 28876271, J4 28876272

```

## [10] subset_carriers (`validation/subset_carriers.py --carriers /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variant_extraction.tsv.gz --output /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/PCSK9_carriers.tsv.gz --region chr1:1-999999999 --drop-merged --negative-to-na --binary`)
- first run: 2026-10-26 16:12:11
- last run: 2026-10-29 23:50:53
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-29 23:36:35 chr1:1-999999999: 1047 of 1047 variant columns kept (0 merged names, drop_merged=True)
[info]  2026-10-29 23:50:52 wrote 469835 rows x 1048 columns to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/PCSK9_carriers.tsv.gz
[info]  2026-10-29 23:50:52 negative values written as NA: 2834 cells
[info]  2026-10-29 23:50:52 binary coding (> 0.5): 18 variant columns had values > 1, 1029 keys written to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/PCSK9_carriers.no_dose2.txt
[info]  2026-10-29 23:50:52 value counts over variant cells: {'0': 490839574, '1': 1074837, 'NA': 2834}

```

## [20] filter_gwas_cat (`/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /home/mvanvugt/projects/lipid_adem/data/temp/tasks.tsv --task-id 116 --step 1`)
- first run: 2026-09-21 22:58:26
- last run: 2026-10-27 13:37:06
- commit: `23ebede` (dirty)
- status: failed

Output:
```text
[info]  2026-10-27 13:37:06 rows 116-116 of 125, 8 gene regions

--- error output (raw) ---
[info]  2026-10-27 13:37:06 rows 116-116 of 125, 8 gene regions
Traceback (most recent call last):
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 385, in main
    run_task(args.tasks_file, args.task_id, args.step)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 308, in run_task
    run_filter(accession, source, outfile, regions, manifest_df)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 222, in run_filter
    filtered = _run_filter_finngen(study_accession, regions, manifest_df)
  File "/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py", line 160, in _run_filter_finngen
    return functions.filter_sumstats_regions(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        tabix_source=url,
        ^^^^^^^^^^^^^^^^^
    ...<5 lines>...
        transform_to_maf=True,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/gpfs/home6/mvanvugt/projects/lipid_adem/src/functions.py", line 3410, in filter_sumstats_regions
    import pysam
ModuleNotFoundError: No module named 'pysam'
```

## [20] filter_gwas_cat_job
- first run: 2026-09-28 23:45:21
- last run: 2026-10-27 13:37:07
- commit: `23ebede` (dirty)
- status: failed

Output:
```text
[info]  2026-10-27 13:37:03 task 116: rows 116-116
[error] 2026-10-27 13:37:06 run_mamba: '/home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.py --tasks-file /home/mvanvugt/projects/lipid_adem/data/temp/tasks.tsv --task-id 116 --step 1' failed in env 'biomed-api' (exit 1)
--- error output (raw) ---
[info]  2026-10-27 13:37:03 repo root=/home/mvanvugt/projects/lipid_adem
[info]  2026-10-27 13:37:03 === /home/mvanvugt/projects/lipid_adem/src/filter_gwas_cat.sh ===
[info]  2026-10-27 13:37:03 started at Tue Oct 27 13:37:03 CET 2026
[info]  2026-10-27 13:37:03 hostname=tcn36
[info]  2026-10-27 13:37:03 job array file=/home/mvanvugt/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-10-27 13:37:03 temp location=/scratch-local/mvanvugt.28623635
[info]  2026-10-27 13:37:03 step=1
[info]  2026-10-27 13:37:03 task 116: rows 116-116
[info]  2026-10-27 13:37:06 rows 116-116 of 125, 8 gene regions
```

## [22] burden_exposure (`src/burden_exposure.py --mask-lists --genes ANGPTL3 APOA1 APOB APOE CETP HMGCR NPC1L1 PCSK9 PPARA`)
- first run: 2026-10-26 11:05:30
- last run: 2026-11-03 16:34:55
- commit: `23ebede` (dirty)

Output:
```text
[stage] 2026-11-03 16:34:53 variant sets
[info]  2026-11-03 16:34:53 3 SelectedGoF rows in no mask
[warn]  2026-11-03 16:34:53 5 site(s) both LoF-listed and GoF/raising, in the gof mask only: 1:55044016:T:A, 1:55044016:T:G, 1:55052400:T:C, 1:55057395:A:T, 1:55059525:T:C
[info]  2026-11-03 16:34:53 ANGPTL3: 554 listed sites; gof 0, am 493, ptv 56, clinvar 12, clinvar_directed 12, lof 62, lof_directed 62, ptv_am 549, am_clinvar 504, am_clinvar_directed 504, ptv_clinvar_am 554, ptv_clinvar_am_directed 554
[info]  2026-11-03 16:34:53 APOA1: 45 listed sites; gof 0, am 0, ptv 15, clinvar 33, clinvar_directed 16, lof 45, lof_directed 28, ptv_am 15, am_clinvar 33, am_clinvar_directed 16, ptv_clinvar_am 45, ptv_clinvar_am_directed 28
[info]  2026-11-03 16:34:53 APOB: 367 listed sites; gof 0, am 0, ptv 172, clinvar 236, clinvar_directed 224, lof 367, lof_directed 355, ptv_am 172, am_clinvar 236, am_clinvar_directed 224, ptv_clinvar_am 367, ptv_clinvar_am_directed 355
[info]  2026-11-03 16:34:53 APOE: 20 listed sites; gof 0, am 0, ptv 0, clinvar 20, clinvar_directed 3, lof 20, lof_directed 3, ptv_am 0, am_clinvar 20, am_clinvar_directed 3, ptv_clinvar_am 20, ptv_clinvar_am_directed 3
[info]  2026-11-03 16:34:53 CETP: 504 listed sites; gof 1, am 439, ptv 58, clinvar 10, clinvar_directed 10, lof 62, lof_directed 62, ptv_am 497, am_clinvar 449, am_clinvar_directed 449, ptv_clinvar_am 501, ptv_clinvar_am_directed 501
[info]  2026-11-03 16:34:53 HMGCR: 2668 listed sites; gof 0, am 2623, ptv 39, clinvar 7, clinvar_directed 6, lof 45, lof_directed 44, ptv_am 2662, am_clinvar 2630, am_clinvar_directed 2629, ptv_clinvar_am 2668, ptv_clinvar_am_directed 2667
[info]  2026-11-03 16:34:53 NPC1L1: 2603 listed sites; gof 0, am 2507, ptv 96, clinvar 0, clinvar_directed 0, lof 96, lof_directed 96, ptv_am 2603, am_clinvar 2507, am_clinvar_directed 2507, ptv_clinvar_am 2603, ptv_clinvar_am_directed 2603
[info]  2026-11-03 16:34:53 PCSK9: 831 listed sites; gof 29, am 732, ptv 68, clinvar 2, clinvar_directed 2, lof 70, lof_directed 70, ptv_am 800, am_clinvar 734, am_clinvar_directed 734, ptv_clinvar_am 802, ptv_clinvar_am_directed 802
[info]  2026-11-03 16:34:53 PPARA: 1566 listed sites; gof 0, am 1543, ptv 23, clinvar 0, clinvar_directed 0, lof 23, lof_directed 23, ptv_am 1566, am_clinvar 1543, am_clinvar_directed 1543, ptv_clinvar_am 1566, ptv_clinvar_am_directed 1566
[info]  2026-11-03 16:34:53 CETP: 3 sites in preferred studies
[stage] 2026-11-03 16:34:53 mask list
[warn]  2026-11-03 16:34:53 ANGPTL3_gof: no sites, not listed
[info]  2026-11-03 16:34:53 ANGPTL3_am: 493 sites
[info]  2026-11-03 16:34:53 ANGPTL3_ptv: 56 sites
[info]  2026-11-03 16:34:53 ANGPTL3_clinvar: 12 sites
[info]  2026-11-03 16:34:53 ANGPTL3_clinvar_directed: 12 sites
[info]  2026-11-03 16:34:53 ANGPTL3_lof: 62 sites
[info]  2026-11-03 16:34:53 ANGPTL3_lof_directed: 62 sites
[info]  2026-11-03 16:34:53 ANGPTL3_ptv_am: 549 sites
[info]  2026-11-03 16:34:53 ANGPTL3_am_clinvar: 504 sites
[info]  2026-11-03 16:34:53 ANGPTL3_am_clinvar_directed: 504 sites
[info]  2026-11-03 16:34:53 ANGPTL3_ptv_clinvar_am: 554 sites
[info]  2026-11-03 16:34:53 ANGPTL3_ptv_clinvar_am_directed: 554 sites
[warn]  2026-11-03 16:34:53 APOA1_gof: no sites, not listed
[warn]  2026-11-03 16:34:53 APOA1_am: no sites, not listed
[info]  2026-11-03 16:34:53 APOA1_ptv: 15 sites
[info]  2026-11-03 16:34:53 APOA1_clinvar: 33 sites
[info]  2026-11-03 16:34:53 APOA1_clinvar_directed: 16 sites
[info]  2026-11-03 16:34:53 APOA1_lof: 45 sites
[info]  2026-11-03 16:34:53 APOA1_lof_directed: 28 sites
[info]  2026-11-03 16:34:53 APOA1_ptv_am: 15 sites
[info]  2026-11-03 16:34:53 APOA1_am_clinvar: 33 sites
[info]  2026-11-03 16:34:53 APOA1_am_clinvar_directed: 16 sites
[info]  2026-11-03 16:34:53 APOA1_ptv_clinvar_am: 45 sites
[info]  2026-11-03 16:34:53 APOA1_ptv_clinvar_am_directed: 28 sites
[warn]  2026-11-03 16:34:53 APOB_gof: no sites, not listed
[warn]  2026-11-03 16:34:53 APOB_am: no sites, not listed
[info]  2026-11-03 16:34:53 APOB_ptv: 172 sites
[info]  2026-11-03 16:34:53 APOB_clinvar: 236 sites
[info]  2026-11-03 16:34:53 APOB_clinvar_directed: 224 sites
[info]  2026-11-03 16:34:53 APOB_lof: 367 sites
[info]  2026-11-03 16:34:53 APOB_lof_directed: 355 sites
[info]  2026-11-03 16:34:53 APOB_ptv_am: 172 sites
[info]  2026-11-03 16:34:53 APOB_am_clinvar: 236 sites
[info]  2026-11-03 16:34:53 APOB_am_clinvar_directed: 224 sites
[info]  2026-11-03 16:34:53 APOB_ptv_clinvar_am: 367 sites
[info]  2026-11-03 16:34:53 APOB_ptv_clinvar_am_directed: 355 sites
[warn]  2026-11-03 16:34:53 APOE_gof: no sites, not listed
[warn]  2026-11-03 16:34:53 APOE_am: no sites, not listed
[warn]  2026-11-03 16:34:53 APOE_ptv: no sites, not listed
[info]  2026-11-03 16:34:53 APOE_clinvar: 20 sites
[info]  2026-11-03 16:34:53 APOE_clinvar_directed: 3 sites
[info]  2026-11-03 16:34:53 APOE_lof: 20 sites
[info]  2026-11-03 16:34:53 APOE_lof_directed: 3 sites
[warn]  2026-11-03 16:34:53 APOE_ptv_am: no sites, not listed
[info]  2026-11-03 16:34:53 APOE_am_clinvar: 20 sites
[info]  2026-11-03 16:34:53 APOE_am_clinvar_directed: 3 sites
[info]  2026-11-03 16:34:53 APOE_ptv_clinvar_am: 20 sites
[info]  2026-11-03 16:34:53 APOE_ptv_clinvar_am_directed: 3 sites
[info]  2026-11-03 16:34:53 CETP_gof: 1 sites
[info]  2026-11-03 16:34:53 CETP_am: 439 sites
[info]  2026-11-03 16:34:53 CETP_ptv: 58 sites
[info]  2026-11-03 16:34:53 CETP_clinvar: 10 sites
[info]  2026-11-03 16:34:53 CETP_clinvar_directed: 10 sites
[info]  2026-11-03 16:34:53 CETP_lof: 62 sites
[info]  2026-11-03 16:34:53 CETP_lof_directed: 62 sites
[info]  2026-11-03 16:34:53 CETP_ptv_am: 497 sites
[info]  2026-11-03 16:34:53 CETP_am_clinvar: 449 sites
[info]  2026-11-03 16:34:53 CETP_am_clinvar_directed: 449 sites
[info]  2026-11-03 16:34:53 CETP_ptv_clinvar_am: 501 sites
[info]  2026-11-03 16:34:53 CETP_ptv_clinvar_am_directed: 501 sites
[warn]  2026-11-03 16:34:53 HMGCR_gof: no sites, not listed
[info]  2026-11-03 16:34:53 HMGCR_am: 2623 sites
[info]  2026-11-03 16:34:53 HMGCR_ptv: 39 sites
[info]  2026-11-03 16:34:53 HMGCR_clinvar: 7 sites
[info]  2026-11-03 16:34:53 HMGCR_clinvar_directed: 6 sites
[info]  2026-11-03 16:34:53 HMGCR_lof: 45 sites
[info]  2026-11-03 16:34:53 HMGCR_lof_directed: 44 sites
[info]  2026-11-03 16:34:53 HMGCR_ptv_am: 2662 sites
[info]  2026-11-03 16:34:53 HMGCR_am_clinvar: 2630 sites
[info]  2026-11-03 16:34:53 HMGCR_am_clinvar_directed: 2629 sites
[info]  2026-11-03 16:34:53 HMGCR_ptv_clinvar_am: 2668 sites
[info]  2026-11-03 16:34:53 HMGCR_ptv_clinvar_am_directed: 2667 sites
[warn]  2026-11-03 16:34:53 NPC1L1_gof: no sites, not listed
[info]  2026-11-03 16:34:53 NPC1L1_am: 2507 sites
[info]  2026-11-03 16:34:53 NPC1L1_ptv: 96 sites
[warn]  2026-11-03 16:34:53 NPC1L1_clinvar: no sites, not listed
[warn]  2026-11-03 16:34:53 NPC1L1_clinvar_directed: no sites, not listed
[info]  2026-11-03 16:34:53 NPC1L1_lof: 96 sites
[info]  2026-11-03 16:34:53 NPC1L1_lof_directed: 96 sites
[info]  2026-11-03 16:34:53 NPC1L1_ptv_am: 2603 sites
[info]  2026-11-03 16:34:53 NPC1L1_am_clinvar: 2507 sites
[info]  2026-11-03 16:34:54 NPC1L1_am_clinvar_directed: 2507 sites
[info]  2026-11-03 16:34:54 NPC1L1_ptv_clinvar_am: 2603 sites
[info]  2026-11-03 16:34:54 NPC1L1_ptv_clinvar_am_directed: 2603 sites
[info]  2026-11-03 16:34:54 PCSK9_gof: 29 sites
[info]  2026-11-03 16:34:54 PCSK9_am: 732 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv: 68 sites
[info]  2026-11-03 16:34:54 PCSK9_clinvar: 2 sites
[info]  2026-11-03 16:34:54 PCSK9_clinvar_directed: 2 sites
[info]  2026-11-03 16:34:54 PCSK9_lof: 70 sites
[info]  2026-11-03 16:34:54 PCSK9_lof_directed: 70 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_am: 800 sites
[info]  2026-11-03 16:34:54 PCSK9_am_clinvar: 734 sites
[info]  2026-11-03 16:34:54 PCSK9_am_clinvar_directed: 734 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_clinvar_am: 802 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_clinvar_am_directed: 802 sites
[warn]  2026-11-03 16:34:54 PPARA_gof: no sites, not listed
[info]  2026-11-03 16:34:54 PPARA_am: 1543 sites
[info]  2026-11-03 16:34:54 PPARA_ptv: 23 sites
[warn]  2026-11-03 16:34:54 PPARA_clinvar: no sites, not listed
[warn]  2026-11-03 16:34:54 PPARA_clinvar_directed: no sites, not listed
[info]  2026-11-03 16:34:54 PPARA_lof: 23 sites
[info]  2026-11-03 16:34:54 PPARA_lof_directed: 23 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_am: 1566 sites
[info]  2026-11-03 16:34:54 PPARA_am_clinvar: 1543 sites
[info]  2026-11-03 16:34:54 PPARA_am_clinvar_directed: 1543 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_clinvar_am: 1566 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_clinvar_am_directed: 1566 sites
[info]  2026-11-03 16:34:54 wrote 55354 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_mask_variants.tsv.gz
[stage] 2026-11-03 16:34:54 fallback mask list
[warn]  2026-11-03 16:34:54 ANGPTL3_gof_fb: no sites, not listed
[info]  2026-11-03 16:34:54 ANGPTL3_am_fb: 493 sites
[info]  2026-11-03 16:34:54 ANGPTL3_ptv_fb: 56 sites
[info]  2026-11-03 16:34:54 ANGPTL3_clinvar_fb: 12 sites
[info]  2026-11-03 16:34:54 ANGPTL3_clinvar_directed_fb: 12 sites
[info]  2026-11-03 16:34:54 ANGPTL3_lof_fb: 62 sites
[info]  2026-11-03 16:34:54 ANGPTL3_lof_directed_fb: 62 sites
[info]  2026-11-03 16:34:54 ANGPTL3_ptv_am_fb: 549 sites
[info]  2026-11-03 16:34:54 ANGPTL3_am_clinvar_fb: 504 sites
[info]  2026-11-03 16:34:54 ANGPTL3_am_clinvar_directed_fb: 504 sites
[info]  2026-11-03 16:34:54 ANGPTL3_ptv_clinvar_am_fb: 554 sites
[info]  2026-11-03 16:34:54 ANGPTL3_ptv_clinvar_am_directed_fb: 554 sites
[warn]  2026-11-03 16:34:54 APOA1_gof_fb: no sites, not listed
[warn]  2026-11-03 16:34:54 APOA1_am_fb: no sites, not listed
[info]  2026-11-03 16:34:54 APOA1_ptv_fb: 15 sites
[info]  2026-11-03 16:34:54 APOA1_clinvar_fb: 33 sites
[info]  2026-11-03 16:34:54 APOA1_clinvar_directed_fb: 16 sites
[info]  2026-11-03 16:34:54 APOA1_lof_fb: 45 sites
[info]  2026-11-03 16:34:54 APOA1_lof_directed_fb: 28 sites
[info]  2026-11-03 16:34:54 APOA1_ptv_am_fb: 15 sites
[info]  2026-11-03 16:34:54 APOA1_am_clinvar_fb: 33 sites
[info]  2026-11-03 16:34:54 APOA1_am_clinvar_directed_fb: 16 sites
[info]  2026-11-03 16:34:54 APOA1_ptv_clinvar_am_fb: 45 sites
[info]  2026-11-03 16:34:54 APOA1_ptv_clinvar_am_directed_fb: 28 sites
[warn]  2026-11-03 16:34:54 APOB_gof_fb: no sites, not listed
[warn]  2026-11-03 16:34:54 APOB_am_fb: no sites, not listed
[info]  2026-11-03 16:34:54 APOB_ptv_fb: 172 sites
[info]  2026-11-03 16:34:54 APOB_clinvar_fb: 236 sites
[info]  2026-11-03 16:34:54 APOB_clinvar_directed_fb: 224 sites
[info]  2026-11-03 16:34:54 APOB_lof_fb: 367 sites
[info]  2026-11-03 16:34:54 APOB_lof_directed_fb: 355 sites
[info]  2026-11-03 16:34:54 APOB_ptv_am_fb: 172 sites
[info]  2026-11-03 16:34:54 APOB_am_clinvar_fb: 236 sites
[info]  2026-11-03 16:34:54 APOB_am_clinvar_directed_fb: 224 sites
[info]  2026-11-03 16:34:54 APOB_ptv_clinvar_am_fb: 367 sites
[info]  2026-11-03 16:34:54 APOB_ptv_clinvar_am_directed_fb: 355 sites
[warn]  2026-11-03 16:34:54 APOE_gof_fb: no sites, not listed
[warn]  2026-11-03 16:34:54 APOE_am_fb: no sites, not listed
[warn]  2026-11-03 16:34:54 APOE_ptv_fb: no sites, not listed
[info]  2026-11-03 16:34:54 APOE_clinvar_fb: 20 sites
[info]  2026-11-03 16:34:54 APOE_clinvar_directed_fb: 3 sites
[info]  2026-11-03 16:34:54 APOE_lof_fb: 20 sites
[info]  2026-11-03 16:34:54 APOE_lof_directed_fb: 3 sites
[warn]  2026-11-03 16:34:54 APOE_ptv_am_fb: no sites, not listed
[info]  2026-11-03 16:34:54 APOE_am_clinvar_fb: 20 sites
[info]  2026-11-03 16:34:54 APOE_am_clinvar_directed_fb: 3 sites
[info]  2026-11-03 16:34:54 APOE_ptv_clinvar_am_fb: 20 sites
[info]  2026-11-03 16:34:54 APOE_ptv_clinvar_am_directed_fb: 3 sites
[info]  2026-11-03 16:34:54 CETP_gof_fb: 1 sites
[info]  2026-11-03 16:34:54 CETP_am_fb: 439 sites
[info]  2026-11-03 16:34:54 CETP_ptv_fb: 58 sites
[info]  2026-11-03 16:34:54 CETP_clinvar_fb: 10 sites
[info]  2026-11-03 16:34:54 CETP_clinvar_directed_fb: 10 sites
[info]  2026-11-03 16:34:54 CETP_lof_fb: 62 sites
[info]  2026-11-03 16:34:54 CETP_lof_directed_fb: 62 sites
[info]  2026-11-03 16:34:54 CETP_ptv_am_fb: 497 sites
[info]  2026-11-03 16:34:54 CETP_am_clinvar_fb: 449 sites
[info]  2026-11-03 16:34:54 CETP_am_clinvar_directed_fb: 449 sites
[info]  2026-11-03 16:34:54 CETP_ptv_clinvar_am_fb: 501 sites
[info]  2026-11-03 16:34:54 CETP_ptv_clinvar_am_directed_fb: 501 sites
[warn]  2026-11-03 16:34:54 HMGCR_gof_fb: no sites, not listed
[info]  2026-11-03 16:34:54 HMGCR_am_fb: 2623 sites
[info]  2026-11-03 16:34:54 HMGCR_ptv_fb: 39 sites
[info]  2026-11-03 16:34:54 HMGCR_clinvar_fb: 7 sites
[info]  2026-11-03 16:34:54 HMGCR_clinvar_directed_fb: 6 sites
[info]  2026-11-03 16:34:54 HMGCR_lof_fb: 45 sites
[info]  2026-11-03 16:34:54 HMGCR_lof_directed_fb: 44 sites
[info]  2026-11-03 16:34:54 HMGCR_ptv_am_fb: 2662 sites
[info]  2026-11-03 16:34:54 HMGCR_am_clinvar_fb: 2630 sites
[info]  2026-11-03 16:34:54 HMGCR_am_clinvar_directed_fb: 2629 sites
[info]  2026-11-03 16:34:54 HMGCR_ptv_clinvar_am_fb: 2668 sites
[info]  2026-11-03 16:34:54 HMGCR_ptv_clinvar_am_directed_fb: 2667 sites
[warn]  2026-11-03 16:34:54 NPC1L1_gof_fb: no sites, not listed
[info]  2026-11-03 16:34:54 NPC1L1_am_fb: 2507 sites
[info]  2026-11-03 16:34:54 NPC1L1_ptv_fb: 96 sites
[warn]  2026-11-03 16:34:54 NPC1L1_clinvar_fb: no sites, not listed
[warn]  2026-11-03 16:34:54 NPC1L1_clinvar_directed_fb: no sites, not listed
[info]  2026-11-03 16:34:54 NPC1L1_lof_fb: 96 sites
[info]  2026-11-03 16:34:54 NPC1L1_lof_directed_fb: 96 sites
[info]  2026-11-03 16:34:54 NPC1L1_ptv_am_fb: 2603 sites
[info]  2026-11-03 16:34:54 NPC1L1_am_clinvar_fb: 2507 sites
[info]  2026-11-03 16:34:54 NPC1L1_am_clinvar_directed_fb: 2507 sites
[info]  2026-11-03 16:34:54 NPC1L1_ptv_clinvar_am_fb: 2603 sites
[info]  2026-11-03 16:34:54 NPC1L1_ptv_clinvar_am_directed_fb: 2603 sites
[info]  2026-11-03 16:34:54 PCSK9_gof_fb: 29 sites
[info]  2026-11-03 16:34:54 PCSK9_am_fb: 732 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_fb: 68 sites
[info]  2026-11-03 16:34:54 PCSK9_clinvar_fb: 2 sites
[info]  2026-11-03 16:34:54 PCSK9_clinvar_directed_fb: 2 sites
[info]  2026-11-03 16:34:54 PCSK9_lof_fb: 70 sites
[info]  2026-11-03 16:34:54 PCSK9_lof_directed_fb: 70 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_am_fb: 800 sites
[info]  2026-11-03 16:34:54 PCSK9_am_clinvar_fb: 734 sites
[info]  2026-11-03 16:34:54 PCSK9_am_clinvar_directed_fb: 734 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_clinvar_am_fb: 802 sites
[info]  2026-11-03 16:34:54 PCSK9_ptv_clinvar_am_directed_fb: 802 sites
[warn]  2026-11-03 16:34:54 PPARA_gof_fb: no sites, not listed
[info]  2026-11-03 16:34:54 PPARA_am_fb: 1543 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_fb: 23 sites
[warn]  2026-11-03 16:34:54 PPARA_clinvar_fb: no sites, not listed
[warn]  2026-11-03 16:34:54 PPARA_clinvar_directed_fb: no sites, not listed
[info]  2026-11-03 16:34:54 PPARA_lof_fb: 23 sites
[info]  2026-11-03 16:34:54 PPARA_lof_directed_fb: 23 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_am_fb: 1566 sites
[info]  2026-11-03 16:34:54 PPARA_am_clinvar_fb: 1543 sites
[info]  2026-11-03 16:34:54 PPARA_am_clinvar_directed_fb: 1543 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_clinvar_am_fb: 1566 sites
[info]  2026-11-03 16:34:54 PPARA_ptv_clinvar_am_directed_fb: 1566 sites
[info]  2026-11-03 16:34:55 wrote 55354 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_mask_variants_fb.tsv.gz

```

## [25] marvel_results_table (`/home/mvanvugt/projects/lipid_adem/src/marvel_results_table.py --ancestry MULTI --tasks /home/mvanvugt/projects/lipid_adem/data/raw/marvel_tasks.tsv /home/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv --replace /home/mvanvugt/projects/lipid_adem/data/raw/marvel_selected_tasks.tsv`)
- first run: 2026-10-08 09:54:25
- last run: 2026-10-27 15:08:16
- commit: `23ebede` (dirty)

Output:
```text
[stage] 2026-10-27 15:03:26 compare
[info]  2026-10-27 15:03:26 /home/mvanvugt/projects/lipid_adem/data/raw/marvel_tasks.tsv: 18 rows
[info]  2026-10-27 15:03:26 /home/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv: 24 rows
[info]  2026-10-27 15:03:26 6 genes over 2 task file(s)
[info]  2026-10-27 15:03:26 /home/mvanvugt/projects/lipid_adem/data/raw/marvel_selected_tasks.tsv: 3 rows
[info]  2026-10-27 15:03:26 1 genes over 1 task file(s)
[info]  2026-10-27 15:03:30 /home/mvanvugt/projects/lipid_adem/results/CETP: 667 loose result files
[info]  2026-10-27 15:03:36 /home/mvanvugt/projects/lipid_adem/results/CETP_all_apoe: 667 loose result files
[info]  2026-10-27 15:03:43 /home/mvanvugt/projects/lipid_adem/results/CETP_eur: 667 loose result files
[info]  2026-10-27 15:03:43 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_all_apoe: 12 loose result files
[info]  2026-10-27 15:03:43 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur: 12 loose result files
[info]  2026-10-27 15:03:43 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_all_apoe_fb: 12 loose result files
[info]  2026-10-27 15:03:43 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur_fb: 12 loose result files
[info]  2026-10-27 15:03:45 /gpfs/home6/mvanvugt/projects/lipid_adem/results/CETP_selected: 3 loose result files
[info]  2026-10-27 15:03:45 /gpfs/home6/mvanvugt/projects/lipid_adem/results/CETP_selected_all_apoe: 3 loose result files
[info]  2026-10-27 15:03:45 /gpfs/home6/mvanvugt/projects/lipid_adem/results/CETP_selected_eur: 3 loose result files
[info]  2026-10-27 15:03:45 CETP: 6840 rows of 3 result files replace the rows of the same files
[info]  2026-10-27 15:03:45 CETP: 6840 loose rows of 3 replaced result files left out
[info]  2026-10-27 15:03:56 CETP: 6840 store rows of 3 replaced result files left out
[info]  2026-10-27 15:03:56 CETP: replaced files 6840 store rows -> 6840 rows, changed
[info]  2026-10-27 15:04:08 CETP: 1347000 loose rows, 0 new, 1347000 already in the store
[warn]  2026-10-27 15:04:08 CETP: 6840 rows of 3 result files in CETP_results.tsv.gz replaced by 6840 rows (11 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-27 15:04:12 /home/mvanvugt/projects/lipid_adem/results/HMGCR: 714 loose result files
[info]  2026-10-27 15:04:18 /home/mvanvugt/projects/lipid_adem/results/HMGCR_all_apoe: 714 loose result files
[info]  2026-10-27 15:04:25 /home/mvanvugt/projects/lipid_adem/results/HMGCR_eur: 714 loose result files
[info]  2026-10-27 15:04:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_all_apoe: 11 loose result files
[info]  2026-10-27 15:04:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_eur: 11 loose result files
[info]  2026-10-27 15:04:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_all_apoe_fb: 11 loose result files
[info]  2026-10-27 15:04:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_eur_fb: 11 loose result files
[info]  2026-10-27 15:04:46 HMGCR: 1486520 loose rows, 0 new, 1486520 already in the store
[info]  2026-10-27 15:04:53 /home/mvanvugt/projects/lipid_adem/results/NPC1L1: 1257 loose result files
[info]  2026-10-27 15:05:04 /home/mvanvugt/projects/lipid_adem/results/NPC1L1_all_apoe: 1257 loose result files
[info]  2026-10-27 15:05:16 /home/mvanvugt/projects/lipid_adem/results/NPC1L1_eur: 1257 loose result files
[info]  2026-10-27 15:05:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_all_apoe: 9 loose result files
[info]  2026-10-27 15:05:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_eur: 9 loose result files
[info]  2026-10-27 15:05:16 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_all_apoe_fb: 9 loose result files
[info]  2026-10-27 15:05:17 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_eur_fb: 9 loose result files
[info]  2026-10-27 15:05:54 NPC1L1: 2411650 loose rows, 0 new, 2411650 already in the store
[info]  2026-10-27 15:06:01 /home/mvanvugt/projects/lipid_adem/results/PCSK9: 1047 loose result files
[info]  2026-10-27 15:06:09 /home/mvanvugt/projects/lipid_adem/results/PCSK9_all_apoe: 1047 loose result files
[info]  2026-10-27 15:06:18 /home/mvanvugt/projects/lipid_adem/results/PCSK9_eur: 1047 loose result files
[info]  2026-10-27 15:06:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_all_apoe: 10 loose result files
[info]  2026-10-27 15:06:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_eur: 10 loose result files
[info]  2026-10-27 15:06:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_all_apoe_fb: 10 loose result files
[info]  2026-10-27 15:06:18 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_eur_fb: 10 loose result files
[info]  2026-10-27 15:06:53 PCSK9: 1975580 loose rows, 0 new, 1975580 already in the store
[info]  2026-10-27 15:06:56 /home/mvanvugt/projects/lipid_adem/results/ANGPTL3: 324 loose result files
[info]  2026-10-27 15:06:58 /home/mvanvugt/projects/lipid_adem/results/ANGPTL3_all_apoe: 324 loose result files
[info]  2026-10-27 15:07:02 /home/mvanvugt/projects/lipid_adem/results/ANGPTL3_eur: 324 loose result files
[info]  2026-10-27 15:07:02 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_all_apoe: 11 loose result files
[info]  2026-10-27 15:07:02 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_eur: 11 loose result files
[info]  2026-10-27 15:07:02 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_all_apoe_fb: 11 loose result files
[info]  2026-10-27 15:07:02 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_eur_fb: 11 loose result files
[info]  2026-10-27 15:07:12 ANGPTL3: 665870 loose rows, 0 new, 665870 already in the store
[info]  2026-10-27 15:07:14 /home/mvanvugt/projects/lipid_adem/results/PPARA: 343 loose result files
[info]  2026-10-27 15:07:17 /home/mvanvugt/projects/lipid_adem/results/PPARA_all_apoe: 343 loose result files
[info]  2026-10-27 15:07:21 /home/mvanvugt/projects/lipid_adem/results/PPARA_eur: 343 loose result files
[info]  2026-10-27 15:07:21 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_all_apoe: 9 loose result files
[info]  2026-10-27 15:07:21 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_eur: 9 loose result files
[info]  2026-10-27 15:07:21 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_all_apoe_fb: 9 loose result files
[info]  2026-10-27 15:07:21 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_eur_fb: 9 loose result files
[info]  2026-10-27 15:07:32 PPARA: 663890 loose rows, 0 new, 663890 already in the store
[stage] 2026-10-27 15:07:33 write_stores
[info]  2026-10-27 15:07:33 CETP: old store kept as CETP_results.20261027_150326.tsv.gz
[info]  2026-10-27 15:07:55 CETP: wrote 1353840 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/CETP_results.tsv.gz
[stage] 2026-10-27 15:07:55 marvel_table
[info]  2026-10-27 15:07:57 ANGPTL3: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 15:07:59 CETP: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 15:08:02 HMGCR: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 15:08:09 NPC1L1: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 15:08:14 PCSK9: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 15:08:16 PPARA: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 15:08:16 wrote 600 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-10-27 15:08:16 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: all marvel strata already listed

```

## [27] compare_marvel_runs (`src/compare_marvel_runs.py --old-stores validation/B --variant-prefix step10_variant_dos --run-dir /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_reindex --genes CETP HMGCR ANGPTL3 PPARA PCSK9 NPC1L1 --out-dir validation/results/step10_vs_b --lost-out /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step10/lost_carriers.tsv.gz`)
- first run: 2026-11-02 14:56:55
- last run: 2026-11-02 15:37:30
- commit: `23ebede` (dirty)

Output:
```text
[stage] 2026-11-02 15:36:13 variant lists
[warn]  2026-11-02 15:36:13 CETP: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv; NA
[info]  2026-11-02 15:36:13 CETP: 508 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv
[warn]  2026-11-02 15:36:13 HMGCR: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv; NA
[info]  2026-11-02 15:36:13 HMGCR: 2668 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[warn]  2026-11-02 15:36:13 ANGPTL3: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv; NA
[info]  2026-11-02 15:36:13 ANGPTL3: 556 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[warn]  2026-11-02 15:36:13 PPARA: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv; NA
[info]  2026-11-02 15:36:13 PPARA: 1567 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv
[warn]  2026-11-02 15:36:13 PCSK9: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv; NA
[info]  2026-11-02 15:36:13 PCSK9: 831 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[warn]  2026-11-02 15:36:13 NPC1L1: no 'source' column in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv; NA
[info]  2026-11-02 15:36:13 NPC1L1: 2606 rows in old list /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[info]  2026-11-02 15:36:16 9158 variants in new list /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-11-02 15:36:19 CETP: 5664 overall variant rows in CETP_results.tsv.gz
[info]  2026-11-02 15:36:23 HMGCR: 5184 overall variant rows in HMGCR_results.tsv.gz
[info]  2026-11-02 15:36:24 ANGPTL3: 3840 overall variant rows in ANGPTL3_results.tsv.gz
[info]  2026-11-02 15:36:26 PPARA: 3600 overall variant rows in PPARA_results.tsv.gz
[info]  2026-11-02 15:36:31 PCSK9: 8708 overall variant rows in PCSK9_results.tsv.gz
[info]  2026-11-02 15:36:37 NPC1L1: 14350 overall variant rows in NPC1L1_results.tsv.gz
[info]  2026-11-02 15:36:37 chunk ukb_ANGPTL3_chr1_plink: 223 variant(s) read, 469835 samples
[info]  2026-11-02 15:36:38 chunk ukb_CETP_chr16_plink: 95 variant(s) read, 469835 samples
[info]  2026-11-02 15:36:39 chunk ukb_HMGCR_chr5_plink: 170 variant(s) read, 469835 samples
[info]  2026-11-02 15:36:39 chunk ukb_NPC1L1_chr7_plink: 270 variant(s) read, 469835 samples
[info]  2026-11-02 15:36:39 chunk ukb_PPARA_chr22_plink: 125 variant(s) read, 469835 samples
[info]  2026-11-02 15:36:40 chunk vep_chr1: 0 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:40 chunk vep_chr11: 18 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:40 chunk vep_chr16: 0 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:40 chunk vep_chr19: 8 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:41 chunk vep_chr2: 179 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:41 chunk vep_chr22: 0 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:41 chunk vep_chr5: 0 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:42 chunk vep_chr7: 0 variant(s) read, 377567 samples
[info]  2026-11-02 15:36:42 variant lists: 8736 old, 9168 new, old matched by {'exact': 8726, 'orig': 10}, 432 new only
[info]  2026-11-02 15:36:42 new extract status: {'not_found': 6649, 'allele_mismatch': 1421, 'found': 1097, 'swapped': 1}
[info]  2026-11-02 15:36:43 wrote 9168 rows to validation/results/step10_vs_b/variant_lists.tsv.gz
[stage] 2026-11-02 15:36:43 carriers
[info]  2026-11-02 15:36:43 CETP: 472 variant column(s) in CETP_variant_extraction.tsv.gz, 95 in the new list
[info]  2026-11-02 15:36:48 CETP: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-02 15:36:48 HMGCR: 432 variant column(s) in HMGCR_variant_extraction.tsv.gz, 170 in the new list
[info]  2026-11-02 15:36:56 HMGCR: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-02 15:36:56 ANGPTL3: 320 variant column(s) in ANGPTL3_variant_extraction.tsv.gz, 90 in the new list
[info]  2026-11-02 15:36:59 ANGPTL3: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-02 15:36:59 PPARA: 300 variant column(s) in PPARA_variant_extraction.tsv.gz, 124 in the new list
[info]  2026-11-02 15:37:03 PPARA: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-02 15:37:03 PCSK9: 622 variant column(s) in PCSK9_variant_extraction.tsv.gz, 131 in the new list
[info]  2026-11-02 15:37:12 PCSK9: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-02 15:37:12 NPC1L1: 1025 variant column(s) in NPC1L1_variant_extraction.tsv.gz, 267 in the new list
[info]  2026-11-02 15:37:25 NPC1L1: 469835 old samples, 469835 of them in the largest new chunk (469835 samples)
[info]  2026-11-02 15:37:25 CETP: 95 variant(s), 0 with lost carriers; totals {'n_old_carriers': 504011, 'n_both': 504011, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-02 15:37:25 HMGCR: 170 variant(s), 0 with lost carriers; totals {'n_old_carriers': 406, 'n_both': 406, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-02 15:37:25 ANGPTL3: 90 variant(s), 0 with lost carriers; totals {'n_old_carriers': 1622, 'n_both': 1622, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-02 15:37:25 PPARA: 124 variant(s), 0 with lost carriers; totals {'n_old_carriers': 1208, 'n_both': 1208, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-02 15:37:25 PCSK9: 131 variant(s), 0 with lost carriers; totals {'n_old_carriers': 2491, 'n_both': 2491, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-02 15:37:25 NPC1L1: 267 variant(s), 0 with lost carriers; totals {'n_old_carriers': 2423, 'n_both': 2423, 'n_lost': 0, 'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0}
[info]  2026-11-02 15:37:25 wrote 877 rows to validation/results/step10_vs_b/carriers.tsv.gz
[info]  2026-11-02 15:37:25 wrote 0 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step10/lost_carriers.tsv.gz
[stage] 2026-11-02 15:37:25 results
[info]  2026-11-02 15:37:26 0 strata_ref reference row(s) dropped
[info]  2026-11-02 15:37:27 128212 new overall variant rows in step10_variant_dos.results.tsv.gz
[info]  2026-11-02 15:37:27 results adjusted: 5653 joined rows, 3598 same sign, 10 with |z_diff| > 2; 7 old only, 58446 new only
[info]  2026-11-02 15:37:27 results unadjusted: 5660 joined rows, 3554 same sign, 10 with |z_diff| > 2; 0 old only, 58446 new only
[info]  2026-11-02 15:37:29 wrote 128212 rows to validation/results/step10_vs_b/results.tsv.gz

```

## [28] compare_results (`/gpfs/home6/mvanvugt/projects/lipid_adem/validation/compare_results.py --left validation/ref/61e2d7b/step10_variant_bin.results.tsv.gz --left-format new --right /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/marvel_f1a3a8a/f1a3a8a_variant_bin.results.tsv.gz --right-format new --rtol 1e-6 --out-dir /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1`)
- first run: 2026-10-26 11:32:16
- last run: 2026-11-04 15:31:04
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-11-04 15:30:56 step10_variant_bin.results.tsv.gz: 678395 rows, 244190 kept
[warn]  2026-11-04 15:30:56 left: 24398 duplicate key/outcome/model row(s), first kept
[info]  2026-11-04 15:30:56 left: 219792 rows, 9158 keys, outcomes ['Apolipoprotein A_i0', 'Apolipoprotein B_i0', 'HDL cholesterol_i0', 'LDL direct_i0', 'Triglycerides_i0', 'all_cause_dementia_algo', 'all_cause_dementia_combined', 'alzheimers_disease_algo', 'alzheimers_disease_combined', 'ascvd_ii', 'frontotemporal_dementia_algo', 'vascular_dementia_algo'], models ['adjusted', 'unadjusted']
[info]  2026-11-04 15:31:00 f1a3a8a_variant_bin.results.tsv.gz: 678395 rows, 244190 kept
[warn]  2026-11-04 15:31:00 right: 24398 duplicate key/outcome/model row(s), first kept
[info]  2026-11-04 15:31:00 right: 219792 rows, 9158 keys, outcomes ['Apolipoprotein A_i0', 'Apolipoprotein B_i0', 'HDL cholesterol_i0', 'LDL direct_i0', 'Triglycerides_i0', 'all_cause_dementia_algo', 'all_cause_dementia_combined', 'alzheimers_disease_algo', 'alzheimers_disease_combined', 'ascvd_ii', 'frontotemporal_dementia_algo', 'vascular_dementia_algo'], models ['adjusted', 'unadjusted']
[info]  2026-11-04 15:31:00 rows per class: {'identical': 219792}
[info]  2026-11-04 15:31:00 GATE PASS
[info]  2026-11-04 15:31:04 wrote 219792 rows to /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1/rows.tsv.gz
[info]  2026-11-04 15:31:04 wrote 168 rows to /scratch-local/mvanvugt.28896425/tmp.3SeI2ER2TM/task_1/summary.tsv.gz

```

## [29] compare_carriers (`validation/compare_carriers.py --old-carriers /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step6b/{gene}_carriers.tsv.gz --run-dir /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a --new-list validation/configs/validation_variants.tsv --genes CETP PCSK9 --out-dir validation/results/step8_carriers_8a --lost-out /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a_lost_carriers.tsv.gz`)
- first run: 2026-10-30 14:05:37
- last run: 2026-10-30 16:04:05
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-30 16:03:49 148 variants in new list validation/configs/validation_variants.tsv
[info]  2026-10-30 16:03:50 chunk ukb_CETP_chr16_plink: 58 variant(s) read, 469835 samples
[info]  2026-10-30 16:03:50 chunk ukb_PCSK9_chr1_plink: 72 variant(s) read, 469835 samples
[info]  2026-10-30 16:03:51 chunk vep_chr1: 0 variant(s) read, 377567 samples
[info]  2026-10-30 16:03:51 chunk vep_chr16: 0 variant(s) read, 377567 samples
[info]  2026-10-30 16:03:51 CETP: 472 variant column(s) in CETP_carriers.tsv.gz, 58 in the new list
[info]  2026-10-30 16:03:56 CETP: chunk ukb_CETP_chr16_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 CETP: chunk ukb_PCSK9_chr1_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 CETP: chunk vep_chr1: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 CETP: chunk vep_chr16: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:03:56 wrote 58 rows to validation/results/step8_carriers_8a/CETP.carriers.tsv.gz
[info]  2026-10-30 16:03:56 CETP: 58 compared key(s), 58 identical; match {'exact': 58}; 0 read key(s) without an old column
[info]  2026-10-30 16:03:56 CETP: carrier changes (summed over keys) {'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0, 'n_gained': 0, 'n_gained_old_missing': 0, 'n_gained_not_in_old': 0}
[info]  2026-10-30 16:03:56 PCSK9: 622 variant column(s) in PCSK9_carriers.tsv.gz, 72 in the new list
[info]  2026-10-30 16:04:04 PCSK9: chunk ukb_CETP_chr16_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:04 PCSK9: chunk ukb_PCSK9_chr1_plink: 469835 samples, 469835 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:05 PCSK9: chunk vep_chr1: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:05 PCSK9: chunk vep_chr16: 377567 samples, 377567 of the 469835 old ones, 0 not in the old file
[info]  2026-10-30 16:04:05 wrote 72 rows to validation/results/step8_carriers_8a/PCSK9.carriers.tsv.gz
[info]  2026-10-30 16:04:05 PCSK9: 72 compared key(s), 72 identical; match {'exact': 72}; 0 read key(s) without an old column
[info]  2026-10-30 16:04:05 PCSK9: carrier changes (summed over keys) {'n_lost_non_carrier': 0, 'n_lost_missing': 0, 'n_lost_not_sampled': 0, 'n_lost_not_read': 0, 'n_gained': 0, 'n_gained_old_missing': 0, 'n_gained_not_in_old': 0}
[info]  2026-10-30 16:04:05 wrote 0 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a_lost_carriers.tsv.gz
[info]  2026-10-30 16:04:05 lost carrier IDs (individual-level) in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step8/8a_lost_carriers.tsv.gz

```

## [30] merge_associations (`/home/mvanvugt/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-27 17:32:09
- commit: `23ebede` (dirty)

Output:
```text
[stage] 2026-10-27 16:58:30 load_sumstats
[info]  2026-10-27 16:58:32 summary-stats: 125 files, 595475 rows incl. one copy per outcome (0 missing)
[info]  2026-10-27 16:58:39 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-27 16:58:39 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-27 16:58:39 marvel
[info]  2026-10-27 16:58:41 marvel ukb apoa: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:41 marvel ukb apoa: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:41 marvel ukb apoa: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:41 marvel ukb apob: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:41 marvel ukb apob: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:41 marvel ukb apob: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb hdl_c: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb hdl_c: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb hdl_c: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb ldl_c: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb ldl_c: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb ldl_c: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb tg: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb tg: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb tg: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb all_cause_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb all_cause_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb all_cause_dementia: 34 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb all_cause_dementia: 1079 rows -> 74 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb all_cause_dementia: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb alzheimers_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb alzheimers_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb alzheimers_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb alzheimers_dementia: 1173 rows -> 69 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb alzheimers_dementia: 1082 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb vascular_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb vascular_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb vascular_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb vascular_dementia: 1074 rows -> 69 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb vascular_dementia: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:42 marvel ukb frontotemporal_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb frontotemporal_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:42 marvel ukb frontotemporal_dementia: 49 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb frontotemporal_dementia: 1064 rows -> 64 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb frontotemporal_dementia: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:43 marvel ukb ascvd: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb ascvd: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb ascvd: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb ascvd: 1102 rows -> 97 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb ascvd: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:43 marvel ukb apoa: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb apoa: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb apoa: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:43 marvel ukb apob: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb apob: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb apob: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:43 marvel ukb hdl_c: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb hdl_c: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb hdl_c: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:43 marvel ukb ldl_c: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb ldl_c: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb ldl_c: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:43 marvel ukb tg: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb tg: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:43 marvel ukb tg: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb all_cause_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb all_cause_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb all_cause_dementia: 41 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb all_cause_dementia: 2429 rows -> 15 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb all_cause_dementia: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb alzheimers_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb alzheimers_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb alzheimers_dementia: 50 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb alzheimers_dementia: 2519 rows -> 11 variant rows, 12 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb alzheimers_dementia: 2496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb vascular_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb vascular_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb vascular_dementia: 56 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb vascular_dementia: 2414 rows -> 6 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb vascular_dementia: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb frontotemporal_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb frontotemporal_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb frontotemporal_dementia: 60 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb frontotemporal_dementia: 2410 rows -> 2 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb frontotemporal_dementia: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb ascvd: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb ascvd: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb ascvd: 32 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb ascvd: 2438 rows -> 19 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb ascvd: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb apoa: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb apoa: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb apoa: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:44 marvel ukb apob: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb apob: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:44 marvel ukb apob: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb hdl_c: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb hdl_c: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb hdl_c: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb ldl_c: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb ldl_c: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb ldl_c: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb tg: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb tg: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb tg: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb all_cause_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb all_cause_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb all_cause_dementia: 77 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb all_cause_dementia: 1741 rows -> 42 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb all_cause_dementia: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb alzheimers_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb alzheimers_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb alzheimers_dementia: 88 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb alzheimers_dementia: 1829 rows -> 31 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb alzheimers_dementia: 1776 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb vascular_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb vascular_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb vascular_dementia: 94 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb vascular_dementia: 1724 rows -> 25 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb vascular_dementia: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:45 marvel ukb frontotemporal_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb frontotemporal_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:45 marvel ukb frontotemporal_dementia: 103 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb frontotemporal_dementia: 1715 rows -> 21 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb frontotemporal_dementia: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:46 marvel ukb ascvd: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb ascvd: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb ascvd: 50 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb ascvd: 1768 rows -> 69 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb ascvd: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:46 marvel ukb apoa: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb apoa: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb apoa: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:46 marvel ukb apob: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb apob: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb apob: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:46 marvel ukb hdl_c: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb hdl_c: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb hdl_c: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:46 marvel ukb ldl_c: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb ldl_c: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb ldl_c: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:46 marvel ukb tg: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb tg: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:46 marvel ukb tg: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:47 marvel ukb all_cause_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb all_cause_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb all_cause_dementia: 65 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb all_cause_dementia: 1427 rows -> 56 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb all_cause_dementia: 1360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:47 marvel ukb alzheimers_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb alzheimers_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb alzheimers_dementia: 74 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb alzheimers_dementia: 1517 rows -> 49 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb alzheimers_dementia: 1448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:47 marvel ukb vascular_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb vascular_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb vascular_dementia: 74 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb vascular_dementia: 1418 rows -> 47 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb vascular_dementia: 1360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:47 marvel ukb frontotemporal_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb frontotemporal_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb frontotemporal_dementia: 91 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb frontotemporal_dementia: 1401 rows -> 41 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb frontotemporal_dementia: 1360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:47 marvel ukb ascvd: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb ascvd: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb ascvd: 30 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb ascvd: 1462 rows -> 90 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb ascvd: 1361 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:47 marvel ukb apoa: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb apoa: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:47 marvel ukb apoa: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb apob: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb apob: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb apob: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb hdl_c: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb hdl_c: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb hdl_c: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb ldl_c: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb ldl_c: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb ldl_c: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb tg: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb tg: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb tg: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb all_cause_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb all_cause_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb all_cause_dementia: 99 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb all_cause_dementia: 1974 rows -> 11 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb all_cause_dementia: 1952 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb alzheimers_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb alzheimers_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb alzheimers_dementia: 104 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb alzheimers_dementia: 2068 rows -> 8 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb alzheimers_dementia: 2040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:48 marvel ukb vascular_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb vascular_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb vascular_dementia: 111 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb vascular_dementia: 1962 rows -> 10 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:48 marvel ukb vascular_dementia: 1952 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:49 marvel ukb frontotemporal_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb frontotemporal_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb frontotemporal_dementia: 117 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb frontotemporal_dementia: 1956 rows -> 4 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb frontotemporal_dementia: 1952 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:49 marvel ukb ascvd: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb ascvd: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb ascvd: 68 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb ascvd: 2005 rows -> 41 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb ascvd: 1953 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:49 marvel ukb apoa: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb apoa: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb apoa: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:49 marvel ukb apob: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb apob: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb apob: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:49 marvel ukb hdl_c: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb hdl_c: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb hdl_c: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:49 marvel ukb ldl_c: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb ldl_c: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:49 marvel ukb ldl_c: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb tg: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb tg: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb tg: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb all_cause_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb all_cause_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb all_cause_dementia: 86 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb all_cause_dementia: 1635 rows -> 70 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb all_cause_dementia: 1554 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb alzheimers_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb alzheimers_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb alzheimers_dementia: 94 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb alzheimers_dementia: 1726 rows -> 62 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb alzheimers_dementia: 1642 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb vascular_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb vascular_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb vascular_dementia: 100 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb vascular_dementia: 1621 rows -> 57 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb vascular_dementia: 1553 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb frontotemporal_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb frontotemporal_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb frontotemporal_dementia: 112 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb frontotemporal_dementia: 1609 rows -> 50 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb frontotemporal_dementia: 1553 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb ascvd: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb ascvd: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb ascvd: 53 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb ascvd: 1668 rows -> 103 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb ascvd: 1554 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:50 marvel ukb apoa: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb apoa: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:50 marvel ukb apoa: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:51 marvel ukb apob: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb apob: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb apob: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:51 marvel ukb hdl_c: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb hdl_c: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb hdl_c: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:51 marvel ukb ldl_c: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb ldl_c: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb ldl_c: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:51 marvel ukb tg: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb tg: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb tg: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:51 marvel ukb all_cause_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb all_cause_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb all_cause_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb all_cause_dementia: 2465 rows -> 11 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb all_cause_dementia: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:51 marvel ukb alzheimers_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb alzheimers_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb alzheimers_dementia: 48 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb alzheimers_dementia: 2555 rows -> 7 variant rows, 12 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:51 marvel ukb alzheimers_dementia: 2536 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb vascular_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb vascular_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb vascular_dementia: 51 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb vascular_dementia: 2453 rows -> 5 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb vascular_dementia: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb frontotemporal_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb frontotemporal_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb frontotemporal_dementia: 54 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb frontotemporal_dementia: 2450 rows -> 2 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb frontotemporal_dementia: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb ascvd: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb ascvd: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb ascvd: 31 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb ascvd: 2473 rows -> 14 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb ascvd: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb apoa: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb apoa: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb apoa: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb apob: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb apob: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb apob: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb hdl_c: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb hdl_c: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb hdl_c: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:52 marvel ukb ldl_c: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb ldl_c: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:52 marvel ukb ldl_c: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb tg: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb tg: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb tg: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb all_cause_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb all_cause_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb all_cause_dementia: 87 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb all_cause_dementia: 1978 rows -> 38 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb all_cause_dementia: 1929 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb alzheimers_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb alzheimers_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb alzheimers_dementia: 96 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb alzheimers_dementia: 2068 rows -> 29 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb alzheimers_dementia: 2017 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb vascular_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb vascular_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb vascular_dementia: 106 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb vascular_dementia: 1959 rows -> 20 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb vascular_dementia: 1928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb frontotemporal_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb frontotemporal_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb frontotemporal_dementia: 114 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb frontotemporal_dementia: 1951 rows -> 17 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb frontotemporal_dementia: 1928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb ascvd: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb ascvd: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb ascvd: 60 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb ascvd: 2005 rows -> 65 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:53 marvel ukb ascvd: 1929 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:53 marvel ukb apoa: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb apoa: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb apoa: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:54 marvel ukb apob: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb apob: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb apob: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:54 marvel ukb hdl_c: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb hdl_c: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb hdl_c: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:54 marvel ukb ldl_c: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb ldl_c: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb ldl_c: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:54 marvel ukb tg: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb tg: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb tg: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:54 marvel ukb all_cause_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb all_cause_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb all_cause_dementia: 96 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb all_cause_dementia: 1900 rows -> 49 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb all_cause_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:54 marvel ukb alzheimers_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb alzheimers_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb alzheimers_dementia: 109 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb alzheimers_dementia: 1986 rows -> 38 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:54 marvel ukb alzheimers_dementia: 1928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb vascular_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb vascular_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb vascular_dementia: 104 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb vascular_dementia: 1892 rows -> 41 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb vascular_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb frontotemporal_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb frontotemporal_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb frontotemporal_dementia: 123 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb frontotemporal_dementia: 1873 rows -> 33 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb frontotemporal_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb ascvd: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb ascvd: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb ascvd: 54 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb ascvd: 1942 rows -> 90 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb ascvd: 1841 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb apoa: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb apoa: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb apoa: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb apob: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb apob: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb apob: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb hdl_c: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb hdl_c: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb hdl_c: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:55 marvel ukb ldl_c: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb ldl_c: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:55 marvel ukb ldl_c: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:56 marvel ukb tg: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb tg: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb tg: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:56 marvel ukb all_cause_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb all_cause_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb all_cause_dementia: 102 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb all_cause_dementia: 2125 rows -> 11 variant rows, 10 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb all_cause_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:56 marvel ukb alzheimers_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb alzheimers_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb alzheimers_dementia: 126 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb alzheimers_dementia: 2200 rows -> 8 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb alzheimers_dementia: 2192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:56 marvel ukb vascular_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb vascular_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb vascular_dementia: 116 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb vascular_dementia: 2111 rows -> 7 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb vascular_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:56 marvel ukb frontotemporal_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb frontotemporal_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb frontotemporal_dementia: 119 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb frontotemporal_dementia: 2108 rows -> 4 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb frontotemporal_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:58:56 marvel ukb ascvd: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb ascvd: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb ascvd: 68 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb ascvd: 2159 rows -> 43 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 16:58:56 marvel ukb ascvd: 2105 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:02 marvel ukb apoa: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:02 marvel ukb apoa: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:02 marvel ukb apoa: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:02 marvel ukb apob: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:02 marvel ukb apob: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:02 marvel ukb apob: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:02 marvel ukb hdl_c: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:02 marvel ukb hdl_c: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:02 marvel ukb hdl_c: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:02 marvel ukb ldl_c: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb ldl_c: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb ldl_c: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:03 marvel ukb tg: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb tg: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb tg: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:03 marvel ukb all_cause_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb all_cause_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb all_cause_dementia: 43 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb all_cause_dementia: 2706 rows -> 160 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb all_cause_dementia: 2536 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:03 marvel ukb alzheimers_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb alzheimers_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb alzheimers_dementia: 67 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb alzheimers_dementia: 2790 rows -> 147 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:03 marvel ukb alzheimers_dementia: 2623 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:04 marvel ukb vascular_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb vascular_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb vascular_dementia: 64 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb vascular_dementia: 2685 rows -> 142 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb vascular_dementia: 2533 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:04 marvel ukb frontotemporal_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb frontotemporal_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb frontotemporal_dementia: 98 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb frontotemporal_dementia: 2651 rows -> 122 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb frontotemporal_dementia: 2522 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:04 marvel ukb ascvd: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb ascvd: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb ascvd: 18 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb ascvd: 2731 rows -> 178 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb ascvd: 2541 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:04 marvel ukb apoa: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb apoa: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:04 marvel ukb apoa: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:05 marvel ukb apob: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:05 marvel ukb apob: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:05 marvel ukb apob: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:05 marvel ukb hdl_c: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:05 marvel ukb hdl_c: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:05 marvel ukb hdl_c: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:05 marvel ukb ldl_c: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:05 marvel ukb ldl_c: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:05 marvel ukb ldl_c: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:05 marvel ukb tg: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb tg: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb tg: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:06 marvel ukb all_cause_dementia: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb all_cause_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb all_cause_dementia: 55 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb all_cause_dementia: 4817 rows -> 45 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb all_cause_dementia: 4765 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:06 marvel ukb alzheimers_dementia: 774 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb alzheimers_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb alzheimers_dementia: 66 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb alzheimers_dementia: 4896 rows -> 37 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb alzheimers_dementia: 4845 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:06 marvel ukb vascular_dementia: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb vascular_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb vascular_dementia: 80 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb vascular_dementia: 4792 rows -> 32 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:06 marvel ukb vascular_dementia: 4759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:07 marvel ukb frontotemporal_dementia: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb frontotemporal_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb frontotemporal_dementia: 89 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb frontotemporal_dementia: 4783 rows -> 24 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb frontotemporal_dementia: 4758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:07 marvel ukb ascvd: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb ascvd: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb ascvd: 52 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb ascvd: 4820 rows -> 45 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb ascvd: 4768 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:07 marvel ukb apoa: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb apoa: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:07 marvel ukb apoa: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:08 marvel ukb apob: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb apob: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb apob: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:08 marvel ukb hdl_c: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb hdl_c: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb hdl_c: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:08 marvel ukb ldl_c: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb ldl_c: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb ldl_c: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:08 marvel ukb tg: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb tg: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:08 marvel ukb tg: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:09 marvel ukb all_cause_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb all_cause_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb all_cause_dementia: 154 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb all_cause_dementia: 3746 rows -> 87 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb all_cause_dementia: 3649 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:09 marvel ukb alzheimers_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb alzheimers_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb alzheimers_dementia: 165 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb alzheimers_dementia: 3843 rows -> 79 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb alzheimers_dementia: 3744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:09 marvel ukb vascular_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb vascular_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb vascular_dementia: 192 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb vascular_dementia: 3708 rows -> 64 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb vascular_dementia: 3643 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:09 marvel ukb frontotemporal_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb frontotemporal_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb frontotemporal_dementia: 208 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb frontotemporal_dementia: 3692 rows -> 49 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:09 marvel ukb frontotemporal_dementia: 3642 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:10 marvel ukb ascvd: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb ascvd: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb ascvd: 94 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb ascvd: 3806 rows -> 126 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb ascvd: 3670 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:10 marvel ukb apoa: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb apoa: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb apoa: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:10 marvel ukb apob: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb apob: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:10 marvel ukb apob: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:11 marvel ukb hdl_c: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb hdl_c: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb hdl_c: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:11 marvel ukb ldl_c: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb ldl_c: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb ldl_c: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:11 marvel ukb tg: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb tg: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb tg: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:11 marvel ukb all_cause_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb all_cause_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb all_cause_dementia: 105 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb all_cause_dementia: 3142 rows -> 128 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:11 marvel ukb all_cause_dementia: 3004 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:12 marvel ukb alzheimers_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb alzheimers_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb alzheimers_dementia: 153 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb alzheimers_dementia: 3202 rows -> 110 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb alzheimers_dementia: 3090 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:12 marvel ukb vascular_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb vascular_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb vascular_dementia: 125 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb vascular_dementia: 3122 rows -> 113 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb vascular_dementia: 3002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:12 marvel ukb frontotemporal_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb frontotemporal_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb frontotemporal_dementia: 149 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb frontotemporal_dementia: 3098 rows -> 99 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:12 marvel ukb frontotemporal_dementia: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:13 marvel ukb ascvd: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb ascvd: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb ascvd: 58 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb ascvd: 3189 rows -> 161 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb ascvd: 3016 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:13 marvel ukb apoa: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb apoa: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb apoa: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:13 marvel ukb apob: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb apob: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:13 marvel ukb apob: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:13 marvel ukb hdl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb hdl_c: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb hdl_c: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:14 marvel ukb ldl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb ldl_c: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb ldl_c: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:14 marvel ukb tg: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb tg: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb tg: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:14 marvel ukb all_cause_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb all_cause_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb all_cause_dementia: 168 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb all_cause_dementia: 4004 rows -> 56 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:14 marvel ukb all_cause_dementia: 3941 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:15 marvel ukb alzheimers_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb alzheimers_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb alzheimers_dementia: 198 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb alzheimers_dementia: 4082 rows -> 46 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb alzheimers_dementia: 4034 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:15 marvel ukb vascular_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb vascular_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb vascular_dementia: 185 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb vascular_dementia: 3987 rows -> 42 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb vascular_dementia: 3938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:15 marvel ukb frontotemporal_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb frontotemporal_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb frontotemporal_dementia: 202 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb frontotemporal_dementia: 3970 rows -> 32 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb frontotemporal_dementia: 3937 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:15 marvel ukb ascvd: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb ascvd: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb ascvd: 113 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb ascvd: 4059 rows -> 87 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:15 marvel ukb ascvd: 3960 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:16 marvel ukb apoa: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:16 marvel ukb apoa: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:16 marvel ukb apoa: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:16 marvel ukb apob: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:16 marvel ukb apob: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:16 marvel ukb apob: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:16 marvel ukb hdl_c: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:16 marvel ukb hdl_c: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:16 marvel ukb hdl_c: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:17 marvel ukb ldl_c: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb ldl_c: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb ldl_c: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:17 marvel ukb tg: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb tg: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb tg: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:17 marvel ukb all_cause_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb all_cause_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb all_cause_dementia: 161 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb all_cause_dementia: 3704 rows -> 129 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:17 marvel ukb all_cause_dementia: 3565 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:17 marvel ukb alzheimers_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb alzheimers_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb alzheimers_dementia: 183 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb alzheimers_dementia: 3790 rows -> 117 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb alzheimers_dementia: 3653 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:18 marvel ukb vascular_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb vascular_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb vascular_dementia: 183 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb vascular_dementia: 3682 rows -> 112 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb vascular_dementia: 3560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:18 marvel ukb frontotemporal_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb frontotemporal_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb frontotemporal_dementia: 209 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb frontotemporal_dementia: 3656 rows -> 96 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb frontotemporal_dementia: 3553 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:18 marvel ukb ascvd: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb ascvd: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb ascvd: 80 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb ascvd: 3785 rows -> 175 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:18 marvel ukb ascvd: 3598 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:19 marvel ukb apoa: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:19 marvel ukb apoa: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:19 marvel ukb apoa: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:19 marvel ukb apob: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:19 marvel ukb apob: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:19 marvel ukb apob: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:19 marvel ukb hdl_c: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:19 marvel ukb hdl_c: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:19 marvel ukb hdl_c: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:19 marvel ukb ldl_c: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb ldl_c: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb ldl_c: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:20 marvel ukb tg: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb tg: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb tg: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:20 marvel ukb all_cause_dementia: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb all_cause_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb all_cause_dementia: 53 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb all_cause_dementia: 4866 rows -> 31 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb all_cause_dementia: 4828 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:20 marvel ukb alzheimers_dementia: 702 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb alzheimers_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb alzheimers_dementia: 63 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb alzheimers_dementia: 4946 rows -> 25 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:20 marvel ukb alzheimers_dementia: 4907 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:21 marvel ukb vascular_dementia: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb vascular_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb vascular_dementia: 73 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb vascular_dementia: 4846 rows -> 23 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb vascular_dementia: 4822 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:21 marvel ukb frontotemporal_dementia: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb frontotemporal_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb frontotemporal_dementia: 77 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb frontotemporal_dementia: 4842 rows -> 19 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb frontotemporal_dementia: 4822 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:21 marvel ukb ascvd: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb ascvd: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb ascvd: 47 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb ascvd: 4872 rows -> 33 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:21 marvel ukb ascvd: 4832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:21 marvel ukb apoa: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb apoa: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb apoa: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:22 marvel ukb apob: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb apob: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb apob: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:22 marvel ukb hdl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb hdl_c: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb hdl_c: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:22 marvel ukb ldl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb ldl_c: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:22 marvel ukb ldl_c: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:23 marvel ukb tg: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb tg: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb tg: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:23 marvel ukb all_cause_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb all_cause_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb all_cause_dementia: 162 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb all_cause_dementia: 4027 rows -> 67 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb all_cause_dementia: 3950 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:23 marvel ukb alzheimers_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb alzheimers_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb alzheimers_dementia: 179 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb alzheimers_dementia: 4118 rows -> 58 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb alzheimers_dementia: 4046 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:23 marvel ukb vascular_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb vascular_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb vascular_dementia: 189 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb vascular_dementia: 4000 rows -> 53 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:23 marvel ukb vascular_dementia: 3946 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:24 marvel ukb frontotemporal_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb frontotemporal_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb frontotemporal_dementia: 203 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb frontotemporal_dementia: 3986 rows -> 39 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb frontotemporal_dementia: 3946 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:24 marvel ukb ascvd: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb ascvd: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb ascvd: 92 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb ascvd: 4097 rows -> 115 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb ascvd: 3972 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:24 marvel ukb apoa: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb apoa: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:24 marvel ukb apoa: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:25 marvel ukb apob: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb apob: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb apob: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:25 marvel ukb hdl_c: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb hdl_c: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb hdl_c: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:25 marvel ukb ldl_c: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb ldl_c: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb ldl_c: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:25 marvel ukb tg: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:25 marvel ukb tg: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb tg: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:26 marvel ukb all_cause_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb all_cause_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb all_cause_dementia: 178 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb all_cause_dementia: 3771 rows -> 102 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb all_cause_dementia: 3659 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:26 marvel ukb alzheimers_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb alzheimers_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb alzheimers_dementia: 223 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb alzheimers_dementia: 3834 rows -> 86 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb alzheimers_dementia: 3746 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:26 marvel ukb vascular_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb vascular_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb vascular_dementia: 202 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb vascular_dementia: 3747 rows -> 86 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:26 marvel ukb vascular_dementia: 3654 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:27 marvel ukb frontotemporal_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb frontotemporal_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb frontotemporal_dementia: 216 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb frontotemporal_dementia: 3733 rows -> 78 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb frontotemporal_dementia: 3648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:27 marvel ukb ascvd: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb ascvd: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb ascvd: 113 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb ascvd: 3836 rows -> 141 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb ascvd: 3683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:27 marvel ukb apoa: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb apoa: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb apoa: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:27 marvel ukb apob: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb apob: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:27 marvel ukb apob: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:28 marvel ukb hdl_c: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:28 marvel ukb hdl_c: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:28 marvel ukb hdl_c: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:28 marvel ukb ldl_c: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:28 marvel ukb ldl_c: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:28 marvel ukb ldl_c: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:28 marvel ukb tg: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:28 marvel ukb tg: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:28 marvel ukb tg: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:29 marvel ukb all_cause_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb all_cause_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb all_cause_dementia: 157 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb all_cause_dementia: 4256 rows -> 45 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb all_cause_dementia: 4204 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:29 marvel ukb alzheimers_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb alzheimers_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb alzheimers_dementia: 183 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb alzheimers_dementia: 4338 rows -> 38 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb alzheimers_dementia: 4298 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:29 marvel ukb vascular_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb vascular_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb vascular_dementia: 169 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb vascular_dementia: 4244 rows -> 36 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb vascular_dementia: 4201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:29 marvel ukb frontotemporal_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb frontotemporal_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb frontotemporal_dementia: 180 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb frontotemporal_dementia: 4233 rows -> 31 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:29 marvel ukb frontotemporal_dementia: 4201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:30 marvel ukb ascvd: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:30 marvel ukb ascvd: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:30 marvel ukb ascvd: 100 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:30 marvel ukb ascvd: 4313 rows -> 76 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 16:59:30 marvel ukb ascvd: 4225 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:35 marvel ukb apoa: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb apoa: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb apoa: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:36 marvel ukb apob: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb apob: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb apob: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:36 marvel ukb hdl_c: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb hdl_c: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb hdl_c: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:36 marvel ukb ldl_c: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb ldl_c: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:36 marvel ukb ldl_c: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:37 marvel ukb tg: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb tg: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb tg: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:37 marvel ukb all_cause_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb all_cause_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb all_cause_dementia: 54 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb all_cause_dementia: 1486 rows -> 87 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb all_cause_dementia: 1390 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:37 marvel ukb alzheimers_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb alzheimers_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb alzheimers_dementia: 59 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb alzheimers_dementia: 1580 rows -> 84 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:37 marvel ukb alzheimers_dementia: 1478 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:38 marvel ukb vascular_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb vascular_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb vascular_dementia: 68 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb vascular_dementia: 1472 rows -> 79 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb vascular_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:38 marvel ukb frontotemporal_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb frontotemporal_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb frontotemporal_dementia: 75 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb frontotemporal_dementia: 1465 rows -> 75 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb frontotemporal_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:38 marvel ukb ascvd: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb ascvd: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb ascvd: 16 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb ascvd: 1524 rows -> 101 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:38 marvel ukb ascvd: 1412 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:38 marvel ukb apoa: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb apoa: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb apoa: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:39 marvel ukb apob: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb apob: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb apob: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:39 marvel ukb hdl_c: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb hdl_c: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb hdl_c: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:39 marvel ukb ldl_c: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb ldl_c: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:39 marvel ukb ldl_c: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:40 marvel ukb tg: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb tg: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb tg: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:40 marvel ukb all_cause_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb all_cause_dementia: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb all_cause_dementia: 161 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb all_cause_dementia: 5588 rows -> 25 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb all_cause_dementia: 5557 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:40 marvel ukb alzheimers_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb alzheimers_dementia: 475 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb alzheimers_dementia: 185 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb alzheimers_dementia: 5658 rows -> 18 variant rows, 12 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:40 marvel ukb alzheimers_dementia: 5628 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:41 marvel ukb vascular_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb vascular_dementia: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb vascular_dementia: 215 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb vascular_dementia: 5534 rows -> 6 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb vascular_dementia: 5528 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:41 marvel ukb frontotemporal_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb frontotemporal_dementia: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb frontotemporal_dementia: 220 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb frontotemporal_dementia: 5529 rows -> 1 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb frontotemporal_dementia: 5528 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:41 marvel ukb ascvd: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb ascvd: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb ascvd: 154 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb ascvd: 5595 rows -> 32 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb ascvd: 5557 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:41 marvel ukb apoa: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb apoa: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:41 marvel ukb apoa: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:42 marvel ukb apob: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:42 marvel ukb apob: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:42 marvel ukb apob: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:42 marvel ukb hdl_c: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:42 marvel ukb hdl_c: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:42 marvel ukb hdl_c: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:42 marvel ukb ldl_c: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:42 marvel ukb ldl_c: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:42 marvel ukb ldl_c: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:43 marvel ukb tg: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb tg: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb tg: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:43 marvel ukb all_cause_dementia: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb all_cause_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb all_cause_dementia: 213 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb all_cause_dementia: 3892 rows -> 60 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb all_cause_dementia: 3823 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:43 marvel ukb alzheimers_dementia: 2286 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb alzheimers_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb alzheimers_dementia: 242 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb alzheimers_dementia: 3944 rows -> 44 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:43 marvel ukb alzheimers_dementia: 3882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:44 marvel ukb vascular_dementia: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb vascular_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb vascular_dementia: 276 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb vascular_dementia: 3829 rows -> 30 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb vascular_dementia: 3790 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:44 marvel ukb frontotemporal_dementia: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb frontotemporal_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb frontotemporal_dementia: 294 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb frontotemporal_dementia: 3811 rows -> 19 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb frontotemporal_dementia: 3792 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:44 marvel ukb ascvd: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb ascvd: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb ascvd: 135 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb ascvd: 3970 rows -> 108 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:44 marvel ukb ascvd: 3853 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:45 marvel ukb apoa: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb apoa: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb apoa: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:45 marvel ukb apob: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb apob: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb apob: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:45 marvel ukb hdl_c: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb hdl_c: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb hdl_c: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:45 marvel ukb ldl_c: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb ldl_c: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:45 marvel ukb ldl_c: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:46 marvel ukb tg: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb tg: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb tg: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:46 marvel ukb all_cause_dementia: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb all_cause_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb all_cause_dementia: 172 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb all_cause_dementia: 2674 rows -> 61 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb all_cause_dementia: 2604 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:46 marvel ukb alzheimers_dementia: 3636 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb alzheimers_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb alzheimers_dementia: 216 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb alzheimers_dementia: 2720 rows -> 50 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:46 marvel ukb alzheimers_dementia: 2670 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:47 marvel ukb vascular_dementia: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb vascular_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb vascular_dementia: 209 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb vascular_dementia: 2637 rows -> 47 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb vascular_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:47 marvel ukb frontotemporal_dementia: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb frontotemporal_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb frontotemporal_dementia: 214 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb frontotemporal_dementia: 2632 rows -> 42 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb frontotemporal_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:47 marvel ukb ascvd: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb ascvd: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb ascvd: 74 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb ascvd: 2772 rows -> 105 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:47 marvel ukb ascvd: 2657 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:47 marvel ukb apoa: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb apoa: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb apoa: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:48 marvel ukb apob: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb apob: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb apob: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:48 marvel ukb hdl_c: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb hdl_c: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb hdl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:48 marvel ukb ldl_c: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb ldl_c: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:48 marvel ukb ldl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:49 marvel ukb tg: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb tg: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb tg: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:49 marvel ukb all_cause_dementia: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb all_cause_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb all_cause_dementia: 285 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb all_cause_dementia: 4536 rows -> 27 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb all_cause_dementia: 4503 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:49 marvel ukb alzheimers_dementia: 1494 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb alzheimers_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb alzheimers_dementia: 326 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb alzheimers_dementia: 4576 rows -> 16 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:49 marvel ukb alzheimers_dementia: 4560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:50 marvel ukb vascular_dementia: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb vascular_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb vascular_dementia: 313 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb vascular_dementia: 4508 rows -> 12 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb vascular_dementia: 4496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:50 marvel ukb frontotemporal_dementia: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb frontotemporal_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb frontotemporal_dementia: 324 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb frontotemporal_dementia: 4497 rows -> 9 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb frontotemporal_dementia: 4488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:50 marvel ukb ascvd: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb ascvd: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb ascvd: 180 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb ascvd: 4641 rows -> 80 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:50 marvel ukb ascvd: 4552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:51 marvel ukb apoa: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb apoa: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb apoa: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:51 marvel ukb apob: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb apob: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb apob: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:51 marvel ukb hdl_c: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb hdl_c: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb hdl_c: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:51 marvel ukb ldl_c: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb ldl_c: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:51 marvel ukb ldl_c: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:52 marvel ukb tg: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb tg: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb tg: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:52 marvel ukb all_cause_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb all_cause_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb all_cause_dementia: 133 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb all_cause_dementia: 2245 rows -> 78 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb all_cause_dementia: 2158 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:52 marvel ukb alzheimers_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb alzheimers_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb alzheimers_dementia: 140 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb alzheimers_dementia: 2337 rows -> 73 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:52 marvel ukb alzheimers_dementia: 2246 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:53 marvel ukb vascular_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb vascular_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb vascular_dementia: 155 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb vascular_dementia: 2223 rows -> 65 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb vascular_dementia: 2152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:53 marvel ukb frontotemporal_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb frontotemporal_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb frontotemporal_dementia: 162 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb frontotemporal_dementia: 2216 rows -> 58 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb frontotemporal_dementia: 2152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:53 marvel ukb ascvd: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb ascvd: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb ascvd: 60 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb ascvd: 2318 rows -> 117 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:53 marvel ukb ascvd: 2190 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:54 marvel ukb apoa: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb apoa: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb apoa: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:54 marvel ukb apob: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb apob: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb apob: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:54 marvel ukb hdl_c: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb hdl_c: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb hdl_c: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:54 marvel ukb ldl_c: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb ldl_c: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:54 marvel ukb ldl_c: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:55 marvel ukb tg: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb tg: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb tg: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:55 marvel ukb all_cause_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb all_cause_dementia: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb all_cause_dementia: 155 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb all_cause_dementia: 5636 rows -> 25 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb all_cause_dementia: 5605 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:55 marvel ukb alzheimers_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb alzheimers_dementia: 487 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb alzheimers_dementia: 179 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb alzheimers_dementia: 5706 rows -> 18 variant rows, 12 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:55 marvel ukb alzheimers_dementia: 5676 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:56 marvel ukb vascular_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb vascular_dementia: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb vascular_dementia: 209 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb vascular_dementia: 5582 rows -> 6 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb vascular_dementia: 5576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:56 marvel ukb frontotemporal_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb frontotemporal_dementia: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb frontotemporal_dementia: 214 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb frontotemporal_dementia: 5577 rows -> 1 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb frontotemporal_dementia: 5576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:56 marvel ukb ascvd: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb ascvd: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb ascvd: 150 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb ascvd: 5641 rows -> 30 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:56 marvel ukb ascvd: 5605 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:57 marvel ukb apoa: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:57 marvel ukb apoa: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:57 marvel ukb apoa: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:57 marvel ukb apob: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:57 marvel ukb apob: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:57 marvel ukb apob: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:57 marvel ukb hdl_c: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:57 marvel ukb hdl_c: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:57 marvel ukb hdl_c: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:57 marvel ukb ldl_c: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb ldl_c: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb ldl_c: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:58 marvel ukb tg: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb tg: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb tg: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:58 marvel ukb all_cause_dementia: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb all_cause_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb all_cause_dementia: 246 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb all_cause_dementia: 4334 rows -> 53 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb all_cause_dementia: 4272 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:58 marvel ukb alzheimers_dementia: 1782 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb alzheimers_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb alzheimers_dementia: 275 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb alzheimers_dementia: 4386 rows -> 37 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:58 marvel ukb alzheimers_dementia: 4331 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:59 marvel ukb vascular_dementia: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb vascular_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb vascular_dementia: 314 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb vascular_dementia: 4266 rows -> 22 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb vascular_dementia: 4238 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:59 marvel ukb frontotemporal_dementia: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb frontotemporal_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb frontotemporal_dementia: 327 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb frontotemporal_dementia: 4253 rows -> 13 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb frontotemporal_dementia: 4240 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 16:59:59 marvel ukb ascvd: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb ascvd: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb ascvd: 162 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb ascvd: 4418 rows -> 99 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 16:59:59 marvel ukb ascvd: 4310 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:00 marvel ukb apoa: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb apoa: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb apoa: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:00 marvel ukb apob: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb apob: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb apob: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:00 marvel ukb hdl_c: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb hdl_c: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb hdl_c: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:00 marvel ukb ldl_c: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb ldl_c: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:00 marvel ukb ldl_c: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:01 marvel ukb tg: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb tg: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb tg: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:01 marvel ukb all_cause_dementia: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb all_cause_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb all_cause_dementia: 228 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb all_cause_dementia: 3259 rows -> 54 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb all_cause_dementia: 3196 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:01 marvel ukb alzheimers_dementia: 2970 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb alzheimers_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb alzheimers_dementia: 271 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb alzheimers_dementia: 3306 rows -> 44 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:01 marvel ukb alzheimers_dementia: 3262 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:02 marvel ukb vascular_dementia: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb vascular_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb vascular_dementia: 265 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb vascular_dementia: 3222 rows -> 40 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb vascular_dementia: 3176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:02 marvel ukb frontotemporal_dementia: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb frontotemporal_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb frontotemporal_dementia: 270 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb frontotemporal_dementia: 3217 rows -> 35 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb frontotemporal_dementia: 3176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:02 marvel ukb ascvd: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb ascvd: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb ascvd: 112 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb ascvd: 3375 rows -> 112 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:02 marvel ukb ascvd: 3253 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:03 marvel ukb apoa: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb apoa: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb apoa: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:03 marvel ukb apob: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb apob: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb apob: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:03 marvel ukb hdl_c: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb hdl_c: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb hdl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:03 marvel ukb ldl_c: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb ldl_c: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:03 marvel ukb ldl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:04 marvel ukb tg: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb tg: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb tg: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:04 marvel ukb all_cause_dementia: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb all_cause_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb all_cause_dementia: 287 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb all_cause_dementia: 4726 rows -> 25 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb all_cause_dementia: 4695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:04 marvel ukb alzheimers_dementia: 1278 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb alzheimers_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb alzheimers_dementia: 327 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb alzheimers_dementia: 4767 rows -> 15 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:04 marvel ukb alzheimers_dementia: 4752 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:05 marvel ukb vascular_dementia: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb vascular_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb vascular_dementia: 315 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb vascular_dementia: 4698 rows -> 10 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb vascular_dementia: 4688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:05 marvel ukb frontotemporal_dementia: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb frontotemporal_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb frontotemporal_dementia: 326 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb frontotemporal_dementia: 4687 rows -> 7 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb frontotemporal_dementia: 4680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:05 marvel ukb ascvd: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb ascvd: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb ascvd: 183 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb ascvd: 4830 rows -> 77 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 17:00:05 marvel ukb ascvd: 4744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:15 marvel ukb apoa: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:15 marvel ukb apoa: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:15 marvel ukb apoa: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:15 marvel ukb apob: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:15 marvel ukb apob: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:15 marvel ukb apob: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:15 marvel ukb hdl_c: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:16 marvel ukb hdl_c: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:16 marvel ukb hdl_c: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:16 marvel ukb ldl_c: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:16 marvel ukb ldl_c: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:16 marvel ukb ldl_c: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:16 marvel ukb tg: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:16 marvel ukb tg: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:16 marvel ukb tg: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:17 marvel ukb all_cause_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb all_cause_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb all_cause_dementia: 197 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb all_cause_dementia: 4057 rows -> 187 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb all_cause_dementia: 3861 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:17 marvel ukb alzheimers_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb alzheimers_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb alzheimers_dementia: 227 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb alzheimers_dementia: 4108 rows -> 162 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:17 marvel ukb alzheimers_dementia: 3928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:18 marvel ukb vascular_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb vascular_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb vascular_dementia: 237 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb vascular_dementia: 4017 rows -> 151 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb vascular_dementia: 3857 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:18 marvel ukb frontotemporal_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb frontotemporal_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb frontotemporal_dementia: 259 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb frontotemporal_dementia: 3995 rows -> 129 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:18 marvel ukb frontotemporal_dementia: 3857 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:19 marvel ukb ascvd: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:19 marvel ukb ascvd: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:19 marvel ukb ascvd: 73 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:19 marvel ukb ascvd: 4181 rows -> 291 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:19 marvel ukb ascvd: 3881 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:19 marvel ukb apoa: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:19 marvel ukb apoa: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:19 marvel ukb apoa: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:20 marvel ukb apob: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:20 marvel ukb apob: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:20 marvel ukb apob: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:20 marvel ukb hdl_c: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:20 marvel ukb hdl_c: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:20 marvel ukb hdl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:21 marvel ukb ldl_c: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:21 marvel ukb ldl_c: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:21 marvel ukb ldl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:21 marvel ukb tg: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:21 marvel ukb tg: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:21 marvel ukb tg: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:22 marvel ukb all_cause_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb all_cause_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb all_cause_dementia: 37 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb all_cause_dementia: 8965 rows -> 36 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb all_cause_dementia: 8920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:22 marvel ukb alzheimers_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb alzheimers_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb alzheimers_dementia: 47 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb alzheimers_dementia: 9036 rows -> 32 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:22 marvel ukb alzheimers_dementia: 8992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:23 marvel ukb vascular_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb vascular_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb vascular_dementia: 59 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb vascular_dementia: 8943 rows -> 17 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb vascular_dementia: 8920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:23 marvel ukb frontotemporal_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb frontotemporal_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb frontotemporal_dementia: 78 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb frontotemporal_dementia: 8924 rows -> 4 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb frontotemporal_dementia: 8920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:23 marvel ukb ascvd: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb ascvd: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:23 marvel ukb ascvd: 29 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:24 marvel ukb ascvd: 8973 rows -> 43 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:24 marvel ukb ascvd: 8924 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:24 marvel ukb apoa: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:24 marvel ukb apoa: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:24 marvel ukb apoa: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:24 marvel ukb apob: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:24 marvel ukb apob: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:24 marvel ukb apob: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:25 marvel ukb hdl_c: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:25 marvel ukb hdl_c: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:25 marvel ukb hdl_c: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:25 marvel ukb ldl_c: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:25 marvel ukb ldl_c: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:25 marvel ukb ldl_c: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:26 marvel ukb tg: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:26 marvel ukb tg: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:26 marvel ukb tg: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:26 marvel ukb all_cause_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:26 marvel ukb all_cause_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:26 marvel ukb all_cause_dementia: 175 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:26 marvel ukb all_cause_dementia: 6624 rows -> 78 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:26 marvel ukb all_cause_dementia: 6537 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:27 marvel ukb alzheimers_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb alzheimers_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb alzheimers_dementia: 184 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb alzheimers_dementia: 6696 rows -> 69 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb alzheimers_dementia: 6609 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:27 marvel ukb vascular_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb vascular_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb vascular_dementia: 208 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb vascular_dementia: 6591 rows -> 48 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:27 marvel ukb vascular_dementia: 6534 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:28 marvel ukb frontotemporal_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb frontotemporal_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb frontotemporal_dementia: 244 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb frontotemporal_dementia: 6555 rows -> 24 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb frontotemporal_dementia: 6531 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:28 marvel ukb ascvd: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb ascvd: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb ascvd: 117 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb ascvd: 6682 rows -> 135 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:28 marvel ukb ascvd: 6538 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:29 marvel ukb apoa: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:29 marvel ukb apoa: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:29 marvel ukb apoa: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:29 marvel ukb apob: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:29 marvel ukb apob: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:29 marvel ukb apob: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:30 marvel ukb hdl_c: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:30 marvel ukb hdl_c: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:30 marvel ukb hdl_c: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:30 marvel ukb ldl_c: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:30 marvel ukb ldl_c: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:30 marvel ukb ldl_c: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:31 marvel ukb tg: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb tg: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb tg: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:31 marvel ukb all_cause_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb all_cause_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb all_cause_dementia: 230 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb all_cause_dementia: 5267 rows -> 138 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb all_cause_dementia: 5120 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:31 marvel ukb alzheimers_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb alzheimers_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:31 marvel ukb alzheimers_dementia: 277 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb alzheimers_dementia: 5301 rows -> 111 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb alzheimers_dementia: 5190 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:32 marvel ukb vascular_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb vascular_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb vascular_dementia: 268 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb vascular_dementia: 5229 rows -> 102 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb vascular_dementia: 5118 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:32 marvel ukb frontotemporal_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb frontotemporal_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb frontotemporal_dementia: 281 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb frontotemporal_dementia: 5216 rows -> 89 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:32 marvel ukb frontotemporal_dementia: 5118 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:33 marvel ukb ascvd: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:33 marvel ukb ascvd: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:33 marvel ukb ascvd: 104 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:33 marvel ukb ascvd: 5393 rows -> 241 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:33 marvel ukb ascvd: 5143 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:33 marvel ukb apoa: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:33 marvel ukb apoa: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:33 marvel ukb apoa: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:34 marvel ukb apob: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:34 marvel ukb apob: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:34 marvel ukb apob: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:34 marvel ukb hdl_c: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:34 marvel ukb hdl_c: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:34 marvel ukb hdl_c: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:35 marvel ukb ldl_c: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:35 marvel ukb ldl_c: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:35 marvel ukb ldl_c: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:35 marvel ukb tg: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:35 marvel ukb tg: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:35 marvel ukb tg: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:36 marvel ukb all_cause_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb all_cause_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb all_cause_dementia: 136 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb all_cause_dementia: 7248 rows -> 43 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb all_cause_dementia: 7196 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:36 marvel ukb alzheimers_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb alzheimers_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb alzheimers_dementia: 160 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb alzheimers_dementia: 7305 rows -> 28 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:36 marvel ukb alzheimers_dementia: 7265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:37 marvel ukb vascular_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb vascular_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb vascular_dementia: 160 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb vascular_dementia: 7224 rows -> 25 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb vascular_dementia: 7193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:37 marvel ukb frontotemporal_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb frontotemporal_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb frontotemporal_dementia: 181 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb frontotemporal_dementia: 7203 rows -> 9 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb frontotemporal_dementia: 7188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:37 marvel ukb ascvd: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb ascvd: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:37 marvel ukb ascvd: 77 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:38 marvel ukb ascvd: 7307 rows -> 96 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:38 marvel ukb ascvd: 7202 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:38 marvel ukb apoa: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:38 marvel ukb apoa: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:38 marvel ukb apoa: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:38 marvel ukb apob: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:39 marvel ukb apob: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:39 marvel ukb apob: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:39 marvel ukb hdl_c: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:39 marvel ukb hdl_c: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:39 marvel ukb hdl_c: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:39 marvel ukb ldl_c: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:40 marvel ukb ldl_c: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:40 marvel ukb ldl_c: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:40 marvel ukb tg: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:40 marvel ukb tg: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:40 marvel ukb tg: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:40 marvel ukb all_cause_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:40 marvel ukb all_cause_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:40 marvel ukb all_cause_dementia: 280 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb all_cause_dementia: 5905 rows -> 142 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb all_cause_dementia: 5754 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:41 marvel ukb alzheimers_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb alzheimers_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb alzheimers_dementia: 306 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb alzheimers_dementia: 5960 rows -> 121 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb alzheimers_dementia: 5821 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:41 marvel ukb vascular_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb vascular_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:41 marvel ukb vascular_dementia: 314 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb vascular_dementia: 5871 rows -> 112 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb vascular_dementia: 5750 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:42 marvel ukb frontotemporal_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb frontotemporal_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb frontotemporal_dementia: 333 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb frontotemporal_dementia: 5852 rows -> 93 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb frontotemporal_dementia: 5750 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:42 marvel ukb ascvd: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb ascvd: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb ascvd: 154 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb ascvd: 6031 rows -> 252 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:42 marvel ukb ascvd: 5770 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:43 marvel ukb apoa: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:43 marvel ukb apoa: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:43 marvel ukb apoa: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:43 marvel ukb apob: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:43 marvel ukb apob: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:43 marvel ukb apob: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:44 marvel ukb hdl_c: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:44 marvel ukb hdl_c: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:44 marvel ukb hdl_c: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:44 marvel ukb ldl_c: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:44 marvel ukb ldl_c: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:44 marvel ukb ldl_c: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:45 marvel ukb tg: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:45 marvel ukb tg: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:45 marvel ukb tg: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:45 marvel ukb all_cause_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:45 marvel ukb all_cause_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:45 marvel ukb all_cause_dementia: 27 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:45 marvel ukb all_cause_dementia: 9177 rows -> 32 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:45 marvel ukb all_cause_dementia: 9136 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:46 marvel ukb alzheimers_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb alzheimers_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb alzheimers_dementia: 36 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb alzheimers_dementia: 9249 rows -> 29 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb alzheimers_dementia: 9208 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:46 marvel ukb vascular_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb vascular_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb vascular_dementia: 45 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb vascular_dementia: 9159 rows -> 17 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:46 marvel ukb vascular_dementia: 9136 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:47 marvel ukb frontotemporal_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb frontotemporal_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb frontotemporal_dementia: 64 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb frontotemporal_dementia: 9140 rows -> 4 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb frontotemporal_dementia: 9136 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:47 marvel ukb ascvd: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb ascvd: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb ascvd: 27 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb ascvd: 9177 rows -> 33 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:47 marvel ukb ascvd: 9138 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:48 marvel ukb apoa: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:48 marvel ukb apoa: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:48 marvel ukb apoa: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:48 marvel ukb apob: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:48 marvel ukb apob: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:48 marvel ukb apob: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:49 marvel ukb hdl_c: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:49 marvel ukb hdl_c: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:49 marvel ukb hdl_c: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:49 marvel ukb ldl_c: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:49 marvel ukb ldl_c: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:49 marvel ukb ldl_c: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:49 marvel ukb tg: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:49 marvel ukb tg: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:49 marvel ukb tg: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:50 marvel ukb all_cause_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb all_cause_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb all_cause_dementia: 165 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb all_cause_dementia: 7286 rows -> 68 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb all_cause_dementia: 7209 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:50 marvel ukb alzheimers_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb alzheimers_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb alzheimers_dementia: 175 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb alzheimers_dementia: 7357 rows -> 58 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:50 marvel ukb alzheimers_dementia: 7281 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:51 marvel ukb vascular_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb vascular_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb vascular_dementia: 198 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb vascular_dementia: 7253 rows -> 38 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb vascular_dementia: 7206 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:51 marvel ukb frontotemporal_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb frontotemporal_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb frontotemporal_dementia: 229 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb frontotemporal_dementia: 7222 rows -> 19 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:51 marvel ukb frontotemporal_dementia: 7203 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:52 marvel ukb ascvd: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:52 marvel ukb ascvd: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:52 marvel ukb ascvd: 120 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:52 marvel ukb ascvd: 7331 rows -> 112 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:52 marvel ukb ascvd: 7210 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:52 marvel ukb apoa: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:52 marvel ukb apoa: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:52 marvel ukb apoa: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:53 marvel ukb apob: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:53 marvel ukb apob: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:53 marvel ukb apob: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:53 marvel ukb hdl_c: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:53 marvel ukb hdl_c: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:53 marvel ukb hdl_c: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:54 marvel ukb ldl_c: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:54 marvel ukb ldl_c: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:54 marvel ukb ldl_c: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:54 marvel ukb tg: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:54 marvel ukb tg: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:54 marvel ukb tg: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:55 marvel ukb all_cause_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb all_cause_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb all_cause_dementia: 254 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb all_cause_dementia: 6670 rows -> 101 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb all_cause_dementia: 6560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:55 marvel ukb alzheimers_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb alzheimers_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb alzheimers_dementia: 298 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb alzheimers_dementia: 6707 rows -> 77 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:55 marvel ukb alzheimers_dementia: 6630 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:56 marvel ukb vascular_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb vascular_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb vascular_dementia: 283 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb vascular_dementia: 6641 rows -> 74 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb vascular_dementia: 6558 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:56 marvel ukb frontotemporal_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb frontotemporal_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb frontotemporal_dementia: 303 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb frontotemporal_dementia: 6621 rows -> 57 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:56 marvel ukb frontotemporal_dementia: 6558 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:57 marvel ukb ascvd: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:57 marvel ukb ascvd: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:57 marvel ukb ascvd: 135 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:57 marvel ukb ascvd: 6789 rows -> 201 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:57 marvel ukb ascvd: 6579 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:57 marvel ukb apoa: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:57 marvel ukb apoa: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:57 marvel ukb apoa: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:58 marvel ukb apob: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:58 marvel ukb apob: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:58 marvel ukb apob: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:58 marvel ukb hdl_c: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:58 marvel ukb hdl_c: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:58 marvel ukb hdl_c: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:59 marvel ukb ldl_c: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:59 marvel ukb ldl_c: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:59 marvel ukb ldl_c: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:00:59 marvel ukb tg: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:59 marvel ukb tg: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:00:59 marvel ukb tg: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:00 marvel ukb all_cause_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb all_cause_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb all_cause_dementia: 131 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb all_cause_dementia: 7809 rows -> 36 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb all_cause_dementia: 7764 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:00 marvel ukb alzheimers_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb alzheimers_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb alzheimers_dementia: 152 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb alzheimers_dementia: 7869 rows -> 24 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb alzheimers_dementia: 7833 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:00 marvel ukb vascular_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb vascular_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:00 marvel ukb vascular_dementia: 151 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb vascular_dementia: 7789 rows -> 22 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb vascular_dementia: 7761 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:01 marvel ukb frontotemporal_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb frontotemporal_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb frontotemporal_dementia: 161 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb frontotemporal_dementia: 7779 rows -> 9 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb frontotemporal_dementia: 7764 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:01 marvel ukb ascvd: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb ascvd: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb ascvd: 82 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb ascvd: 7858 rows -> 81 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 17:01:01 marvel ukb ascvd: 7768 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:09 marvel ukb apoa: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:09 marvel ukb apoa: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:09 marvel ukb apoa: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:09 marvel ukb apob: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:09 marvel ukb apob: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:09 marvel ukb apob: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:10 marvel ukb hdl_c: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:10 marvel ukb hdl_c: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:10 marvel ukb hdl_c: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:10 marvel ukb ldl_c: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:10 marvel ukb ldl_c: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:10 marvel ukb ldl_c: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:10 marvel ukb tg: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb tg: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb tg: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:11 marvel ukb all_cause_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb all_cause_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb all_cause_dementia: 160 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb all_cause_dementia: 3312 rows -> 113 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb all_cause_dementia: 3189 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:11 marvel ukb alzheimers_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb alzheimers_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb alzheimers_dementia: 212 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb alzheimers_dementia: 3350 rows -> 87 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:11 marvel ukb alzheimers_dementia: 3243 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:12 marvel ukb vascular_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb vascular_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb vascular_dementia: 238 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb vascular_dementia: 3234 rows -> 65 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb vascular_dementia: 3159 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:12 marvel ukb frontotemporal_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb frontotemporal_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb frontotemporal_dementia: 250 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb frontotemporal_dementia: 3222 rows -> 57 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:12 marvel ukb frontotemporal_dementia: 3158 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:13 marvel ukb ascvd: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb ascvd: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb ascvd: 98 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb ascvd: 3374 rows -> 176 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb ascvd: 3188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:13 marvel ukb apoa: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb apoa: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb apoa: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:13 marvel ukb apob: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb apob: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:13 marvel ukb apob: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:14 marvel ukb hdl_c: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:14 marvel ukb hdl_c: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:14 marvel ukb hdl_c: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:14 marvel ukb ldl_c: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:14 marvel ukb ldl_c: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:14 marvel ukb ldl_c: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:14 marvel ukb tg: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:14 marvel ukb tg: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:14 marvel ukb tg: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:15 marvel ukb all_cause_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb all_cause_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb all_cause_dementia: 21 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb all_cause_dementia: 7532 rows -> 14 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb all_cause_dementia: 7508 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:15 marvel ukb alzheimers_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb alzheimers_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb alzheimers_dementia: 28 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb alzheimers_dementia: 7615 rows -> 10 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:15 marvel ukb alzheimers_dementia: 7585 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:16 marvel ukb vascular_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb vascular_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb vascular_dementia: 36 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb vascular_dementia: 7517 rows -> 7 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb vascular_dementia: 7504 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:16 marvel ukb frontotemporal_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb frontotemporal_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb frontotemporal_dementia: 47 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb frontotemporal_dementia: 7506 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb frontotemporal_dementia: 7503 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:16 marvel ukb ascvd: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb ascvd: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb ascvd: 9 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb ascvd: 7544 rows -> 16 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:16 marvel ukb ascvd: 7518 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:17 marvel ukb apoa: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:17 marvel ukb apoa: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:17 marvel ukb apoa: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:17 marvel ukb apob: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:17 marvel ukb apob: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:17 marvel ukb apob: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:17 marvel ukb hdl_c: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:18 marvel ukb hdl_c: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:18 marvel ukb hdl_c: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:18 marvel ukb ldl_c: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:18 marvel ukb ldl_c: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:18 marvel ukb ldl_c: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:18 marvel ukb tg: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:18 marvel ukb tg: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:18 marvel ukb tg: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:19 marvel ukb all_cause_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb all_cause_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb all_cause_dementia: 131 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb all_cause_dementia: 5704 rows -> 41 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb all_cause_dementia: 5653 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:19 marvel ukb alzheimers_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb alzheimers_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb alzheimers_dementia: 153 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb alzheimers_dementia: 5772 rows -> 34 variant rows, 14 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb alzheimers_dementia: 5724 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:19 marvel ukb vascular_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb vascular_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb vascular_dementia: 161 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb vascular_dementia: 5674 rows -> 22 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:19 marvel ukb vascular_dementia: 5645 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:20 marvel ukb frontotemporal_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb frontotemporal_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb frontotemporal_dementia: 175 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb frontotemporal_dementia: 5660 rows -> 16 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb frontotemporal_dementia: 5644 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:20 marvel ukb ascvd: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb ascvd: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb ascvd: 80 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb ascvd: 5755 rows -> 68 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:20 marvel ukb ascvd: 5677 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:21 marvel ukb apoa: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:21 marvel ukb apoa: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:21 marvel ukb apoa: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:21 marvel ukb apob: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:21 marvel ukb apob: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:21 marvel ukb apob: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:21 marvel ukb hdl_c: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:21 marvel ukb hdl_c: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:21 marvel ukb hdl_c: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:22 marvel ukb ldl_c: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:22 marvel ukb ldl_c: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:22 marvel ukb ldl_c: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:22 marvel ukb tg: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:22 marvel ukb tg: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:22 marvel ukb tg: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:23 marvel ukb all_cause_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb all_cause_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb all_cause_dementia: 181 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb all_cause_dementia: 3960 rows -> 52 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb all_cause_dementia: 3898 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:23 marvel ukb alzheimers_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb alzheimers_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb alzheimers_dementia: 223 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb alzheimers_dementia: 4008 rows -> 30 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb alzheimers_dementia: 3960 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:23 marvel ukb vascular_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb vascular_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb vascular_dementia: 230 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb vascular_dementia: 3911 rows -> 26 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:23 marvel ukb vascular_dementia: 3875 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:24 marvel ukb frontotemporal_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb frontotemporal_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb frontotemporal_dementia: 233 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb frontotemporal_dementia: 3908 rows -> 22 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb frontotemporal_dementia: 3880 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:24 marvel ukb ascvd: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb ascvd: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb ascvd: 88 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb ascvd: 4053 rows -> 129 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:24 marvel ukb ascvd: 3914 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:24 marvel ukb apoa: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:25 marvel ukb apoa: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:25 marvel ukb apoa: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:25 marvel ukb apob: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:25 marvel ukb apob: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:25 marvel ukb apob: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:25 marvel ukb hdl_c: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:25 marvel ukb hdl_c: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:25 marvel ukb hdl_c: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:26 marvel ukb ldl_c: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb ldl_c: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb ldl_c: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:26 marvel ukb tg: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb tg: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb tg: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:26 marvel ukb all_cause_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb all_cause_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb all_cause_dementia: 99 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb all_cause_dementia: 6201 rows -> 13 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:26 marvel ukb all_cause_dementia: 6181 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:27 marvel ukb alzheimers_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb alzheimers_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb alzheimers_dementia: 105 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb alzheimers_dementia: 6285 rows -> 10 variant rows, 14 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb alzheimers_dementia: 6261 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:27 marvel ukb vascular_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb vascular_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb vascular_dementia: 116 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb vascular_dementia: 6184 rows -> 7 variant rows, 1 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:27 marvel ukb vascular_dementia: 6176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:28 marvel ukb frontotemporal_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb frontotemporal_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb frontotemporal_dementia: 122 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb frontotemporal_dementia: 6178 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb frontotemporal_dementia: 6175 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:28 marvel ukb ascvd: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb ascvd: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb ascvd: 40 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb ascvd: 6260 rows -> 41 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb ascvd: 6209 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:28 marvel ukb apoa: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb apoa: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:28 marvel ukb apoa: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:29 marvel ukb apob: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:29 marvel ukb apob: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:29 marvel ukb apob: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:29 marvel ukb hdl_c: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:29 marvel ukb hdl_c: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:29 marvel ukb hdl_c: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:30 marvel ukb ldl_c: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb ldl_c: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb ldl_c: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:30 marvel ukb tg: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb tg: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb tg: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:30 marvel ukb all_cause_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb all_cause_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb all_cause_dementia: 198 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb all_cause_dementia: 4936 rows -> 79 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:30 marvel ukb all_cause_dementia: 4847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:31 marvel ukb alzheimers_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb alzheimers_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb alzheimers_dementia: 242 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb alzheimers_dementia: 4982 rows -> 58 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb alzheimers_dementia: 4904 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:31 marvel ukb vascular_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb vascular_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb vascular_dementia: 261 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb vascular_dementia: 4873 rows -> 43 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:31 marvel ukb vascular_dementia: 4820 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:32 marvel ukb frontotemporal_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb frontotemporal_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb frontotemporal_dementia: 271 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb frontotemporal_dementia: 4863 rows -> 37 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb frontotemporal_dementia: 4820 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:32 marvel ukb ascvd: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb ascvd: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb ascvd: 138 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb ascvd: 4996 rows -> 136 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb ascvd: 4850 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:32 marvel ukb apoa: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb apoa: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:32 marvel ukb apoa: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:33 marvel ukb apob: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:33 marvel ukb apob: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:33 marvel ukb apob: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:33 marvel ukb hdl_c: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:33 marvel ukb hdl_c: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:33 marvel ukb hdl_c: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:33 marvel ukb ldl_c: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb ldl_c: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb ldl_c: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:34 marvel ukb tg: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb tg: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb tg: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:34 marvel ukb all_cause_dementia: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb all_cause_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb all_cause_dementia: 20 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb all_cause_dementia: 7760 rows -> 7 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:34 marvel ukb all_cause_dementia: 7744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:35 marvel ukb alzheimers_dementia: 810 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb alzheimers_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb alzheimers_dementia: 7839 rows -> 5 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb alzheimers_dementia: 7816 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:35 marvel ukb vascular_dementia: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb vascular_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb vascular_dementia: 25 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb vascular_dementia: 7755 rows -> 5 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb vascular_dementia: 7744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:35 marvel ukb frontotemporal_dementia: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb frontotemporal_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb frontotemporal_dementia: 34 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb frontotemporal_dementia: 7746 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:35 marvel ukb frontotemporal_dementia: 7743 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:36 marvel ukb ascvd: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:36 marvel ukb ascvd: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:36 marvel ukb ascvd: 5 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:36 marvel ukb ascvd: 7775 rows -> 9 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:36 marvel ukb ascvd: 7757 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:36 marvel ukb apoa: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:36 marvel ukb apoa: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:36 marvel ukb apoa: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:37 marvel ukb apob: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:37 marvel ukb apob: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:37 marvel ukb apob: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:37 marvel ukb hdl_c: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:37 marvel ukb hdl_c: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:37 marvel ukb hdl_c: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:37 marvel ukb ldl_c: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:37 marvel ukb ldl_c: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:37 marvel ukb ldl_c: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:38 marvel ukb tg: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:38 marvel ukb tg: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:38 marvel ukb tg: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:38 marvel ukb all_cause_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:38 marvel ukb all_cause_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:38 marvel ukb all_cause_dementia: 112 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:38 marvel ukb all_cause_dementia: 6233 rows -> 31 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:38 marvel ukb all_cause_dementia: 6193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:39 marvel ukb alzheimers_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb alzheimers_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb alzheimers_dementia: 127 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb alzheimers_dementia: 6308 rows -> 28 variant rows, 12 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb alzheimers_dementia: 6268 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:39 marvel ukb vascular_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb vascular_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb vascular_dementia: 134 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb vascular_dementia: 6211 rows -> 17 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb vascular_dementia: 6188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:39 marvel ukb frontotemporal_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb frontotemporal_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb frontotemporal_dementia: 146 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb frontotemporal_dementia: 6199 rows -> 11 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:39 marvel ukb frontotemporal_dementia: 6188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:40 marvel ukb ascvd: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:40 marvel ukb ascvd: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:40 marvel ukb ascvd: 83 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:40 marvel ukb ascvd: 6262 rows -> 45 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:40 marvel ukb ascvd: 6207 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:40 marvel ukb apoa: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:40 marvel ukb apoa: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:40 marvel ukb apoa: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:41 marvel ukb apob: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:41 marvel ukb apob: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:41 marvel ukb apob: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:41 marvel ukb hdl_c: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:41 marvel ukb hdl_c: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:41 marvel ukb hdl_c: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:41 marvel ukb ldl_c: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:41 marvel ukb ldl_c: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:41 marvel ukb ldl_c: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:42 marvel ukb tg: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:42 marvel ukb tg: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:42 marvel ukb tg: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:42 marvel ukb all_cause_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:42 marvel ukb all_cause_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:42 marvel ukb all_cause_dementia: 172 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:42 marvel ukb all_cause_dementia: 5315 rows -> 32 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:42 marvel ukb all_cause_dementia: 5273 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:43 marvel ukb alzheimers_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb alzheimers_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb alzheimers_dementia: 200 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb alzheimers_dementia: 5377 rows -> 18 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb alzheimers_dementia: 5341 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:43 marvel ukb vascular_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb vascular_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb vascular_dementia: 212 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb vascular_dementia: 5275 rows -> 12 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb vascular_dementia: 5256 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:43 marvel ukb frontotemporal_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb frontotemporal_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb frontotemporal_dementia: 209 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb frontotemporal_dementia: 5278 rows -> 11 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:43 marvel ukb frontotemporal_dementia: 5261 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:44 marvel ukb ascvd: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:44 marvel ukb ascvd: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:44 marvel ukb ascvd: 90 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:44 marvel ukb ascvd: 5397 rows -> 96 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:44 marvel ukb ascvd: 5291 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:44 marvel ukb apoa: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:44 marvel ukb apoa: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:44 marvel ukb apoa: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:45 marvel ukb apob: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:45 marvel ukb apob: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:45 marvel ukb apob: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:45 marvel ukb hdl_c: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:45 marvel ukb hdl_c: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:45 marvel ukb hdl_c: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:45 marvel ukb ldl_c: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb ldl_c: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb ldl_c: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:46 marvel ukb tg: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb tg: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb tg: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:46 marvel ukb all_cause_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb all_cause_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb all_cause_dementia: 69 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb all_cause_dementia: 6686 rows -> 8 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:46 marvel ukb all_cause_dementia: 6672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:47 marvel ukb alzheimers_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb alzheimers_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb alzheimers_dementia: 76 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb alzheimers_dementia: 6769 rows -> 5 variant rows, 12 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb alzheimers_dementia: 6752 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:47 marvel ukb vascular_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb vascular_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb vascular_dementia: 78 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb vascular_dementia: 6677 rows -> 5 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb vascular_dementia: 6672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:47 marvel ukb frontotemporal_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb frontotemporal_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:47 marvel ukb frontotemporal_dementia: 81 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:48 marvel ukb frontotemporal_dementia: 6674 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:48 marvel ukb frontotemporal_dementia: 6671 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:48 marvel ukb ascvd: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:48 marvel ukb ascvd: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:48 marvel ukb ascvd: 25 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:48 marvel ukb ascvd: 6730 rows -> 29 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 17:01:48 marvel ukb ascvd: 6691 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:51 marvel ukb apoa: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb apoa: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb apoa: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:51 marvel ukb apob: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb apob: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb apob: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:51 marvel ukb hdl_c: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb hdl_c: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb hdl_c: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:51 marvel ukb ldl_c: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb ldl_c: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb ldl_c: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:51 marvel ukb tg: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb tg: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb tg: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:51 marvel ukb all_cause_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb all_cause_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb all_cause_dementia: 35 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb all_cause_dementia: 923 rows -> 48 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:51 marvel ukb all_cause_dementia: 866 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb alzheimers_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb alzheimers_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb alzheimers_dementia: 41 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb alzheimers_dementia: 998 rows -> 42 variant rows, 18 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb alzheimers_dementia: 938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb vascular_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb vascular_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb vascular_dementia: 47 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb vascular_dementia: 911 rows -> 36 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb vascular_dementia: 866 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb frontotemporal_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb frontotemporal_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb frontotemporal_dementia: 62 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb frontotemporal_dementia: 896 rows -> 31 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb frontotemporal_dementia: 865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb ascvd: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb ascvd: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb ascvd: 17 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb ascvd: 941 rows -> 66 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb ascvd: 866 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb apoa: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb apoa: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb apoa: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb apob: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb apob: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb apob: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:52 marvel ukb hdl_c: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb hdl_c: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:52 marvel ukb hdl_c: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb ldl_c: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb ldl_c: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb ldl_c: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb tg: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb tg: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb tg: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb all_cause_dementia: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb all_cause_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb all_cause_dementia: 15 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb all_cause_dementia: 2597 rows -> 7 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb all_cause_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb alzheimers_dementia: 288 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb alzheimers_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb alzheimers_dementia: 16 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb alzheimers_dementia: 2650 rows -> 6 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb alzheimers_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb vascular_dementia: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb vascular_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb vascular_dementia: 22 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb vascular_dementia: 2590 rows -> 3 variant rows, 3 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb vascular_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb frontotemporal_dementia: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb frontotemporal_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb frontotemporal_dementia: 26 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb frontotemporal_dementia: 2586 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb frontotemporal_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:53 marvel ukb ascvd: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb ascvd: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:53 marvel ukb ascvd: 15 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb ascvd: 2597 rows -> 7 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb ascvd: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:54 marvel ukb apoa: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb apoa: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb apoa: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:54 marvel ukb apob: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb apob: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb apob: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:54 marvel ukb hdl_c: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb hdl_c: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb hdl_c: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:54 marvel ukb ldl_c: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb ldl_c: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb ldl_c: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:54 marvel ukb tg: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb tg: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb tg: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:54 marvel ukb all_cause_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb all_cause_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb all_cause_dementia: 52 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb all_cause_dementia: 1870 rows -> 18 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:54 marvel ukb all_cause_dementia: 1846 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb alzheimers_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb alzheimers_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb alzheimers_dementia: 57 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb alzheimers_dementia: 1946 rows -> 16 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb alzheimers_dementia: 1918 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb vascular_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb vascular_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb vascular_dementia: 56 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb vascular_dementia: 1866 rows -> 14 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb vascular_dementia: 1846 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb frontotemporal_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb frontotemporal_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb frontotemporal_dementia: 73 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb frontotemporal_dementia: 1849 rows -> 9 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb frontotemporal_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb ascvd: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb ascvd: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb ascvd: 35 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb ascvd: 1887 rows -> 30 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb ascvd: 1848 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb apoa: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb apoa: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb apoa: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb apob: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb apob: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:55 marvel ukb apob: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:55 marvel ukb hdl_c: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb hdl_c: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb hdl_c: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:56 marvel ukb ldl_c: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb ldl_c: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb ldl_c: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:56 marvel ukb tg: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb tg: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb tg: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:56 marvel ukb all_cause_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb all_cause_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb all_cause_dementia: 62 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb all_cause_dementia: 1268 rows -> 27 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb all_cause_dementia: 1232 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:56 marvel ukb alzheimers_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb alzheimers_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb alzheimers_dementia: 73 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb alzheimers_dementia: 1338 rows -> 22 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb alzheimers_dementia: 1304 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:56 marvel ukb vascular_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb vascular_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb vascular_dementia: 72 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb vascular_dementia: 1258 rows -> 20 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb vascular_dementia: 1232 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:56 marvel ukb frontotemporal_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb frontotemporal_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb frontotemporal_dementia: 82 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb frontotemporal_dementia: 1248 rows -> 16 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:56 marvel ukb frontotemporal_dementia: 1232 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:57 marvel ukb ascvd: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb ascvd: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb ascvd: 37 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb ascvd: 1293 rows -> 50 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb ascvd: 1234 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:57 marvel ukb apoa: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb apoa: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb apoa: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:57 marvel ukb apob: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb apob: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb apob: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:57 marvel ukb hdl_c: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb hdl_c: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb hdl_c: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:57 marvel ukb ldl_c: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb ldl_c: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:57 marvel ukb ldl_c: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb tg: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb tg: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb tg: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb all_cause_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb all_cause_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb all_cause_dementia: 45 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb all_cause_dementia: 2230 rows -> 8 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb all_cause_dementia: 2216 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb alzheimers_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb alzheimers_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb alzheimers_dementia: 64 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb alzheimers_dementia: 2292 rows -> 4 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb alzheimers_dementia: 2288 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb vascular_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb vascular_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb vascular_dementia: 57 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb vascular_dementia: 2218 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb vascular_dementia: 2216 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb frontotemporal_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb frontotemporal_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb frontotemporal_dementia: 56 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb frontotemporal_dementia: 2219 rows -> 3 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb frontotemporal_dementia: 2216 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb ascvd: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb ascvd: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb ascvd: 26 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb ascvd: 2249 rows -> 18 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb ascvd: 2222 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:58 marvel ukb apoa: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb apoa: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:58 marvel ukb apoa: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:59 marvel ukb apob: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb apob: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb apob: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:59 marvel ukb hdl_c: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb hdl_c: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb hdl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:59 marvel ukb ldl_c: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb ldl_c: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb ldl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:59 marvel ukb tg: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb tg: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb tg: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:59 marvel ukb all_cause_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb all_cause_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb all_cause_dementia: 58 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb all_cause_dementia: 1369 rows -> 35 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb all_cause_dementia: 1325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:01:59 marvel ukb alzheimers_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb alzheimers_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb alzheimers_dementia: 63 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb alzheimers_dementia: 1445 rows -> 30 variant rows, 18 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:01:59 marvel ukb alzheimers_dementia: 1397 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb vascular_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb vascular_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb vascular_dementia: 67 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb vascular_dementia: 1360 rows -> 26 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb vascular_dementia: 1325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb frontotemporal_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb frontotemporal_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb frontotemporal_dementia: 86 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb frontotemporal_dementia: 1341 rows -> 20 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb frontotemporal_dementia: 1321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb ascvd: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb ascvd: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb ascvd: 41 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb ascvd: 1386 rows -> 52 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb ascvd: 1325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb apoa: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb apoa: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb apoa: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb apob: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb apob: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb apob: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb hdl_c: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb hdl_c: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb hdl_c: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:00 marvel ukb ldl_c: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb ldl_c: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:00 marvel ukb ldl_c: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:01 marvel ukb tg: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb tg: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb tg: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:01 marvel ukb all_cause_dementia: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb all_cause_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb all_cause_dementia: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb all_cause_dementia: 2643 rows -> 5 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb all_cause_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:01 marvel ukb alzheimers_dementia: 234 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb alzheimers_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb alzheimers_dementia: 2697 rows -> 5 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb alzheimers_dementia: 2680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:01 marvel ukb vascular_dementia: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb vascular_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb vascular_dementia: 20 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb vascular_dementia: 2637 rows -> 2 variant rows, 3 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb vascular_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:01 marvel ukb frontotemporal_dementia: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb frontotemporal_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb frontotemporal_dementia: 23 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb frontotemporal_dementia: 2634 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb frontotemporal_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:01 marvel ukb ascvd: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb ascvd: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb ascvd: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb ascvd: 2643 rows -> 5 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:01 marvel ukb ascvd: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb apoa: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb apoa: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb apoa: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb apob: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb apob: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb apob: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb hdl_c: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb hdl_c: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb hdl_c: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb ldl_c: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb ldl_c: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb ldl_c: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb tg: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb tg: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb tg: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb all_cause_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb all_cause_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb all_cause_dementia: 59 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb all_cause_dementia: 2133 rows -> 17 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb all_cause_dementia: 2110 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:02 marvel ukb alzheimers_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb alzheimers_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:02 marvel ukb alzheimers_dementia: 64 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb alzheimers_dementia: 2209 rows -> 15 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb alzheimers_dementia: 2182 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:03 marvel ukb vascular_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb vascular_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb vascular_dementia: 63 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb vascular_dementia: 2129 rows -> 13 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb vascular_dementia: 2110 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:03 marvel ukb frontotemporal_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb frontotemporal_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb frontotemporal_dementia: 80 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb frontotemporal_dementia: 2112 rows -> 8 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb frontotemporal_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:03 marvel ukb ascvd: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb ascvd: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb ascvd: 46 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb ascvd: 2146 rows -> 25 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb ascvd: 2112 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:03 marvel ukb apoa: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb apoa: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb apoa: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:03 marvel ukb apob: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb apob: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb apob: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:03 marvel ukb hdl_c: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb hdl_c: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:03 marvel ukb hdl_c: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:04 marvel ukb ldl_c: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb ldl_c: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb ldl_c: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:04 marvel ukb tg: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb tg: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb tg: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:04 marvel ukb all_cause_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb all_cause_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb all_cause_dementia: 72 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb all_cause_dementia: 1607 rows -> 14 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb all_cause_dementia: 1584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:04 marvel ukb alzheimers_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb alzheimers_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb alzheimers_dementia: 81 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb alzheimers_dementia: 1679 rows -> 11 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb alzheimers_dementia: 1656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:04 marvel ukb vascular_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb vascular_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb vascular_dementia: 80 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb vascular_dementia: 1599 rows -> 9 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb vascular_dementia: 1584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:04 marvel ukb frontotemporal_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb frontotemporal_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb frontotemporal_dementia: 88 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb frontotemporal_dementia: 1591 rows -> 7 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:04 marvel ukb frontotemporal_dementia: 1584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb ascvd: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb ascvd: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb ascvd: 47 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb ascvd: 1632 rows -> 34 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb ascvd: 1589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb apoa: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb apoa: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb apoa: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb apob: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb apob: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb apob: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb hdl_c: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb hdl_c: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb hdl_c: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb ldl_c: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb ldl_c: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb ldl_c: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb tg: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb tg: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb tg: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:05 marvel ukb all_cause_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb all_cause_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb all_cause_dementia: 36 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb all_cause_dementia: 2341 rows -> 7 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:05 marvel ukb all_cause_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:06 marvel ukb alzheimers_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb alzheimers_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb alzheimers_dementia: 55 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb alzheimers_dementia: 2403 rows -> 3 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb alzheimers_dementia: 2400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:06 marvel ukb vascular_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb vascular_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb vascular_dementia: 47 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb vascular_dementia: 2330 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb vascular_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:06 marvel ukb frontotemporal_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb frontotemporal_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb frontotemporal_dementia: 46 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb frontotemporal_dementia: 2331 rows -> 3 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb frontotemporal_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 17:02:06 marvel ukb ascvd: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb ascvd: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb ascvd: 19 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb ascvd: 2358 rows -> 15 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 17:02:06 marvel ukb ascvd: 2334 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-10-27 17:02:07 fetch_curated
[info]  2026-10-27 17:03:28 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1
[info]  2026-10-27 17:03:29 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-27 17:03:33 MONDO_0013792 (exact): 42 fetched; in region: none
[info]  2026-10-27 17:03:38 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-27 17:04:11 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-27 17:04:39 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6
[info]  2026-10-27 17:04:41 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-27 17:04:46 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-27 17:12:47 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3
[info]  2026-10-27 17:12:58 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-27 17:13:00 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-27 17:13:01 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-27 17:30:05 MONDO_0004975 (with child traits): 7125 fetched; in region: APOB=1
[info]  2026-10-27 17:30:25 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-27 17:30:37 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-27 17:30:45 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-27 17:30:47 EFO ids with 0 curated associations: 4
[stage] 2026-10-27 17:30:47 gene_burden
[info]  2026-10-27 17:30:47 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-27 17:30:48 curated MAF: numeric=58 not_reported=28
[info]  2026-10-27 17:30:48 curated: 54 rows dropped from studies excluded for cohort overlap
[info]  2026-10-27 17:30:48 gene-burden rows: none (8 genes with 0)
[info]  2026-10-27 17:30:53 ancestry: 0 rows of studies not in the discovery log labelled NR
[info]  2026-10-27 17:30:53 ancestry: curated EAS=21
[info]  2026-10-27 17:30:53 ancestry: curated EUR=26
[info]  2026-10-27 17:30:53 ancestry: curated MULTI=21
[info]  2026-10-27 17:30:53 ancestry: curated NR=18
[info]  2026-10-27 17:30:53 ancestry: gene-burden EUR=2661
[info]  2026-10-27 17:30:53 ancestry: gene-burden MULTI=2718
[info]  2026-10-27 17:30:53 ancestry: summary-stats AFR=159854
[info]  2026-10-27 17:30:53 ancestry: summary-stats AMR=73617
[info]  2026-10-27 17:30:53 ancestry: summary-stats CSA=43677
[info]  2026-10-27 17:30:53 ancestry: summary-stats EAS=45135
[info]  2026-10-27 17:30:53 ancestry: summary-stats EUR=203384
[info]  2026-10-27 17:30:53 ancestry: summary-stats MULTI=184989
[info]  2026-10-27 17:30:53 ancestry: summary-stats NR=5898
[stage] 2026-10-27 17:30:54 effect_scale
[info]  2026-10-27 17:30:56 wrote 216 studies to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-27 17:30:56 study effect scale: linear=52, log_or=112, unknown=52
[stage] 2026-10-27 17:30:56 normalise
[info]  2026-10-27 17:30:58 normalisation: summary-stats rows unchanged=673290 no_sequence=40564 ref_mismatch=2699 normalised=1
[info]  2026-10-27 17:30:58 normalisation: curated rows effect_only=86
[stage] 2026-10-27 17:30:58 ensembl_check
[info]  2026-10-27 17:30:58 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-27 17:30:58 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-27 17:30:59 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-27 17:30:59 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-27 17:30:59 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-27 17:30:59 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-27 17:31:00 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-27 17:31:00 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-27 17:31:02 Ensembl check: 23697 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-27 17:31:04 summary-stats rows: alleles match=530816 flipped=135502 not_found=31938 mismatch=17830 strand_flip=468; rsid same=523657 no_source_rsid=116612 rsid_only=41315 different=3032
[info]  2026-10-27 17:31:04 curated rows: alleles match=33 flipped=28 effect_unknown=25; rsid same=86
[info]  2026-10-27 17:31:05 duplicate variants flagged: 766 rows
[stage] 2026-10-27 17:31:05 write
[info]  2026-10-27 17:32:08 wrote 722019 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-27 17:32:10
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 16:58:26 using root directory: /home/mvanvugt/projects/lipid_adem

```

## [40] clinvar_filter (`mamba run --no-capture-output -n clinvar-build clinvar-filter /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_vcv.db --rcv-db /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_rcv.db -g gene CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA APOA1 APOB APOE -o /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv -vvv`)
- first run: 2026-10-06 17:09:48
- last run: 2026-10-06 17:09:48
- commit: `7e96ca6` (dirty)

Output:
```text
2026-10-06 17:09:48,842 - INFO - Wrote 313818 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
```

## [40] match_variants (`/home/mvanvugt/projects/lipid_adem/src/match_variants.py`)
- first run: 2026-10-01 09:59:12
- last run: 2026-10-27 17:38:08
- commit: `23ebede` (dirty)

Output:
```text
[stage] 2026-10-27 17:37:37 load_variant_lists
[info]  2026-10-27 17:37:37 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv: 9227 rows
[info]  2026-10-27 17:37:37 0 duplicate rows removed
[info]  2026-10-27 17:37:37 ANGPTL3 AM: 493 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 ANGPTL3 ClinVar: 12 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 ANGPTL3 PTV: 56 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 APOA1 ClinVar: 33 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 APOA1 PTV: 15 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 APOB ClinVar: 236 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 APOB PTV: 172 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 APOE ClinVar: 20 rows, 0 without alleles, 20 outside gene region
[info]  2026-10-27 17:37:37 CETP AM: 439 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 CETP ClinVar: 10 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 CETP GoF: 1 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 CETP PTV: 58 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 CETP SelectedGoF: 3 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 HMGCR AM: 2623 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 HMGCR ClinVar: 7 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 HMGCR PTV: 39 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 NPC1L1 AM: 2507 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 NPC1L1 PTV: 96 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 PCSK9 AM: 737 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 PCSK9 ClinVar: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 PCSK9 GoF: 18 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 PCSK9 PTV: 68 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 PPARA AM: 1543 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 PPARA PTV: 23 rows, 0 without alleles, 0 outside gene region
[info]  2026-10-27 17:37:37 normalisation: variant-list rows unchanged=9207 no_sequence=20
[stage] 2026-10-27 17:37:37 load_gwas
[info]  2026-10-27 17:37:58 /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz: 722019 rows, 716640 variant-level (summary-stats, curated)
[info]  2026-10-27 17:37:59 wrote 5379 marvel gene-burden rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_burden.tsv.gz
[info]  2026-10-27 17:38:02 curated: 25 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-27 17:38:03 match
[info]  2026-10-27 17:38:04 ANGPTL3 AM: 493 variants, 37 matched, GWAS rows: summary-stats=1531
[info]  2026-10-27 17:38:04 ANGPTL3 ClinVar: 12 variants, 6 matched, GWAS rows: summary-stats=383
[info]  2026-10-27 17:38:04 ANGPTL3 PTV: 56 variants, 54 matched, GWAS rows: summary-stats=2229
[info]  2026-10-27 17:38:04 APOA1 ClinVar: 33 variants, 0 matched, GWAS rows: none
[info]  2026-10-27 17:38:04 APOA1 PTV: 15 variants, 0 matched, GWAS rows: none
[info]  2026-10-27 17:38:04 APOB ClinVar: 236 variants, 3 matched, GWAS rows: summary-stats=137
[info]  2026-10-27 17:38:04 APOB PTV: 172 variants, 0 matched, GWAS rows: none
[info]  2026-10-27 17:38:04 APOE ClinVar: 20 variants, 1 matched, GWAS rows: summary-stats=16
[info]  2026-10-27 17:38:04 CETP AM: 439 variants, 34 matched, GWAS rows: summary-stats=1291
[info]  2026-10-27 17:38:04 CETP ClinVar: 10 variants, 6 matched, GWAS rows: summary-stats=275
[info]  2026-10-27 17:38:04 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=306
[info]  2026-10-27 17:38:04 CETP PTV: 58 variants, 58 matched, GWAS rows: summary-stats=2554
[info]  2026-10-27 17:38:04 CETP SelectedGoF: 3 variants, 3 matched, GWAS rows: summary-stats=971
[info]  2026-10-27 17:38:04 HMGCR AM: 2623 variants, 131 matched, GWAS rows: summary-stats=4749
[info]  2026-10-27 17:38:04 HMGCR ClinVar: 7 variants, 4 matched, GWAS rows: summary-stats=127
[info]  2026-10-27 17:38:04 HMGCR PTV: 39 variants, 39 matched, GWAS rows: summary-stats=1409
[info]  2026-10-27 17:38:04 NPC1L1 AM: 2507 variants, 178 matched, GWAS rows: summary-stats=6671
[info]  2026-10-27 17:38:04 NPC1L1 PTV: 96 variants, 93 matched, GWAS rows: summary-stats=3453
[info]  2026-10-27 17:38:04 PCSK9 AM: 737 variants, 49 matched, GWAS rows: summary-stats=1770
[info]  2026-10-27 17:38:04 PCSK9 ClinVar: 18 variants, 4 matched, GWAS rows: summary-stats=219
[info]  2026-10-27 17:38:04 PCSK9 GoF: 18 variants, 12 matched, GWAS rows: summary-stats=955
[info]  2026-10-27 17:38:04 PCSK9 PTV: 68 variants, 68 matched, GWAS rows: summary-stats=2574
[info]  2026-10-27 17:38:04 PPARA AM: 1543 variants, 102 matched, GWAS rows: summary-stats=3665
[info]  2026-10-27 17:38:04 PPARA PTV: 23 variants, 22 matched, GWAS rows: summary-stats=719
[warn]  2026-10-27 17:38:04 a1 vs Ensembl ref: 20225 matched SNV rows checked, 140 where a1 is not the Ensembl ref (e.g. 1:62604235:GG:G, 5:75355116:GG:GGG, 1:55052661:TGAC:TGACTGAC)
[stage] 2026-10-27 17:38:04 write
[info]  2026-10-27 17:38:08 wrote 36004 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_variants.tsv.gz

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
- last run: 2026-10-29 18:19:29
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-28 16:36:27 task 1: rows 1-1
[info]  2026-10-29 18:19:29 PCSK9: results in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step4b7/PCSK9

```

## [50] meta_analysis (`/home/mvanvugt/projects/lipid_adem/src/meta_analysis.py --ancestry MULTI --variant-sources SelectedGoF --stratified --label selected_gof_multi --no-gene-burden --require-expected-scale`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-27 17:38:36
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 17:38:32 ancestry MULTI, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-27 17:38:32 load_matched
[info]  2026-10-27 17:38:33 /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_variants.tsv.gz: 36004 rows, 889 variants
[info]  2026-10-27 17:38:33 16 rows of excluded gene(s) APOE dropped
[info]  2026-10-27 17:38:33 35988 of 35988 rows kept (MULTI pools every ancestry) (all: AFR=465, AMR=194, CSA=1370, EAS=204, EUR=17837, MULTI=15894, NR=24)
[info]  2026-10-27 17:38:33 MULTI: 35988 rows pooled across ancestries (AFR=465, AMR=194, CSA=1370, EAS=204, EUR=17837, MULTI=15894, NR=24), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
[stage] 2026-10-27 17:38:33 effect_scale
[warn]  2026-10-27 17:38:33 GCST90276157: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90276158: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apoa: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apoa_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apoa_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apoa_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apoa_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apob: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apob_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apob_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apob_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_apob_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_hdl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_hdl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_hdl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_hdl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_hdl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_ldl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_ldl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_ldl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_ldl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_ldl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_tg: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_tg_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_tg_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_tg_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_EUR_tg_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apoa: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apoa_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apoa_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apoa_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apoa_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apob: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apob_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apob_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apob_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_apob_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_hdl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_hdl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_hdl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_hdl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_hdl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_ldl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_ldl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_ldl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_ldl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_ldl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_tg: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_tg_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_tg_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_tg_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 marvel_ukb_MULTI_tg_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST002245: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST005195: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90014122: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90014123: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90475198: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90475199: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90475933: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90475987: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476370: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476592: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476593: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476594: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476595: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476621: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476622: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90476623: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477866: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477867: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477928: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477929: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477937: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477938: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477939: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477941: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477942: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477943: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477944: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477958: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477959: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477976: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477977: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90477978: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90479542: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90479543: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480131: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480173: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480174: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480187: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480188: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480191: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90480807: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90481154: effect scale unknown, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 17:38:33 GCST90481158: effect scale unknown, not log-OR; kept (--require-log-or drops)
[info]  2026-10-27 17:38:33 GCST002245: 8 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST005195: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90014122: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90014123: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90276157: 4 rows on scale linear, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90276158: 8 rows on scale linear, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90475198: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90475199: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90475933: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90475987: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476370: 10 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476592: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476593: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476594: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476595: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476621: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476622: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90476623: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477866: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477867: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477928: 6 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477929: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477937: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477938: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477939: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477941: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477942: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477943: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477944: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477958: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477959: 20 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477976: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477977: 45 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90477978: 30 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90479542: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90479543: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480131: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480173: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480174: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480187: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480188: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480191: 12 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90480807: 18 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90481154: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 GCST90481158: 27 rows on scale unknown, not the expected one for their outcome; dropped
[info]  2026-10-27 17:38:33 --require-expected-scale: 1187 of 35988 rows of 45 studies dropped
[stage] 2026-10-27 17:38:33 prepare_effects
[info]  2026-10-27 17:38:33 18780 rows dropped: no beta or odds ratio
[info]  2026-10-27 17:38:33 16021 usable rows, 0 with SE derived from p
[stage] 2026-10-27 17:38:33 resolve_ambiguous
[stage] 2026-10-27 17:38:33 orient
[info]  2026-10-27 17:38:33 511 variants oriented as a2
[info]  2026-10-27 17:38:33 13 variants oriented as a2_gof_flipped
[info]  2026-10-27 17:38:33 PPARA: flipped to the therapeutic direction (drugs raise gene function)
[info]  2026-10-27 17:38:33 10 ClinVar variants with direction lowering
[info]  2026-10-27 17:38:33 2 ClinVar variants with direction conflicting
[info]  2026-10-27 17:38:33 1 ClinVar variants with direction raising
[info]  2026-10-27 17:38:33 1 ClinVar variants with direction unknown
[info]  2026-10-27 17:38:33 variant_list_source in SelectedGoF: 587 of 16021 rows kept
[stage] 2026-10-27 17:38:33 apoe_strata
[info]  2026-10-27 17:38:33 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: 104 studies with an APOE stratum entry
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_all_cause_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_all_cause_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_all_cause_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apoa, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apoa, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apoa, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apoa, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apoa, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apob, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apob, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apob, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apob, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_apob, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ascvd, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ascvd, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ascvd, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ascvd, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ascvd, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_hdl_c, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_hdl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_hdl_c, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_hdl_c, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_hdl_c, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ldl_c, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ldl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ldl_c, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ldl_c, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_ldl_c, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_tg, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_tg, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_tg, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_tg, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_tg, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_vascular_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_vascular_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_vascular_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_EUR_vascular_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_all_cause_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_all_cause_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_all_cause_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apoa, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apoa, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apoa, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apoa, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apoa, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apob, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apob, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apob, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apob, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_apob, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ascvd, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ascvd, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ascvd, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ascvd, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ascvd, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_hdl_c, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_hdl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_hdl_c, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_hdl_c, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_hdl_c, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ldl_c, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ldl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ldl_c, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ldl_c, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_ldl_c, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_tg, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_tg, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_tg, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_tg, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_tg, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_vascular_dementia, stratum all: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_vascular_dementia, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_vascular_dementia, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group marvel_ukb_MULTI_vascular_dementia, stratum e44: 1 studies
[info]  2026-10-27 17:38:33 study group thomassen, stratum e22_e32: 1 studies
[info]  2026-10-27 17:38:33 study group thomassen, stratum e33: 1 studies
[info]  2026-10-27 17:38:33 study group thomassen, stratum e43: 1 studies
[info]  2026-10-27 17:38:33 study group thomassen, stratum e44: 1 studies
[stage] 2026-10-27 17:38:33 pooled_run
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_all_cause_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_alzheimers_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_apoa: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_apob: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_ascvd: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_hdl_c: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_ldl_c: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_tg: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_EUR_vascular_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_all_cause_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_alzheimers_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_apoa: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_apob: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_ascvd: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_hdl_c: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_ldl_c: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_tg: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group marvel_ukb_MULTI_vascular_dementia: unstratified run, strata left out
[info]  2026-10-27 17:38:33 pooled run, study group thomassen: IVW of the strata
[stage] 2026-10-27 17:38:33 dedupe
[info]  2026-10-27 17:38:33 0 duplicate rows removed
[info]  2026-10-27 17:38:33 0 estimates removed as copies of another study
[stage] 2026-10-27 17:38:33 meta_analyse
[info]  2026-10-27 17:38:34 51 groups, 48 pooling more than one estimate
[info]  2026-10-27 17:38:35 347 groups, 0 pooling more than one estimate
[info]  2026-10-27 17:38:35 no gene burden (--no-gene-burden)
[stage] 2026-10-27 17:38:35 write
[info]  2026-10-27 17:38:35 wrote 398 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/meta_MULTI_selected_gof_multi.tsv.gz
[stage] 2026-10-27 17:38:35 apoe_strata_run
[info]  2026-10-27 17:38:35 252 rows from APOE strata: pooled per stratum
[stage] 2026-10-27 17:38:35 dedupe
[info]  2026-10-27 17:38:35 0 duplicate rows removed
[info]  2026-10-27 17:38:35 0 estimates removed as copies of another study
[stage] 2026-10-27 17:38:35 meta_analyse
[info]  2026-10-27 17:38:36 120 groups, 120 pooling more than one estimate
[info]  2026-10-27 17:38:36 252 groups, 0 pooling more than one estimate
[info]  2026-10-27 17:38:36 no gene burden (--no-gene-burden)
[stage] 2026-10-27 17:38:36 write
[info]  2026-10-27 17:38:36 wrote 372 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/meta_MULTI_selected_gof_multi_apoe_strata.tsv.gz

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

## [55] combine_variants (`/home/mvanvugt/projects/lipid_adem/src/combine_variants.py`)
- first run: 2026-10-21 13:50:41
- last run: 2026-10-27 14:48:49
- commit: `23ebede` (dirty)

Output:
```text
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/ptv_variants.tsv.gz: 527 PTVs
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/plp_variants.tsv: 1900 rows; /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-10-27 14:48:48 0 P/LP rows with ref = alt dropped
[warn]  2026-10-27 14:48:48 APOE condition 'Alzheimer disease 3, protection against, due to APOE3-Christchurch' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 APOA1 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 ANGPTL3 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 PPARA condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 PCSK9 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 HMGCR condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 NPC1L1 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 CETP condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 APOB condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-27 14:48:48 APOE condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[info]  2026-10-27 14:48:48 262 truncating P/LP variants set to lowering, 213 of them against their conditions
[info]  2026-10-27 14:48:48 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-10-27 14:48:48 ANGPTL3 ClinVar P/LP: 2 variants unknown
[info]  2026-10-27 14:48:48 APOA1 ClinVar P/LP: 11 variants altered
[info]  2026-10-27 14:48:48 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-10-27 14:48:48 APOA1 ClinVar P/LP: 16 variants lowering
[info]  2026-10-27 14:48:48 APOA1 ClinVar P/LP: 6 variants unknown
[info]  2026-10-27 14:48:48 APOB ClinVar P/LP: 5 variants altered
[info]  2026-10-27 14:48:48 APOB ClinVar P/LP: 6 variants conflicting
[info]  2026-10-27 14:48:48 APOB ClinVar P/LP: 224 variants lowering
[info]  2026-10-27 14:48:48 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-10-27 14:48:48 APOE ClinVar P/LP: 12 variants altered
[info]  2026-10-27 14:48:48 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-10-27 14:48:48 APOE ClinVar P/LP: 6 variants unknown
[info]  2026-10-27 14:48:48 CETP ClinVar P/LP: 10 variants lowering
[info]  2026-10-27 14:48:48 CETP ClinVar P/LP: 2 variants unknown
[info]  2026-10-27 14:48:48 HMGCR ClinVar P/LP: 6 variants lowering
[info]  2026-10-27 14:48:48 HMGCR ClinVar P/LP: 3 variants unknown
[info]  2026-10-27 14:48:48 NPC1L1 ClinVar P/LP: 2 variants unknown
[info]  2026-10-27 14:48:48 PCSK9 ClinVar P/LP: 2 variants lowering
[info]  2026-10-27 14:48:48 PCSK9 ClinVar P/LP: 16 variants raising
[info]  2026-10-27 14:48:48 PCSK9 ClinVar P/LP: 2 variants unknown
[info]  2026-10-27 14:48:48 PPARA ClinVar P/LP: 2 variants unknown
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/gof_variants.tsv: 47 GoF variants
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 17323 AM variants of class Benign/Likely Benign
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 8342 AM variants of class Pathogenic/Likely pathogenic
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 2874 AM variants of class Uncertain significance
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/am_variants.tsv: 8342 AM variants kept (Pathogenic/Likely pathogenic)
[info]  2026-10-27 14:48:48 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/selected_variants.tsv: 3 selected GoF variants
[warn]  2026-10-27 14:48:48 ANGPTL3 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 APOA1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 APOB ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 APOE ClinVar: 1 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 CETP ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 HMGCR ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 NPC1L1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 PCSK9 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-27 14:48:48 PPARA ClinVar: 2 rows without GRCh38 chr/pos/alleles
[info]  2026-10-27 14:48:48 normalisation AM: unchanged=8342
[info]  2026-10-27 14:48:48 normalisation ClinVar: no_sequence=20
[info]  2026-10-27 14:48:48 normalisation ClinVar: unchanged=316
[info]  2026-10-27 14:48:48 normalisation GoF: unchanged=19
[info]  2026-10-27 14:48:48 normalisation PTV: normalised=18
[info]  2026-10-27 14:48:48 normalisation PTV: unchanged=509
[info]  2026-10-27 14:48:48 normalisation SelectedGoF: unchanged=3
[info]  2026-10-27 14:48:48 67 sites are in several sources
[info]  2026-10-27 14:48:48 ANGPTL3 AM: 493 variants
[info]  2026-10-27 14:48:48 ANGPTL3 ClinVar: 12 variants
[info]  2026-10-27 14:48:48 ANGPTL3 PTV: 56 variants
[info]  2026-10-27 14:48:48 APOA1 ClinVar: 33 variants
[info]  2026-10-27 14:48:48 APOA1 PTV: 15 variants
[info]  2026-10-27 14:48:48 APOB ClinVar: 236 variants
[info]  2026-10-27 14:48:48 APOB PTV: 172 variants
[info]  2026-10-27 14:48:48 APOE ClinVar: 20 variants
[info]  2026-10-27 14:48:48 CETP AM: 439 variants
[info]  2026-10-27 14:48:48 CETP ClinVar: 10 variants
[info]  2026-10-27 14:48:48 CETP GoF: 1 variants
[info]  2026-10-27 14:48:48 CETP PTV: 58 variants
[info]  2026-10-27 14:48:48 CETP SelectedGoF: 3 variants
[info]  2026-10-27 14:48:48 HMGCR AM: 2623 variants
[info]  2026-10-27 14:48:48 HMGCR ClinVar: 7 variants
[info]  2026-10-27 14:48:48 HMGCR PTV: 39 variants
[info]  2026-10-27 14:48:48 NPC1L1 AM: 2507 variants
[info]  2026-10-27 14:48:48 NPC1L1 PTV: 96 variants
[info]  2026-10-27 14:48:48 PCSK9 AM: 737 variants
[info]  2026-10-27 14:48:48 PCSK9 ClinVar: 18 variants
[info]  2026-10-27 14:48:48 PCSK9 GoF: 18 variants
[info]  2026-10-27 14:48:48 PCSK9 PTV: 68 variants
[info]  2026-10-27 14:48:48 PPARA AM: 1543 variants
[info]  2026-10-27 14:48:48 PPARA PTV: 23 variants
[info]  2026-10-27 14:48:48 Wrote 9227 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-10-27 14:48:49 marvel lists: 9158 sites, 17 with an extra original-form row
[info]  2026-10-27 14:48:49 Wrote 556 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 46 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOA1_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 373 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOB_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 20 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOE_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 508 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 2668 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 2606 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 831 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[info]  2026-10-27 14:48:49 Wrote 1567 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv

```

## [90] archive_results (`src/archive_results.py --apply --tag 20261026_myriad`)
- first run: 2026-10-26 22:35:39
- last run: 2026-10-26 21:40:48
- commit: `a14bc5e`

Output:
```text
[stage] 2026-10-26 21:39:34 collect
[info]  2026-10-26 21:39:34 annotated_eur: 20 files (output current 10, output redundant 6, output stale 4)
[info]  2026-10-26 21:39:34 annotated_eur_unoriented: 20 files (output current 4, output redundant 12, output stale 4)
[info]  2026-10-26 21:39:34 broad_per_variant: 18 files (output current 5, output stale 13)
[info]  2026-10-26 21:39:34 early_snapshots: 3 files (output retired 3)
[info]  2026-10-26 21:39:34 lists_early: 24 files (output retired 24)
[info]  2026-10-26 21:39:34 maf_filter_all: 20 files (output current 10, output redundant 6, output stale 4)
[info]  2026-10-26 21:39:34 region_rare: 12 files (output current 12)
[stage] 2026-10-26 21:39:34 archive
[info]  2026-10-26 21:39:34 wrote 117 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/inventory.tsv.gz
[info]  2026-10-26 21:39:34 annotated_eur: 20 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/annotated_eur (output.tar.gz)
[info]  2026-10-26 21:39:34 annotated_eur_unoriented: 20 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/annotated_eur_unoriented (output.tar.gz)
[info]  2026-10-26 21:39:34 broad_per_variant: 18 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/broad_per_variant (output.tar.gz)
[info]  2026-10-26 21:40:01 early_snapshots: 3 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/early_snapshots (plain files)
[info]  2026-10-26 21:40:17 lists_early: 24 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/lists_early (output.tar.gz)
[info]  2026-10-26 21:40:24 maf_filter_all: 20 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/maf_filter_all (output.tar.gz)
[info]  2026-10-26 21:40:36 region_rare: 12 files -> /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/region_rare (output.tar.gz)
[info]  2026-10-26 21:40:42 wrote /myriadfs/home/rmgpmva/projects/lipid_adem/results/archive/20261026_myriad/README.md

```
