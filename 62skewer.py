# authors: Aidan, Mo

import dogma
import mcb185
import sys

seq = ""
path = sys.argv[1]
for defline, s in mcb185.read_fasta(sys.argv[1]):
	seq += s
w = int(sys.argv[2])

c_count = 0
g_count = 0

for i in range(len(seq) - w + 1):
	s = seq[i:i + w]
	if i == 0:
		c_count = s.count('C')
		g_count = s.count('G')
	else:
		if seq[i - 1] == 'C':
			c_count -= 1
		if seq[i - 1] == 'G':
			g_count -= 1
		if seq[i + w - 1] == 'C':
			c_count += 1
		if seq[i + w - 1] == 'G':
			g_count += 1
			
	print(f'{i}\t{dogma.gc_comp_counts(c_count, g_count, w)}', end = '')
	print(f'\t{dogma.gc_skew_counts(c_count, g_count):.3f}')
