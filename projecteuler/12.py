#!/usr/bin/env python

N = 1

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] 
        for i in range(1, int(n**0.5) + 1) if n % i == 0))) 

factor_bag = set()
print len(factors(76576500))

N = 1
X = 1
while len(factors(X)) <= 500:
    N += 1
    X += N

print N, X

