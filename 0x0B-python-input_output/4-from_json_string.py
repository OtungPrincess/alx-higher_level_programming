#!/usr/bin/python3
"""Function that returns JSON string representation"""


import json


def from_json_string(my_str):
    """ Returns JSON representation"""

    return json.loads(my_str)
