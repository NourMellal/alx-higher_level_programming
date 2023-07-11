#!/usr/bin/python3
"""function that read from a txt file"""


def read_file(filename=""):
    """ read file and print its content"""
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
