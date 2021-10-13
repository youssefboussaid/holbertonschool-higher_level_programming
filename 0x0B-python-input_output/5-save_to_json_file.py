#!/usr/bin/python3
"""
saves an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ save to json file"""
    with open(filename, "w", encoding="utp-8") as filename:
        json.dump(my_obj, filename)
