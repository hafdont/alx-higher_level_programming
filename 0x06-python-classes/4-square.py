#!/usr/bin/python

"""A module that represents a square"""

class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializes a new instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: The size is not an integer.
            ValueError: If the size is less than 0.
        """

        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

