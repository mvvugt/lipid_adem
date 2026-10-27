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

## [10] subset_carriers (`validation/subset_carriers.py --carriers /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variant_extraction.tsv.gz --output /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step4na/PCSK9_carriers.tsv.gz --region chr1:1-999999999 --drop-merged --negative-to-na`)
- first run: 2026-10-26 16:12:11
- last run: 2026-10-27 09:44:08
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:38:09 chr1:1-999999999: 1047 of 1047 variant columns kept (0 merged names, drop_merged=True)
[info]  2026-10-27 09:44:08 wrote 469835 rows x 1048 columns to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/validation/step4na/PCSK9_carriers.tsv.gz
[info]  2026-10-27 09:44:08 negative values written as NA: 2834 cells
[info]  2026-10-27 09:44:08 value counts over variant cells: {'0': 490839574, '2': 763308, '1': 311529, 'NA': 2834}

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

## [25] marvel_results_table (`/home/mvanvugt/projects/lipid_adem/src/marvel_results_table.py --ancestry MULTI --tasks /home/mvanvugt/projects/lipid_adem/data/raw/marvel_tasks.tsv /home/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv`)
- first run: 2026-10-08 09:54:25
- last run: 2026-10-27 00:49:46
- commit: `244d529` (dirty)

Output:
```text
[stage] 2026-10-27 00:45:48 compare
[info]  2026-10-27 00:45:48 /home/mvanvugt/projects/lipid_adem/data/raw/marvel_tasks.tsv: 18 rows
[info]  2026-10-27 00:45:48 /home/mvanvugt/projects/lipid_adem/data/raw/marvel_burden_tasks.tsv: 24 rows
[info]  2026-10-27 00:45:48 6 genes over 2 task file(s)
[info]  2026-10-27 00:45:51 /home/mvanvugt/projects/lipid_adem/results/CETP: 667 loose result files
[info]  2026-10-27 00:45:56 /home/mvanvugt/projects/lipid_adem/results/CETP_all_apoe: 667 loose result files
[info]  2026-10-27 00:46:01 /home/mvanvugt/projects/lipid_adem/results/CETP_eur: 667 loose result files
[info]  2026-10-27 00:46:01 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_all_apoe: 12 loose result files
[info]  2026-10-27 00:46:01 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur: 12 loose result files
[info]  2026-10-27 00:46:01 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_all_apoe_fb: 12 loose result files
[info]  2026-10-27 00:46:01 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/CETP_eur_fb: 12 loose result files
[info]  2026-10-27 00:46:05 CETP: 1353840 loose rows, 1339320 new, 14520 already in the store
[warn]  2026-10-27 00:46:05 CETP: 1339320 rows added to CETP_results.tsv.gz (675 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-27 00:46:09 /home/mvanvugt/projects/lipid_adem/results/HMGCR: 714 loose result files
[info]  2026-10-27 00:46:14 /home/mvanvugt/projects/lipid_adem/results/HMGCR_all_apoe: 714 loose result files
[info]  2026-10-27 00:46:19 /home/mvanvugt/projects/lipid_adem/results/HMGCR_eur: 714 loose result files
[info]  2026-10-27 00:46:19 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_all_apoe: 11 loose result files
[info]  2026-10-27 00:46:19 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_eur: 11 loose result files
[info]  2026-10-27 00:46:19 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_all_apoe_fb: 11 loose result files
[info]  2026-10-27 00:46:19 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/HMGCR_eur_fb: 11 loose result files
[info]  2026-10-27 00:46:23 HMGCR: 1486520 loose rows, 1473840 new, 12680 already in the store
[warn]  2026-10-27 00:46:23 HMGCR: 1473840 rows added to HMGCR_results.tsv.gz (722 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-27 00:46:29 /home/mvanvugt/projects/lipid_adem/results/NPC1L1: 1257 loose result files
[info]  2026-10-27 00:46:38 /home/mvanvugt/projects/lipid_adem/results/NPC1L1_all_apoe: 1257 loose result files
[info]  2026-10-27 00:46:49 /home/mvanvugt/projects/lipid_adem/results/NPC1L1_eur: 1257 loose result files
[info]  2026-10-27 00:46:49 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_all_apoe: 9 loose result files
[info]  2026-10-27 00:46:49 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_eur: 9 loose result files
[info]  2026-10-27 00:46:49 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_all_apoe_fb: 9 loose result files
[info]  2026-10-27 00:46:49 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/NPC1L1_eur_fb: 9 loose result files
[info]  2026-10-27 00:46:54 NPC1L1: 2411650 loose rows, 2400760 new, 10890 already in the store
[warn]  2026-10-27 00:46:54 NPC1L1: 2400760 rows added to NPC1L1_results.tsv.gz (1265 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-27 00:46:58 /home/mvanvugt/projects/lipid_adem/results/PCSK9: 1047 loose result files
[info]  2026-10-27 00:47:05 /home/mvanvugt/projects/lipid_adem/results/PCSK9_all_apoe: 1047 loose result files
[info]  2026-10-27 00:47:12 /home/mvanvugt/projects/lipid_adem/results/PCSK9_eur: 1047 loose result files
[info]  2026-10-27 00:47:12 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_all_apoe: 10 loose result files
[info]  2026-10-27 00:47:12 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_eur: 10 loose result files
[info]  2026-10-27 00:47:12 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_all_apoe_fb: 10 loose result files
[info]  2026-10-27 00:47:12 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PCSK9_eur_fb: 10 loose result files
[info]  2026-10-27 00:47:17 PCSK9: 1975580 loose rows, 1963480 new, 12100 already in the store
[warn]  2026-10-27 00:47:17 PCSK9: 1963480 rows added to PCSK9_results.tsv.gz (1055 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-27 00:47:19 /home/mvanvugt/projects/lipid_adem/results/ANGPTL3: 324 loose result files
[info]  2026-10-27 00:47:22 /home/mvanvugt/projects/lipid_adem/results/ANGPTL3_all_apoe: 324 loose result files
[info]  2026-10-27 00:47:25 /home/mvanvugt/projects/lipid_adem/results/ANGPTL3_eur: 324 loose result files
[info]  2026-10-27 00:47:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_all_apoe: 11 loose result files
[info]  2026-10-27 00:47:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_eur: 11 loose result files
[info]  2026-10-27 00:47:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_all_apoe_fb: 11 loose result files
[info]  2026-10-27 00:47:25 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/ANGPTL3_eur_fb: 11 loose result files
[info]  2026-10-27 00:47:27 ANGPTL3: 665870 loose rows, 652560 new, 13310 already in the store
[warn]  2026-10-27 00:47:27 ANGPTL3: 652560 rows added to ANGPTL3_results.tsv.gz (332 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-27 00:47:29 /home/mvanvugt/projects/lipid_adem/results/PPARA: 343 loose result files
[info]  2026-10-27 00:47:31 /home/mvanvugt/projects/lipid_adem/results/PPARA_all_apoe: 343 loose result files
[info]  2026-10-27 00:47:35 /home/mvanvugt/projects/lipid_adem/results/PPARA_eur: 343 loose result files
[info]  2026-10-27 00:47:35 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_all_apoe: 9 loose result files
[info]  2026-10-27 00:47:35 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_eur: 9 loose result files
[info]  2026-10-27 00:47:35 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_all_apoe_fb: 9 loose result files
[info]  2026-10-27 00:47:35 /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel_burden/PPARA_eur_fb: 9 loose result files
[info]  2026-10-27 00:47:37 PPARA: 663890 loose rows, 653000 new, 10890 already in the store
[warn]  2026-10-27 00:47:37 PPARA: 653000 rows added to PPARA_results.tsv.gz (351 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44, overall; Variable: Apolipoprotein A_i0, Apolipoprotein B_i0, HDL cholesterol_i0, LDL direct_i0, Triglycerides_i0, all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[stage] 2026-10-27 00:47:37 write_stores
[info]  2026-10-27 00:47:56 CETP: wrote 1353840 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/CETP_results.tsv.gz
[info]  2026-10-27 00:48:15 HMGCR: wrote 1486520 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/HMGCR_results.tsv.gz
[info]  2026-10-27 00:48:46 NPC1L1: wrote 2411650 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/NPC1L1_results.tsv.gz
[info]  2026-10-27 00:49:10 PCSK9: wrote 1975580 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/PCSK9_results.tsv.gz
[info]  2026-10-27 00:49:19 ANGPTL3: wrote 665870 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/ANGPTL3_results.tsv.gz
[info]  2026-10-27 00:49:27 PPARA: wrote 663890 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/marvel/PPARA_results.tsv.gz
[stage] 2026-10-27 00:49:27 marvel_table
[info]  2026-10-27 00:49:29 ANGPTL3: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 00:49:32 CETP: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 00:49:35 HMGCR: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 00:49:39 NPC1L1: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 00:49:44 PCSK9: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 00:49:45 PPARA: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo
[info]  2026-10-27 00:49:45 wrote 600 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-10-27 00:49:45 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: all marvel strata already listed

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
- last run: 2026-10-27 01:12:17
- commit: `244d529` (dirty)

Output:
```text
[stage] 2026-10-27 00:50:28 load_sumstats
[warn]  2026-10-27 00:50:30 1 outfiles listed in /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/study_outcomes.tsv do not exist yet, skipped (first: /home/mvanvugt/projects/lipid_adem/data/temp/gwas_filtered/I9_CVD_HARD_result.tsv.gz)
[info]  2026-10-27 00:50:30 summary-stats: 124 files, 593027 rows incl. one copy per outcome (1 missing)
[info]  2026-10-27 00:50:36 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-27 00:50:36 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-27 00:50:36 marvel
[info]  2026-10-27 00:50:39 marvel ukb apoa: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb apoa: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb apoa: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:39 marvel ukb apob: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb apob: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb apob: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:39 marvel ukb hdl_c: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb hdl_c: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb hdl_c: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:39 marvel ukb ldl_c: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb ldl_c: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:39 marvel ukb ldl_c: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:40 marvel ukb tg: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb tg: 1092 rows -> 111 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb tg: 970 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:40 marvel ukb all_cause_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb all_cause_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb all_cause_dementia: 34 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb all_cause_dementia: 1079 rows -> 74 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb all_cause_dementia: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:40 marvel ukb alzheimers_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb alzheimers_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb alzheimers_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb alzheimers_dementia: 1173 rows -> 69 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb alzheimers_dementia: 1082 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:40 marvel ukb vascular_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb vascular_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb vascular_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb vascular_dementia: 1074 rows -> 69 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb vascular_dementia: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:40 marvel ukb frontotemporal_dementia: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb frontotemporal_dementia: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb frontotemporal_dementia: 49 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb frontotemporal_dementia: 1064 rows -> 64 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb frontotemporal_dementia: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:40 marvel ukb ascvd: 1899 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb ascvd: 3 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb ascvd: 11 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb ascvd: 1102 rows -> 97 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:40 marvel ukb ascvd: 994 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb apoa: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb apoa: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb apoa: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb apob: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb apob: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb apob: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb hdl_c: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb hdl_c: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb hdl_c: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb ldl_c: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb ldl_c: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb ldl_c: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb tg: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb tg: 797 rows -> 286 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb tg: 500 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb all_cause_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb all_cause_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb all_cause_dementia: 41 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb all_cause_dementia: 2429 rows -> 15 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb all_cause_dementia: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:41 marvel ukb alzheimers_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb alzheimers_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb alzheimers_dementia: 50 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb alzheimers_dementia: 2519 rows -> 11 variant rows, 12 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:41 marvel ukb alzheimers_dementia: 2496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:42 marvel ukb vascular_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb vascular_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb vascular_dementia: 56 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb vascular_dementia: 2414 rows -> 6 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb vascular_dementia: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:42 marvel ukb frontotemporal_dementia: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb frontotemporal_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb frontotemporal_dementia: 60 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb frontotemporal_dementia: 2410 rows -> 2 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb frontotemporal_dementia: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:42 marvel ukb ascvd: 306 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb ascvd: 239 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb ascvd: 32 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb ascvd: 2438 rows -> 19 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb ascvd: 2408 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:42 marvel ukb apoa: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb apoa: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb apoa: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:42 marvel ukb apob: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb apob: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb apob: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:42 marvel ukb hdl_c: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb hdl_c: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:42 marvel ukb hdl_c: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb ldl_c: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb ldl_c: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb ldl_c: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb tg: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb tg: 1251 rows -> 200 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb tg: 1040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb all_cause_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb all_cause_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb all_cause_dementia: 77 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb all_cause_dementia: 1741 rows -> 42 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb all_cause_dementia: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb alzheimers_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb alzheimers_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb alzheimers_dementia: 88 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb alzheimers_dementia: 1829 rows -> 31 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb alzheimers_dementia: 1776 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb vascular_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb vascular_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb vascular_dementia: 94 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb vascular_dementia: 1724 rows -> 25 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb vascular_dementia: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb frontotemporal_dementia: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb frontotemporal_dementia: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb frontotemporal_dementia: 103 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb frontotemporal_dementia: 1715 rows -> 21 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb frontotemporal_dementia: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:43 marvel ukb ascvd: 1116 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb ascvd: 81 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:43 marvel ukb ascvd: 50 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb ascvd: 1768 rows -> 69 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb ascvd: 1688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:44 marvel ukb apoa: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb apoa: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb apoa: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:44 marvel ukb apob: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb apob: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb apob: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:44 marvel ukb hdl_c: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb hdl_c: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb hdl_c: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:44 marvel ukb ldl_c: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb ldl_c: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb ldl_c: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:44 marvel ukb tg: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb tg: 1226 rows -> 158 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb tg: 1057 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:44 marvel ukb all_cause_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb all_cause_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:44 marvel ukb all_cause_dementia: 65 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb all_cause_dementia: 1427 rows -> 56 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb all_cause_dementia: 1360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:45 marvel ukb alzheimers_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb alzheimers_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb alzheimers_dementia: 74 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb alzheimers_dementia: 1517 rows -> 49 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb alzheimers_dementia: 1448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:45 marvel ukb vascular_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb vascular_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb vascular_dementia: 74 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb vascular_dementia: 1418 rows -> 47 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb vascular_dementia: 1360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:45 marvel ukb frontotemporal_dementia: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb frontotemporal_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb frontotemporal_dementia: 91 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb frontotemporal_dementia: 1401 rows -> 41 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb frontotemporal_dementia: 1360 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:45 marvel ukb ascvd: 1485 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb ascvd: 38 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb ascvd: 30 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb ascvd: 1462 rows -> 90 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb ascvd: 1361 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:45 marvel ukb apoa: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb apoa: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb apoa: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:45 marvel ukb apob: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb apob: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:45 marvel ukb apob: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb hdl_c: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb hdl_c: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb hdl_c: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb ldl_c: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb ldl_c: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb ldl_c: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb tg: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb tg: 1212 rows -> 230 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb tg: 971 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb all_cause_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb all_cause_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb all_cause_dementia: 99 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb all_cause_dementia: 1974 rows -> 11 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb all_cause_dementia: 1952 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb alzheimers_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb alzheimers_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb alzheimers_dementia: 104 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb alzheimers_dementia: 2068 rows -> 8 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb alzheimers_dementia: 2040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb vascular_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb vascular_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb vascular_dementia: 111 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb vascular_dementia: 1962 rows -> 10 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb vascular_dementia: 1952 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:46 marvel ukb frontotemporal_dementia: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb frontotemporal_dementia: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:46 marvel ukb frontotemporal_dementia: 117 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb frontotemporal_dementia: 1956 rows -> 4 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb frontotemporal_dementia: 1952 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:47 marvel ukb ascvd: 819 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb ascvd: 123 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb ascvd: 68 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb ascvd: 2005 rows -> 41 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb ascvd: 1953 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:47 marvel ukb apoa: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb apoa: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb apoa: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:47 marvel ukb apob: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb apob: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb apob: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:47 marvel ukb hdl_c: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb hdl_c: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb hdl_c: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:47 marvel ukb ldl_c: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb ldl_c: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb ldl_c: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:47 marvel ukb tg: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb tg: 1546 rows -> 181 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:47 marvel ukb tg: 1354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:48 marvel ukb all_cause_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb all_cause_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb all_cause_dementia: 86 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb all_cause_dementia: 1635 rows -> 70 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb all_cause_dementia: 1554 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:48 marvel ukb alzheimers_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb alzheimers_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb alzheimers_dementia: 94 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb alzheimers_dementia: 1726 rows -> 62 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb alzheimers_dementia: 1642 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:48 marvel ukb vascular_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb vascular_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb vascular_dementia: 100 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb vascular_dementia: 1621 rows -> 57 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb vascular_dementia: 1553 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:48 marvel ukb frontotemporal_dementia: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb frontotemporal_dementia: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb frontotemporal_dementia: 112 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb frontotemporal_dementia: 1609 rows -> 50 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb frontotemporal_dementia: 1553 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:48 marvel ukb ascvd: 1269 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb ascvd: 25 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb ascvd: 53 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb ascvd: 1668 rows -> 103 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb ascvd: 1554 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:48 marvel ukb apoa: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb apoa: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:48 marvel ukb apoa: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb apob: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb apob: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb apob: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb hdl_c: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb hdl_c: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb hdl_c: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb ldl_c: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb ldl_c: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb ldl_c: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb tg: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb tg: 754 rows -> 291 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb tg: 452 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb all_cause_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb all_cause_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb all_cause_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb all_cause_dementia: 2465 rows -> 11 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb all_cause_dementia: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb alzheimers_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb alzheimers_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb alzheimers_dementia: 48 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb alzheimers_dementia: 2555 rows -> 7 variant rows, 12 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb alzheimers_dementia: 2536 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:49 marvel ukb vascular_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb vascular_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb vascular_dementia: 51 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb vascular_dementia: 2453 rows -> 5 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:49 marvel ukb vascular_dementia: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:50 marvel ukb frontotemporal_dementia: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb frontotemporal_dementia: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb frontotemporal_dementia: 54 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb frontotemporal_dementia: 2450 rows -> 2 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb frontotemporal_dementia: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:50 marvel ukb ascvd: 261 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb ascvd: 250 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb ascvd: 31 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb ascvd: 2473 rows -> 14 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb ascvd: 2448 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:50 marvel ukb apoa: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb apoa: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb apoa: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:50 marvel ukb apob: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb apob: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb apob: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:50 marvel ukb hdl_c: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb hdl_c: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb hdl_c: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:50 marvel ukb ldl_c: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb ldl_c: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:50 marvel ukb ldl_c: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb tg: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb tg: 1337 rows -> 229 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb tg: 1097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb all_cause_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb all_cause_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb all_cause_dementia: 87 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb all_cause_dementia: 1978 rows -> 38 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb all_cause_dementia: 1929 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb alzheimers_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb alzheimers_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb alzheimers_dementia: 96 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb alzheimers_dementia: 2068 rows -> 29 variant rows, 22 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb alzheimers_dementia: 2017 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb vascular_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb vascular_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb vascular_dementia: 106 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb vascular_dementia: 1959 rows -> 20 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb vascular_dementia: 1928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb frontotemporal_dementia: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb frontotemporal_dementia: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb frontotemporal_dementia: 114 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb frontotemporal_dementia: 1951 rows -> 17 variant rows, 6 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb frontotemporal_dementia: 1928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb ascvd: 846 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb ascvd: 104 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb ascvd: 60 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb ascvd: 2005 rows -> 65 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:51 marvel ukb ascvd: 1929 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:51 marvel ukb apoa: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb apoa: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb apoa: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:52 marvel ukb apob: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb apob: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb apob: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:52 marvel ukb hdl_c: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb hdl_c: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb hdl_c: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:52 marvel ukb ldl_c: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb ldl_c: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb ldl_c: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:52 marvel ukb tg: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb tg: 1478 rows -> 218 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb tg: 1249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:52 marvel ukb all_cause_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb all_cause_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb all_cause_dementia: 96 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb all_cause_dementia: 1900 rows -> 49 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb all_cause_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:52 marvel ukb alzheimers_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb alzheimers_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb alzheimers_dementia: 109 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb alzheimers_dementia: 1986 rows -> 38 variant rows, 20 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:52 marvel ukb alzheimers_dementia: 1928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:53 marvel ukb vascular_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb vascular_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb vascular_dementia: 104 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb vascular_dementia: 1892 rows -> 41 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb vascular_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:53 marvel ukb frontotemporal_dementia: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb frontotemporal_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb frontotemporal_dementia: 123 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb frontotemporal_dementia: 1873 rows -> 33 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb frontotemporal_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:53 marvel ukb ascvd: 945 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb ascvd: 74 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb ascvd: 54 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb ascvd: 1942 rows -> 90 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb ascvd: 1841 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:53 marvel ukb apoa: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb apoa: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb apoa: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:53 marvel ukb apob: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb apob: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb apob: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:53 marvel ukb hdl_c: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb hdl_c: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:53 marvel ukb hdl_c: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb ldl_c: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb ldl_c: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb ldl_c: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb tg: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb tg: 1247 rows -> 249 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb tg: 987 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb all_cause_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb all_cause_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb all_cause_dementia: 102 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb all_cause_dementia: 2125 rows -> 11 variant rows, 10 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb all_cause_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb alzheimers_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb alzheimers_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb alzheimers_dementia: 126 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb alzheimers_dementia: 2200 rows -> 8 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb alzheimers_dementia: 2192 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb vascular_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb vascular_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb vascular_dementia: 116 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb vascular_dementia: 2111 rows -> 7 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb vascular_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb frontotemporal_dementia: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb frontotemporal_dementia: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb frontotemporal_dementia: 119 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb frontotemporal_dementia: 2108 rows -> 4 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb frontotemporal_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:50:54 marvel ukb ascvd: 648 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb ascvd: 140 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb ascvd: 68 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb ascvd: 2159 rows -> 43 variant rows, 11 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-27 00:50:54 marvel ukb ascvd: 2105 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:00 marvel ukb apoa: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:00 marvel ukb apoa: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:00 marvel ukb apoa: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:00 marvel ukb apob: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:00 marvel ukb apob: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:00 marvel ukb apob: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:00 marvel ukb hdl_c: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:00 marvel ukb hdl_c: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:00 marvel ukb hdl_c: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:01 marvel ukb ldl_c: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb ldl_c: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb ldl_c: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:01 marvel ukb tg: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb tg: 2588 rows -> 208 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb tg: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:01 marvel ukb all_cause_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb all_cause_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb all_cause_dementia: 43 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb all_cause_dementia: 2706 rows -> 160 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb all_cause_dementia: 2536 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:01 marvel ukb alzheimers_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb alzheimers_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb alzheimers_dementia: 67 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb alzheimers_dementia: 2790 rows -> 147 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:01 marvel ukb alzheimers_dementia: 2623 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:02 marvel ukb vascular_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb vascular_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb vascular_dementia: 64 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb vascular_dementia: 2685 rows -> 142 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb vascular_dementia: 2533 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:02 marvel ukb frontotemporal_dementia: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb frontotemporal_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb frontotemporal_dementia: 98 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb frontotemporal_dementia: 2651 rows -> 122 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb frontotemporal_dementia: 2522 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:02 marvel ukb ascvd: 3339 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb ascvd: 23 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb ascvd: 18 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb ascvd: 2731 rows -> 178 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:02 marvel ukb ascvd: 2541 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:03 marvel ukb apoa: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb apoa: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb apoa: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:03 marvel ukb apob: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb apob: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb apob: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:03 marvel ukb hdl_c: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb hdl_c: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb hdl_c: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:03 marvel ukb ldl_c: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb ldl_c: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:03 marvel ukb ldl_c: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:04 marvel ukb tg: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb tg: 1491 rows -> 420 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb tg: 1061 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:04 marvel ukb all_cause_dementia: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb all_cause_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb all_cause_dementia: 55 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb all_cause_dementia: 4817 rows -> 45 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb all_cause_dementia: 4765 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:04 marvel ukb alzheimers_dementia: 774 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb alzheimers_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb alzheimers_dementia: 66 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb alzheimers_dementia: 4896 rows -> 37 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:04 marvel ukb alzheimers_dementia: 4845 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:05 marvel ukb vascular_dementia: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb vascular_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb vascular_dementia: 80 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb vascular_dementia: 4792 rows -> 32 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb vascular_dementia: 4759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:05 marvel ukb frontotemporal_dementia: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb frontotemporal_dementia: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb frontotemporal_dementia: 89 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb frontotemporal_dementia: 4783 rows -> 24 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb frontotemporal_dementia: 4758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:05 marvel ukb ascvd: 756 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb ascvd: 483 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb ascvd: 52 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb ascvd: 4820 rows -> 45 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb ascvd: 4768 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:05 marvel ukb apoa: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb apoa: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:05 marvel ukb apoa: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:06 marvel ukb apob: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:06 marvel ukb apob: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:06 marvel ukb apob: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:06 marvel ukb hdl_c: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:06 marvel ukb hdl_c: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:06 marvel ukb hdl_c: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:06 marvel ukb ldl_c: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb ldl_c: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb ldl_c: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:07 marvel ukb tg: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb tg: 2598 rows -> 320 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb tg: 2266 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:07 marvel ukb all_cause_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb all_cause_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb all_cause_dementia: 154 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb all_cause_dementia: 3746 rows -> 87 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:07 marvel ukb all_cause_dementia: 3649 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:08 marvel ukb alzheimers_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb alzheimers_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb alzheimers_dementia: 165 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb alzheimers_dementia: 3843 rows -> 79 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb alzheimers_dementia: 3744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:08 marvel ukb vascular_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb vascular_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb vascular_dementia: 192 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb vascular_dementia: 3708 rows -> 64 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb vascular_dementia: 3643 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:08 marvel ukb frontotemporal_dementia: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb frontotemporal_dementia: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb frontotemporal_dementia: 208 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb frontotemporal_dementia: 3692 rows -> 49 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb frontotemporal_dementia: 3642 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:08 marvel ukb ascvd: 2025 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb ascvd: 186 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:08 marvel ukb ascvd: 94 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb ascvd: 3806 rows -> 126 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb ascvd: 3670 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:09 marvel ukb apoa: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb apoa: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb apoa: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:09 marvel ukb apob: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb apob: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb apob: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:09 marvel ukb hdl_c: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb hdl_c: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:09 marvel ukb hdl_c: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:10 marvel ukb ldl_c: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb ldl_c: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb ldl_c: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:10 marvel ukb tg: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb tg: 2792 rows -> 248 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb tg: 2532 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:10 marvel ukb all_cause_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb all_cause_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb all_cause_dementia: 105 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb all_cause_dementia: 3142 rows -> 128 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb all_cause_dementia: 3004 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:10 marvel ukb alzheimers_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb alzheimers_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:10 marvel ukb alzheimers_dementia: 153 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb alzheimers_dementia: 3202 rows -> 110 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb alzheimers_dementia: 3090 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:11 marvel ukb vascular_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb vascular_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb vascular_dementia: 125 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb vascular_dementia: 3122 rows -> 113 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb vascular_dementia: 3002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:11 marvel ukb frontotemporal_dementia: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb frontotemporal_dementia: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb frontotemporal_dementia: 149 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb frontotemporal_dementia: 3098 rows -> 99 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb frontotemporal_dementia: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:11 marvel ukb ascvd: 2799 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb ascvd: 65 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb ascvd: 58 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb ascvd: 3189 rows -> 161 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:11 marvel ukb ascvd: 3016 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:12 marvel ukb apoa: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb apoa: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb apoa: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:12 marvel ukb apob: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb apob: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb apob: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:12 marvel ukb hdl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb hdl_c: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb hdl_c: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:12 marvel ukb ldl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb ldl_c: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:12 marvel ukb ldl_c: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:13 marvel ukb tg: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb tg: 2380 rows -> 348 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb tg: 2020 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:13 marvel ukb all_cause_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb all_cause_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb all_cause_dementia: 168 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb all_cause_dementia: 4004 rows -> 56 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb all_cause_dementia: 3941 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:13 marvel ukb alzheimers_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb alzheimers_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb alzheimers_dementia: 198 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb alzheimers_dementia: 4082 rows -> 46 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:13 marvel ukb alzheimers_dementia: 4034 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:14 marvel ukb vascular_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb vascular_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb vascular_dementia: 185 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb vascular_dementia: 3987 rows -> 42 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb vascular_dementia: 3938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:14 marvel ukb frontotemporal_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb frontotemporal_dementia: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb frontotemporal_dementia: 202 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb frontotemporal_dementia: 3970 rows -> 32 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb frontotemporal_dementia: 3937 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:14 marvel ukb ascvd: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb ascvd: 256 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb ascvd: 113 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb ascvd: 4059 rows -> 87 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb ascvd: 3960 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:14 marvel ukb apoa: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb apoa: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:14 marvel ukb apoa: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:15 marvel ukb apob: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:15 marvel ukb apob: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:15 marvel ukb apob: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:15 marvel ukb hdl_c: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:15 marvel ukb hdl_c: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:15 marvel ukb hdl_c: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:15 marvel ukb ldl_c: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:15 marvel ukb ldl_c: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:15 marvel ukb ldl_c: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:16 marvel ukb tg: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb tg: 3326 rows -> 286 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb tg: 3028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:16 marvel ukb all_cause_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb all_cause_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb all_cause_dementia: 161 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb all_cause_dementia: 3704 rows -> 129 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb all_cause_dementia: 3565 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:16 marvel ukb alzheimers_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb alzheimers_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb alzheimers_dementia: 183 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb alzheimers_dementia: 3790 rows -> 117 variant rows, 20 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb alzheimers_dementia: 3653 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:16 marvel ukb vascular_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb vascular_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb vascular_dementia: 183 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb vascular_dementia: 3682 rows -> 112 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:16 marvel ukb vascular_dementia: 3560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:17 marvel ukb frontotemporal_dementia: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb frontotemporal_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb frontotemporal_dementia: 209 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb frontotemporal_dementia: 3656 rows -> 96 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb frontotemporal_dementia: 3553 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:17 marvel ukb ascvd: 2169 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb ascvd: 77 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb ascvd: 80 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb ascvd: 3785 rows -> 175 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb ascvd: 3598 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:17 marvel ukb apoa: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb apoa: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:17 marvel ukb apoa: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:18 marvel ukb apob: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb apob: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb apob: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:18 marvel ukb hdl_c: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb hdl_c: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb hdl_c: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:18 marvel ukb ldl_c: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb ldl_c: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb ldl_c: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:18 marvel ukb tg: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb tg: 1363 rows -> 421 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:18 marvel ukb tg: 932 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:19 marvel ukb all_cause_dementia: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb all_cause_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb all_cause_dementia: 53 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb all_cause_dementia: 4866 rows -> 31 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb all_cause_dementia: 4828 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:19 marvel ukb alzheimers_dementia: 702 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb alzheimers_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb alzheimers_dementia: 63 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb alzheimers_dementia: 4946 rows -> 25 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb alzheimers_dementia: 4907 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:19 marvel ukb vascular_dementia: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb vascular_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb vascular_dementia: 73 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb vascular_dementia: 4846 rows -> 23 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:19 marvel ukb vascular_dementia: 4822 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:20 marvel ukb frontotemporal_dementia: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb frontotemporal_dementia: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb frontotemporal_dementia: 77 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb frontotemporal_dementia: 4842 rows -> 19 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb frontotemporal_dementia: 4822 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:20 marvel ukb ascvd: 684 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb ascvd: 508 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb ascvd: 47 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb ascvd: 4872 rows -> 33 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb ascvd: 4832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:20 marvel ukb apoa: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb apoa: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb apoa: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:20 marvel ukb apob: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb apob: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:20 marvel ukb apob: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:21 marvel ukb hdl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:21 marvel ukb hdl_c: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:21 marvel ukb hdl_c: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:21 marvel ukb ldl_c: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:21 marvel ukb ldl_c: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:21 marvel ukb ldl_c: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:21 marvel ukb tg: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:21 marvel ukb tg: 2516 rows -> 350 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:21 marvel ukb tg: 2154 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:22 marvel ukb all_cause_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb all_cause_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb all_cause_dementia: 162 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb all_cause_dementia: 4027 rows -> 67 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb all_cause_dementia: 3950 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:22 marvel ukb alzheimers_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb alzheimers_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb alzheimers_dementia: 179 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb alzheimers_dementia: 4118 rows -> 58 variant rows, 14 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb alzheimers_dementia: 4046 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:22 marvel ukb vascular_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb vascular_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb vascular_dementia: 189 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb vascular_dementia: 4000 rows -> 53 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb vascular_dementia: 3946 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:22 marvel ukb frontotemporal_dementia: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb frontotemporal_dementia: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:22 marvel ukb frontotemporal_dementia: 203 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb frontotemporal_dementia: 3986 rows -> 39 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb frontotemporal_dementia: 3946 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:23 marvel ukb ascvd: 1683 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb ascvd: 239 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb ascvd: 92 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb ascvd: 4097 rows -> 115 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb ascvd: 3972 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:23 marvel ukb apoa: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb apoa: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb apoa: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:23 marvel ukb apob: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb apob: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:23 marvel ukb apob: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:24 marvel ukb hdl_c: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb hdl_c: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb hdl_c: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:24 marvel ukb ldl_c: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb ldl_c: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb ldl_c: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:24 marvel ukb tg: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb tg: 3116 rows -> 305 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb tg: 2799 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:24 marvel ukb all_cause_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb all_cause_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:24 marvel ukb all_cause_dementia: 178 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb all_cause_dementia: 3771 rows -> 102 variant rows, 10 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb all_cause_dementia: 3659 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:25 marvel ukb alzheimers_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb alzheimers_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb alzheimers_dementia: 223 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb alzheimers_dementia: 3834 rows -> 86 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb alzheimers_dementia: 3746 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:25 marvel ukb vascular_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb vascular_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb vascular_dementia: 202 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb vascular_dementia: 3747 rows -> 86 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb vascular_dementia: 3654 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:25 marvel ukb frontotemporal_dementia: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb frontotemporal_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb frontotemporal_dementia: 216 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb frontotemporal_dementia: 3733 rows -> 78 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:25 marvel ukb frontotemporal_dementia: 3648 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:26 marvel ukb ascvd: 2043 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb ascvd: 119 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb ascvd: 113 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb ascvd: 3836 rows -> 141 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb ascvd: 3683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:26 marvel ukb apoa: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb apoa: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb apoa: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:26 marvel ukb apob: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb apob: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:26 marvel ukb apob: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:26 marvel ukb hdl_c: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb hdl_c: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb hdl_c: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:27 marvel ukb ldl_c: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb ldl_c: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb ldl_c: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:27 marvel ukb tg: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb tg: 2229 rows -> 370 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb tg: 1847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:27 marvel ukb all_cause_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb all_cause_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb all_cause_dementia: 157 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb all_cause_dementia: 4256 rows -> 45 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:27 marvel ukb all_cause_dementia: 4204 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:28 marvel ukb alzheimers_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb alzheimers_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb alzheimers_dementia: 183 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb alzheimers_dementia: 4338 rows -> 38 variant rows, 2 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb alzheimers_dementia: 4298 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:28 marvel ukb vascular_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb vascular_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb vascular_dementia: 169 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb vascular_dementia: 4244 rows -> 36 variant rows, 7 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb vascular_dementia: 4201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:28 marvel ukb frontotemporal_dementia: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb frontotemporal_dementia: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb frontotemporal_dementia: 180 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb frontotemporal_dementia: 4233 rows -> 31 variant rows, 1 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb frontotemporal_dementia: 4201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:28 marvel ukb ascvd: 1386 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb ascvd: 312 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb ascvd: 100 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb ascvd: 4313 rows -> 76 variant rows, 12 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-27 00:51:28 marvel ukb ascvd: 4225 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:34 marvel ukb apoa: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:34 marvel ukb apoa: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:34 marvel ukb apoa: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:35 marvel ukb apob: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb apob: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb apob: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:35 marvel ukb hdl_c: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb hdl_c: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb hdl_c: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:35 marvel ukb ldl_c: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb ldl_c: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb ldl_c: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:35 marvel ukb tg: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb tg: 1484 rows -> 116 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:35 marvel ukb tg: 1357 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:36 marvel ukb all_cause_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb all_cause_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb all_cause_dementia: 54 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb all_cause_dementia: 1486 rows -> 87 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb all_cause_dementia: 1390 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:36 marvel ukb alzheimers_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb alzheimers_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb alzheimers_dementia: 59 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb alzheimers_dementia: 1580 rows -> 84 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb alzheimers_dementia: 1478 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:36 marvel ukb vascular_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb vascular_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb vascular_dementia: 68 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb vascular_dementia: 1472 rows -> 79 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:36 marvel ukb vascular_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:37 marvel ukb frontotemporal_dementia: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb frontotemporal_dementia: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb frontotemporal_dementia: 75 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb frontotemporal_dementia: 1465 rows -> 75 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb frontotemporal_dementia: 1384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:37 marvel ukb ascvd: 4977 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb ascvd: 8 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb ascvd: 16 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb ascvd: 1524 rows -> 101 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb ascvd: 1412 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:37 marvel ukb apoa: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb apoa: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:37 marvel ukb apoa: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:38 marvel ukb apob: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:38 marvel ukb apob: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:38 marvel ukb apob: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:38 marvel ukb hdl_c: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:38 marvel ukb hdl_c: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:38 marvel ukb hdl_c: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:38 marvel ukb ldl_c: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:38 marvel ukb ldl_c: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:38 marvel ukb ldl_c: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:39 marvel ukb tg: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb tg: 2459 rows -> 398 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb tg: 2050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:39 marvel ukb all_cause_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb all_cause_dementia: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb all_cause_dementia: 161 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb all_cause_dementia: 5588 rows -> 25 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb all_cause_dementia: 5557 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:39 marvel ukb alzheimers_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb alzheimers_dementia: 475 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb alzheimers_dementia: 185 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb alzheimers_dementia: 5658 rows -> 18 variant rows, 12 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:39 marvel ukb alzheimers_dementia: 5628 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:40 marvel ukb vascular_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb vascular_dementia: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb vascular_dementia: 215 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb vascular_dementia: 5534 rows -> 6 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb vascular_dementia: 5528 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:40 marvel ukb frontotemporal_dementia: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb frontotemporal_dementia: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb frontotemporal_dementia: 220 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb frontotemporal_dementia: 5529 rows -> 1 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb frontotemporal_dementia: 5528 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:40 marvel ukb ascvd: 306 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb ascvd: 470 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb ascvd: 154 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb ascvd: 5595 rows -> 32 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb ascvd: 5557 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:40 marvel ukb apoa: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb apoa: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:40 marvel ukb apoa: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:41 marvel ukb apob: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:41 marvel ukb apob: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:41 marvel ukb apob: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:41 marvel ukb hdl_c: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:41 marvel ukb hdl_c: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:41 marvel ukb hdl_c: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:41 marvel ukb ldl_c: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:41 marvel ukb ldl_c: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:41 marvel ukb ldl_c: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:42 marvel ukb tg: 2250 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb tg: 3043 rows -> 283 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb tg: 2749 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:42 marvel ukb all_cause_dementia: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb all_cause_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb all_cause_dementia: 213 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb all_cause_dementia: 3892 rows -> 60 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb all_cause_dementia: 3823 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:42 marvel ukb alzheimers_dementia: 2286 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb alzheimers_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb alzheimers_dementia: 242 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb alzheimers_dementia: 3944 rows -> 44 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:42 marvel ukb alzheimers_dementia: 3882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:43 marvel ukb vascular_dementia: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb vascular_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb vascular_dementia: 276 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb vascular_dementia: 3829 rows -> 30 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb vascular_dementia: 3790 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:43 marvel ukb frontotemporal_dementia: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb frontotemporal_dementia: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb frontotemporal_dementia: 294 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb frontotemporal_dementia: 3811 rows -> 19 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb frontotemporal_dementia: 3792 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:43 marvel ukb ascvd: 2268 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb ascvd: 152 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb ascvd: 135 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb ascvd: 3970 rows -> 108 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:43 marvel ukb ascvd: 3853 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:44 marvel ukb apoa: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:44 marvel ukb apoa: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:44 marvel ukb apoa: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:44 marvel ukb apob: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:44 marvel ukb apob: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:44 marvel ukb apob: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:44 marvel ukb hdl_c: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:44 marvel ukb hdl_c: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:44 marvel ukb hdl_c: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:45 marvel ukb ldl_c: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb ldl_c: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb ldl_c: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:45 marvel ukb tg: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb tg: 2482 rows -> 185 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb tg: 2287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:45 marvel ukb all_cause_dementia: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb all_cause_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb all_cause_dementia: 172 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb all_cause_dementia: 2674 rows -> 61 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb all_cause_dementia: 2604 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:45 marvel ukb alzheimers_dementia: 3636 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb alzheimers_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:45 marvel ukb alzheimers_dementia: 216 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb alzheimers_dementia: 2720 rows -> 50 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb alzheimers_dementia: 2670 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:46 marvel ukb vascular_dementia: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb vascular_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb vascular_dementia: 209 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb vascular_dementia: 2637 rows -> 47 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb vascular_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:46 marvel ukb frontotemporal_dementia: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb frontotemporal_dementia: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb frontotemporal_dementia: 214 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb frontotemporal_dementia: 2632 rows -> 42 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb frontotemporal_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:46 marvel ukb ascvd: 3627 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb ascvd: 52 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb ascvd: 74 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb ascvd: 2772 rows -> 105 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:46 marvel ukb ascvd: 2657 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:47 marvel ukb apoa: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:47 marvel ukb apoa: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:47 marvel ukb apoa: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:47 marvel ukb apob: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:47 marvel ukb apob: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:47 marvel ukb apob: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:47 marvel ukb hdl_c: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:47 marvel ukb hdl_c: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:47 marvel ukb hdl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:48 marvel ukb ldl_c: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb ldl_c: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb ldl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:48 marvel ukb tg: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb tg: 3225 rows -> 330 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb tg: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:48 marvel ukb all_cause_dementia: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb all_cause_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb all_cause_dementia: 285 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb all_cause_dementia: 4536 rows -> 27 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:48 marvel ukb all_cause_dementia: 4503 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:49 marvel ukb alzheimers_dementia: 1494 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb alzheimers_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb alzheimers_dementia: 326 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb alzheimers_dementia: 4576 rows -> 16 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb alzheimers_dementia: 4560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:49 marvel ukb vascular_dementia: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb vascular_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb vascular_dementia: 313 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb vascular_dementia: 4508 rows -> 12 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb vascular_dementia: 4496 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:49 marvel ukb frontotemporal_dementia: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb frontotemporal_dementia: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb frontotemporal_dementia: 324 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb frontotemporal_dementia: 4497 rows -> 9 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb frontotemporal_dementia: 4488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:49 marvel ukb ascvd: 1476 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb ascvd: 228 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:49 marvel ukb ascvd: 180 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb ascvd: 4641 rows -> 80 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb ascvd: 4552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:50 marvel ukb apoa: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb apoa: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb apoa: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:50 marvel ukb apob: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb apob: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb apob: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:50 marvel ukb hdl_c: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb hdl_c: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:50 marvel ukb hdl_c: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:51 marvel ukb ldl_c: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:51 marvel ukb ldl_c: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:51 marvel ukb ldl_c: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:51 marvel ukb tg: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:51 marvel ukb tg: 2140 rows -> 190 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:51 marvel ukb tg: 1939 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:52 marvel ukb all_cause_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb all_cause_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb all_cause_dementia: 133 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb all_cause_dementia: 2245 rows -> 78 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb all_cause_dementia: 2158 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:52 marvel ukb alzheimers_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb alzheimers_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb alzheimers_dementia: 140 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb alzheimers_dementia: 2337 rows -> 73 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb alzheimers_dementia: 2246 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:52 marvel ukb vascular_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb vascular_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb vascular_dementia: 155 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb vascular_dementia: 2223 rows -> 65 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:52 marvel ukb vascular_dementia: 2152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:53 marvel ukb frontotemporal_dementia: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb frontotemporal_dementia: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb frontotemporal_dementia: 162 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb frontotemporal_dementia: 2216 rows -> 58 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb frontotemporal_dementia: 2152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:53 marvel ukb ascvd: 4113 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb ascvd: 34 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb ascvd: 60 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb ascvd: 2318 rows -> 117 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb ascvd: 2190 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:53 marvel ukb apoa: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb apoa: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:53 marvel ukb apoa: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:54 marvel ukb apob: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb apob: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb apob: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:54 marvel ukb hdl_c: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb hdl_c: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb hdl_c: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:54 marvel ukb ldl_c: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb ldl_c: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb ldl_c: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:54 marvel ukb tg: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb tg: 2417 rows -> 404 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:54 marvel ukb tg: 2002 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:55 marvel ukb all_cause_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb all_cause_dementia: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb all_cause_dementia: 155 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb all_cause_dementia: 5636 rows -> 25 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb all_cause_dementia: 5605 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:55 marvel ukb alzheimers_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb alzheimers_dementia: 487 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb alzheimers_dementia: 179 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb alzheimers_dementia: 5706 rows -> 18 variant rows, 12 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb alzheimers_dementia: 5676 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:55 marvel ukb vascular_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb vascular_dementia: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb vascular_dementia: 209 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb vascular_dementia: 5582 rows -> 6 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:55 marvel ukb vascular_dementia: 5576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:56 marvel ukb frontotemporal_dementia: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb frontotemporal_dementia: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb frontotemporal_dementia: 214 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb frontotemporal_dementia: 5577 rows -> 1 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb frontotemporal_dementia: 5576 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:56 marvel ukb ascvd: 252 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb ascvd: 482 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb ascvd: 150 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb ascvd: 5641 rows -> 30 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb ascvd: 5605 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:56 marvel ukb apoa: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb apoa: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:56 marvel ukb apoa: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:57 marvel ukb apob: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:57 marvel ukb apob: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:57 marvel ukb apob: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:57 marvel ukb hdl_c: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:57 marvel ukb hdl_c: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:57 marvel ukb hdl_c: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:57 marvel ukb ldl_c: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:57 marvel ukb ldl_c: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:57 marvel ukb ldl_c: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:58 marvel ukb tg: 1746 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb tg: 3315 rows -> 312 variant rows, 11 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb tg: 2992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:58 marvel ukb all_cause_dementia: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb all_cause_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb all_cause_dementia: 246 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb all_cause_dementia: 4334 rows -> 53 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb all_cause_dementia: 4272 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:58 marvel ukb alzheimers_dementia: 1782 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb alzheimers_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb alzheimers_dementia: 275 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb alzheimers_dementia: 4386 rows -> 37 variant rows, 18 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb alzheimers_dementia: 4331 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:58 marvel ukb vascular_dementia: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb vascular_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:58 marvel ukb vascular_dementia: 314 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb vascular_dementia: 4266 rows -> 22 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb vascular_dementia: 4238 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:59 marvel ukb frontotemporal_dementia: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb frontotemporal_dementia: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb frontotemporal_dementia: 327 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb frontotemporal_dementia: 4253 rows -> 13 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb frontotemporal_dementia: 4240 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:59 marvel ukb ascvd: 1764 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb ascvd: 181 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb ascvd: 162 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb ascvd: 4418 rows -> 99 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb ascvd: 4310 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:51:59 marvel ukb apoa: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb apoa: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:51:59 marvel ukb apoa: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:00 marvel ukb apob: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:00 marvel ukb apob: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:00 marvel ukb apob: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:00 marvel ukb hdl_c: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:00 marvel ukb hdl_c: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:00 marvel ukb hdl_c: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:00 marvel ukb ldl_c: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:00 marvel ukb ldl_c: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:00 marvel ukb ldl_c: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:01 marvel ukb tg: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb tg: 2948 rows -> 243 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb tg: 2695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:01 marvel ukb all_cause_dementia: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb all_cause_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb all_cause_dementia: 228 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb all_cause_dementia: 3259 rows -> 54 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb all_cause_dementia: 3196 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:01 marvel ukb alzheimers_dementia: 2970 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb alzheimers_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb alzheimers_dementia: 271 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb alzheimers_dementia: 3306 rows -> 44 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:01 marvel ukb alzheimers_dementia: 3262 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:02 marvel ukb vascular_dementia: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb vascular_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb vascular_dementia: 265 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb vascular_dementia: 3222 rows -> 40 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb vascular_dementia: 3176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:02 marvel ukb frontotemporal_dementia: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb frontotemporal_dementia: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb frontotemporal_dementia: 270 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb frontotemporal_dementia: 3217 rows -> 35 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb frontotemporal_dementia: 3176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:02 marvel ukb ascvd: 2961 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb ascvd: 77 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb ascvd: 112 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb ascvd: 3375 rows -> 112 variant rows, 10 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:02 marvel ukb ascvd: 3253 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:03 marvel ukb apoa: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb apoa: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb apoa: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:03 marvel ukb apob: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb apob: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb apob: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:03 marvel ukb hdl_c: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb hdl_c: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb hdl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:03 marvel ukb ldl_c: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb ldl_c: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:03 marvel ukb ldl_c: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:04 marvel ukb tg: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb tg: 3249 rows -> 354 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb tg: 2886 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:04 marvel ukb all_cause_dementia: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb all_cause_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb all_cause_dementia: 287 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb all_cause_dementia: 4726 rows -> 25 variant rows, 6 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb all_cause_dementia: 4695 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:04 marvel ukb alzheimers_dementia: 1278 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb alzheimers_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb alzheimers_dementia: 327 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb alzheimers_dementia: 4767 rows -> 15 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:04 marvel ukb alzheimers_dementia: 4752 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:05 marvel ukb vascular_dementia: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb vascular_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb vascular_dementia: 315 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb vascular_dementia: 4698 rows -> 10 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb vascular_dementia: 4688 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:05 marvel ukb frontotemporal_dementia: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb frontotemporal_dementia: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb frontotemporal_dementia: 326 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb frontotemporal_dementia: 4687 rows -> 7 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb frontotemporal_dementia: 4680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:05 marvel ukb ascvd: 1260 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb ascvd: 252 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb ascvd: 183 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb ascvd: 4830 rows -> 77 variant rows, 9 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-27 00:52:05 marvel ukb ascvd: 4744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:15 marvel ukb apoa: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:15 marvel ukb apoa: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:15 marvel ukb apoa: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:15 marvel ukb apob: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:15 marvel ukb apob: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:15 marvel ukb apob: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:16 marvel ukb hdl_c: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:16 marvel ukb hdl_c: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:16 marvel ukb hdl_c: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:16 marvel ukb ldl_c: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:16 marvel ukb ldl_c: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:16 marvel ukb ldl_c: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:17 marvel ukb tg: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb tg: 3855 rows -> 386 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb tg: 3460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:17 marvel ukb all_cause_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb all_cause_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb all_cause_dementia: 197 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb all_cause_dementia: 4057 rows -> 187 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb all_cause_dementia: 3861 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:17 marvel ukb alzheimers_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb alzheimers_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:17 marvel ukb alzheimers_dementia: 227 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb alzheimers_dementia: 4108 rows -> 162 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb alzheimers_dementia: 3928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:18 marvel ukb vascular_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb vascular_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb vascular_dementia: 237 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb vascular_dementia: 4017 rows -> 151 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb vascular_dementia: 3857 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:18 marvel ukb frontotemporal_dementia: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb frontotemporal_dementia: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:18 marvel ukb frontotemporal_dementia: 259 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb frontotemporal_dementia: 3995 rows -> 129 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb frontotemporal_dementia: 3857 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:19 marvel ukb ascvd: 7083 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb ascvd: 57 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb ascvd: 73 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb ascvd: 4181 rows -> 291 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb ascvd: 3881 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:19 marvel ukb apoa: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb apoa: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:19 marvel ukb apoa: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:20 marvel ukb apob: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:20 marvel ukb apob: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:20 marvel ukb apob: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:20 marvel ukb hdl_c: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:20 marvel ukb hdl_c: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:20 marvel ukb hdl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:21 marvel ukb ldl_c: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:21 marvel ukb ldl_c: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:21 marvel ukb ldl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:21 marvel ukb tg: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:21 marvel ukb tg: 1771 rows -> 892 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:21 marvel ukb tg: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:22 marvel ukb all_cause_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb all_cause_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb all_cause_dementia: 37 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb all_cause_dementia: 8965 rows -> 36 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb all_cause_dementia: 8920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:22 marvel ukb alzheimers_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb alzheimers_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb alzheimers_dementia: 47 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb alzheimers_dementia: 9036 rows -> 32 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:22 marvel ukb alzheimers_dementia: 8992 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:23 marvel ukb vascular_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb vascular_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb vascular_dementia: 59 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb vascular_dementia: 8943 rows -> 17 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb vascular_dementia: 8920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:23 marvel ukb frontotemporal_dementia: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb frontotemporal_dementia: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb frontotemporal_dementia: 78 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb frontotemporal_dementia: 8924 rows -> 4 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:23 marvel ukb frontotemporal_dementia: 8920 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:24 marvel ukb ascvd: 1359 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:24 marvel ukb ascvd: 1033 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:24 marvel ukb ascvd: 29 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:24 marvel ukb ascvd: 8973 rows -> 43 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:24 marvel ukb ascvd: 8924 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:24 marvel ukb apoa: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:24 marvel ukb apoa: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:24 marvel ukb apoa: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:25 marvel ukb apob: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:25 marvel ukb apob: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:25 marvel ukb apob: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:25 marvel ukb hdl_c: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:25 marvel ukb hdl_c: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:25 marvel ukb hdl_c: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:26 marvel ukb ldl_c: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:26 marvel ukb ldl_c: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:26 marvel ukb ldl_c: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:26 marvel ukb tg: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:26 marvel ukb tg: 2984 rows -> 652 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:26 marvel ukb tg: 2323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:27 marvel ukb all_cause_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb all_cause_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb all_cause_dementia: 175 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb all_cause_dementia: 6624 rows -> 78 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb all_cause_dementia: 6537 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:27 marvel ukb alzheimers_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb alzheimers_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb alzheimers_dementia: 184 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb alzheimers_dementia: 6696 rows -> 69 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:27 marvel ukb alzheimers_dementia: 6609 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:28 marvel ukb vascular_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb vascular_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb vascular_dementia: 208 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb vascular_dementia: 6591 rows -> 48 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb vascular_dementia: 6534 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:28 marvel ukb frontotemporal_dementia: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb frontotemporal_dementia: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb frontotemporal_dementia: 244 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb frontotemporal_dementia: 6555 rows -> 24 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:28 marvel ukb frontotemporal_dementia: 6531 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:29 marvel ukb ascvd: 4050 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:29 marvel ukb ascvd: 545 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:29 marvel ukb ascvd: 117 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:29 marvel ukb ascvd: 6682 rows -> 135 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:29 marvel ukb ascvd: 6538 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:29 marvel ukb apoa: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:29 marvel ukb apoa: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:29 marvel ukb apoa: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:30 marvel ukb apob: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:30 marvel ukb apob: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:30 marvel ukb apob: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:30 marvel ukb hdl_c: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:30 marvel ukb hdl_c: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:30 marvel ukb hdl_c: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:31 marvel ukb ldl_c: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:31 marvel ukb ldl_c: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:31 marvel ukb ldl_c: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:31 marvel ukb tg: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:31 marvel ukb tg: 3719 rows -> 517 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:31 marvel ukb tg: 3193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:31 marvel ukb all_cause_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:31 marvel ukb all_cause_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:31 marvel ukb all_cause_dementia: 230 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb all_cause_dementia: 5267 rows -> 138 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb all_cause_dementia: 5120 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:32 marvel ukb alzheimers_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb alzheimers_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb alzheimers_dementia: 277 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb alzheimers_dementia: 5301 rows -> 111 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb alzheimers_dementia: 5190 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:32 marvel ukb vascular_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb vascular_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb vascular_dementia: 268 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb vascular_dementia: 5229 rows -> 102 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:32 marvel ukb vascular_dementia: 5118 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:33 marvel ukb frontotemporal_dementia: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb frontotemporal_dementia: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb frontotemporal_dementia: 281 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb frontotemporal_dementia: 5216 rows -> 89 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb frontotemporal_dementia: 5118 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:33 marvel ukb ascvd: 5643 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb ascvd: 254 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb ascvd: 104 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb ascvd: 5393 rows -> 241 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:33 marvel ukb ascvd: 5143 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:34 marvel ukb apoa: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:34 marvel ukb apoa: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:34 marvel ukb apoa: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:34 marvel ukb apob: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:34 marvel ukb apob: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:34 marvel ukb apob: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:35 marvel ukb hdl_c: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:35 marvel ukb hdl_c: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:35 marvel ukb hdl_c: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:35 marvel ukb ldl_c: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:35 marvel ukb ldl_c: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:35 marvel ukb ldl_c: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:36 marvel ukb tg: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:36 marvel ukb tg: 2435 rows -> 724 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:36 marvel ukb tg: 1702 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:36 marvel ukb all_cause_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:36 marvel ukb all_cause_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:36 marvel ukb all_cause_dementia: 136 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:36 marvel ukb all_cause_dementia: 7248 rows -> 43 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:36 marvel ukb all_cause_dementia: 7196 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:37 marvel ukb alzheimers_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb alzheimers_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb alzheimers_dementia: 160 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb alzheimers_dementia: 7305 rows -> 28 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb alzheimers_dementia: 7265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:37 marvel ukb vascular_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb vascular_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb vascular_dementia: 160 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb vascular_dementia: 7224 rows -> 25 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:37 marvel ukb vascular_dementia: 7193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:38 marvel ukb frontotemporal_dementia: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb frontotemporal_dementia: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb frontotemporal_dementia: 181 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb frontotemporal_dementia: 7203 rows -> 9 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb frontotemporal_dementia: 7188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:38 marvel ukb ascvd: 3303 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb ascvd: 707 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb ascvd: 77 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb ascvd: 7307 rows -> 96 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:38 marvel ukb ascvd: 7202 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:39 marvel ukb apoa: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:39 marvel ukb apoa: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:39 marvel ukb apoa: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:39 marvel ukb apob: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:39 marvel ukb apob: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:39 marvel ukb apob: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:40 marvel ukb hdl_c: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:40 marvel ukb hdl_c: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:40 marvel ukb hdl_c: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:40 marvel ukb ldl_c: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:40 marvel ukb ldl_c: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:40 marvel ukb ldl_c: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:41 marvel ukb tg: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:41 marvel ukb tg: 4372 rows -> 578 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:41 marvel ukb tg: 3785 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:41 marvel ukb all_cause_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:41 marvel ukb all_cause_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:41 marvel ukb all_cause_dementia: 280 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:41 marvel ukb all_cause_dementia: 5905 rows -> 142 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:41 marvel ukb all_cause_dementia: 5754 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:42 marvel ukb alzheimers_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb alzheimers_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb alzheimers_dementia: 306 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb alzheimers_dementia: 5960 rows -> 121 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb alzheimers_dementia: 5821 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:42 marvel ukb vascular_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb vascular_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb vascular_dementia: 314 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb vascular_dementia: 5871 rows -> 112 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:42 marvel ukb vascular_dementia: 5750 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:43 marvel ukb frontotemporal_dementia: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb frontotemporal_dementia: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb frontotemporal_dementia: 333 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb frontotemporal_dementia: 5852 rows -> 93 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb frontotemporal_dementia: 5750 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:43 marvel ukb ascvd: 4950 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb ascvd: 259 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb ascvd: 154 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb ascvd: 6031 rows -> 252 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:43 marvel ukb ascvd: 5770 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:43 marvel ukb apoa: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:44 marvel ukb apoa: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:44 marvel ukb apoa: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:44 marvel ukb apob: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:44 marvel ukb apob: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:44 marvel ukb apob: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:44 marvel ukb hdl_c: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:44 marvel ukb hdl_c: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:44 marvel ukb hdl_c: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:45 marvel ukb ldl_c: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:45 marvel ukb ldl_c: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:45 marvel ukb ldl_c: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:45 marvel ukb tg: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:45 marvel ukb tg: 1686 rows -> 919 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:45 marvel ukb tg: 758 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:46 marvel ukb all_cause_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb all_cause_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb all_cause_dementia: 27 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb all_cause_dementia: 9177 rows -> 32 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb all_cause_dementia: 9136 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:46 marvel ukb alzheimers_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb alzheimers_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb alzheimers_dementia: 36 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb alzheimers_dementia: 9249 rows -> 29 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:46 marvel ukb alzheimers_dementia: 9208 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:47 marvel ukb vascular_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb vascular_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb vascular_dementia: 45 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb vascular_dementia: 9159 rows -> 17 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb vascular_dementia: 9136 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:47 marvel ukb frontotemporal_dementia: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb frontotemporal_dementia: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb frontotemporal_dementia: 64 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb frontotemporal_dementia: 9140 rows -> 4 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:47 marvel ukb frontotemporal_dementia: 9136 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:48 marvel ukb ascvd: 1116 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:48 marvel ukb ascvd: 1074 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:48 marvel ukb ascvd: 27 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:48 marvel ukb ascvd: 9177 rows -> 33 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:48 marvel ukb ascvd: 9138 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:48 marvel ukb apoa: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:48 marvel ukb apoa: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:48 marvel ukb apoa: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:49 marvel ukb apob: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:49 marvel ukb apob: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:49 marvel ukb apob: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:49 marvel ukb hdl_c: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:49 marvel ukb hdl_c: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:49 marvel ukb hdl_c: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:50 marvel ukb ldl_c: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:50 marvel ukb ldl_c: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:50 marvel ukb ldl_c: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:50 marvel ukb tg: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:50 marvel ukb tg: 2908 rows -> 728 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:50 marvel ukb tg: 2171 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:51 marvel ukb all_cause_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb all_cause_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb all_cause_dementia: 165 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb all_cause_dementia: 7286 rows -> 68 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb all_cause_dementia: 7209 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:51 marvel ukb alzheimers_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb alzheimers_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb alzheimers_dementia: 175 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb alzheimers_dementia: 7357 rows -> 58 variant rows, 18 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:51 marvel ukb alzheimers_dementia: 7281 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:52 marvel ukb vascular_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb vascular_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb vascular_dementia: 198 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb vascular_dementia: 7253 rows -> 38 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb vascular_dementia: 7206 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:52 marvel ukb frontotemporal_dementia: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb frontotemporal_dementia: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb frontotemporal_dementia: 229 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb frontotemporal_dementia: 7222 rows -> 19 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:52 marvel ukb frontotemporal_dementia: 7203 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:53 marvel ukb ascvd: 3294 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:53 marvel ukb ascvd: 649 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:53 marvel ukb ascvd: 120 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:53 marvel ukb ascvd: 7331 rows -> 112 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:53 marvel ukb ascvd: 7210 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:53 marvel ukb apoa: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:53 marvel ukb apoa: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:53 marvel ukb apoa: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:54 marvel ukb apob: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:54 marvel ukb apob: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:54 marvel ukb apob: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:54 marvel ukb hdl_c: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:54 marvel ukb hdl_c: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:54 marvel ukb hdl_c: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:55 marvel ukb ldl_c: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:55 marvel ukb ldl_c: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:55 marvel ukb ldl_c: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:55 marvel ukb tg: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:55 marvel ukb tg: 3795 rows -> 669 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:55 marvel ukb tg: 3117 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:56 marvel ukb all_cause_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb all_cause_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb all_cause_dementia: 254 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb all_cause_dementia: 6670 rows -> 101 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb all_cause_dementia: 6560 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:56 marvel ukb alzheimers_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb alzheimers_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb alzheimers_dementia: 298 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb alzheimers_dementia: 6707 rows -> 77 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:56 marvel ukb alzheimers_dementia: 6630 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:57 marvel ukb vascular_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb vascular_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb vascular_dementia: 283 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb vascular_dementia: 6641 rows -> 74 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb vascular_dementia: 6558 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:57 marvel ukb frontotemporal_dementia: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb frontotemporal_dementia: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb frontotemporal_dementia: 303 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb frontotemporal_dementia: 6621 rows -> 57 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:57 marvel ukb frontotemporal_dementia: 6558 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:58 marvel ukb ascvd: 4023 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:58 marvel ukb ascvd: 447 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:58 marvel ukb ascvd: 135 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:58 marvel ukb ascvd: 6789 rows -> 201 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:58 marvel ukb ascvd: 6579 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:58 marvel ukb apoa: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:58 marvel ukb apoa: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:58 marvel ukb apoa: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:59 marvel ukb apob: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:59 marvel ukb apob: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:59 marvel ukb apob: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:52:59 marvel ukb hdl_c: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:59 marvel ukb hdl_c: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:52:59 marvel ukb hdl_c: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:00 marvel ukb ldl_c: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:00 marvel ukb ldl_c: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:00 marvel ukb ldl_c: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:00 marvel ukb tg: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:00 marvel ukb tg: 2410 rows -> 784 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:00 marvel ukb tg: 1617 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:00 marvel ukb all_cause_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:00 marvel ukb all_cause_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:00 marvel ukb all_cause_dementia: 131 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb all_cause_dementia: 7809 rows -> 36 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb all_cause_dementia: 7764 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:01 marvel ukb alzheimers_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb alzheimers_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb alzheimers_dementia: 152 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb alzheimers_dementia: 7869 rows -> 24 variant rows, 12 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb alzheimers_dementia: 7833 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:01 marvel ukb vascular_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb vascular_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb vascular_dementia: 151 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb vascular_dementia: 7789 rows -> 22 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:01 marvel ukb vascular_dementia: 7761 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:02 marvel ukb frontotemporal_dementia: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb frontotemporal_dementia: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb frontotemporal_dementia: 161 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb frontotemporal_dementia: 7779 rows -> 9 variant rows, 6 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb frontotemporal_dementia: 7764 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:02 marvel ukb ascvd: 2664 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb ascvd: 790 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb ascvd: 82 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb ascvd: 7858 rows -> 81 variant rows, 9 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-27 00:53:02 marvel ukb ascvd: 7768 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:10 marvel ukb apoa: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:10 marvel ukb apoa: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:10 marvel ukb apoa: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:10 marvel ukb apob: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:10 marvel ukb apob: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:10 marvel ukb apob: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:11 marvel ukb hdl_c: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:11 marvel ukb hdl_c: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:11 marvel ukb hdl_c: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:11 marvel ukb ldl_c: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:11 marvel ukb ldl_c: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:11 marvel ukb ldl_c: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:11 marvel ukb tg: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb tg: 3143 rows -> 251 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb tg: 2882 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:12 marvel ukb all_cause_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb all_cause_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb all_cause_dementia: 160 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb all_cause_dementia: 3312 rows -> 113 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb all_cause_dementia: 3189 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:12 marvel ukb alzheimers_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb alzheimers_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb alzheimers_dementia: 212 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb alzheimers_dementia: 3350 rows -> 87 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:12 marvel ukb alzheimers_dementia: 3243 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:13 marvel ukb vascular_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb vascular_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb vascular_dementia: 238 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb vascular_dementia: 3234 rows -> 65 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb vascular_dementia: 3159 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:13 marvel ukb frontotemporal_dementia: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb frontotemporal_dementia: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb frontotemporal_dementia: 250 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb frontotemporal_dementia: 3222 rows -> 57 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:13 marvel ukb frontotemporal_dementia: 3158 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:14 marvel ukb ascvd: 5994 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb ascvd: 47 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb ascvd: 98 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb ascvd: 3374 rows -> 176 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb ascvd: 3188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:14 marvel ukb apoa: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb apoa: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb apoa: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:14 marvel ukb apob: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb apob: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:14 marvel ukb apob: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:15 marvel ukb hdl_c: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:15 marvel ukb hdl_c: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:15 marvel ukb hdl_c: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:15 marvel ukb ldl_c: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:15 marvel ukb ldl_c: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:15 marvel ukb ldl_c: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:16 marvel ukb tg: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb tg: 1330 rows -> 546 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb tg: 774 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:16 marvel ukb all_cause_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb all_cause_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb all_cause_dementia: 21 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb all_cause_dementia: 7532 rows -> 14 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb all_cause_dementia: 7508 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:16 marvel ukb alzheimers_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb alzheimers_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb alzheimers_dementia: 28 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb alzheimers_dementia: 7615 rows -> 10 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:16 marvel ukb alzheimers_dementia: 7585 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:17 marvel ukb vascular_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb vascular_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb vascular_dementia: 36 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb vascular_dementia: 7517 rows -> 7 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb vascular_dementia: 7504 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:17 marvel ukb frontotemporal_dementia: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb frontotemporal_dementia: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb frontotemporal_dementia: 47 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb frontotemporal_dementia: 7506 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb frontotemporal_dementia: 7503 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:17 marvel ukb ascvd: 1071 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb ascvd: 889 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:17 marvel ukb ascvd: 9 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:18 marvel ukb ascvd: 7544 rows -> 16 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:18 marvel ukb ascvd: 7518 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:18 marvel ukb apoa: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:18 marvel ukb apoa: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:18 marvel ukb apoa: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:18 marvel ukb apob: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:18 marvel ukb apob: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:18 marvel ukb apob: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:19 marvel ukb hdl_c: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:19 marvel ukb hdl_c: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:19 marvel ukb hdl_c: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:19 marvel ukb ldl_c: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:19 marvel ukb ldl_c: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:19 marvel ukb ldl_c: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:19 marvel ukb tg: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:19 marvel ukb tg: 2265 rows -> 390 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:19 marvel ukb tg: 1865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:20 marvel ukb all_cause_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb all_cause_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb all_cause_dementia: 131 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb all_cause_dementia: 5704 rows -> 41 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb all_cause_dementia: 5653 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:20 marvel ukb alzheimers_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb alzheimers_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb alzheimers_dementia: 153 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb alzheimers_dementia: 5772 rows -> 34 variant rows, 14 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:20 marvel ukb alzheimers_dementia: 5724 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:21 marvel ukb vascular_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb vascular_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb vascular_dementia: 161 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb vascular_dementia: 5674 rows -> 22 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb vascular_dementia: 5645 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:21 marvel ukb frontotemporal_dementia: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb frontotemporal_dementia: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb frontotemporal_dementia: 175 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb frontotemporal_dementia: 5660 rows -> 16 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb frontotemporal_dementia: 5644 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:21 marvel ukb ascvd: 3168 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb ascvd: 510 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:21 marvel ukb ascvd: 80 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:22 marvel ukb ascvd: 5755 rows -> 68 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:22 marvel ukb ascvd: 5677 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:22 marvel ukb apoa: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:22 marvel ukb apoa: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:22 marvel ukb apoa: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:22 marvel ukb apob: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:22 marvel ukb apob: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:22 marvel ukb apob: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:23 marvel ukb hdl_c: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:23 marvel ukb hdl_c: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:23 marvel ukb hdl_c: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:23 marvel ukb ldl_c: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:23 marvel ukb ldl_c: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:23 marvel ukb ldl_c: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:23 marvel ukb tg: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb tg: 2699 rows -> 305 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb tg: 2384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:24 marvel ukb all_cause_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb all_cause_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb all_cause_dementia: 181 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb all_cause_dementia: 3960 rows -> 52 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb all_cause_dementia: 3898 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:24 marvel ukb alzheimers_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb alzheimers_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb alzheimers_dementia: 223 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb alzheimers_dementia: 4008 rows -> 30 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:24 marvel ukb alzheimers_dementia: 3960 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:25 marvel ukb vascular_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb vascular_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb vascular_dementia: 230 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb vascular_dementia: 3911 rows -> 26 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb vascular_dementia: 3875 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:25 marvel ukb frontotemporal_dementia: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb frontotemporal_dementia: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb frontotemporal_dementia: 233 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb frontotemporal_dementia: 3908 rows -> 22 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:25 marvel ukb frontotemporal_dementia: 3880 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:26 marvel ukb ascvd: 5166 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb ascvd: 206 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb ascvd: 88 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb ascvd: 4053 rows -> 129 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb ascvd: 3914 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:26 marvel ukb apoa: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb apoa: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb apoa: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:26 marvel ukb apob: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb apob: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:26 marvel ukb apob: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:27 marvel ukb hdl_c: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:27 marvel ukb hdl_c: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:27 marvel ukb hdl_c: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:27 marvel ukb ldl_c: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:27 marvel ukb ldl_c: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:27 marvel ukb ldl_c: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:28 marvel ukb tg: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb tg: 1764 rows -> 426 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb tg: 1328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:28 marvel ukb all_cause_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb all_cause_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb all_cause_dementia: 99 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb all_cause_dementia: 6201 rows -> 13 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb all_cause_dementia: 6181 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:28 marvel ukb alzheimers_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb alzheimers_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb alzheimers_dementia: 105 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb alzheimers_dementia: 6285 rows -> 10 variant rows, 14 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:28 marvel ukb alzheimers_dementia: 6261 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:29 marvel ukb vascular_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb vascular_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb vascular_dementia: 116 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb vascular_dementia: 6184 rows -> 7 variant rows, 1 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb vascular_dementia: 6176 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:29 marvel ukb frontotemporal_dementia: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb frontotemporal_dementia: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb frontotemporal_dementia: 122 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb frontotemporal_dementia: 6178 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:29 marvel ukb frontotemporal_dementia: 6175 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:30 marvel ukb ascvd: 2565 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb ascvd: 648 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb ascvd: 40 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb ascvd: 6260 rows -> 41 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb ascvd: 6209 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:30 marvel ukb apoa: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb apoa: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb apoa: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:30 marvel ukb apob: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb apob: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:30 marvel ukb apob: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:31 marvel ukb hdl_c: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:31 marvel ukb hdl_c: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:31 marvel ukb hdl_c: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:31 marvel ukb ldl_c: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:31 marvel ukb ldl_c: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:31 marvel ukb ldl_c: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:31 marvel ukb tg: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:31 marvel ukb tg: 3209 rows -> 367 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:31 marvel ukb tg: 2832 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:32 marvel ukb all_cause_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb all_cause_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb all_cause_dementia: 198 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb all_cause_dementia: 4936 rows -> 79 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb all_cause_dementia: 4847 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:32 marvel ukb alzheimers_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb alzheimers_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb alzheimers_dementia: 242 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb alzheimers_dementia: 4982 rows -> 58 variant rows, 20 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:32 marvel ukb alzheimers_dementia: 4904 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:33 marvel ukb vascular_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb vascular_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb vascular_dementia: 261 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb vascular_dementia: 4873 rows -> 43 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb vascular_dementia: 4820 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:33 marvel ukb frontotemporal_dementia: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb frontotemporal_dementia: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb frontotemporal_dementia: 271 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb frontotemporal_dementia: 4863 rows -> 37 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb frontotemporal_dementia: 4820 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:33 marvel ukb ascvd: 4104 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb ascvd: 275 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:33 marvel ukb ascvd: 138 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:34 marvel ukb ascvd: 4996 rows -> 136 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:34 marvel ukb ascvd: 4850 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:34 marvel ukb apoa: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:34 marvel ukb apoa: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:34 marvel ukb apoa: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:34 marvel ukb apob: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:34 marvel ukb apob: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:34 marvel ukb apob: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:35 marvel ukb hdl_c: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:35 marvel ukb hdl_c: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:35 marvel ukb hdl_c: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:35 marvel ukb ldl_c: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:35 marvel ukb ldl_c: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:35 marvel ukb ldl_c: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:35 marvel ukb tg: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:35 marvel ukb tg: 1256 rows -> 564 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:35 marvel ukb tg: 683 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:36 marvel ukb all_cause_dementia: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb all_cause_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb all_cause_dementia: 20 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb all_cause_dementia: 7760 rows -> 7 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb all_cause_dementia: 7744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:36 marvel ukb alzheimers_dementia: 810 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb alzheimers_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb alzheimers_dementia: 22 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb alzheimers_dementia: 7839 rows -> 5 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:36 marvel ukb alzheimers_dementia: 7816 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:37 marvel ukb vascular_dementia: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb vascular_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb vascular_dementia: 25 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb vascular_dementia: 7755 rows -> 5 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb vascular_dementia: 7744 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:37 marvel ukb frontotemporal_dementia: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb frontotemporal_dementia: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb frontotemporal_dementia: 34 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb frontotemporal_dementia: 7746 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb frontotemporal_dementia: 7743 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:37 marvel ukb ascvd: 801 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb ascvd: 932 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:37 marvel ukb ascvd: 5 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:38 marvel ukb ascvd: 7775 rows -> 9 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:38 marvel ukb ascvd: 7757 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:38 marvel ukb apoa: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:38 marvel ukb apoa: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:38 marvel ukb apoa: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:38 marvel ukb apob: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:38 marvel ukb apob: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:38 marvel ukb apob: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:39 marvel ukb hdl_c: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:39 marvel ukb hdl_c: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:39 marvel ukb hdl_c: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:39 marvel ukb ldl_c: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:39 marvel ukb ldl_c: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:39 marvel ukb ldl_c: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:39 marvel ukb tg: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb tg: 2061 rows -> 440 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb tg: 1611 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:40 marvel ukb all_cause_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb all_cause_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb all_cause_dementia: 112 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb all_cause_dementia: 6233 rows -> 31 variant rows, 9 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb all_cause_dementia: 6193 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:40 marvel ukb alzheimers_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb alzheimers_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb alzheimers_dementia: 127 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb alzheimers_dementia: 6308 rows -> 28 variant rows, 12 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:40 marvel ukb alzheimers_dementia: 6268 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:41 marvel ukb vascular_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb vascular_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb vascular_dementia: 134 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb vascular_dementia: 6211 rows -> 17 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb vascular_dementia: 6188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:41 marvel ukb frontotemporal_dementia: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb frontotemporal_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb frontotemporal_dementia: 146 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb frontotemporal_dementia: 6199 rows -> 11 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:41 marvel ukb frontotemporal_dementia: 6188 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:42 marvel ukb ascvd: 2556 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb ascvd: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb ascvd: 83 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb ascvd: 6262 rows -> 45 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb ascvd: 6207 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:42 marvel ukb apoa: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb apoa: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb apoa: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:42 marvel ukb apob: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb apob: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:42 marvel ukb apob: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:43 marvel ukb hdl_c: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:43 marvel ukb hdl_c: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:43 marvel ukb hdl_c: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:43 marvel ukb ldl_c: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:43 marvel ukb ldl_c: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:43 marvel ukb ldl_c: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:44 marvel ukb tg: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb tg: 2505 rows -> 395 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb tg: 2100 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:44 marvel ukb all_cause_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb all_cause_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb all_cause_dementia: 172 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb all_cause_dementia: 5315 rows -> 32 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb all_cause_dementia: 5273 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:44 marvel ukb alzheimers_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb alzheimers_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb alzheimers_dementia: 200 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb alzheimers_dementia: 5377 rows -> 18 variant rows, 18 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:44 marvel ukb alzheimers_dementia: 5341 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:45 marvel ukb vascular_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb vascular_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb vascular_dementia: 212 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb vascular_dementia: 5275 rows -> 12 variant rows, 7 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb vascular_dementia: 5256 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:45 marvel ukb frontotemporal_dementia: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb frontotemporal_dementia: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb frontotemporal_dementia: 209 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb frontotemporal_dementia: 5278 rows -> 11 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:45 marvel ukb frontotemporal_dementia: 5261 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:46 marvel ukb ascvd: 3600 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb ascvd: 426 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb ascvd: 90 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb ascvd: 5397 rows -> 96 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb ascvd: 5291 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:46 marvel ukb apoa: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb apoa: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb apoa: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:46 marvel ukb apob: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb apob: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:46 marvel ukb apob: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:47 marvel ukb hdl_c: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:47 marvel ukb hdl_c: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:47 marvel ukb hdl_c: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:47 marvel ukb ldl_c: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:47 marvel ukb ldl_c: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:47 marvel ukb ldl_c: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:48 marvel ukb tg: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb tg: 1498 rows -> 469 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb tg: 1019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:48 marvel ukb all_cause_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb all_cause_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb all_cause_dementia: 69 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb all_cause_dementia: 6686 rows -> 8 variant rows, 6 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb all_cause_dementia: 6672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:48 marvel ukb alzheimers_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb alzheimers_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb alzheimers_dementia: 76 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb alzheimers_dementia: 6769 rows -> 5 variant rows, 12 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:48 marvel ukb alzheimers_dementia: 6752 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:49 marvel ukb vascular_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb vascular_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb vascular_dementia: 78 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb vascular_dementia: 6677 rows -> 5 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb vascular_dementia: 6672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:49 marvel ukb frontotemporal_dementia: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb frontotemporal_dementia: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb frontotemporal_dementia: 81 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb frontotemporal_dementia: 6674 rows -> 3 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:49 marvel ukb frontotemporal_dementia: 6671 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:50 marvel ukb ascvd: 2007 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:50 marvel ukb ascvd: 751 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:50 marvel ukb ascvd: 25 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:50 marvel ukb ascvd: 6730 rows -> 29 variant rows, 10 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-27 00:53:50 marvel ukb ascvd: 6691 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:52 marvel ukb apoa: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:52 marvel ukb apoa: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:52 marvel ukb apoa: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:52 marvel ukb apob: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:52 marvel ukb apob: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:52 marvel ukb apob: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:52 marvel ukb hdl_c: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:52 marvel ukb hdl_c: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:52 marvel ukb hdl_c: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:53 marvel ukb ldl_c: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb ldl_c: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb ldl_c: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:53 marvel ukb tg: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb tg: 860 rows -> 92 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb tg: 759 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:53 marvel ukb all_cause_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb all_cause_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb all_cause_dementia: 35 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb all_cause_dementia: 923 rows -> 48 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb all_cause_dementia: 866 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:53 marvel ukb alzheimers_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb alzheimers_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb alzheimers_dementia: 41 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb alzheimers_dementia: 998 rows -> 42 variant rows, 18 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb alzheimers_dementia: 938 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:53 marvel ukb vascular_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb vascular_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb vascular_dementia: 47 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb vascular_dementia: 911 rows -> 36 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb vascular_dementia: 866 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:53 marvel ukb frontotemporal_dementia: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb frontotemporal_dementia: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb frontotemporal_dementia: 62 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb frontotemporal_dementia: 896 rows -> 31 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:53 marvel ukb frontotemporal_dementia: 865 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb ascvd: 2196 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb ascvd: 14 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb ascvd: 17 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb ascvd: 941 rows -> 66 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb ascvd: 866 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb apoa: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb apoa: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb apoa: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb apob: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb apob: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb apob: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb hdl_c: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb hdl_c: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb hdl_c: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb ldl_c: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb ldl_c: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb ldl_c: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb tg: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb tg: 547 rows -> 276 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb tg: 265 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:54 marvel ukb all_cause_dementia: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb all_cause_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb all_cause_dementia: 15 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb all_cause_dementia: 2597 rows -> 7 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:54 marvel ukb all_cause_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:55 marvel ukb alzheimers_dementia: 288 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb alzheimers_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb alzheimers_dementia: 16 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb alzheimers_dementia: 2650 rows -> 6 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb alzheimers_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:55 marvel ukb vascular_dementia: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb vascular_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb vascular_dementia: 22 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb vascular_dementia: 2590 rows -> 3 variant rows, 3 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb vascular_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:55 marvel ukb frontotemporal_dementia: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb frontotemporal_dementia: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb frontotemporal_dementia: 26 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb frontotemporal_dementia: 2586 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb frontotemporal_dementia: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:55 marvel ukb ascvd: 261 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb ascvd: 295 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb ascvd: 15 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb ascvd: 2597 rows -> 7 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb ascvd: 2584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:55 marvel ukb apoa: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb apoa: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb apoa: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:55 marvel ukb apob: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb apob: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:55 marvel ukb apob: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:56 marvel ukb hdl_c: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb hdl_c: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb hdl_c: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:56 marvel ukb ldl_c: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb ldl_c: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb ldl_c: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:56 marvel ukb tg: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb tg: 886 rows -> 191 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb tg: 686 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:56 marvel ukb all_cause_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb all_cause_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb all_cause_dementia: 52 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb all_cause_dementia: 1870 rows -> 18 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb all_cause_dementia: 1846 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:56 marvel ukb alzheimers_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb alzheimers_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb alzheimers_dementia: 57 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb alzheimers_dementia: 1946 rows -> 16 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb alzheimers_dementia: 1918 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:56 marvel ukb vascular_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb vascular_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb vascular_dementia: 56 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb vascular_dementia: 1866 rows -> 14 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:56 marvel ukb vascular_dementia: 1846 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb frontotemporal_dementia: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb frontotemporal_dementia: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb frontotemporal_dementia: 73 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb frontotemporal_dementia: 1849 rows -> 9 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb frontotemporal_dementia: 1840 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb ascvd: 1098 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb ascvd: 148 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb ascvd: 35 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb ascvd: 1887 rows -> 30 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb ascvd: 1848 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb apoa: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb apoa: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb apoa: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb apob: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb apob: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb apob: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb hdl_c: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb hdl_c: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb hdl_c: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb ldl_c: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb ldl_c: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:57 marvel ukb ldl_c: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:57 marvel ukb tg: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb tg: 938 rows -> 132 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb tg: 797 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:58 marvel ukb all_cause_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb all_cause_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb all_cause_dementia: 62 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb all_cause_dementia: 1268 rows -> 27 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb all_cause_dementia: 1232 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:58 marvel ukb alzheimers_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb alzheimers_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb alzheimers_dementia: 73 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb alzheimers_dementia: 1338 rows -> 22 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb alzheimers_dementia: 1304 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:58 marvel ukb vascular_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb vascular_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb vascular_dementia: 72 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb vascular_dementia: 1258 rows -> 20 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb vascular_dementia: 1232 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:58 marvel ukb frontotemporal_dementia: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb frontotemporal_dementia: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb frontotemporal_dementia: 82 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb frontotemporal_dementia: 1248 rows -> 16 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb frontotemporal_dementia: 1232 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:58 marvel ukb ascvd: 1782 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb ascvd: 56 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb ascvd: 37 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb ascvd: 1293 rows -> 50 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb ascvd: 1234 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:58 marvel ukb apoa: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb apoa: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:58 marvel ukb apoa: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb apob: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb apob: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb apob: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb hdl_c: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb hdl_c: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb hdl_c: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb ldl_c: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb ldl_c: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb ldl_c: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb tg: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb tg: 749 rows -> 228 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb tg: 512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb all_cause_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb all_cause_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb all_cause_dementia: 45 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb all_cause_dementia: 2230 rows -> 8 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb all_cause_dementia: 2216 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb alzheimers_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb alzheimers_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb alzheimers_dementia: 64 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb alzheimers_dementia: 2292 rows -> 4 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb alzheimers_dementia: 2288 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:53:59 marvel ukb vascular_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb vascular_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:53:59 marvel ukb vascular_dementia: 57 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb vascular_dementia: 2218 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb vascular_dementia: 2216 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:00 marvel ukb frontotemporal_dementia: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb frontotemporal_dementia: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb frontotemporal_dementia: 56 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb frontotemporal_dementia: 2219 rows -> 3 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb frontotemporal_dementia: 2216 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:00 marvel ukb ascvd: 675 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb ascvd: 218 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb ascvd: 26 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb ascvd: 2249 rows -> 18 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb ascvd: 2222 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:00 marvel ukb apoa: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb apoa: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb apoa: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:00 marvel ukb apob: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb apob: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb apob: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:00 marvel ukb hdl_c: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb hdl_c: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb hdl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:00 marvel ukb ldl_c: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb ldl_c: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:00 marvel ukb ldl_c: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb tg: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb tg: 1021 rows -> 142 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb tg: 870 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb all_cause_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb all_cause_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb all_cause_dementia: 58 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb all_cause_dementia: 1369 rows -> 35 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb all_cause_dementia: 1325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb alzheimers_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb alzheimers_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb alzheimers_dementia: 63 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb alzheimers_dementia: 1445 rows -> 30 variant rows, 18 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb alzheimers_dementia: 1397 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb vascular_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb vascular_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb vascular_dementia: 67 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb vascular_dementia: 1360 rows -> 26 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb vascular_dementia: 1325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb frontotemporal_dementia: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb frontotemporal_dementia: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb frontotemporal_dementia: 86 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb frontotemporal_dementia: 1341 rows -> 20 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb frontotemporal_dementia: 1321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb ascvd: 1683 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb ascvd: 58 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb ascvd: 41 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb ascvd: 1386 rows -> 52 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:01 marvel ukb ascvd: 1325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:01 marvel ukb apoa: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb apoa: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb apoa: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:02 marvel ukb apob: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb apob: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb apob: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:02 marvel ukb hdl_c: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb hdl_c: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb hdl_c: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:02 marvel ukb ldl_c: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb ldl_c: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb ldl_c: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:02 marvel ukb tg: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb tg: 529 rows -> 282 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb tg: 241 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:02 marvel ukb all_cause_dementia: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb all_cause_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb all_cause_dementia: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb all_cause_dementia: 2643 rows -> 5 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb all_cause_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:02 marvel ukb alzheimers_dementia: 234 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb alzheimers_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb alzheimers_dementia: 2697 rows -> 5 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:02 marvel ukb alzheimers_dementia: 2680 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:03 marvel ukb vascular_dementia: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb vascular_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb vascular_dementia: 20 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb vascular_dementia: 2637 rows -> 2 variant rows, 3 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb vascular_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:03 marvel ukb frontotemporal_dementia: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb frontotemporal_dementia: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb frontotemporal_dementia: 23 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb frontotemporal_dementia: 2634 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb frontotemporal_dementia: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:03 marvel ukb ascvd: 207 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb ascvd: 304 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb ascvd: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb ascvd: 2643 rows -> 5 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb ascvd: 2632 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:03 marvel ukb apoa: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb apoa: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb apoa: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:03 marvel ukb apob: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb apob: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb apob: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:03 marvel ukb hdl_c: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb hdl_c: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:03 marvel ukb hdl_c: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb ldl_c: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb ldl_c: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb ldl_c: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb tg: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb tg: 967 rows -> 220 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb tg: 738 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb all_cause_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb all_cause_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb all_cause_dementia: 59 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb all_cause_dementia: 2133 rows -> 17 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb all_cause_dementia: 2110 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb alzheimers_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb alzheimers_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb alzheimers_dementia: 64 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb alzheimers_dementia: 2209 rows -> 15 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb alzheimers_dementia: 2182 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb vascular_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb vascular_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb vascular_dementia: 63 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb vascular_dementia: 2129 rows -> 13 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb vascular_dementia: 2110 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb frontotemporal_dementia: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb frontotemporal_dementia: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb frontotemporal_dementia: 80 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb frontotemporal_dementia: 2112 rows -> 8 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb frontotemporal_dementia: 2104 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:04 marvel ukb ascvd: 801 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb ascvd: 175 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb ascvd: 46 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb ascvd: 2146 rows -> 25 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:04 marvel ukb ascvd: 2112 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:05 marvel ukb apoa: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb apoa: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb apoa: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:05 marvel ukb apob: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb apob: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb apob: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:05 marvel ukb hdl_c: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb hdl_c: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb hdl_c: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:05 marvel ukb ldl_c: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb ldl_c: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb ldl_c: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:05 marvel ukb tg: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb tg: 958 rows -> 172 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb tg: 777 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:05 marvel ukb all_cause_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb all_cause_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb all_cause_dementia: 72 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb all_cause_dementia: 1607 rows -> 14 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:05 marvel ukb all_cause_dementia: 1584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb alzheimers_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb alzheimers_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb alzheimers_dementia: 81 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb alzheimers_dementia: 1679 rows -> 11 variant rows, 12 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb alzheimers_dementia: 1656 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb vascular_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb vascular_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb vascular_dementia: 80 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb vascular_dementia: 1599 rows -> 9 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb vascular_dementia: 1584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb frontotemporal_dementia: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb frontotemporal_dementia: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb frontotemporal_dementia: 88 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb frontotemporal_dementia: 1591 rows -> 7 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb frontotemporal_dementia: 1584 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb ascvd: 1386 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb ascvd: 103 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb ascvd: 47 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb ascvd: 1632 rows -> 34 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb ascvd: 1589 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb apoa: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb apoa: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb apoa: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb apob: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb apob: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:06 marvel ukb apob: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:06 marvel ukb hdl_c: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb hdl_c: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb hdl_c: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:07 marvel ukb ldl_c: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb ldl_c: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb ldl_c: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:07 marvel ukb tg: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb tg: 683 rows -> 242 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb tg: 432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:07 marvel ukb all_cause_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb all_cause_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb all_cause_dementia: 36 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb all_cause_dementia: 2341 rows -> 7 variant rows, 6 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb all_cause_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:07 marvel ukb alzheimers_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb alzheimers_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:07 marvel ukb alzheimers_dementia: 55 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb alzheimers_dementia: 2403 rows -> 3 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb alzheimers_dementia: 2400 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:08 marvel ukb vascular_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb vascular_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb vascular_dementia: 47 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb vascular_dementia: 2330 rows -> 2 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb vascular_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:08 marvel ukb frontotemporal_dementia: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb frontotemporal_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb frontotemporal_dementia: 46 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb frontotemporal_dementia: 2331 rows -> 3 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb frontotemporal_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-27 00:54:08 marvel ukb ascvd: 549 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb ascvd: 242 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb ascvd: 19 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb ascvd: 2358 rows -> 15 variant rows, 9 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-27 00:54:08 marvel ukb ascvd: 2334 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-10-27 00:54:09 fetch_curated
[info]  2026-10-27 00:55:36 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1
[info]  2026-10-27 00:55:38 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-27 00:55:45 MONDO_0013792 (exact): 42 fetched; in region: none
[info]  2026-10-27 00:55:54 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-27 00:56:27 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-27 00:56:53 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6
[info]  2026-10-27 00:56:55 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-27 00:56:59 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-27 01:01:43 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3
[info]  2026-10-27 01:01:50 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-27 01:01:51 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-27 01:01:51 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-27 01:10:27 MONDO_0004975 (with child traits): 7102 fetched; in region: APOB=1
[info]  2026-10-27 01:10:35 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-27 01:10:39 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-27 01:10:43 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-27 01:10:44 EFO ids with 0 curated associations: 4
[stage] 2026-10-27 01:10:44 gene_burden
[info]  2026-10-27 01:10:44 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-27 01:10:45 curated MAF: numeric=58 not_reported=28
[info]  2026-10-27 01:10:45 curated: 54 rows dropped from studies excluded for cohort overlap
[info]  2026-10-27 01:10:45 gene-burden rows: none (8 genes with 0)
[info]  2026-10-27 01:10:50 ancestry: 0 rows of studies not in the discovery log labelled NR
[info]  2026-10-27 01:10:50 ancestry: curated EAS=21
[info]  2026-10-27 01:10:50 ancestry: curated EUR=26
[info]  2026-10-27 01:10:50 ancestry: curated MULTI=21
[info]  2026-10-27 01:10:50 ancestry: curated NR=18
[info]  2026-10-27 01:10:50 ancestry: gene-burden EUR=2661
[info]  2026-10-27 01:10:50 ancestry: gene-burden MULTI=2718
[info]  2026-10-27 01:10:50 ancestry: summary-stats AFR=159854
[info]  2026-10-27 01:10:50 ancestry: summary-stats AMR=73617
[info]  2026-10-27 01:10:50 ancestry: summary-stats CSA=43677
[info]  2026-10-27 01:10:50 ancestry: summary-stats EAS=45135
[info]  2026-10-27 01:10:50 ancestry: summary-stats EUR=200936
[info]  2026-10-27 01:10:50 ancestry: summary-stats MULTI=184989
[info]  2026-10-27 01:10:50 ancestry: summary-stats NR=5898
[stage] 2026-10-27 01:10:50 effect_scale
[info]  2026-10-27 01:10:59 wrote 215 studies to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-27 01:10:59 study effect scale: linear=52, log_or=111, unknown=52
[stage] 2026-10-27 01:10:59 normalise
[info]  2026-10-27 01:11:01 normalisation: summary-stats rows unchanged=670842 no_sequence=40564 ref_mismatch=2699 normalised=1
[info]  2026-10-27 01:11:01 normalisation: curated rows effect_only=86
[stage] 2026-10-27 01:11:01 ensembl_check
[info]  2026-10-27 01:11:01 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:02 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:02 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:02 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:02 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:02 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:03 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:03 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-27 01:11:05 Ensembl check: 23697 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-27 01:11:06 summary-stats rows: alleles match=528379 flipped=135502 not_found=31932 mismatch=17825 strand_flip=468; rsid same=521285 no_source_rsid=116542 rsid_only=41315 different=3032
[info]  2026-10-27 01:11:06 curated rows: alleles match=33 flipped=28 effect_unknown=25; rsid same=86
[info]  2026-10-27 01:11:08 duplicate variants flagged: 766 rows
[stage] 2026-10-27 01:11:08 write
[info]  2026-10-27 01:12:09 wrote 719571 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-27 01:12:18
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 00:50:25 using root directory: /home/mvanvugt/projects/lipid_adem

