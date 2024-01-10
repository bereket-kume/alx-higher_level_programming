#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write_file method"""

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
