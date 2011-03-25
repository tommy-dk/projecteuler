#!/usr/bin/env python

result = 0
for i in xrange(1,1000):
    if not i % 5 or not i % 3:
        result += i

print result
