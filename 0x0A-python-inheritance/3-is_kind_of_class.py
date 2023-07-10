#!/usr/bin/python3
"""Define class that check the function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specific class.

    Args:
    obj: Any object. The object whose type we want to compare.
    a_class: The class we want to check if 'obj' is an instance of.

    Returns:
    True if 'obj' is an instance of 'a_class'; False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
