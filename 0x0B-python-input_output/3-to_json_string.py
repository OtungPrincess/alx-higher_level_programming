#!/usr/bin/python3
"""This module return JSON representation"""


import json


def to_json_string(my_obj):
    """Returns JSON representation of an object"""

    return json.dumps(my_obj)
