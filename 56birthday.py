# Authors: Aidan, Mo

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

dup = 0
probability = 0
bdays = list()

for t in range(trials):
	for i in range(people):
		bday = random.randint(0, days-1)
		if bday in bdays:
			dup += 1
			break
		bdays.append(bday)
	bdays = list()
probability = dup / trials
print(probability)

