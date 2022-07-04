#!/usr/bin/python3
'''
a module with public instance method area
'''


class BaseGeometry:
    '''
    a geometry class with public instance method
    '''
    def area(self):
        raise Exception("area() is not implemented")
