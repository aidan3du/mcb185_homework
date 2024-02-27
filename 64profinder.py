# authors: Aidan, Mo

import sys
import dogma
import mcb185

def six_frame_translation(dna):
	frames = []
	reverse = dogma.revcomp(dna)
	for i in range(3):
		frames.append(dogma.translate(dna[i:]))
		frames.append(dogma.translate(reverse[i:]))
	return "".join(frames)

def find_putative_genes(dna_sequence_file, protein_length):
	protein_deflines = []
	protein_sequences = []
	for defline, sequence in mcb185.read_fasta(dna_sequence_file):
		translated_frame = six_frame_translation(sequence)
	segments = translated_frame.split('*')

	for segment in segments:
		start_index = segment.find('M')
		if start_index != -1:
			protein = segment[start_index:]
			if len(protein) >= protein_length:
				protein_deflines.append(defline)
				protein_sequences.append(protein)

	for i in range(len(protein_deflines)):
		print(f'>{protein_deflines[i]}')
		print(protein_sequences[i])

	print(f'Found {len(protein_deflines)} putative genes')
path = sys.argv[1]
protein_length = int(sys.argv[2])

find_putative_genes(path, protein_length)