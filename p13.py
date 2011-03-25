#!/usr/bin/env python

result = 0
for c in open('p13.txt'):
    result += int(c)

print str(result)[:10]

print str(sum(int(x) for x in open('p13.txt')))[:10]
