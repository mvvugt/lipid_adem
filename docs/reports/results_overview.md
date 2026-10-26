# Results overview: lipid-lowering drug targets and dementia

State on 2026-10-26.
- Source: the pipeline batch of 2026-10-26, 18:45–19:17, copied from Myriad.
- These files are now archived under `results/archive/20261026/` (see its `README.md`).

## 1. Question and design

- **Question:** does genetically proxied lipid-lowering change dementia risk?
  - The proxy is rare variants that lower the function of a drug-target gene.
- **Positive controls:** lipids (does the proxy work?) and ASCVD (does it reach a clinical outcome?).
- **Gene to drug:**

  | Gene | Drug | Note |
  |---|---|---|
  | HMGCR | statins | |
  | PCSK9 | PCSK9 inhibitors | |
  | NPC1L1 | ezetimibe | |
  | CETP | CETP inhibitors | |
  | ANGPTL3 | evinacumab | |
  | PPARA | fibrates | fibrates are **agonists**, so PPARA loss of function proxies the *opposite* of the drug |

- **Variant sets:**
  - PTV;
  - AlphaMissense (AM) P/LP;
  - ClinVar P/LP that do not raise function;
  - their combinations;
  - GoF sites (CETP, PCSK9), oriented to lower function.
- **Main source:** the UKB carrier burden (0/1 carrier mask, marvel). All UKB samples are used, with no MAF cap.
- **Other sources:**
  - FinnGen and Thomassen (Alzheimer's) per-variant summary statistics, pooled with the burden by IVW in the `annotated_eur` runs.
  - These become sensitivity analyses.
  - All of Us may later join as a second burden cohort.

## 2. Positive controls (UKB, EUR)

Lipids are betas (mmol/L or g/L); ASCVD is an OR (95% CI).

| Gene | Carriers | Main lipid effect | ASCVD | Verdict |
|---|---|---|---|---|
| PCSK9 | 937 | LDL −0.81, ApoB −0.21 | **0.67 (0.52; 0.88)** | Strong pass |
| CETP | 473 | HDL +0.39, LDL −0.14 | 0.76 (0.55; 1.04); PTV+AM 0.82 (0.66; 1.01) | Lipids pass; ASCVD borderline |
| NPC1L1 | 669 | LDL −0.16 | 0.82 (0.64; 1.06); PTV+AM 0.88 (0.77; 1.00) | Lipids pass; ASCVD borderline |
| ANGPTL3 | 974 | TG −0.53, LDL −0.33 | 0.93 (0.76; 1.14) | Lipids pass; ASCVD weak |
| HMGCR | 85 | LDL −0.19 (p = 0.08) | 1.51 (0.82; 2.79) | **Fails**: weak instrument |
| PPARA | 73 | TG +0.25 (p = 0.05) | 2.06 (1.15; 3.67) | Opposite of a fibrate, as expected; few carriers |

- **The lipid effects match each drug**, so the variant sets capture gene function.
- **The dementia outcomes are valid:** APOE gives all-cause dementia OR 2.03 (p = 2e-86).

## 3. Dementia in UKB (EUR)

- Format: OR (95% CI), then `~n`, a rough count of **cases among carriers** (≈ 1/SE²).
- No estimate has p < 0.05, except HMGCR AM vascular dementia: 3.09 (1.15; 8.30), ~4 cases.

| Gene | Set | All-cause | Alzheimer's | Vascular |
|---|---|---|---|---|
| PCSK9 | PTV | 1.18 (0.73; 1.91) ~16 | 1.05 (0.50; 2.22) ~7 | 0.33 ~1 |
| PCSK9 | PTV+AM | 1.06 (0.73; 1.54) ~27 | 0.99 (0.56; 1.75) ~12 | 0.53 ~3 |
| CETP | PTV | 1.02 (0.53; 1.98) ~9 | 0.50 (0.12; 1.99) ~2 | 0.53 ~1 |
| CETP | AM | 0.46 (0.19; 1.12) ~5 | 0.21 (0.03; 1.46) ~1 | 0.44 ~1 |
| CETP | PTV+AM | 0.73 (0.43; 1.24) ~14 | **0.34 (0.11; 1.07) ~3** | 0.49 ~2 |
| NPC1L1 | PTV+AM | 1.05 (0.79; 1.40) ~48 | 0.94 (0.60; 1.46) ~20 | 0.80 ~8 |
| ANGPTL3 | PTV+AM | 0.74 (0.50; 1.11) ~24 | 0.89 (0.52; 1.54) ~13 | 1.01 ~7 |
| HMGCR | PTV+AM | 1.60 (0.90; 2.85) ~12 | 1.15 (0.43; 3.09) ~4 | 2.49 (0.93; 6.70) ~4 |
| PPARA | PTV+AM | 1.40 (0.98; 1.99) ~31 | 1.24 (0.72; 2.15) ~13 | 1.01 ~5 |

### Interpretation

- **Only CETP shows a pattern:** every estimate is below 1, which fits CETP inhibition being protective.
  - It rests on about 1–3 Alzheimer's cases among carriers.
  - About 9 would be expected at OR = 1: 948 carriers × ~1% Alzheimer's prevalence.
  - One or two extra cases would remove the signal.
  - It matches the earlier cetp_marvel run. The old AM + HC PTV Alzheimer's OR of 0.14 came from the old phenotype file. On the current file, AM + any PTV gives 0.34.
- **PCSK9, the strongest instrument:** ORs of 1.0–1.2, with no hint of protection.
- **The intervals are wide.** For all-cause dementia, the effects that can be excluded are:

  | Gene | Can exclude OR below | Can exclude OR above |
  |---|---|---|
  | NPC1L1 (best case) | ~0.79 | ~1.40 |
  | PCSK9 | ~0.73 | ~1.54 |

  - So effects of OR ≈ 0.8 can't be excluded.

### Why "the sets are not independent" matters

- PTV+AM is the union of the PTV and AM carriers. Its estimate is roughly a mix of the two, not a third, separate test.
- **Interpretation:** "CETP < 1 in PTV, AM and PTV+AM" is **two** pieces of evidence (PTV ~2 cases, AM ~1), not three replications.
- **Multiple testing:** the tests across sets are correlated, so a Bonferroni over all sets is too strict. Count about 2 independent sets per gene (PTV, AM), with PTV+AM as the primary combination.
- The same holds for the duplicate sets:
  - `lof` (PTV + ClinVar) = `ptv`, and `ptv_clinvar_am` = `ptv_am`, for every gene.
  - `am_clinvar` ≈ `am`.
  - ClinVar adds no carriers (follow-up in TODO.md).

## 4. Why FinnGen points the other way

FinnGen is **not measuring the same exposure**:

| | UKB | FinnGen |
|---|---|---|
| What enters | Carrier burden, CETP PTV+AM: 92 sites, 948 carriers | Per-variant summary stats: only **1–2 Finnish-enriched variants** survive their frequency filter |
| CETP variants | All PTV + AM P/LP | `16:56962097 TGTAA>T` splice donor (LOFTEE HC, `NON_CAN_SPLICE`, AF 0.09%); `16:56973332 G>T` missense (AM 0.74, ClinVar conflicting, AF 0.02%) |
| Alzheimer's precision | SE 0.58 (~3 carrier cases) | SE 0.19 for the splice variant: **~9× the weight** |
| Lipid check | Burden raises HDL | None: their function is unverified |

The same two variants, per variant:

| Variant | Outcome | FinnGen | UKB |
|---|---|---|---|
| Splice | All-cause | 0.97 | 0.95 |
| Splice | Alzheimer's | 1.11 | 1.10 |
| Missense | All-cause | **2.50** | 0.55 |
| Missense | Alzheimer's | 1.71 | 0.22 |

- **The splice variant agrees, and is null in both.**
- **The missense variant disagrees** (all-cause heterogeneity p ≈ 0.05).
  - In FinnGen it also has CHD OR 1.51 (p = 0.07). That is the opposite of CETP loss of function, so it may not be loss of function at all.
- **The UKB signal comes from carriers that are absent from FinnGen.** So this is a contrast between *different variants*, not a failed replication.
- Pooling pulls the estimate to the null splice variant: CETP PTV+AM Alzheimer's pooled = 1.04 (0.74; 1.47).
- **The same pattern appears elsewhere:**
  - PPARA all-cause: FinnGen 0.80 vs UKB 1.40.
  - NPC1L1 vascular: FinnGen 1.72 vs UKB 0.80.
- **Other differences:**
  - Outcome definitions: FinnGen registries, including primary care (`F5_DEMENTIA_INCLAVO`), vs UKB `_combined`.
  - Age: FinnGen has lifetime follow-up; UKB recruited at 40–69.
  - Per-allele SAIGE estimates are less stable for ultra-rare variants.
- **Decision:** UKB (later + AoU) is the main analysis. The pooled results with FinnGen and Thomassen are a sensitivity analysis.

## 5. Other findings and their reliability

| Finding | Estimate | Reliability |
|---|---|---|
| CETP common GoF site rs1800777 (R451Q), oriented to lower function | Alzheimer's 1.07 (1.02; 1.12), p = 0.005; all-cause 1.07; frontotemporal 0.63; HDL +0.11; ASCVD 0.96 | Low. A single common variant (pleiotropy and LD can't be separated). Driven by one Thomassen stratum (GCST90861029: 1.13); UKB gives 1.02. Opposite in direction to the UKB rare-variant burden. Doesn't pass multiple testing |
| Frontotemporal dementia: HMGCR 22, NPC1L1 5.2 | p = 0.002 and 0.02 | Noise: ~1 case among carriers |
| APOE strata (LoF) | Signs flip between strata | Stale file (26 Oct 08:32); not interpreted |
| Thomassen | – | Contributes no rare variants: the `_fb` masks equal the full masks |

