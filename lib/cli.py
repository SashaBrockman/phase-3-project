# lib/cli.py

from branch_helpers import (
    exit_program,
    branch_menu
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            branch_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View Branch menu")


if __name__ == "__main__":
    main()