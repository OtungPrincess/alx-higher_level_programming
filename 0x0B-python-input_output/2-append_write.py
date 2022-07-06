#!/usr/bin/python3
"""Function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Use UTF8 and with to append string"""

    with open(filename, mode="a+", encoding="utf-8") as file:
        return file.write(text)
