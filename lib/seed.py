# lib/seed.py

from models.__init__ import CURSOR, CONN
from models.branch import Branch
from models.customer import Customer

def seed_database():
    Branch.drop_table()
    Branch.create_table()
    Customer.drop_table()
    Customer.create_table()


    hoover = Branch.create("Hoover", "1558 Valleydale Rd")
    homewood = Branch.create("Homewood", "2865 Lakeshore Dr")
    trussville = Branch.create("Trussville", "8456 Carraway St")

    megan = Customer.create("Megan", 1, 1)
    greg = Customer.create("Greg", 2, 1, 12500.00)
    matthew = Customer.create("Matthew", 3, 2)
    sarah = Customer.create("Sarah", 4, 2)
    lucas = Customer.create("Lucas", 5, 3)
    ashley = Customer.create("Ashley", 6, 3, 100.00)
