#!/usr/bin/env python

"""
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""

import time
st = time.time()

from euler import ispandigital

product = {}
for i in xrange(1,101):
    for j in xrange(1,2001):
        if ispandigital(str(i)+str(j)+str(i*j)):
            if not str(i*j) in product:
                product[i*j] = 1

print sum(p for p in product)




print "Time taken: %s" % str(time.time() - st)

