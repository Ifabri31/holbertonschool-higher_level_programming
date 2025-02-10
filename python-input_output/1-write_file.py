#!/usr/bin/python3
"""
Module documented: 1-write_file.py
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w') as file:
        return file.write(text)