```

## [40] clinvar_filter (`mamba run --no-capture-output -n clinvar-build clinvar-filter /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_vcv.db --rcv-db /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_rcv.db -g gene CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA APOA1 APOB APOE -o /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv -vvv`)
- first run: 2026-10-06 17:09:48
- last run: 2026-10-06 17:09:48
- commit: `7e96ca6` (dirty)

Output:
```text
2026-10-06 17:09:48,842 - INFO - Wrote 313818 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
```

## [40] match_variants (`src/match_variants.py`)
- first run: 2026-10-01 09:59:12
- last run: 2026-10-27 09:08:59
- commit: `244d529` (dirty)

Output:
```text
[stage] 2026-10-27 09:08:29 load_variant_lists
[info]  2026-10-27 09:08:29 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv: 9224 rows
[info]  2026-10-27 09:08:29 0 duplicate rows removed
[warn]  2026-10-27 09:08:29 /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/gene_regions.tsv not found: rows outside the gene region are not counted
[info]  2026-10-27 09:08:29 ANGPTL3 AM: 493 rows, 0 without alleles, 493 outside gene region
[info]  2026-10-27 09:08:29 ANGPTL3 ClinVar: 12 rows, 0 without alleles, 12 outside gene region
[info]  2026-10-27 09:08:29 ANGPTL3 PTV: 56 rows, 0 without alleles, 56 outside gene region
[info]  2026-10-27 09:08:29 APOA1 ClinVar: 33 rows, 0 without alleles, 33 outside gene region
[info]  2026-10-27 09:08:29 APOA1 PTV: 15 rows, 0 without alleles, 15 outside gene region
[info]  2026-10-27 09:08:29 APOB ClinVar: 236 rows, 0 without alleles, 236 outside gene region
[info]  2026-10-27 09:08:29 APOB PTV: 172 rows, 0 without alleles, 172 outside gene region
[info]  2026-10-27 09:08:29 APOE ClinVar: 20 rows, 0 without alleles, 20 outside gene region
[info]  2026-10-27 09:08:29 CETP AM: 439 rows, 0 without alleles, 439 outside gene region
[info]  2026-10-27 09:08:29 CETP ClinVar: 10 rows, 0 without alleles, 10 outside gene region
[info]  2026-10-27 09:08:29 CETP GoF: 1 rows, 0 without alleles, 1 outside gene region
[info]  2026-10-27 09:08:29 CETP PTV: 58 rows, 0 without alleles, 58 outside gene region
[info]  2026-10-27 09:08:29 HMGCR AM: 2623 rows, 0 without alleles, 2623 outside gene region
[info]  2026-10-27 09:08:29 HMGCR ClinVar: 7 rows, 0 without alleles, 7 outside gene region
[info]  2026-10-27 09:08:29 HMGCR PTV: 39 rows, 0 without alleles, 39 outside gene region
[info]  2026-10-27 09:08:29 NPC1L1 AM: 2507 rows, 0 without alleles, 2507 outside gene region
[info]  2026-10-27 09:08:29 NPC1L1 PTV: 96 rows, 0 without alleles, 96 outside gene region
[info]  2026-10-27 09:08:29 PCSK9 AM: 737 rows, 0 without alleles, 737 outside gene region
[info]  2026-10-27 09:08:29 PCSK9 ClinVar: 18 rows, 0 without alleles, 18 outside gene region
[info]  2026-10-27 09:08:29 PCSK9 GoF: 18 rows, 0 without alleles, 18 outside gene region
[info]  2026-10-27 09:08:29 PCSK9 PTV: 68 rows, 0 without alleles, 68 outside gene region
[info]  2026-10-27 09:08:29 PPARA AM: 1543 rows, 0 without alleles, 1543 outside gene region
[info]  2026-10-27 09:08:29 PPARA PTV: 23 rows, 0 without alleles, 23 outside gene region
[info]  2026-10-27 09:08:29 normalisation: variant-list rows no_sequence=9224
[stage] 2026-10-27 09:08:29 load_gwas
[info]  2026-10-27 09:08:52 /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/merged_associations.tsv.gz: 719571 rows, 714192 variant-level (summary-stats, curated)
[info]  2026-10-27 09:08:53 wrote 5379 marvel gene-burden rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_burden.tsv.gz
[info]  2026-10-27 09:08:56 curated: 25 rows without chrom/pos or effect allele, cannot be matched
[stage] 2026-10-27 09:08:56 match
[info]  2026-10-27 09:08:57 ANGPTL3 AM: 493 variants, 37 matched, GWAS rows: summary-stats=1531
[info]  2026-10-27 09:08:57 ANGPTL3 ClinVar: 12 variants, 6 matched, GWAS rows: summary-stats=383
[info]  2026-10-27 09:08:57 ANGPTL3 PTV: 56 variants, 54 matched, GWAS rows: summary-stats=2229
[info]  2026-10-27 09:08:57 APOA1 ClinVar: 33 variants, 0 matched, GWAS rows: none
[info]  2026-10-27 09:08:57 APOA1 PTV: 15 variants, 0 matched, GWAS rows: none
[info]  2026-10-27 09:08:57 APOB ClinVar: 236 variants, 3 matched, GWAS rows: summary-stats=137
[info]  2026-10-27 09:08:57 APOB PTV: 172 variants, 0 matched, GWAS rows: none
[info]  2026-10-27 09:08:57 APOE ClinVar: 20 variants, 1 matched, GWAS rows: summary-stats=16
[info]  2026-10-27 09:08:57 CETP AM: 439 variants, 34 matched, GWAS rows: summary-stats=1290
[info]  2026-10-27 09:08:57 CETP ClinVar: 10 variants, 6 matched, GWAS rows: summary-stats=275
[info]  2026-10-27 09:08:57 CETP GoF: 1 variants, 1 matched, GWAS rows: summary-stats=305
[info]  2026-10-27 09:08:57 CETP PTV: 58 variants, 58 matched, GWAS rows: summary-stats=2553
[info]  2026-10-27 09:08:57 HMGCR AM: 2623 variants, 131 matched, GWAS rows: summary-stats=4749
[info]  2026-10-27 09:08:57 HMGCR ClinVar: 7 variants, 4 matched, GWAS rows: summary-stats=127
[info]  2026-10-27 09:08:57 HMGCR PTV: 39 variants, 39 matched, GWAS rows: summary-stats=1409
[info]  2026-10-27 09:08:57 NPC1L1 AM: 2507 variants, 178 matched, GWAS rows: summary-stats=6670
[info]  2026-10-27 09:08:57 NPC1L1 PTV: 96 variants, 93 matched, GWAS rows: summary-stats=3453
[info]  2026-10-27 09:08:57 PCSK9 AM: 737 variants, 49 matched, GWAS rows: summary-stats=1770
[info]  2026-10-27 09:08:57 PCSK9 ClinVar: 18 variants, 4 matched, GWAS rows: summary-stats=219
[info]  2026-10-27 09:08:57 PCSK9 GoF: 18 variants, 12 matched, GWAS rows: summary-stats=955
[info]  2026-10-27 09:08:57 PCSK9 PTV: 68 variants, 68 matched, GWAS rows: summary-stats=2574
[info]  2026-10-27 09:08:57 PPARA AM: 1543 variants, 102 matched, GWAS rows: summary-stats=3663
[info]  2026-10-27 09:08:57 PPARA PTV: 23 variants, 22 matched, GWAS rows: summary-stats=719
[warn]  2026-10-27 09:08:57 a1 vs Ensembl ref: 19249 matched SNV rows checked, 140 where a1 is not the Ensembl ref (e.g. 1:62604235:GG:G, 5:75355116:GG:GGG, 1:55052661:TGAC:TGACTGAC)
[stage] 2026-10-27 09:08:57 write
[info]  2026-10-27 09:08:59 wrote 35027 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_variants.tsv.gz

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
- last run: 2026-10-27 00:30:03
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 00:21:48 task 1: rows 1-1
[info]  2026-10-27 00:30:02 APOE_diplotype: results in /home/mvanvugt/projects/lipid_adem/results/APOE_diplotype

