#!/usr/bin/python3
'''Defines class FileStorage. FileStorage saves all of our
objects created when the programming is running to a file.
'''


class FileStorage:
    '''Class serializes instances to a JSON file and
    deserializes JSON file to instances.
    Private class attrs:
        __file_path: A string, the path to the JSON file.
        __objects: A dictionary, stores all objects by
            <class name>.id (ex: to store a BaseModel object with
            id=12121212, the key will be BaseModel.12121212).
    Public instance methods:
        all(self): Returns the dictionary __objects.
        new(self, obj): Sets in __objects the obj with key
            <obj class name>.id
        save(self): Serializes __objects to the JSON file (path: __file_path)
        reload(self): Deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, does nothing.
    '''

