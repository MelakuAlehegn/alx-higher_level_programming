#!/usr/bin/python3
'''
appends a string at the end of a text file
'''


def append_write(filename="", text=""):
    '''
    appends a text at the end of filename
    Args:
        -filename: file to write to
        -text: text to write
    Returns: number of chars appended
    '''
    with open(filename, 'a+') as f:
        write = f.write(text)
        return write
