#!/usr/bin/env python

words_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelwe", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
words_decades = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]


result = ""
for i in xrange(1,1001):
    if i < 20:
        result += words_numbers[i-1] + ", "
    if i >= 20 and i < 100:
        pstr = str(i)
        if not i % 10 == 0:
            result += words_decades[int(pstr[0])-1] + words_numbers[int(pstr[1])-1] + ", "
        else:
            result += words_decades[int(pstr[0])-1] + ", "
    if i >= 100 and i < 199:
        pstr = str(i)
        if i % 100 == 0:
            result += words_numbers[int(pstr[0])-1] + " hundred, "
        else:
            result += words_numbers[int(pstr[0])-1] + " hundred and " + words_decades[int(pstr[1])-1] + words_numbers[int(pstr[2])-1] + ", "

print result
