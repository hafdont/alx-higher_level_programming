#!/usr/bin/python3

"""This modules defines a JSSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to JSON file"""
    try:
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
    except TypeError:
        pass
