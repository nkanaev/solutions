#!/usr/bin/env python

N = 600851475143
#N = 13195

divs = []
while N != 1:
    i = 2
    while i <= N:
        if N % i == 0:
            divs.append(i)
            N /= i
        i += 1

print divs
