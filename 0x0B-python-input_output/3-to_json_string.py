#!/usr/bin/python3
"""
a module convert object to json string
"""
import json


def to_json_string(my_obj):
    """ return a json representation of the object """
    return json.dumps(my_obj)
