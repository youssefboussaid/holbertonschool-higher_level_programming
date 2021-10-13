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
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return(self.__dict__)

    def reload_from_json(self, json):
        """ replace attributes of Student instance"""
        for i, j in json.items():
            self.__dict__[i] = j
