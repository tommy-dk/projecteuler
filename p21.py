#!/usr/bin/env python

from math import sqrt

def divisors(n):
    div=[1]
    check=2
    rootn=sqrt(n)
    while check<rootn:
        if n%check==0:
            div.append(check)
            div.append(n/check)
        check+=1
    if rootn==check:
        div.append(check)
        div.sort()
    return div

delta, res = 0, 0
for i in xrange(1,10000):
    delta = sum(divisors(i))
    if sum(divisors(delta)) == i and i <> delta:
        res += i

print res
