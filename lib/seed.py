# lib/seed.py

from models.__init__ import CURSOR, CONN
from models.branch import Branch

def seed_database():
    Branch.drop_table()
    Branch.create_table()

    hoover = Branch.create("Hoover", "1558_Valleydale_Rd")
    homewood = Branch.create("Homewood", "2865_Lakeshore_Dr")
    trussville = Branch.create("Trussville", "8456_Carraway_St")

seed_database()