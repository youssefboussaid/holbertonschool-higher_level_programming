#!/usr/bin/python3
"""
module reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    func reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as filename:
        print(filename.read(), end="")
