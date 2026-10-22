#!/usr/bin/env bash
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SETUP
#
# REFERENCE OUTLINE ONLY -- do not run end-to-end.
set -euo pipefail

case "$(uname)" in
    Linux)
        ROOT="${HOME}/projects/lipid_adem"
        ;;
    Darwin)
        ROOT="${HOME}/Documents/work.nosync/projects/lipid_adem"
        ;;
    *)
        echo "Unknown system"
        ;;
esac

# shellcheck source=/dev/null
. "${ROOT}"/src/functions.sh


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# APOE DIPLOTYPE
# Needs only the phenotype file, so it runs first. Each diplotype (e3e3
# included) vs all other diplotypes.

# [myriad] exposure file: one 0/1 carrier column per diplotype
run_mamba biomed-api "${ROOT}"/src/apoe_exposure.py
# [myriad] associate the diplotypes with outcomes (all samples and EUR)
run_mamba marvel "${ROOT}"/src/create_config.py -a \
    -t "${ROOT}"/data/raw/marvel_apoe_tasks.tsv
run_mamba biomed-api pyjasub "${ROOT}"/config/marvel_apoe_task.cnf
# [local] rsync results/APOE_diplotype{,_eur} from Myriad first
run_mamba plot-misc "${ROOT}"/src/apoe_genotype_forest.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VARIANT ANNOTATION

# [snellius] VEP/LOFTEE consequences per gene, region read from the
# indexed per-chromosome VEP VCFs (-p pattern with {chrom})
LOF_DIR="/projects/0/aus20644/data/ukbiobank/genetics/b38/lof"
sbatch "${ROOT}"/src/vep_extract.sh -r "${ROOT}" -o "${ROOT}"/data/temp        \
    -d "${LOF_DIR}" -g "${ROOT}"/data/raw/gene_list.txt                        \
    -p "chr{chrom}_merged_vep.vcf.gz" -v

# Manually copy data/raw/vep_lipid_gene_csq.tsv.gz
# [myriad] LOFTEE HC PTVs on the canonical transcript
run_mamba biomed-api "${ROOT}"/src/annotate_ptv.py

# [local] query ClinVar for all variants in the curated genes
mapfile -t genes < <(cut -f1 "${ROOT}/data/raw/gene_list.txt")
runlog run --id clinvar_filter --order 40 --root "${ROOT}" --                  \
    mamba run --no-capture-output -n clinvar-build                             \
    clinvar-filter                                                             \
    "${HOME}/Documents/work.nosync/data/clinvar/clinvar_vcv.db"                \
    --rcv-db "${HOME}/Documents/work.nosync/data/clinvar/clinvar_rcv.db"       \
    -g "${genes[@]}"                                                           \
    -o "${ROOT}/data/raw/clinvar_variants.tsv"                                 \
    -vvv

run_mamba marvel "${ROOT}"/src/annotate_clinvar.py

# [myriad] combine PTV + ClinVar normalised against GRCh38
run_mamba biomed-api "${ROOT}"/src/combine_variants.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CARRIER EXTRACTION

