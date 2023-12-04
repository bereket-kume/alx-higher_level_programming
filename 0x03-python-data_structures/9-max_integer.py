#!/usr/bin/python3
def max_integer(my_list=None):
    my_list = my_list or []
    sorted_list = sorted(my_list)
    return sorted_list[-1] if sorted_list else None
