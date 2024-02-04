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
        """Getter method for the Branch name."""
        return self._name

    @name.setter
    def name(self, name):
        """Setter method for the Branch name. Verifies that name is a non empty string."""
        if (type(name) == str) and (name != ""):
            self._name = name
        else:
            raise ValueError("Branch name must be a non-empty string")

    @property
    def address(self):
        """Getter method for the Branch address"""
        return self._address

    @address.setter
    def address(self, address):
        """Getter method for the Branch address. Verifies that the address is a non empty string."""
        if (type(address) == str) and (address != ""):
            self._address = address
        else:
            raise ValueError("Address must be a non-empty string")

    @classmethod
    def create_table(cls):
        """Creates a table to store Branch information is one doesn't already exist."""
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
        """Deletes the branches table if it exists."""
        sql = """
            DROP TABLE IF EXISTS branches;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, address):
        """Creates and saves a new instance of the Branch class."""
        new_branch = cls(name, address)
        new_branch.save()
        return new_branch

    def delete(self):
        """Deletes Branch instance information from both the table and the all variable."""
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
        """Fetches all stored branch instances from the table and creates a new instance for each one."""
        sql = """
            SELECT * FROM branches
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def instance_from_db(cls, row):
        """Takes a row retrieved from the branch table and:
            updates an instance stored in all if it exists with information from the table OR
            creates and stores a new Branch instance if it doesn't already exists.
        """
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
        """Inserts a Branch instance's information into the table and stores the instance in all."""
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
        """Fetches information from the branches table based on the name provided and creates a new instance."""
        sql = """
            SELECT * FROM branches
            WHERE name = (?)
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, id):
        """Fetches information from the branches table based on the id provided and creates a new instance."""
        sql = """
            SELECT * FROM branches
            WHERE id = (?)
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def has_name(cls, name):
        """Searches the branches table to see if a name exists and returns a corresponding boolean value."""
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
        """Searches the branches table to see if an address exists and returns a corresponding boolean value."""
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
        """Fetches informtion from the customers table to return one or more instances of Customer that belong to a branch."""
        from models.customer import Customer

        sql = """
            SELECT * FROM customers
            WHERE branch_id = (?)
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Customer.instance_from_db(row) for row in rows if rows]