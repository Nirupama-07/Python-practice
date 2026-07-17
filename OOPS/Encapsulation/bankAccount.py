class BankAccount:
    def __init__(self):
        self.bank="SBI"
        self.__accountNumber=2345671890
        self.__balance=45000
        self.__pin=7564

    def deposit(self,amount):
        if(amount<0):
            print("Amount cannot be negative")
        else:
            self.__balance+=amount
            print(amount,"Amount is credited")
    
    def withdraw(self,amount,pin):
        if(pin==self.__pin):
            if(amount<=self.__balance):
                if(amount<0):
                    print("Amount cannot be in negative")
                else:
                    self.__balance-=amount
                    print(amount,"is debited")
            else:
                print("Amount cannot be negative")
        else:
            print("Incorrect PIN")
    
    def check_balance(self,pin):
        if(pin==self.__pin):
            print("Your total balance is:",self.__balance)
        else:
            print("Invalid PIN")
    
    def change_pin(self,old_pin,new_pin):
        if old_pin != self.__pin:
            print("Incorrect Old PIN")
            return

        if 1000 <= new_pin <= 9999:
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("PIN must be exactly 4 digits.")

bank=BankAccount()
bank.deposit(1000)
bank.withdraw(3000,7564)
bank.check_balance(7564)
bank.change_pin(7564,8970)

print('\n')

bank.deposit(-800)
bank.withdraw(-900,8970)
bank.check_balance(9876)
bank.change_pin(0000,9875)