#!/usr/bin/python3
"""
module reads a text file (UTF8) and prints it to stdout
"""


def write_file(filename="", text=""):
    """
    func reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "w", encoding="utf-8") as filename:
        filename.write(text)
    return len(text)
    