#!/usr/bin/python3

        """a module that defines a square"""

class Square:
        """ A class module that represents a square """


        def __init__(self, size=0):
                """
                Intitializes a new instance

                Args:
                        size (int): THe size of the square

                Raises:
                        TypeError: If the size is not an integer.
                        Value Error: If the size is less than ).
                """


                if not isinstance(size, int):
                        raise TypeError("size must be an integer")
                elif size < 0:
                        raise ValueError("size must be >= 0")
                else:
                        
                        self.__size = size


        def area(self):
                """ 
                Calculates the are of the squre.

                Returns: The area of te square
                """
    
                return self.__size ** 2
