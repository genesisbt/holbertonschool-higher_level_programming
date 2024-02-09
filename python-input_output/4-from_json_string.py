#!/usr/bin/python3
"""
module for from_json_string function
"""
import json


def from_json_string(my_str):
    """
    function returns a python data structure from a json string
    """
    return json.loads(my_str)
