#!/usr/bin/python3
'''File defines the class Basemodel'''

from uuis import uuid4
'''Used to generate a random id for eac instance of the clas.'''

class Basemodel:
    '''Class defines all common attributes/methods for other classes.
    Public instance attributes:
        id: a string assigned an uuid when an instance is created
        created_at: a datetime object assigned the current datetime when an instance is created
        updated_at: a datetime object assigned the current datetime when an instance is created
            and it will be updated every time the object is changed
    Public instance methods:
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance,
            self.__dict__ only returns the attributes of the instance, so a key __class__ will be added 
            to this dictionary paired with the class name of the object. created_at/updated_at will be 
            converted to string objects in ISO format(format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)). 
            This method will be the first piece of the serialization/deserialization process: It creates a 
            dictionary representation with "simple object type" of our BaseModel
    '''

