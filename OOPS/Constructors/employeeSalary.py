class Employee:
    def __init__(self, employeeId, employeeName, basicSalary):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.basicSalary = basicSalary

    def calculate_bonus(self):
        if self.basicSalary >= 50000:
            bonus = self.basicSalary * 20 / 100
        else:
            bonus = self.basicSalary * 10 / 100

        return bonus

    def display_employee(self):
        bonus = self.calculate_bonus()
        total = self.basicSalary + bonus

        print("Employee ID:", self.employeeId)
        print("Employee Name:", self.employeeName)
        print("Basic Salary:", self.basicSalary)
        print("Bonus:", bonus)
        print("Total Salary:", total)


e = Employee(101, "Bidyit", 60000)
e.display_employee()