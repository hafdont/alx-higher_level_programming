import math

class MagicClass:
    def __init__(self, radius=0):
        """
        Initializes an instance of MagicClass.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        # Initialize a private attribute __radius
        self.__radius = 0

        # Check if radius is of type int or float
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        # Set the value of __radius
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

