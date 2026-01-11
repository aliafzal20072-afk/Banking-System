# Base Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        print(f"\nDepositing {amount}...")
        self.balance += amount
        print("Deposit successful.")

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")


# Child Class
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"\nWithdrawing {amount}...")
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance. Withdrawal failed.")


# --------- Main Program -----------
name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

account = SavingsAccount(name, balance)


account.deposit(2000)
account.withdraw(3000)
account.show_balance()




