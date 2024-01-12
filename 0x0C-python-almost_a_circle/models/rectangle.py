#!/usr/bin/python3
"""module for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @proprety
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
    
    @proprety
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        self.__height = value

    @proprety
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @proprety
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
