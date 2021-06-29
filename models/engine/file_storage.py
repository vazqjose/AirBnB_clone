#!/usr/bin/python3
'''comments'''


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

        with open(__file_path, 'w+') as jfile:
            json.dump(obj, jfile)

    def reload(self):
        '''json string to obj'''

        try:
            with open(__file_path, 'w+') as jfile:
                json.load(fjile)

        except:
            pass

