# lib/branch_helpers.py

from models.branch import Branch


def branch_menu():
    print("You have reached the branch menu.")
    print("Please select an option: ")
    print("0: Return to previous menu")
    print("1: Display all Branches")
    print("2: NOT YET IMPLEMENTED (displays customers)")
    print("3: NOT YET IMPLEMENTED (displays total money held)")
    print("4: Create a Branch")
    print("5: Delete a Branch")

def branch_cli():
    while True:
        branch_menu()
        branch_command = input("> ")
        if branch_command == "1":
            display_branches()
        elif branch_command == "2":
            display_customers()
        elif branch_command == "3":
            display_total()
        elif branch_command == "4":
            create_branch()
        elif branch_command == "5":
            delete_branch()
        elif branch_command == "0":
            break
        else:
            print("Please enter a valid number command.")

def display_branches():
    print("displaying branches...")
    branches = Branch.get_all()
    for branch in branches:
        print(f"Branch name: {branch.name}, Branch address: {branch.address}")
    input("Press Enter to return to previous menu")

def get_branch_by_name(method):
    while True:
        print("Enter 'cancel' at any time to return to previous menu")
        print("Please enter the branch's name: ")
        branch_name = input("> ")
        if branch_name == "cancel":
            break
        elif (type(branch_name) == str) and (branch_name != ""):
            branch = Branch.find_by_name(branch_name)
            method(branch)
        else:
            print("Branch name must be a non empty string!")

def display_customers():
    print("displaying customers...")

def display_total():
    print("displaying total...")

def create_branch():
    looper = True
    print("creating branch...")
    while looper:
        print("Enter 'cancel' to leave branch creation.")
        print("Please enter the branch name: ")
        name = input("> ")
        if name == "cancel":
            looper = False
        elif Branch.has_name(name):
            print("A branch with that name already exists!")
        elif (type(name) == str) and (name != ""):
            while looper:
                print("Please enter the branch's address: ")
                address = input("> ")
                if address == "cancel":
                    looper = False
                elif Branch.has_address(address):
                    print("A branch with that address already exists!")
                elif (type(address) == str) and (address != ""):
                    Branch.create(name, address)
                    print("New branch has been created.")
                    looper = False
                else:
                    print("Incorrect format. Branch's address must be a non-empty string.")
        else:
            print("Incorrect format. Branch name must be a non-empty string.")

def delete_branch():
    print("deleting branch...")
    while True:
        print("Enter 'cancel' to leave branch creation.")
        print("Enter the name of the branch you want to delete: ")
        name = input("> ")
        if name == "cancel":
            break
        elif (type(name) == str) and Branch.has_name(name):
            Branch.delete_by_name(name)
            print("Branch has been deleted.")
            break
        else:
            print("The name entered does not exist.")
