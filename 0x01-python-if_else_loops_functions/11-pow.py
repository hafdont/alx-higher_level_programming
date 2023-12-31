#!/usr/bin/python3

def pow(a, b):
    """
    Computes a to the power of b and returns the result.

    Parameters:
    - a: The base
    - b: The exponent

    Returns:
    - The result of a ^ b
    """
    # Check if the exxponent and base are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("invalid input.")
        return None

    result = a ** b

    return result
