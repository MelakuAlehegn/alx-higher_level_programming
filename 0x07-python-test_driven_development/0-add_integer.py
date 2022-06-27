#!/usr/bin/python3
'''
   0-add_integer module
   a function that adds two integers
   raises TypeError for non ints
'''


def add_integer(a, b=98):
    '''
    a function to return sum of two integers, converts floats to int
    '''
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
