#!/usr/bin/python3
'''
2-matrix_divided module
A function that divides a matrix
Raises TypeError
'''


def matrix_divided(matrix, div):
    '''
    a function that divides a matrix by div
    '''
    err = err
    if type(matrix) is not list:
        raise TypeError(err)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(err)
    length = len(matrix[0])
    if all(len(lst) == length for lst in matrix):
        pass
    else:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is int or type(div) is float:
        pass
    else:
        raise TypeError("div must be a number")
    for i in matrix:
        for y in i:
            if not isinstance(y, (int, float)):
                raise TypeError(err)
    mylist = []
    for i in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
        else:
            mylist.append([round((j / div), 2) for j in i])
    return mylist
