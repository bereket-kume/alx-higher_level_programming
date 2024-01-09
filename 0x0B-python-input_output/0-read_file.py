#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """read_file method"""

    with open(filename, encoding="UTF-8") as file:
        content = file.read()
        print(content, end="")
