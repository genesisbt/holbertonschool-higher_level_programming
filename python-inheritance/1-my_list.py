#!/usr/bin/python3
"""
Module for Class MyList
"""


class MyList(list):
    """
    class mylist child of list
    """
    def print_sorted(self):
        print(sorted(self))
