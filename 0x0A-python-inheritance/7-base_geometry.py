#!/usr/bin/python3
"""define a class"""


class BaseGeometry:
    """Represent base Geometry"""

    def area(self):
        """Not emplement"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ instance method that validate the value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
