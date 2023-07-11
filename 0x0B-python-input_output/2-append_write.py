#!/usr/bin/python3
""" implement append_write function"""


def append_write(filename="", text=""):
    """append in the end of a text file """
    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)
