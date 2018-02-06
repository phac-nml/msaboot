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
PROGRAM_USAGE = "%(prog)s -i INPUT_LOCATION -o OUTPUT_LOCATION"

# ARGUMENTS #

LONG = "--"
SHORT = "-"

# REQUIRED ARGUMENTS #

# Version number
VERSION = 'version'
VERSION_SHORT = SHORT + 'V'
VERSION_LONG = LONG + VERSION

INPUT_LOCATION = ""

OUTPUT_LOCATION = ""


"""
# ==============================================================================

RUN
---


PURPOSE
-------

Runs the script.

INPUT
-----

[FILE LOCATION] [INPUT_LOCATION]
    The file location of the FASTA multiple sequence alignment input.

[FILE LOCATION] [OUTPUT_LOCATION]
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

    run()


"""
# ==============================================================================

MAIN
----

PURPOSE
-------
Adds arguments to parser, calls parse function.

# ==============================================================================
"""

def main():

    # --- PARSER --- #
    parser = argparse.ArgumentParser(
        description=PROGRAM_DESCRIPTION,
        usage=PROGRAM_USAGE)

    # --- VERSION --- #
    parser.add_argument(
        VERSION_SHORT,
        VERSION_LONG,
        action='version',
        version='%(prog)s ' + str(__version__))


    parse(None) #todo

"""
# =============================================================================
# =============================================================================
"""
if __name__ == '__main__':

    main()



