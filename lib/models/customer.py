# lib/models/customer.py
from models.__init__ import CONN, CURSOR
from models.branch import Branch

class Customer:

    all = {}

    def __init__(self, name, account_number, branch_id, balance = 0.00):
        self.id = None
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.branch_id = branch_id

    @property
    def name(self):
        """Getter method for the customer name."""
        return self._name

    @name.setter
    def name(self, name):
        """Setter method for the customer name. Verfies that it is a non empty string."""
        if (type(name) == str) and (name != ""):
            self._name = name
        else:
            raise ValueError("Name must be a non empty string.")

    @property
    def account_number(self):
        """Getter method for the customer's account number."""
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Setter method for the customer's account number. Verifies that the number is an integer."""
        if (type(account_number) == int):
            self._account_number = account_number
        else:
            raise ValueError("Account number must be an integer")

    @property
    def balance(self):
        """Getter method for the customer's balance."""
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Setter method for the customer's balance.  Verifies that the balance is a float."""
        if (type(balance) == float):
            self._balance = balance
        else:
            raise ValueError("Balance must be a float")

    @property
    def branch_id(self):
        """Getter method for the customer's branch id."""
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Setter method for the customer's branch id. Verifies that it is an integer and 
            a branch with that id already exists."""
        if (type(branch_id) == int) and Branch.find_by_id(branch_id):
            self._branch_id = branch_id
        else:
            raise ValueError("Branch id must be an integer and from existing branch")

    @classmethod
    def create_table(cls):
        """Creates a new customers table if one does not already exist."""
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                account_number INTEGER,
                balance REAL,
                branch_id INTEGER,
                FOREIGN KEY (branch_id) REFERENCES branches(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Deletes the customers table if it exists."""
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, account_number, branch_id, balance = 0.00):
        """Creates a new instance of Customer and saves it."""
        customer = cls(name, account_number, branch_id, balance)
        customer.save()
        return customer

    def delete(self):
        """Deletes a customer's information from the table and removes the instance from all."""
        sql = """
            DELETE FROM customers
            WHERE id = (?)
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        """Fetches all customer information in the table and creates a new instance for each."""
        sql = """
            SELECT * FROM customers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def instance_from_db(cls, row):
        """Takes a row retrieved from customers and:
            updates an existing instance with the information OR
            creates and saves a new instance of customer in all"""
        customer = cls.all.get(row[0])
        if customer:
            customer.name = row[1]
            customer.account_number = row[2]
            customer.balance = row[3]
            customer.branch_id = row[4]
        else:
            customer = cls(row[1], row[2], row[4], row[3])
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer

    def save(self):
        """Inserts a customer's information into the table and adds the instance to all."""
        sql = """
            INSERT INTO customers 
            (name, account_number, balance, branch_id)
            VALUES
            (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.account_number, self.balance, self.branch_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def find_by_account_number(cls, account_number):
        """Selects a row from the table by the account number and creates a new instance
            based on the information retrieved."""
        sql = """
            SELECT * FROM customers
            WHERE account_number = (?)
        """

        row = CURSOR.execute(sql, (account_number,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def has_account_number(cls, account_number):
        """Checks if the customer table has an account number and returns a corresponding boolean value."""
        sql = """
            SELECT * FROM customers
            WHERE account_number = (?)
        """

        row = CURSOR.execute(sql, (account_number,)).fetchone()

        if row:
            return True
        else:
            return False
