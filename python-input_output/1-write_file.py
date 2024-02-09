#!/usr/bin/python3
"""
module to define write_file function
"""


def write_file(filename="", text=""):
    """
    function to write a string to a file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
