#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method ofr height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= =")
        self.__height = value

    def area(self):
        """Calculate the perimetter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__widht * 2) + (slef.__height * 2)
