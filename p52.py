#!/usr/bin/env python

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import time
st = time.time()

def has_digits(n):
    digit_keys = dict.fromkeys(list(str(n)))

    for x in xrange(2,4):
        for d in list(str(n*x)):
            if not digit_keys.has_key(d): return False
    return True


n=0
while True:
    n = n + 9
    if has_digits(n):
        print n
        break
        




print "Time taken: %s" % str(time.time() - st)

