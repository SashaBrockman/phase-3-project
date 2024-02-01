# lib/customer_helpers.py

from models.customer import Customer

def customer_cli():
    while True:
        customer_menu()
        customer_command = input("> ")
        if customer_command == "0":
            break
        elif customer_command == "1":
            pass
        elif customer_command == "2":
            pass
        elif customer_command == "3":
            pass
        elif customer_command == "4":
            pass
        elif customer_command == "5":
            pass
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