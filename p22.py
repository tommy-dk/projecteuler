#!/usr/bin/env python

chars = dict(zip(('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'), (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)))

#for line in open('p22.txt'):
#    names = line.split(',')

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
