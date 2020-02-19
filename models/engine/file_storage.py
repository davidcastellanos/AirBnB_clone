#!/usr/bin/python3
import json
import datetime
import uuid
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = (obj.__class__.__name__ + "." + obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_to_dict = {}
        for key,value in FileStorage.__objects.items():
            obj_to_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_to_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r', encoding='UTF8') as file:
                loaded = json.load(file)
                for key in loaded.keys():
                    print(key)
                    FileStorage.__objects[key] = BaseModel(**loaded[key])
        except:
            pass
