#!/usr/bin/python3
"""class Student that defines a student by
    firstname, lastname age
"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """instantiation of student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
