#!/usr/bin/python3
"""module for the function"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as my_file:
        """appenf_write method"""

        my_file.write(text)
        return len(text)
