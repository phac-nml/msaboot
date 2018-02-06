"""
# ==============================================================================
Copyright Government of Canada 2018

Written by: Matthew Fogel, Public Health Agency of Canada

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
# ==============================================================================
"""
__version__ = '0.1.0'

from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.Consensus import *
import argparse

"""
# ==============================================================================

GLOBALS

# ==============================================================================
"""

PROGRAM_DESCRIPTION = "This program bootstraps multiple sequence alignment data."

# ARGUMENTS #

LONG = "--"
SHORT = "-"

"""
# ==============================================================================

RUN
---


PURPOSE
-------

Runs the script.

INPUT
-----

[FILE LOCATION] [inputLocation]
    The file location of the FASTA multiple sequence alignment input.

[FILE LOCATION] [output location]
    The file location to store output bootstrapped multiple sequence alignment data.

RETURN
------

[NONE]

POST
----

The bootstrapped FASTA data will be generated and written to [outputLocation].

# ==============================================================================
"""

def run():

    inputAlignment = AlignIO.read('msa.fasta', 'fasta')
    multipleSequenceAlignments = bootstrap(inputAlignment, 7) # generate bootstrap

    for alignment in multipleSequenceAlignments:
        print(alignment)
	    
    print("\nDone!")


"""
# ==============================================================================

PARSE
-----

PURPOSE
-----
Get parameters from parser, call run function

# ==============================================================================
"""

def parse(parameters):


"""
# ==============================================================================

MAIN

PURPOSE
-------
Adds arguments to parser, calls parse function.

# ==============================================================================
"""

def main():



"""
# =============================================================================
# =============================================================================
"""
if __name__ == '__main__':

    main()



