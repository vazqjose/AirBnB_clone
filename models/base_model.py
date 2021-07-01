#!/usr/bin/python3
'''comments'''

import uuid
from datetime import datetime, timezone
import models


class BaseModel:
    '''comments'''

    def __init__(self, *args, **kwargs):
        '''
        id: assign with an uuid when an instance is created
        created_at: current datetime when an instance is created
        updated_at: current datetime when an instance is updated
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated at":
                    dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt)
                else:
                    if key != "__class__":
                        setattr(self, key, value)

    def __str__(self):
        '''
        Print class name, id and dictionary info
        '''

        #base_str = ""
        base_str = "[{}] ".format(self.__class__.__name__)
        base_str += "({}) ".format(self.id)
        base_str += "{}".format(self.__dict__)

        return base_str

    def save(self):
        '''
        updates the public instance attribute updated_at with datetime.now
        '''

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a copy of keys/values of __dict__
        '''

        new_copy = self.__dict__.copy()
        new_copy['__class__'] = self.__class__.__name__

        for key, val in new_copy.items():
            if isinstance(val, (datetime)):
                new_copy[key] = val.isoformat()

        return new_copy
