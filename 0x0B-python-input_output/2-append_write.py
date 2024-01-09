#!/usr/bin/python3
"""Module contains a functions that appends a string to a UTF-* text file"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file in UTF-8 encoding"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
