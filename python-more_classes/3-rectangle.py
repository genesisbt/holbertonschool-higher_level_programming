#!/usr/bin/python3
"""
This module contains the definition of the clas Rectangle
"""


class Rectangle:
    """
    Class to define a Rectangle
    """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else
        return ('\n'.join(("#" * self.width for a in range(self.height))))
    def __repr__(self):
        return f"Rectangle({self.width},{self.height})"
