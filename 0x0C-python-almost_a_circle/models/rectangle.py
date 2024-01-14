#!/usr/bin/python3
"""module for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value, False)
        self.__width = value
    
    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value
    def validation(self, name, value, eq=True):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise TypeError("{} must be > 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be >= 0".format(name))
    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)
