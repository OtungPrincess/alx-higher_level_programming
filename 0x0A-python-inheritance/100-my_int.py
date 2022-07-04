#!/usr/bin/python3
"""This module have a class rebel"""


class MyInt(int):
    """Rebel class from int
    attribute of class value"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other) -> bool:
        """Method to compare =="""
        return int(self) != other

    def __ne__(self, other):
        """Method to compare =="""
        return int(self) == other
