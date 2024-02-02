#!/usr/bin/python3
"""
Module for dividing a matrix.
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints "my name is <first_name> <last_name>"

    Args:
        first_name (string): not default
        last_name (string): default empty ""

    Returns:
        nothing just prints
    Raises:
        TypeError: first_name must be string
        TypeError: last_name must be string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
