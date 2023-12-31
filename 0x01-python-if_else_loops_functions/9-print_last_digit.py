#!/usr/bin/python3

def print_last_digit(number):
    """"
    Prints the last digit of a given number.

    Parameters:
    - number: The input number
    Returns:
    - The value of the last digit
    """
    # Ensure the input is an integer
    if not isinstance(number, int):
        raise TypeError("Invalid input.")
        return None

    # Get the last digit
    last_digit = abs(number) % 10

    # Print the last digit
    print(last_digit, end="")

    # Return the value of the last digit
    return last_digit
