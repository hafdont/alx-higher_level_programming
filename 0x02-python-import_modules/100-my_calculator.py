#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check the numm=ber of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get arguments
    a, operator, b = map(int, sys.argv[1:])

    # Perform the operator based on the operator
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in ops:
        print("Unknown operator. Available operators +, -, * and /")
        sys.exit(1)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
