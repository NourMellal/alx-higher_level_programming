#!/usr/bin/python3
"""
    implement square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    implement square class
    """
    def __init__(self, size):
        """Concontructor and width, height"""
        self.__size = size
        super().__init__(self.__size, self.__size)
