#!/usr/bin/python3
"""define a Student class """


class Student:
    """ retrieves a dictionary representation of a Student instance """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student.
        Args:
            json (dict): the key/value pairs to replace with
        """
        for k, v in json.items():
            setattr(self, k, v)