## 6. Answer so far

- **There is no robust evidence that genetically proxied lipid-lowering affects dementia risk.**
  - This holds for every gene with a valid instrument: PCSK9, CETP, NPC1L1, ANGPTL3.
- **The proxies are valid.** The lipids and the ASCVD effect of PCSK9 check out.
- **CETP in UKB is hypothesis-generating at best.** The ORs are below 1 on about 3 Alzheimer's cases, and there are no comparable variants in other cohorts.
- **This is absence of evidence, not evidence of absence.** Modest effects (OR ≈ 0.8) are compatible with the data.
- **All of Us would roughly double the carriers** and is the natural replication cohort.

## 7. Next

- Branch `ukb-burden-main`:
  - UKB-only meta-analysis for all variant sets, with an empty slot for AoU;
  - pooled UKB + FinnGen + Thomassen as the single sensitivity run;
  - drop the stale and redundant runs.
- **Planned figures:**
  1. Positive controls: lipids + ASCVD per gene, with markers for the variant sets.
  2. Dementia per gene in UKB, with carrier cases and an APOE reference row.
  3. ASCVD vs dementia scatter, one point per gene.
  4. CETP: the UKB burden against the FinnGen variants, per variant.
  - Supplement: pooled sensitivity, APOE strata, CETP rs1800777.
- **Choose one final variant set** (e.g. PTV+AM) after the rerun.
- **Follow-up:** why ClinVar adds no carriers (TODO.md).
