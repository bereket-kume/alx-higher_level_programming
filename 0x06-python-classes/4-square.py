#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    This class represents a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square (default 0)
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
     @property
     def size(self):
       """
       getter method
       """
       return self.__size
    @size.setter
    def size(self, value):
      """
      setter method
      """
      self.__size = value
      if not isinstance(size, int):
        raise TypeError("size must be an integer")
      if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
