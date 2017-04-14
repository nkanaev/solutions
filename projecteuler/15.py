#!/usr/bin/env python

width, height = 20, 20

matrix = [[1 for x in xrange(width+1)] for x in xrange(height+1)]

for x in xrange(1, width+1):
    for y in xrange(1, height+1):
        matrix[x][y] = matrix[x-1][y] + matrix[x][y-1]

print matrix[x][y]
