class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

account = BankAccount("BA-1001", 5000, "04-09-2026", "NAZRUL ISLAM NABIL")

account.check_balance()
account.deposit(2000)
account.check_balance()
account.withdraw(1500)
account.check_balance()