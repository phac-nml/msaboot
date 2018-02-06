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
import os

"""
# ==============================================================================

GLOBALS

# ==============================================================================
"""

PROGRAM_DESCRIPTION = "This program bootstraps multiple sequence alignment data."
PROGRAM_USAGE = "%(prog)s -i INPUT_LOCATION -o OUTPUT_LOCATION -n NUM_BOOTSTRAPS"

# ARGUMENTS #

LONG = "--"
SHORT = "-"

# REQUIRED ARGUMENTS #

# Version number
VERSION = "version"
VERSION_SHORT = SHORT + "V"
VERSION_LONG = LONG + VERSION

INPUT = "input"
INPUT_SHORT = SHORT + "i"
INPUT_LONG = LONG + INPUT
INPUT_HELP = "The file name of the FASTA file to be used as input."

OUTPUT = "output"
OUTPUT_SHORT = SHORT + "o"
OUTPUT_LONG = LONG + OUTPUT
OUTPUT_HELP = "The file name of the bootstrapped alignment data output."

NUMBER = "number"
NUMBER_SHORT = SHORT + "n"
NUMBER_LONG = LONG + NUMBER
NUMBER_HELP = "The number of times the input multiple sequence alignments will be bootstrapped."


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

[FILE LOCATION] [outputLocation]
    The file location to store output bootstrapped multiple sequence alignment data.

[FILE LOCATION] [numBootstraps]
    The number of times bootstrapping will be performed on the multiple sequence alignment data.

RETURN
------

[NONE]

POST
----

The bootstrapped FASTA data will be generated and written to [outputLocation].

# ==============================================================================
"""

def run(inputLocation, outputLocation, numBootstraps):

    if not os.path.isfile(inputLocation):
        raise RuntimeError(
            "ERROR: Could not open input file: " + inputLocation + "\n")

    inputAlignment = AlignIO.read(inputLocation, 'fasta')
    multipleSequenceAlignments = bootstrap(inputAlignment, int(numBootstraps)) # generate bootstrap

    for alignment in multipleSequenceAlignments:
        print(alignment)


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

    inputLocation = parameters.get(INPUT)
    outputLocation = parameters.get(OUTPUT)
    numBootstraps = parameters.get(NUMBER)

    run(inputLocation, outputLocation, numBootstraps)


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

    # --- INPUT --- #
    parser.add_argument(
        INPUT_SHORT,
        INPUT_LONG,
        dest = INPUT,
        help = INPUT_HELP,
        type=str, required=True)

    # --- OUTPUT --- #
    parser.add_argument(
        OUTPUT_SHORT,
        OUTPUT_LONG,
        dest = OUTPUT,
        help = OUTPUT_HELP,
        type=str, required=True)

    # --- NUMBER --- #
    parser.add_argument(
        NUMBER_SHORT,
        NUMBER_LONG,
        dest = NUMBER,
        help = NUMBER_HELP,
        type=str, required=True)

    args = parser.parse_args()
    parameters = vars(args)

    print("Bootstrapping v" + str(__version__) + "\n")
    parse(parameters)

    print("\nComplete!")

"""
# =============================================================================
# =============================================================================
"""
if __name__ == '__main__':

    main()



