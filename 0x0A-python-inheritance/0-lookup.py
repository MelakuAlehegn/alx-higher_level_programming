#!/usr/bin/python3
'''
module that returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''
    returns the list of attributes of obj
    '''
    return dir(obj)
