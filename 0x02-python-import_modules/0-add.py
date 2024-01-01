#!/usr/bin/python3

if __name__ == "__main__":
    # Import the add function from the add_0 module
    from add_0 import add

    # Assign the value 1 to variable a
    a = 1

    # Assign the value 2 to variable b
    b = 2

    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
