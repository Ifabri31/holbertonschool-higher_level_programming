#!/usr/bin/python3
"""
Module documented: 0-read_file.py
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end="")
