#!/usr/bin/python3
"""
Creates an Object from JSON file
"""


import json


def load_from_json_file(filename):
    """create an object from filename.
    Args:
        - filename: JSON file
    Returns: object
    """

    with open(filename, 'r') as f:
        return json.load(f)
