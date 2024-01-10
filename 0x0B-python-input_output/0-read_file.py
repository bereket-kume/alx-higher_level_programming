#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """read_file method"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
