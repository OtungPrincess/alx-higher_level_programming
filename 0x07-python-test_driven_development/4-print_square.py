#!/usr/bin/python3
"""
Function that prints a square with #
"""


def print_square(size):
    """
    Function that prints a square
    """

    if not type(size) is (int) or type(size) == float:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size > 0:
        print(("#" * size + "\n") * size, end="")
