# Authors: Aidan, Mo

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

dup = 0
bdays = []

for i in range(days):
	bdays.append(0)

for t in range(trials):
	for i in range(days):
		bdays[i] = 0

	for i in range(people):
		bdays[random.randint(0, days-1)] += 1

	for count in bdays:
		if count > 1:
			dup += 1
			break
probability = dup / trials
print(probability)
