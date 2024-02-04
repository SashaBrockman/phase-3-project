# lib/cli.py

from branch_helpers import branch_cli
from customer_helpers import customer_cli
from seed import seed_database


def main():
    seed_database()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("\n Goodbye! \n")
            exit()
        elif choice == "1":
            branch_cli()
        elif choice == "2":
            customer_cli()
        else:
            print("\n Please select a valid number option. \n")


def menu():
    print("\n -----WELCOME----- \n")
    print("Please select an option: \n")
    print("0: Exit the program")
    print("1: View Branch menu")
    print("2: View Customer menu")


if __name__ == "__main__":
    main()