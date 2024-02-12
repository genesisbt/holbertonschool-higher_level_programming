#!/usr/bin/python3
"""
This module contains the class Rectangle
which inherits from class Base
"""
from base import Base


class Rectangle(Base):
    """
    Class Rectangle contains definition of the geometric figure Rectangle
    including its functions and its atributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer".format(width))
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y
