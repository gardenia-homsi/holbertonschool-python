#!/usr/bin/python3
"""module"""


def matrix_divided(matrix, div):
    """funct"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not int or type(matrix[i][j]) not float:
                raise TypeError
