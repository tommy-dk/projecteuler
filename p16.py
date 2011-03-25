#!/usr/bin/env python

"""
What is the sum of the digits of the number 2^1000?
"""

import time
st = time.time()

total = 0
for n in str(2**1000):
    total += int(n)

print total

# one liner
print reduce(lambda x, y: x + y, [int(i) for i in str(2 ** 1000)])

print "Time taken: %s" % str(time.time() - st)

