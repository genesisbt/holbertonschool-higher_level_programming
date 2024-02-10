#!/usr/bin/python3
"""
module for inherits from function
"""


def inherits_from(obj, a_class):
    """
    checks if object is a subclass only
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
