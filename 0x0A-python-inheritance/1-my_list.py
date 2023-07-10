#!/usr/bin/python3
"""Module: 1-my_list.py
"""


class MyList(list):
    """Subclass of list with an additional method to print
    the list in sorted order."""

    def print_sorted(self):
        """
        Prints the elements of the list in sorted (ascending) order.

        Note that this does not modify the original list; it only prints
        a sorted version.
        """
        print(sorted(self))
