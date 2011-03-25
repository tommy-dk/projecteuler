#!/usr/bin/env python

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.



"""

fact_c = { 0: 1, 1: 1 }
def factorial(n): return fact_c.has_key(n) and fact_c[n] or fact_c.setdefault(n, n * factorial(n-1))


def calc(n,r):
    c = factorial(n) / factorial(r) / factorial(n - r)
    return c

total = 0
for n in xrange(1,101):
    for r in xrange(1,n):
        c = calc(n,r)
        if c > 1000000:
            total += 1

print total

import time
st = time.time()







print "Time taken: %s" % str(time.time() - st)

