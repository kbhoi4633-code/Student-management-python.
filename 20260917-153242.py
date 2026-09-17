class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print("Amount credited:", amount)

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount debited:", amount)
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Account holder:", self.name)
        print("Current balance:", self.balance)


# Creating an object
account = BankAccount("Komal", 1000)

# Credit amount
account.credit(500)

# Debit amount
account.debit(200)

# Display balance
account.show_balance()