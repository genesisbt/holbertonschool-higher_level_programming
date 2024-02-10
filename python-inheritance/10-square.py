#!/usr/bin/python3
"""
module for class rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines Class Rectangle, subclass of BaseGeometry
    """
    def __init__(self, sidesize):
        self.integer_validator("sidesize", sidesize)
        self.__sidesize = sidesize

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__sidesize, self.__sidesize)

    def area(self):
        return self.__sidesize ** 2
