#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Class rectangle that defines a rectangle based on 0-rectangle.py"""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Retrieves the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns a value to the private instance attribute height"""
        self.__height = value
        if not type(value) is (int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """Retrieves the Private instance attributte: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns a value for the private instance attribute width"""
        self.__width = value
        if not type(value) is (int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.width * self.__height

    def perimeter(self):
        """calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns printable string representation of a Rectangle"""

        rec_string = ""
        if self.__width != 0 and self.__height != 0:
            rec_string += "\n".join("#" * self.__width
                                    for j in range(self.__height))
        return rec_string

    def __repr__(self):
        """Returns a String with a representation of the state of the object"""

        return f"Rectangle({self.__width}, {self.__height})"
