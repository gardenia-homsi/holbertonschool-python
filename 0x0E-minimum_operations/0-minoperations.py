#!/usr/bin/python3
"""model minoperation"""


def minOperations(n):
    """return min operation"""
    if n <= 1:
        return 0
    nb = n
    div = 2
    min_operation = 0
    while nb > 1:
        if nb % div == 0:
            nb = nb / div
            min_operation += div
        else:
            div += 1
    return min_operation
