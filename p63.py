#!/usr/bin/env python

max = 0
for i in xrange(1,100):
    for j in xrange(1,100):
        if len(str(i**j)) == j:
            max += 1
print max
