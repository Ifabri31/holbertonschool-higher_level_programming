#!/usr/bin/python3
def no_c(my_string):
    string2 = ""
    for a in my_string:
        if a != 'c' and a != 'C':
            string2 += a
    return string2
