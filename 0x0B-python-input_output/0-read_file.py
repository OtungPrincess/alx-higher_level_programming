#!/usr/bin/python3
"""Function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """read a file with, with and UTF8"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
