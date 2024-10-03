#!/usr/bin/python3
"""
This file defines a Square class that inherits from Rectangle.
It validates the size attribute, calculates the area, 
and provides a string representation of the square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from Rectangle.
    It validates the size of the square upon initialization 
    and provides methods to calculate the area and represent the square.
    """
    def __init__(self, size):
        """
        Initializes a new instance of Square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Provides a string representation of the square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
