#!/usr/bin/python33
"""Module: file_reader.py - Contains function to read and print a UTF* text file."""

def read_file(filename=""):
    """Reads a text file in UTF-8 encoding and prints its content."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
