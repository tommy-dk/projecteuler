#!/usr/bin/env python

for a in xrange(1,1000):
    for b in xrange(a,1000):
        c = 1000 - a - b
        if c > 0:
            if c**2 == a**2 + b**2:
                print a * b *c
