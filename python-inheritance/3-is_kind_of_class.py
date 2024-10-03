#!/usr/bin/python3
"""
This file defines a function to check if an object is an instance
of a specified class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a_class
    or an instance of a subclass of a_class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
