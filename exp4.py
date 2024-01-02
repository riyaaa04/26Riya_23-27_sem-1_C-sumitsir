#Write a Python program to create a class representing a bank. Include methods formanaging customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created successfully.")
        else:
            print(f"Account {account_number} already exists.")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Account {account_number} balance: ${balance}")
        else:
            print(f"Account {account_number} does not exist.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount} into account {account_number}.")
            self.display_balance(account_number)
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew ${amount} from account {account_number}.")
                self.display_balance(account_number)
            else:
                print("Insufficient funds.")
        else:
            print(f"Account {account_number} does not exist.")

# Example usage with user input:
bank = Bank()

while True:
    print("\nBank Menu:")
    print("1. Create Account")
    print("2. Display Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        account_number = input("Enter account number: ")
        bank.create_account(account_number)

    elif choice == '2':
        account_number = input("Enter account number: ")
        bank.display_balance(account_number)

    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_number, amount)

    elif choice == '4':
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(account_number, amount)

    elif choice == '5':
        print("Exiting the bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")