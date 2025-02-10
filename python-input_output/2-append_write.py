#!/usr/bin/python3
"""
Module documented: 2-append_write.py
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'a') as file:
        return file.write(text)
