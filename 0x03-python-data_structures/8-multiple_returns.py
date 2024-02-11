#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first characters

    Args:
        sentence (str): The input string.

    Returns:
        A tuple contains two elements:
        - The length of the string.
        - THe first characters of the string (or None if the string is empty)
    """
    if not sentence:
        return (0, None)

    return(len(sentence), sentence[0])
