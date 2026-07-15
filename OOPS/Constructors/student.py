class Student:
    def __init__(self,name,age):
        print("Object created successfully")
        self.name=name
        self.age=age


s=Student("Rahul",18)
print(s.name)
print(s.age)