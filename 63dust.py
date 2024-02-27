# authors: Aidan, Mo

import dogma
import mcb185
import sys

path = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(path):
	print('>' + defline)
	seq_list = list(seq)
	for i in range(len(seq) - w + 1):
		s = seq[i:i + w]
		a_count = s.count('A')
		c_count = s.count('C')
		g_count = s.count('G')
		t_count = s.count('T')
		if dogma.entropy(a_count, c_count, g_count, t_count) < threshold:
			for j in range(i, i + w):
				seq_list[j] = 'N'
	final_seq = ''.join(seq_list)

	for i in range(0, len(final_seq), 60):
		print(final_seq[i:i+60])
