#!/usr/bin/python3
'''comments'''

import uuid
from datetime import datetime, timezone

class BaseModel:
    '''comments'''

    def __init__(self, id, created_at, updated_at):
        '''comments'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()

    def __str__(self):
        '''comments'''
        print("[{}] ".format(self.__class__.__name__), end="")
        print("({}) ".format(self.id), end="")
        print("<{}>".format(self.__dict__)

    def save(self):
    '''comments'''


