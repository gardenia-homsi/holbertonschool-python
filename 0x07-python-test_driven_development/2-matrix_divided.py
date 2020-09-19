#!/usr/bin/python3
"""module"""


def matrix_divided(matrix, div):
    """funct"""
    i = 0
    new-matrix = []
    if type(div) is int or type(div) is float:
        if int(div) == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    for row in matrix:
        if row-size != len(matrix[i]):
            rasie TypeError("Each row of the matrix must have the same size")
        else:
            for cell in row:
                if type(cell) not int or type(cell) not float:
                    raise TypeError("matrix must be a matrix (list of lists) of 
                    integers/floats")
                result = round(cell / div, 2)
                new-matrix.append(result)
        i += 1
    return new-matrix
