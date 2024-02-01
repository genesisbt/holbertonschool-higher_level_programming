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
        Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
