#!/usr/bin/python3
"""function to represet find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    mylist = list_of_integers
    l = len(mylist)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or mylist[m] >= mylist[m + 1]) and (m == 0 or mylist[m] >= mylist[m - 1]):
        return mylist[m]
    if m != l - 1 and mylist[m + 1] > mylist[m]:
        return find_peak(mylist[m + 1:])
    return find_peak(mylist[:m])
