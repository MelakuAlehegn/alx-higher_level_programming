#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for i in matrix:
        matrix1.append(list(map(lambda x: x*x, i)))
    return matrix1
