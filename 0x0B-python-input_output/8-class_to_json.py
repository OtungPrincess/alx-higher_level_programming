#!/usr/bin/python3
"""function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """return dict description of the object"""
    obj_json = obj.__dict__
    return obj_json
