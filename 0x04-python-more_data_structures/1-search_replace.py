#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for key, value in enumerate(new_list):
        if search == value:
            new_list[key] = replace
    return new_list
