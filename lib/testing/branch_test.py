from models.__init__ import CONN, CURSOR
from models.branch import Branch
import pytest

class TestBranch:

    @pytest.fixture(autouse=True)
    def drop_table(self):
        """Drops branch table prior to each test"""
        
        CURSOR.execute("DROP TABLE IF EXISTS branches")

        Branch.all = {}

    def test_create_table(self):
        """Tests the creation of a table"""

        Branch.create_table()

        assert(CURSOR.execute("SELECT * FROM branches"))

    def test_drop_table(self):
        """Tests the deletion of a table"""

        sql = """
            CREATE TABLE IF NOT EXISTS branches (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

        Branch.drop_table()

        sql_table_names = """
            SELECT * FROM sqlite_master
            WHERE type = 'table' AND name = 'branches'
        """

        result = CURSOR.execute(sql_table_names).fetchone()
        assert(result is None)

    def test_save(self):
        """Tests the functionality of the save method"""
        branch = Branch("Hoover", "1234 Downing St")
        Branch.create_table()

        branch.save()

        sql = """
            SELECT * FROM branches
        """

        result = CURSOR.execute(sql).fetchone()

        assert((result[0], result[1], result[2]) == 
                (branch.id, "Hoover", "1234 Downing St") == 
                (result[0], branch.name, branch.address))

    def test_create(self):
        """Tests the creation of a Branch instance and row in table using .create"""
        Branch.create_table()
        branch = Branch.create("Hoover", "1234 Downing St")

        sql = """
            SELECT * FROM branches
        """

        result = CURSOR.execute(sql).fetchone()

        assert((result[0], result[1], result[2]) == 
                (branch.id, "Hoover", "1234 Downing St") == 
                (result[0], branch.name, branch.address))
