#!/usr/bin/env python

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

import time
st = time.time()

def factorial(n):
    total = 0
    for i in str(n):
        res = 1
        for j in xrange(1,int(i)+1):
            res = res * j
        total += res
    return total

total = 0
for x in xrange(3,100000):
    if factorial(x) == x:
        total += x

print total

# oneliner - approx just as fast as the above
print sum(x for x in xrange(3,100000) if factorial(x) == x)

print "Time taken: %s" % str(time.time() - st)

