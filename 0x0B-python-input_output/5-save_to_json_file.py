#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to JSON file

    Args:
        my_obj: The Python object to be serialized.
        filename: THe name of the file to save the JSON representation

    Returns: 
        none
    """
    try:
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
    except TypeError:
        pass        
