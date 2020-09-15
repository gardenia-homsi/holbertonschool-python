#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


class Square:
    """This class has private size attribute with exceptions."""
    def __init__(self, size=0):
        self.__size = size

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @preperty
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if self.__position[0] < 0 and self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[0]) != int and type(self.__position[1]) != in
        t:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
       
    def area(self):
        """This function return the area of square."""
        return self.__size * self.__size

    def my_print(self):
        for n in range(self.__position[1]):
            print()
        
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="") 
                for j in range(0, self.__size):
                    print("#", end="")
                print()
