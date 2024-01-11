#!/usr/bin/python3
"""module for 3-say_my_name.py"""


def say_my_name(first_name, last_name=""):
    """say my name method"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if last_name and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My Name is {:s} {:s}".format(first_name, last_name))
    else:
        print("My Name is {:s}".format(first_name))
