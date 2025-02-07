#!/usr/bin/python3
"""
Module documented: 10-square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class documented: Square
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Method documented: __init__
        Initializes the Square instance.
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Method documented: area
        Computes the area of the Square.
        """
        return self.__size ** 2
