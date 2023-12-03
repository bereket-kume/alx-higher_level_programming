#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    items = my_list[::-1]
    for item in items:
        print("{:d}".format(item))
