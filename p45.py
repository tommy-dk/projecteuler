#!/usr/bin/env python

MAX=100000
triangle = [ n * (n+1)/2 for n in xrange(0,MAX) ]
pentagonal = [ n * (3*n-1)/2 for n in xrange(0,MAX) ]
hexagonal = [ n * (2*n-1) for n in xrange(0,MAX) ]

pent_dict = dict.fromkeys(pentagonal, True)
hex_dict = dict.fromkeys(hexagonal, True)

for n in xrange(286,MAX):
    value = triangle[n]
    if value in pent_dict and value in hex_dict:
        print value
        break
