#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(i for i in my_list)
    sum1 = 0
    for y in a:
        sum1 += y
    return sum1
