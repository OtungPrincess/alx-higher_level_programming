#!/usr/bin/python3
"A class Square that defines a square"


class Square:
    "init allows data of square class to be used"
    def __init__(self, size=0):
        "asign private instance attribute size"
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
