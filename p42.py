#!/usr/bin/env python

"""
"""

import time
st = time.time()

chars = dict(zip(('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'), range(1,27)))

def triangle(n): return int(0.5 * n * (n+1))
triangle_numbers = dict([(triangle(n), 1) for n in xrange(1,100)])

words = open('p42.txt').read().replace('"','').split(',')

triangle_words = 0
for word in words:
    delta = 0
    for char in str(word.lower()):
        delta += chars.get(char)
    if delta in triangle_numbers:
        triangle_words += 1

print triangle_words

# one liner
print len([num for num in [sum([ord(letter) - 64 for letter in list(word)]) for word in open('p42.txt', 'r').readline().replace('\"', '').split(',')] if num in [0.5 * n * (n + 1) for n in range(500)]])

print "Time taken: %s" % str(time.time() - st)

