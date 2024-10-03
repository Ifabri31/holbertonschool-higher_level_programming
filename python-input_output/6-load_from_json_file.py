#!/usr/bin/python3
"""
This file contains a function to load an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    This file create an object from a JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        objeto = json.load(f)
        return objeto
