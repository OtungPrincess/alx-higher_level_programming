#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.
    """
    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
