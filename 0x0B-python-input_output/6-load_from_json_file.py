#!/usr/bin/python3
"""
module to load from a json file
"""


def load_from_json_file(filename):
    """func that loads from a json file"""
    with open(filename, "r", encoding="utf-8") as filename:
        return json.load(filename)
