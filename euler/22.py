#!/usr/bin/env python

with open('names.txt') as f:
	names = sorted(map(lambda i: i[1:-1], f.read().split(',')))

def name_score(name):
	return reduce(lambda x, y: x+ord(y)-ord('A')+1, name, 0)

scores = 0
for i in range(len(names)):
	scores += (i+1) * name_score(names[i])
print scores