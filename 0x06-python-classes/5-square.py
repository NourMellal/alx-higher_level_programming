#!/usr/bin/python3
"""define class square"""


class Square:
    """Define constructor size of a square"""
    def __init__(self, size=0):
        """initialization of a new square

        size is the size of new aquare
        """
        self.__size = size

    @property
    def size(self):
        """set or get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
            if self.size == 0:
                print("")
