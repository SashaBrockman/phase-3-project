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
            get_customer_by_acc_num(display_customer)
        elif customer_command == "3":
            get_customer_by_acc_num(display_branch)
        elif customer_command == "4":
            get_customer_by_acc_num(adjust_balance)
        elif customer_command == "5":
            create_customer()
        elif customer_command == "6":
            delete_customer
        else:
            print("Please enter a valid number command.")


def customer_menu():
    print("You have reached the Customer menu.")
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
    for customer in customers:
        print(f"Customer name: {customer.name}, Account number: {customer.account_number}, Balance: ${customer.balance: .2f}, Branch id: {customer.branch_id}")
    input("Press enter to return to Customer menu")

def get_customer_by_acc_num(method):
    while True:
        print("Enter 'cancel' to return to previous menu")
        print("Please enter account number: ")
        account_number = input("> ")
        if account_number == "cancel":
            break
        try:
            customer = Customer.find_by_account_number(int(account_number))
            if customer:
                method(customer)
                input("Press enter to return to Customer menu")
                break
            else:
                print("No customer could be found with that account number.")
        except ValueError:
            print("Account number must be an integer!")

def display_customer(customer):
    print(f"Customer name: {customer.name}, Account number: {customer.account_number}, Balance: ${customer.balance: .2f}, Branch id: {customer.branch_id}")

def display_branch(customer):
    branch = Branch.find_by_id(customer.branch_id)
    print(f"Customer name: {customer.name}")
    print(f"Branch name: {branch.name}, Branch address: {branch.address}")

def adjust_balance(customer):
    while True:
        print("Please enter a dollar amount to increase the balance by.")
        print("NOTE: Include '-' before the amount with no space to decrease the balance.")
        amount = input("> ")
        try:
            customer.balance += float(amount)
            print(f"{customer.name}'s new balance is ${customer.balance: .2f}")
            break
        except ValueError:
            print("Amount must be a float or integer. Please read the note as well.")

def create_customer():
    print("Creating customer...")

def delete_customer():
    print("Deleting customer...")