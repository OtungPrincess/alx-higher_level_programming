#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:

    """Init allows the data to be used."""
    def __init__(self, size=0):
        """asign private instance attribute size"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """asign private instance attribute value"""
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints to stdout the square with the character #."""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            print("#" * self.__size)
