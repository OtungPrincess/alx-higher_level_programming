#!/usr/bin/python3
"""This module create an object from a JSON file"""


import json


def load_from_json_file(filename):
    """create object with JSON file"""

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
