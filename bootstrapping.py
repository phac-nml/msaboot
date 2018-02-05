from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.Consensus import *

inputAlignment = AlignIO.read('msa.fasta', 'fasta')
multipleSequenceAlignments = bootstrap(inputAlignment, 7) # generate bootstrap

for alignment in multipleSequenceAlignments:
    print(alignment)
    

print("\nDone!")
