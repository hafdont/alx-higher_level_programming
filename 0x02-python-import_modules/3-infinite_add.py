#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Initializ the sum to 0
    total_sum = 0

    # Loop through each argument and add it to the sum
    for arg in sys.argv[1:]:
        total_sum += int(arg)

    # Print the result
    print(total_sum)
