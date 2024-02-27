# authors: Aidan, Mo
import dogma

print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))
print(dogma.translate('ATGTAA'))

s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skeq(s), dogma.gc_skew(dogma.revcomp(s)))

