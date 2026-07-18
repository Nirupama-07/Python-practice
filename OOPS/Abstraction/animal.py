from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog -> Bark")

class Cat(Animal):
    def sound(self):
        print("Cat -> Meow")

class Cow(Animal):
    def sound(self):
        print("Cow -> Moo")

d=Dog()
d.sound()

c=Cat()
c.sound()

cow=Cow()
cow.sound()