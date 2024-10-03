#!/usr/bin/python3
"""
This file contains a module JSON
"""
import json


def from_json_string(my_str):
    """
    This function return an object represent in a JSON
    """
    return json.loads(my_str)
