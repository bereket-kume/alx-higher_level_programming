#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_dict = max(a_dictionary, key=a_dictionary.get)
        return max_dict
    else:
        return None
