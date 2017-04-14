#!/usr/bin/env python

import sys

max_num = 0
for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        product = str(a*b)
        if product == product[::-1]:
            max_num = max(max_num, a*b)

print max_num
