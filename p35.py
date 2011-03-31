#!/usr/bin/env python

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import time
st = time.time()

from euler import primes, is_prime

def rotate_seq (seq):
    for i in range (len (seq)):
        yield seq[i:] + seq[:i]

def is_circular(n):
    for i in rotate_seq(str(n)):
        if not is_prime(i):
            return False
    return True


numbers = primes(1000000)
result = 0

for i in numbers:
    if is_circular(i):
        result += 1

print result

print "Time taken: %s" % str(time.time() - st)
