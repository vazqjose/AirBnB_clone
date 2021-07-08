#!/usr/bin/python3
'''unittests for our BaseModel class found in models/base_model.py
'''

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    '''unittests for our BaseModel class, testing:
    __init__, __str__, to_dict, and the save methods from the class.
    '''
    def test_save(self):
        '''Testing the save method from BaseModel class'''
        test_obj = BaseModel()
        time_created = test_obj.created_at
        sleep(1)
        test_obj.save()
        time_updated = test_obj.updated_at
        self.assertNotEqual(time_created, time_updated)

if __name__ == '__main__':
        unittest.main()
