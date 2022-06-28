#!/usr/bin/python3
"""Class that prevents user from dynamically creating new instance"""


class LockedClass:
    """__slots__ prevents new instance from being created"""

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """instantiation with first_name"""
        self.first_name = first_name
