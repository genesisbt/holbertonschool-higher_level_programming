#!/usr/bin/python3
"""
This module contains the class Rectangle
which inherits from class Base
"""
from .base import Base


class Rectangle(Base):
    """
    Class Rectangle contains definition of the geometric figure Rectangle
    including its functions and its atributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class base constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """position x getter"""
        return self.__x

    @property
    def y(self):
        """position y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter and validation"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer".format(width))
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height setter and validation"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """position x setter and validation"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be = 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """position y setter and validation"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """calculates the area and returns the result"""
        return self.height * self.width

    def display(self):
        """ prints the Rectangle height * width using "#" on screen"""
        for n1 in range(self.height):
            print("".join("#" for n2 in range(self.width)))
