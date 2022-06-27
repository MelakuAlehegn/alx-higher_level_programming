#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        i = fct(*args)
        return i
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return None
