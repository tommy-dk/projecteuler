#!/usr/bin/env python

res = 1
for i in xrange(1,101):
    res = res * i

final = 0
for i in str(res):
    final += int(i)

print str(final)

print sum([int(x*x) for x in xrange(1,101)])

# one liners
reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])

sum(int(n) for n in str(reduce(lambda x,y: x*y, xrange(1,101))))
