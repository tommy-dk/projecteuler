#!/usr/bin/env python

"""
Functions used several times in the Project Euler solutions
"""

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

def ispandigital(n, s=9): n=str(n);return len(n)==s and not '1234567890'[:s].strip(n)
