#!/usr/bin/python3


"""Defines a studnt class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance with first,last name and age."""
        sel.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"Returns a dictionary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(selff, attr):
                    result[attr] = getattr(self, attr)
            return result
