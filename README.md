# Objective
Quickly call lineages using different SNP schemes from .vcf files. The package will be developed primarily to call MTB (_Mycobacterium tuberculosis_) lineages, but if you build your own SNP scheme you can use it to call lineages for virtually any bacterial species.



# Installation
```
git clone https://github.com/farhat-lab/fast-lineage-caller-vcf.git
cd fast-lineage-caller-vcf/
python setup.py sdist
pip install dist/fast_lineage_caller_vcf-0.1.1.tar.gz
```


# Example
I try to assign the lineage to the isolate SAMEA1708322:
```
fast-lineage-caller-vcf ~/mfarhat/rollingDB/genomic_data/SAMEA1708322/pilon/SAMEA1708322.vcf ./snp_schemes/coll.tsv
lineage4,lineage4.3,lineage4.3.4,lineage4.3.4.2,lineage4.3.4.2.1
```

# Changelog (roadmap)

Version 0.1.1
- working python module
- updated README (installation section)

Version 0.1.0

- initial python module (not tested)