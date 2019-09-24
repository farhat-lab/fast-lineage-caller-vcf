# Objective
Quickly call lineages using different SNP schemes from vcf files. The package will be developed primarily to call MTB (Mycobacterium tuberculosis) lineages, but if you build your own SNP scheme you can use it to call lineages for vistually any bacterial species.



# Installation
```
git clone https://github.com/farhat-lab/fast-lineage-caller-vcf.git
cd fast-lineage-caller-vcf/
python setup.py sdist

```


# Example
I try to assign the lineage to the isolate SAMEA1708322:
```
fast-lineage-caller-vcf ~/mfarhat/rollingDB/genomic_data/SAMEA1708322/pilon/SAMEA1708322.vcf ./snp_schemes/coll.tsv
```

# Changelog (roadmap)

Version 0.1.1
- working python module
- updated README (installation section)

Version 0.1.0
- initial python module (not tested)