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
- last run: 2026-10-07 10:52:52
- commit: `648f324`

Output:
```text
[info]  2026-10-07 10:49:37 9 genes, 84 icd codes
[stage] 2026-10-07 10:49:37 resolve_genes
[stage] 2026-10-07 10:49:37 resolve_efo
[info]  2026-10-07 10:49:38 trait ids checked: 21, obsolete replaced: 0
[info]  2026-10-07 10:49:38 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-07 10:49:38 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-07 10:49:38 finngen_manual
[info]  2026-10-07 10:49:41 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/study_outcome_review.tsv: 673 outcome x study exclusions for 10 outcomes
[info]  2026-10-07 10:49:41 catalog studies with aou, ukb excluded for every outcome
[info]  2026-10-07 10:49:41 all_cause_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 alzheimers_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 coronary_heart_disease: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 frontotemporal_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 hf: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 parkinsons_disease_dementia: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 stroke: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 sudden_cardiac_death: own results for finngen; catalog studies with these cohorts excluded
[info]  2026-10-07 10:49:41 vascular_dementia: own results for finngen; catalog studies with these cohorts excluded
[stage] 2026-10-07 10:49:41 discover_gwas
[info]  2026-10-07 10:49:48 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, finngen, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 10:49:49 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 10:49:49 EFO_0003913 (exact): 56 studies -> 38 dropped for cohort overlap (aou, ukb) -> 9 with full sumstats -> 9 included, 0 included with blank cohort
[info]  2026-10-07 10:49:58 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, finngen, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 10:49:59 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 10:49:59 EFO_0004269 (exact): 76 studies -> 28 dropped for cohort overlap (aou, ukb) -> 9 dropped by review -> 9 with full sumstats -> 9 included, 1 included with blank cohort
[info]  2026-10-07 10:50:01 EFO_0006799 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:03 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:04 EFO_0008584 (exact): 2 studies -> 2 dropped for cohort overlap (aou, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:07 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, finngen, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 10:50:08 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 10:50:08 EFO_0009492 (exact): 21 studies -> 10 dropped for cohort overlap (aou, ukb) -> 8 with full sumstats -> 8 included, 0 included with blank cohort
[info]  2026-10-07 10:50:10 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:11 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:11 EFO_0009493 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 5 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:13 EFO_0011057 (with child traits, cap per term and 30 total): 4 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 4 dropped by review -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:50:17 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:18 MONDO_0004648 (with child traits, cap per term and 30 total): 15 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 dropped by review -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:20 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, finngen, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:21 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:21 MONDO_0004781 (exact): 11 studies -> 6 dropped for cohort overlap (aou, ukb) -> 1 with full sumstats -> 1 included, 0 included with blank cohort
[info]  2026-10-07 10:50:56 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 72 dropped by review -> 7 with full sumstats -> 7 included, 2 included with blank cohort
[info]  2026-10-07 10:50:59 MONDO_0004975 (with child traits, cap per term and 30 total): 261 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 60 dropped by review -> 9 with full sumstats -> 9 included, 3 included with blank cohort
[info]  2026-10-07 10:51:27 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 74 dropped by review -> 16 with full sumstats -> 16 included, 5 included with blank cohort
[info]  2026-10-07 10:51:28 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-07 10:51:29 MONDO_0005010 (exact): 207 studies -> 41 dropped for cohort overlap (aou, ukb) -> 76 dropped by review -> 15 with full sumstats -> 15 included, 5 included with blank cohort
[info]  2026-10-07 10:51:47 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, finngen, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 10:51:47 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 10:51:48 MONDO_0005098 (exact): 134 studies -> 46 dropped for cohort overlap (aou, ukb) -> 16 dropped by review -> 24 with full sumstats -> 22 included, 0 included with blank cohort
[info]  2026-10-07 10:51:52 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, finngen, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:51:52 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:51:52 MONDO_0005099 (exact): 19 studies -> 9 dropped for cohort overlap (aou, ukb) -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:03 MONDO_0005252 (exact): 77 studies -> 37 dropped for cohort overlap (aou, finngen, ukb) -> 12 dropped by review -> 18 with full sumstats -> 16 included, 0 included with blank cohort
[info]  2026-10-07 10:52:04 MONDO_0005252 (exact): 77 studies -> 34 dropped for cohort overlap (aou, ukb) -> 13 dropped by review -> 20 with full sumstats -> 17 included, 0 included with blank cohort
[info]  2026-10-07 10:52:11 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, finngen, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:12 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:12 MONDO_0005267 (exact): 58 studies -> 41 dropped for cohort overlap (aou, ukb) -> 6 dropped by review -> 4 with full sumstats -> 4 included, 0 included with blank cohort
[info]  2026-10-07 10:52:15 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, finngen, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 10:52:15 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 10:52:16 MONDO_0005394 (exact): 10 studies -> 4 dropped for cohort overlap (aou, ukb) -> 3 with full sumstats -> 3 included, 0 included with blank cohort
[info]  2026-10-07 10:52:18 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:52:18 MONDO_0008243 (with child traits, cap per term and 30 total): 1 studies -> 0 dropped for cohort overlap (aou, finngen, ukb) -> 0 with full sumstats -> 0 included, 0 included with blank cohort
[info]  2026-10-07 10:52:23 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, finngen, ukb) -> 5 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 10:52:23 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 10:52:24 MONDO_0013792 (exact): 30 studies -> 11 dropped for cohort overlap (aou, ukb) -> 2 dropped by review -> 7 with full sumstats -> 7 included, 0 included with blank cohort
[info]  2026-10-07 10:52:25 EFO ids with 0 GWAS Catalog studies: 2
[stage] 2026-10-07 10:52:25 write_tasks
[info]  2026-10-07 10:52:31 wrote 124 tasks (311 study x outcome rows, 9 gene regions) to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-10-07 10:52:31 archived /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs -> /myriadfs/home/rmgpmva/projects/lipid_adem/src/logs/filter_task_logs_20261007_092533
[stage] 2026-10-07 10:52:31 scale_meta
[warn]  2026-10-07 10:52:46 GCST90477959: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477959)
[warn]  2026-10-07 10:52:46 GCST90477958: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477958)
[warn]  2026-10-07 10:52:46 GCST90246093: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246093)
[warn]  2026-10-07 10:52:46 GCST90399712: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90399712)
[warn]  2026-10-07 10:52:46 GCST90399711: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90399711)
[warn]  2026-10-07 10:52:46 GCST90726898: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726898)
[warn]  2026-10-07 10:52:46 GCST90246094: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246094)
[warn]  2026-10-07 10:52:46 GCST90246086: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246086)
[warn]  2026-10-07 10:52:46 GCST90246085: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246085)
[warn]  2026-10-07 10:52:46 GCST90726916: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726916)
[warn]  2026-10-07 10:52:47 GCST90432123: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432123)
[warn]  2026-10-07 10:52:47 GCST90246098: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246098)
[warn]  2026-10-07 10:52:47 GCST90726915: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726915)
[warn]  2026-10-07 10:52:47 GCST90432122: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90432122)
[warn]  2026-10-07 10:52:47 GCST90480188: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90480188)
[warn]  2026-10-07 10:52:47 GCST90477978: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477978)
[warn]  2026-10-07 10:52:47 GCST90477977: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90477977)
[warn]  2026-10-07 10:52:48 GCST90246096: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90246096)
[warn]  2026-10-07 10:52:48 GCST90018650: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018650)
[warn]  2026-10-07 10:52:48 GCST90726750: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90726750)
[warn]  2026-10-07 10:52:48 GCST90704648: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90704648)
[warn]  2026-10-07 10:52:48 GCST90727420: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90727420)
[warn]  2026-10-07 10:52:48 GCST90565439: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90565439)
[warn]  2026-10-07 10:52:48 GCST90566388: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90566388)
[warn]  2026-10-07 10:52:48 GCST90276158: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276158)
[warn]  2026-10-07 10:52:48 GCST90276157: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90276157)
[warn]  2026-10-07 10:52:48 GCST007511: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST007511)
[warn]  2026-10-07 10:52:48 GCST003452: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST003452)
[warn]  2026-10-07 10:52:48 GCST002245: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST002245)
[warn]  2026-10-07 10:52:48 GCST90861026: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861026)
[warn]  2026-10-07 10:52:48 GCST90861027: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861027)
[warn]  2026-10-07 10:52:48 GCST90861029: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861029)
[warn]  2026-10-07 10:52:48 GCST90861030: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90861030)
[warn]  2026-10-07 10:52:48 GCST90476370: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90476370)
[warn]  2026-10-07 10:52:48 GCST90018586: metadata yaml not read (429 Client Error: Too Many Requests for url: https://www.ebi.ac.uk/gwas/rest/api/v2/studies/GCST90018586)
[info]  2026-10-07 10:52:48 metadata yaml read for 115 included studies, scale: unknown=115
[info]  2026-10-07 10:52:49 wrote 2636 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv.gz

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
- last run: 2026-10-22 03:17:59
- commit: `d22d73f` (dirty)
- status: failed

Output:
```text
[info]  2026-10-22 03:17:59 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:59 stage: extract
[info]  2026-10-22 03:17:59 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:59 node: tcn5.local.snellius.surf.nl, job id: 28452648, task: 1
[info]  2026-10-22 03:17:59 task 1: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_ANGPTL3_chr1_plink.vcf.gz
[error] 2026-10-22 03:17:59 extract ukb_ANGPTL3_chr1_plink.vcf.gz: unexpected exit code 127
--- error output (raw) ---
[info]  2026-10-22 03:17:59 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:59 stage: extract
[info]  2026-10-22 03:17:59 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:59 node: tcn5.local.snellius.surf.nl, job id: 28452648, task: 1
[info]  2026-10-22 03:17:59 task 1: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_ANGPTL3_chr1_plink.vcf.gz

```

## [10] slurm_script_extract_task2
- first run: 2026-10-22 03:17:58
- last run: 2026-10-22 03:17:58
- commit: `d22d73f` (dirty)
- status: failed

Output:
```text
[info]  2026-10-22 03:17:58 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:58 stage: extract
[info]  2026-10-22 03:17:58 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:58 node: tcn17.local.snellius.surf.nl, job id: 28452649, task: 2
[info]  2026-10-22 03:17:58 task 2: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_CETP_chr16_plink.vcf.gz
[error] 2026-10-22 03:17:58 extract ukb_CETP_chr16_plink.vcf.gz: unexpected exit code 127
--- error output (raw) ---
[info]  2026-10-22 03:17:58 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:58 stage: extract
[info]  2026-10-22 03:17:58 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:58 node: tcn17.local.snellius.surf.nl, job id: 28452649, task: 2
[info]  2026-10-22 03:17:58 task 2: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_CETP_chr16_plink.vcf.gz

