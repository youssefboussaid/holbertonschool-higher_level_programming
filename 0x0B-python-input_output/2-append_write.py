#!/usr/bin/python3
"""
module that write to a text file
"""


def append_write(filename="", text=""):
    """write to a fiel function"""
    with open(filename, "a+", encoding="utf-8") as filename:
        filename.write(text)
        return len(text)
