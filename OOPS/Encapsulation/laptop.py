class Laptop:
    def __init__(self):
        self.brand="HP"
        self.__price=120000
    def get_price(self):
        return self.__price
    def set_price(self,updated):
        if(updated<0):
            print("Negative values are not allowed")
        else:
            self.__price+=updated
            print("Total Price is",self.__price)

l=Laptop()
print("Laptop of",l.brand,"costs",l.get_price())

l.set_price(2000)

l.set_price(-900)