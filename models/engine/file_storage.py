#!/usr/bin/python3
'''comments'''


import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''comments'''

        return self.__objects

    def new(self, obj):
        '''comments'''

        key = "{}.".format(obj.__class__.__name__)
        key += "{}".format(obj.id)
        self.__objects[key] = obj

    def save(self):
        '''obj to json file'''

        with open(self.__file_path, 'w+') as jfile:
            json.dump(self.__objects, jfile)

    def reload(self):
        '''json string to obj'''

        try:
            with open(self.__file_path) as jfile:
                json.load(jfile)

        except:
            pass

