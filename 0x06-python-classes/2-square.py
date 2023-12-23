#!/usr/bin/python3
"""
class that define square
"""


class Square:
    """
    Defines a square class
    """
    def __init__(self, size=0):
        """
         Initializes a Square instance
         Args:
            size (int): The size of the square
        """
        self.__size = size
      if not isinstance(int, size):
         raise TypeError("size must be an integer")
      if size < 0:
        raise TypeError("size must be >= 0")
