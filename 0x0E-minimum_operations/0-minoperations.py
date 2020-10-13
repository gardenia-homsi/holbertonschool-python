#!/usr/bin/python3
"""model minoperation"""


def minOperations(n):
    """return min operation"""
    min_operation = 0
    div = 2
    if n <= 1:
        return 0
    while div < n:
        if n % 3 == 0:
            min_operation = n / 3 + 3
            return min_operation
        elif n % 5 == 0:
            min_operation = n / 5 + 5
            return min_operation
        elif n % div == 0:
            min_operation = n / div + div
            return min_operation
        else:
            div += 1
    return n
