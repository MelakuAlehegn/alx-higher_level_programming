#!/usr/bin/python3
'''
read a text file
'''
def read_file(filename=""):
    '''
    reads file named filename
    Args:
        - filename: name of file
    '''
    with open (filename) as f:
        line = f.read()
        print(line, end='')