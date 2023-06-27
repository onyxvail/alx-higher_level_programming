#!/usr/bin/python3
""" Defining a Square """


class Square:
    """ Square """
    def __init__(self, size=0):
        """ Initializing a Square
        args:
            size: size of square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ Area of square method """
    def area(self):
        """ area definition """
        return self.__size ** 2
