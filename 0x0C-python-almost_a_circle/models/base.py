#!/usr/bin/python3
"""module for base"""
from json import dumps, loads


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None and not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
            with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objs))
    
    def from_json_string(json_string):
        if json_string is None and not json_string:
            return "[]"
        else:
            return loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + "json"
        ins_list = []
        try:
            with open(filename, mode="r", encoding="utf") as f:
                json_data = f.read()
                dictionaries = cls.from_json_string(json_data)
                for di in dictionaries:
                    ins = cls.create(**dictionary)
                    ins_list.append(ins)
        except FileNotFoundError:
            return []
        return ins_list
