#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxu = my_list[0]
        for i in my_list:
            if i > maxu:
                maxu = i
        return maxu
    return None
