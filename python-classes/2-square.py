#!/usr/bin/python3
'''Class that defines a square'''


class Square:
    """
    Class for defining a Square and its atributes
    Attributes:
    __size (int): Private attribute
    """
    def __init__(self, size):
        """
        Initializes a new Instance of the Class Square

        Args:
            size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
