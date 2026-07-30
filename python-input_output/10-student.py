#!/usr/bin/python3
"""Module that defines a Student class with filter capability."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes named in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            res = {}
            for k in attrs:
                if hasattr(self, k):
                    res[k] = getattr(self, k)
            return res
        return self.__dict__
