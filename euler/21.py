#!/usr/bin/env python

def divisors(num):
	result = [1]
	for i in range(2, num/2+2):
		if num % i == 0:
			result.append(i)
	return result

AMICABLES = {}
def amicable(num):
	if num == 1:
		return 0
	if AMICABLES.get(num):
		return AMICABLES[num]

	AMICABLES[num] = x = sum(divisors(num))
	return x

amicable_bag = set()
for i in range(2, 10000):
	if amicable(amicable(i)) == i:
		if amicable(i) == i:
			continue
		amicable_bag.add(i)
		amicable_bag.add(amicable(i))

print sum(amicable_bag)