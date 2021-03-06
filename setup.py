from setuptools import find_packages, setup

dependencies = ['numpy', 'biopython']

setup(
    name='msaboot',
    version='0.1.2',
    url='https://github.com/phac-nml/msaboot.git',
    license='Apache-2.0',
    author='Matthew Fogel',
    author_email='matthew.fogel@canada.ca',
    description='Creates bootstrapping replicates from FASTA file and saves them in relaxed PHYLIP format.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'msaboot = msaboot.msaboot:main',
        ],
    },
)
