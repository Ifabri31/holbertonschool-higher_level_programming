#!/usr/bin/python3
"""
Module documented: 6-base_geometry
"""


class BaseGeometry:
    """
    Class documented: BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method documented: integer_validator
        Validates value.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
