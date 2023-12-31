#!/usr/bin/python3

def add(a, b):
    """
    Adds two integers and returns the results.

    Parameters:
    - a: The first integer
    - b: The second integer

    Returns:
    - The sum of a and b
    """

    # Ensure both inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Invalid input. both inputs must be integers")
        return None

    result = a + b

    return result
