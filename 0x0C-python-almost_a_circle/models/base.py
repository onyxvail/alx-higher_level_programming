#!/usr/bin/python3
"""module doc"""
import json
import csv
from os import path


class Base:
    """Base class doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor doc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file doc"""
        new_list = []
        name = str(cls.__name__) + ".json"
        with open(name, 'w', encoding='utf8') as f:
            if list_objs is None:
                f.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(cls.to_dictionary(obj))
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string doc"""
        aux_list = []
        if json_string is None:
            return aux_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create doc"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file doc"""
        l_instances = []
        if path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", 'r') as f:
                for line in f:
                    instances = cls.from_json_string(line)
                    for item in instances:
                        l_instances.append(cls.create(**item))
        return l_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv doc"""
        name = str(cls.__name__) + ".csv"
        with open(name, 'w', newline='') as f:
            writer = csv.writer(f)
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                if cls.__name__ == "Square":
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        l_instances = []
        if path.isfile(f"{cls.__name__}.csv"):
            with open(f"{cls.__name__}.csv", 'r') as f:
                my_reader = csv.reader(f)
                for line in my_reader:
                    if cls.__name__ == "Rectangle":
                        my_dict = {"id": int(line[0]),
                                   "width": int(line[1]),
                                   "height": int(line[2]),
                                   "x": int(line[3]),
                                   "y": int(line[4])}
                    if cls.__name__ == "Square":
                        my_dict = {"id": int(line[0]),
                                   "size": int(line[1]),
                                   "x": int(line[2]),
                                   "y": int(line[3])}
                    ob = cls.create(**my_dict)
                    l_instances.append(ob)
        return l_instances
