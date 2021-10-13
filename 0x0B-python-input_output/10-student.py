#!/usr/bin/python3
"""
module to define Student class
"""


class Student():
    """ Student class"""

    def __init__(self, first_name, last_name, age):
        """ init methode"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation"""
        if isinstance(attrs, list) and all(
                [isinstance(x, str) for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return(self.__dict__)
