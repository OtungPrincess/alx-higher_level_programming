#!/usr/bin/python3
"""
Creates square class and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """initialization of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"computes the area of the square"""
        return self.__size ** 2
