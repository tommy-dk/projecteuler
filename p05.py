#!/usr/bin/env python

set_max = 20L
l = range (set_max/2 + 1, set_max+1)
start = set_max


while True:
    checked_all_divs = True
    for i in l:
        if start % i:
            checked_all_divs = False
            break
    if (checked_all_divs):
        print start
        break
    else:
        start += set_max
