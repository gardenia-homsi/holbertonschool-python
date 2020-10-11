#!/usr/bin/python3
""" this model contain Rectangle class """


class Rectangle(Base):
    """this calss contain one __init__ function with 4 private atribut"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this function define 4 private attribute and one public defiened by s
        uper class"""
        __width = width
        __height = height
        __x = x
        __y = y
        id = super().id

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def display(self):
        for h in range(0, x):
            print(" ")
        for v in range(0, y):
            print()
        for i in range(0, height):
            for j in range(0, width):
                print("#", end="")
            print()

    def area(self):
        """ return thr area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """overriding the str method"""
        return ("[Rectangle](self.id) self.__x/self.__y - self.__width/self.__h
        eight")

    def update(self, *args, **kwargs):
        if args not None and args != []:
            if len(args) == 5:
                self.__id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            if len(args) == 4:
                self.__id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 3:
                self.__id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 2:
                self.__id = args[0]
                self.__width = args[1]
            if len(args) == 1:
                self.__id = args[0]
        else:
            for key, value in kwargs.iteritems():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
