#!/usr/bin/python3
"""
Defines a function read_file
"""


def read_file(filename=""):
    """
    Function for printing a file content as String
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
