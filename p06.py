#!/usr/bin/env python

"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import time
st = time.time()

sum_of_squares, squares_of_sum = 0,0
for i in xrange(1,101):
    sum_of_squares += i**2
    squares_of_sum += i

print (squares_of_sum**2) - sum_of_squares

print "Time taken: %s" % str(time.time() - st)
