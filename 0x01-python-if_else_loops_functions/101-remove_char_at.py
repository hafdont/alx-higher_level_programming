def remove_char_at(s, n):
    """
    Creates a copy of the string with the characters at position n removed.
    Parameters:
    - s: The input string
    - n: The position (C array index style) to remove

    Returrns:
    - The new string with the character remmoved
    """

    if n < 0 or n >= len(s):
        # check if the index is valid
        return s
    # Create a list of characters from the original string
    char_list = list(s)

    # Remove the characters back into a string
    char_list.pop(n)

    # Join the characters back into a string
    result = ''.join(char_list)

    return result
