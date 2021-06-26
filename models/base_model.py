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
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()

        if kwargs is not None:
            for key in kwargs:
                if key != "__class__" and key != "id":

                    if key == "created_at" or key == "updated at":
                        print("HERE YOU GO")
                        print(kwargs[key])
                        print(type(datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')))
                        print("OVER")

                    else
                        self.key = kwargs[key]

    def __str__(self):
        '''
        Print class name, id and dictionary info
        '''

        base_str = ""
        base_str += "[{}] ".format(self.__class__.__name__)
        base_str += "({}) ".format(self.id)
        base_str += "<{}>".format(self.__dict__)

        return base_str

    def save(self):
        '''comments'''

        self.updated_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        '''comments'''

        return self.__dict__
