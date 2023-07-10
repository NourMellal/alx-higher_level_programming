#!/usr/bin/python3
"""Define class that check the function"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specific class.

    Args:
    obj: Any object.
    a_class: The class to check if 'obj' is an instance of.

    Returns:
    True if 'obj' is an instance of 'a_class'; False otherwise.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
