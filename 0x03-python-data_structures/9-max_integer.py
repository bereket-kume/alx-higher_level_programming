#!/usr/bin/python3
def max_integer(my_list=[]):
    l = sorted(my_list)
    return l[-1] if l else None
