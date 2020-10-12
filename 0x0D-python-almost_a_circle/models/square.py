#!/usr/bin/python3
"""this model contain square class that inheret from rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inheret from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, size, size, x, y, id)

    def __str__(self):
        return("[Square] (self.id) self.x/self.y - self.size")

    @property
    def size(self):
        """size getter"""
        retrurn self.size

    @size.setter
    def size(self, value):
        """setter for size"""
        super().width(self, value)

    def update(self, *args, **kwargs):
        """ It allows don´t have a fixed number of arguments """
        if args:
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 1:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary rep"""
        dictionary = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.
        y}
        return(dictionary)
