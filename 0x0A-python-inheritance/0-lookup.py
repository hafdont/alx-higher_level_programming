#!/usr/bin/python3

def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return [
        attribute
        for attribute in dir(obj)
        if not callable(getattr(obj, attribute obj, attribute))]
