#!/usr/bin/python3
"""contain class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inheret from Rectangle"""
     def __init__(self, size):
        """initiate size"""
        super().__init__(size, size)
        self.__size = size
        super().integer_validator(self, "size", self.__size)

    def area(self):
        """Return the area"""
        return self.__size * self.__size
