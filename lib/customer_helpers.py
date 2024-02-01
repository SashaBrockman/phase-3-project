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
    customers = Customer.get_all()
    for customer in customers:
        print(f"Customer name: {customer.name}, Account number: {customer.account_number}, Balance: ${customer.balance: .2f}, Branch id: {customer.branch_id}")
    input("Press enter to return to Customer menu")

def display_by_acc_num():
    print("Displaying customer by account number...")
    while True:
        print("Enter 'cancel' to return to previous menu")
        print("Please enter account number: ")
        account_number = input("> ")
        if account_number == "cancel":
            break
        try:
            customer = Customer.find_by_account_number(int(account_number))
            if customer:
                print(f"Customer name: {customer.name}, Account number: {customer.account_number}, Balance: ${customer.balance: .2f}, Branch id: {customer.branch_id}")
                input("Press enter to return to Customer menu")
                break
            else:
                print("No customer could be found with that account number.")
        except ValueError:
            print("Account number must be an integer!")

def display_branch():
    print("Displaying branch information...")

def create_customer():
    print("Creating customer...")

def delete_customer():
    print("Deleting customer...")