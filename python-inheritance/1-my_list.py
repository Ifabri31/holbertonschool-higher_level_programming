#!/usr/bin/python3
"""
This file defines a custom list class
that extends the built-in list.
"""


class MyList(list):
    """
    MyList is a custom list class that inherits from the built-in list class.
    It includes a method to print the elements of the list in sorted order.
    """
    def print_sorted(self):
        """
        This method prints the elements of the list in ascending order.
        """
        lista_ordenada = sorted(self)
        print(lista_ordenada)
