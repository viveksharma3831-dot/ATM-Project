from display_balance import show_balance
from deposit_money import deposit_money
from withdraw_money import withdraw_money
from statement import show_statement


def atm_menu():
    while True:
        print("\n----- ATM MENU -----")
        print("1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            show_statement()
        elif choice == "5":
            print("Thank you")
            break
        else:
            print("Invalid choice")


atm_menu()
