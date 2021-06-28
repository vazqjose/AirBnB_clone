#!/usr/bin/python3
'''comments'''


import json


class FileStorage():
    '''comments'''

    __file_path = "file.json"
    __object = {}

    def all(self):
        '''commetns'''
        return self.__object

    def new(self, obj):
        '''adds new key/value pair'''
        key = "{}.".format(obj.__class__.__name__)
        key += "{}".format(obj.id)
        self.__object[key] = obj

    def save(self):
        '''object to string'''
        with open(__file_path, 'w+') as jfile:
            json.dump(self.__object, jfile)

    def reload(self):
        '''string to object'''
        try:
            with open(__file_path) as jfile:
                self.__object = json.load(jfile)
        except:
            pass
