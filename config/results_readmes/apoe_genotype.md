# apoe_genotype

UKB marvel association of each APOE diplotype (carriers vs all other diplotypes) with the outcomes, for EUR and all samples.

## Script and command

- `src/apoe_exposure.py`, then marvelous associate (`config/marvel/apoe_<subset>.toml`, rows `apoe` of `data/raw/marvel_runs.tsv`, both from `src/create_config.py`), then `src/apoe_genotype_forest.py`. All in the APOE DIPLOTYPE section of `src/lipid_adem.sh`.

## Inputs

- `data/processed/lipids_full_pheno.tsv.gz` (UKB phenotypes with the APOE diplotype; 469,560 participants with a genotype).

## Choices

- The reference group is all other diplotypes, which mixes ε2 and ε4 carriers. So the ORs are **not** vs ε3/ε3.

## Results and interpretation

- **The positive control for the dementia outcomes:** the ε4 diplotypes raise the risk of all dementias, as expected.
- Confirms that the UKB dementia outcome definitions behave.
