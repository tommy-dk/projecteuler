#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 
digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

import time
st = time.time()

def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def is_prime(n):
    if n < 2:
        return False
    import math
    n = int(n)
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def truncate_left(n):
    for i in xrange(1,len(str(n))):
        if not is_prime(int(str(n)[i:len(str(n))])):
            return False
    return True

def truncate_right(n):
    for i in xrange(1,len(str(n))):
        if not is_prime(int(str(n)[0:-i])):
            return False
    return True

primes = primes(1000000)
total = 0
result = []
for i in primes:
    if i > 7:
        if truncate_left(i) and truncate_right(i):
            result.append(i)

print "Result: " + str(result)
print "Total: " + str(sum(result))

print "Time taken: %s" % str(time.time() - st)

