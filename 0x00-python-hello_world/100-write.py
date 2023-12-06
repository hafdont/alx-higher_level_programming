#!/usr/bin/python3
import sys

def print_error_message():
    """Prints an error message to stderr."""
    sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")

if __name__ == "__main__":
    print_error_message()
    sys.exit(1)
