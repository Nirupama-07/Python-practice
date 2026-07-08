def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Nirupama", age=20, course="CSE", city="Bhubaneswar")