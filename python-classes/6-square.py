#!/usr/bin/python3
"""
This module defines Square as a class.
"""


class Square:
    """
    This is a class where a square is defined.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, number):
        self.__size = number
        if not isinstance(number, int):
            raise TypeError("size must be an integer")
        elif number < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, postuple):
        if not isinstance(postuple, tuple) or \
            not isinstance(postuple[0], int) or \
                not isinstance(postuple[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif postuple[0] < 0 or postuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = postuple

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for posY in range(self.__position[1]):
                print()
            for unit in range(self.__size):
                for posX in range(self.__position[0]):
                    print(" ", end="")
                for unit2 in range(self.__size):
                    print("#", end="")
                print()
