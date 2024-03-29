# authors: Aidan, Mo

import dogma
import sys
import mcb185

def no_proline(sequence):
	if "P" in sequence:
		return False
	return True

def check_region(sequence, window, threshold):
	for i in range(len(sequence) - window + 1):
		subseq = sequence[i:i+window]
		tot = 0
		num = 0
		for aa in subseq:
			tot += dogma.hydropathy(aa)
			num += 1
		average = tot/num
		if average >= threshold and no_proline(subseq):
			return True
	return False

path = sys.argv[1]
num_transmembrane = 0
for defline, sequence in mcb185.read_fasta(path):
	signal_region = sequence[:30]
	transmembrane_region = sequence[30:]
	has_signal_peptide = check_region(signal_region, 8, 2.5)
	has_transmembrane_region = check_region(transmembrane_region, 11, 2.0)

	if has_signal_peptide and has_transmembrane_region:
		num_transmembrane += 1
		print(defline)

print("Number of Transmembrane Proteins:", num_transmembrane)
