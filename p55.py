#!/usr/bin/env python


def is_lychrel(n):
    n = str(n)
    for x in xrange(0,50):
        n = str(int(n) + int(n[::-1]))
        if n == n[::-1]: return False
    return True

print sum([1 for i in xrange(0,10000) if is_lychrel(i)])
