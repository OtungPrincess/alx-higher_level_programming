#!/usr/bin/python3
"""function that inserts a line of text to a file,
    after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts "new_string" after a line containing
    "search_string" in "filename" """

    text = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
