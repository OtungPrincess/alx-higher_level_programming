#!/usr/bin/python3
""" A function that Finds if an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """Returns: True if obj is an instance of a_class,
    False otherwise"""
    if type(obj) is a_class:
        return True
    return False
