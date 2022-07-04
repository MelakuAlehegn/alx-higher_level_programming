#!/usr/bin/python3
'''
a module that checks if an object of a specified class
'''


def is_same_class(obj, a_class):
    '''
    checks if obj is object of a_class
    '''
    if issubclass(a_class, type(obj)):
        return True
    else:
        False
