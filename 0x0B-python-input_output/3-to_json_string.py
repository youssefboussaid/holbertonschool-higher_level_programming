#!/usr/bin/python3
"""
module  that appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """add func"""
    with open(filename, "a+", encoding="utf-8") as filename:
        filename.write(text)
        return len(text)
