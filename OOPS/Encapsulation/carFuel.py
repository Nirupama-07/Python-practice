class Car:
    def __init__(self):
        self.__fuel=2000
    
    def addFuel(self,quantity):
        self.__fuel+=quantity
        print("Total fuel quantity is:",self.__fuel)

    def drive(self,distance):
        fuel_used=distance*100
        self.__fuel-=fuel_used
        print("Remaining fuel is",self.__fuel)

c=Car()
c.addFuel(400)
c.drive(20)