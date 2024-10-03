#!/usr/bin/python3
"""
This file defines a class named BaseGeometry,
which serves as a base class for geometric shapes
and provides methods for area calculation and value validation.
"""


class BaseGeometry:
    """
    This class serves as a base class for geometry-related classes.
    It includes an unimplemented method area() and a method for 
    validating integer values.
    """
    def area(self):
        """
        Method that raises an exception if called.
        This indicates that the area method is not implemented in
        the BaseGeometry class and must be overridden in subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
