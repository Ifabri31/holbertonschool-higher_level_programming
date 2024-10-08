#!/usr/bin/python3
"""
This file contains a function that returns available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object.
    """
    return dir(obj)
