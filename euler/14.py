#!/usr/bin/env python

number_sequences = {1: 1}

MAX_LIMIT = 1000000

def collatz_sequence(N):
    while N != 1:
        if N % 2 == 0:
            N /= 2
        else:
            N = 3*N + 1
        yield N

for x in xrange(2, MAX_LIMIT):
    if x in number_sequences:
        continue
    counter, uniq_path = 0, True
    for seq in collatz_sequence(x):
        counter += 1
        if seq in number_sequences:
            number_sequences[x] = number_sequences[seq] + counter
            uniq_path = False
            break
    if uniq_path:
        number_sequences[x] = counter

longest_chain_number = sorted(number_sequences, key=number_sequences.__getitem__, reverse=True)[0]
print longest_chain_number, number_sequences[longest_chain_number]
