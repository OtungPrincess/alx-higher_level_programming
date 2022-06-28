#!/usr/bin/python3
"""
Print a text with 2 new lines after
each of these characters
. ? :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    """
    flag = 0

    if type(text) != (str):
        raise TypeError("text must be a string")

    for n in text:
        if n == ' ' and flag is True:
            continue
        if n in ['.', '?', ':']:
            print(n, end="")
            print()
            print()
            flag = True
        else:
            print(n, end="")
            flag = False
