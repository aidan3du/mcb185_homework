# authors: Aidan, Mo

import dogma
import mcb185
import sys

seq = ""
path = sys.argv[1]
for defline, s in mcb185.read_fasta(sys.argv[1]):
	seq += s
w = int(sys.argv[2])

for i in range(len(seq) - w +1):
	s = seq[i:i + w]
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
