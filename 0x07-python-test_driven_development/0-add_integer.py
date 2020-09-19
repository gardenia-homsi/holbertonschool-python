#!/usr/bin/python3
"""this module contain one function that add 2 integers
Functions:def add_integer(a, b=98)
def add_integer(a) -> integer def add_integer(b=98) -> integer
return sum of a+b
"""


def add_integer(a, b=98):
    """Returns the sum of two integer numbers in binary digits.
      Returns:
      binary_sum (str): Binary string of the sum of a and b"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(a, float):
        b = int(b)

    return a + b
