#!/usr/bin/python3
"""
base models
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init methode"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json methode"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class methode
        """
        list = []
        if list_objs is None:
            list = []
        else:
            for i in list_objs:
                list.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), 'w', encoding="UTF8") as f:
            f.write(cls.to_json_string(list))

    def from_json_string(json_string):
        """
        from json methode
        """
        list = []
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create a dummy
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
