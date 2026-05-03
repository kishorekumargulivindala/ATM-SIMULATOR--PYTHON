import json
import os

FILE_NAME = "balance.json"

# Load balance from file
def load_balance():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    else:
        return 1000   # default balance

# Save balance to file
def save_balance(balance):
    with open(FILE_NAME, "w") as file:
        json.dump(balance, file)

# Main program
balance = load_balance()

while True:
    print("\n===== ATM MENU =====")
    print("1. Balance Check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        save_balance(balance)
        print("Thank you! Visit Again")
        break

    else:
        print("Invalid Choice")