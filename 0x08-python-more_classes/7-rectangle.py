#!/usr/bin/python3
"""Defines a classs Rectangle"""


class Rectangle:
    """Class that defines a rectangle based on 6-rectangle.py"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle """

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Retrieves the private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns a value for the height of the rectangle"""
        self.__height = value
        if not type(value) is (int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """Private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns a value for the width of the rectangle"""
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
        """Returns a printable string representation of a Rectangle"""

        if self.width == 0 or self.__height == 0:
            return ""

        length = list()
        for i in range(self.__height):
            for j in range(self.__width):
                length.append(str(self.print_symbol))
            if i + 1 != self.__height:
                length.append('\n')
        return ''.join(length)

    def __repr__(self):
        """Returns a String with a representation of the state of the object"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
