#!/usr/bin/env python

limit = 28123+1

divisors_sum = [0] * limit
abundants = {12}
for i in range(2, limit/2+2):
	for n in range(i+i, limit, i):
		divisors_sum[n] += n
		if divisors_sum[n] > n:
			abundants.add(n)

abundants = [i for i in range(12, limit) if divisors_sum[i] > i]

len_abundants = len(abundants)
non_abundants = {i for i in range(1, limit)}
for i1 in range(len_abundants):
	for i2 in range(i1+1, len_abundants):
		num = abundants[i1] + abundants[i2]
		if num >= limit:
			break
		try:
			non_abundants.remove(num)
		except:
			pass
	print i1

print sum(non_abundants)