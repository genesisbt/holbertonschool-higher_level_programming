#!/usr/bin/python3
'''Class that defines a square'''


class Square:
    """ Class for defining a Square and its atributes """

    def __init__(self, size):
        """ Initializes a new Instance of the Class Square """

        if type(size) is not int:
            raise TypeError("size must be an integer")
            size = 0
        elif size < 0:
            raise ValueError("size must be >=0")
            size = 0
        self.__size = size
