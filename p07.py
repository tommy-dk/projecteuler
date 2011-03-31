#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import time
st = time.time()

from euler import primes

numbers = primes(200000)
print numbers[10000]

print "Time taken: %s" % str(time.time() - st)
