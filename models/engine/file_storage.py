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
        print("Info of __objects dictionary:")
        print(type(self.__objects))
        print(self.__objects)
        print("---------------------------------")

        new_dict = {}

        # its not entering through this loop
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
            print("{}.{}".format(key, obj))

        with open(self.__file_path, 'w') as jfile:
            json.dump(new_dict, jfile)


    def reload(self):
        '''json string to obj'''

        try:
            with open(self.__file_path) as jfile:
                json.load(jfile)

        except:
            pass

