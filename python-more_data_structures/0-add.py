#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = result = list(map(list, map(map(square), matrix)))
    
    def square(number):
        number = number * number
    return number
