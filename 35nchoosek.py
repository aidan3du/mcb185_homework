# Authors: Aidan, Mo

import math

def nchoosek(n, k):
	numerator = math.factorial(n)
	if n < k:
		print('n cannot be less than')
	else:
		denominator = math.factorial(k) * math.factorial(n-k)
		print(numerator/denominator)


nchoosek(4, 6)
nchoosek(6, 9)
nchoosek(23, 11)
