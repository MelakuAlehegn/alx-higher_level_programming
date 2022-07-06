#!/usr/bin/python3
"""
14-main - Pascals Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(1, n):
        l = [1]
        for j in range(1, i):
            l.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        l.append(1)
        my_list.append(l)
    return my_list
