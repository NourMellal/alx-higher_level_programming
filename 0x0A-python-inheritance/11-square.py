#!/usr/bin/python3
"""
    implement square class
"""

Rectangle = __import__("9-rectangle").Rectangle
"""
    super class
"""


class Square(Rectangle):
    """
    implement square class
    """

    def __init__(self, size):
        """Concontructor and width, height"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return  rectangle description: [Square] <size>/<size>"""
        strn = "[" + str(self.__class__.__name__) + "] "
        strn += str(self.__size) + "/" + str(self.__size)
        return strn