# TODO not implemented: plan in docs/rap_carrier_extraction.md
# [rap] MARVELous Docker on Swiss Army Knife; extract both forms of each
# variant from the RAP PLINK files (WGS or WES)
# Manual copies:
# - git -> rap: dx upload data/temp/<GENE>_variants.tsv, the extraction
#   cnfs, src/rap_extract.sh and the Docker image tarball (once)
# - rap -> myriad: dx download the <GENE>_carriers.tsv.gz files into
#   data/raw/carriers/; individual-level data: check the UKB approval
#   allows the download, never commit, delete when no longer needed
# [myriad] collapse the two forms per variant (no merge on conflict) into
# data/temp/<GENE>_variant_extraction.tsv.gz (read by marvel_tasks.tsv)
# TODO if individual data/temp/<GENE>_variants.tsv doe not exist, but data/processed/lipid_variants does, create the individual files anytime the individual ones are needed (not in marvel itself of course, but before marvel submission e.g.)
# list full-sample vcf-files for some genes; exclude one of the chr1 genes
realpath "${ROOT}"/../cetp_marvel/data/temp/*plink*vcf.gz | 
    grep -v PCSK9 > "${ROOT}"/data/raw/plink_gene_vcfs.txt
DATA_DIR="/gpfs/work2/0/aus20644/data"
REF_DIR="${DATA_DIR}/resources/human_genome/b38"
LOF_DIR="${DATA_DIR}/ukbiobank/genetics/b38/lof"
"${ROOT}"/src/submit_two_source.sh                                             \
    -c "${ROOT}"/config/marvel_config.toml                                     \
    -p "${ROOT}"/data/raw/plink_gene_vcfs.txt                                  \
    -P "${LOF_DIR}"'/chr{chrom}_merged_vep.vcf.gz'                             \
    -R "${REF_DIR}/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz"             \
    -o "${ROOT}"/data/temp/marvel                                              \
    -a "${HOME}"/software/marvel/resources/workflows/slurm_array.sh            \
    -m '2023 BCFtools/1.18-GCC-12.3.0'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GWAS LOOKUPS

# [myriad] resolve gene/outcome lookups, discover studies, write job-array file
run_mamba biomed-api "${ROOT}"/src/gwas_cat_prep.py

# [myriad] filter GWAS catalog results to the gene regions
run_mamba biomed-api pyjasub "${ROOT}"/config/filter_task.cnf


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NON-AGGREGATED ANALYSES
# TODO AoU

# [myriad] marvel association per gene
run_mamba marvel "${ROOT}"/src/create_config.py -a
run_mamba biomed-api pyjasub "${ROOT}"/config/marvel_task.cnf

# [myriad] combine all marvel results
# Add --archive to tar the loose files, --refresh to rebuild the stores
run_mamba biomed-api "${ROOT}"/src/marvel_results_table.py --ancestry MULTI


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MERGE

# [myriad] adds GWAS Catalog associations + Open Targets gene-burden evidence
# and the marvel results listed in marvel_results.tsv with ≥ 5 carriers
qsub "${ROOT}"/src/merge_associations.sh -r "${ROOT}"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INTERMEDIATE MATCH

# [myriad] match GWAS lookups to the gene variant lists
run_mamba biomed-api "${ROOT}"/src/match_variants.py
# [myriad] filter GWAS for MAF, keep all marvel, no other variant selection
run_mamba biomed-api "${ROOT}"/src/match_variants.py --region-rare \
    --max-maf 0.01


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# META-ANALYSIS

# [myriad] fixed-effect IVW meta-analysis of the matched variants
# TODO why still in here?
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR

# [myriad] main meta-analysis: Thomassen and EUR UKB + FinnGen where Thomassen
# lacks variant
THOMASSEN_STUDIES=(GCST90861026 GCST90861027 GCST90861029 GCST90861030)
FINNGEN_STUDIES=(F5_DEMENTIA_INCLAVO G6_ALZHEIMER F5_VASCDEM FTD)
UKB_EUR_GROUPS=(
    marvel_ukb_EUR_{all_cause,alzheimers,vascular,frontotemporal}_dementia
)
UKB_GROUPS=(
    marvel_ukb_MULTI_{all_cause,alzheimers,vascular,frontotemporal}_dementia
)
# UKB accessions are written by marvel_results_table.py:
# marvel_ukb_<MULTI|EUR>_<outcome>, + _<stratum> for the APOE strata
UKB_OUTCOMES=(all_cause alzheimers vascular frontotemporal)
UKB_STUDIES=()
UKB_EUR_STUDIES=()
for outcome in "${UKB_OUTCOMES[@]}"; do
    for stratum in "" _e44 _e43 _e33 _e22_e32; do
        UKB_STUDIES+=("marvel_ukb_MULTI_${outcome}_dementia${stratum}")
        UKB_EUR_STUDIES+=("marvel_ukb_EUR_${outcome}_dementia${stratum}")
    done
done
ARMB_STUDIES=("${UKB_STUDIES[@]}" "${FINNGEN_STUDIES[@]}")

run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --studies "${THOMASSEN_STUDIES[@]}" "${UKB_EUR_STUDIES[@]}" \
    "${FINNGEN_STUDIES[@]}" \
    --variant-sources PTV ClinVar --stratified \
    --prefer-groups thomassen \
    --fallback-groups "${UKB_EUR_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
    --label annotated_eur

# [myriad] sensitivity using all UKB samples
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${THOMASSEN_STUDIES[@]}" "${UKB_STUDIES[@]}" \
    "${FINNGEN_STUDIES[@]}" \
    --variant-sources PTV ClinVar --stratified \
    --prefer-groups thomassen \
    --fallback-groups "${UKB_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
    --label maf_filter_all

# [myriad] sensitivity: main analysis without orientation by gene function
# (no GoF / ClinVar-raising flips, a2 allele effects)
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --studies "${THOMASSEN_STUDIES[@]}" "${UKB_EUR_STUDIES[@]}" \
    "${FINNGEN_STUDIES[@]}" \
    --variant-sources PTV ClinVar --stratified \
    --prefer-groups thomassen \
    --fallback-groups "${UKB_EUR_GROUPS[@]}" "${FINNGEN_STUDIES[@]}" \
    --label annotated_eur_unoriented --no-orient

# [myriad] without the variant lists: every rare variant in the gene region,
# alt-allele effects, NOT oriented by gene function
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry EUR \
    --outcomes alzheimers_dementia \
    --studies GCST90861026 GCST90861027 GCST90861029 GCST90861030 \
    --region-rare --stratified --label thomassen_ad_region_rare
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${ARMB_STUDIES[@]}" \
    --region-rare --stratified --label armb_dementia_region_rare
run_mamba biomed-api "${ROOT}"/src/meta_analysis.py --ancestry MULTI \
    --studies "${UKB_STUDIES[@]}" \
    --region-rare --stratified --label ukb_dementia_region_rare


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIGURES

# [local] copy results/output/burden_EUR_*.tsv.gz from Myriad first
# TODO still necessary?
for analysis in lists region_rare; do
    for script in burden_forest burden_apoe_forest burden_heatmap; do
        run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry MULTI \
            --label "armb_dementia_${analysis}"
    done
    for script in burden_forest burden_apoe_forest; do
        run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry EUR \
            --label "thomassen_ad_${analysis}"
    done
done

# [local] main analysis figures; only those in FigureNames.MAIN_FIGURES are
# written to results/figures, the rest to results/figures/sensitivity
for script in burden_forest burden_apoe_forest sources_forest pooled_forest; do
    run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry EUR \
        --label annotated_eur
    run_mamba plot-misc "${ROOT}/src/${script}.py" --ancestry MULTI \
        --label maf_filter_all
done
# [local] sensitivity: main analysis without orientation by gene function
run_mamba plot-misc "${ROOT}/src/burden_forest.py" --ancestry EUR \
    --label annotated_eur_unoriented
