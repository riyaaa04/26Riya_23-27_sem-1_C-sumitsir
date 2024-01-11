#Build a simulation of an ATM system with classes for accounts, transactions, andusers. Implement methods for withdrawing cash, checking balances, and handlingPIN verification
class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class Transaction:
    @staticmethod
    def display_menu():
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Exit")

    @staticmethod
    def process_transaction(account):
        while True:
            Transaction.display_menu()
            choice = input("Enter choice (1-3): ")

            if choice == '1':
                print(f"Current Balance: ${account.check_balance()}")
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: $"))
                if account.withdraw_cash(amount):
                    print(f"Withdrawal successful. New Balance: ${account.check_balance()}")
                else:
                    print("Invalid amount or insufficient funds.")
            elif choice == '3':
                print("Exiting transaction.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account

# Example usage:
account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")
initial_balance = float(input("Enter your initial balance: $"))

user_account = Account(account_number, pin, initial_balance)
user = User("John Doe", user_account)

print(f"Welcome, {user.name}!")
entered_pin = input("Enter your PIN to verify: ")

if user.account.check_pin(entered_pin):
    Transaction.process_transaction(user.account)
else:
    print("Invalid PIN. Exiting.")
