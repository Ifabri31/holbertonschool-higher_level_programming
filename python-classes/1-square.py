#!/usr/bin/python3
"""
This module defines a class Square which represents a square.

It contains methods to set and retrieve the size and position of the square,
compute its area, and print the square with '#' characters.
"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square.
    """


    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
