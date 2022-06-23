#!/usr/bin/python3
"""a square class with private instance attribute with property setter"""


class Square:
    """initialize size of square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def my_print(self):
        """prints in stdout the square with the character #
        Returns:
            square with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """getter for size
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size
        Args:
            value(int):size of square
        Returns:
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """calculate aresa of square
        Returns:
            Area of Square
        """
        return (self.__size * self.__size)
