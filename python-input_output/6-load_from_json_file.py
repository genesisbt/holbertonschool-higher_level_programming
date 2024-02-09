#!/usr/bin/python3
"""
module for load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    makes a json object from the json string representation in a file
    """
    with open(filename) as f:
        return json.loads(f.read())
