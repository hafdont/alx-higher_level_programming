#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
        matrix (list of lists): the matrix of integers to be printed

    Returns:
        None
    """
    for row in matrix:
        formatted_row = " ".join("{:d}".format(num) for num in row)
        print(formatted_row)
