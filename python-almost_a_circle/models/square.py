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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

def update(self, *args, **kwargs):
    """updates the attributes of the object"""
    keys = ["id", "size", "x", "y"]
    if args:
        for i in range(len(args)):
            setattr(self, keys[i], args[i])
        elif kwargs:
            for kname, kvalue in kwargs.items():
                for keyname in keys:
                    if keyname == kname:
                        setattr(self, kname, kvalue)
                        break
