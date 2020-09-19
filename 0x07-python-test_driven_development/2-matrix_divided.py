#!/usr/bin/python3
"""module"""


def matrix_divided(matrix, div):
    """function"""
    try:
        row_size = len(matrix[0])
    except IndexError:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    cont = 0
    new_mtx = []
    result = 0

    if type(div) is int or type(div) is float:
        if int(div) == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    for iter1 in matrix:
        if row_size == len(matrix[cont]):
            new = []
            for iter in iter1:
                if type(iter) is int or type(iter) is float:
                    result = round(iter / div, 2)
                    new.append(result)
#                    iter = iter / div
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            new_mtx.append(new)
        else:
            raise TypeError("Each row of the matrix must have the same size")
        cont += 1
    return new_mtx
