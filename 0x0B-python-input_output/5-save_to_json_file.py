#!/usr/bin/python3
"""
es an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ save to json file"""
    with open(filename, "w", encoding="utp-8") as filename:
        json.dumps(my_obj, filename)