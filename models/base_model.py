#!/usr/bin/python3
'''comments'''

import uuid
from datetime import datetime, timezone

class BaseModel:
    '''comments'''

    def __init__(self):
        '''
        id: assign with an uuid when an instance is created
        created_at: current datetime when an instance is created
        updated_at: current datetime when an instance is updated
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()

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