```

## [10] slurm_script_extract_task3
- first run: 2026-10-22 03:17:57
- last run: 2026-10-22 03:17:57
- commit: `d22d73f` (dirty)
- status: failed

Output:
```text
[info]  2026-10-22 03:17:57 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:57 stage: extract
[info]  2026-10-22 03:17:57 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:57 node: tcn26.local.snellius.surf.nl, job id: 28452650, task: 3
[info]  2026-10-22 03:17:57 task 3: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_HMGCR_chr5_plink.vcf.gz
[error] 2026-10-22 03:17:57 extract ukb_HMGCR_chr5_plink.vcf.gz: unexpected exit code 127
--- error output (raw) ---
[info]  2026-10-22 03:17:57 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:57 stage: extract
[info]  2026-10-22 03:17:57 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:57 node: tcn26.local.snellius.surf.nl, job id: 28452650, task: 3
[info]  2026-10-22 03:17:57 task 3: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_HMGCR_chr5_plink.vcf.gz

```

## [10] slurm_script_extract_task5
- first run: 2026-10-22 03:18:01
- last run: 2026-10-22 03:18:01
- commit: `d22d73f` (dirty)
- status: failed

Output:
```text
[info]  2026-10-22 03:18:01 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:18:01 stage: extract
[info]  2026-10-22 03:18:01 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:18:01 node: tcn97.local.snellius.surf.nl, job id: 28452652, task: 5
[info]  2026-10-22 03:18:01 task 5: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_PCSK9_chr1_plink.vcf.gz
[error] 2026-10-22 03:18:01 extract ukb_PCSK9_chr1_plink.vcf.gz: unexpected exit code 127
--- error output (raw) ---
[info]  2026-10-22 03:18:01 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:18:01 stage: extract
[info]  2026-10-22 03:18:01 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:18:01 node: tcn97.local.snellius.surf.nl, job id: 28452652, task: 5
[info]  2026-10-22 03:18:01 task 5: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_PCSK9_chr1_plink.vcf.gz

```

## [10] slurm_script_extract_task6
- first run: 2026-10-22 03:17:58
- last run: 2026-10-22 03:17:58
- commit: `d22d73f` (dirty)
- status: failed

Output:
```text
[info]  2026-10-22 03:17:58 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:58 stage: extract
[info]  2026-10-22 03:17:58 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:58 node: tcn102.local.snellius.surf.nl, job id: 28452629, task: 6
[info]  2026-10-22 03:17:58 task 6: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_PPARA_chr22_plink.vcf.gz
[error] 2026-10-22 03:17:58 extract ukb_PPARA_chr22_plink.vcf.gz: unexpected exit code 127
--- error output (raw) ---
[info]  2026-10-22 03:17:58 config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml
[info]  2026-10-22 03:17:58 stage: extract
[info]  2026-10-22 03:17:58 output directory: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:58 node: tcn102.local.snellius.surf.nl, job id: 28452629, task: 6
[info]  2026-10-22 03:17:58 task 6: /gpfs/home6/mvanvugt/projects/cetp_marvel/data/temp/ukb_PPARA_chr22_plink.vcf.gz

```

## [10] submit_two_source_submit_task1
- first run: 2026-10-21 21:41:00
- last run: 2026-10-22 03:17:19
- commit: `d22d73f` (dirty)

Output:
```text
[info]  2026-10-22 03:17:15 stage: submit; config: /home/mvanvugt/projects/lipid_adem/config/marvel_config.toml; output: /home/mvanvugt/projects/lipid_adem/data/temp/marvel
[info]  2026-10-22 03:17:17 6 plink gene VCF(s); chromosomes: 1 11 2 19 16 5 7 22
[info]  2026-10-22 03:17:19 submitted: J1 28452629, J2 28452630, J3 28452631, J4 28452632

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

## [25] marvel_results_table (`/home/rmgpmva/projects/lipid_adem/src/marvel_results_table.py --ancestry MULTI`)
- first run: 2026-10-08 09:54:25
- last run: 2026-10-13 17:44:55
- commit: `8781963`

Output:
```text
[stage] 2026-10-13 17:41:00 compare
[info]  2026-10-13 17:41:00 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_tasks.tsv: 18 rows, 6 genes
[info]  2026-10-13 17:41:02 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP: 667 loose result files
[info]  2026-10-13 17:41:05 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP_all_apoe: 667 loose result files
[info]  2026-10-13 17:41:09 /myriadfs/home/rmgpmva/projects/lipid_adem/results/CETP_eur: 667 loose result files
[info]  2026-10-13 17:41:26 CETP: 874437 loose rows, 0 new, 874437 already in the store
[info]  2026-10-13 17:41:29 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR: 714 loose result files
[info]  2026-10-13 17:41:32 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR_all_apoe: 714 loose result files
[info]  2026-10-13 17:41:36 /myriadfs/home/rmgpmva/projects/lipid_adem/results/HMGCR_eur: 714 loose result files
[info]  2026-10-13 17:41:53 HMGCR: 936054 loose rows, 0 new, 936054 already in the store
[info]  2026-10-13 17:41:58 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1: 1257 loose result files
[info]  2026-10-13 17:42:04 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1_all_apoe: 1257 loose result files
[info]  2026-10-13 17:42:12 /myriadfs/home/rmgpmva/projects/lipid_adem/results/NPC1L1_eur: 1257 loose result files
[info]  2026-10-13 17:42:19 NPC1L1: 1671810 loose rows, 1504629 new, 167181 already in the store
[warn]  2026-10-13 17:42:19 NPC1L1: 1504629 rows added to NPC1L1_results.tsv.gz (1265 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, e22_e32, e33, e43, e44; Variable: all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-13 17:42:24 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9: 1047 loose result files
[info]  2026-10-13 17:42:29 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9_all_apoe: 1047 loose result files
[info]  2026-10-13 17:42:36 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9_eur: 1047 loose result files
[info]  2026-10-13 17:42:48 PCSK9: 1392510 loose rows, 835506 new, 557004 already in the store
[warn]  2026-10-13 17:42:48 PCSK9: 835506 rows added to PCSK9_results.tsv.gz (1055 exposures; Model name: model_1, model_2, model_3; Stratification name: EUR, EUR_e22_e32, EUR_e33, EUR_e43, EUR_e44, overall; Variable: all_cause_dementia_algo, all_cause_dementia_combined, alzheimers_disease_algo, alzheimers_disease_combined, ascvd_ii, frontotemporal_dementia_algo, vascular_dementia_algo)
[info]  2026-10-13 17:42:50 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3: 324 loose result files
[info]  2026-10-13 17:42:52 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3_all_apoe: 324 loose result files
[info]  2026-10-13 17:42:54 /myriadfs/home/rmgpmva/projects/lipid_adem/results/ANGPTL3_eur: 324 loose result files
[info]  2026-10-13 17:43:01 ANGPTL3: 424764 loose rows, 0 new, 424764 already in the store
[info]  2026-10-13 17:43:02 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA: 343 loose result files
[info]  2026-10-13 17:43:04 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA_all_apoe: 343 loose result files
[info]  2026-10-13 17:43:07 /myriadfs/home/rmgpmva/projects/lipid_adem/results/PPARA_eur: 343 loose result files
[info]  2026-10-13 17:43:14 PPARA: 449673 loose rows, 0 new, 449673 already in the store
[stage] 2026-10-13 17:43:14 write_stores
[info]  2026-10-13 17:43:59 NPC1L1: wrote 1671810 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/NPC1L1_results.tsv.gz
[info]  2026-10-13 17:44:35 PCSK9: wrote 1392510 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/marvel/PCSK9_results.tsv.gz
[stage] 2026-10-13 17:44:35 marvel_table
[info]  2026-10-13 17:44:37 ANGPTL3: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-13 17:44:39 CETP: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-13 17:44:43 HMGCR: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-13 17:44:48 NPC1L1: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-13 17:44:53 PCSK9: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-13 17:44:54 PPARA: variables not in Constants.MARVEL_UKB_OUTCOMES, left out: all_cause_dementia_algo, alzheimers_disease_algo, ascvd_ii
[info]  2026-10-13 17:44:54 wrote 240 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/marvel_results.tsv
[info]  2026-10-13 17:44:54 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/apoe_strata.tsv: all marvel strata already listed

```

## [30] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-10-13 18:08:03
- commit: `8781963`

