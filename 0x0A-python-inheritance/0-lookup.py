#!/usr/bin/python3
""" Function returns alist"""


def lookup(obj):
    """Return the list of methods and attributes"""
    return list(dir(obj))
