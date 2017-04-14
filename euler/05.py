#!?usr/bin/emv python

import fractions
def lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0

smallest = 1
for i in range(2, 21, 1):
    smallest = lcm(smallest, i)

print smallest
