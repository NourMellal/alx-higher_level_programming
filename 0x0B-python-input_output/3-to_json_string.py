#!/usr/bin/python3
import json
"""returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """convert python object to an JSON"""
    return json.dumps(my_obj)
