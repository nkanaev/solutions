#!/usr/bin/env python

N = 100
a = sum([a*a for a in range(N+1)])
b = sum(range(N+1))
print abs(a - b*b)
