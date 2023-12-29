#!/usr/bin/python3
def uppercase(s):
    for c in s:
        # check if the character is lowercase letter
        if ord('a') <= ord(c) <= ord('z'):
            # convert to uppercase ussing ASCII values
            uppercase_char = chr(ord(c) - ord('a') + ord ('A'))
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(c), end="")
    print()
