#!/usr/bin/python3
"""
Imprime un cuadrado segun el tamaño que se le pase
"""


def print_square(size):
    """
    imprime un cuadrado corroborando que size sea del tipo solicitado
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for a in range(size):
        print("#" * size)
