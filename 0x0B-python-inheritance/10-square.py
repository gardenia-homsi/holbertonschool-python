#!/usr/bin/python3
"""contain class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inheret from Rectangle"""
    def __init__(self, size):
        """function"""
        super().__init__(size, size)
        self.__size = size
