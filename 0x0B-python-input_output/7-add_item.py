#!/usr/bin/python3

"""Script to add arguments to a python list and save them to a JSON file."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_arguments_to_list(filename, *args):
    """ Add arguments to a python lisst and save them to a JSON file."""
    try:
        existing_list = load_from_json_file(filename)
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(args)
    save_to_json_file(existing_list, filename)


if __name__ == "__main__":

    arguments = sys.argv[1:]
    add_arguments_to_list('add_item.json', *arguments)