```

## [50] meta_analysis (`/home/mvanvugt/projects/lipid_adem/src/meta_analysis.py --ancestry EUR --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 marvel_ukb_EUR_all_cause_dementia marvel_ukb_EUR_all_cause_dementia_e44 marvel_ukb_EUR_all_cause_dementia_e43 marvel_ukb_EUR_all_cause_dementia_e33 marvel_ukb_EUR_all_cause_dementia_e22_e32 marvel_ukb_EUR_alzheimers_dementia marvel_ukb_EUR_alzheimers_dementia_e44 marvel_ukb_EUR_alzheimers_dementia_e43 marvel_ukb_EUR_alzheimers_dementia_e33 marvel_ukb_EUR_alzheimers_dementia_e22_e32 marvel_ukb_EUR_vascular_dementia marvel_ukb_EUR_vascular_dementia_e44 marvel_ukb_EUR_vascular_dementia_e43 marvel_ukb_EUR_vascular_dementia_e33 marvel_ukb_EUR_vascular_dementia_e22_e32 marvel_ukb_EUR_frontotemporal_dementia marvel_ukb_EUR_frontotemporal_dementia_e44 marvel_ukb_EUR_frontotemporal_dementia_e43 marvel_ukb_EUR_frontotemporal_dementia_e33 marvel_ukb_EUR_frontotemporal_dementia_e22_e32 marvel_ukb_EUR_ascvd marvel_ukb_EUR_ascvd_e44 marvel_ukb_EUR_ascvd_e43 marvel_ukb_EUR_ascvd_e33 marvel_ukb_EUR_ascvd_e22_e32 marvel_ukb_EUR_apoa marvel_ukb_EUR_apoa_e44 marvel_ukb_EUR_apoa_e43 marvel_ukb_EUR_apoa_e33 marvel_ukb_EUR_apoa_e22_e32 marvel_ukb_EUR_apob marvel_ukb_EUR_apob_e44 marvel_ukb_EUR_apob_e43 marvel_ukb_EUR_apob_e33 marvel_ukb_EUR_apob_e22_e32 marvel_ukb_EUR_hdl_c marvel_ukb_EUR_hdl_c_e44 marvel_ukb_EUR_hdl_c_e43 marvel_ukb_EUR_hdl_c_e33 marvel_ukb_EUR_hdl_c_e22_e32 marvel_ukb_EUR_ldl_c marvel_ukb_EUR_ldl_c_e44 marvel_ukb_EUR_ldl_c_e43 marvel_ukb_EUR_ldl_c_e33 marvel_ukb_EUR_ldl_c_e22_e32 marvel_ukb_EUR_tg marvel_ukb_EUR_tg_e44 marvel_ukb_EUR_tg_e43 marvel_ukb_EUR_tg_e33 marvel_ukb_EUR_tg_e22_e32 F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD I9_CVD_HARD --variant-sources PTV ClinVar AM --stratified --prefer-groups thomassen --fallback-groups marvel_ukb_EUR_all_cause_dementia marvel_ukb_EUR_alzheimers_dementia marvel_ukb_EUR_vascular_dementia marvel_ukb_EUR_frontotemporal_dementia marvel_ukb_EUR_ascvd marvel_ukb_EUR_apoa marvel_ukb_EUR_apob marvel_ukb_EUR_hdl_c marvel_ukb_EUR_ldl_c marvel_ukb_EUR_tg F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD I9_CVD_HARD --label pooled_eur_ptv_clinvar_am --ukb-burden`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-27 09:30:34
- commit: `244d529` (dirty)

Output:
```text
[info]  2026-10-27 09:29:53 ancestry EUR, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-27 09:29:53 load_matched
[info]  2026-10-27 09:29:54 /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/matched_variants.tsv.gz: 35027 rows, 887 variants
[info]  2026-10-27 09:29:54 16 rows of excluded gene(s) APOE dropped
[info]  2026-10-27 09:29:55 17498 of 35011 rows are EUR (all: AFR=366, AMR=116, CSA=1259, EAS=164, EUR=17498, MULTI=15602, NR=6)
[info]  2026-10-27 09:29:55 study_accession in GCST90861026, GCST90861027, GCST90861029, GCST90861030, marvel_ukb_EUR_all_cause_dementia, marvel_ukb_EUR_all_cause_dementia_e44, marvel_ukb_EUR_all_cause_dementia_e43, marvel_ukb_EUR_all_cause_dementia_e33, marvel_ukb_EUR_all_cause_dementia_e22_e32, marvel_ukb_EUR_alzheimers_dementia, marvel_ukb_EUR_alzheimers_dementia_e44, marvel_ukb_EUR_alzheimers_dementia_e43, marvel_ukb_EUR_alzheimers_dementia_e33, marvel_ukb_EUR_alzheimers_dementia_e22_e32, marvel_ukb_EUR_vascular_dementia, marvel_ukb_EUR_vascular_dementia_e44, marvel_ukb_EUR_vascular_dementia_e43, marvel_ukb_EUR_vascular_dementia_e33, marvel_ukb_EUR_vascular_dementia_e22_e32, marvel_ukb_EUR_frontotemporal_dementia, marvel_ukb_EUR_frontotemporal_dementia_e44, marvel_ukb_EUR_frontotemporal_dementia_e43, marvel_ukb_EUR_frontotemporal_dementia_e33, marvel_ukb_EUR_frontotemporal_dementia_e22_e32, marvel_ukb_EUR_ascvd, marvel_ukb_EUR_ascvd_e44, marvel_ukb_EUR_ascvd_e43, marvel_ukb_EUR_ascvd_e33, marvel_ukb_EUR_ascvd_e22_e32, marvel_ukb_EUR_apoa, marvel_ukb_EUR_apoa_e44, marvel_ukb_EUR_apoa_e43, marvel_ukb_EUR_apoa_e33, marvel_ukb_EUR_apoa_e22_e32, marvel_ukb_EUR_apob, marvel_ukb_EUR_apob_e44, marvel_ukb_EUR_apob_e43, marvel_ukb_EUR_apob_e33, marvel_ukb_EUR_apob_e22_e32, marvel_ukb_EUR_hdl_c, marvel_ukb_EUR_hdl_c_e44, marvel_ukb_EUR_hdl_c_e43, marvel_ukb_EUR_hdl_c_e33, marvel_ukb_EUR_hdl_c_e22_e32, marvel_ukb_EUR_ldl_c, marvel_ukb_EUR_ldl_c_e44, marvel_ukb_EUR_ldl_c_e43, marvel_ukb_EUR_ldl_c_e33, marvel_ukb_EUR_ldl_c_e22_e32, marvel_ukb_EUR_tg, marvel_ukb_EUR_tg_e44, marvel_ukb_EUR_tg_e43, marvel_ukb_EUR_tg_e33, marvel_ukb_EUR_tg_e22_e32, F5_DEMENTIA_INCLAVO, G6_ALZHEIMER, F5_VASCDEM, FTD, I9_CVD_HARD: 17219 of 17498 rows kept
[warn]  2026-10-27 09:29:55 no rows with study_accession I9_CVD_HARD
[stage] 2026-10-27 09:29:55 effect_scale
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apoa: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apoa_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apoa_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apoa_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apoa_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apob: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apob_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apob_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apob_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_apob_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_hdl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_hdl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_hdl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_hdl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_hdl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_ldl_c: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_ldl_c_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_ldl_c_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_ldl_c_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_ldl_c_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_tg: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_tg_e22_e32: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_tg_e33: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_tg_e43: effect scale linear, not log-OR; kept (--require-log-or drops)
[warn]  2026-10-27 09:29:55 marvel_ukb_EUR_tg_e44: effect scale linear, not log-OR; kept (--require-log-or drops)
[stage] 2026-10-27 09:29:55 prepare_effects
[info]  2026-10-27 09:29:55 10200 rows dropped: no beta or odds ratio
[info]  2026-10-27 09:29:55 7019 usable rows, 0 with SE derived from p
[stage] 2026-10-27 09:29:55 resolve_ambiguous
[stage] 2026-10-27 09:29:55 orient
[info]  2026-10-27 09:29:55 461 variants oriented as a2
[info]  2026-10-27 09:29:55 10 variants oriented as a2_gof_flipped
[info]  2026-10-27 09:29:55 8 ClinVar variants with direction lowering
[info]  2026-10-27 09:29:55 1 ClinVar variants with direction unknown
[info]  2026-10-27 09:29:55 variant_list_source in PTV, ClinVar, AM: 6816 of 7019 rows kept
[stage] 2026-10-27 09:29:55 apoe_strata
[info]  2026-10-27 09:29:55 /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/apoe_strata.tsv: 104 studies with an APOE stratum entry
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e44: 1 studies
[stage] 2026-10-27 09:29:55 choose_groups
[warn]  2026-10-27 09:29:55 no rows from study group(s) I9_CVD_HARD, thomassen
[info]  2026-10-27 09:29:55 ANGPTL3, all_cause_dementia: marvel_ukb_EUR_all_cause_dementia 26 variants
[info]  2026-10-27 09:29:55 ANGPTL3, alzheimers_dementia: marvel_ukb_EUR_alzheimers_dementia 20 variants
[info]  2026-10-27 09:29:55 ANGPTL3, apoa: marvel_ukb_EUR_apoa 65 variants
[info]  2026-10-27 09:29:55 ANGPTL3, apob: marvel_ukb_EUR_apob 65 variants
[info]  2026-10-27 09:29:55 ANGPTL3, ascvd: marvel_ukb_EUR_ascvd 37 variants
[info]  2026-10-27 09:29:55 ANGPTL3, frontotemporal_dementia: marvel_ukb_EUR_frontotemporal_dementia 17 variants
[info]  2026-10-27 09:29:55 ANGPTL3, hdl_c: marvel_ukb_EUR_hdl_c 65 variants
[info]  2026-10-27 09:29:55 ANGPTL3, ldl_c: marvel_ukb_EUR_ldl_c 65 variants
[info]  2026-10-27 09:29:55 ANGPTL3, tg: marvel_ukb_EUR_tg 65 variants
[info]  2026-10-27 09:29:55 ANGPTL3, vascular_dementia: marvel_ukb_EUR_vascular_dementia 22 variants
[info]  2026-10-27 09:29:55 CETP, all_cause_dementia: F5_DEMENTIA_INCLAVO 2 variants, marvel_ukb_EUR_all_cause_dementia 23 variants
[info]  2026-10-27 09:29:55 CETP, alzheimers_dementia: G6_ALZHEIMER 2 variants, marvel_ukb_EUR_alzheimers_dementia 21 variants
[info]  2026-10-27 09:29:55 CETP, apoa: marvel_ukb_EUR_apoa 59 variants
[info]  2026-10-27 09:29:55 CETP, apob: marvel_ukb_EUR_apob 59 variants
[info]  2026-10-27 09:29:55 CETP, ascvd: marvel_ukb_EUR_ascvd 40 variants
[info]  2026-10-27 09:29:55 CETP, frontotemporal_dementia: FTD 2 variants, marvel_ukb_EUR_frontotemporal_dementia 19 variants
[info]  2026-10-27 09:29:55 CETP, hdl_c: marvel_ukb_EUR_hdl_c 59 variants
[info]  2026-10-27 09:29:55 CETP, ldl_c: marvel_ukb_EUR_ldl_c 59 variants
[info]  2026-10-27 09:29:55 CETP, tg: marvel_ukb_EUR_tg 59 variants
[info]  2026-10-27 09:29:55 CETP, vascular_dementia: F5_VASCDEM 2 variants, marvel_ukb_EUR_vascular_dementia 20 variants
[info]  2026-10-27 09:29:55 HMGCR, all_cause_dementia: marvel_ukb_EUR_all_cause_dementia 43 variants
[info]  2026-10-27 09:29:55 HMGCR, alzheimers_dementia: marvel_ukb_EUR_alzheimers_dementia 30 variants
[info]  2026-10-27 09:29:55 HMGCR, apoa: marvel_ukb_EUR_apoa 134 variants
[info]  2026-10-27 09:29:55 HMGCR, apob: marvel_ukb_EUR_apob 134 variants
[info]  2026-10-27 09:29:55 HMGCR, ascvd: marvel_ukb_EUR_ascvd 79 variants
[info]  2026-10-27 09:29:55 HMGCR, frontotemporal_dementia: marvel_ukb_EUR_frontotemporal_dementia 11 variants
[info]  2026-10-27 09:29:55 HMGCR, hdl_c: marvel_ukb_EUR_hdl_c 134 variants
[info]  2026-10-27 09:29:55 HMGCR, ldl_c: marvel_ukb_EUR_ldl_c 134 variants
[info]  2026-10-27 09:29:55 HMGCR, tg: marvel_ukb_EUR_tg 134 variants
[info]  2026-10-27 09:29:55 HMGCR, vascular_dementia: marvel_ukb_EUR_vascular_dementia 21 variants
[info]  2026-10-27 09:29:55 NPC1L1, all_cause_dementia: F5_DEMENTIA_INCLAVO 1 variants, marvel_ukb_EUR_all_cause_dementia 22 variants
[info]  2026-10-27 09:29:55 NPC1L1, alzheimers_dementia: G6_ALZHEIMER 1 variants, marvel_ukb_EUR_alzheimers_dementia 16 variants
[info]  2026-10-27 09:29:55 NPC1L1, apoa: marvel_ukb_EUR_apoa 112 variants
[info]  2026-10-27 09:29:55 NPC1L1, apob: marvel_ukb_EUR_apob 112 variants
[info]  2026-10-27 09:29:55 NPC1L1, ascvd: marvel_ukb_EUR_ascvd 52 variants
[info]  2026-10-27 09:29:55 NPC1L1, frontotemporal_dementia: FTD 1 variants, marvel_ukb_EUR_frontotemporal_dementia 16 variants
[info]  2026-10-27 09:29:55 NPC1L1, hdl_c: marvel_ukb_EUR_hdl_c 112 variants
[info]  2026-10-27 09:29:55 NPC1L1, ldl_c: marvel_ukb_EUR_ldl_c 112 variants
[info]  2026-10-27 09:29:55 NPC1L1, tg: marvel_ukb_EUR_tg 112 variants
[info]  2026-10-27 09:29:55 NPC1L1, vascular_dementia: F5_VASCDEM 1 variants, marvel_ukb_EUR_vascular_dementia 16 variants
[info]  2026-10-27 09:29:55 PCSK9, all_cause_dementia: marvel_ukb_EUR_all_cause_dementia 13 variants
[info]  2026-10-27 09:29:55 PCSK9, alzheimers_dementia: marvel_ukb_EUR_alzheimers_dementia 10 variants
[info]  2026-10-27 09:29:55 PCSK9, apoa: marvel_ukb_EUR_apoa 43 variants
[info]  2026-10-27 09:29:55 PCSK9, apob: marvel_ukb_EUR_apob 43 variants
[info]  2026-10-27 09:29:55 PCSK9, ascvd: marvel_ukb_EUR_ascvd 18 variants
[info]  2026-10-27 09:29:55 PCSK9, frontotemporal_dementia: marvel_ukb_EUR_frontotemporal_dementia 6 variants
[info]  2026-10-27 09:29:55 PCSK9, hdl_c: marvel_ukb_EUR_hdl_c 43 variants
[info]  2026-10-27 09:29:55 PCSK9, ldl_c: marvel_ukb_EUR_ldl_c 43 variants
[info]  2026-10-27 09:29:55 PCSK9, tg: marvel_ukb_EUR_tg 43 variants
[info]  2026-10-27 09:29:55 PCSK9, vascular_dementia: marvel_ukb_EUR_vascular_dementia 7 variants
[info]  2026-10-27 09:29:55 PPARA, all_cause_dementia: F5_DEMENTIA_INCLAVO 2 variants, marvel_ukb_EUR_all_cause_dementia 14 variants
[info]  2026-10-27 09:29:55 PPARA, alzheimers_dementia: G6_ALZHEIMER 2 variants, marvel_ukb_EUR_alzheimers_dementia 13 variants
[info]  2026-10-27 09:29:55 PPARA, apoa: marvel_ukb_EUR_apoa 46 variants
[info]  2026-10-27 09:29:55 PPARA, apob: marvel_ukb_EUR_apob 46 variants
[info]  2026-10-27 09:29:55 PPARA, ascvd: marvel_ukb_EUR_ascvd 19 variants
[info]  2026-10-27 09:29:55 PPARA, frontotemporal_dementia: FTD 2 variants, marvel_ukb_EUR_frontotemporal_dementia 6 variants
[info]  2026-10-27 09:29:55 PPARA, hdl_c: marvel_ukb_EUR_hdl_c 46 variants
[info]  2026-10-27 09:29:55 PPARA, ldl_c: marvel_ukb_EUR_ldl_c 46 variants
[info]  2026-10-27 09:29:55 PPARA, tg: marvel_ukb_EUR_tg 46 variants
[info]  2026-10-27 09:29:55 PPARA, vascular_dementia: F5_VASCDEM 2 variants, marvel_ukb_EUR_vascular_dementia 8 variants
[info]  2026-10-27 09:29:55 0 fallback rows dropped for variants a preferred group has
[stage] 2026-10-27 09:29:55 ukb_burden
[info]  2026-10-27 09:29:55 UKB carrier burden (ptv_clinvar_am): 289 rows, ptv_clinvar_am 266, ptv_clinvar_am_fb 23
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_all_cause_dementia, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apoa, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_apob, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ascvd, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_hdl_c, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_ldl_c, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_tg, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum all: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e33: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e43: 1 studies
[info]  2026-10-27 09:29:55 study group marvel_ukb_EUR_vascular_dementia, stratum e44: 1 studies
[info]  2026-10-27 09:29:55 UKB carrier burden: 266 rows of mask ptv_clinvar_am, 0 as ptv_clinvar_am_fb (preferred groups have the gene and outcome)
[stage] 2026-10-27 09:29:55 pooled_run
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_all_cause_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_alzheimers_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_apoa: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_apob: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_ascvd: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_hdl_c: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_ldl_c: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_tg: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_vascular_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_all_cause_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_alzheimers_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_apoa: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_apob: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_ascvd: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_hdl_c: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_ldl_c: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_tg: unstratified run, strata left out
[info]  2026-10-27 09:29:55 pooled run, study group marvel_ukb_EUR_vascular_dementia: unstratified run, strata left out
[stage] 2026-10-27 09:29:55 dedupe
[info]  2026-10-27 09:29:55 54 duplicate rows removed
[info]  2026-10-27 09:29:55 0 estimates removed as copies of another study
[stage] 2026-10-27 09:29:55 meta_analyse
[info]  2026-10-27 09:30:01 1925 groups, 11 pooling more than one estimate
[info]  2026-10-27 09:30:08 1936 groups, 0 pooling more than one estimate
[stage] 2026-10-27 09:30:08 gene_burden
[info]  2026-10-27 09:30:08 gene burden: 1910 per-variant rows of the UKB burden studies replaced by 59 carrier-burden rows
[info]  2026-10-27 09:30:08 gene burden: 60 pooled and 72 per-study rows
[stage] 2026-10-27 09:30:08 write
[info]  2026-10-27 09:30:08 wrote 3861 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/meta_EUR_pooled_eur_ptv_clinvar_am.tsv.gz
[info]  2026-10-27 09:30:08 wrote 132 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/burden_EUR_pooled_eur_ptv_clinvar_am.tsv.gz
[stage] 2026-10-27 09:30:08 apoe_strata_run
[info]  2026-10-27 09:30:08 4826 rows from APOE strata: pooled per stratum
[stage] 2026-10-27 09:30:08 dedupe
[info]  2026-10-27 09:30:08 131 duplicate rows removed
[info]  2026-10-27 09:30:08 0 estimates removed as copies of another study
[stage] 2026-10-27 09:30:08 meta_analyse
[info]  2026-10-27 09:30:21 4695 groups, 0 pooling more than one estimate
[info]  2026-10-27 09:30:33 4695 groups, 0 pooling more than one estimate
[stage] 2026-10-27 09:30:33 gene_burden
[info]  2026-10-27 09:30:33 gene burden: 4606 per-variant rows of the UKB burden studies replaced by 207 carrier-burden rows
[info]  2026-10-27 09:30:33 gene burden: 232 pooled and 232 per-study rows
[stage] 2026-10-27 09:30:33 write
[info]  2026-10-27 09:30:34 wrote 9390 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/meta_EUR_pooled_eur_ptv_clinvar_am_apoe_strata.tsv.gz
[info]  2026-10-27 09:30:34 wrote 464 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/results/output/burden_EUR_pooled_eur_ptv_clinvar_am_apoe_strata.tsv.gz

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
- last run: 2026-10-26 15:04:34
- commit: `ecae536`

