#!/usr/bin/env python

import time
st = time.time()

chars = dict(zip(('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'), range(1,27)))

names = open('p22.txt').read().replace('"','').split(',')
names.sort()

result,line = 0,1
for name in names:
    name = str(name).lower()
    delta = 0
    for char in str(name):
        delta += chars.get(char)
    result += delta * line
    line += 1

print result

# one liner
print sum((i+1)*sum(ord(c)-64 for c in list(n)) for i,n in enumerate(sorted(eval('['+open('p22.txt').read()+']'))))

print "Time taken: %s" % str(time.time() - st)
