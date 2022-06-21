#!/usr/bin/python3
"""A class that defines a square and can compute area"""


class Square:
    """A class that defines a square
    Instantiation with optional size.
    """

    def __init__(self, size=0):
        """Init allows data of square class to be used."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """assign private instance attribute size."""
        self.__size = size

    """public instance method."""
    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
