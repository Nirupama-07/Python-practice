from abc import ABC,abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,empName,salary):
        self.empName=empName
        self.salary=salary

    def calculate_salary(self):
        print(f"{self.empName} is a full time employee and has salary of {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self,empName,salary):
        self.empName=empName
        self.salary=salary

    def calculate_salary(self):
        print(f"{self.empName} is a part time employee and has salary of {self.salary}")

fte=FullTimeEmployee("Rahul",50000)
fte.calculate_salary()

pte=PartTimeEmployee("Ritesh",30000)
pte.calculate_salary()