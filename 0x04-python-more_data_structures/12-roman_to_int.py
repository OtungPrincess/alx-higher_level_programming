#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    rep = 0
    rom_figs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i != len(roman_string) - 1 and (rom_figs[roman_string[i + 1]] > rom_figs[roman_string[i]]):
            rep -= rom_figs[roman_string[i]]
        else:
            rep += rom_figs[roman_string[i]]
    return rep
