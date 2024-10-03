#!/usr/bin/python3
"""
This file defines a function to check class inheritance.
"""


def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a class
    that inherits (directly or indirectly) from the specified class.
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
