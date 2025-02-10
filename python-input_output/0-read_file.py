#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
