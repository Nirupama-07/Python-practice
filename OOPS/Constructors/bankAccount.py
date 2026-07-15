class BankAccount:

    def __init__(self, name, bank_no, balance):
        self.name = name
        self.bank_no = bank_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    def display_balance(self):
        print(f"Available Balance: ₹{self.balance}")


acc = BankAccount("Rahul", 231453267, 5000)

acc.display_balance()
acc.deposit(300)
acc.display_balance()
acc.withdraw(200)
acc.display_balance()