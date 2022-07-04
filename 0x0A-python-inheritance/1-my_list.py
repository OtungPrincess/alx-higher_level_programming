#!/usr/bin/python3
"""A Class: Mylist
that inherist from list
"""


class MyList(list):
    """This class sorted the list"""

    def print_sorted(self):
        """Use sorted to sort the list"""
        print(sorted(self))
