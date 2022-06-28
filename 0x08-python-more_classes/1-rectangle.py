#!/usr/bin/python3
'''
a class that defines a rectange
'''


class Rectangle:
    '''
    a rectangle class to define a rectange with setter
    and getter methods for height and width
    '''
    def __init__(self, width=0, height=0):
        '''initializes the class attributes'''
        self.width = width
        self.height = height

    @property
    def height(self):
        '''getter for height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height of rectangle
        raises TypeError if type is not int
        raises ValueError if value is < 0
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value< 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    
    @property
    def width(self):
        '''getter for width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width of rectangle
        raises TypeError if type is not int
        raises ValueError if value is < 0
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
