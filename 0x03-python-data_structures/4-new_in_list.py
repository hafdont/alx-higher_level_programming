#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position without modifying

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element,
        element: the new element to replace the existing one.


    Returns:
        A copy of the original list with the element replaced
        or the original list if idx is negative or out of range.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]

    new_list[idx] = element

    return new_list
