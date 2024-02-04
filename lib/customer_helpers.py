# lib/customer_helpers.py

from models.customer import Customer
from models.branch import Branch

def customer_cli():
    while True:
        customer_menu()
        customer_command = input("> ")
        if customer_command == "0":
            break
        elif customer_command == "1":
            display_customers()
        elif customer_command == "2":
            print("\n ---VIEW CUSTOMER---")
            get_customer_by_acc_num(display_customer)
        elif customer_command == "3":
            print("\n ---VIEW BRANCH---")
            get_customer_by_acc_num(display_branch)
        elif customer_command == "4":
            print("\n ---ADJUST BALANCE---")
            get_customer_by_acc_num(adjust_balance)
        elif customer_command == "5":
            create_customer()
        elif customer_command == "6":
            print("\n ---DELETE CUSTOMER---")
            get_customer_by_acc_num(delete_customer)
        else:
            print("Please enter a valid number command.")


def customer_menu():
    print("\n -----CUSTOMER MENU----- \n")
    print("Please select an option: ")
    print("0: Return to previous menu")
    print("1: Display all customers")
    print("2: Display customer by account number")
    print("3: Display branch information for a customer")
    print("4: Adjust customer balance")
    print("5: Create a customer")
    print("6: Delete a customer")


def display_customers():
    customers = Customer.get_all()
    print("\n ---CURRENT CUSTOMERS--- \n")
    
    for customer in customers:
        display_customer(customer)
    
    input("\nPress enter to return to Customer menu \n")


def get_customer_by_acc_num(method):
    while True:
        print("\nEnter 'cancel' at any time to return to previous menu")
        print("Please enter account number: \n")
        account_number = input("> ")
        
        if account_number == "cancel":
            break

        try:
            customer = Customer.find_by_account_number(int(account_number))
            
            if customer:
                print("\n")
                method(customer)
                input("\nPress enter to return to Customer menu\n")
                break
            
            else:
                print("\nNo customer could be found with that account number.\n")
        
        except ValueError:
            print("\nAccount number must be an integer!\n")


def display_customer(customer):
    branch = Branch.find_by_id(customer.branch_id)
    print(f"Customer name: {customer.name}, Account number: {customer.account_number}, Balance: ${customer.balance: .2f}, Branch: {branch.name}")


def display_branch(customer):
    branch = Branch.find_by_id(customer.branch_id)
    print(f"Customer name: {customer.name}")
    print(f"Branch name: {branch.name}, Branch address: {branch.address}")


def adjust_balance(customer): 
    while True:
        print("Please enter a dollar amount to increase the balance by.")
        print("NOTE: Include '-' before the amount with no space to decrease the balance.\n")
        amount = input("> ")
        
        if amount == "cancel":
            break
        
        try:
            customer.balance += float(amount)
            print(f"\n{customer.name}'s new balance is ${customer.balance: .2f}\n")
            break
        
        except ValueError:
            print("\nAmount must be a float or integer. Please read the note as well.\n")


def create_customer():
    print("\n ---CREATE CUSTOMER--- \n")
    looper = True
    
    while looper:
        print("Enter 'cancel' at any time to leave this menu.")
        print("Please enter the customer's name: \n")
        name = input("> ")
        
        if name == "cancel":
            looper = False
        
        elif (type(name) == str) and (name != ""):
            while looper:
                print("\n Please enter a unique account number: \n")
                account_number = input("> ")
                
                if account_number == "cancel":
                    looper = False
                
                else:
                    try:
                        account_number = int(account_number)
                        
                        if Customer.has_account_number(account_number):
                            print("\nAn account with that number already exists!\n")
                        
                        else:
                            while looper:
                                print("\nPlease enter the name of the customer's branch:\n")
                                branch_name = input("> ")
                                
                                if branch_name == "cancel":
                                    looper = False
                                
                                elif (type(branch_name) == str) and Branch.has_name(branch_name):
                                    branch = Branch.find_by_name(branch_name)
                                    branch_id = branch.id
                                    
                                    while looper:
                                        print("\nPlease enter an initial balance: \n")
                                        balance = input("> ")
                                        
                                        if balance == "cancel":
                                            looper = False
                                        
                                        else:
                                            try:
                                                customer = Customer.create(name, account_number, branch_id, float(balance))
                                                print("\nNew customer has been created.\n")
                                                display_customer(customer)
                                                input("\nPress enter to return to Customer menu.\n")
                                                looper = False
                                            
                                            except ValueError:
                                                print("\nBalance needs to be an integer or float!\n")
                                else:
                                    print("\nBranch name must be a string and an existing branch!\n")
                    except ValueError:
                        print("\nAccount number must be an integer!\n")
        else:
            print("\nName must be a non empty string!\n")


def delete_customer(customer):
    customer.delete()
    print("\nCustomer has been deleted.")