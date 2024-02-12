#!/usr/bin/python3
"""
This module contains the base class for all geometric figures
"""


class Base:
    """
    Base class for all geometric figures
    Contains its atributes and functions
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
