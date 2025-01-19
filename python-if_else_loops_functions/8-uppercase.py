#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = ord(letter) - 32
            letter = chr(letter)
        print("{0}".format(letter), end='')
    print()
