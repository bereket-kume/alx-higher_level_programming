#!/usr/bin/python3
"""module for load_from_json_file"""


import json


def load_from_json_file(filename):
    """load from json file"""

    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
