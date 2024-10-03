#!/usr/bin/python3
"""
This file writes an object in a text file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file in JSON format.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
