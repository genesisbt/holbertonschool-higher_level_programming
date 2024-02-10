#!/usr/bin/python3
"""
This module contains the class student
"""


class student:
    """
    Defines the class student, its atributes and functions
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