Output:
```text
[stage] 2026-10-13 17:51:13 load_sumstats
[info]  2026-10-13 17:51:14 summary-stats: 124 files, 593027 rows incl. one copy per outcome (0 missing)
[info]  2026-10-13 17:51:19 MONDO_0011057 (all_cause_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[info]  2026-10-13 17:51:19 MONDO_0011057 (vascular_dementia) in Constants.EXCLUDED_EFO_IDS, skipped
[stage] 2026-10-13 17:51:19 marvel
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 25 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 2369 rows -> 237 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 29 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 2365 rows -> 233 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 29 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 2365 rows -> 233 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 30 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 2364 rows -> 232 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 233 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 2347 rows -> 19 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb all_cause_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 233 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 40 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 2346 rows -> 18 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb alzheimers_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 233 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 48 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 2338 rows -> 10 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb vascular_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 297 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 233 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 52 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 2334 rows -> 6 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:21 marvel ukb frontotemporal_dementia: 2328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 71 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 83 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 2240 rows -> 108 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 71 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 89 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 2234 rows -> 102 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 71 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 97 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 2226 rows -> 94 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 71 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 102 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 2221 rows -> 89 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 2132 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 32 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 59 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 2249 rows -> 166 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 2083 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 32 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 66 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 2242 rows -> 159 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 2083 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 32 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 71 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 2237 rows -> 154 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 2083 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 576 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 32 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 73 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 2235 rows -> 152 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb frontotemporal_dementia: 2083 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 103 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 2226 rows -> 49 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb all_cause_dementia: 2177 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 108 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 2221 rows -> 44 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb alzheimers_dementia: 2177 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 108 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 2221 rows -> 44 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:22 marvel ukb vascular_dementia: 2177 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 468 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 119 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 120 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 2209 rows -> 32 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 2177 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 80 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 2435 rows -> 175 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 2260 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 90 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 2425 rows -> 165 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 2260 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 94 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 2421 rows -> 162 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 2259 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 378 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 23 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 100 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 2415 rows -> 156 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 2259 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 246 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 37 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 2381 rows -> 13 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 246 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 39 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 2379 rows -> 11 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 246 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 43 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 2375 rows -> 7 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb vascular_dementia: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 252 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 246 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 45 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 2373 rows -> 5 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb frontotemporal_dementia: 2368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 92 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 94 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 2343 rows -> 91 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb all_cause_dementia: 2252 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 92 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 101 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 2336 rows -> 84 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:23 marvel ukb alzheimers_dementia: 2252 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 92 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 112 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 2325 rows -> 74 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 2251 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 387 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 92 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 115 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 2322 rows -> 71 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 2251 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 70 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 96 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 2381 rows -> 114 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 2267 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 70 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 107 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 2370 rows -> 103 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 2267 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 70 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 104 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 2373 rows -> 106 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 2267 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 369 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 70 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 112 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 2365 rows -> 98 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 2267 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 104 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 2235 rows -> 34 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb all_cause_dementia: 2201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 107 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 2232 rows -> 31 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb alzheimers_dementia: 2201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 107 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 2232 rows -> 31 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb vascular_dementia: 2201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 441 rows with < 5 exposed dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 112 rows with SE > 30.0 (separation) dropped (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 2227 rows -> 26 variant rows, 0 gene-burden rows (ANGPTL3_results.tsv.gz)
[info]  2026-10-13 17:51:24 marvel ukb frontotemporal_dementia: 2201 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 35 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 4672 rows -> 338 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 4334 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:28 marvel ukb alzheimers_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb alzheimers_dementia: 49 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb alzheimers_dementia: 4658 rows -> 329 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb alzheimers_dementia: 4329 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:28 marvel ukb vascular_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb vascular_dementia: 52 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb vascular_dementia: 4655 rows -> 324 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb vascular_dementia: 4331 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:28 marvel ukb frontotemporal_dementia: 1296 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb frontotemporal_dementia: 72 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb frontotemporal_dementia: 4635 rows -> 311 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb frontotemporal_dementia: 4324 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 468 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 61 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 4781 rows -> 52 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:28 marvel ukb all_cause_dementia: 4729 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 468 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 68 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 4774 rows -> 45 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 4729 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 468 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 78 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 4764 rows -> 38 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 4726 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:29 marvel ukb frontotemporal_dementia: 693 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb frontotemporal_dementia: 468 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb frontotemporal_dementia: 94 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb frontotemporal_dementia: 4748 rows -> 27 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb frontotemporal_dementia: 4721 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:29 marvel ukb all_cause_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb all_cause_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb all_cause_dementia: 149 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb all_cause_dementia: 4465 rows -> 159 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb all_cause_dementia: 4306 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 153 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 4461 rows -> 156 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb alzheimers_dementia: 4305 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 175 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 4439 rows -> 138 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:29 marvel ukb vascular_dementia: 4301 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 1224 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 192 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 4422 rows -> 122 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 4300 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 53 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 97 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 4584 rows -> 257 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 4327 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:30 marvel ukb alzheimers_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb alzheimers_dementia: 53 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb alzheimers_dementia: 123 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb alzheimers_dementia: 4558 rows -> 241 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb alzheimers_dementia: 4317 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:30 marvel ukb vascular_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb vascular_dementia: 53 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb vascular_dementia: 122 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb vascular_dementia: 4559 rows -> 239 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb vascular_dementia: 4320 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 1269 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 53 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 135 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 4546 rows -> 232 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb frontotemporal_dementia: 4314 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 162 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 4439 rows -> 108 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:30 marvel ukb all_cause_dementia: 4331 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 170 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 4431 rows -> 101 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 4330 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 186 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 4415 rows -> 90 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 4325 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:31 marvel ukb frontotemporal_dementia: 1170 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb frontotemporal_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb frontotemporal_dementia: 205 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb frontotemporal_dementia: 4396 rows -> 75 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb frontotemporal_dementia: 4321 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:31 marvel ukb all_cause_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb all_cause_dementia: 61 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb all_cause_dementia: 150 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb all_cause_dementia: 4865 rows -> 255 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb all_cause_dementia: 4610 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 61 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 169 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 4846 rows -> 244 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb alzheimers_dementia: 4602 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 61 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 171 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 4844 rows -> 239 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:31 marvel ukb vascular_dementia: 4605 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 927 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 61 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 192 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 4823 rows -> 225 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 4598 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 498 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 54 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 4857 rows -> 42 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 4815 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:32 marvel ukb alzheimers_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb alzheimers_dementia: 498 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb alzheimers_dementia: 61 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb alzheimers_dementia: 4850 rows -> 36 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb alzheimers_dementia: 4814 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:32 marvel ukb vascular_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb vascular_dementia: 498 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb vascular_dementia: 66 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb vascular_dementia: 4845 rows -> 32 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb vascular_dementia: 4813 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 594 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 498 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 75 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 4836 rows -> 27 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb frontotemporal_dementia: 4809 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 224 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 159 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 4621 rows -> 123 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:32 marvel ukb all_cause_dementia: 4498 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 224 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 165 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 4615 rows -> 117 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 4498 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 224 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 173 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 4607 rows -> 112 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 4495 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:33 marvel ukb frontotemporal_dementia: 999 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb frontotemporal_dementia: 224 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb frontotemporal_dementia: 186 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb frontotemporal_dementia: 4594 rows -> 99 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb frontotemporal_dementia: 4495 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:33 marvel ukb all_cause_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb all_cause_dementia: 106 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb all_cause_dementia: 180 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb all_cause_dementia: 4682 rows -> 188 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb all_cause_dementia: 4494 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 106 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 205 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 4657 rows -> 172 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb alzheimers_dementia: 4485 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 106 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 200 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 4662 rows -> 174 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:33 marvel ukb vascular_dementia: 4488 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 1035 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 106 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 214 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 4648 rows -> 166 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 4482 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:34 marvel ukb all_cause_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb all_cause_dementia: 292 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb all_cause_dementia: 160 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb all_cause_dementia: 4543 rows -> 80 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb all_cause_dementia: 4463 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:34 marvel ukb alzheimers_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb alzheimers_dementia: 292 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb alzheimers_dementia: 164 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb alzheimers_dementia: 4539 rows -> 76 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb alzheimers_dementia: 4463 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:34 marvel ukb vascular_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb vascular_dementia: 292 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb vascular_dementia: 167 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb vascular_dementia: 4536 rows -> 73 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb vascular_dementia: 4463 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 1008 rows with < 5 exposed dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 292 rows with SE < 1e-06 (degenerate fit) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 176 rows with SE > 30.0 (separation) dropped (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 4527 rows -> 67 variant rows, 0 gene-burden rows (CETP_results.tsv.gz)
[info]  2026-10-13 17:51:34 marvel ukb frontotemporal_dementia: 4460 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:38 marvel ukb all_cause_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb all_cause_dementia: 15 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb all_cause_dementia: 5961 rows -> 380 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb all_cause_dementia: 5581 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:38 marvel ukb alzheimers_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb alzheimers_dementia: 5962 rows -> 381 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb alzheimers_dementia: 5581 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:38 marvel ukb vascular_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb vascular_dementia: 15 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb vascular_dementia: 5961 rows -> 380 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb vascular_dementia: 5581 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:38 marvel ukb frontotemporal_dementia: 450 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb frontotemporal_dementia: 15 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb frontotemporal_dementia: 5961 rows -> 380 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:38 marvel ukb frontotemporal_dementia: 5581 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 448 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 166 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 5542 rows -> 34 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 5508 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 448 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 189 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 5519 rows -> 28 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 5491 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:39 marvel ukb vascular_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb vascular_dementia: 448 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb vascular_dementia: 222 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb vascular_dementia: 5486 rows -> 14 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb vascular_dementia: 5472 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:39 marvel ukb frontotemporal_dementia: 270 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb frontotemporal_dementia: 448 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb frontotemporal_dementia: 230 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb frontotemporal_dementia: 5478 rows -> 6 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb frontotemporal_dementia: 5472 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 125 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 211 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 5217 rows -> 167 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb all_cause_dementia: 5050 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 125 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 237 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 5191 rows -> 154 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:39 marvel ukb alzheimers_dementia: 5037 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 125 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 265 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 5163 rows -> 138 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 5025 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:40 marvel ukb frontotemporal_dementia: 873 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb frontotemporal_dementia: 125 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb frontotemporal_dementia: 282 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb frontotemporal_dementia: 5146 rows -> 127 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb frontotemporal_dementia: 5019 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:40 marvel ukb all_cause_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb all_cause_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb all_cause_dementia: 126 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb all_cause_dementia: 5587 rows -> 280 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb all_cause_dementia: 5307 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:40 marvel ukb alzheimers_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb alzheimers_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb alzheimers_dementia: 150 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb alzheimers_dementia: 5563 rows -> 270 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb alzheimers_dementia: 5293 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 161 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 5552 rows -> 265 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:40 marvel ukb vascular_dementia: 5287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 675 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 38 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 162 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 5551 rows -> 264 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 5287 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:41 marvel ukb all_cause_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb all_cause_dementia: 195 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb all_cause_dementia: 281 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb all_cause_dementia: 5257 rows -> 94 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb all_cause_dementia: 5163 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:41 marvel ukb alzheimers_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb alzheimers_dementia: 195 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb alzheimers_dementia: 314 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb alzheimers_dementia: 5224 rows -> 82 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb alzheimers_dementia: 5142 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:41 marvel ukb vascular_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb vascular_dementia: 195 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb vascular_dementia: 311 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb vascular_dementia: 5227 rows -> 77 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb vascular_dementia: 5150 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 693 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 195 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 329 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 5209 rows -> 67 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:41 marvel ukb frontotemporal_dementia: 5142 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 31 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 111 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 6023 rows -> 309 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 5714 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 31 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 114 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 6020 rows -> 306 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 5714 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:42 marvel ukb vascular_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb vascular_dementia: 31 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb vascular_dementia: 123 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb vascular_dementia: 6011 rows -> 297 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb vascular_dementia: 5714 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:42 marvel ukb frontotemporal_dementia: 261 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb frontotemporal_dementia: 31 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb frontotemporal_dementia: 137 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb frontotemporal_dementia: 5997 rows -> 291 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb frontotemporal_dementia: 5706 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 461 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 160 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 5580 rows -> 32 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb all_cause_dementia: 5548 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 461 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 183 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 5557 rows -> 26 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:42 marvel ukb alzheimers_dementia: 5531 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 461 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 216 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 5524 rows -> 12 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 5512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 225 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 461 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 222 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 5518 rows -> 6 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 5512 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:43 marvel ukb all_cause_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb all_cause_dementia: 153 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb all_cause_dementia: 246 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb all_cause_dementia: 5307 rows -> 142 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb all_cause_dementia: 5165 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:43 marvel ukb alzheimers_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb alzheimers_dementia: 153 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb alzheimers_dementia: 272 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb alzheimers_dementia: 5281 rows -> 129 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb alzheimers_dementia: 5152 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 153 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 294 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 5259 rows -> 113 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb vascular_dementia: 5146 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 720 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 153 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 309 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 5244 rows -> 104 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:43 marvel ukb frontotemporal_dementia: 5140 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 198 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 5668 rows -> 219 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 5449 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:44 marvel ukb alzheimers_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb alzheimers_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb alzheimers_dementia: 222 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb alzheimers_dementia: 5644 rows -> 209 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb alzheimers_dementia: 5435 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:44 marvel ukb vascular_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb vascular_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb vascular_dementia: 231 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb vascular_dementia: 5635 rows -> 206 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb vascular_dementia: 5429 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:44 marvel ukb frontotemporal_dementia: 486 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb frontotemporal_dementia: 74 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb frontotemporal_dementia: 238 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb frontotemporal_dementia: 5628 rows -> 199 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb frontotemporal_dementia: 5429 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 220 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 285 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 5327 rows -> 76 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:44 marvel ukb all_cause_dementia: 5251 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:45 marvel ukb alzheimers_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb alzheimers_dementia: 220 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb alzheimers_dementia: 317 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb alzheimers_dementia: 5295 rows -> 65 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb alzheimers_dementia: 5230 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:45 marvel ukb vascular_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb vascular_dementia: 220 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb vascular_dementia: 315 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb vascular_dementia: 5297 rows -> 59 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb vascular_dementia: 5238 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:45 marvel ukb frontotemporal_dementia: 594 rows with < 5 exposed dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb frontotemporal_dementia: 220 rows with SE < 1e-06 (degenerate fit) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb frontotemporal_dementia: 327 rows with SE > 30.0 (separation) dropped (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb frontotemporal_dementia: 5285 rows -> 55 variant rows, 0 gene-burden rows (HMGCR_results.tsv.gz)
[info]  2026-10-13 17:51:45 marvel ukb frontotemporal_dementia: 5230 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:51 marvel ukb all_cause_dementia: 4410 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:51 marvel ukb all_cause_dementia: 167 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:51 marvel ukb all_cause_dementia: 6736 rows -> 487 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:51 marvel ukb all_cause_dementia: 6249 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:52 marvel ukb alzheimers_dementia: 4410 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb alzheimers_dementia: 196 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb alzheimers_dementia: 6707 rows -> 461 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb alzheimers_dementia: 6246 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:52 marvel ukb vascular_dementia: 4410 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb vascular_dementia: 201 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb vascular_dementia: 6702 rows -> 455 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb vascular_dementia: 6247 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:52 marvel ukb frontotemporal_dementia: 4410 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb frontotemporal_dementia: 228 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb frontotemporal_dementia: 6675 rows -> 428 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:52 marvel ukb frontotemporal_dementia: 6247 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:53 marvel ukb all_cause_dementia: 1341 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb all_cause_dementia: 1022 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb all_cause_dementia: 34 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb all_cause_dementia: 8916 rows -> 48 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb all_cause_dementia: 8868 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:53 marvel ukb alzheimers_dementia: 1341 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb alzheimers_dementia: 1022 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb alzheimers_dementia: 40 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb alzheimers_dementia: 8910 rows -> 43 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb alzheimers_dementia: 8867 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:53 marvel ukb vascular_dementia: 1341 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb vascular_dementia: 1022 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb vascular_dementia: 53 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb vascular_dementia: 8897 rows -> 30 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb vascular_dementia: 8867 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:53 marvel ukb frontotemporal_dementia: 1341 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb frontotemporal_dementia: 1022 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:53 marvel ukb frontotemporal_dementia: 77 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb frontotemporal_dementia: 8873 rows -> 9 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb frontotemporal_dementia: 8864 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:54 marvel ukb all_cause_dementia: 3510 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb all_cause_dementia: 494 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb all_cause_dementia: 189 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb all_cause_dementia: 7120 rows -> 157 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb all_cause_dementia: 6963 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:54 marvel ukb alzheimers_dementia: 3510 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb alzheimers_dementia: 494 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb alzheimers_dementia: 202 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb alzheimers_dementia: 7107 rows -> 145 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb alzheimers_dementia: 6962 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:54 marvel ukb vascular_dementia: 3510 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb vascular_dementia: 494 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb vascular_dementia: 217 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb vascular_dementia: 7092 rows -> 127 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:54 marvel ukb vascular_dementia: 6965 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:55 marvel ukb frontotemporal_dementia: 3510 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb frontotemporal_dementia: 494 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb frontotemporal_dementia: 251 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb frontotemporal_dementia: 7058 rows -> 99 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb frontotemporal_dementia: 6959 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:55 marvel ukb all_cause_dementia: 4041 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb all_cause_dementia: 189 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb all_cause_dementia: 233 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb all_cause_dementia: 6850 rows -> 319 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb all_cause_dementia: 6531 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:55 marvel ukb alzheimers_dementia: 4041 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb alzheimers_dementia: 189 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb alzheimers_dementia: 264 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb alzheimers_dementia: 6819 rows -> 290 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:55 marvel ukb alzheimers_dementia: 6529 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:56 marvel ukb vascular_dementia: 4041 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb vascular_dementia: 189 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb vascular_dementia: 271 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb vascular_dementia: 6812 rows -> 283 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb vascular_dementia: 6529 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:56 marvel ukb frontotemporal_dementia: 4041 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb frontotemporal_dementia: 189 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb frontotemporal_dementia: 283 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb frontotemporal_dementia: 6800 rows -> 271 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb frontotemporal_dementia: 6529 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:56 marvel ukb all_cause_dementia: 2970 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb all_cause_dementia: 681 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb all_cause_dementia: 138 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb all_cause_dementia: 7524 rows -> 92 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:56 marvel ukb all_cause_dementia: 7432 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:57 marvel ukb alzheimers_dementia: 2970 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb alzheimers_dementia: 681 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb alzheimers_dementia: 158 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb alzheimers_dementia: 7504 rows -> 77 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb alzheimers_dementia: 7427 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:57 marvel ukb vascular_dementia: 2970 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb vascular_dementia: 681 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb vascular_dementia: 160 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb vascular_dementia: 7502 rows -> 75 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb vascular_dementia: 7427 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:57 marvel ukb frontotemporal_dementia: 2970 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb frontotemporal_dementia: 681 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb frontotemporal_dementia: 187 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb frontotemporal_dementia: 7475 rows -> 47 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb frontotemporal_dementia: 7428 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:57 marvel ukb all_cause_dementia: 3195 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb all_cause_dementia: 208 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb all_cause_dementia: 275 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb all_cause_dementia: 7635 rows -> 338 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:57 marvel ukb all_cause_dementia: 7297 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:58 marvel ukb alzheimers_dementia: 3195 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb alzheimers_dementia: 208 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb alzheimers_dementia: 305 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb alzheimers_dementia: 7605 rows -> 313 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb alzheimers_dementia: 7292 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:58 marvel ukb vascular_dementia: 3195 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb vascular_dementia: 208 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb vascular_dementia: 312 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb vascular_dementia: 7598 rows -> 305 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb vascular_dementia: 7293 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:58 marvel ukb frontotemporal_dementia: 3195 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb frontotemporal_dementia: 208 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb frontotemporal_dementia: 334 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb frontotemporal_dementia: 7576 rows -> 283 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:58 marvel ukb frontotemporal_dementia: 7293 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:59 marvel ukb all_cause_dementia: 1143 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb all_cause_dementia: 1065 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb all_cause_dementia: 26 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb all_cause_dementia: 9079 rows -> 38 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb all_cause_dementia: 9041 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:59 marvel ukb alzheimers_dementia: 1143 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb alzheimers_dementia: 1065 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb alzheimers_dementia: 32 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb alzheimers_dementia: 9073 rows -> 33 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb alzheimers_dementia: 9040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:51:59 marvel ukb vascular_dementia: 1143 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb vascular_dementia: 1065 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb vascular_dementia: 40 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb vascular_dementia: 9065 rows -> 25 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:51:59 marvel ukb vascular_dementia: 9040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:00 marvel ukb frontotemporal_dementia: 1143 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb frontotemporal_dementia: 1065 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb frontotemporal_dementia: 56 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb frontotemporal_dementia: 9049 rows -> 9 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb frontotemporal_dementia: 9040 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:00 marvel ukb all_cause_dementia: 2871 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb all_cause_dementia: 606 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb all_cause_dementia: 182 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb all_cause_dementia: 7654 rows -> 127 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb all_cause_dementia: 7527 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:00 marvel ukb alzheimers_dementia: 2871 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb alzheimers_dementia: 606 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb alzheimers_dementia: 200 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb alzheimers_dementia: 7636 rows -> 112 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:00 marvel ukb alzheimers_dementia: 7524 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:00 marvel ukb vascular_dementia: 2871 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb vascular_dementia: 606 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb vascular_dementia: 208 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb vascular_dementia: 7628 rows -> 99 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb vascular_dementia: 7529 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:01 marvel ukb frontotemporal_dementia: 2871 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb frontotemporal_dementia: 606 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb frontotemporal_dementia: 237 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb frontotemporal_dementia: 7599 rows -> 76 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb frontotemporal_dementia: 7523 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:01 marvel ukb all_cause_dementia: 3069 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb all_cause_dementia: 388 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb all_cause_dementia: 251 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb all_cause_dementia: 7605 rows -> 221 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb all_cause_dementia: 7384 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:01 marvel ukb alzheimers_dementia: 3069 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb alzheimers_dementia: 388 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb alzheimers_dementia: 277 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb alzheimers_dementia: 7579 rows -> 197 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:01 marvel ukb alzheimers_dementia: 7382 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:02 marvel ukb vascular_dementia: 3069 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb vascular_dementia: 388 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb vascular_dementia: 278 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb vascular_dementia: 7578 rows -> 196 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb vascular_dementia: 7382 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:02 marvel ukb frontotemporal_dementia: 3069 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb frontotemporal_dementia: 388 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb frontotemporal_dementia: 297 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb frontotemporal_dementia: 7559 rows -> 177 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb frontotemporal_dementia: 7382 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:02 marvel ukb all_cause_dementia: 2439 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb all_cause_dementia: 770 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb all_cause_dementia: 139 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb all_cause_dementia: 7965 rows -> 65 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:02 marvel ukb all_cause_dementia: 7900 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:03 marvel ukb alzheimers_dementia: 2439 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb alzheimers_dementia: 770 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb alzheimers_dementia: 151 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb alzheimers_dementia: 7953 rows -> 56 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb alzheimers_dementia: 7897 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:03 marvel ukb vascular_dementia: 2439 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb vascular_dementia: 770 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb vascular_dementia: 155 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb vascular_dementia: 7949 rows -> 52 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb vascular_dementia: 7897 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:03 marvel ukb frontotemporal_dementia: 2439 rows with < 5 exposed dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb frontotemporal_dementia: 770 rows with SE < 1e-06 (degenerate fit) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb frontotemporal_dementia: 166 rows with SE > 30.0 (separation) dropped (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb frontotemporal_dementia: 7938 rows -> 38 variant rows, 0 gene-burden rows (NPC1L1_results.tsv.gz)
[info]  2026-10-13 17:52:03 marvel ukb frontotemporal_dementia: 7900 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:08 marvel ukb all_cause_dementia: 1134 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:08 marvel ukb all_cause_dementia: 880 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:08 marvel ukb all_cause_dementia: 22 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:08 marvel ukb all_cause_dementia: 7387 rows -> 15 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:08 marvel ukb all_cause_dementia: 7372 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:09 marvel ukb alzheimers_dementia: 1134 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb alzheimers_dementia: 880 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb alzheimers_dementia: 28 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb alzheimers_dementia: 7381 rows -> 12 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb alzheimers_dementia: 7369 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:09 marvel ukb vascular_dementia: 1134 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb vascular_dementia: 880 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb vascular_dementia: 34 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb vascular_dementia: 7375 rows -> 7 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb vascular_dementia: 7368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:09 marvel ukb frontotemporal_dementia: 1134 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb frontotemporal_dementia: 880 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb frontotemporal_dementia: 37 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb frontotemporal_dementia: 7372 rows -> 4 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb frontotemporal_dementia: 7368 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:09 marvel ukb all_cause_dementia: 3123 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb all_cause_dementia: 450 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb all_cause_dementia: 144 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb all_cause_dementia: 5706 rows -> 78 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:09 marvel ukb all_cause_dementia: 5628 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:10 marvel ukb alzheimers_dementia: 3123 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb alzheimers_dementia: 450 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb alzheimers_dementia: 160 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb alzheimers_dementia: 5690 rows -> 71 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb alzheimers_dementia: 5619 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:10 marvel ukb vascular_dementia: 3123 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb vascular_dementia: 450 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb vascular_dementia: 172 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb vascular_dementia: 5678 rows -> 58 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb vascular_dementia: 5620 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:10 marvel ukb frontotemporal_dementia: 3123 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb frontotemporal_dementia: 450 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb frontotemporal_dementia: 181 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb frontotemporal_dementia: 5669 rows -> 50 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb frontotemporal_dementia: 5619 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:10 marvel ukb all_cause_dementia: 4896 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb all_cause_dementia: 156 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb all_cause_dementia: 159 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb all_cause_dementia: 4212 rows -> 106 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:10 marvel ukb all_cause_dementia: 4106 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:11 marvel ukb alzheimers_dementia: 4896 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb alzheimers_dementia: 156 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb alzheimers_dementia: 207 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb alzheimers_dementia: 4164 rows -> 83 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb alzheimers_dementia: 4081 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:11 marvel ukb vascular_dementia: 4896 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb vascular_dementia: 156 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb vascular_dementia: 216 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb vascular_dementia: 4155 rows -> 80 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb vascular_dementia: 4075 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:11 marvel ukb frontotemporal_dementia: 4896 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb frontotemporal_dementia: 156 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb frontotemporal_dementia: 220 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb frontotemporal_dementia: 4151 rows -> 74 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb frontotemporal_dementia: 4077 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:11 marvel ukb all_cause_dementia: 2754 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb all_cause_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:11 marvel ukb all_cause_dementia: 105 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb all_cause_dementia: 5952 rows -> 19 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb all_cause_dementia: 5933 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:12 marvel ukb alzheimers_dementia: 2754 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb alzheimers_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb alzheimers_dementia: 107 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb alzheimers_dementia: 5950 rows -> 17 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb alzheimers_dementia: 5933 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:12 marvel ukb vascular_dementia: 2754 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb vascular_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb vascular_dementia: 115 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb vascular_dementia: 5942 rows -> 14 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb vascular_dementia: 5928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:12 marvel ukb frontotemporal_dementia: 2754 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb frontotemporal_dementia: 612 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb frontotemporal_dementia: 118 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb frontotemporal_dementia: 5939 rows -> 11 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:12 marvel ukb frontotemporal_dementia: 5928 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:13 marvel ukb all_cause_dementia: 5004 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb all_cause_dementia: 149 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb all_cause_dementia: 4270 rows -> 211 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb all_cause_dementia: 4059 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:13 marvel ukb alzheimers_dementia: 5004 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb alzheimers_dementia: 200 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb alzheimers_dementia: 4219 rows -> 186 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb alzheimers_dementia: 4033 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:13 marvel ukb vascular_dementia: 5004 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb vascular_dementia: 226 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb vascular_dementia: 4193 rows -> 165 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb vascular_dementia: 4028 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:13 marvel ukb frontotemporal_dementia: 5004 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb frontotemporal_dementia: 241 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb frontotemporal_dementia: 4178 rows -> 154 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:13 marvel ukb frontotemporal_dementia: 4024 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:14 marvel ukb all_cause_dementia: 3474 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb all_cause_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb all_cause_dementia: 199 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb all_cause_dementia: 5508 rows -> 138 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb all_cause_dementia: 5370 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:14 marvel ukb alzheimers_dementia: 3474 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb alzheimers_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb alzheimers_dementia: 241 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb alzheimers_dementia: 5466 rows -> 119 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb alzheimers_dementia: 5347 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:14 marvel ukb vascular_dementia: 3474 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb vascular_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb vascular_dementia: 265 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb vascular_dementia: 5442 rows -> 103 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb vascular_dementia: 5339 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:14 marvel ukb frontotemporal_dementia: 3474 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb frontotemporal_dementia: 242 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb frontotemporal_dementia: 273 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb frontotemporal_dementia: 5434 rows -> 95 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:14 marvel ukb frontotemporal_dementia: 5339 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:15 marvel ukb all_cause_dementia: 792 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb all_cause_dementia: 930 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb all_cause_dementia: 21 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb all_cause_dementia: 7680 rows -> 8 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb all_cause_dementia: 7672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:15 marvel ukb alzheimers_dementia: 792 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb alzheimers_dementia: 930 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb alzheimers_dementia: 23 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb alzheimers_dementia: 7678 rows -> 6 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb alzheimers_dementia: 7672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:15 marvel ukb vascular_dementia: 792 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb vascular_dementia: 930 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb vascular_dementia: 24 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb vascular_dementia: 7677 rows -> 5 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb vascular_dementia: 7672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:15 marvel ukb frontotemporal_dementia: 792 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb frontotemporal_dementia: 930 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb frontotemporal_dementia: 25 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb frontotemporal_dementia: 7676 rows -> 4 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:15 marvel ukb frontotemporal_dementia: 7672 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:16 marvel ukb all_cause_dementia: 2601 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb all_cause_dementia: 554 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb all_cause_dementia: 126 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb all_cause_dementia: 6142 rows -> 57 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb all_cause_dementia: 6085 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:16 marvel ukb alzheimers_dementia: 2601 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb alzheimers_dementia: 554 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb alzheimers_dementia: 134 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb alzheimers_dementia: 6134 rows -> 54 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb alzheimers_dementia: 6080 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:16 marvel ukb vascular_dementia: 2601 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb vascular_dementia: 554 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb vascular_dementia: 145 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb vascular_dementia: 6123 rows -> 43 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb vascular_dementia: 6080 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:16 marvel ukb frontotemporal_dementia: 2601 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb frontotemporal_dementia: 554 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb frontotemporal_dementia: 151 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb frontotemporal_dementia: 6117 rows -> 37 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:16 marvel ukb frontotemporal_dementia: 6080 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:17 marvel ukb all_cause_dementia: 3447 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb all_cause_dementia: 391 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb all_cause_dementia: 168 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb all_cause_dementia: 5417 rows -> 63 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb all_cause_dementia: 5354 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:17 marvel ukb alzheimers_dementia: 3447 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb alzheimers_dementia: 391 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb alzheimers_dementia: 205 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb alzheimers_dementia: 5380 rows -> 48 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb alzheimers_dementia: 5332 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:17 marvel ukb vascular_dementia: 3447 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb vascular_dementia: 391 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb vascular_dementia: 219 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb vascular_dementia: 5366 rows -> 43 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb vascular_dementia: 5323 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:17 marvel ukb frontotemporal_dementia: 3447 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb frontotemporal_dementia: 391 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb frontotemporal_dementia: 219 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb frontotemporal_dementia: 5366 rows -> 38 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:17 marvel ukb frontotemporal_dementia: 5328 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:18 marvel ukb all_cause_dementia: 2178 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb all_cause_dementia: 719 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb all_cause_dementia: 72 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb all_cause_dementia: 6454 rows -> 14 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb all_cause_dementia: 6440 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:18 marvel ukb alzheimers_dementia: 2178 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb alzheimers_dementia: 719 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb alzheimers_dementia: 74 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb alzheimers_dementia: 6452 rows -> 12 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb alzheimers_dementia: 6440 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:18 marvel ukb vascular_dementia: 2178 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb vascular_dementia: 719 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb vascular_dementia: 74 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb vascular_dementia: 6452 rows -> 12 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb vascular_dementia: 6440 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:18 marvel ukb frontotemporal_dementia: 2178 rows with < 5 exposed dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb frontotemporal_dementia: 719 rows with SE < 1e-06 (degenerate fit) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb frontotemporal_dementia: 75 rows with SE > 30.0 (separation) dropped (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb frontotemporal_dementia: 6451 rows -> 11 variant rows, 0 gene-burden rows (PCSK9_results.tsv.gz)
[info]  2026-10-13 17:52:18 marvel ukb frontotemporal_dementia: 6440 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 24 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 1830 rows -> 151 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:20 marvel ukb alzheimers_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb alzheimers_dementia: 31 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb alzheimers_dementia: 1823 rows -> 144 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb alzheimers_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:20 marvel ukb vascular_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb vascular_dementia: 36 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb vascular_dementia: 1818 rows -> 139 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb vascular_dementia: 1679 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:20 marvel ukb frontotemporal_dementia: 1233 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb frontotemporal_dementia: 42 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb frontotemporal_dementia: 1812 rows -> 134 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb frontotemporal_dementia: 1678 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 294 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 15 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 2562 rows -> 10 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:20 marvel ukb all_cause_dementia: 2552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 294 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 16 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 2561 rows -> 9 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 2552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 294 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 20 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 2557 rows -> 5 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 2552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 216 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 294 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 21 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 2556 rows -> 4 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 2552 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 52 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 1954 rows -> 40 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 1914 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 55 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 1951 rows -> 37 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 1914 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 56 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 1950 rows -> 36 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 1914 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 945 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 136 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 69 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 1937 rows -> 29 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 1908 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 39 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 58 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 1712 rows -> 83 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb all_cause_dementia: 1629 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 39 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 63 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 1707 rows -> 78 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb alzheimers_dementia: 1629 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 39 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 65 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 1705 rows -> 76 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:21 marvel ukb vascular_dementia: 1629 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:21 marvel ukb frontotemporal_dementia: 1278 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 39 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 69 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 1701 rows -> 72 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 1629 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 203 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 48 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 2188 rows -> 20 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 2168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 203 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 54 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 2182 rows -> 14 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 2168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 203 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 56 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 2180 rows -> 12 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 2168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 648 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 203 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 57 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 2179 rows -> 11 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 2168 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 45 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 61 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 2009 rows -> 105 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 1904 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 45 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 67 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 2003 rows -> 99 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 1904 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 45 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 70 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 2000 rows -> 96 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb vascular_dementia: 1904 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 972 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 45 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 80 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 1990 rows -> 90 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb frontotemporal_dementia: 1900 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 302 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 2600 rows -> 8 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb all_cause_dementia: 2592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 302 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 14 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 2600 rows -> 8 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:22 marvel ukb alzheimers_dementia: 2592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 302 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 18 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 2596 rows -> 4 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 2592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 171 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 302 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 18 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 2596 rows -> 4 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 2592 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 59 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 2134 rows -> 31 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 2103 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 61 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 2132 rows -> 29 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 2103 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 63 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 2130 rows -> 27 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 2103 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 729 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 165 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 74 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 2119 rows -> 22 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 2097 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 87 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 75 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 1899 rows -> 50 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 1849 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 87 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 78 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 1896 rows -> 47 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb alzheimers_dementia: 1849 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 87 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 79 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 1895 rows -> 46 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb vascular_dementia: 1849 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 1026 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 87 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 81 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 1893 rows -> 44 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb frontotemporal_dementia: 1849 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 39 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 2294 rows -> 14 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:23 marvel ukb all_cause_dementia: 2280 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:24 marvel ukb alzheimers_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb alzheimers_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb alzheimers_dementia: 44 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb alzheimers_dementia: 2289 rows -> 9 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb alzheimers_dementia: 2280 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:24 marvel ukb vascular_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb vascular_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb vascular_dementia: 45 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb vascular_dementia: 2288 rows -> 8 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb vascular_dementia: 2280 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[info]  2026-10-13 17:52:24 marvel ukb frontotemporal_dementia: 522 rows with < 5 exposed dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb frontotemporal_dementia: 232 rows with SE < 1e-06 (degenerate fit) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb frontotemporal_dementia: 44 rows with SE > 30.0 (separation) dropped (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb frontotemporal_dementia: 2289 rows -> 9 variant rows, 0 gene-burden rows (PPARA_results.tsv.gz)
[info]  2026-10-13 17:52:24 marvel ukb frontotemporal_dementia: 2280 exposures (intercept, covariates) neither a variant in a gene region nor a gene (mask) in gene_list.txt, dropped
[stage] 2026-10-13 17:52:24 fetch_curated
[info]  2026-10-13 17:53:19 MONDO_0005252 (exact): 892 fetched; in region: CETP=2 PCSK9=1
[info]  2026-10-13 17:53:21 MONDO_0005099 (exact): 15 fetched; in region: none
[info]  2026-10-13 17:53:25 MONDO_0013792 (exact): 42 fetched; in region: none
[info]  2026-10-13 17:53:29 MONDO_0005394 (exact): 41 fetched; in region: none
[info]  2026-10-13 17:53:50 MONDO_0005098 (exact): 327 fetched; in region: CETP=1
[info]  2026-10-13 17:54:11 EFO_0003913 (exact): 320 fetched; in region: PCSK9=2 APOB=6
[info]  2026-10-13 17:54:14 MONDO_0004781 (exact): 17 fetched; in region: none
[info]  2026-10-13 17:54:20 MONDO_0005267 (exact): 55 fetched; in region: none
[info]  2026-10-13 17:58:54 MONDO_0005010 (exact): 3913 fetched; in region: CETP=9 HMGCR=2 PCSK9=21 APOB=3
[info]  2026-10-13 17:59:01 EFO_0004269 (exact): 102 fetched; in region: none
[info]  2026-10-13 17:59:04 EFO_0009492 (exact): 8 fetched; in region: none
[info]  2026-10-13 17:59:06 EFO_0009493 (exact): 3 fetched; in region: none
[info]  2026-10-13 18:06:36 MONDO_0004975 (with child traits): 7069 fetched; in region: APOB=1
[info]  2026-10-13 18:06:45 MONDO_0004648 (with child traits): 120 fetched; in region: none
[info]  2026-10-13 18:06:51 EFO_0006799 (with child traits): 40 fetched; in region: none
[info]  2026-10-13 18:06:54 EFO_0011057 (with child traits): 26 fetched; in region: none
[info]  2026-10-13 18:06:57 EFO ids with 0 curated associations: 4
[stage] 2026-10-13 18:06:57 gene_burden
[info]  2026-10-13 18:06:57 Open Targets disease ids: 29 (from 20 outcome ids)
[info]  2026-10-13 18:06:58 curated MAF: numeric=58 not_reported=28
[info]  2026-10-13 18:06:58 curated: 54 rows dropped from studies excluded for cohort overlap
[info]  2026-10-13 18:06:58 gene-burden rows: none (8 genes with 0)
[info]  2026-10-13 18:07:00 ancestry: 0 rows of studies not in the discovery log labelled NR
[info]  2026-10-13 18:07:00 ancestry: curated EAS=21
[info]  2026-10-13 18:07:00 ancestry: curated EUR=26
[info]  2026-10-13 18:07:00 ancestry: curated MULTI=21
[info]  2026-10-13 18:07:00 ancestry: curated NR=18
[info]  2026-10-13 18:07:00 ancestry: summary-stats AFR=159854
[info]  2026-10-13 18:07:00 ancestry: summary-stats AMR=73617
[info]  2026-10-13 18:07:00 ancestry: summary-stats CSA=43677
[info]  2026-10-13 18:07:00 ancestry: summary-stats EAS=45135
[info]  2026-10-13 18:07:00 ancestry: summary-stats EUR=148736
[info]  2026-10-13 18:07:00 ancestry: summary-stats MULTI=143102
[info]  2026-10-13 18:07:00 ancestry: summary-stats NR=5898
[stage] 2026-10-13 18:07:00 effect_scale
[info]  2026-10-13 18:07:02 wrote 155 studies to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/study_effect_scale.tsv.gz
[info]  2026-10-13 18:07:02 study effect scale: linear=2, log_or=97, unknown=56
[stage] 2026-10-13 18:07:02 normalise
[info]  2026-10-13 18:07:03 normalisation: summary-stats rows unchanged=576755 no_sequence=40564 ref_mismatch=2699 normalised=1
[info]  2026-10-13 18:07:03 normalisation: curated rows effect_only=86
[stage] 2026-10-13 18:07:03 ensembl_check
[info]  2026-10-13 18:07:03 CETP: 16262 Ensembl variants in 16:56951980-56993663 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:03 HMGCR: 13932 Ensembl variants in 5:75332606-75370339 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:03 NPC1L1: 17649 Ensembl variants in 7:44503450-44551259 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:04 PCSK9: 16676 Ensembl variants in 1:55029838-55073581 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:04 ANGPTL3: 9469 Ensembl variants in 1:62587567-62614814 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:04 PPARA: 21414 Ensembl variants in 22:46188384-46245377 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:04 APOA1: 11180 Ensembl variants in 11:116824677-116852065 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:04 APOB: 26572 Ensembl variants in 2:20991305-21054075 (0 windows fetched, rest cached)
[info]  2026-10-13 18:07:06 Ensembl check: 22350 unique variant rows checked, 0 rsids fetched via the variation endpoint
[info]  2026-10-13 18:07:07 summary-stats rows: alleles match=469415 flipped=135502 not_found=8387 mismatch=6247 strand_flip=468; rsid same=521285 no_source_rsid=46000 rsid_only=41315 different=3032
[info]  2026-10-13 18:07:07 curated rows: alleles match=33 flipped=28 effect_unknown=25; rsid same=86
[info]  2026-10-13 18:07:08 duplicate variants flagged: 766 rows
[stage] 2026-10-13 18:07:08 write
[info]  2026-10-13 18:08:02 wrote 620105 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz

```

