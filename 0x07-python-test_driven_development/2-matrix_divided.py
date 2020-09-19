#!/usr/bin/python3
"""module"""


def matrix_divided(matrix, div):
    """funct"""
    new-matrix = []
    if type(div) is int or type(div) is float:
        if int(div) == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    for i in range(len(matrix)):
        if len(matrix(i)) != len(matrix(i) + 1):
            rasie TypeError("Each row of the matrix must have the same size")
        else:
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not int or type(matrix[i][j]) not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                new-matrix[i][j] = round(matrix [i][j] / div, 2)
    return new-matrix
