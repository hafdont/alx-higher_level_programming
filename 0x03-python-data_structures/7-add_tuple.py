#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples.

    Args:
    tuple_a (tuple): The first tuple.
    tuple_b (tuple): The second tuple.

    Returns:
        a tuple with 2 integers:
        - The first elements is the addititon of the first element.
        - The second element is the addition 0f the second element.
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]

    return (first_element, second_element)
