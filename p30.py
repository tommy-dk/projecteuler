#!/usr/bin/env python

"""
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import time
st = time.time()

""" 
9^5 = 59049

2 digits * 59049 = 118098 > 99
3 digits * 59049 = 177147 > 999
4 digits * 59049 = 236196 > 9999
...
9 digits * 59049 = 531441 < 999999999

max 
"""


def calc(n):
    total = 0
    for i in str(n):
        total += int(i)**5
    return total

total = 0
for i in xrange(2,200000):
    if i == calc(i):
        total += i

print total

# one liner
print sum(i for i in range(2,200000) if i == sum(int(j)**5 for j in str(i)))

print "Time taken: %s" % str(time.time() - st)

