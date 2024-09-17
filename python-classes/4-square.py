#!/usr/bin/python3
"""
This module defines a class Square which represents a square.

It contains methods to set and retrieve the size and position of the square,
compute its area, and print the square with '#' characters.
"""


class Square:
    """
    Represents a square with a specific size.

    Attributes:
        size (int): The size of the square. Must be a non-negative integer.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square, which is the square of the size.

        Example:
            >>> sq = Square(3)
            >>> sq.area()
            9
        """
        return self.__size ** 2
