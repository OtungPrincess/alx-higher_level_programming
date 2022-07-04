#!/usr/bin/python3
"""This module contains the class BaseGeometry and subclass Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle"""

    def __init__(self, width, height):
        """Init method"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
