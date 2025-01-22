#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for x in range(len(roman_string)):
        current = dict_roman[roman_string[x]]
        if x+1 < len(roman_string) and dict_roman[roman_string[x+1]] > current:
            total -= current
        else:
            total += current
    return total
