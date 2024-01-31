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
        sql = """
            SELECT * FROM branches
        """
        rows = CURSOR.execute(sql).fetchall()
        return [instance_from_db(row) for row in rows]
    
    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.name = row[1]
            department.address = row[2]
        else:
            department = cls(name = row[1], address = row[2])
            department.id = row[0]
            cls.all[department.id] = department
        return department 

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