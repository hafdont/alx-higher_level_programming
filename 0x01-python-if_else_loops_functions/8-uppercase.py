#!/usr/bin/python3

def uppercase(input_str):
    """
    Prints the input string in uppercase followed by a new line.
    Parameters:
    - input_str: The input string
    Returns:
    - None
    """
    result_str = ""
    for char in input_str:
        # check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # convert the lowercase letter to uppercasse using ord() and chr()
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result_str += "{}".format(uppercase_char)
        else:
            result_str += "{}".format(char)
      
    print(result_str)
