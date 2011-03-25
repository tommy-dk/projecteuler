#!/usr/bin/env python

import math

# See formulae here: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html?n=20
def getfibdigits(n):
    phi = (1+math.sqrt(5))/2
    return n * math.log10(phi) - math.log10(math.sqrt(5))

i = 1
while True:
    if getfibdigits(i) >= 999:
        print i
        break
    i += 1

# keeps in a list
f=[1,2]
while len(str(f[-1]))<1000:
    f.append(f[-1]+f[-2])
    print len(f)+1

