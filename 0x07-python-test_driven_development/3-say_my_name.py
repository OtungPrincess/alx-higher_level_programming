#!/usr/bin/python3
"""
Function that prints name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints "My name is <first name> <last name>" """
    if not type(first_name) is (str):
        raise TypeError("first_name must be a string")

    if not type(last_name) is (str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
