#!/usr/bin/python3
"""Function that write and overwrite a string to a text file"""


def write_file(filename="", text=""):
    """Use UTF8 and with to write string"""

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
