#!/usr/bin/python3

"""Function to convert an object to a JSON-serializable dictionary."""


def class_to_json(obj):
    """convertes an object to a dict representation for JSON serialization"""

    obj_dict = obj.__dict__

    for key, value in obj_dict.items():
        if hasattr(value, '__dict__'):
            obj_dict[key] = class_to_json(value)

        elif isinstance(value, (list, dict, str, int, bool)):
            pass
        else:
            obj_dict[key] = str(value)

    return obj_dict
