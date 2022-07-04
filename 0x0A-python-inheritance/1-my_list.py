#!/usr/bin/python3
'''
a module that inherits from list
'''


class MyList(list):
    '''
    a list class with public instance method
    '''
    def print_sorted(self):
        print(sorted(self))
