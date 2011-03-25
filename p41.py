#!/usr/bin/env python

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from euler import ispandigital, primes

import time
st = time.time()

primes = primes(10000000)

total = 0
for prime in primes:
    if ispandigital(prime, len(str(prime))):
        if prime > total:
            total = prime

print total



print "Time taken: %s" % str(time.time() - st)
