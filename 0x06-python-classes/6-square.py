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
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(1, self.__size + 1):
                for j in range(1, self.__size + 1):
                    print("#", end="")
                print()

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
        if len(value) > 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
