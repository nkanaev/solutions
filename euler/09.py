#!/usr/bin/env python

from math import sqrt


for a in xrange(1, 500):
    for b in xrange(a+1, 500):
        c = sqrt(a*a + b*b)
        if c == int(c) and a + b + c == 1000:
            print a, b, c
            print a*b*c
            import sys
            sys.exit(0)
