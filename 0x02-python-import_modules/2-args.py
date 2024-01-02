#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Check and print based on the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Print each argument and its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

