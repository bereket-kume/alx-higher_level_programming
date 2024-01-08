#!/usr/bin/python3
"""
module for mylist
"""


class MyList(list):
    """class with sort method"""

    def print_sorted(self):
        """sort method"""
        print(sorted(list(self)))
