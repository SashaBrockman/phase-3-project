# lib/customer_helpers.py

from models.customer import Customer

def customer_cli():
    while True:
        customer_menu()
        customer_command = input("> ")
        if customer_command == "0":
            break
        elif customer_command == "1":
            display_customers()
        elif customer_command == "2":
            display_by_acc_num()
        elif customer_command == "3":
            display_branch()
        elif customer_command == "4":
            create_customer()
        elif customer_command == "5":
            delete_customer()
        else:
            print("Please enter a valid number command.")


def customer_menu():
    print("You have reached the Customer menu.")
    print("Please select an option: ")
    print("0: Return to previous menu")
    print("1: Display all customers")
    print("2: Display customer by account number")
    print("3: Display branch information for a customer")
    print("4: Create a customer")
    print("5: Delete a customer")

def display_customers():
    print("Displaying customers...")

def display_by_acc_num():
    print("Displaying customer by account number...")

def display_branch():
    print("Displaying branch information...")

def create_customer():
    print("Creating customer...")

def delete_customer():
    print("Deleting customer...")