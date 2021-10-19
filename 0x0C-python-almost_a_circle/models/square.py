#!/usr/bin/python3
"""
rectangle module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init methode"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str methode"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        ))

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def update(self, *args, **kwargs):
        """update methode"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        elif len(kwargs) > 0:
            for i in kwargs.keys():
                if i == "id":
                    self.id = kwargs["id"]
                if i == "size":
                    self.size = kwargs["size"]
                if i == "x":
                    self.x = kwargs["x"]
                if i == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """dict methdoe"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
