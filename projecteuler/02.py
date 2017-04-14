#!/usr/bin/env python

f_prev, f = 1, 2

n = 2
even_sums = 0
while True:
    if f % 2 == 0:
        even_sums += f
    if f > 4000000:
        break
    f = f + f_prev
    f_prev = f - f_prev

print even_sums
