#!/usr/bin/python3
"""
module for is kind of class function
"""


def is_kind_of_class(obj, a_class):
    """
    checks if object belongs to a_class or is a subclass of it
    """
    return isinstance(obj, a_class)
