#!/usr/bin/python3
'''
a module for basegeometry
'''


class BaseGeometry:
    '''
    a geometry class with public instance method and integer validator
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
