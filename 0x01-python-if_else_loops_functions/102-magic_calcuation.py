#!/usr/bin/python3

def magic_calculation(a, b, c):
    # Check if 'a' is less than 'b'
    if a < b:
        # If true, return the value of 'c'
        return c
    # Check if 'c' is greater than 'b'
    elif c > b:
        # If true, return the sum of 'a' and 'b'
        return a + b
    else:
        # If none of the above conditions are met, return the result
        return a * b - c

