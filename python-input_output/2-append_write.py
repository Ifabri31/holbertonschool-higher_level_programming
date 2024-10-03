#!/usr/bin/python3
"""
This file opens a file and appends a string to it.
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a
    file and returns the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
