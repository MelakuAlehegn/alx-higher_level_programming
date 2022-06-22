#!/usr/bin/python3
class Square:
    '''a square class with private instance attribute'''

    def __init__(self, size=0):
        '''initialize size of square
        Args:
            size (int): size of side of square
        Returns:
            None
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
