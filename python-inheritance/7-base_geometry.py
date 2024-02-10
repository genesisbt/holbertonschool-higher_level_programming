#!/usr/bin/python3
"""
module for inherits from function
"""


class BaseGeometry:
    """
    Defines the class BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise Exception("{} must be an integer".format(name))
        elif value <= 0:
            raise Exception("{} must be greater than 0".format(name))
