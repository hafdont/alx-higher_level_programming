#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print all integer af a list in reverse order, one integer per line.

    Args:
        my_list (list): THe list f integers to be printed in revrse order.

    Returns:
        None
    """

    for num in reversed(my_list):
        print("{:d}".format(num))
