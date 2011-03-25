#!/usr/bin/env python

result, integer = 0, 0

for i in xrange(2,1000):
    res = 1 / float(i)
    print i, res
    if len(str(res)) > result:
        result = res
        integer = i

#print result, integer
