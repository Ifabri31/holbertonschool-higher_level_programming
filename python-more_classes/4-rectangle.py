#!/usr/bin/python3
"""
Module documented
"""


class Rectangle:
    """
    Class documented
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for row in range(self.height):
            rectangle += "#" * self.width + "\n"

        return rectangle[:-1]

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
