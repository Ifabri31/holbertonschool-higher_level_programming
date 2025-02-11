#!/usr/bin/python3
"""
Module documentation: 10-student.py
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {i: self.__dict__[i] for i in attrs if i in self.__dict__}
        return self.__dict__
