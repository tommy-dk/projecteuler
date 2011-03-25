#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 
digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

from euler import primes, is_prime

import time
st = time.time()


def truncate_left(n):
    for i in xrange(1,len(str(n))):
        if not is_prime(int(str(n)[i:len(str(n))])):
            return False
    return True

def truncate_right(n):
    for i in xrange(1,len(str(n))):
        if not is_prime(int(str(n)[0:-i])):
            return False
    return True

primes = primes(1000000)
total = 0
result = []
for i in primes:
    if i > 7:
        if truncate_left(i) and truncate_right(i):
            result.append(i)

print "Result: " + str(result)
print "Total: " + str(sum(result))

print "Time taken: %s" % str(time.time() - st)