Output:
```text
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/ptv_variants.tsv.gz: 527 PTVs
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/plp_variants.tsv: 1900 rows; /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-10-26 15:04:33 0 P/LP rows with ref = alt dropped
[warn]  2026-10-26 15:04:33 APOE condition 'Alzheimer disease 3, protection against, due to APOE3-Christchurch' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 APOA1 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 ANGPTL3 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 PPARA condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 PCSK9 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 HMGCR condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 NPC1L1 condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 CETP condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 APOB condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-26 15:04:33 APOE condition 'nan' not in /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[info]  2026-10-26 15:04:33 262 truncating P/LP variants set to lowering, 213 of them against their conditions
[info]  2026-10-26 15:04:33 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-10-26 15:04:33 ANGPTL3 ClinVar P/LP: 2 variants unknown
[info]  2026-10-26 15:04:33 APOA1 ClinVar P/LP: 11 variants altered
[info]  2026-10-26 15:04:33 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-10-26 15:04:33 APOA1 ClinVar P/LP: 16 variants lowering
[info]  2026-10-26 15:04:33 APOA1 ClinVar P/LP: 6 variants unknown
[info]  2026-10-26 15:04:33 APOB ClinVar P/LP: 5 variants altered
[info]  2026-10-26 15:04:33 APOB ClinVar P/LP: 6 variants conflicting
[info]  2026-10-26 15:04:33 APOB ClinVar P/LP: 224 variants lowering
[info]  2026-10-26 15:04:33 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-10-26 15:04:33 APOE ClinVar P/LP: 12 variants altered
[info]  2026-10-26 15:04:33 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-10-26 15:04:33 APOE ClinVar P/LP: 6 variants unknown
[info]  2026-10-26 15:04:33 CETP ClinVar P/LP: 10 variants lowering
[info]  2026-10-26 15:04:33 CETP ClinVar P/LP: 2 variants unknown
[info]  2026-10-26 15:04:33 HMGCR ClinVar P/LP: 6 variants lowering
[info]  2026-10-26 15:04:33 HMGCR ClinVar P/LP: 3 variants unknown
[info]  2026-10-26 15:04:33 NPC1L1 ClinVar P/LP: 2 variants unknown
[info]  2026-10-26 15:04:33 PCSK9 ClinVar P/LP: 2 variants lowering
[info]  2026-10-26 15:04:33 PCSK9 ClinVar P/LP: 16 variants raising
[info]  2026-10-26 15:04:33 PCSK9 ClinVar P/LP: 2 variants unknown
[info]  2026-10-26 15:04:33 PPARA ClinVar P/LP: 2 variants unknown
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/gof_variants.tsv: 47 GoF variants
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/am_variants.tsv: 17323 AM variants of class Benign/Likely Benign
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/am_variants.tsv: 8342 AM variants of class Pathogenic/Likely pathogenic
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/am_variants.tsv: 2874 AM variants of class Uncertain significance
[info]  2026-10-26 15:04:33 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/am_variants.tsv: 8342 AM variants kept (Pathogenic/Likely pathogenic)
[warn]  2026-10-26 15:04:33 ANGPTL3 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 APOA1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 APOB ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 APOE ClinVar: 1 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 CETP ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 HMGCR ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 NPC1L1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 PCSK9 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-26 15:04:33 PPARA ClinVar: 2 rows without GRCh38 chr/pos/alleles
[info]  2026-10-26 15:04:33 normalisation AM: unchanged=8342
[info]  2026-10-26 15:04:33 normalisation ClinVar: no_sequence=20
[info]  2026-10-26 15:04:33 normalisation ClinVar: unchanged=316
[info]  2026-10-26 15:04:33 normalisation GoF: unchanged=19
[info]  2026-10-26 15:04:33 normalisation PTV: normalised=18
[info]  2026-10-26 15:04:33 normalisation PTV: unchanged=509
[info]  2026-10-26 15:04:33 66 sites are in several sources
[info]  2026-10-26 15:04:33 ANGPTL3 AM: 493 variants
[info]  2026-10-26 15:04:33 ANGPTL3 ClinVar: 12 variants
[info]  2026-10-26 15:04:33 ANGPTL3 PTV: 56 variants
[info]  2026-10-26 15:04:33 APOA1 ClinVar: 33 variants
[info]  2026-10-26 15:04:33 APOA1 PTV: 15 variants
[info]  2026-10-26 15:04:33 APOB ClinVar: 236 variants
[info]  2026-10-26 15:04:33 APOB PTV: 172 variants
[info]  2026-10-26 15:04:33 APOE ClinVar: 20 variants
[info]  2026-10-26 15:04:33 CETP AM: 439 variants
[info]  2026-10-26 15:04:33 CETP ClinVar: 10 variants
[info]  2026-10-26 15:04:33 CETP GoF: 1 variants
[info]  2026-10-26 15:04:33 CETP PTV: 58 variants
[info]  2026-10-26 15:04:33 HMGCR AM: 2623 variants
[info]  2026-10-26 15:04:33 HMGCR ClinVar: 7 variants
[info]  2026-10-26 15:04:33 HMGCR PTV: 39 variants
[info]  2026-10-26 15:04:33 NPC1L1 AM: 2507 variants
[info]  2026-10-26 15:04:33 NPC1L1 PTV: 96 variants
[info]  2026-10-26 15:04:33 PCSK9 AM: 737 variants
[info]  2026-10-26 15:04:33 PCSK9 ClinVar: 18 variants
[info]  2026-10-26 15:04:33 PCSK9 GoF: 18 variants
[info]  2026-10-26 15:04:33 PCSK9 PTV: 68 variants
[info]  2026-10-26 15:04:33 PPARA AM: 1543 variants
[info]  2026-10-26 15:04:33 PPARA PTV: 23 variants
[info]  2026-10-26 15:04:34 Wrote 9224 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-10-26 15:04:34 marvel lists: 9156 sites, 17 with an extra original-form row
[info]  2026-10-26 15:04:34 Wrote 556 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 46 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOA1_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 373 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOB_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 20 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/APOE_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 506 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/CETP_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 2668 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 2606 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 831 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[info]  2026-10-26 15:04:34 Wrote 1567 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/PPARA_variants.tsv

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
