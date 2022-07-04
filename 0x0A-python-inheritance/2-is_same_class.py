#!/usr/bin/python3
'''
a module that checks if an object is exactly instance of of a specified class
'''


def is_same_class(obj, a_class):
    '''
    checks if obj is object of a_class
    '''
    return issubclass(a_class, type(obj))
