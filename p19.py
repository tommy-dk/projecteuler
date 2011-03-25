#!/usr/bin/env python

from datetime import date

result = 0
for year in xrange(1901,2001):
    for month in xrange(1,13):
        if date(year, month, 1).isoweekday() == 7:
            result += 1

print result

print sum(int(date(y,m,1).isoweekday() == 7) for y in xrange(1901,2001) for m in xrange(1,13))
