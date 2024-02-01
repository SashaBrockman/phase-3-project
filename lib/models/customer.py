# lib/models/customer.py
from models.__init__ import CONN, CURSOR

class Customer:

    all = {}

    def __init__(self, name, account_number, balance = 0, branch_id):
        self.id = None
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.branch_id = branch_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (name != ""):
            self._name = name
        else:
            raise ValueError("Name must be a non empty string.")

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        if (type(account_number) = int) and (len(account_number) != 0):
            self._account_number = account_number
        else:
            raise ValueError("Account number must be a non empty integer")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if (type(balance) = float) and (len(balance) != 0):
            self._balance = balance
        else:
            raise ValueError("Balance must be a non empty float")

    @property
    def branch_id(self):
        return self._branch_id

    @branch_id.setter
    def branch_id(self, id):
        if (type(branch_id) = int) and (len(branch_id) != 0):
            self._branch_id = branch_id
        else:
            raise ValueError("Branch id must be a non empty integer")

    @classmethod
    def create_table(cls):
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
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, account_number, balance = 0, branch_id):
        customer = cls(name, account_number, balance, branch_id)
        customer.save()
        return customer

    def delete(self):
        sql = """
            DELETE FROM customers
            WHERE id = (?)
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def delete_by_account_number(cls, account_number):
        pass

    @classmethod
    def get_all(cls):
        pass
    
    @classmethod
    def instance_from_db(cls, row):
        pass

    def save(self):
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
        pass

    @classmethod
    def has_account_number(cls, account_number):
        pass

    def add_to_balance(self, amount):
        pass

    def branch(self):
        pass