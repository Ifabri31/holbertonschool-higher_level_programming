#!/usr/bin/python3
"""
This file contains a class Student that represents a student
with first name, last name, and age. It includes methods to retrieve
and reload the dictionary representation of the student.
"""


class Student:
    """
    This class represents a Student with first name, last name, and age.
    It includes methods to convert the instance attributes to a dictionary,
    with an option to filter which attributes to include, and to reload
    attributes from a dictionary.
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

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
