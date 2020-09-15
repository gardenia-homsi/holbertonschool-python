#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


class Square:
    """This class has private size attribute with exceptions."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """set size value."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get position value."""
        return self.__position

    @position.setter
    def position(self, value):
        """set position value."""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This function return the area of square."""
        return self.__size * self.__size

    def my_print(self):
        """print."""
        if self.__size == 0:
            print()

        for k in range(self.position[1]):
            print()

        for i in range(self.__size):
            for h in range(self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
