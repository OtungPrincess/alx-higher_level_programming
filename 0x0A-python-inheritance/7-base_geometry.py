#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry with public methods"""

    def area(self):
        """public method, raises exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
