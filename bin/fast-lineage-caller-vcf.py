#!/usr/bin/env python3

from importlib import reload
import argparse
import sys
sys.path.insert(0, '.')
from fast_lineage_caller import base

parser = argparse.ArgumentParser()
parser.add_argument("vcf_file", type=str,
                    help="Input VCF (variants called against the reference of a given SNP scheme)")
parser.add_argument('snp_scheme', type=str,
                    help="TSV containing the SNP scheme")
args = parser.parse_args()

(snp_scheme, list_positions_lineage_snps_reference) = base.read_snp_scheme(args.snp_scheme)
lineage = base.assign_lineage(args.vcf_file, snp_scheme, list_positions_lineage_snps_reference)
print(lineage)
