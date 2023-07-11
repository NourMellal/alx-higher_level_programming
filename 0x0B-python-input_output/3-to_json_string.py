#!/usr/bin/python3
"""returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """convert python object to an JSON"""
    return json.dumps(my_obj)
