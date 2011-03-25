#!/usr/bin/env python

def calc_next(n):
    result = 0
    for i in str(n):
        result += int(i)**2
    return result


def is_89(n):
#    print str(n) + ": ",
    for i in xrange(1,50):
        if i == 1:
            result = n
        result = calc_next(result)
#        print str(result) + " -> ",
        if result == 89:
#            print "" 
            return True
        if result == 1:
#            print ""
            return False
#    print ""
    return False


print sum([1 for i in xrange(1,10000000) if is_89(i)])
