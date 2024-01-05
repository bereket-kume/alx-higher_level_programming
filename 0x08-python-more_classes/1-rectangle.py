#!/usr/bin/python3
"""
this moduale contain Reactangle class
"""


class Rectangle:
    """ define Reactangle class """
    def __init__(self, width=0, height=0):
        """ intialize a Rectangle instance"""
        self.__width = width
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
