#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:

    """initializes the data."""
    def __init__(self, size=0):
        """assigns private instance attribute."""
        self.size = size

    @property
    def size(self):
        """retrives the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size to an integer value."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """assigns private instance attribute."""
        self.__size = size

    def area(self):
        """returns current square area"""
        return self.__size * self.__size
