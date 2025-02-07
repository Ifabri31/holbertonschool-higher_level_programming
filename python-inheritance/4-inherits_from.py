#!/usr/bin/python3
"""
Module documented: 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a
    class that inherited from a class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
