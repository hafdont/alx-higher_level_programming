#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all occurence of the characters 'c' and 'C' from a string.

    Args:
        my_string (str): THe input string.

    Returns:
        The new string with 'c' and 'C' removed.
    """

    result = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            result += char

    return result
