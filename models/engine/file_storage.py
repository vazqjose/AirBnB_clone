#!/usr/bin/python3
''' File storage '''


import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''comments'''
        return self.__objects

    def new(self, obj):
        '''comments'''
        if obj:
            key = "{}.".format(obj.__class__.__name__)
            key += "{}".format(obj.id)
            self.__objects[key] = obj

    def save(self):
        '''obj to json file'''
        '''
        this print block is for debugging
        __objects is empty
        '''

        with open(self.__file_path, 'w') as jfile:
            json.dump(self.__file_path, jfile)

    def reload(self):
        '''json string to obj'''

        try:
            with open(self.__file_path) as jfile:
                json.load(jfile)

        except:
            pass
