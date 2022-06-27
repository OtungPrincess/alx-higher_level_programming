#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class that defines a rectangle based on 4-rectangle.py"""

    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle """

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Retrieves the private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns a value to the private instance attribute: height"""
        self.__height = value
        if not type(value) is (int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """Private instance attributte: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns a value to the private instance attribute: width"""
        self.__width = value
        if not type(value) is (int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    def area(self):
        """calculates and Return the area of the Rectangle."""
        return self.width * self.__height

    def perimeter(self):
        """Calculates and Return the area of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns the printable string representation of a Rectangle"""

        if self.width == 0 or self.__height == 0:
            return ""

        rectangle = list()
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)

    def __repr__(self):
        """Returns a String with a representation of the reactangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance"""
        print('Bye rectangle...')
