#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = matrix
    result = result = list(map(list, map(map(square), newmatrix))) 
    def square(number):
        number = number * number
    return number
