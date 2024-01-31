#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = [row[:] for row in matrix]
    n = len(matrix)
    for i in range(n):
        m = len(matrix[i])
        for j in range(m):
            newmatrix[i][j] = matrix[i][j] ** 2
    return newmatrix
