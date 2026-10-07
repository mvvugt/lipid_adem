#!/usr/bin/env python3
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Script information
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
## Script name: create_config
##
## Purpose of script: Create one marvel configuration file per gene for the
## per-gene association runs (src/marvel_assoc.sh, config/marvel_task.cnf)
##
## Author: M. van Vugt
## Date created: 07/11/2025
## Last updated: 07/10/2026
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
from project_constants import FileNames
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
                    help = 'job-array file with the columns gene, carriers '
                    'and config (default: %(default)s)')

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
bin_list = ['GLM-Binom', ]
outcomes = [
    'all_cause_dementia_algo',
    'all_cause_dementia_combined',
    'alzheimers_dementia_algo',
    'alzheimers_dementia_combined',
    'vascular_dementia_algo',
    'frontotemporal_dementia_algo',
    ]
bin_tests = {outcome: list(bin_list) for outcome in outcomes}

# `model_1` is the `model` value in data/raw/marvel_results.tsv
pcs = [f'PC{i}' for i in range(1, 7)]
covs = {
    'model_1' : 'None',
    'model_2' : pcs,
    'model_3' : ['Sex'] + pcs,
    }

# # Thomassen 2026 APOE strata (data/raw/apoe_strata.tsv); e42 in none. The
# # unstratified run (`overall`, stratify_overall) is the pooled result.
# apoe_col = '<apoe_col>'
# stratify = {
#     'e44'     : f'{apoe_col}=<e4e4>',
#     'e43'     : f'{apoe_col}=<e3e4>',
#     'e33'     : f'{apoe_col}=<e3e3>',
#     'e22_e32' : f'{apoe_col}=<e2e2>,<e2e3>',
#     }

# one row per gene: the gene's carriers file (earlier marvel extraction
# output; every column is tested) and the configuration file to write
tasks = pd.read_csv(args.tasks, sep='\t')


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Create configuration files
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# tmp_dir and checkpoint_dir are relative: src/marvel_assoc.sh runs marvel
# inside a per-gene staging directory and removes it afterwards; output goes
# to marvelous --outpath
for row in tasks.itertuples(index = False):
    create_config(
        path                 = row.config,
        extract_variants     = False,
        association_analysis = True,
        exp_input            = {row.gene : row.carriers},
        pheno_input          = pheno_input,
        bin_tests            = bin_tests,
        covs                 = covs,
        id_column            = 'f.eid',
        raise_on_error       = False,
        tmp_dir              = './tmp',
        checkpoint_dir       = './checkpoint',
    )
    print(f'[info] {row.gene}: {row.config}')
