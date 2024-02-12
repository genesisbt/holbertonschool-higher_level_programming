#!/usr/bin/python3
"""
This module contains the base class for all geometric figures
"""
import json


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

    def to_json_string(list_dictionaries):
        """turns a list of dict into a json string representation"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json str in a file"""
        with open("{}.json".format(cls), 'w') as file:
            file.write(self.tojson_string(list_objs))
