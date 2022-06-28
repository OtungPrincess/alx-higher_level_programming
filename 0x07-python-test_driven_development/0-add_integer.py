#!/usr/bin/python3
"""
Adds two integer
"""


def add_integer(a, b=98):
    """
       calculates and returns The addition of the two given numbers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not type(a) in (int, float):
        raise TypeError('a must be an integer')

    if not type(b) in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
