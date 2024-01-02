#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    # Get the number of argumenets
    num_args = len(argv) - 1

    # Print the number of arguments
    print("{} arguments{}{}".format(
        num_args,
        's' if num_args != 1 else '',
        '' if num_args == 0 else ':'
    ))

    # Print each argument and its positiion
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
