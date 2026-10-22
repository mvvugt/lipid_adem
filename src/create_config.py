#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: create_config
##
## Purpose of script: Create one marvel configuration file per task row for
## the association runs (src/marvel_assoc.sh, config/marvel_task.cnf); the
## row's `subset` sets the UKB samples (all, EUR) and APOE strata
##
## Author: M. van Vugt
## Date created: 07/11/2025
## Last updated: 12/10/2026
##
## Copyright (c) M. van Vugt, 2026
## Email: m.vanvugt1@amsterdamumc.nl
##
## Notes: marvel https://gitlab.com/mvvugt/marvel, commit eed4510, branch
## annotation. Run in the marvel env on Myriad after replacing every
## <placeholder> below and in data/raw/marvel_tasks.tsv.
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Imports
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import argparse
import pandas as pd
from project_constants import ApoeStratum, Constants, FileNames
from marvel.utils.config_tools import create_config
from marvel.constants import CONFIG_LHS as CFLhs


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Parse arguments
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--association',
                    action='store_true',
                    help = 'create configuration files for phenotype '
                    'association analysis, one per gene')
parser.add_argument('-t', '--tasks',
                    default = str(FileNames.MARVEL_TASKS),
                    help = 'job-array file with the columns gene, carriers, '
                    'config and subset (default: %(default)s)')

args = parser.parse_args()
if not args.association:
    parser.error('nothing to do: pass -a/--association')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Define files
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# UKB phenotype and covariates file
pheno_input = {
    CFLhs.PhenoFile : FileNames.UKB_PHENO,
    CFLhs.CovFile   : FileNames.UKB_PHENO,
    }

# the dementia outcomes in data/raw/icd_codes.txt, one binary (0/1) column
# each; GLM-Binom gives log-OR (Constants.MARVEL_METHOD_SCALE)
outcomes = [
    'ascvd_ii',
    'all_cause_dementia_algo',
    'all_cause_dementia_combined',
    'alzheimers_disease_algo',
    'alzheimers_disease_combined',
    'vascular_dementia_algo',
    'frontotemporal_dementia_algo',
    ]
lipids = [
        'Apolipoprotein A_i0',
        'Apolipoprotein B_i0',
        'HDL cholesterol_i0',
        'LDL direct_i0',
        'Triglycerides_i0',
        ]

# `model_1` is the `model` value in data/raw/marvel_results.tsv
pcs = [f'PC{i}' for i in range(1, 7)]
covs = {
    'model_1' : 'None',
    'model_2' : pcs,
    'model_3' : ['Sex'] + pcs,
    }

# UKB samples per task row (`subset` column of the job-array file); marvel
# names each subset by its `Stratification name`. Thomassen 2026 APOE
# strata (ApoeStratum.GENOTYPES, e2e4 in none); with stratify_overall
# False, marvel runs only the subsets listed here
pop_col = Constants.UKB_POPULATION_COLUMN
apoe_col = Constants.UKB_APOE_COLUMN
eur = f"{pop_col}={','.join(Constants.UKB_EUR_POPULATIONS)}"
apoe = {
    stratum: f"{apoe_col}={','.join(genotypes)}"
    for stratum, genotypes in ApoeStratum.GENOTYPES.items()
    }
sep = Constants.MARVEL_ANCESTRY_SEP
subsets = {
    # all samples, unstratified (`overall`)
    'all'         : None,
    # all samples, per APOE stratum
    'all_apoe'    : dict(apoe),
    # EUR, and EUR per APOE stratum
    'eur'         : {'EUR': eur} | {
        f'EUR{sep}{stratum}': f'{eur};{criterion}'
        for stratum, criterion in apoe.items()
        },
    # EUR only (APOE diplotype exposure, data/raw/marvel_apoe_tasks.tsv)
    'eur_overall' : {'EUR': eur},
    }

# one row per gene: the gene's carriers file (earlier marvel extraction
# output; every column is tested) and the configuration file to write
tasks = pd.read_csv(args.tasks, sep='\t')
if 'subset' not in tasks.columns:
    raise ValueError(f'{args.tasks}: no subset column')
unknown = sorted(set(tasks['subset']) - set(subsets))
if unknown:
    raise ValueError(
        f'{args.tasks}: unknown subset(s) {unknown}, expected one of '
        f'{sorted(subsets)}'
        )


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Check the stratification values
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# marvel keeps the rows whose value is listed and does not complain about a
# listed value that never occurs, so a misspelled genotype would silently
# shrink a stratum: every listed value must occur in the phenotype file
wanted = {}
for subset in set(tasks['subset']):
    for criteria in (subsets[subset] or {}).values():
        for criterion in criteria.split(';'):
            column, values = criterion.split('=', 1)
            wanted.setdefault(column, set()).update(values.split(','))
if wanted:
    header = pd.read_csv(FileNames.UKB_PHENO, sep='\t', nrows=0).columns
    missing = sorted(set(wanted) - set(header))
    if missing:
        raise ValueError(f'{FileNames.UKB_PHENO}: no column(s) {missing}')
    pheno = pd.read_csv(
        FileNames.UKB_PHENO, sep='\t', usecols=sorted(wanted), dtype=str
        )
    for column, values in sorted(wanted.items()):
        present = set(pheno[column].dropna())
        absent = sorted(values - present)
        if absent:
            raise ValueError(
                f'{FileNames.UKB_PHENO}: {column} has no {absent} '
                f'(values: {sorted(present)})'
                )
        print(f'[info] {column}: ' + ', '.join(
            f'{value}={n}' for value, n in
            pheno[column].value_counts(dropna=False).items()
            ))
    del pheno


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Create configuration files
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# tmp_dir and checkpoint_dir are relative: src/marvel_assoc.sh runs marvel
# inside a per-gene staging directory and removes it afterwards; output goes
# to marvelous --outpath
for row in tasks.itertuples(index = False):
    stratify = subsets[row.subset]
    options = {} if stratify is None else {
        'stratify'           : stratify,
        CFLhs.StratifyOverall : False,
        }
    # APOE diplotype (data/raw/marvel_apoe_tasks.tsv): the carriers file is
    # the 0/1 file of apoe_exposure.py, so no extra options; every column
    # is tested, as in the gene runs
    create_config(
        path                 = row.config,
        extract_variants     = False,
        association_analysis = True,
        exp_input            = {row.gene : row.carriers},
        pheno_input          = pheno_input,
        bin_tests            = {outcome: ['GLM-Binom'] for outcome in outcomes},
        con_tests            = {lipid: ['OLS'] for lipid in lipids},
        covs                 = covs,
        id_column            = 'f.eid',
        raise_on_error       = False,
        tmp_dir              = './tmp',
        checkpoint_dir       = './checkpoint',
        **options,
    )
    print(f'[info] {row.gene} ({row.subset}): {row.config}')
