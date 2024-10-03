#!/usr/bin/python3
"""
This file opens a file and writes text to it
"""


def write_file(filename="", text=""):
    """
    Function that writes text to a file and
    returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
