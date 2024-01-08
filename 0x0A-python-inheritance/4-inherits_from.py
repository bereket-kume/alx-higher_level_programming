#!/usr/bin/python3
"""module for inherits"""


def inherits_from(obj, a_class):
    """inherits_from method"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
