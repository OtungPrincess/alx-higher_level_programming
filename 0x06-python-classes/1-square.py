#!/usr/bin/python3
"""A class Square that defines a square
   assigns Private instance attribute: size
    Instantiation with size (no type/value verification)
"""


class Square:
    "init allows square class data to be used"
    def __init__(self, size):
        self.__size = size
