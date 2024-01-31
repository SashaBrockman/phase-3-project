# lib/branch_helpers.py

from models.branch import Branch

#TOP LEVEL HELPERS#

def branch_menu():
    print("You have reached the branch menu.")
    print("Please select an option: ")
    print("1: Display all Branches")
    print("2: NOT YET IMPLEMENTED (displays customers)")
    print("3: NOT YET IMPLEMENTED (displays total money held)")
    print("4: Create a Branch")
    print("5: Delete a Branch")
    print("0: Return to previous menu")

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

#TIER ONE HELPERS#

def display_branches():
    print("displaying branches...")
    while True:
        branches = Branch.get_all()
        for branch in branches:
            print_branch(branch)
        input("Press Enter to return to previous menu")
        break

def display_customers():
    print("displaying customers...")

def display_total():
    print("displaying total...")

def create_branch():
    print("creating branch...")

def delete_branch():
    print("deleting branch...")

#TIER TWO HELPERS#

def print_branch(branch):
    print(f"Branch name: {branch.name}, Branch address: {branch.address}")