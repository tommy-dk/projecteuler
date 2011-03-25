#!/usr/bin/env python

"""
Python source code - describe the code here
"""

import time
st = time.time()

import sys
import re

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)

total = 0

def r(a):
    i = a.find('0')
    if i == -1: 
        global total
        total += int(a[:3])

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
        # At this point, m is not excluded by any row, column, or block, so let's place it and recurse
            r(a[:i]+m+a[i+1:])

sudoku = open("p96.txt").read().replace('\r\n','').split('Grid')

for s in sudoku:
    if len(s) == 0: continue
    r(s[3:])

print total
print "Time taken: %s" % str(time.time() - st)
