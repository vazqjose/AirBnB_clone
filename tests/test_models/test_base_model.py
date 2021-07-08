#!/usr/bin/python3
'''unittests for our BaseModel class found in models/base_model.py
'''

import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''unittests for our BaseModel class, testing:
    __init__, __str__, to_dict, and the save methods from the class.
    '''
    def test_save(self):
        '''Testing the save method from BaseModel class, by creating
        an object, then making the program wait 1 second before calling
        the save method from BaseModel and then comparing the created_at
        attr with the updated_at attr to make sure they are different
        '''
        test_obj = BaseModel()
        time_created = test_obj.created_at
        sleep(1)
        test_obj.save()
        time_updated = test_obj.updated_at
        self.assertNotEqual(time_created, time_updated)

    def test_to_dict(self):
        '''Testing the to_dict method by creating a creating an object,
        initializing the attributes to the values I want, creating a
        dictionary that represents that to_dict called on that object
        is supposed to return, and then actually calling the to_dict
        method to see if it matches
        '''
        date = datetime.now()
        test_obj = BaseModel()
        test_obj.id = "1"
        test_obj.created_at = date
        test_obj.updated_at = date
        test_dict = {
                'id': '1',
                '__class__': 'BaseModel',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat(),
                }
        self.assertDictEqual(test_obj.to_dict(), test_dict)

if __name__ == '__main__':
        unittest.main()
