#!/usr/bin/python3
"""
module convert json rep to string
"""
import json


def from_json_string(my_str):
    """
    returns string from json
    """
    return json.loads(my_str)
    