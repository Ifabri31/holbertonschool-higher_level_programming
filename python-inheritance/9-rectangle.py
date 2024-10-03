#!/usr/bin/python3
"""
This file defines a Rectangle class that inherits from BaseGeometry.
It validates the width and height attributes, calculates the area, 
and provides a string representation of the rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from BaseGeometry.
    It validates the width and height of the rectangle upon initialization
    and provides methods to calculate the area and represent the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Provides a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
