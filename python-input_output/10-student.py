#!/usr/bin/python3
"""
This file contains a class Student that represents a student
with first name, last name, and age. It includes a method to retrieve
the dictionary representation of the student, optionally filtering attributes.
"""


class Student:
    """
    This class represents a Student with first name, last name, and age.
    It includes a method to convert the instance attributes to a dictionary,
    with an option to filter which attributes to include.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            dic = {}
            for a in attrs:
                if a == "first_name":
                    dic[a] = self.first_name
                if a == "last_name":
                    dic[a] = self.last_name
                if a == "age":
                    dic[a] = self.age
        return dic
