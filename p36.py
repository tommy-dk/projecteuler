#!/usr/bin/env python

def ispalindrome(x):
    string = str(x)
    string = string.lstrip('-0b')
    if string == string[::-1]:
        return True
    else:
        return False

result = 0

for i in range(1,1000000):
    if ispalindrome(i) and ispalindrome(bin(i)):
        result += i

print result
