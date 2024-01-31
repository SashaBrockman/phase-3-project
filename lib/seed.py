# lib/seed.py

from models.__init__ import CURSOR, CONN
from models.branch import Branch

def seed_database():
    Branch.drop_table()
    Branch.create_table()

    hoover = Branch.create("Hoover", "1558 Valleydale Rd")
    homewood = Branch.create("Homewood", "2865 Lakeshore Dr")
    trussville = Branch.create("Trussville", "8456 Carraway St")