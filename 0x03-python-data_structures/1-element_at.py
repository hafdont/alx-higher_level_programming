#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieve an element from a list.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to rtrieve.

    Returns:
        The element at the specified index if it exists, otherwise None.
    """
    if idx < 0:
        return None

    current_idx = 0

    for element in my_list:

        if current_idx == idx:
            return element

        current_idx += 1

    return None
