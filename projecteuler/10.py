#!/usr/bin/env python

from math import sqrt, floor


primebag = [2, 3, 5, 7, 11, 13]

for n in xrange(15, 2000000, 2):
    prime = True
    lim = floor(sqrt(n))
    for x in primebag:
        if n % x == 0:
            prime = False
            break
        if x >= lim:
            break
   
    if prime:
        primebag.append(n)

print sum(primebag)
