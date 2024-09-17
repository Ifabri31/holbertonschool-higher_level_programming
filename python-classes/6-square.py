#!/usr/bin/python3
"""
This module defines a class Square which represents a square.

It contains methods to set and retrieve the size and position of the square,
compute its area, and print the square with '#' characters.
"""


class Square:
    """
    Class that defines a square with size and position attributes.

    Attributes:
        size (int): The size of the square (must be a positive integer).
        position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance with a size and a position.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Position of the square (default is (0, 0)).
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, ensuring it's a positive integer.

        Args:
            value (int): New size value for the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square,
        ensuring it's a tuple of two positive integers.

        Args:
            value (tuple): New position for the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        te = TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple) or len(value) != 2:
            raise te
        for num in value:
            if not isinstance(num, int) or num < 0:
                raise te
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' based on its size and position.
        If the size is 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for b in range(self.__position[1]):
                print()
            for a in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
