#!/usr/bin/env python

words_numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelwe", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
words_decades = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
words_centuries = ["", "ten", "hundred", "thousand", "million"]

def count_letters(word):
    exclude = " ,-"
    return len(filter(lambda x: x not in exclude, word))

def number_to_letter(number):
    if number == 0:
        return ""
    length = len(str(number))
    integers = map(int, str(number))
    if length == 4:
        if int(str(number)[1:]) == 0:
            return words_numbers[integers[0]] + " " + words_centuries[length-1]
        elif int(str(number)[1:]) >= 1 and int(str(number)[1:]) <= 99:
            return words_numbers[integers[0]] + " " + words_centuries[length-1] + " and " + number_to_letter(int(str(number)[1:]))
        else:
            return words_numbers[integers[0]] + " " + words_centuries[length-1] + " " + number_to_letter(int(str(number)[1:]))
    if length == 3:
        if int(str(number)[1:]) >= 1:
            return words_numbers[integers[0]] + " " + words_centuries[length-1] + " and " + number_to_letter(int(str(number)[1:]))
        else:
            return words_numbers[integers[0]] + " " + words_centuries[length-1]
    if length == 2:
        if number < 20:
            return words_numbers[number]
        if number >= 20:
            if integers[1] == 0:
                return words_decades[integers[0]]
            else:
                return words_decades[integers[0]] + "-" + words_numbers[integers[1]]
    if length == 1:
        return words_numbers[number]

result=0
for i in xrange(1,1001):
#    print str(i) + ": " + number_to_letter(i)
    result += count_letters(number_to_letter(i))
print result

#print number_to_letter(2110)
#print number_to_letter(2010)
#print number_to_letter(2000)
#print number_to_letter(201)

# 21124
