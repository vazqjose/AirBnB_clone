#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print("Object {} created:".format(my_model.name))
print(my_model)
