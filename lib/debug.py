#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.branch import Branch

def debug_database():
    Branch.drop_table()
    Branch.create_table()

    hoover = Branch.create("Hoover", "1558_Valleydale_Rd")
    homewood = Branch.create("Homewood", "2865_Lakeshore_Dr")
    trussville = Branch.create("Trussville", "8456_Carraway_St")

debug_database()

test = Branch.find_by_id(2)

ipdb.set_trace()