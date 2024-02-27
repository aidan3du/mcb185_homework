# authors: Aidan, Mo

import math

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: rc.append('N')
	return ''.join(rc)

def translate(dna):
	protein_sequence = ''
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'TTT' or codon == 'TTC':
			protein_sequence += 'F'
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC'\
		or codon == 'CTA' or codon == 'CTG':
			protein_sequence += 'L'
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG':
			protein_sequence += 'S'
		elif codon == 'TAT' or codon == 'TAC':
			protein_sequence += 'Y'
		elif codon == 'TGT' or codon == 'TGC':
			protein_sequence += 'C'
		elif codon == 'TGG':
			protein_sequence += 'W'
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
			protein_sequence += 'P'
		elif codon == 'CAT' or codon == 'CAC':
			protein_sequence += 'H'
		elif codon == 'CAA' or codon == 'CAG':
			protein_sequence += 'Q'
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG'\
		or codon == 'AGA' or codon == 'AGG':
			protein_sequence += 'R'
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
			protein_sequence += 'I'
		elif codon == 'ATG':
			protein_sequence += 'M'
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
			protein_sequence += 'T'
		elif codon == 'AAT' or codon == 'AAC':
			protein_sequence += 'N'
		elif codon == 'AAA' or codon == 'AAG':
			protein_sequence += 'K'
		elif codon == 'AGT' or codon == 'AGC':
			protein_sequence += 'S'
		elif codon == 'AGA' or codon == 'AGG':
			protein_sequence += 'R'
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
			protein_sequence += 'V'
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
			protein_sequence += 'A'
		elif codon == 'GAT' or codon == 'GAC':
			protein_sequence += 'D'
		elif codon == 'GAA' or codon == 'GAG':
			protein_sequence += 'E'
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
			protein_sequence += 'G'
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			protein_sequence += '*'
		else:
			protein_sequence += 'X'
	return protein_sequence

def hydropathy(amino_acid):
	if amino_acid == "A":
		return 1.80
	elif amino_acid == "C":
		return 2.50
	elif amino_acid == "D":
		return -3.50
	elif amino_acid == "E":
		return -3.50
	elif amino_acid == "F":
		return 2.80
	elif amino_acid == "G":
		return -0.40
	elif amino_acid == "H":
		return -3.20
	elif amino_acid == "I":
		return 4.50
	elif amino_acid == "K":
		return -3.90
	elif amino_acid == "L":
		return 3.80
	elif amino_acid == "M":
		return 1.90
	elif amino_acid == "N":
		return -3.50
	elif amino_acid == "P":
		return -1.60
	elif amino_acid == "Q":
		return -3.50
	elif amino_acid == "R":
		return -4.50
	elif amino_acid == "S":
		return -0.80
	elif amino_acid == "T":
		return -0.70
	elif amino_acid == "U":
		return 2.50
	elif amino_acid == "V":
		return 4.20
	elif amino_acid == "W":
		return -0.90
	elif amino_acid == "Y":
		return -1.30
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_comp_counts(count_c, count_g, seq_length):
	return (count_c + count_g) / seq_length

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	return gc_skew_counts(c, g)

def gc_skew_counts(c, g):
	if c + g == 0:
		return 0
	return (g - c) / (g + c)

def entropy(A, C, G, T):
	total = A + C + G + T

	if total == 0:
		return 0

	probability_a = A / total
	probability_c = C / total
	probability_g = G / total
	probability_t = T / total

	a = probability_a * math.log2(probability_a) if probability_a > 0 else 0
	c = probability_c * math.log2(probability_c) if probability_c > 0 else 0
	g = probability_g * math.log2(probability_g) if probability_g > 0 else 0
	t = probability_t * math.log2(probability_t) if probability_t > 0 else 0

	return -(a + c + g + t)

