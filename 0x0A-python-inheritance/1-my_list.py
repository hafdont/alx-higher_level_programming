#!/usr/bin/python3
"""A module that inherits from a list"""


class MyList(list):
    """A class that inherits from a list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self)
