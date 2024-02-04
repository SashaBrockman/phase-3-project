# Mock Bank CLI Program

    The purpose of this application is to simulate accessing and altering information for both a bank branch
    as well as the customers of the bank through the use of a CLI. Information for the branches and customers 
    in this application are both stored using SQLite in a local database and retrieved by the respective classes.
    The latest version of this program can be found at https://github.com/SashaBrockman/phase-3-project.


## Menus

    Both the Branch and Customer menues are accessed by first going through the main menu rendered by lib/cli.py. This 
    main file is where the project is run from and imports the Branch and Customer menu scripts. The initial 
    commands available to the user are:
    
    0: Exit the program
        Calls exit() to exit the command line interface.

    1: View Branch menu
        Accesses the Branch menu and displays its commands.

    2: View Customer menu
        Accesses the Customer menu and displays its commands.

### Branch Helpers

    lib/branch_helpers.py

    This file is where all of the methods that the user will use to access and alter Branch information are 
    stored. The user can access these methods by entering in the corresponding number for each command which
    are printed directly directly to the command line. These commands are:

    0: Return to the previous menu
        Breaks the while loop that is keeping the user in the Branch menu. User returns to the main menu.

    1: Display all Branches
        Accesses the information for all current branches and displays them to the user. Hitting enter
        afterwards returns the user to the Branch menu.

    2: Display customers for a Branch
        Brings up another input for the user to enter the name of the Branch. From there, it accesses the
        Customers associated with that Branch and prints them to the command line.

    3: Display total held by a Branch
        Brings up another input for the user to enter the name of the Branch. From there, it accesses the
        Customers associated with that Branch, adds their total balances, and displays it on the command
        line.

    4: Create a Branch
        Brings up a series of inputs that requests information from the user in order to create a new 
        Branch. Each input is validated to ensure that a Branch can be created without errors.

    5: Delete a Branch
        Brings up another input for the user to enter the name of the Branch. From there it grabs the Branch
        instance from the table and removes its information from the class "all" variable and table.

    NOTE: For the commands that bring up a new input, typing "cancel" will return the user to the previous
    menu. Also, once an action has completed, the user will be prompted to hit enter to return to the 
    previous menu.

### Customer Helpers

    lib/customer_helpers.py

    This file is where all of the methods that the user will use to access and alter Customer information are 
    stored. The user can access these methods by entering in the corresponding number for each command which
    are printed directly directly to the command line. These commands are:

    0: Return to previous menu
        Breaks the while loop that is keeping the user in the Customer menu. User returns to the main menu.

    1: Display all customers
        Accesses the information for all current Customers and displays them to the user.

    2: Display customer by account number
        Brings up another input for the user to enter the account number for the Customer. From there it 
        grabs the Customer instance from the table and displays it to the user.

    3: Display branch information for a customer
        Brings up another input for the user to enter the account number for the Customer. From there it 
        grabs the Customer information, finds the Branch associated with the account, and displays the
        information.

    4: Adjust customer balance
        Brings up another input for the user to enter the account number for the Customer. It grabs the 
        Customer information and then prompts the user to enter the amount they wish to change the 
        balance by.

    5: Create a customer
        Brings up a series of inputs that requests information from the user in order to create a new 
        Customer. Each input is validated to ensure that a Branch can be created without errors.

    6: Delete a customer
        Brings up another input for the user to enter the account number for the Customer. From there it 
        grabs the Customer instance from the table and removes its information from the class "all" variable 
        and table.

    NOTE: For the commands that bring up a new input, typing "cancel" will return the user to the previous
    menu. Also, once an action has completed, the user will be prompted to hit enter to return to the 
    previous menu.


## Classes

    The Branch and Customer classes are built with methods meant to allow communication with a SQLite database
    in order to store and retrieve information that can be used to build an instance. This allows for information
    to persist between uses of the program. Both classes contain methods to perform the following functions:

    create table (class method)
        Creates a table in the database if one doesn't exist to store information

    drop table (class method)
        Deletes the associated table in the database if it exists

    save (self method)
        Takes the information from an instance and stores it in a table and also stores the instance in the
        classes "all" dictionary.

    delete (self method)
        Removes the information for an instance from the table and "all" dictionary.

    create (class method)
        Combines the creation of an instance and the saving of the information.

    instance from db (class method)
        Takes a row retrieved from the table and:
            updates an instance stored in all if it exists with information from the table OR
            creates and stores in "all" a new instance if it doesn't already exists.

    get all (class method)
        Fetches all stored instances from the table and creates a new instance for each one.

### Branch
    
    lib/models/branch.py

    The Branch class is responsible for getting, setting, and storing all Branch information. This includes:
        
        name and address

    both of which are set up as properties with getters and setters that validate the provided information
    before altering the value. This class also contains a few unique methods. They are:

    find by name (class method)
        Fetches information from the branches table based on the name provided and creates a new instance.

    find by id (class method)
        Fetches information from the branches table based on the id provided and creates a new instance.

    has name (class method)
        Searches the branches table to see if a name exists and returns a corresponding boolean value.

    customers (self method)
        Fetches informtion from the customers table to return one or more instances of Customer that belong 
        to a branch.

### Customer

    lib/models/customer.py

    The Customer class is responsible for getting, setting, and storing all Customer information. This includes:

        name, account_number, balance, and branch_id

    all of which are set up as properties with getters and setters that validate the provided information
    before altering the value. This class also contains a few unique methods. They are:

    find by account number (class method)
        Selects a row from the table by the account number and creates a new instance based on the information 
        retrieved.

    has account number (class method)
        Checks if the customer table has an account number and returns a corresponding boolean value.