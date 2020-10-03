#!/usr/bin/python3
"""contain class BaseGeometry"""


class BaseGeometry:
    """contain 2 functions"""
    def area(self):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check value if integer type"""
        self.name = name
        self.value = value

        if type(self.value) not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
