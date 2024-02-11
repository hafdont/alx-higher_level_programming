#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    Args:
        my_ist (list): The input list.
        idx (int): The index of the item to be deleted.

    Returns:
        The modified list with the item at the specified position deleted,
        if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx+1:]
