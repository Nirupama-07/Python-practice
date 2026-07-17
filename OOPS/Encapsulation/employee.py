class Employee:
    def __init__(self):
        self.name = "Rahul"
        self.__salary = 90000

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print("Salary Updated Successfully")
        else:
            print("Increase amount must be positive.")

e = Employee()

print("Salary:", e.get_salary())

e.increase_salary(5000)
print("Updated Salary:", e.get_salary())

e.increase_salary(-1000)