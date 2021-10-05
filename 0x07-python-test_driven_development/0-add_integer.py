#!/usr/bin/python3
"""
variables additions module
"""


def add_integer(a, b=98):
    """
    ADD Two integer a and b
    Args:
        a (int/float): first int
        b (int/float): Second int
    Raises:
        TypeError: in case the arguments are not int or float
        (int) : Sum of the int a and b
    """
    if isinstance(a, int) == False and isinstance(a, float) == False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) == False and isinstance(b, float) == False:
        raise TypeError("b must be an integer")
    else:
        return(int(a + b))
