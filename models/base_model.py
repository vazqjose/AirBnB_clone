#!/usr/bin/python3
'''comments'''

import uuid
from datetime import datetime, timezone


class BaseModel:
    '''comments'''

    def __init__(self, *args, **kwargs):
        '''
        id: assign with an uuid when an instance is created
        created_at: current datetime when an instance is created
        updated_at: current datetime when an instance is updated
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

        if kwargs is not None:
            for key in kwargs:
                if key == "created_at" or key == "updated at":
                    dt = datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt)
                else:
                    if key != "__class__" and key != "id":
                        setattr(self, key, kwargs[key])

    def __str__(self):
        '''
        Print class name, id and dictionary info
        '''

        base_str = ""
        base_str += "[{}] ".format(self.__class__.__name__)
        base_str += "({}) ".format(self.id)
        base_str += "{}".format(self.__dict__)

        return base_str

    def save(self):
        '''comments'''

        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        '''comments'''

        new_copy = self.__dict__.copy()
        new_copy['__class__'] = self.__class__.__name__
        new_copy['created_at'] = self.created_at
        new_copy['updated_at'] = self.updated_at

        return new_copy

