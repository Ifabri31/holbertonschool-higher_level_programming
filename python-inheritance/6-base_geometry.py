#!/usr/bin/python3
"""
This file defines a class named BaseGeometry,
which serves as a base class for geometric shapes.
"""


class BaseGeometry:
    """
    This class serves as a base class for geometry-related classes.
    It includes an unimplemented method area() that must be defined
    in any subclass that inherits from BaseGeometry.
    """
    def area(self):
        """
        Method that raises an exception if called.
        This indicates that the area method is not implemented in
        the BaseGeometry class and must be overridden in subclasses.
        """
        raise Exception("area() is not implemented")