## [30] merge_associations_job
- first run: 2026-09-30 11:30:47
- last run: 2026-10-13 18:08:07
- commit: `8781963`

Output:
```text
[info]  2026-10-13 17:50:58 using root directory: /home/rmgpmva/projects/lipid_adem

```

## [40] clinvar_filter (`mamba run --no-capture-output -n clinvar-build clinvar-filter /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_vcv.db --rcv-db /Users/marionvanvugt/Documents/work.nosync/data/clinvar/clinvar_rcv.db -g gene CETP HMGCR NPC1L1 PCSK9 ANGPTL3 PPARA APOA1 APOB APOE -o /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv -vvv`)
- first run: 2026-10-06 17:09:48
- last run: 2026-10-06 17:09:48
- commit: `7e96ca6` (dirty)

Output:
```text
2026-10-06 17:09:48,842 - INFO - Wrote 313818 rows to /Users/marionvanvugt/Documents/work.nosync/projects/lipid_adem/data/raw/clinvar_variants.tsv
```

## [40] match_variants (`/home/rmgpmva/projects/lipid_adem/src/match_variants.py --region-rare --max-maf 0.01`)
- first run: 2026-10-01 09:59:12
- last run: 2026-10-16 12:22:34
- commit: `a763a00`

Output:
```text
[stage] 2026-10-16 12:21:10 load_gwas
[info]  2026-10-16 12:21:36 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/merged_associations.tsv.gz: 620105 rows, 620105 variant-level (summary-stats, curated)
[info]  2026-10-16 12:21:38 curated: 25 rows without chrom/pos or effect allele, cannot be matched
[info]  2026-10-16 12:21:41 region-rare: 620080 rows, 0 outside their gene region, 271216 with MAF >= 0.01, 9645 without MAF (not marvel) dropped, 26992 marvel rows without MAF kept; 339219 rows kept
[stage] 2026-10-16 12:21:41 build_region_list
[info]  2026-10-16 12:21:42 region-rare list: 10047 sites (4253 duplicates after ref/alt ordering removed), 1 without a known reference allele (alleles in alphabetical order)
[info]  2026-10-16 12:21:42 region-rare list: ANGPTL3 689 sites
[info]  2026-10-16 12:21:42 region-rare list: APOA1 607 sites
[info]  2026-10-16 12:21:42 region-rare list: APOB 1640 sites
[info]  2026-10-16 12:21:42 region-rare list: APOE 614 sites
[info]  2026-10-16 12:21:42 region-rare list: CETP 1347 sites
[info]  2026-10-16 12:21:42 region-rare list: HMGCR 1091 sites
[info]  2026-10-16 12:21:42 region-rare list: NPC1L1 1526 sites
[info]  2026-10-16 12:21:42 region-rare list: PCSK9 1267 sites
[info]  2026-10-16 12:21:42 region-rare list: PPARA 1266 sites
[stage] 2026-10-16 12:21:42 match
[info]  2026-10-16 12:21:43 ANGPTL3 region_rare: 689 variants, 689 matched, GWAS rows: summary-stats=20130
[info]  2026-10-16 12:21:43 APOA1 region_rare: 607 variants, 607 matched, GWAS rows: summary-stats=23493
[info]  2026-10-16 12:21:43 APOB region_rare: 1640 variants, 1640 matched, GWAS rows: summary-stats=63380
[info]  2026-10-16 12:21:43 APOE region_rare: 614 variants, 614 matched, GWAS rows: summary-stats=20375
[info]  2026-10-16 12:21:43 CETP region_rare: 1347 variants, 1347 matched, GWAS rows: summary-stats=51273
[info]  2026-10-16 12:21:43 HMGCR region_rare: 1091 variants, 1091 matched, GWAS rows: summary-stats=34246
[info]  2026-10-16 12:21:44 NPC1L1 region_rare: 1526 variants, 1526 matched, GWAS rows: summary-stats=45092
[info]  2026-10-16 12:21:44 PCSK9 region_rare: 1267 variants, 1267 matched, GWAS rows: summary-stats=46108
[info]  2026-10-16 12:21:44 PPARA region_rare: 1266 variants, 1266 matched, GWAS rows: summary-stats=43260
[warn]  2026-10-16 12:21:44 a1 vs Ensembl ref: 319516 matched SNV rows checked, 108 where a1 is not the Ensembl ref (e.g. 1:62598799:AAAA:AAA, 1:62601803:AGGT:AGGTAGGT, 1:62604235:GG:G)
[stage] 2026-10-16 12:21:45 write
[info]  2026-10-16 12:22:33 wrote 347357 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz

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
- last run: 2026-10-13 17:39:08
- commit: `8781963`

Output:
```text
[info]  2026-10-12 12:53:10 task 1: rows 1-1
[info]  2026-10-13 17:39:07 PCSK9: results in /myriadfs/home/rmgpmva/projects/lipid_adem/results/PCSK9

