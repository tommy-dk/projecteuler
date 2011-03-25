#!/usr/bin/env python

from math import log10
line,delta,final = 1,0,0

for c in open('p99.txt'):
    result = 0
    p = c.split(',')
#    result = int(p[0]) ** int(p[1])
    # b * log(a) is equivalent to a^b
    result = int(p[1]) * log10(int(p[0]))
    if result > delta:
        delta = result
        final = line
    line += 1

print final
