#!/usr/bin/python3
''''
a modcule that test if only subclass of class
'''


def inherits_from(obj, a_class):
    '''
    returns true if obj is only a subclass fo a_class
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