```

## [50] meta_analysis (`/home/rmgpmva/projects/lipid_adem/src/meta_analysis.py --ancestry MULTI --studies marvel_ukb_MULTI_all_cause_dementia marvel_ukb_MULTI_all_cause_dementia_e44 marvel_ukb_MULTI_all_cause_dementia_e43 marvel_ukb_MULTI_all_cause_dementia_e33 marvel_ukb_MULTI_all_cause_dementia_e22_e32 marvel_ukb_MULTI_alzheimers_dementia marvel_ukb_MULTI_alzheimers_dementia_e44 marvel_ukb_MULTI_alzheimers_dementia_e43 marvel_ukb_MULTI_alzheimers_dementia_e33 marvel_ukb_MULTI_alzheimers_dementia_e22_e32 marvel_ukb_MULTI_vascular_dementia marvel_ukb_MULTI_vascular_dementia_e44 marvel_ukb_MULTI_vascular_dementia_e43 marvel_ukb_MULTI_vascular_dementia_e33 marvel_ukb_MULTI_vascular_dementia_e22_e32 marvel_ukb_MULTI_frontotemporal_dementia marvel_ukb_MULTI_frontotemporal_dementia_e44 marvel_ukb_MULTI_frontotemporal_dementia_e43 marvel_ukb_MULTI_frontotemporal_dementia_e33 marvel_ukb_MULTI_frontotemporal_dementia_e22_e32 --region-rare --stratified --label ukb_dementia_region_rare`)
- first run: 2026-10-01 10:26:24
- last run: 2026-10-16 12:36:28
- commit: `a763a00`

Δ vs previous run (was `a763a00`):
stage `load_matched`:
```diff
@@ -1,5 +1,5 @@
 [info]  2026-10-16 12:34:04 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz: 347357 rows, 10047 variants
 [info]  2026-10-16 12:34:04 20375 rows of excluded gene(s) APOE dropped
 [info]  2026-10-16 12:34:06 326982 of 326982 rows kept (MULTI pools every ancestry) (all: AFR=87047, AMR=42782, CSA=36051, EAS=10748, EUR=81062, MULTI=69061, NR=231)
