#!/usr/bin/python3
"""This module have a two classes BaseGeometry
and Rectangle that inherist from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle
    """

    def __init__(self, width, height):
        """Init method"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Publuc methos, calculate and returns the area"""
        return self.__height * self.__width

    def __str__(self) -> str:
        """Returns a formatted string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
