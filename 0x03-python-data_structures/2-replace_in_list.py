#!/usr/bin/python3 

def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a space position.

    Args:
        my_list (list): The list at a specific position.
        idx (int): The index at which to replace the element.
        Element: The new elemnt to replace the exististingone.


    Return:
        The modified list if idx is valid, otherwise the original list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element

    return my_list
