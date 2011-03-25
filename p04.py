#!/usr/bin/env python

result, max = 0, 0
for i in xrange(100,999):
    for j in xrange(100,999):
        result = i * j
        pstr = str(result)
        if pstr == pstr[::-1] and result > max:
            max = result

print max
