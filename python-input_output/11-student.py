#!/usr/bin/python3
"""
This module contains the class student
"""


class Student:
    """
    Defines the class student, its atributes and functions
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict_

    def to_json(self, attrs=None):

        if isinstance(attrs, list):
            if all(isinstance(name, str) for name in attrs):
                add_dict = {}
                for name in attrs:
                    if hasattr(self, name):
                        add_dict[name] = getattr(self, name)
                return add_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            setattr(self, key, json[key])
