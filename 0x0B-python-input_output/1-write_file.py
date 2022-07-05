''''
writes a string to a textfile
'''


def write_file(filename="", text=""):
    '''
    writes text to filename
    '''
    with open('filename', 'w') as f:
        writes = f.write(text)
        return writes
