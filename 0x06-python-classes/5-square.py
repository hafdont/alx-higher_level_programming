#!/usr/bin/python3

"""A module that defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represents the size of the square defined
            position: represents the position of the square
        Raises:
            TypeError: if size is not an integer or position is not a tuple of 2 positive integers
            ValueError: if size is less than zero or position contains non-positive integers
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # and using position"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

