#!/usr/bin/env python

"""
Python source code - describe the code here
"""

import time
s = time.time()
def distinct(seq, idfun=None): 
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

terms = []
for a in xrange(2,101):
    for b in xrange(2,101):
        terms += [a**b]

print len(distinct(terms))
print time.time() - s

# 2nd solution
l = []
for a in range(2,101):
    for b in range (2,101):
        c = a**b
        if c not in l:
            l.append(c)
print len(l)
print time.time() - s

# 3rd solution
# one liner
print len(set(a**b for a in range(2, 101) for b in range(2, 101)))
print time.time() - s

