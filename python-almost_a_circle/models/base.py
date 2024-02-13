#!/usr/bin/python3
"""
This module contains the base class for all geometric figures
"""
import json
import os


class Base:
    """
    Base class for all geometric figures
    Contains its atributes and functions
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """turns a list of dict into a json string representation"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json str in a file"""

        if list_objs is None:
            list_objs = []

        for num, obj in enumerate(list_objs):
            list_objs[num] = obj.to_dictionary()

        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Transforms from json string to dictionary"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an object from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        path = "{}.json".format(cls.__name__)
        objectlist = []
        if not os.path.exists(path):
            return []
        else:
            with open(path) as jsonfile:
                dictionary = cls.from_json_string(jsonfile.read())
            for element in dictionary:
                objectlist.append(cls.create(**element))
        return objectlist
