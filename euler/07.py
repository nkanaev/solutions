#!/usr/bin/env python

primebag = [2, 3, 5, 7, 11, 13]

i = 6
n = 15
while i != 10001:
    prime = True
    for prime in primebag:
        if n % prime == 0:
            prime = False
            break

    if prime:
        i += 1
        primebag.append(n)

    n += 2

print primebag[-1]
