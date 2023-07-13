#!/usr/bin/python3
"""Defines a text file"""


def append_after(filename="", search_string="", new_string=""):
    """insert text"""
    text = ""
    with open(filename) as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as write:
        write.write(text)
