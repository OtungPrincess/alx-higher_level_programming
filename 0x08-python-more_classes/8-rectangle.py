#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle based on 7-rectangle.py"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle """

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self, value):
        """Retrieves the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns a value for the private instance attribute height"""
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
        """Assigns a value for the private instance attribute width"""
        self.__width = value
        if not type(value) is (int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    def area(self):
        """Calculates and returns the area of the Rectangle"""
        return self.width * self.__height

    def perimeter(self):
        """Calculates and Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns string representation of a Rectangle"""

        if self.width == 0 or self.__height == 0:
            return ""
        new_string = ""
        new_string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return new_string

    def __repr__(self):
        """Returns a String with a representation of the state of the object"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the bigger rectangle"""
        if not type(rect_1) is Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not type(rect_2) is Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
