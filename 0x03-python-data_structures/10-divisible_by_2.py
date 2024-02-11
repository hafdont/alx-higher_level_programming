#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 9 in a list.

    Args:
        my_list (list): The input list.

    Returns:
        A new list with True or False.
        The new list has the same size as the original list.
    """

    results = []

    for num in my_list:
        if num % 2 == 0:
            results.append(True)
        else:
            results.append(False)

    return results
