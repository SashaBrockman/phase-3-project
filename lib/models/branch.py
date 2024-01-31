# lib/models/branch.py
from models.__init__ import CURSOR, CONN

class Branch:

    all = {}

    def __init__(self, name, address):
        pass

    @classmethod
    def create(cls, name, address):
        pass

    def delete(self):
        pass

    @classmethod
    def get_all(cls):
        pass
    
    @classmethod
    def instance_from_db(cls, row):
        pass

    def save(self):
        pass

    @classmethod
    def find_by_id(cls, id):
        pass

    @property
    def name(self):
        pass

    @name.setter
    def name(self, name):
        pass

    @property
    def address(self):
        pass

    @address.setter
    def address(self, address):
        pass

    def customers(self):
        pass