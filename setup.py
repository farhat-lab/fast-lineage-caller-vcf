from setuptools import setup

def readme():
	    with open('README.rst') as f:
		            return f.read()

		    setup(name='metatools_ncbi',
				    version='0.1.4',
				    description='Download biosample and SRA runinfo metadata from NCBI',
				    url='http://github.com/farhat-lab/metatools_ncbi',
				    author='Luca Freschi',
				    author_email='l.freschi@gmail.com',
				    license='LGPLv3',
				    packages=['metatools_ncbi'],
				    classifiers=[
					            'Development Status :: 4 - Beta',
						            'Environment :: Console',
							            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
								            'Operating System :: POSIX :: Linux',
									            'Programming Language :: Python :: 3',
										            'Topic :: Scientific/Engineering :: Bio-Informatics',
											          ],
				          keywords='ncbi download metadata biosample runinfo',
					        install_requires=[
							          'progress',
								            'requests'
									          ],
						      scripts=['bin/metatools_download'],
						      zip_safe=False)

