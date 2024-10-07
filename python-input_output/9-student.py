#!/usr/bin/python3
"""
This file contains a class Student that represents a student
with a first name, last name, and age. It also provides a
method to retrieve the dictionary representation of the student.
"""


class Student:
    """
    This class represents a Student with first name, last name, and age.
    It includes a method to convert the instance attributes to a dictionary.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves the dictionary representation of the Student instance.
        """
        return self.__dict__
