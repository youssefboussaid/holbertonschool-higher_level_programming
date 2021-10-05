#!/usr/bin/python3
"""
Module to print a square
"""


def print_square(size):
    """
    function that prints a square with the character #.
    Args:
        size(int): size of teh square
    Raises:
        TypeError: if size is not integer
        ValueError: if size is less then 0
    Returns:
        a square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) == float:
        raise TypeError("size must be an integer")
    for i in range(1, size + 1):
        for x in range(1, size + 1):
            print("#", end="")
        print()
