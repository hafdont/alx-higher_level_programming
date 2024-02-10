def print_list_integer(my_list=[]):
    """
    Print all integers of a list, one integer per line.

    Args:
        my_list (list): The list of integers to be printed.

    Returns:
        None
    """

    for num in my_list:
        # Print each integer using str.format() without any additional formatt
        print("{:d}".format(num))
