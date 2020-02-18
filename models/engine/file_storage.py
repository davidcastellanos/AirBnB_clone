#!/usr/bin/python3
import json
import datetime
import uuid
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def odict_object_hook(self, odict):
        try:
            print('printe')
            classes = odict('__class__')
        except KeyError:
            #print('except1')
            return odict

        else:
            try:
                #print('try')
                self.new(getattr(datetime, classes)(**odict))
            except AttributeError:
                #print('exvep')
                return odict

    def all(self):
        #print('All')
        return FileStorage.__objects

    def new(self, obj):
        #print('new')
        key = (obj.__class__.__name__ + "." + obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        #print(FileStorage.__objects)
        obj_to_dict = {}
        for key,value in FileStorage.__objects.items():
            obj_to_dict[key] = value.to_dict()
        #print(obj_to_dict)
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_to_dict, file)

    def reload(self):
        #print('Reload')
        try:
            with open(FileStorage.__file_path, mode='r', encoding='UTF8') as file:
                FileStorage.__objects = json.load(file, object_hook = odict_object_hook)
    
        except:
            pass