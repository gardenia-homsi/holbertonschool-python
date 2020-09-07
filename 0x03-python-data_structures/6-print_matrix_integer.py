#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if len(matrix) == 1 and any(matrix) is False:
        print()

    for row in matrix:
        c = 0
        for col in row:
            if c == (len(row) - 1):
                print("{:d}".format(col), end="")
                print()
            else:
                print("{:d}".format(col), end=" ")
            c += 1
