#!/usr/bin/python3
""" Defining a Square """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing a Square
        args:
            size: size of square """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter def """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setting
        args:
            value: new value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the area of suqare """
        return self.size ** 2

    def my_print(self):
        """ prints a square in # """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print('#', end='')
            print("")
        if self.size == 0:
            print()

    def __str__(self):
        """ prints a square instance """
        _str = ""
        for i in range(self.__position[1]):
            _str += "\n"
        for i in range(self.__size):
            for k in range(self.__position[0]):
                _str += " "
            for j in range(self.__size):
                _str += "#"
            _str += "\n"
        if self.size == 0:
            _str += "\n"
        return _str[:-1]
