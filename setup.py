from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='fast_lineage_caller_vcf',
version='0.1.1',
description='Module to call MTB lineages from a .vcf file',
url='https://github.com/farhat-lab/fast-lineage-caller-vcf/',
author='Luca Freschi',
author_email='l.freschi@gmail.com',
license='LGPLv3',
packages=[],
classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
      keywords='Mycobacterium tuberculosis lineage calling',
      install_requires=[],
      scripts=['bin/fast-lineage-caller-vcf'],
zip_safe=False)
