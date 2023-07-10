#!/usr/bin/python3
"""module 4: 4-inhertis_from.py"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that
        inherited from the specified class.

    Args:
    obj: Any object. The object whose type we want to check.
    a_class: The class we want to check if 'obj' is a subclass of.

    Returns:
    True if 'obj' is an instance of a class that is a subclass of
        'a_class'; False otherwise.
    """
    # Use Python's built-in type function to get the type of obj,
    # then compare this with a_class to make sure obj is not
    #  an instance of a_class itself.
    # Use Python's built-in isinstance function to check if obj
    #  is an instance of a subclass of a_class.
    return type(obj) != a_class and isinstance(obj, a_class)
