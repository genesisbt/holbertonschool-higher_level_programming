#!/usr/bin/python3
"""
Module for square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    class square, its attributtes and methods"
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
