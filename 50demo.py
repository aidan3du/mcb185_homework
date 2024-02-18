# Authors: Aidan, Mo

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)
intercepts = quadratic(5, 6, 1)
print(intercepts[0], intercepts[1]) 
