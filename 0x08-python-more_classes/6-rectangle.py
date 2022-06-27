#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns a value to the private instance attribute width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns a value for the private instance attribute height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns a printable string representation of the rectangle"""
        rec_string = ""
        if self.__width != 0 and self.__height != 0:
            rec_string += "\n".join("#" * self.__width
                                    for j in range(self.__height))
        return rec_string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
