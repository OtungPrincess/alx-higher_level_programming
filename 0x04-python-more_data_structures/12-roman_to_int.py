#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    rep = 0
    rf = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numb = len(roman_string)
    for i in range(len(roman_string)):
        if i != numb - 1 and (rf[roman_string[i + 1]] > rf[roman_string[i]]):
            rep -= rf[roman_string[i]]
        else:
            rep += rf[roman_string[i]]
    return rep
