#!/usr/bin/python3
"""module for 9-student.py"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """intialize method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json method"""

        return self.__dict__
