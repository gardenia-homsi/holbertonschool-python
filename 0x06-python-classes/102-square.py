#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


class Square:
    """This class has private size attribute with exceptions."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This function return the area of square."""
        return self.__size * self.__size
        
    def __lt__(self, other):
        # return comparison x<y
        if not isinstance(other, Square):
            pass
        if self.area < other.area:
            return True
        else:
            return False

    def __le__(self, other):
        # return comparison x<=y
        if not isinstance(other, Square):
            pass
        if self.area <= other.area:
            return True
        else:
            return False

    def __eq__(self, other):
        # return comparison x==y
        if not isinstance(other, Square):
            pass
        if self.area == other.area:
            return True
        else:
                return False

    def __ne__(self, other):
        # return comparison x!=y
        if not isinstance(other, Square):
            pass
        if self.area != other.area:
            return True
        else:
            return False

    def __gt__(self, other):
        # return comparison x>y
        if not isinstance(other, Square):
            pass
        if self.area > other.area:
            return True
        else:
            return False

    def __ge__(self, other):
        # return comparison x>=y
        if not isinstance(other, Square):
            pass
        if self.area >= other.area:
            return True
        else:
            return False
