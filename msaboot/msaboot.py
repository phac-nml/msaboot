#!/usr/bin/env python

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
__version__ = '0.1.2'

from Bio import Phylo
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.Consensus import *
import argparse
import os

"""
# ==============================================================================

GLOBALS

# ==============================================================================
"""

PROGRAM_DESCRIPTION = "This program bootstraps FASTA input data."
PROGRAM_USAGE = "%(prog)s -i IN_LOCATION -o OUT_LOCATION -n NUM_REPLICATES"

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
NUMBER_HELP = "The number of bootstrap replicates."


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
    The output location to store bootstrapped multiple sequence alignment data.

[INT >= 0] [numBootstraps]
    The number of bootstrap replicates that will be created.

RETURN
------

[NONE]

POST
----

The bootstrapped FASTA data will be generated and written to [outputLocation].

# ==============================================================================
"""

def run(inputLocation, outputLocation, numBootstraps):

    # input
    if not os.path.isfile(inputLocation):
        raise RuntimeError(
            "ERROR: Could not open input file: " + inputLocation + "\n")

    print("Reading from input file " + inputLocation)

    # bootstrapping

    inputAlignment = AlignIO.read(inputLocation, 'fasta')

    seq_length = inputAlignment.get_alignment_length()

    #check that sequences are all the same length
    if len(inputAlignment) == 0:
        raise ValueError("The input file must contain at least one sequence.")
    if seq_length <= 0:
        raise ValueError("Non empty sequences are required")
    for record in inputAlignment:
        if seq_length != len(record.seq):
            raise ValueError("Sequences must be all the same length")
        #end if
    #end if

    # generate bootstrap
    bootstrapAlignments = bootstrap(inputAlignment, int(numBootstraps))

    count = 0

    file = open(outputLocation, 'w')
    for alignment in bootstrapAlignments:
        if count>0:
            file.write("\n")
        #end if
        file.write(" %i %s\n" % (len(alignment), seq_length))
        #for each sequence record write the sequence name, a space, and the sequence itself
        file.write('\n'.join([(str(record.id) + " " + str(record.seq)) for record in alignment]))
        count += 1

    # output
    print("Wrote to output file " + outputLocation)


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

    # get parameters inputted from command line
    inputLocation = parameters.get(INPUT)
    outputLocation = parameters.get(OUTPUT)
    numBootstraps = parameters.get(NUMBER)

    # run bootstrapping program with above parameters
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
        dest=INPUT,
        help=INPUT_HELP,
        type=str, required=True)

    # --- OUTPUT --- #
    parser.add_argument(
        OUTPUT_SHORT,
        OUTPUT_LONG,
        dest=OUTPUT,
        help=OUTPUT_HELP,
        type=str, required=True)

    # --- NUMBER --- #
    parser.add_argument(
        NUMBER_SHORT,
        NUMBER_LONG,
        dest=NUMBER,
        help=NUMBER_HELP,
        type=str, required=True)

    args = parser.parse_args()
    parameters = vars(args)

    print("msaboot v" + str(__version__) + "\n")
    parse(parameters)

    print("\nComplete!")

"""
# =============================================================================
# =============================================================================
"""
if __name__ == '__main__':

    main()
