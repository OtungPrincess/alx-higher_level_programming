#!/usr/bin/python3
"""
function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the obj inherited, false if otherwise"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
