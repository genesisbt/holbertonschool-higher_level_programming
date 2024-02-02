#!/usr/bin/python3
"""
Module for dividing a matrix.
"""


def matrix_divided(matrix, div):
    """
    Receives a matrix and a divisor.

    Args:
        matrix (list of lists of integers or floats):
        the matrix to divide, no default
        div (integer or float): divisor, no default

    Returns:
        New Matrix
    Raises:
        TypeError: if rows in matrix arent same size
        TypeError: if matrix isnt a list of list of integers amd/or floats
        TypeError: if div isnt integer or float
        ZeroDivisionError: if div = 0
    """
    sublength = len(matrix[0])
    newmatrix = []
    for sublist in matrix:
        if not isinstance(div, (float, int)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if len(sublist) != sublength:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for number in sublist:
            if not isinstance(number, (float, int)):
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
            numtemp = round((number / div), 2)
            newlist.append(int(numtemp) if numtemp % 1 == 0 else numtemp)
        newmatrix.append(newlist)
    return newmatrix
