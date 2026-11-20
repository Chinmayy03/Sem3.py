class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Chinmay vasista", 5000)
account.deposit(2000)
account.withdraw(1000)
account.display()
