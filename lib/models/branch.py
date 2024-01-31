# lib/models/branch.py
from models.__init__ import CURSOR, CONN

class Branch:

    all = {}

    def __init__(self, name, address, id = None):
        self.id = id
        self.name = name
        self.address = address

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS branches(
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, address):
        new_branch = cls(name, address)
        new_branch.save()
        return new_branch

    def delete(self):
        sql = """
            DELETE FROM branches
            WHERE id = (?)
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

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