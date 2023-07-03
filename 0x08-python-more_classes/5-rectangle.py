#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represent a rectangle """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return the perimetre of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):

        """
    Returns a string representation of the rectangle.

    This method first checks if the rectangle's perimeter is 0.
    If it is, it returns an empty string.
    If the perimeter is not 0, it builds a string representation
    of the rectangle using the '#' character.
    This string has the same number of '#' characters per line as the
    rectangle's width, and the same number of lines as the rectangle's height.
    Lines are separated by the newline character '\n'.

    Returns:
        A string representation of the rectangle.
    """

        if self.perimeter() == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string Representaion of the rectangle"""
        rect = "Rectangle(" + str(self.__width) + ", "
        rect += str(self.__height) + ")"
        return rect

    def __del__(self):
        """print a message after deletion"""
        print("Bye rectangle...")
