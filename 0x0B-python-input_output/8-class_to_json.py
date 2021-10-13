#!/usr/bin/python3
""" module to return dict representation of an object """


def class_to_json(obj):
    """ return dict representation of an object """
    return (obj.__dict__)
