#!/usr/bin/python3
'''Class that defines a square'''


class Square:
    """
    Class name

    Atributes:
        size (int): private atribute
    """

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
