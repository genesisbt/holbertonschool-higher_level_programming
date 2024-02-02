#!/usr/bin/python3
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
    Receives two integers or float,
    casts them as int, and adds them, returns an int.

    Args:
        a (int or float): First number, no default
        b (int or float): Second number, defaullt 98

    Returns:
        The add of a and b.
    Raises:
        TypeError: if a or b are integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b
