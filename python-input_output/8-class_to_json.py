#!/usr/bin/python3

"""
This file contains a function to return dict
"""


def class_to_json(obj):
    """
    This function return a dictionary description with simple data structure
    """
    dictionary = {}
    dictionary = obj.__dict__
    return dictionary
