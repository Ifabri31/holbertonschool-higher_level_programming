#!/usr/bin/python3
"""
Module documented: 8-rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class documented: Rectangle
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Method documented: __init__
        Initializes the Rectangle instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
