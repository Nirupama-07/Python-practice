from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class creditCard(Payment):
    def pay(self,amount):
        print(amount,"paid using credit card")

class debitCard(Payment):
    def pay(self,amount):
        print(amount,"paid using debit card")

class upi(Payment):
    def pay(self,amount):
        print(amount,"paid using upi")

cc=creditCard()
cc.pay(1000)

dc=debitCard()
dc.pay(1000)

up=upi()
up.pay(1000)