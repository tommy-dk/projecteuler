#!/usr/bin/env python

def chain(n):
    length = 1
    while n > 1:
        # even
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        length += 1

    return length


res, number = 0, 0

for i in range(1,999999):
    length = chain(i)
    if length > res:
        res = length
        number = i


print 'The number: ' + str(number) + ' has the longest sequence: ' + str(length)
