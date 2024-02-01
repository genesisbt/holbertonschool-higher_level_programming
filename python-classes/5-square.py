#!/usr/bin/python3
"""
This module defines Square as a class.
"""


class Square:
    """
    This is a class where a square is defined.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, number):
        self.__size = number
        if not isinstance(number, int):
            raise TypeError("size must be an integer")
        elif number < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for unit in range(self.__size):
            for unit2 in range(self.__size):
                print("#", end="")
            print()
