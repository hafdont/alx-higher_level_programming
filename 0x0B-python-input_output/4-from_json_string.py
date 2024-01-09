#!/usr/bin/python3
"""module contains function to converete a JSON string to python object"""


import json


def from_json_string(my_str):
    """Returns the python data structures represented by a JSON string."""
    return json.loads(my_str)
