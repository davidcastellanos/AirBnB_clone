#!/usr/bin/python3
"""
Module that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import datetime
import uuid
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    File Storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = (obj.__class__.__name__ + "." + obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_to_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_to_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_to_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='UTF8') as f:
                loaded = json.load(f)
                for key in loaded.keys():
                    FileStorage.__objects[key] = BaseModel(**loaded[key])
        except:
            pass