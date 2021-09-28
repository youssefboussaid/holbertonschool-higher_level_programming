#!/usr/bin/python3
"""square class
"""


class Square:
    """ Square class defined by geometric shap
        Attributes:
            size (int): Size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        set square square area
        Return:
            the current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            size (int): size of a side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print a square from the size using ##
        Returns:
            None
        """
        if self.__size > 0:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                if self.position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print(end="\n")

    @property
    def position(self):
        """
        getter position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter position
        Args:
            value (tuple) : position of the square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
