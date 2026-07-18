from abc import ABC,abstractmethod

class Vehcile(ABC):
    
    @abstractmethod
    def start(self):
        pass

class Car(Vehcile):
    def start(self):
        print("Car started")

class Bike(Vehcile):
    def start(self):
        print("Bike started")

class Bus(Vehcile):
    def start(self):
        print("Bus started")

c=Car()
c.start()

bike=Bike()
bike.start()

bus=Bus()
bus.start()