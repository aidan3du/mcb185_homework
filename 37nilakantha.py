# Authors: Aidan, Mo

def nilakantha(n):
	sum = 3
	sign = 1

	for i in range(2, n, 2):
		sum += sign * 4 / (i * (i+1) * (i+2))
		sign *= -1
	print(sum)

nilakantha(1000000)
nilakantha(5)
nilakantha(500)

