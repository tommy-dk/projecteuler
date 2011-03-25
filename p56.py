#!/usr/bin/env python

summa, delta = 0, 0

for i in xrange(0,100):
    for j in xrange(0,100):
        summa = sum(int(result) for result in str(i**j))
        if summa > delta:
            delta = summa
print delta

