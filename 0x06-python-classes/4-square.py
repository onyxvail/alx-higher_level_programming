#!/usr/bin/python3
""" Defining a Square """


class Square:
    """ Square """
    def __init__(self, size=0):
        """ Initializing a Square
        args:
            size: size of square """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns area of square """
        return self.__size ** 2
