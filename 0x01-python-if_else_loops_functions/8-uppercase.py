#!/usr/bin/python3

def uppercase(input_str):
    """
    Prints the input string in uppercase followed by a new line.
    
    Parameters:
    - input_str: The input string
    Returns:
    - None
    """
    for char in input_str:
        # check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # convert the lowercase letter to uppercasse using ord() and chr()
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end='')
        else:
            print("{}".format(char), end='')
      
    # Print a new line
    print()
