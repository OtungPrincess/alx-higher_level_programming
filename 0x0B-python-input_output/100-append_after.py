#!/usr/bin/python3
"""function that inserts a line of text to a file,
    after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts "new_string" after a line containing
    "search_string" in "filename" """

    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()

    with open(filename, "w", encoding="utf-8") as f:
        for n in range(len(line)):
            if search_string in line[n]:
                line[n] += new_string
        f.writeline(line)
