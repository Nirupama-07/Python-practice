class Student:
    def __init__(self,studentId,name,course,marks):
        self.studentId=studentId
        self.name=name
        self.course=course
        self.marks=marks
    def display_details(self):
        print("\nStudent Id:",self.studentId)
        print("Name:",self.name)
        print("Course:",self.course)
        print("Marks:",self.marks)

s=Student(101,"Nirupama","CS",78)
s.display_details()