-[info]  2026-10-16 12:30:21 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32, F5_DEMENTIA_INCLAVO, G6_ALZHEIMER, F5_VASCDEM, FTD: 21335 of 326982 rows kept
-[info]  2026-10-16 12:30:22 MULTI: 21335 rows pooled across ancestries (EUR=5704, MULTI=15631), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
+[info]  2026-10-16 12:34:07 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32: 15631 of 326982 rows kept
+[info]  2026-10-16 12:34:07 MULTI: 15631 rows pooled across ancestries (MULTI=15631), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
```
stage `prepare_effects`:
```diff
@@ -1 +1 @@
-[info]  2026-10-16 12:30:22 21335 usable rows, 0 with SE derived from p
+[info]  2026-10-16 12:34:07 15631 usable rows, 0 with SE derived from p
```
stage `orient`:
```diff
@@ -1 +1 @@
-[info]  2026-10-16 12:30:22 3217 variants oriented as a2
+[info]  2026-10-16 12:34:07 1821 variants oriented as a2
```
stage `dedupe`:
```diff
@@ -1,4 +1,4 @@
-[info]  2026-10-16 12:30:22 8 duplicate rows removed
+[info]  2026-10-16 12:34:07 0 duplicate rows removed
 [info]  2026-10-16 12:34:07 0 estimates removed as copies of another study
 [info]  2026-10-16 12:35:05 0 duplicate rows removed
 [info]  2026-10-16 12:35:05 0 estimates removed as copies of another study
