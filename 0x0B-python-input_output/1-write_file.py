''''
writes a string to a textfile
'''


def write_file(filename="", text=""):
    '''
    writes text to filename
    Args:
        -filename: file to write to
        -text: text to write
    Returns: number of chars written
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
