#!/usr/bin/python3
"""
Module to append_write function
"""


def append_write(filename="", text=""):
    """
    function to append a string at the eof
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
