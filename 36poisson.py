# Authors: Aidan, Mo

import math

def poisson(n ,k):
	# numerator = (n**k) * math.e**-n
	# denominator = math.factorial(k)
	print((n**k) * math.e**-n / math.factorial(k))

poisson(2, 3)
poisson(3, 4)
poisson(2, 4)
