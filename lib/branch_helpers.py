# lib/branch_helpers.py

from models.branch import Branch
from customer_helpers import display_customer

def branch_menu():
    print("\n -----BRANCH MENU----- \n")
    print("Please select an option: \n")
    print("0: Return to previous menu")
    print("1: Display all Branches")
    print("2: Display customers for a Branch")
    print("3: Display total held by a Branch")
    print("4: Create a Branch")
    print("5: Delete a Branch")


def branch_cli():
    while True:
        branch_menu()
        branch_command = input("> ")
        if branch_command == "1":
            display_branches()
        elif branch_command == "2":
            print("\n ---CUSTOMERS---")
            get_branch_by_name(display_customers)
        elif branch_command == "3":
            print("\n ---TOTAL HELD---")
            get_branch_by_name(display_total)
        elif branch_command == "4":
            create_branch()
        elif branch_command == "5":
            get_branch_by_name(delete_branch)
        elif branch_command == "0":
            break
        else:
            print("Please enter a valid number command.")


def display_branches():
    print("\n ---CURRENT BRANCHES--- \n")
    branches = Branch.get_all()
    
    for branch in branches:
        print(f"Branch name: {branch.name}, Branch address: {branch.address}")
    
    input("\nPress Enter to return to previous menu \n")


def get_branch_by_name(method):
    while True:
        print("\nEnter 'cancel' at any time to return to previous menu")
        print("Please enter the branch's name: \n")
        branch_name = input("> ")
        
        if branch_name == "cancel":
            break
        
        elif (type(branch_name) == str) and (branch_name != ""):
            branch = Branch.find_by_name(branch_name)
            
            if branch:
                print("/n")
                method(branch)
                input("\nPress enter to return to Branch menu. \n")
                break
            
            else:
                print("\nThere is no branch with that name! \n")
        else:
            print("\nBranch name must be a non empty string! \n")

def display_customers(branch):
    customers = branch.customers()
    
    for customer in customers:
        display_customer(customer)


def display_total(branch):
    total = 0.0
    customers = branch.customers()
    
    for customer in customers:
        total += customer.balance
    
    print(f"\nThe total held by this bank is ${total: .2f}.")


def create_branch():
    looper = True
    print("\n ---CREATE BRANCH--- \n")
    
    while looper:
        print("Enter 'cancel' to leave branch creation.")
        print("Please enter the branch name: \n")
        name = input("> ")
        
        if name == "cancel":
            looper = False
        
        elif (type(name) == str) and (Branch.has_name(name)):
            print("\nA branch with that name already exists! \n")
        
        elif (type(name) == str) and (name != ""):
            while looper:
                print("\nPlease enter the branch's address: \n")
                address = input("> ")
                
                if address == "cancel":
                    looper = False
                
                elif Branch.has_address(address):
                    print("\nA branch with that address already exists! \n")
                
                elif (type(address) == str) and (address != ""):
                    Branch.create(name, address)
                    print("\nNew branch has been created.")
                    looper = False
                
                else:
                    print("\nIncorrect format. Branch's address must be a non-empty string. \n")
        else:
            print("\nIncorrect format. Branch name must be a non-empty string. \n")


def delete_branch(branch):
    branch.delete()
    print("\nBranch has been deleted.")
