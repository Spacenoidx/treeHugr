import random
import datetime
from peewee import *

db = SqliteDatabase('tree-Hugr.db')

class BaseModel(Model):
    class Meta:
        database = db

class Tree(BaseModel):
    species = CharField()
    diameter = FloatField()
    postdate = TextField(default=datetime.date.today)
    activity = TextField()
    photo = BlobField()
