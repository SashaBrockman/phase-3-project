# lib/models/customer.py
from __init__ import CONN, CURSOR

class Customer:

    all = {}

    def __init__(self, name, account_number, balance = 0):
        pass

    @classmethod
    def create(cls, name, account_number, balance = 0):
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
    def account_number(self):
        pass

    @account_number.setter
    def account_number(self, account_number):
        pass

    @property
    def balance(self):
        pass

    @balance.setter
    def balance(self):
        pass

    @property
    def branch_id(self):
        pass

    @branch_id.setter
    def branch_id(self, id):
        pass

    def branch(self):
        pass