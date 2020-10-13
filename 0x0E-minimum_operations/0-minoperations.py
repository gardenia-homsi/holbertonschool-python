#!/usr/bin/python3
"""model minoperation"""


def minOperations(n):
    """return min operation"""
    min_operation = 0
    if n <= 1:
        return 0
    elif n % 2 == 0 and n % 3 != 0:
        min_operation = n/2 + 2
        return min_operation
    elif n % 3 == 0 and n % 5 != 0:
        min_operation = int(n/3) + 3
        return min_operation
    elif n % 5 == 0:
        min_operation = n / 5 + 5
        return min_operation
    else:
        return n
