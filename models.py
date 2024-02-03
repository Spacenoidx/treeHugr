import random
from peewee import *

db = SqliteDatabase('tree-Hugr.db')

class Tree(Model):

    class Meta:
        database = db

    id_num = AutoField()
    species = CharField()
    diameter = FloatField()
