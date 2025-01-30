#!/usr/bin/python3
"""
Module documented
"""


class Rectangle:
    """
    Class documented
    """
    def __init__(self, width=0, height=0):
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value)is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
