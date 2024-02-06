#!/usr/bin/python3
"""
This module contains the definition of the clas Rectangle
"""


class Rectangle:
    """
    Class to define a Rectangle
    """


    def __init__(self width=0, height=0):
        height(self, height)
        width(self, width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        else
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        elif value < 0:
            raise ValueError("heigth must be an integer")
        else
        self.__height = value
