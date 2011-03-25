#!/usr/bin/env python

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
    import math
    n = int(n)
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def rotate_seq (seq):
    for i in range (len (seq)):
        yield seq[i:] + seq[:i]


numbers = primes(100)
result = 0

for i in numbers:
    pstr = str(i)
    for j in rotate_seq(pstr):
        if is_prime(j):
            result += 1

print result
