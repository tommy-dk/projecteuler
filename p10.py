#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from euler import primes

import time
st = time.time()

numbers = primes(2000000)

result = 0
for i in numbers:
    result += i

print result

print "Time taken: %s" % str(time.time() - st)
