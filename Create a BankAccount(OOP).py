class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

account1 = BankAccount("54321", "Bob", 1000)
account1.deposit(500)
account1.withdraw(200)
print(f"Balance: {account1.balance}")
account1.withdraw(2000)