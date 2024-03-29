#!/usr/bin/python3
"""
This module defines Square as a class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
    __size (int): The size of the square.
    __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): The size of the square.
        position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
        value (int): The new size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
        value (tuple): The new position of the square.

        Raises:
        TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or not \
                all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a \
                tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints a representation of the square.
        """
        if self.__size == 0:
            print()
        else:
            for posY in range(self.__position[1]):
                print()
            for unit in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
