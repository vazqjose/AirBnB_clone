#!/usr/bin/python3
'''unittests for our BaseModel class found in models/base_model.py
'''

import unittest
from time import sleep
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

if __name__ == '__main__':
        unittest.main()
