#!/usr/bin/python3
"""module for save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """save to json method"""

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
