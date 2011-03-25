#!/usr/bin/env python

def fibonacci(n):
    a, b = 0, 1
    res = 0
    while a < n:
        a, b = b, a+b
        if a % 2 == 0:
            res += a

    return res

print fibonacci(4000000)
