#!/usr/bin/env python

fact = 1
for i in range(2, 100):
	fact *= i

print sum(map(int, list(str(fact))))