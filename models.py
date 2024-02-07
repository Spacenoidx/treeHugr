import random
from peewee import *

db = SqliteDatabase('tree-Hugr.db')

class Tree(Model):
    species = CharField()
    diameter = FloatField()

    class Meta:
        database = db




db.connect()
db.create_tables([Tree])  # Ensure table creation
print(Tree._meta.fields)
db.close()


test = Tree.create(species="Oak", diameter=10.0)