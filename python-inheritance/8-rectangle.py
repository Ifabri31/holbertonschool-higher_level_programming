#!/usr/bin/python3
"""
This file defines a Rectangle class that inherits from BaseGeometry.
It validates the width and height attributes to ensure they are positive integers.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from BaseGeometry.
    It validates the width and height of the rectangle upon initialization.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
