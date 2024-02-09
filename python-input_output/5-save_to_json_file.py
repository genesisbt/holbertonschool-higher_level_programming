#!/usr/bin/python3
"""
module for save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function to save json string representation into file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
