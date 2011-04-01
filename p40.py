#!/usr/bin/env python

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

"""

import time
st = time.time()

number = list()

for i in xrange(0,200000):
    for j in str(i):
        number.append(str(j))

total = 1
for i in range(7):
    total *= int(number[10**i])

print total

print "Time taken: %s" % str(time.time() - st)

