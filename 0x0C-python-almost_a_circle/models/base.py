#!/usr/bin/python3
'''
Base package
'''


class Base:
    '''
    a class base class with class attribute
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.__nb_objects = id
