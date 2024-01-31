# lib/cli.py

from branch_helpers import branch_cli
from seed import seed_database


def main():
    seed_database()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Goodbye!")
            exit()
        elif choice == "1":
            branch_cli()
        else:
            print("Please select a valid number option")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View Branch menu")


if __name__ == "__main__":
    main()