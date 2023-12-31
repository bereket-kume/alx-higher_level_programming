#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    This class represents a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square (default 0)
        """
        self.__size = size
        self.position = position
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
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """
        my_print method
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
    @property
    def position(self):
        """getter method"""
        return self.__postion
    @position.setter
    def position(self, value):
        """setter method"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

