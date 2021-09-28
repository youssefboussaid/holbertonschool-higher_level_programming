#!/usr/bin/python3
"""square class
"""


class Square:
    """square class
    Attributes:
    size (int) : square size
    """

    def __init__(self, size=0):
        """
        Initialize methode
        Args:
            size (int) : square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        square area
        Return : square area
        """
        return(self.__size * self.__size)