```
stage `meta_analyse`:
```diff
@@ -1,4 +1,4 @@
-[info]  2026-10-16 12:31:16 12477 groups, 96 pooling more than one estimate
-[info]  2026-10-16 12:32:08 12573 groups, 0 pooling more than one estimate
+[info]  2026-10-16 12:34:36 6877 groups, 0 pooling more than one estimate
+[info]  2026-10-16 12:35:05 6877 groups, 0 pooling more than one estimate
 [info]  2026-10-16 12:35:39 8754 groups, 0 pooling more than one estimate
 [info]  2026-10-16 12:36:15 8754 groups, 0 pooling more than one estimate
```
stage `gene_burden`:
```diff
@@ -1,2 +1,2 @@
-[info]  2026-10-16 12:32:09 gene burden: 32 pooled and 56 per-study rows
+[info]  2026-10-16 12:35:05 gene burden: 24 pooled and 24 per-study rows
 [info]  2026-10-16 12:36:15 gene burden: 96 pooled and 96 per-study rows
```
stage `write`:
```diff
@@ -1,4 +1,4 @@
-[info]  2026-10-16 12:32:21 wrote 25050 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_armb_dementia_region_rare.tsv.gz
-[info]  2026-10-16 12:32:31 wrote 88 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_armb_dementia_region_rare.tsv.gz
-[info]  2026-10-16 12:33:44 wrote 17508 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_armb_dementia_region_rare_apoe_strata.tsv.gz
-[info]  2026-10-16 12:33:44 wrote 192 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_armb_dementia_region_rare_apoe_strata.tsv.gz
+[info]  2026-10-16 12:35:05 wrote 13754 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare.tsv.gz
+[info]  2026-10-16 12:35:05 wrote 48 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare.tsv.gz
+[info]  2026-10-16 12:36:19 wrote 17508 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare_apoe_strata.tsv.gz
+[info]  2026-10-16 12:36:23 wrote 192 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare_apoe_strata.tsv.gz
```

Output:
```text
[info]  2026-10-16 12:33:50 ancestry MULTI, pooled by variant_site, outcome, ancestry_group
[stage] 2026-10-16 12:33:50 load_matched
[info]  2026-10-16 12:34:04 /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/matched_region_variants.tsv.gz: 347357 rows, 10047 variants
[info]  2026-10-16 12:34:04 20375 rows of excluded gene(s) APOE dropped
[info]  2026-10-16 12:34:06 326982 of 326982 rows kept (MULTI pools every ancestry) (all: AFR=87047, AMR=42782, CSA=36051, EAS=10748, EUR=81062, MULTI=69061, NR=231)
[info]  2026-10-16 12:34:07 study_accession in marvel_ukb_MULTI_all_cause_dementia, marvel_ukb_MULTI_all_cause_dementia_e44, marvel_ukb_MULTI_all_cause_dementia_e43, marvel_ukb_MULTI_all_cause_dementia_e33, marvel_ukb_MULTI_all_cause_dementia_e22_e32, marvel_ukb_MULTI_alzheimers_dementia, marvel_ukb_MULTI_alzheimers_dementia_e44, marvel_ukb_MULTI_alzheimers_dementia_e43, marvel_ukb_MULTI_alzheimers_dementia_e33, marvel_ukb_MULTI_alzheimers_dementia_e22_e32, marvel_ukb_MULTI_vascular_dementia, marvel_ukb_MULTI_vascular_dementia_e44, marvel_ukb_MULTI_vascular_dementia_e43, marvel_ukb_MULTI_vascular_dementia_e33, marvel_ukb_MULTI_vascular_dementia_e22_e32, marvel_ukb_MULTI_frontotemporal_dementia, marvel_ukb_MULTI_frontotemporal_dementia_e44, marvel_ukb_MULTI_frontotemporal_dementia_e43, marvel_ukb_MULTI_frontotemporal_dementia_e33, marvel_ukb_MULTI_frontotemporal_dementia_e22_e32: 15631 of 326982 rows kept
[info]  2026-10-16 12:34:07 MULTI: 15631 rows pooled across ancestries (MULTI=15631), relabelled MULTI; a study reported both per ancestry and combined is counted twice unless --studies excludes one
[stage] 2026-10-16 12:34:07 effect_scale
[stage] 2026-10-16 12:34:07 prepare_effects
[info]  2026-10-16 12:34:07 15631 usable rows, 0 with SE derived from p
[stage] 2026-10-16 12:34:07 resolve_ambiguous
[stage] 2026-10-16 12:34:07 orient
[info]  2026-10-16 12:34:07 1821 variants oriented as a2
[stage] 2026-10-16 12:34:07 apoe_strata
[info]  2026-10-16 12:34:07 /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/apoe_strata.tsv: 44 studies with an APOE stratum entry
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_all_cause_dementia, stratum all: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_all_cause_dementia, stratum e22_e32: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_all_cause_dementia, stratum e33: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_all_cause_dementia, stratum e43: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_all_cause_dementia, stratum e44: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_alzheimers_dementia, stratum all: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e22_e32: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e33: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e43: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_alzheimers_dementia, stratum e44: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum all: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e22_e32: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e33: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e43: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_frontotemporal_dementia, stratum e44: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_vascular_dementia, stratum all: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_vascular_dementia, stratum e22_e32: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_vascular_dementia, stratum e33: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_vascular_dementia, stratum e43: 1 studies
[info]  2026-10-16 12:34:07 study group marvel_ukb_MULTI_vascular_dementia, stratum e44: 1 studies
[stage] 2026-10-16 12:34:07 pooled_run
[info]  2026-10-16 12:34:07 pooled run, study group marvel_ukb_MULTI_all_cause_dementia: unstratified run, strata left out
[info]  2026-10-16 12:34:07 pooled run, study group marvel_ukb_MULTI_alzheimers_dementia: unstratified run, strata left out
[info]  2026-10-16 12:34:07 pooled run, study group marvel_ukb_MULTI_frontotemporal_dementia: unstratified run, strata left out
[info]  2026-10-16 12:34:07 pooled run, study group marvel_ukb_MULTI_vascular_dementia: unstratified run, strata left out
[stage] 2026-10-16 12:34:07 dedupe
[info]  2026-10-16 12:34:07 0 duplicate rows removed
[info]  2026-10-16 12:34:07 0 estimates removed as copies of another study
[stage] 2026-10-16 12:34:07 meta_analyse
[info]  2026-10-16 12:34:36 6877 groups, 0 pooling more than one estimate
[info]  2026-10-16 12:35:05 6877 groups, 0 pooling more than one estimate
[stage] 2026-10-16 12:35:05 gene_burden
[info]  2026-10-16 12:35:05 gene burden: 24 pooled and 24 per-study rows
[stage] 2026-10-16 12:35:05 write
[info]  2026-10-16 12:35:05 wrote 13754 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare.tsv.gz
[info]  2026-10-16 12:35:05 wrote 48 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare.tsv.gz
[stage] 2026-10-16 12:35:05 apoe_strata_run
[info]  2026-10-16 12:35:05 8754 rows from APOE strata: pooled per stratum
[stage] 2026-10-16 12:35:05 dedupe
[info]  2026-10-16 12:35:05 0 duplicate rows removed
[info]  2026-10-16 12:35:05 0 estimates removed as copies of another study
[stage] 2026-10-16 12:35:05 meta_analyse
[info]  2026-10-16 12:35:39 8754 groups, 0 pooling more than one estimate
[info]  2026-10-16 12:36:15 8754 groups, 0 pooling more than one estimate
[stage] 2026-10-16 12:36:15 gene_burden
[info]  2026-10-16 12:36:15 gene burden: 96 pooled and 96 per-study rows
[stage] 2026-10-16 12:36:15 write
[info]  2026-10-16 12:36:19 wrote 17508 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/meta_MULTI_ukb_dementia_region_rare_apoe_strata.tsv.gz
[info]  2026-10-16 12:36:23 wrote 192 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/burden_MULTI_ukb_dementia_region_rare_apoe_strata.tsv.gz

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
- last run: 2026-10-21 13:50:41
- commit: `e9443d3` (dirty)

