#!/usr/bin/python3
"""
This module defines a Rectangle class that represents a rectangle
with width and height attributes, along with methods to get and set them.
"""


class Rectangle:
    """
    This class defines a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.
        If no values are given, width and height default to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.
        Returns the current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Ensures that width is an integer and not negative.
        Raises a TypeError if width is not an integer.
        Raises a ValueError if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        Returns the current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Ensures that height is an integer and not negative.
        Raises a TypeError if height is not an integer.
        Raises a ValueError if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
