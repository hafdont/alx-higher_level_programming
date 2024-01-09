#!/usr/bin/python3
"""module thats contains a function that wriites a string to UTF8 textfile."""


def write_file(filename="", text=""):
    """Writes a string to a text file in UTF"""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
