#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


class Square:
    """This class has private size attribute with exceptions."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        if len(position) == 2:
            if type(position[0]) != int\
               or type(position[1]) != int or type(position) != tuple:
                raise TypeError("position must be a tuple of \
2 positive integers")
            if type(position[0]) is int and type(position[1]) is int:
                if int(position[0]) < 0 or int(position[1]) < 0:
                    raise TypeError("position must be a tuple of \
2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        """get size value."""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2:
            if value[0] < 0 or value[1] < 0 or type(value[0]) != int or\
               type(value[1]) != int or type(value) != tuple:
                raise TypeError("position must be a tuple of \
2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """set size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """set size value."""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return area."""
        return self.__size * self.__size

    def my_print(self):
        """print the square."""
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
