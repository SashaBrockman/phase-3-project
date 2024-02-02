# lib/models/branch.py
from models.__init__ import CURSOR, CONN

class Branch:

    all = {}

    def __init__(self, name, address, id = None):
        self.id = id
        self.name = name
        self.address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (name != ""):
            self._name = name
        else:
            raise ValueError("Branch name must be a non-empty string")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if (type(address) == str) and (address != ""):
            self._address = address
        else:
            raise ValueError("Address must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS branches (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS branches;
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

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM branches
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
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
        sql = """
            INSERT INTO branches (name, address)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.address))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM branches
            WHERE name = (?)
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM branches
            WHERE id = (?)
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def has_name(cls, name):
        sql = """
            SELECT * FROM branches
            WHERE name = (?)
        """

        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return True
        else:
            return False
    
    @classmethod
    def has_address(cls, address):
        sql = """
            SELECT * FROM branches
            WHERE address = (?)
        """

        row = CURSOR.execute(sql, (address,)).fetchone()

        if row:
            return True
        else:
            return False

    def customers(self):
        from models.customer import Customer

        sql = """
            SELECT * FROM customers
            WHERE branch_id = (?)
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Customer.instance_from_db(row) for row in rows if rows]