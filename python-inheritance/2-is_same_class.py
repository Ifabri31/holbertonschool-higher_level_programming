#!/usr/bin/python3
"""
This file defines a function to check if an object is an instance
of a specific class.
"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is exactly an instance of
    the specified class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
