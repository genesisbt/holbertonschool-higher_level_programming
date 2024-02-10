#!/usr/bin/python3
"""
module for class rectangle 
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


Class Rectangle(BaseGeometry):
    """
    Defines Class Rectangle, subclass of BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
