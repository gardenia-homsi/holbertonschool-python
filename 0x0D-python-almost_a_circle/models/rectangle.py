#!/usr/bin/python3
""" Rectangle class inheris from Base class
    class to create Rectangles
"""
from models.base import Base


class Rectangle(Base):
    """ Definition of own methods and attributes """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor with private attributes and its validations """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ Returns the area of rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the rectangle acording to parameters """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """ It allows don´t have a fixed number of arguments """
        if args:
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 1:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with every attribute of the
            Rectangle class
        """
        dic_rec = {"x": self.x, "y": self.y, "id": self.id,
                   "height": self.height, "width": self.width}
        return dic_rec

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def __str__(self):
        '''Method that returns string representation of rectangle '''
        a, d, e = self.id, self.width, self.height
        b, c = self.x, self.y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))