Output:
```text
[info]  2026-10-21 13:49:03 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/ptv_variants.tsv.gz: 527 PTVs
[info]  2026-10-21 13:49:03 /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/plp_variants.tsv: 1900 rows; /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: 86 rows
[info]  2026-10-21 13:49:03 0 P/LP rows with ref = alt dropped
[warn]  2026-10-21 13:49:03 APOE condition 'Alzheimer disease 3, protection against, due to APOE3-Christchurch' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 APOA1 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 ANGPTL3 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 PPARA condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 PCSK9 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 HMGCR condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 NPC1L1 condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 CETP condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 APOB condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[warn]  2026-10-21 13:49:03 APOE condition 'nan' not in /gpfs/home6/mvanvugt/projects/lipid_adem/data/raw/clinvar_condition_direction.tsv: counted as unknown
[info]  2026-10-21 13:49:03 262 truncating P/LP variants set to lowering, 213 of them against their conditions
[info]  2026-10-21 13:49:03 ANGPTL3 ClinVar P/LP: 12 variants lowering
[info]  2026-10-21 13:49:03 ANGPTL3 ClinVar P/LP: 2 variants unknown
[info]  2026-10-21 13:49:03 APOA1 ClinVar P/LP: 11 variants altered
[info]  2026-10-21 13:49:03 APOA1 ClinVar P/LP: 2 variants conflicting
[info]  2026-10-21 13:49:03 APOA1 ClinVar P/LP: 16 variants lowering
[info]  2026-10-21 13:49:03 APOA1 ClinVar P/LP: 6 variants unknown
[info]  2026-10-21 13:49:03 APOB ClinVar P/LP: 5 variants altered
[info]  2026-10-21 13:49:03 APOB ClinVar P/LP: 6 variants conflicting
[info]  2026-10-21 13:49:03 APOB ClinVar P/LP: 224 variants lowering
[info]  2026-10-21 13:49:03 APOB ClinVar P/LP: 3 variants unknown
[info]  2026-10-21 13:49:03 APOE ClinVar P/LP: 12 variants altered
[info]  2026-10-21 13:49:03 APOE ClinVar P/LP: 3 variants lowering
[info]  2026-10-21 13:49:03 APOE ClinVar P/LP: 6 variants unknown
[info]  2026-10-21 13:49:03 CETP ClinVar P/LP: 10 variants lowering
[info]  2026-10-21 13:49:03 CETP ClinVar P/LP: 2 variants unknown
[info]  2026-10-21 13:49:03 HMGCR ClinVar P/LP: 6 variants lowering
[info]  2026-10-21 13:49:03 HMGCR ClinVar P/LP: 3 variants unknown
[info]  2026-10-21 13:49:03 NPC1L1 ClinVar P/LP: 2 variants unknown
[info]  2026-10-21 13:49:03 PCSK9 ClinVar P/LP: 2 variants lowering
[info]  2026-10-21 13:49:03 PCSK9 ClinVar P/LP: 16 variants raising
[info]  2026-10-21 13:49:03 PCSK9 ClinVar P/LP: 2 variants unknown
[info]  2026-10-21 13:49:03 PPARA ClinVar P/LP: 2 variants unknown
[warn]  2026-10-21 13:49:03 ANGPTL3 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 APOA1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 APOB ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 APOE ClinVar: 1 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 CETP ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 HMGCR ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 NPC1L1 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 PCSK9 ClinVar: 2 rows without GRCh38 chr/pos/alleles
[warn]  2026-10-21 13:49:03 PPARA ClinVar: 2 rows without GRCh38 chr/pos/alleles
[info]  2026-10-21 13:50:41 normalisation ClinVar: no_sequence=20
[info]  2026-10-21 13:50:41 normalisation ClinVar: unchanged=316
[info]  2026-10-21 13:50:41 normalisation PTV: normalised=18
[info]  2026-10-21 13:50:41 normalisation PTV: unchanged=509
[info]  2026-10-21 13:50:41 57 sites are both PTV and ClinVar
[info]  2026-10-21 13:50:41 ANGPTL3 ClinVar: 12 variants
[info]  2026-10-21 13:50:41 ANGPTL3 PTV: 56 variants
[info]  2026-10-21 13:50:41 APOA1 ClinVar: 33 variants
[info]  2026-10-21 13:50:41 APOA1 PTV: 15 variants
[info]  2026-10-21 13:50:41 APOB ClinVar: 236 variants
[info]  2026-10-21 13:50:41 APOB PTV: 172 variants
[info]  2026-10-21 13:50:41 APOE ClinVar: 20 variants
[info]  2026-10-21 13:50:41 CETP ClinVar: 10 variants
[info]  2026-10-21 13:50:41 CETP PTV: 58 variants
[info]  2026-10-21 13:50:41 HMGCR ClinVar: 7 variants
[info]  2026-10-21 13:50:41 HMGCR PTV: 39 variants
[info]  2026-10-21 13:50:41 NPC1L1 PTV: 96 variants
[info]  2026-10-21 13:50:41 PCSK9 ClinVar: 18 variants
[info]  2026-10-21 13:50:41 PCSK9 PTV: 68 variants
[info]  2026-10-21 13:50:41 PPARA PTV: 23 variants
[info]  2026-10-21 13:50:41 Wrote 863 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/processed/lipid_variants.tsv
[info]  2026-10-21 13:50:41 marvel lists: 806 sites, 17 with an extra original-form row
[info]  2026-10-21 13:50:41 Wrote 64 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/ANGPTL3_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 46 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOA1_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 373 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOB_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 20 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/APOE_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 66 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/CETP_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 45 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/HMGCR_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 99 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/NPC1L1_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 86 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PCSK9_variants.tsv
[info]  2026-10-21 13:50:41 Wrote 24 rows to /gpfs/home6/mvanvugt/projects/lipid_adem/data/temp/PPARA_variants.tsv

```
``
