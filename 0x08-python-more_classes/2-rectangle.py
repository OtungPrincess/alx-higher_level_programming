#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """Representation of a rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance attribute, height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns value to private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate and returns the perimeter of the rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
