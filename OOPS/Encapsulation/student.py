class Student:

    def __init__(self):
        self.name = "Rahul"
        self.__marks = 90

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks Updated")
        else:
            print("Invalid Marks")

s = Student()

print("Marks:", s.get_marks())

s.set_marks(95)
print("Updated Marks:", s.get_marks())

s.set_marks(120)