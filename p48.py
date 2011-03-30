#!/usr/bin/env python

result = 0

for i in range(1,1000):
    result += i**i

result = str(result)
print int(result[-10:])

#one liner
print str(sum(p**p for p in xrange(1,1000)))[-10:]
